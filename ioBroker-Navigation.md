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

Subpages haben verschiedene Navigationsmöglichkeiten, diese definiert Ihr im Bereich der Page-Definition. Damit definiert ihr auch, welche der vier Navi-Symbole in den oberen Ecken angezeigt werden.

* subPage: true -> Seite wird als Unterseite definiert
* parent: <Seitenname der übergeordneten Seite> -> definiert welche Seite aufgerufen wird beim Drücken auf den Pfeil nach oben
* prev: <Seitenname der vorhergehenden Seite> -> definiert welche Seite aufgerufen wird beim Drücken auf den Pfeil nach links
* next: <Seitenname der nächsten Seite> -> definiert welche Seite aufgerufen wird beim Drücken auf den Pfeil nach rechts
* home: <Seitenname der Übersichtsseite> -> definiert welche Seite aufgerufen wird beim Drücken auf das Haus-Symbol

> **Wichtig!** 
> Wenn „prev“ eine Seite zugewiesen wurde, wird „parent“ nicht ausgewertet. Das gleiche gilt auch für „next“ und „home“. 
 
```
let Level_2_Erdgeschoss_1: PageGrid =
    {
        'type': 'cardGrid',
        'heading': 'Erdgeschoss (1)',
        'useColor': true,
        'subPage': true,
        'parent': Level_1_Haus,
        'prev': undefined,
        'next': 'Level_2_Erdgeschoss_2',
        'home': 'Level_1_Haus',
        'items': [
                    <PageItem>{ navigate: true, id: null, targetPage: 'Level_3_Wohnzimmer', name: 'Wohnzimmer' , icon: 'sofa-outline', offColor: MSRed, onColor: MSGreen},
                    <PageItem>{ navigate: true, id: null, targetPage: 'Level_3_Esszimmer', name: 'Esszimmer' , icon: 'table-chair', offColor: MSRed, onColor: MSGreen},
                    <PageItem>{ navigate: true, id: null, targetPage: 'Level_3_Buero', name: 'Büro' , icon: 'desk', offColor: MSRed, onColor: MSGreen},
                    <PageItem>{ navigate: true, id: null, targetPage: 'Level_3_Kueche', name: 'Küche' , icon: 'silverware-variant', offColor: MSRed, onColor: MSGreen},
                    <PageItem>{ navigate: true, id: null, targetPage: 'Level_3_Bad', name: 'Bad' , icon: 'bathtub-outline', offColor: MSRed, onColor: MSGreen},
                    <PageItem>{ navigate: true, id: null, targetPage: 'Level_3_Kaminzimmer', name: "Kaminzimmer" , icon: "fireplace", offColor: MSRed, onColor: MSGreen},
                    ]
                };
```  

![image](https://user-images.githubusercontent.com/102996011/210829375-90ab3d40-b3a4-4794-816d-dcc60f2e7271.png)


#### Icons für Subpages (ab v3.7.3.2)  

Es gibt jetzt 3 Varianten, um ein Icon für Subpages anzulegen.

* Die alte Variante mit festem Icon und Farbe.
```
<PageItem>{ navigate: true, id: 'NSPanel_Einstellungen', icon: 'wrench-outline', onColor: White, name: 'Screensaver'}  
```
## Navigation mit den Hardware-Buttons  
