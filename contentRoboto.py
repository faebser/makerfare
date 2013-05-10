import markdown2 as markdown
from bs4 import BeautifulSoup as soup
from os import path, walk, remove
from shutil import copytree
import logging as log

content = path.abspath("content")
templatePath = None
targetDir = None

log.basicConfig(format='%(levelname)s:%(message)s', level=log.DEBUG)

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

print("templatePath => ") + templatePath
print("Path for website folder => ") + targetDir

log.info("gathering content")

for paths, directories, files in walk(content):
	log.info("paths: %s", paths)
	log.info("directories %s", directories)
	log.info("files: %s", files)