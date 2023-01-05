by TT-Tom

# Einleitung:  

> **ab TS-Script v3.8.0**

**Es gibt zwei Möglichkeiten durch die Seiten des Panels zu navigieren. Zum einen gibt es die Navigation auf dem Panel mit den Symbolen Pfeil Rechts, Links und Pfeil nach oben und Haus-Symbol. Die Zweite und etwas schwierige Variante ist über die Tasten unter dem Panel, dazu aber später mehr. Zuerst sehen wir uns die Struktur der Seiten und ihre Aufteilung an.**  

## Navigation mit den TFT-Icons (Pfeil rechts, -links, -oben und Haus)  

[![image](https://user-images.githubusercontent.com/102996011/210832636-750fee62-ec5f-455b-9be0-b73c70fb6eb8.png)](https://user-images.githubusercontent.com/102996011/210832636-750fee62-ec5f-455b-9be0-b73c70fb6eb8.png)

### Vorbereitung und Gedanken zur Menüstruktur  

Bevor Ihr eure Seiten definiert, sollte ihr euch Gedanken über die Menüstruktur eures Panels machen. Hier ein Beispiel wie so etwas aussehen kann. Es ist auch nützlich, seine Alias Struktur genauso anzulegen mit Ordner und Unterordnern, wie sie im Panel existiert. So behaltet ihr den Überblick welcher Alias zu welcher Page gehört.

![image](https://user-images.githubusercontent.com/102996011/210839808-5d1c9531-1db4-41f2-88f3-ced3b59a4943.png)

Es bewährt sich ebenfalls, dass Schema in einer Excel-Tabelle niederzuschreiben. Nachfolgend ein Beispiel:  
![image](https://user-images.githubusercontent.com/102996011/210841168-46f76dc4-6755-4728-80f5-05f55992f21a.png)
 
In der ersten Ebene befinden sich die Hauptseiten / Pages, welche im Skript im Bereich „Config -> Pages [...]“ deklariert werden. Hier werden die Namen der Seiten eingetragen, die Ihr an Anfang des Skripts definiert habt. Dabei ist die Reihenfolge zwischen den beiden eckigen Klammern wichtig, diese spiegelt auch die Reihenfolge auf dem Panel wider. Eine Besonderheit hat der erste Eintrag, dass ist die Startseite / Page 0. Diese hat auch den Status der Homeseite und wird aufgerufen, wenn ihr auf das Haus Symbol bei den Subpages drückt. Die Subpages könnt ihr von den Hauptseiten / Pages öffnen, wenn ihr die Eigenschaften naviagte:true und tagetPage: in Kombination nutzt.  

Wie so etwas in den Seiten definiert wird, steht im Abschnitt: ["Icon für Subpages"](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-Navigation#icons-f%C3%BCr-subpages-ab-v3732)  

Um durch die Hauptseiten / Pages zu blättern, habt Ihr oben links und rechts jeweils ein Pfeil. Die Seiten sind als Endlosschleife angelegt, das heißt, wenn ihr bei der letzten Seite weiter nach rechts blättert, kommt ihr wieder zur ersten Seite und umgekehrt.

### Subpages  

Subpages haben verschiedene Navigationsmöglichkeiten, diese definiert Ihr im Bereich der Page-Definition. Damit definiert ihr auch, welche der vier Navi-Symbole in den oberen Ecken angezeigt werden.

* **subPage**: true -> Seite wird als Unterseite definiert
* **parent**: <Seitenname der übergeordneten Seite> -> definiert welche Seite aufgerufen wird beim Drücken auf den Pfeil nach oben
* **prev**: <Seitenname der vorhergehenden Seite> -> definiert welche Seite aufgerufen wird beim Drücken auf den Pfeil nach links
* **next**: <Seitenname der nächsten Seite> -> definiert welche Seite aufgerufen wird beim Drücken auf den Pfeil nach rechts
* **home**: <Seitenname der Übersichtsseite> -> definiert welche Seite aufgerufen wird beim Drücken auf das Haus-Symbol

> **Wichtig!**  
> Wenn **„prev“** eine Seite zugewiesen wurde, wird **„parent“** nicht ausgewertet. Das gleiche gilt auch für **„next“** und **„home“**. 
 
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

##### Variante 1 (ursprüngliche Notation)  
* Die ursprüngliche Variante mit festem Icon und fester Farbe:
  ```
  <PageItem>{ navigate: true, id: 'NSPanel_Einstellungen', icon: 'wrench-outline', onColor: White, name: 'Screensaver'}  
  ```  
  Die Eigenschaft "navigate: true" macht aus einem normalen Steuerelement, ein Icon, um eine Subpage zu öffnen. Des Weiteren wird die Eigenschaft "id:" benötigt. Sie enthält den Namen der Subpage. Diese beiden Angaben sind Pflicht, mit "icon: und onColor:" kann man von dem Standardicon und Farbe abweichen und Eigene definieren.  

##### Variante 2 (neue Notation)  
* Die neue Variante:
  ```
  <PageItem>{ navigate: true, id: null, targetPage: 'WlanDaten', onColor: White, name: 'Gäste WLAN Daten'}
  ```
  Bei der neuen Schreibweise bleibt das Verhalten zu der Alten gleich. Hier ist nur die Schreibweise für das Ziel (Subpage) angepasst. Wobei meiner Meinung nach es die richtige Schreibweise ist. Pflicht sind folgende Eigenschaften: "naigate: true",  "id: null" und (neu) "tagetPage:" hier kommt jetzt der Name der Subpage ran, der bei der alten Schreibweise hinter "id:" stand.

> Wichtiger Hinweis:  
> Ihr müsst euer Icon für die Subpage nicht umschreiben, es funktionieren beide Schreibweisen. Die User, die auch die Variante 3 (dynamische) einsetzen wollen, sollten auch die neue Schreibweise für die statischen Icon nutzen.  

##### Variante 3 dynamische Icon (neue Notation)  

**Was heißt dynamische Icon?**  

Das Icon auf eurem Panel kann die Farbe und das Icon selbst ändern, je nach Status des Alias (ture/false).
Ich nutze es für meine Fenster- und Türkontakte, die ich in Subpages gebündelt habe. Auf der Übersichtspage habe ich Icons für die einzelnen Subpages, diese Icon ändern ihr Aussehen, wenn auf der Subpage sich ein Kontakt ändert. Somit sehe ich auf der Übersichtseite, dass alle Fenster und Türen geschlossen sind. Sollte ein Fenster offen sein, ändert sich auf der Überichtseite das Icon auf "offenes Fenster und wird Rot". Jetzt kann ich auf das Icon drücken und sehe in der Subpage welches Fenster noch offen ist.

Um dieses Verhalten zu nutzen, benötigt ihr ein Alias vom Typ "Info", einen Datenpunkt unter "0_userdata.0." welcher mit dem Alias verknüpft ist und ein kleines Skript, welches eure Kontakte überwacht und den Datenpunkt unter 0_userdata.0. auf true bzw. false setzt.

* Die neue Variante mit dynamischem Icon und dynamischer Farbe:
  ```
  <PageItem>{ navigate: true, id: alias.0.haus.fenster, targetPage: 'Fenster', onColor: MSGreen, offColor: MSRed, name: 'Fenster'}
  ```

Hier ein Beispiel als Blockly, welches alle Fenster in einem Aliasordner überwacht und den Datenpunkt entsprechend setzt.
  
  
![Blockly_dynamische _Srungmarke](https://user-images.githubusercontent.com/101348966/210888849-35b34ea7-86b1-4c3f-814a-b98873d6d158.png)
  
  
Wie Ihr den Datenpunkt unter 0_userdata.0. setzen wollt, könnt ihr selbst entscheiden und ist auch ganz von der Anzahl der Kontakte abhängig. Auf einer cardGrid könnt ihr maximal 6 Icon / Kontakte darstellen. Deshalb kann es notwendig sein, noch eine Subpage dazwischen zu setzen und diese nach Stockwerken aufzuteilen.

## Navigation mit den Hardware-Buttons  

es gibt mehrere Möglichkeiten die Tasten mit Funktionen zur Steuerung des Panels zu belegen. Standardmäßig steuern diese Tasten die Relais im Panel. Durch Aktivierung einer Regel in der Tasmota Konsole (Info zu Tasmota link) können die Tasten von den Relais entkoppelt werden und softwareseitig genutzt werden.

> **Bitte nicht verwenden, wenn Rule 2 mit buttonXPages belegt ist**

**In der Tasmota Konsole:**
```
Rule2 on Button1#state do Publish %topic%/%prefix%/RESULT {"CustomRecv":"event,button1"} endon on Button2#state do Publish %topic%/%prefix%/RESULT {"CustomRecv":"event,button2"} endon
Rule2 1 (Rule aktivieren)
Rule2 0 (Rule deaktivieren)
```  

Um die Tasten mit festen Seiten zu belegen, müssen im Skript im Bereich „Config“ die Parameter „button1Page bzw. button2Page“ die Seiten definiert werden. Beispiel:

```  
button1Page: null, // keine Seite definiert
button2Page: Thermostat_WZ // CardThermo für Wohnzimmer
```  

Wenn die Seiten zum Blättern durch die Seiten genutzt werden sollen, müssen folgende Änderungen durchgeführt werden. Mit dieser Rule kann die linke Taste eine Seite nach oben springen (Eigenschaft parent: ) und die rechte Taste zur Startseite bzw. auf die Seite die durch die Eigenschaft home: definiert wurde.

``` 
Rule1 on Button1#state do Publish %topic%/tele/RESULT {"CustomRecv":"event,buttonPress1,hwbtn,bUp"} endon on Button2#state do Publish %topic%/tele/RESULT {"CustomRecv":"event,buttonPress2,hwbtn,bHome"} endon
``` 