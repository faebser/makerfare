import markdown2 as markdown
from bs4 import BeautifulSoup as soup
from os import path, walk, remove
from shutil import copytree
import logging as log
from copy import copy

content = path.abspath("content")
templatePath = None
targetDir = None
targetHtmlFile = None
blockTemplate = "<div class='block'></div>"
articleTemplate = "<article class='clearfix'><h1></h1></article>"
menuElementTemplate = "<li><a></a></li>"
workshopMailTemplate = "<a class='course' href='mailto:contact@makershop.in'>Anmelden</a>"
workshopIntroTemplate = "<div class='intro clearfix'></div>"

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

print contentSection

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
		article.h1.string = nameForArticle
		log.info("htmlId: " + htmlId)
		#print article
		for filename in files:
			if not filename.startswith(".") and filename.endswith(".md"):
				f = open(path.join(paths, filename))
				htmlContent = soup(markdown.markdown(file.read(f)), "html.parser")
				if htmlId == "anfahrt":
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
						p2 = pList[1].extract()
						p.name = "div"
						p['class'] = "smallInfoBox"
						intro.append(p)
						intro.append(p2)
						htmlContent.insert(1, intro)
						block.append(htmlContent)
						block.append(soup(workshopMailTemplate, "html.parser"))
						article.append(block)
					elif filename == 'intro.md':
						article.insert(1, htmlContent)
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