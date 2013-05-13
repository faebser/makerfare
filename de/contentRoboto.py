import markdown2 as markdown
from bs4 import BeautifulSoup as soup
from os import path, walk, remove
from shutil import copytree
import logging as log

def addMenuItem(nameInLowercase):
	menuItem = soup(menuElementTemplate, "html.parser")
	a = menuItem.a
	a['href'] = "#" + nameInLowercase
	a.string = nameInLowercase.capitalize();
	menuContainer.append(menuItem)

content = path.abspath("content")
templatePath = None
targetDir = None
targetHtmlFile = None
menuContainer = None
blockTemplate = "<div class='block'></div>"
articleTemplate = "<article class='clearfix'></article>"
menuElementTemplate = "<li><a></a></li>"
workshopMailTemplate = "<a class='course' href='mailto:contact@makershop.in'>Anmelden</a>"
workshopIntroTemplate = "<div class='intro clearfix'></div>"
menuItemList = ['programm', 'projekt', 'workshops', 'anfahrt']

log.basicConfig(format='%(levelname)s: %(message)s', level=log.DEBUG)

log.info("--------- checking paths & init ---------")
if path.exists(path.abspath("template")):
	templatePath = path.abspath("template")
else:
	log.error("templatePath not found, exiting")
	exit()

if path.exists(path.abspath("content")):
	content = path.abspath("content")
else:
	log.error("content not found, exiting")
	exit()

if path.exists(path.abspath("website")):
	log.error("please remove website directory, exiting")
	exit()
else:
	targetDir = path.abspath("website")
	copytree(templatePath, targetDir)
	log.info("copying all files")
	remove(path.join(targetDir, "index.html"))

log.info("templatePath => " + templatePath) 
log.info("Path for website folder => " + targetDir) 

log.info("parsing index.html")

targetHtmlFile = soup(open(path.join(templatePath, "index.html")), "html.parser")

contentSection = targetHtmlFile.find_all(id = "content")[0]
menuContainer = targetHtmlFile.find_all(id = "menuContainer")[0].ul

log.info("gathering content")

for paths, directories, files in walk(content):
	#log.info("paths: %s", paths)
	#log.info("directories %s", directories)
	#log.info("files: %s", files)

	nameForArticle = paths.split("_")
	if len(nameForArticle) > 1:
		nameForArticle = nameForArticle[1]
		htmlId = nameForArticle
		nameForArticle = nameForArticle.capitalize()
		log.info("working on " + nameForArticle)
		article = soup(articleTemplate, "html.parser").article
		article['id'] = htmlId
		#fix sorting
		if htmlId == 'programm' or htmlId == 'workshops':
			files.sort()
		for filename in files:
			if not filename.startswith(".") and filename.endswith(".md"):
				f = open(path.join(paths, filename))
				htmlContent = soup(markdown.markdown(file.read(f)), "html.parser")
				if filename == 'intro.md':
					log.info("found intro, adding that")
					article.insert(0, htmlContent)
					if htmlId in menuItemList:
						addMenuItem(htmlContent.h1.string.lower())
				elif htmlId == "anfahrt":
					log.info("special content: anfahrt")
					block = soup(blockTemplate, "html.parser").div
					block.append(htmlContent)
					block['class'].append("simple")
					article.append(block)
				elif htmlId == "workshops":
					log.info("special content: workshops")
					if  not filename == 'intro.md':
						block = soup(blockTemplate, "html.parser").div
						intro = soup(workshopIntroTemplate, "html.parser").div
						pList = htmlContent.find_all("p")
						p = pList[0].extract()
						smallInfoBox = soup("<div class='smallInfoBox'></div>", "html.parser").div
						for a in p.find_all("a"):
							a.extract();
							newP = soup("<p></p>").p
							newP.append(a)
							smallInfoBox.append(newP)
						for item in p.contents:
							for line in item.string.splitlines():
								if len(line) > 0:
									newP = soup("<p></p>").p
									newP.string = line
									smallInfoBox.append(newP)
						intro.append(smallInfoBox)
						p2 = pList[1].extract()
						intro.append(p2)
						htmlContent.insert(1, intro)
						block.append(htmlContent)
						block.append(soup(workshopMailTemplate, "html.parser"))
						article.append(block)
				elif htmlId == 'projekt':
					log.info("special content: projekt")
					article.append(htmlContent)
				else :
					log.info("no special content found, simply adding blocks")
					block = soup(blockTemplate, "html.parser").div
					block.append(htmlContent)
					article.append(block)

		contentSection.append(article)

targetFile = open(path.join(targetDir, "index.html"), "w")
targetFile.write(str(targetHtmlFile))
targetFile.close()