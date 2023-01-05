# Einleitung:  

## Navigation mit den TFT-Icons (Pfeil rechts, -links, -oben und Haus)  

Es gibt zwei Möglichkeiten durch die Seiten des Panels zu navigieren. Zum einen gibt es die Navigation auf dem Panel mit den Symbolen Pfeil Rechts, Links und Pfeil nach oben und Haus-Symbol. Die Zweite und etwas schwierige Variante ist über die Tasten unter dem Panel, dazu aber später mehr. Zuerst sehen wir uns die Struktur der Seiten und ihre Aufteilung an.

> Bild folgt  

### Vorbereitung und Gedanken zur Menüstruktur  

Bevor Ihr eure Seiten definiert, sollte ihr euch Gedanken über die Menüstruktur eures Panels machen. Hier ein Beispiel wie so etwas aussehen kann. Es ist auch nützlich, seine Alias Struktur genauso anzulegen mit Ordner und Unterordnern, wie sie im Panel existiert. So behaltet ihr den Überblick welcher Alias zu welcher Page gehört.

> bild folgt  

In der ersten Ebene befinden sich die Hauptseiten / Pages, welche im Skript im Bereich „Config -> Pages [...]“ deklariert werden. Hier werden die Namen der Seiten eingetragen, die Ihr an Anfang des Skripts definiert habt. Dabei ist die Reihenfolge zwischen den beiden eckigen Klammern wichtig, diese spiegelt auch die Reihenfolge auf dem Panel wider. Eine Besonderheit hat der erste Eintrag, dass ist die Startseite / Page 0. Diese hat auch den Status der Homeseite und wird aufgerufen, wenn ihr auf das Haus Symbol bei den Subpages drückt. Die Subpages könnt ihr von den Hauptseiten / Pages öffnen, wenn ihr die Eigenschaften naviagte:true und tagetPage: in Kombination nutzt.  

Wie so etwas in den Seiten definiert wird, steht im Abschnitt "Icon für Subpages"  

> Link folgt  

Um durch die Hauptseiten / Pages zu blättern, habt Ihr oben links und rechts jeweils ein Pfeil. Die Seiten sind als Endlosschleife angelegt, das heißt, wenn ihr bei der letzten Seite weiter nach rechts blättert, kommt ihr wieder zur ersten Seite und umgekehrt.

### Subpages  

  

## Navigation mit den Hardware-Buttons  
