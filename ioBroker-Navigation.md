by TT-Tom

# Einleitung:  

> **ab TS-Script v3.8.0**

**Es gibt zwei Möglichkeiten durch die Seiten des Panels zu navigieren. Zum einen gibt es die Navigation auf dem Panel mit den Symbolen Pfeil Rechts, Links und Pfeil nach oben und Haus-Symbol. Die Zweite und etwas schwierige Variante ist über die Tasten unter dem Panel, dazu aber später mehr. Zuerst sehen wir uns die Struktur der Seiten und ihre Aufteilung an.**  

> ab TS-Script v3.8.3  
**Die Definition der Seiten hat sich geändert.**  
```typescript  
let Variablenname = <Seitentyp>
```

Daraus ergeben sich folgende Vorteile:  

Es müssen nicht mehr alle Seitenparameter angegeben werden, wie z.B  
```typescript  
let CardPowerExample = <PagePower>  
  {
  'type': 'cardPower',
  'heading': 'cardPower Emulator',
  'items': [
  <PageItem>{ id: 'alias.0.NSPanel_1.Power.PowerCard' },
   ]};
```
d.h. alle optionalen Seitenparameter mit undefined oder false können entfallen.  
Zusätzlich können weitere Typen verwendet werden, diese werden [hier](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-Navigation#subpages) beschrieben.

```typescript  
let CardPowerExample = <PagePower>
   {
   'type': 'cardPower',
   'heading': 'cardPower Emulator',
   'useColor': true oder false
   'subPage': true oder false
   'parent': undefined oder Page
   'parentIcon': undefined oder Icon als String, z.B. 'alert'
   'prev': undefined oder 'Page'
   'prevIcon': undefined oder Icon als String
   'next': undefined oder 'Page'
   'nextIcon': undefined oder Icon als String
   'home': undefined oder 'Page'
   'homeIcon': undefined oder Icon als String
   'items': [
   <PageItem>{ id: 'alias.0.NSPanel_1.Power.PowerCard' },
   ]
   };
```


## Navigation mit den TFT-Icons (Pfeil rechts, -links, -oben und Haus)  

![Grafik Navi](https://user-images.githubusercontent.com/101348966/212481713-b1122be0-0138-4c30-a41c-69565b258f9d.png)

### Vorbereitung und Gedanken zur Menüstruktur  

Bevor Ihr eure Seiten definiert, sollte ihr euch Gedanken über die Menüstruktur eures Panels machen. Hier ein Beispiel wie so etwas aussehen kann. Es ist auch nützlich, seine Alias Struktur genauso anzulegen mit Ordner und Unterordnern, wie sie im Panel existiert. So behaltet ihr den Überblick welcher Alias zu welcher Page gehört.

![image](https://user-images.githubusercontent.com/102996011/210839808-5d1c9531-1db4-41f2-88f3-ced3b59a4943.png)

Es bewährt sich ebenfalls, dass Schema in einer Excel-Tabelle niederzuschreiben. Nachfolgend ein Beispiel:  
![image](https://user-images.githubusercontent.com/102996011/210841168-46f76dc4-6755-4728-80f5-05f55992f21a.png)
 
In der ersten Ebene befinden sich die Hauptseiten / Pages, welche im Skript im Bereich „export const config: Config = { -> Pages [...]“ deklariert werden. Hier werden die Namen der Seiten eingetragen, die Ihr an Anfang des Skripts definiert habt. Dabei ist die Reihenfolge zwischen den beiden eckigen Klammern wichtig, diese spiegelt auch die Reihenfolge auf dem Panel wider. Eine Besonderheit hat der erste Eintrag, dass ist die Startseite / Page 0. Diese hat auch den Status der Homeseite und wird aufgerufen, wenn ihr auf das Haus Symbol bei den Subpages drückt, wenn die Eigenschaft **'home': undefined** ist. Die Subpages könnt ihr von den Hauptseiten / Pages öffnen, wenn ihr die Eigenschaften **navigate:true** und **targetPage: <Seitenname>** in Kombination nutzt.  

Wie so etwas in den Seiten definiert wird, steht im Abschnitt: [Icon für Subpages](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-Navigation#icons-f%C3%BCr-subpages-ab-v3732)  

Um durch die Hauptseiten / Pages zu blättern, habt Ihr oben links und rechts jeweils ein Pfeil. Die Seiten sind als Endlosschleife angelegt, das heißt, wenn ihr bei der letzten Seite weiter nach rechts blättert, kommt ihr wieder zur ersten Seite und umgekehrt.

### Subpages  

Subpages haben verschiedene Navigationsmöglichkeiten, diese definiert Ihr im Bereich der Page-Definition. Damit definiert ihr auch, welche der vier Navi-Symbole in den oberen Ecken angezeigt werden. Zusätzlich könnt ihr ab **Version 3.8.3** auch optional Icon definieren.

* **'subPage'**: true -> Seite wird als Unterseite definiert
* **'parent'**: <Seitenname der übergeordneten Seite> -> definiert welche Seite aufgerufen wird beim Drücken auf den Pfeil nach oben
* **'prev'**: <Seitenname der vorhergehenden Seite> -> definiert welche Seite aufgerufen wird beim Drücken auf den Pfeil nach links
* **'next'**: <Seitenname der nächsten Seite> -> definiert welche Seite aufgerufen wird beim Drücken auf den Pfeil nach rechts
* **'home'**: <Seitenname der Übersichtsseite> -> definiert welche Seite aufgerufen wird beim Drücken auf das Haus-Symbol

* **'parentIcon', 'prevIcon', 'nextIcon' und 'homeIcon'**: als Parameter gelten ->  undefined oder Icon als String, z.B. 'alert'

> **Wichtig!**  
> Wenn **'prev'** eine Seite zugewiesen wurde, wird **'parent'** nicht ausgewertet. Das gleiche gilt auch für **'next'** und **'home'**. 
 
```typescript  
let Level_2_Erdgeschoss_2 = <PageGrid>
                {
                    'type': 'cardGrid',
                    'heading': 'Erdgeschoss (2)',
                    'useColor': true,
                    'subPage': true,
                    'parent': Level_1_Haus,
                    'prev': 'Level_2_Erdgeschoss_1',
                    'prevIcon': 'home-group-minus',
                    'home': 'Level_1_Haus',
                    'homeIcon': 'play-pause',
                    'items': [
                        <PageItem>{ navigate: true, id: 'alias.0.Haus.Erdgeschoss.Gaeste_WC.Indikator', targetPage: 'Level_3_GaesteWC', name: 'Gäste WC' , icon: 'toilet', offColor: MSGreen, onColor: MSRed},
                        <PageItem>{ navigate: true, id: 'alias.0.Haus.Erdgeschoss.Hauswirtschaftsraum.Indikator', targetPage: 'Level_3_Hauswirtschaftsraum', name: 'Hauswirtschaft' , icon: 'floor-plan', offColor: MSGreen, onColor: MSRed},
                        <PageItem>{ navigate: true, id: 'alias.0.Haus.Erdgeschoss.Flur_vorne.Indikator', targetPage: 'Level_3_EG_FlurVorne', name: 'Flur vorne' , icon: 'floor-plan', offColor: MSGreen, onColor: MSRed},
                        <PageItem>{ navigate: true, id: 'alias.0.Haus.Erdgeschoss.Flur_hinten.Indikator', targetPage: 'Level_3_EG_FlurHinten', name: 'Flur hinten' , icon: 'floor-plan', offColor: MSGreen, onColor: MSRed},
                    ]
                };
```  

![screenPanelNavi](https://user-images.githubusercontent.com/101348966/212483124-5c3c4f67-2a54-469a-a514-7aef78ff02d8.png)



#### Icons für Subpages (ab v3.7.3.2)  

Es gibt jetzt 3 Varianten, um ein Icon für Subpages anzulegen.

##### Variante 1 (ursprüngliche Notation)  
* Die ursprüngliche Variante mit festem Icon und fester Farbe:
  ```
  <PageItem>{ navigate: true, id: 'NSPanel_Einstellungen', icon: 'wrench-outline', onColor: White, name: 'Screensaver'}  
  ```  
  Die Eigenschaft **navigate: true** macht aus einem normalen Steuerelement, ein Icon, um eine Subpage zu öffnen. Des Weiteren wird die Eigenschaft **id:** benötigt. Sie enthält den Namen der Subpage. Diese beiden Angaben **sind Pflicht**, mit **icon:** und **onColor:** kann man von dem Standardicon und Farbe abweichen und Eigene definieren.  

##### Variante 2 (neue Notation)  
* Die neue Variante:
  ```
  <PageItem>{ navigate: true, id: null, targetPage: 'WlanDaten', onColor: White, name: 'Gäste WLAN Daten'}
  ```
  Bei der neuen Schreibweise bleibt das Verhalten zu der Alten gleich. Hier ist nur die Schreibweise für das Ziel (Subpage) angepasst. Wobei meiner Meinung nach es die richtige Schreibweise ist. Pflicht sind folgende Eigenschaften: **naigate: true, id: null**, und (neu) **tagetPage:**. Hier kommt jetzt der Name der Subpage ran, der bei der alten Schreibweise hinter **id:** stand.

> Wichtiger Hinweis:  
> Ihr müsst euer Icon für die Subpage nicht umschreiben, es funktionieren beide Schreibweisen. Die User, die auch die Variante 3 (dynamische) einsetzen wollen, sollten auch die neue Schreibweise für die statischen Icon nutzen.  

##### Variante 3 dynamische Icon (neue Notation)  

**Was heißt dynamische Icon?**  

Das Icon auf eurem Panel kann die Farbe und das Icon selbst ändern, je nach Status des Alias (ture/false).
Ich nutze es für meine Fenster- und Türkontakte, die ich in Subpages gebündelt habe. Auf der Übersichtspage habe ich Icons für die einzelnen Subpages, diese Icon ändern ihr Aussehen, wenn auf der Subpage sich ein Kontakt ändert. Somit sehe ich auf der Übersichtseite, dass alle Fenster und Türen geschlossen sind. Sollte ein Fenster offen sein, ändert sich auf der Überichtseite das Icon auf "offenes Fenster und wird Rot". Jetzt kann ich auf das Icon drücken und sehe in der Subpage welches Fenster noch offen ist.

Um dieses Verhalten zu nutzen, benötigt ihr ein Alias vom **Typ "Info"**, einen Datenpunkt unter "0_userdata.0." welcher mit dem Alias verknüpft ist und ein kleines Skript, welches eure Kontakte überwacht und den Datenpunkt unter 0_userdata.0. auf true bzw. false setzt.

* Die neue Variante mit dynamischem Icon und dynamischer Farbe:
  ```typescript  
  <PageItem>{ navigate: true, id: alias.0.haus.fenster, targetPage: 'Fenster', onColor: MSGreen, offColor: MSRed, name: 'Fenster'}
  ```

Hier ein Beispiel als Blockly, welches alle Fenster in einem Aliasordner überwacht und den Datenpunkt entsprechend setzt.
  
  
![Blockly_dynamische _Srungmarke](https://user-images.githubusercontent.com/101348966/210888849-35b34ea7-86b1-4c3f-814a-b98873d6d158.png)
  
  
Wie Ihr den Datenpunkt unter 0_userdata.0. setzen wollt, könnt ihr selbst entscheiden und ist auch ganz von der Anzahl der Kontakte abhängig. Auf einer cardGrid könnt ihr maximal 8 Icon / Kontakte darstellen. Deshalb kann es notwendig sein, noch eine Subpage dazwischen zu setzen und diese nach Stockwerken aufzuteilen.

**Erweiterung ab Version 4.2**  
  
die Flexibilität der Icon wurde um die Farbe und dem Buttontext(CardEntities) erweitert.  
Dazu müssen zwei Datenpunkte im Alias angelegt werden.  
**COLORDEC** (Typ Zahl) beinhaltet die Farbzahl entsprechend DEC565.  
[Hier gibt es ein Nextion-HMI-Color-Converter](https://nodtem66.github.io/nextion-hmi-color-convert/index.html)  
**BUTTONTEXT** (Typ String) statt PRESS kann der Text freigewählt werden.  
  
<img width="331" alt="Bildschirmfoto 2023-08-21 um 16 10 40" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/5edbb8b0-ead3-4c69-9a9a-479eb2cb6e16">

Mindest Schreibweise, wenn DatenPunkte angelegt sind.  
```typescript  
<PageItem>{ navigate: true, id: AliasPath + 'Status_offene_Tuer', targetPage:'Tuer', name: 'Türen'},
```
  
Wenn einer oder beide Datenpunkte nicht vorhanden sind, wird die altbekannt Schreibweise heran gezogen, wie z.B.  
```typescript  
<PageItem>{ navigate: true, id: AliasPath + 'Status_offene_Tuer', targetPage:'Tuer', useColor:true, onColor: Green, offColor: Red, name: 'Türen', buttonText: 'hier drücken'},
```

## Navigation mit den Hardware-Buttons  

Es gibt mehrere Möglichkeiten die Tasten mit Funktionen zur Steuerung des Panels zu belegen. Standardmäßig steuern diese Tasten die Relais im Panel. Durch Aktivierung einer Regel in der Tasmota Konsole können die Tasten von den Relais entkoppelt werden und softwareseitig genutzt werden. Wir haben die Einstellungen unter der Rubrik [NSPanel Tasmota FAQ](https://github.com/joBr99/nspanel-lovelace-ui/wiki/NSPanel-Tasmota-FAQ) zusammengefasst. 

