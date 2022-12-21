> **Seite befindet sich noch im Aufbau  
> Sollte aktuell ein Alias nicht vollständig beschrieben werden, dann gerne eine Frage am Ende des nachfolgenden Thread stellen:**
> https://forum.iobroker.net/topic/50888/sonoff-nspanel

# Einleitung: 

## Alias-Hilfsmittel
**Welche Hilfsmittel werden zur Erstellung eines Alias benötigt?:**  

Der "Geräte verwalten"-Adapter für die meisten Alias-Typen:  
![image](https://user-images.githubusercontent.com/102996011/189475521-07d78146-e49d-406a-95bc-804b3302caa2.png)

Der "Alias-Manager"-Adapter für spezielle Alias-Typen, wie dem Alias "Media":  
![image](https://user-images.githubusercontent.com/102996011/189475471-26f0ed04-4715-4eed-8924-cf6d7be879a9.png)  

**Ich habe die zwei Adapter installiert. Wie bekomme ich die in das ioBroker-Menü:**  
Über das Stift-Symbol im ioBroker-Hauptmenü lassen sich die Adapter individuell für jeden Benutzer ein- oder ausschalten.
![image](https://user-images.githubusercontent.com/102996011/189476871-85b18ead-f032-4bd0-b8a4-310742b778fc.png)
![image](https://user-images.githubusercontent.com/102996011/189476923-59ef3397-543f-43ef-9ab9-e839b9eba9cb.png)

Es sollte ein Haken bei Geräte und Alias-Manager gesetzt sein.

**Was sind Aliase:**  
Aliase (Pseudonyme) sind die virtuellen Zustandsobjekte, die mit realen Zuständen (Datenpunkten) verknüpft sind.  

**Warum benötige ich im TS-Skript überhaupt Aliase und keine Datenpunkte?**  
Das TS-Script für das Sonoff NSPanel ist so aufgebaut, dass eigentlich jeder Adapter zur Steuerung benutzt werden kann. Hierbei haben die Entwickler von Adaptern für gleiche Funktionen unterschiedliche Namen verwendet:

Beispiel: 
* Sonoff-Adapter: **.power** (aus Tasmota übertragen)
* MQTT-Adapter: **.power** (aus Tasmota übertragen) 
* Shelly-Adapter: **.switch**
* KNX-Adapter: **.switch**
* Deconz-Adapter: **.on**
* etc.  

Also immer der Wunsch, einen Zustand eines Aktors mit true/false zu verändern.  

> Innerhalb der Licht-Adapter wird das später noch deutlicher

Der Alias benötigt also anstatt **.Power** oder **.Switch** oder **.On** immer nur ein **.SET**, damit der Zustand des Schalt-Aktor's unabhängig vom installierten Adapter geschaltet werden kann. In diesem Fall meldet der im Skript eingebundene Alias ein true oder false in den Alias-Datenpunkt .SET und reicht den Zustandswert an den zugewiesenen spezifischen Adapter-Datenpunkt (ganz egal welcher Typ erwartet wird) weiter.

# "Geräte verwalten"-Adapter
Zunächst sollt man sich überlegen, welche Aliase nur für ein bestimmtes NSPanel gelten sollen oder für mehrere NSPanels oder sogar innerhalb anderer Visualisierungsarten z.B. ioBroker VIS mitverwendet werden sollen. Dann kann man die Alias Struktur entsprechend mit Ordnern und Unterordnern verfeinern. Das Bürolicht soll z.B. nur über NSPanel_1 geschaltet werden, aber nicht über NS_Panel_2. Das Wetter hingegen ist für alle NSPanel gleich.  
![image](https://user-images.githubusercontent.com/102996011/189477432-2c814d56-7c37-41c2-b371-31b06e6fe2aa.png)

## Alias erzeugen - Schritt 1 - Tab "Allgemein"
Der erste Schritt in der Alias Erstellung mit dem "Geräte verwalten"-Adapter ist fast immer der gleiche.

Es wird über die "+" Schaltfläche folgender Dialog aufgeschaltet:  
![image](https://user-images.githubusercontent.com/102996011/189480182-02d50b01-53ba-4c83-baa6-9bd5f10bc671.png)  
Jetzt gibst vergibst du einen "sprechenden Namen" für den Alias in der Zeile "Gerätename" und wählst einen der nachfolgenden "Alias-Typen" unter Gerätetyp aus (Auswahlliste wird aufgeschaltet und beinhaltet auch noch weitere Typen als im Bild gezeigt (Momentaufnahme)):     

![image](https://user-images.githubusercontent.com/102996011/189480322-0441c5b7-fc7e-4fd4-9920-72915753a802.png)  

> Achtung:  
> Nicht jeder Gerätetyp (Alias-Typ) funktioniert mit dem NSPanel, sondern nur die, die entweder im weiteren Verlauf benannt sin, oder die im Header des TypeScript definiert sind.  

Die Zeilen Funktion und Raum können ebenfalls ausgewählt werden, haben jedoch keinen Einfluss auf die Funktionalität des NSPAnel's

## Alias erzeugen - Schritt 2 - Tab "Zustände"

### Alarm - cardAlarm

siehe auch das Beispiel zur vollständigen Integration der cardAlarm in den ioBroker:  
https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#2-alarm-page
   
![image](https://user-images.githubusercontent.com/102996011/189404542-81735372-7bbd-4c1a-8cad-73d1a62bd735.png)

***
### Dimmer (channel dimmer)

Der Alias "Dimmer" hat 2 relevante Eigenschaften.   
* Schalter (an/aus) über Adapter-Datenpunkte on, switch, power, etc.  
* Helligkeit (dunkel/hell) über Adapter-Datenpunkte level, brightness, bri, etc.  

**Im Beispiel ist eine dimmbare Deckenbeleuchtung über den DeConz-Adapter (Zigbee)**  

Der Schalter im DeConz wird über den Datenpunkt "on" (true/false), d.h Datentyp "boolean" gesteuert.
Die Helligkeit wird im Deconz-Adapter über "level" 0-100 oder "bri" 0-255 gesteuert. Für uns bietet sich also der Datenpunkt **level** an, da dieser bereits die Helligkeit in % von 0% bis 100% beinhaltet. Jedoch könnten wir auch mit dem Datentyp **bri** arbeiten und im TypeScript die Umrechnung von 255 (absolut) auf 100 (%) parametrieren.  

Der Dimmer kann in einer cardEntities oder in einer cardGrid platziert werden. (Nachfolgende Abb. cardEntities):   
![image](https://user-images.githubusercontent.com/102996011/189492309-e678414a-21b9-417f-b6a5-bdd769db7fc4.png)  
 
Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ Dimmer an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des DeConz-Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/189492261-48519b87-3210-4bb9-a039-489e57bc21de.png)  

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung.
![image](https://user-images.githubusercontent.com/102996011/189492446-1c530407-cac3-4f3e-ab06-258dcd88629c.png)  

Der Schaltzustand (Lampe an/aus) kann direkt aus der cardEntities oder carGrid erfolgen. Für die Regelung der Helligkeit hat der Alias-Gerätetyp "Dimmer" bereits eine Unterseite (siehe nachfolgende Abb.). Diese kann über einen Klick auf den Dimmer-Bezeichner (in diesem Fall "Deckenbeleuchtung") aufgeschaltet werden:  

![image](https://user-images.githubusercontent.com/102996011/189493396-b94fdccb-61ee-4c1d-97d2-8732e7c1d9ae.png)  

Das zugehörige PageItem im TypeScript:  
![image](https://user-images.githubusercontent.com/102996011/189493609-51ebffec-c119-4a58-bb85-bdf253383548.png)  
Mit dem Parameter "name" legen wir den Anzeigenamen fest.  
Mit dem Parameter "interpolateColor" (optional), soll die abgebildete Lampe (Icon) den An/Aus und die Helligkeit emulieren.  
  
Es können noch weitere Parameter übergeben werden:
* icon  
* onColor  
* offColor  
* minValueBrightness (Default = 0)
* maxValueBrightness (Default = 100; im Beispiel mit dem Datenpunkt "bri" also 255)

***

### Farbtemperatur (channel ct)  

Der Alias "Farbtemperatur" hat 3 relevante Eigenschaften.   
* Schalter (an/aus) über Adapter-Datenpunkte on, switch, power, etc.  
* Helligkeit (dunkel/hell) über Adapter-Datenpunkte level, brightness, bri, etc. 
* Farbtemperatur (K = Kelvin) über Adapter-Datenpunkte ct, colortemp, etc.  

Der Alias "Farbtemperatur" kann in einer cardEntities oder in einer cardGrid platziert werden. (Nachfolgende Abb. cardEntities):
![image](https://user-images.githubusercontent.com/102996011/189497667-0362a360-ef6b-4d7a-98ea-de55e6b42535.png)  

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **Farbtemperatur** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  

![image](https://user-images.githubusercontent.com/102996011/189498366-2d0d8e4c-e161-4f57-a084-c2377da001c3.png)  

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung.
![image](https://user-images.githubusercontent.com/102996011/189498497-989cc054-812a-4c58-8995-5c4ccf39f4b9.png)  

Der Schaltzustand (Lampe an/aus) kann direkt aus der cardEntities oder carGrid erfolgen. Für die Regelung der Helligkeit und CT hat der Alias-Gerätetyp "Farbtemperatur" bereits eine Unterseite (siehe nachfolgende Abb.). Diese kann über einen Klick auf den Bezeichner (in diesem Fall "Farbtemperatur") aufgeschaltet werden: 
![image](https://user-images.githubusercontent.com/102996011/189497755-b3bbc89a-8b36-451e-add2-ba6c12e94330.png)  

Das zugehörige PageItem im TypeScript:  
![image](https://user-images.githubusercontent.com/102996011/189498614-4aa1dc89-cf5e-48f5-a0be-f2b0e11cc8d0.png)  
Mit dem Parameter "name" legen wir den Anzeigenamen fest.  
Mit dem Parameter "interpolateColor" (optional), soll die abgebildete Lampe (Icon) den An/Aus und die Helligkeit emulieren.  
  
Es können noch weitere Parameter übergeben werden:
* icon  
* onColor  
* offColor  
* minValueBrightness (Default = 0)
* maxValueBrightness (Default = 100; im Beispiel mit dem Datenpunkt "bri" also 255)
* minValueColorTemp  (z.B. 500  - in Abhängigkeit des jeweiligen Adapters) 
* maxValueColorTemp: (z.B. 6500 - in Abhängigkeit des jeweiligen Adapters)

> Hinweis: Es kann auch der HUE-CT verwendet werden

***

### Fenster (channel window)

Der Alias "Fenster" hat 1 relevante Eigenschaft.   
* Zustand (offen/geschlossen) über Adapter-Datenpunkte open, etc.  

Darstellung in einer "cardGrid"  
![image](https://user-images.githubusercontent.com/102996011/189404690-69e61c60-88f3-4ea7-b5ad-0c423094eb11.png)
Darstellung in einer "cardEntities"  
![image](https://user-images.githubusercontent.com/102996011/189403796-ab118db1-fb38-49ae-bbdf-199717e77bbe.png)

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **Fenster** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt den Datenpunkt des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/189498976-965bae49-3643-4c23-820f-e1540b3b28a2.png)  
Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:  
![image](https://user-images.githubusercontent.com/102996011/189499063-f0fa5d5a-4302-46ec-802c-0c99626f908a.png)  

Das zugehörige PageItem im TypeScript:  
![image](https://user-images.githubusercontent.com/102996011/189498910-6d64cfdd-faa6-448c-9542-43410866dfa2.png)

***

### Feuchtigkeit (channel humidity)

Der Alias "Feuchtigkeit" hat 1 relevante Eigenschaft.   
* Zustand (Sensorwert) 

![image](https://user-images.githubusercontent.com/102996011/189403392-4ba6c9b6-5d33-4bdb-abfb-36c85e99eebf.png)

**Im Beispiel ist ein Homatic IP Sensor über den hmip-Adapter (Funk).** Es kann aber auch jeder andere Sensor (z.B. Zigbee oder WLAN) oder ein Datenpunkt aus einem Wetter-Adapter verwendet werden.  

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **Feuchtigkeit** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/189499807-aba39d1c-5a83-4e50-ba04-8cc972f76208.png)  

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:  

![image](https://user-images.githubusercontent.com/102996011/189499784-2b3dc3c5-3196-4b8e-93d0-cf1c57452f8a.png)  

Das zugehörige PageItem im TypeScript:  
![image](https://user-images.githubusercontent.com/102996011/189499885-ace4b001-0c9c-4d0d-9667-d7c808d1f8fc.png)

Folgende Parameter können verwendet werden:  
* name: legt den Anzeigenamen fest  
* icon: Symbol  
* unit: Einheit der Luftfeuchte  
* onColor: Farbe des Icons  

`<PageItem>{ id: "alias.0.NSPanel_1.TestFeuchtigkeit", name: "Luftfeuchte außen", icon: "water-percent", unit: "%H", onColor: White}`  

> **Hinweis**  
> **Alternativ kann auch der Alias-Typ "Info" verwendet werden.**  

***

### HUE-Licht (channel hue)

> Der Alias Geräte-Typ **HUE-Licht** funktioniert **mit und ohne** dem Wert **"HUE"**. Wenn der Datenpunkt **.HUE** nicht vorhanden ist, wird durch das TypeScript automatisch eine CT (ColorTemperature-Steuerung emuliert)  

![image](https://user-images.githubusercontent.com/102996011/189403062-a5fed1f9-8c6b-49b5-ad94-82c344603d5a.png)

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **HUE-Licht** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/189500932-7d2f043a-f279-4525-ba98-3fe11cece1d5.png)

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:  
![image](https://user-images.githubusercontent.com/102996011/189500907-e527fc9b-b8d2-49d0-bc89-ba729cfe65b4.png)

Der Schaltzustand (Lampe an/aus) kann direkt aus der cardEntities oder carGrid erfolgen. Für die Regelung der Helligkeit, Farbtemperatur und (wenn vorhanden) Farbe hat der Alias-Gerätetyp "HUE-Licht" bereits eine Unterseite (siehe nachfolgende Abb.). Diese kann über einen Klick auf den Bezeichner  aufgeschaltet werden:
![image](https://user-images.githubusercontent.com/102996011/189402777-0937bfbf-6695-4768-9123-d61546175726.png)
![image](https://user-images.githubusercontent.com/102996011/189402911-7a9edf50-bb22-4211-9117-5b55e4ecba56.png)


***

### Info (channel info)
![image](https://user-images.githubusercontent.com/102996011/189403645-a9511303-c873-469c-9e92-136809162728.png)
![image](https://user-images.githubusercontent.com/102996011/189404981-bbd544b0-1019-48d7-a5eb-8f38616bb8b4.png)

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **Info** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/191102534-cd77c638-a947-46b7-a2c4-dafd4ba1380a.png)

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:  
![image](https://user-images.githubusercontent.com/102996011/191102721-3a6a5ab6-792c-4274-8ff3-227c61d4a949.png)

Beispiel für das PageItem  
`<PageItem>{ id: "alias.0.NSPanel_1.TestInfo", name: "Windstärke", icon: "wind-power-outline", offColor: MSRed, onColor: MSGreen, unit: "bft", minValue: 0, maxValue: 12, interpolateColor: true, useColor: true }`

**Parameter**
name:
icon:
offcolor:
oncolor:
unit:
minValue:
maxValue:
interpolateColor:
useColor:

***

### Jalousien (channel blind)
![image](https://user-images.githubusercontent.com/102996011/189403904-914ff6ad-a7df-4859-a523-ff5ec02f2381.png)  

Und die zugehörige Detailseite  
![image](https://user-images.githubusercontent.com/102996011/194716743-81b81575-b7b6-475a-9cbf-5332561bec46.png)  

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **Jalousie** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/194716982-6470580e-b8eb-4be0-8c45-c60dd9220a9c.png)  

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung: 
![image](https://user-images.githubusercontent.com/102996011/194716899-3064db6c-8516-46c0-857a-1126cae78783.png)  

Beispiel für das PageItem:  
`<PageItem>{ id: "alias.0.NSPanel_1.TestBlind", onColor: White, name: "IKEA Fyrtur", secondRow: "Hier Text für 2. Zeile"},`  

Bereits in der FAQ & Anleitung beschrieben: https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#8-rolladen--jalousie--shutter

***

### Klimaanlage - cardThermo - (channel airCondition)
![image](https://user-images.githubusercontent.com/102996011/189401952-86b47d90-69f2-4229-909c-8d4c2ee84d20.png)
***

### Lautstärke (channel volume)
![image](https://user-images.githubusercontent.com/102996011/189403220-a2540eb2-4b47-4947-9258-a7687403710c.png)

> **Analog zum Alias "Lautstärkegruppe", jedoch mit dem Alias-Gerätetypen "Lautstärke**"

***

### Lautstärke-Gruppe (channel volumeGroup)
![image](https://user-images.githubusercontent.com/102996011/189403220-a2540eb2-4b47-4947-9258-a7687403710c.png)

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **HUE-Licht** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/190144094-a13df619-fe45-4c92-a43a-e6a4e653083e.png)  

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:
![image](https://user-images.githubusercontent.com/102996011/190144755-8b2c2ae6-c9d4-4fa2-9139-c430b8385114.png)

Das zugehörige PageItem im TypeScript:  
![image](https://user-images.githubusercontent.com/102996011/190146010-ab51fa66-a8bc-4a2c-8f79-98425e19eabd.png)  

**Parameter:**  
name: Vom Alias abweichender Name  
offColor: wenn Muted  
onColor: wenn nicht Muted  
minValue: Minimale Lautstärkewert (Default 0)  
maxValue: Minimale Lautstärkewert (Default 100)  

***

### Licht (channel light)  
![image](https://user-images.githubusercontent.com/102996011/191106464-5ce4597e-fa4b-4e48-89e0-40d1cd9653d2.png)  
![image](https://user-images.githubusercontent.com/102996011/191106556-aa7dc0e8-00a5-4b09-90c5-9266e524567f.png)  

**Zur Steuerung von Leuchtmitteln ohne Farbtemperatur oder Farbeffekten (Alternativ kann auch Socket verwendet werden)**.  

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **Licht** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/191105077-428ba7d0-f62f-43e4-a829-ba42f260d727.png)
 
Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:  
![image](https://user-images.githubusercontent.com/102996011/191105279-aae89e95-cb4f-46d1-91b9-0fcd7e1385c2.png)

***

### Medien - cardMedia
Der Alias-Medien für die cardMedia lässt sich mit dem Geräte-Manager nicht erstellen. Auch mit dem Alias-Manager unter "Automatisch erstellen" aus einem Player-Pfad ist das je nach Adapter eher eine Zufallsproduktion.  
> Es gibt von britzelpuf bereits einen noch offenen github-Issue: https://github.com/ioBroker/ioBroker.devices/issues/152 seit dem 17.03.2022  

Der Alias gibt aktuell nur einen .ACTUAL her. Das ist jedoch für einen Media-Player definitiv zu wenig.  

> **Daher bitte eines der nachfolgenden Skripte (je eingesetzten Adaptertyp) nutzen. In der Javascript Instanz muss "Kommando SetObject erlauben" aktiviert werden. Die Struktur sieht im Gerätemanager danach etwa so aus und sollte vernachlässigt werden, da der ALIAS dennoch funktioniert!**  

![image](https://user-images.githubusercontent.com/102996011/189842715-75f9d554-3395-42f6-903b-b92b0828143c.png)
Obwohl das alles Aliase vom Typ Medien sind, sehen bis auf zwei alle anderen nicht korrekt aus, sind aber in der Objektstruktur korrekt und funktionieren auch mit dem NSPanel

#### Spotify-Premium-Adapter  
**Skript zum Anlegen eines Spotify-Premium - media-Alias (ab Version 3.3.2)**

![image](https://user-images.githubusercontent.com/102996011/189699416-70ca5726-5bd5-49ca-9771-d9d0f41fb414.png)

<details>
  <summary><b>Spoiler:</b> JavaScript Code für Erstellung eines Spotify-Premium-Alias</summary>

```
const aliasPath = 'alias.0.NSPanel_1.Media';
const aliasDevice = 'PlayerSpotifyPremium';
//Ergibt alias.0.NSPanel_1.Media.PlayerSpotifyPremium.

const spotifyPremiumInstanz = 'spotify-premium.0.'; //Falls abweichende Instanznummer, bitte ändern


var typeAlias, read, write, nameAlias, role, desc, min, max, unit, states, custom;

function createAlias(idDst, idName,idSrc, idRd, idType, idRole, idAliasType) {
  if(existsState(idDst)) log(idDst + ' schon vorhanden !', 'warn');
  else {
     var obj = {};
     obj.type = idType;
     obj.common = getObject(idSrc).common;
     obj.common.alias = {};
     if(idRd) {
         obj.common.alias.id = {};
         obj.common.alias.id.read = idRd;
         obj.common.alias.id.write = idSrc;
         obj.common.read = true;
     } else obj.common.alias.id = idSrc;
     obj.common.type = idAliasType;
     if(obj.common.read !== false && read) obj.common.alias.read = read;
     if(obj.common.write !== false && write) obj.common.alias.write = write;
     obj.common.name = idName;
     obj.common.role = idRole;
     obj.common.desc = idDst;
     if(min !== undefined) obj.common.min = min;
     if(max !== undefined) obj.common.max = max;
     if(unit) obj.common.unit = unit;
     obj.common.states = states;
     if(custom && obj.common.custom) obj.common.custom = custom;
     obj.native = {};
     setObject(idDst, obj);
  } 
}

createAlias(aliasPath + '.' + aliasDevice, '', spotifyPremiumInstanz + 'player', '', 'channel', 'media', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.ALBUM', 'ALBUM',  spotifyPremiumInstanz + 'player.album', '', 'state', 'media.album', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.ARTIST', 'ARTIST', spotifyPremiumInstanz + 'player.artistName', '', 'state', 'media.artist', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.TITLE', 'TITLE', spotifyPremiumInstanz + 'player.trackName', '', 'state', 'media.title', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.CONTEXT_DESCRIPTION', 'CONTEXT_DESCRIPTION', spotifyPremiumInstanz + 'player.contextDescription', '', 'state', 'media.station', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.NEXT', 'NEXT', spotifyPremiumInstanz + 'player.skipPlus', '', 'state', 'button.next', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PREV', 'PREV', spotifyPremiumInstanz + 'player.skipMinus', '', 'state', 'button.prev', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PLAY', 'PLAY', spotifyPremiumInstanz + 'player.play', '', 'state', 'button.play', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PAUSE', 'PAUSE', spotifyPremiumInstanz + 'player.pause', '', 'state', 'button.pause', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.STOP', 'STOP', spotifyPremiumInstanz + 'player.pause', '', 'state', 'button.stop', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.STATE', 'STATE', spotifyPremiumInstanz + 'player.isPlaying', '', 'state', 'media.state', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.VOLUME', 'VOLUME', spotifyPremiumInstanz + 'player.volume', '', 'state', 'level.volume', 'number');
createAlias(aliasPath + '.' + aliasDevice + '.VOLUME_ACTUAL', 'VOLUME_ACTUAL', spotifyPremiumInstanz + 'player.volume', '', 'state', 'value.volume', 'number');
```
</details> 

> Anleitung:  
> * Neues Skript (JavaScript JS) anlegen   
> * Code kopieren und einfügen  
> * Skript aktivieren und ausführen  
> * Danach wieder Deaktivieren  

![image](https://user-images.githubusercontent.com/102996011/189696453-9b04a453-24c1-4ad1-9224-3dc1f214b0a5.png)  
#### Alexa2-Adapter
**Skript zum Anlegen eines Alexa2 - media-Alias**

![image](https://user-images.githubusercontent.com/102996011/189757236-0106ed14-d634-4f64-bb07-697ae4d70188.png)

<details>
  <summary><b>Spoiler:</b> JavaScript Code für Erstellung eines Alexa2-Alias</summary>

```
const aliasPath = 'alias.0.NSPanel_1.Media';
const aliasDevice = 'PlayerAlexa2';
//Ergibt alias.0.NSPanel_1.Media.PlayerAlexa2.

const alexaInstanz = 'alexa2.0.Echo-Devices.';
const alexaDevice = 'G0XXXXXXXXXXXXXXXX'; //!!! Anpassen !!! Seriennummer des Primär Device (Kann auch Gruppe sein)

var typeAlias, read, write, nameAlias, role, desc, min, max, unit, states, custom;

function createAlias(idDst, idName,idSrc, idRd, idType, idRole, idAliasType) {
  if(existsState(idDst)) log(idDst + ' schon vorhanden !', 'warn');
  else {
     var obj = {};
     obj.type = idType;
     obj.common = getObject(idSrc).common;
     obj.common.alias = {};
     if(idRd) {
         obj.common.alias.id = {};
         obj.common.alias.id.read = idRd;
         obj.common.alias.id.write = idSrc;
         obj.common.read = true;
     } else obj.common.alias.id = idSrc;
     obj.common.type = idAliasType;
     if(obj.common.read !== false && read) obj.common.alias.read = read;
     if(obj.common.write !== false && write) obj.common.alias.write = write;
     obj.common.name = idName;
     obj.common.role = idRole;
     obj.common.desc = idDst;
     if(min !== undefined) obj.common.min = min;
     if(max !== undefined) obj.common.max = max;
     if(unit) obj.common.unit = unit;
     obj.common.states = states;
     if(custom && obj.common.custom) obj.common.custom = custom;
     obj.native = {};
     setObject(idDst, obj);
  } 
}

createAlias(aliasPath + '.' + aliasDevice, '', alexaInstanz + alexaDevice, '', 'channel', 'media', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.ALBUM', 'ALBUM',  alexaInstanz + alexaDevice + '.Player.currentAlbum', '', 'state', 'media.album', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.ARTIST', 'ARTIST', alexaInstanz + alexaDevice + '.Player.currentArtist', '', 'state', 'media.artist', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.TITLE', 'TITLE', alexaInstanz + alexaDevice + '.Player.currentTitle', '', 'state', 'media.title', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.NEXT', 'NEXT', alexaInstanz + alexaDevice + '.Player.controlNext', '', 'state', 'button.next', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PREV', 'PREV', alexaInstanz + alexaDevice + '.Player.controlPrevious', '', 'state', 'button.prev', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PLAY', 'PLAY', alexaInstanz + alexaDevice + '.Player.controlPlay', '', 'state', 'button.play', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PAUSE', 'PAUSE', alexaInstanz + alexaDevice + '.Player.controlPause', '', 'state', 'button.pause', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.STOP', 'STOP', alexaInstanz + alexaDevice + '.Commands.deviceStop', '', 'state', 'button.stop', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.STATE', 'STATE', alexaInstanz + alexaDevice + '.Player.currentState', '', 'state', 'media.state', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.VOLUME', 'VOLUME', alexaInstanz + alexaDevice + '.Player.volume', '', 'state', 'level.volume', 'number');
createAlias(aliasPath + '.' + aliasDevice + '.VOLUME_ACTUAL', 'VOLUME_ACTUAL', alexaInstanz + alexaDevice + '.Player.volume', '', 'state', 'value.volume', 'number');
```
</details> 

> Anleitung:  
> * Neues Skript (JavaScript JS) anlegen   
> * Code kopieren und einfügen  
> * Skript aktivieren und ausführen  
> * Danach wieder Deaktivieren  

![image](https://user-images.githubusercontent.com/102996011/189696453-9b04a453-24c1-4ad1-9224-3dc1f214b0a5.png)  


#### Sonos-Adpter
**Skript zum Anlegen eines Sonos - media-Alias (ab Version 3.3.2)**

![image](https://user-images.githubusercontent.com/102996011/189748619-02961946-c9e1-42d4-90fc-54d8344b87e3.png)


<details>
  <summary><b>Spoiler:</b> JavaScript Code für Erstellung eines Sonos-Alias</summary>

```
const aliasPath = 'alias.0.NSPanel_1.Media';
const aliasDevice = 'PlayerSonos';
//Ergibt alias.0.NSPanel_1.Media.PlayerSonos.

const sonosInstanz = 'sonos.0.root.';
const sonosIP = '192_168_1_212';

var typeAlias, read, write, nameAlias, role, desc, min, max, unit, states, custom;

function createAlias(idDst, idName,idSrc, idRd, idType, idRole, idAliasType) {
  if(existsState(idDst)) log(idDst + ' schon vorhanden !', 'warn');
  else {
     var obj = {};
     obj.type = idType;
     obj.common = getObject(idSrc).common;
     obj.common.alias = {};
     if(idRd) {
         obj.common.alias.id = {};
         obj.common.alias.id.read = idRd;
         obj.common.alias.id.write = idSrc;
         obj.common.read = true;
     } else obj.common.alias.id = idSrc;
     obj.common.type = idAliasType;
     if(obj.common.read !== false && read) obj.common.alias.read = read;
     if(obj.common.write !== false && write) obj.common.alias.write = write;
     obj.common.name = idName;
     obj.common.role = idRole;
     obj.common.desc = idDst;
     if(min !== undefined) obj.common.min = min;
     if(max !== undefined) obj.common.max = max;
     if(unit) obj.common.unit = unit;
     obj.common.states = states;
     if(custom && obj.common.custom) obj.common.custom = custom;
     obj.native = {};
     setObject(idDst, obj);
  } 
}

createAlias(aliasPath + '.' + aliasDevice, '', sonosInstanz + sonosIP, '', 'channel', 'media', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.ALBUM', 'ALBUM',  sonosInstanz + sonosIP + '.current_album', '', 'state', 'media.album', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.ARTIST', 'ARTIST', sonosInstanz + sonosIP + '.current_artist', '', 'state', 'media.artist', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.TITLE', 'TITLE', sonosInstanz + sonosIP + '.current_title', '', 'state', 'media.title', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.CONTEXT_DESCRIPTION', 'CONTEXT_DESCRIPTION', sonosInstanz + sonosIP + '.current_station', '', 'state', 'media.station', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.NEXT', 'NEXT', sonosInstanz + sonosIP + '.next', '', 'state', 'button.next', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PREV', 'PREV', sonosInstanz + sonosIP + '.prev', '', 'state', 'button.prev', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PLAY', 'PLAY', sonosInstanz + sonosIP + '.play', '', 'state', 'button.play', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PAUSE', 'PAUSE', sonosInstanz + sonosIP + '.pause', '', 'state', 'button.pause', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.STOP', 'STOP', sonosInstanz + sonosIP + '.stop', '', 'state', 'button.stop', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.STATE', 'STATE', sonosInstanz + sonosIP + '.state_simple', '', 'state', 'media.state', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.VOLUME', 'VOLUME', sonosInstanz + sonosIP + '.volume', '', 'state', 'level.volume', 'number');
createAlias(aliasPath + '.' + aliasDevice + '.VOLUME_ACTUAL', 'VOLUME_ACTUAL', sonosInstanz + sonosIP + '.volume', '', 'state', 'value.volume', 'number');
```
</details> 

> Anleitung:  
> * Neues Skript (JavaScript JS) anlegen   
> * Code kopieren und einfügen  
> * Skript aktivieren und ausführen  
> * Danach wieder Deaktivieren  
 
![image](https://user-images.githubusercontent.com/102996011/189696453-9b04a453-24c1-4ad1-9224-3dc1f214b0a5.png)  
#### Chromecast-Adpter (Google home)
**Skript zum Anlegen eines Chromecast - media-Alias (ab Version 3.3.2)**

<details>
  <summary><b>Spoiler:</b> JavaScript Code für Erstellung eines Chrome-Alias</summary>

```
const aliasPath = 'alias.0.NSPanel_1.Media';  // ggfs. Anpassen
const aliasDevice = 'PlayerChromecast';       // ggfs. Anpassen
//Ergibt alias.0.NSPanel_1.Media.PlayerChromecast.

const chromecastInstanz = 'chromecast.0.'; // Anpasssen, wenn nicht Instanz 0
const chromecastDevice = 'GoogleHome3224'; // Anpassen an dein eigenes Devoice

var typeAlias, read, write, nameAlias, role, desc, min, max, unit, states, custom;

function createAlias(idDst, idName,idSrc, idRd, idType, idRole, idAliasType) {
  if(existsState(idDst)) log(idDst + ' schon vorhanden !', 'warn');
  else {
     var obj = {};
     obj.type = idType;
     obj.common = getObject(idSrc).common;
     obj.common.alias = {};
     if(idRd) {
         obj.common.alias.id = {};
         obj.common.alias.id.read = idRd;
         obj.common.alias.id.write = idSrc;
         obj.common.read = true;
     } else obj.common.alias.id = idSrc;
     obj.common.type = idAliasType;
     if(obj.common.read !== false && read) obj.common.alias.read = read;
     if(obj.common.write !== false && write) obj.common.alias.write = write;
     obj.common.name = idName;
     obj.common.role = idRole;
     obj.common.desc = idDst;
     if(min !== undefined) obj.common.min = min;
     if(max !== undefined) obj.common.max = max;
     if(unit) obj.common.unit = unit;
     obj.common.states = states;
     if(custom && obj.common.custom) obj.common.custom = custom;
     obj.native = {};
     setObject(idDst, obj);
  } 
}

createAlias(aliasPath + '.' + aliasDevice, '', chromecastInstanz + chromecastDevice, '', 'channel', 'media', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.ALBUM', 'ALBUM',  chromecastInstanz + chromecastDevice + '.album', '', 'state', 'media.album', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.ARTIST', 'ARTIST', chromecastInstanz + chromecastDevice + '.artist', '', 'state', 'media.artist', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.TITLE', 'TITLE', chromecastInstanz + chromecastDevice + '.title', '', 'state', 'media.title', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.NEXT', 'NEXT', chromecastInstanz + chromecastDevice + '.next', '', 'state', 'button.next', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PREV', 'PREV', chromecastInstanz + chromecastDevice + '.prev', '', 'state', 'button.prev', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PLAY', 'PLAY', chromecastInstanz + chromecastDevice + '.play', '', 'state', 'button.play', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PAUSE', 'PAUSE', chromecastInstanz + chromecastDevice + '.pause', '', 'state', 'button.pause', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.STOP', 'STOP', chromecastInstanz + chromecastDevice + '.stop', '', 'state', 'button.stop', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.STATE', 'STATE', chromecastInstanz + chromecastDevice + '.state', '', 'state', 'media.state', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.VOLUME', 'VOLUME', chromecastInstanz + chromecastDevice + '.volume', '', 'state', 'level.volume', 'number');
createAlias(aliasPath + '.' + aliasDevice + '.VOLUME_ACTUAL', 'VOLUME_ACTUAL', chromecastInstanz + chromecastDevice + '.volume', '', 'state', 'value.volume', 'number');
```
</details> 

> Anleitung:  
> * Neues Skript (JavaScript JS) anlegen   
> * Code kopieren und einfügen  
> * Skript aktivieren und ausführen  
> * Danach wieder Deaktivieren  

***

![image](https://user-images.githubusercontent.com/102996011/189696453-9b04a453-24c1-4ad1-9224-3dc1f214b0a5.png)  

#### Logitech SqueezeBoxRPC-Adapter
**Skript zum Anlegen eines SqueezeBoxRPC - media-Alias (ab Version 3.4.0.6)**

![image](https://user-images.githubusercontent.com/102996011/194286414-a1635626-d33b-4cc6-b8e6-1c1749636900.png)

<details>
  <summary><b>Spoiler:</b> JavaScript Code für Erstellung eines SqueezeBoxRPC -Alias</summary>

```
const aliasPath = 'alias.0.Media.LMS';  // ggfs. Anpassen
const aliasDevice = 'SqueezePlay';       // ggfs. Anpassen
//Ergibt alias.0.NSPanel_1.Media.SqueezeBoxRPC

const squeezeBoxInstanz = 'squeezeboxrpc.0.Players.'; // Anpasssen, wenn nicht Instanz 0
const squeezeBoxDevice = 'SqueezePlay'; // Anpassen an dein eigenes Device

var typeAlias, read, write, nameAlias, role, desc, min, max, unit, states, custom;

function createAlias(idDst, idName,idSrc, idRd, idType, idRole, idAliasType) {
  if(existsState(idDst)) log(idDst + ' schon vorhanden !', 'warn');
  else {
     var obj = {};
     obj.type = idType;
     obj.common = getObject(idSrc).common
     obj.common.alias = {};
     if(idRd) {
         obj.common.alias.id = {};
         obj.common.alias.id.read = idRd;
         obj.common.alias.id.write = idSrc;
         obj.common.read = true;
     } else {
         obj.common.alias.id = idSrc;
     }
     obj.common.type = idAliasType;
     if(obj.common.read !== false && read) obj.common.alias.read = read;
     if(obj.common.write !== false && write) obj.common.alias.write = write;
     obj.common.name = idName;
     obj.common.role = idRole;
     obj.common.desc = idDst;
     if(min !== undefined) obj.common.min = min;
     if(max !== undefined) obj.common.max = max;
     if(unit) obj.common.unit = unit;
     obj.common.states = states;
     if(custom && obj.common.custom) obj.common.custom = custom;
     obj.native = {};
     setObject(idDst, obj);
  } 
}

createAlias(aliasPath + '.' + aliasDevice + '.ALBUM', 'ALBUM',  squeezeBoxInstanz + squeezeBoxDevice + '.Album', '', 'state', 'media.album', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.ARTIST', 'ARTIST', squeezeBoxInstanz + squeezeBoxDevice + '.Artist', '', 'state', 'media.artist', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.TITLE', 'TITLE', squeezeBoxInstanz + squeezeBoxDevice + '.Title', '', 'state', 'media.title', 'string');
createAlias(aliasPath + '.' + aliasDevice + '.NEXT', 'NEXT', squeezeBoxInstanz + squeezeBoxDevice + '.btnForward', '', 'state', 'button.forward', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PREV', 'PREV', squeezeBoxInstanz + squeezeBoxDevice + '.btnRewind', '', 'state', 'button.reverse', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PLAY', 'PLAY', squeezeBoxInstanz + squeezeBoxDevice + '.state', '', 'state', 'media.state', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.PAUSE', 'PAUSE', squeezeBoxInstanz + squeezeBoxDevice + '.state', '', 'state', 'media.state', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.STOP', 'STOP', squeezeBoxInstanz + squeezeBoxDevice + '.state', '', 'state', 'media.state', 'boolean');
createAlias(aliasPath + '.' + aliasDevice + '.STATE', 'STATE', squeezeBoxInstanz + squeezeBoxDevice + '.Power', '', 'state', 'switch', 'number');
createAlias(aliasPath + '.' + aliasDevice + '.VOLUME', 'VOLUME', squeezeBoxInstanz + squeezeBoxDevice + '.Volume', '', 'state', 'level.volume', 'number');
createAlias(aliasPath + '.' + aliasDevice + '.VOLUME_ACTUAL', 'VOLUME_ACTUAL', squeezeBoxInstanz + squeezeBoxDevice + '.Volume', '', 'state', 'value.volume', 'number');
```
</details> 

> Anleitung:  
> * Neues Skript (JavaScript JS) anlegen   
> * Code kopieren und einfügen  
> * Skript aktivieren und ausführen  
> * Danach wieder Deaktivieren  

Jetzt kommt der spezielle Teil für diesen Adapter. Hierfür sind noch weitere Einstellungen erforderlich:  
* Alias Manager öffnen, den neu erstellten Alias auswählen und unter "common.role" **media** eingeben  
![image](https://user-images.githubusercontent.com/102996011/194288676-c329fa66-8a87-4d07-bc44-91367a334b5f.png)  

![image](https://user-images.githubusercontent.com/102996011/194288476-38251d04-3656-44bc-b4d3-bb43f42f4ae2.png)  

* unter Objekte zu den Aliasen (alias.0.) gehen:  
![image](https://user-images.githubusercontent.com/102996011/194288944-f30822c7-c911-480d-a93a-8b9e8e71dbe0.png)  
![image](https://user-images.githubusercontent.com/102996011/194289119-175acf67-4136-48ac-935c-984ce72e740b.png)  
Bei **PAUSE **und **PLAY **mit dem Stiftsymbol am Ende der Zeile den Dialog aufschalten und 3. Tab Alias die Konvertierungsfunktionen einschalten und analog der nachfolgenden Bilder anpassen (Konverter beim Lesen):  
![image](https://user-images.githubusercontent.com/102996011/194289939-8ae781cb-deb0-4205-9f7a-30f282ee1510.png)  
![image](https://user-images.githubusercontent.com/102996011/194290059-fc28e452-fa49-47d3-9b4d-729ee48a66e7.png)  

Jetzt sollte der spueezeboxrpc korrekt arbeiten  
 
![image](https://user-images.githubusercontent.com/102996011/189696453-9b04a453-24c1-4ad1-9224-3dc1f214b0a5.png)  


### RGB-Licht (channel rgb)

![image](https://user-images.githubusercontent.com/102996011/191094426-3c86ce5a-3d95-4e95-ba68-aefb09a6e9c3.png)

> Der Alias RGB-Licht wird verwendet, wenn als Color Datenpunkte **RED, GREEN, BLUE und WHITE** vorliegen

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **RGB-Licht** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/191094851-cbd29a38-1cb7-400f-89b4-c647ca1f03eb.png)  
![image](https://user-images.githubusercontent.com/102996011/191094933-317204e0-01ab-43eb-83ab-c2efce8bbb91.png)
> Für das Beispiel standen leider keine echten Adapter-Datenpunkte zur Verfügung, daher die Darstellung in 0_userdata.0...

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:
![image](https://user-images.githubusercontent.com/102996011/191095305-86bbdbdd-220d-4f9a-a85f-b74cf934f422.png)  

Das zugehörige PageItem im TypeScript:  
![image](https://user-images.githubusercontent.com/102996011/191095621-cb705027-32ae-4443-b21a-913dfcd9663b.png)  

**Parameter:**  
name: Vom Alias abweichender Name  
offColor: abweichende Farbe für aus  
onColor: abweichende Farbe für an  
minValueBrightness: Minimale Helligkeit (Default 0)  
maxValueBrightness: Minimale Maxiamale Helligkeit (Default 100)
minValueColorTemp: Minimale Farbtemperatur je nach Leuchtmittel/Adapter (z.B. 500K) 
maxValueColorTemp: Maximale Farbtemperatur je nach Leuchtmittel/Adapter (z.B. 6500K)
interpolateColor: Errechnet den Farbton und weist diesen dem Icon zu (Beispiel Pink)

Mit klick auf den Bezeichner wird das popUpLight aufgeschaltet:
![image](https://user-images.githubusercontent.com/102996011/191096635-91bdab6c-e88f-459a-9699-9d2e6804c86a.png)  

![image](https://user-images.githubusercontent.com/102996011/191096702-a0b2c5a2-f19e-4e61-9831-09b88b589332.png)  

***

### RGB-Licht-einzeln (channel rgbSingle)

![image](https://user-images.githubusercontent.com/102996011/191097789-1ffe592e-6316-4311-87cc-e0f0ed41a8ef.png)

> Der Alias RGB-Licht wird verwendet, wenn als **Color Datenpunkt (RGB) im Hexadezimal-Format (z.B. #7dff7e)** vorliegt.

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **RGB-Licht** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/191098059-280232ca-5d69-432e-a32d-f85984ce68f7.png)  
> Für das Beispiel standen leider keine echten Adapter-Datenpunkte zur Verfügung, daher die Darstellung in 0_userdata.0...

Alternativ kann dieser Alias auch via CIE, d.h über den XY Parameter (z.B. beim deConz-Adapter) gesteuert werden:  
![image](https://user-images.githubusercontent.com/102996011/191099845-2d9364a1-52db-40c1-9e83-876a1a251e41.png)  

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:
![image](https://user-images.githubusercontent.com/102996011/191097931-113a507e-e52a-4a6f-a695-6e5eedb2d383.png)

Das zugehörige PageItem im TypeScript:  
![image](https://user-images.githubusercontent.com/102996011/191098487-bd09249b-56a2-4253-b6f3-74b21f8a20f5.png)  

**Parameter:**  
name: Vom Alias abweichender Name  
offColor: abweichende Farbe für aus  
onColor: abweichende Farbe für an  
minValueBrightness: Minimale Helligkeit (Default 0)  
maxValueBrightness: Minimale Maxiamale Helligkeit (Default 100)
minValueColorTemp: Minimale Farbtemperatur je nach Leuchtmittel/Adapter (z.B. 500K) 
maxValueColorTemp: Maximale Farbtemperatur je nach Leuchtmittel/Adapter (z.B. 6500K)
interpolateColor: Errechnet den Farbton und weist diesen dem Icon zu (Beispiel Grün)
colormode: "xy" oder "rgb" (default) zur Steuerung der CIE XY Color-Datenpunkte

Mit klick auf den Bezeichner wird das popUpLight aufgeschaltet:
![image](https://user-images.githubusercontent.com/102996011/191096635-91bdab6c-e88f-459a-9699-9d2e6804c86a.png)  

![image](https://user-images.githubusercontent.com/102996011/191096702-a0b2c5a2-f19e-4e61-9831-09b88b589332.png) 

***

### Schieberegler (channel slider)
![image](https://user-images.githubusercontent.com/102996011/191107077-4ad6e4e8-7b59-4427-9a69-25a4ef3c755d.png)

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **Schieberegler** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/191345106-68981bc1-f083-4a35-b0b9-3fc46fe459b5.png)  
 
Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:  
![image](https://user-images.githubusercontent.com/102996011/191345261-2f138190-2de3-4bef-80ba-d1c24833619b.png)  

Das zugehörige PageItem im TypeScript:  
`<PageItem>{ id: "alias.0.NSPanel_1.Dimmode_BrightnessDay", name: "Brightness Tag", icon: "brightness-5", offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 5, maxValue: 10}`  

**Parameter:**  
name: Vom Alias abweichender Name  
offColor: abweichende Farbe für aus  
onColor: abweichende Farbe für an  
icon: zu visualisierendes Icon  
minValue: Minimaler Sliderwert  
maxValue: Maximaler Sliderwert  
usecolor:  

***

### Steckdose (channel socket)  

![image](https://user-images.githubusercontent.com/102996011/191107198-298d0b94-dcc2-49f9-bcbb-92b926c7ae3a.png)  

> Alternativ kann der Alias Licht verwendet werden!

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **Steckdose** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/191347586-e04414dd-7a87-4821-9c31-913874f9a5c3.png)  
 
Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:  
![image](https://user-images.githubusercontent.com/102996011/191347855-92667d50-93ce-46fe-9d4a-3fb26bc99db2.png)  

Das zugehörige PageItem im TypeScript:  
`<PageItem>{ id: "alias.0.NSPanel_1.Luftreiniger", icon: "power", icon2: "power",offColor: MSRed, onColor: MSGreen}`  

**Parameter:**  
name: Vom Alias abweichender Name  
offColor: abweichende Farbe für aus  
onColor: abweichende Farbe für an  
icon: zu visualisierendes Icon für On  
icon2: zu visualisierendes Icon für Off


***

### Taste (channel button)

![image](https://user-images.githubusercontent.com/102996011/189404781-7fe9c2b0-e81d-446f-9aab-50865cc39a40.png)  

> Beschreibung für den Alias Taste folgt...

***

### Tastensensor (channel buttonSensor)

> Beschreibung für den Alias Tastensenso folgt...

***

### Temperatur (channel temperature)

![image](https://user-images.githubusercontent.com/102996011/189403527-4a94e690-9a5d-4121-8dcb-5636951a7df6.png)

> Beschreibung für den Alias Temperatur folgt...

***

### Thermostat - cardThermo - (channel thermostat)
![image](https://user-images.githubusercontent.com/102996011/191052850-06276337-1000-4eb6-b010-5f6d49fd0e24.png)

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **Thermostat** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  

![image](https://user-images.githubusercontent.com/102996011/191053643-75545e7e-995e-4a28-88c3-87268dcbb44d.png)  

Im unteren Teil können ebenfalls Indikatoren eingeblendet werden:  
![image](https://user-images.githubusercontent.com/102996011/191338688-e5cf4b91-2385-4f09-8523-e52ed797b9be.png)  
z.B.  
![image](https://user-images.githubusercontent.com/102996011/191054046-4d3279f1-6dc8-484d-b70f-9dd65ae9929b.png)  
oder  
![image](https://user-images.githubusercontent.com/102996011/191054242-dc679425-592e-490a-9383-73030a9e20e5.png)  
etc.  

Wenn der Thermostat über Mode verfügt und dieser auch genutzt werden soll:  
![image](https://user-images.githubusercontent.com/102996011/191054557-89060dca-825a-4d38-b756-c67eb2fbe7ea.png)  

Mode wird über externe Datenpunkte gesteuert. Hierzu legst du dir unter 0_userdate.0. einen Ordner deiner Wahl an. In diesem Ordner können jetzt bis zu 5 Datenpunkte (Alle vom Typ boolean (true/false)) angelegt werden:
* AUTOMATIC  
* MANUAL  
* PARTY  
* VACATION  
* BOOST  

Im Alias können "BOOST" und "PARTY" (sofern gewünscht) bereits den neu erstellten Datenpunkten zugewiesen werden:  
![image](https://user-images.githubusercontent.com/102996011/191055917-bf05d8a1-fc3f-4c4e-a4a8-da5aafcf1317.png)  

Die Datenpunkte AUTOMATIC, MANUAL und VACATION können nicht sofort zugewiesen werden, da die ALIAS-Definition diese Objekte nicht vorsieht. In diesem Fall kannst du diese selbst hinzufügen und im Anschluss deine erstellten Datenpunkten zuordnen:  
![image](https://user-images.githubusercontent.com/102996011/191056534-c33656e6-178c-4f95-a47a-4c609f5236f1.png)  

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:
![image](https://user-images.githubusercontent.com/102996011/191056980-98c196cf-7991-4d33-978b-b19b31403477.png)  

> Es müssen nicht alle 5 Modi vorhanden sein. Das Skript liest die vorhandenen Modi ein und verarbeitet auch nur diese  

> Insgesamt stehen Icons im unteren Bereich zur Verfügung. Somit ist es nicht möglich 5 Modi-Icons und 7 Indikatoren-Icons gleichzeitig zu visualisieren. Die Modi (falls im Alias definiert) werden zuerst visualisiert (vorne) und dann, falls verfügbar mit Indikatoren (sofern im Alias definiert) auf insgesamt 8 Icons aufgefüllt.

Das zugehörige PageItem im TypeScript:  
![image](https://user-images.githubusercontent.com/102996011/191057213-18660084-dd69-4af9-9cfd-c677002eb017.png)

**Parameter:**  
name: Vom Alias abweichender Name  
minValue: Minimaltemperatur Beispiel 5°C = 50  
maxValue: Minimaltemperatur Beispiel 30°C = 300  

***

### Timer - popUpTimer - (level.timer)  
  
> Ab Release 3.7.0
  
![image](https://user-images.githubusercontent.com/102996011/208918067-65174b22-a7b6-4a81-a11b-cdca44c947e2.png)  
  
![image](https://user-images.githubusercontent.com/102996011/208920490-e000b054-dc6b-4583-a501-0c684a9de43f.png)  
![image](https://user-images.githubusercontent.com/102996011/208920708-4dac1e8f-9e21-4809-b5d8-e5f1a03fb048.png)  
  

Für den Timer (Stopp-Uhr) gibt es weder im Geräte-Manager, noch im Alias-Manager einen vorgefertigten ALIAS Gerätetypen. Daher muss dieser eigenhändig erstellt werden.

Objekte
![image](https://user-images.githubusercontent.com/102996011/208917886-2c84cb2c-dee6-456d-8222-1a76f0cb3782.png)  

Der Timer greift auf selbsterstellte Datenpunkte zurück, welche (analog Beispiel) wie folgt angelegt werden müssen.

* 0_userdata.0...Timer_1.ACTUAL --> number --> Nimmt die eingestellte Zeit aus dem NSPanel in Sekunden auf und wird bei Ausführung durch das externe Script dekrementiert.
* 0_userdata.0...Timer_1.STATE --> string --> Erhält den Status vom Blockly und vom NSPanel
Blockly
![image](https://user-images.githubusercontent.com/102996011/208922045-9bd46a61-4c8a-490b-b999-5e12dc911854.png)

<details>
  <summary>Blockly</summary>
```
<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="QPiqoyWT$%Cp)OZ=|`*W">vSTATE</variable>
    <variable id="!E]!o]+#iwtI}R=X+,zV">vACTUAL</variable>
    <variable id="#BYGZV@hvwAL/]L2%/8w">sec_timer</variable>
    <variable type="interval" id="Intervall">Intervall</variable>
  </variables>
  <block type="variables_set" id="XV2H4i,jWn`z+)|k#NJw" x="38" y="-263">
    <field name="VAR" id="QPiqoyWT$%Cp)OZ=|`*W">vSTATE</field>
    <value name="VALUE">
      <block type="text" id="r,7fA;o:e.|28/,@0]JH">
        <field name="TEXT">0_userdata.0.Timer.NSPanel.1.Countdown.Zustand</field>
      </block>
    </value>
    <next>
      <block type="variables_set" id="r4Cw8qj}45yA4j7D(^B-">
        <field name="VAR" id="!E]!o]+#iwtI}R=X+,zV">vACTUAL</field>
        <value name="VALUE">
          <block type="text" id="nRXWb#VRyJS5cXNbhq0y">
            <field name="TEXT">0_userdata.0.Timer.NSPanel.1.Countdown.Sekunden</field>
          </block>
        </value>
        <next>
          <block type="variables_set" id="57{xGHam)5G*~)???W)5">
            <field name="VAR" id="#BYGZV@hvwAL/]L2%/8w">sec_timer</field>
            <value name="VALUE">
              <block type="get_value_var" id="s9stp?b253SRZwZo*b`t">
                <field name="ATTR">val</field>
                <value name="OID">
                  <shadow type="text" id="K,Lb1bBP41R.OE[NS)i1">
                    <field name="TEXT"></field>
                  </shadow>
                  <block type="variables_get" id="uqn`Azeg-~BoGAP`6l7c">
                    <field name="VAR" id="!E]!o]+#iwtI}R=X+,zV">vACTUAL</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="on_ext" id="KTTXX_aR/l#vo.Oy!god">
                <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                <field name="CONDITION">ne</field>
                <field name="ACK_CONDITION"></field>
                <value name="OID0">
                  <shadow type="field_oid" id="[~]6MakRk81y;6T=D#E1">
                    <field name="oid">default</field>
                  </shadow>
                  <block type="text" id="99{OsQ*le2{H2clp=,[^">
                    <field name="TEXT">0_userdata.0.Timer.NSPanel.1.Countdown.Zustand</field>
                  </block>
                </value>
                <statement name="STATEMENT">
                  <block type="logic_switch_case" id="*DcmKGH^MzH`@|}$)`Vi">
                    <mutation xmlns="http://www.w3.org/1999/xhtml" default="1"></mutation>
                    <value name="CONDITION">
                      <block type="on_source" id="Kv#`7##ZlSfAaV9U*YlU">
                        <field name="ATTR">state.val</field>
                      </block>
                    </value>
                    <value name="CASECONDITION0">
                      <block type="text" id="jSK+-X9^LZ52;FZkF{N@">
                        <field name="TEXT">active</field>
                      </block>
                    </value>
                    <statement name="CASE0">
                      <block type="timeouts_clearinterval" id="H1?KT2GS=;m|lB4B[d9{">
                        <field name="NAME">Intervall</field>
                        <next>
                          <block type="timeouts_setinterval" id="OCAffLYx5xl2^)mb:1ON">
                            <field name="NAME">Intervall</field>
                            <field name="INTERVAL">1000</field>
                            <field name="UNIT">ms</field>
                            <statement name="STATEMENT">
                              <block type="controls_if" id="M:$D10b:c^VB7N-[zAAs">
                                <mutation else="1"></mutation>
                                <value name="IF0">
                                  <block type="logic_compare" id="Y%K:Fww+C*D)mW_pAvb5" inline="false">
                                    <field name="OP">GT</field>
                                    <value name="A">
                                      <block type="get_value_var" id="AkNnDdzS;{lm8`UsDA$a">
                                        <field name="ATTR">val</field>
                                        <value name="OID">
                                          <shadow type="text" id="jvzl]}[mrPTl0ev@@~.i">
                                            <field name="TEXT"></field>
                                          </shadow>
                                          <block type="variables_get" id="0}HonAc*HO)G!?xMBnx]">
                                            <field name="VAR" id="!E]!o]+#iwtI}R=X+,zV">vACTUAL</field>
                                          </block>
                                        </value>
                                      </block>
                                    </value>
                                    <value name="B">
                                      <block type="math_number" id="E}Xx=@{9XDIhj5($(DXz">
                                        <field name="NUM">0</field>
                                      </block>
                                    </value>
                                  </block>
                                </value>
                                <statement name="DO0">
                                  <block type="variables_set" id="[lc#LS]+_y3JU6;*iy/;">
                                    <field name="VAR" id="#BYGZV@hvwAL/]L2%/8w">sec_timer</field>
                                    <value name="VALUE">
                                      <block type="get_value_var" id="()czu@y9l5__t%_~guQ4">
                                        <field name="ATTR">val</field>
                                        <value name="OID">
                                          <shadow type="text" id="O~#Pq`;j8,}OcT/IMc2|">
                                            <field name="TEXT"></field>
                                          </shadow>
                                          <block type="variables_get" id="B0a}HDdI9+PoN,71,$tV">
                                            <field name="VAR" id="!E]!o]+#iwtI}R=X+,zV">vACTUAL</field>
                                          </block>
                                        </value>
                                      </block>
                                    </value>
                                    <next>
                                      <block type="control_ex" id="3I8#ZkQ(OTw*^t6-dpu6" inline="true">
                                        <field name="TYPE">false</field>
                                        <field name="CLEAR_RUNNING">FALSE</field>
                                        <value name="OID">
                                          <shadow type="field_oid" id="YjjD8L[b+^gS7jV^+[Y~">
                                            <field name="oid">Object ID</field>
                                          </shadow>
                                          <block type="variables_get" id="?r6MSEFq,iv61OR]$K6R">
                                            <field name="VAR" id="!E]!o]+#iwtI}R=X+,zV">vACTUAL</field>
                                          </block>
                                        </value>
                                        <value name="VALUE">
                                          <shadow type="logic_boolean" id="G4EZc5H)j2Zdg:=;eu%n">
                                            <field name="BOOL">TRUE</field>
                                          </shadow>
                                          <block type="math_arithmetic" id="0178UKVA@dcT|$46OmJx">
                                            <field name="OP">MINUS</field>
                                            <value name="A">
                                              <shadow type="math_number" id="8Ymex9XyD-+Ouo]MD`8d">
                                                <field name="NUM">1</field>
                                              </shadow>
                                              <block type="variables_get" id="RHFea=Bu!IabYuXBG:EX">
                                                <field name="VAR" id="#BYGZV@hvwAL/]L2%/8w">sec_timer</field>
                                              </block>
                                            </value>
                                            <value name="B">
                                              <shadow type="math_number" id="sejG{?~!bE6~.u.4td%|">
                                                <field name="NUM">1</field>
                                              </shadow>
                                            </value>
                                          </block>
                                        </value>
                                        <value name="DELAY_MS">
                                          <shadow type="math_number" id="k:`kho).[#@/%ye+g.u?">
                                            <field name="NUM">0</field>
                                          </shadow>
                                        </value>
                                      </block>
                                    </next>
                                  </block>
                                </statement>
                                <statement name="ELSE">
                                  <block type="control_ex" id="QsmpsLDys?p|Hy=+M`nA" inline="true">
                                    <field name="TYPE">false</field>
                                    <field name="CLEAR_RUNNING">FALSE</field>
                                    <value name="OID">
                                      <shadow type="field_oid" id=".74}mEqIO9M~:ek5U;R(">
                                        <field name="oid">Object ID</field>
                                      </shadow>
                                      <block type="variables_get" id="f`@kho?65GVY~$;xysw3">
                                        <field name="VAR" id="!E]!o]+#iwtI}R=X+,zV">vACTUAL</field>
                                      </block>
                                    </value>
                                    <value name="VALUE">
                                      <shadow type="logic_boolean" id="hkR7Dc_[$;{L`+JxicRa">
                                        <field name="BOOL">TRUE</field>
                                      </shadow>
                                      <block type="math_number" id="4u6KIhWH@!VZ0*$MD;u7">
                                        <field name="NUM">0</field>
                                      </block>
                                    </value>
                                    <value name="DELAY_MS">
                                      <shadow type="math_number" id="g]^hfC+$vJu[_o`O!8c1">
                                        <field name="NUM">0</field>
                                      </shadow>
                                    </value>
                                    <next>
                                      <block type="control_ex" id="Bk@3kjR?T{Px,8U!3]{w" inline="true">
                                        <field name="TYPE">false</field>
                                        <field name="CLEAR_RUNNING">FALSE</field>
                                        <value name="OID">
                                          <shadow type="field_oid" id="#GVc9+G/u85]l_vcm;zH">
                                            <field name="oid">Object ID</field>
                                          </shadow>
                                          <block type="variables_get" id=":,.Z}O;]8X=;wj%SxO5w">
                                            <field name="VAR" id="QPiqoyWT$%Cp)OZ=|`*W">vSTATE</field>
                                          </block>
                                        </value>
                                        <value name="VALUE">
                                          <shadow type="logic_boolean" id="5ne=aTSnU@7c$CGM9EUC">
                                            <field name="BOOL">TRUE</field>
                                          </shadow>
                                          <block type="text" id="mm{`e;eblljVtUBz2(_!">
                                            <field name="TEXT">idle</field>
                                          </block>
                                        </value>
                                        <value name="DELAY_MS">
                                          <shadow type="math_number" id="/.0#c4XU-@]c!Q{onR2T">
                                            <field name="NUM">0</field>
                                          </shadow>
                                        </value>
                                        <next>
                                          <block type="comment" id="Uvi2,2[ruXRlYD.4c(=^">
                                            <field name="COMMENT">An dieser Stelle kann auch noch eine Meldung an Alexa oder Telegram, etc. erfolgen</field>
                                          </block>
                                        </next>
                                      </block>
                                    </next>
                                  </block>
                                </statement>
                              </block>
                            </statement>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <statement name="ONDEFAULT">
                      <block type="timeouts_clearinterval" id="t*fh0y@^c/W:T/x#PS!g">
                        <field name="NAME">Intervall</field>
                      </block>
                    </statement>
                  </block>
                </statement>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>
```
</details>  
  (Bild & Blockly by @Armilar)  

***

### Tür (channel door)
![image](https://user-images.githubusercontent.com/102996011/189403985-7eed8829-ea85-4785-88f9-610edaeb9485.png)

> Analog Alias Fenster. Im "Schritt 1" wird jedoch der Alias-Gerätetyp Tür gewählt  

***

### Verschluss (channel lock)

![image](https://user-images.githubusercontent.com/102996011/189404088-9a2cd3ea-5c43-4c3f-9bd9-e58eac2e6fd6.png)

> Beschreibung für den Alias Verschluss folgt...

***

### Warnung (channel warning)  

Dieser Alias dient nur der Einbindung des dynamischen Abfallkalenders. Dieser ist hier ausführlich beschrieben:  
https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#4-abfallkalender

![image](https://user-images.githubusercontent.com/102996011/189405183-22b51c18-3b92-44e3-bd84-c23359f2783d.png)

***

### Wettervorhersage

![image](https://user-images.githubusercontent.com/102996011/189405373-8ea44dd3-a073-40e8-8379-faab8a836d12.png)

![image](https://user-images.githubusercontent.com/102996011/189480728-116bd2fb-f23a-4158-85cc-0a9bed85024c.png)
und die Temperatur (etwas tiefer). Weitere Datenpunkte, wie z.B. Min- und Max-Temperatur können ebenfalls verknüpft werden, finden jedoch im TypeScript keine Berücksichtigung.  
![image](https://user-images.githubusercontent.com/102996011/189480739-3d10df44-c7dc-43d2-af0d-58e492579d32.png)
In diesem Fall wird die Temperatur aus einem Datenpunkt einer Wetterstation visualisiert. Es kann natürlich auch ein Datenpunkt mit der aktuellen Außentemperatur aus einem anderen Adapter daswetter.0.xxxxx, accuweather.0.xxxxx, openweathermap.0.xxxxx, etc. ausgewählt werden.

> **Achtung:**  
> **Dieser Alias muss erstellt werden, damit die 4 kleineren Icons (Weather-Forecast und/oder 4 Sensordatenpunkte) im unteren Screensaver visualisiert werden können.**  

***
