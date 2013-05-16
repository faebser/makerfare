# Manual

## Installation Python-Modules

In die Konsole/Terminal wechseln.

* [Pip](https://pypi.python.org/pypi/pip) -> ``` sudo easy_install pip ```
* [Markdown2](https://github.com/trentm/python-markdown2) -> ``` sudo pip install markdown2 ```
* [BeautifulSoup](http://www.crummy.com/software/BeautifulSoup/bs4/doc/) -> ``` sudo pip install beautifulsoup4 ```

## Content

Der Content für die Website befindet sich unter ```/de/content``` und ```/fr/content/``` aufgeteilt in Abschnitte (z.B. ```/de/content/01_projekt```). Das Skript verarbeitet diese Abschnitte von 01 ausgehend.
Der Inhalt dieser Abschnitte ist in [Markdown](http://daringfireball.net/projects/markdown/syntax) verfasst.
In jedem Ordner muss sich eine Datei ```intro.md``` befinden, sie enthält den Titel des Abschnitts und falls gewünscht einen Einführungstext.

### 01_projekt
Der Markdown-Text dieses Abschnittes wird als einfacher Fliesstext eingefügt.

### 02_programm
Für jede Datei wird ein Block von der halben Inhalts-Breite erstellt. Der Inhalt ist als [Liste](http://daringfireball.net/projects/markdown/syntax#list) erfasst. Um Text linksbünding  und fett zu machen in das HTML-Tag ```<span>Text</span>``` verpacken.

### 03_workshops
Wie beim Programm wird für jede Datei ein Block erzeugt. Der erste Fliesstext-Abschnitt wird in die kleine Info-Box verschoben, der folgenden Abschnitt grösser als Einführungstext genutzt.

### 04_anfahrt
Die Karte befindet sich in der Datei ```intro.md```. Um sie zu aktualiseren kann man den Link hinter dem Argument ```src``` austauschen.

### 05_partner
Die Partner sind ein Spezialfall aufgrund der gewünschten Formatierung. Die Datei ```intro.md``` enthält in diesem Fall reinen HTML-Code. Dieser kann direkt verändert werden. Um ein Link zu einer externen Website hinzuzufügen muss die Linie von    
```
			<li class="row1" id="motoco"><img src="img/logos/motoco.jpg"/></li>
```       
zu      
```
<li class="row1" id="motoco"><a href="htttp://www.google.ch"><img src="img/logos/motoco.jpg"/></a></li>
```    
angepasst werden.

### Bilder
Bilder können folgendermassen eingefügt werden:     
```
      <img src="img/panorama1bearb.jpg" class="full">
```   
Die class ist entwerder ```right``` für rechtsbündig, ```links``` für links oder ```full``` für die ganze Breite.
Die Bilder müssen unter ```template/img``` abgespeichert werden.


## Script ausführen

Um die Website aus dem Inhalt und der Vorlage zu generieren, muss das Python-Script ```contentRoboto.py``` zu Hilfe genommen werden. Dazu in der Konsole/Terminal in das makershop-Verzeichnis und von dort in den Spracheordner wechseln. Dort kann das Script mit dem Befehl ```python contentRoboto.py``` aufgerufen werden. Es genertiert dann einen Ordner ```/website``` der dann mit Cyperduck auf den FTP-Server von Simone transferiert werden kann.

### Pfade
* Deutsche Website: ```httpdocs/mulhouse```
* Französische Website: ```httpdocs/mulhouse/fr```