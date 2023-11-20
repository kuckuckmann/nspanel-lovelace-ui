  
  
## Step für Step - Anleitung 
Anleitung zur Einrichtung eines Sonoff NSPanel mit Lovelace UI unter ioBroker  
  
![image](https://user-images.githubusercontent.com/102996011/204623453-78d15235-136f-4c7b-96dc-4eeda0dace70.png)  


# **Index**

 **1.)** [ioBroker Voraussetzungen](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#1-voraussetzungen-f%C3%BCr-den-iobroker)  
 **2.)** [NSPanel mit Tasmota flashen](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#2-panel-mit-tasmota-flashen)  
 **3.)** [Berry-Treiber installieren](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#3-berry-treiber-installieren)  
 **4.)** [MQTT (Tasmota) Config](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#4-mqtt-tasmota-config)  
 **5.)** [TFT-Firmware flashen](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#5-tft-firmware-flashen)  
 **6.)** [MQTT (ioBroker) Config](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#6-mqtt-iobroker-config)  
 **7.)** [CustomSend anlegen](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#7-customsend-anlegen)  
 **8.)** [Einstellungen in JS-Adapter Instanz](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#8--einstellungen-in-js-adapter-instanz)  
 **9.)** [Icon "TypeScript" anlegen](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#8--icon-typescript-anlegen)  
 **10.)** [„NSPanelTs.ts“ anlegen](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#9--nspaneltsts-anlegen)  
**11.)** [„NSPanelTs.ts“ konfigurieren](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#9--nspaneltsts-konfigurieren)  
**12.)** [Aliase anlegen](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#11--aliase-anlegen)  
**13.)** [Seitengestaltung](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#12--seitengestaltung) 

## **1.) ioBroker Voraussetzungen**

Für den Betrieb benötigst du „keinen“ ioBroker-lovelace-Adapter. Die komplette lovelace-Integration erfolgt über die TFT-Firmware und die nachfolgenden ioBroker-Adapter.
* ### MQTT-Adapter
![image](https://user-images.githubusercontent.com/102996011/189351691-41cfbd56-cd3d-4340-9ab3-8a9d514eace7.png)
Die Kommunikation zwischen dem NSPanel und ioBroker erfolgt mittels MQTT über Tasmota. Da der Datenpunkt „CustomSend“ erforderlich ist und dieser nicht im Sonoff-Adapter vorhanden ist und auch nicht durch das Skript angelegt werden kann, erfolgt die Kommunikation „nicht“ über den Sonoff-Adapter --> später mehr …
* ### Javascript-Adapter
Es werden zwei Type-Skripte (TS = das etwas mächtigere Javascript) benötigt. Zum Einen ein Icon-Skript, da alle verwendeten Icons nicht als „echte Grafiken“ im Panel hinterlegt sind, sondern als Schriftzeichen-Symbole. Des Weiteren ein TS-Skript mit dem eigentlichen Laufzeit-Code, welches für jedes eingesetzte NSPanel vorhanden und konfiguriert sein sollte --> später mehr …
* ### Geräte verwalten-Adapter
![image](https://user-images.githubusercontent.com/102996011/189352272-e5cd0d82-c6c0-4cc5-983a-49725fdf97cf.png)
Über diesen Adapter sollten die Aliase später (mit Ausnahme des Media-Alias für Alexa & Co.) erstellt werden --> später mehr …
* ### Accu-Weather-Adapter
![image](https://user-images.githubusercontent.com/102996011/189352371-e327f599-d1cc-4d49-9088-1ddd0dcf88da.png)
Spielt in erster Linie eine Rolle beim Screensaver-Wetter, da zum Ersten die Icons und die Temperatur-Informationen für den Forecast ausgelesen werden (falls genutzt) und zum Zweiten das aktuelle Wettericon für den Screensaver benötigt wird. Wer keine Wetterstation oder Außentemperatursensor hat, kann auch die Temperatur aus Accu-Weather importieren --> später mehr …
* ### Alexa2-Adapter, Spotify-Adapter oder Sonos-Adapter
Zur Visualisierung des Media-Player‘s sollte der Alexa2-Adapter installiert sein. Wenn du statt Alexa-Devices andere Hersteller wie z.B. Google-Home-Geräte oder in erster Linie der Spotify-Premium-Adapter im Einsatz hast, so ist es auch möglich mit einem entsprechend, alternativen Media-Adapter den Media-Player zu betreiben --> später mehr …
***

## **2.) Panel mit Tasmota flashen**
  
**Sollte das NSPanel bereits vor der Bereitstellung der Tasmota v13.0.X initial geflashed worden sein, kann es zu Partitionierungs-Problemen mit einer Version >= 13.0.X kommen. In diesem Fall muss das Partitionsschema geändert werden. Ein neues NSPanel kann mit der neuesten Tasmota-Version geflashed werden.
Dazu gibt es eine Anleitung hier im Wiki unter [Tasmota FAQ](https://github.com/joBr99/nspanel-lovelace-ui/wiki/NSPanel-Tasmota-FAQ).  
Danach kann man auf Version 13.0 und höher updaten.**


Matthias Kleine hat ein neues Video zum ganzen Installationsprozzes, vom flashen bis zum Anpassen der NSPanel-Script Datei, erstellt. 
  
**Neues Video Tutorial** von [haus-automatisierung.com](http://haus-automatisierung.com/)
https://www.youtube.com/watch?v=ZPLJk2ZLo_8 - NSPanel mit Lovelace UI - so habe ich mir das vorgestellt!

[Altes Video mit der Beschreibung zum Flashen](https://www.youtube.com/watch?v=uqPz08ZpFW8)  
  
Als Alternative zu den von Matthias gezeigten Tools zum Flashen des ESP32 kann man mittlerweile auch den [Tasmota WebInstaller](https://tasmota.github.io/install/) nutzen. Die Nutzung ist relativ selbsterklärend.  
  
  
Nach dem Flashen solltest du bereits die grundsätzliche Tasmota Konfiguration vornehmen:

a) Unter „Sonstige Einstellungen“ trägst du im Feld Vorlage  
```json
{"NAME":"NSPanel","GPIO":[0,0,0,0,3872,0,0,0,0,0,32,0,0,0,0,225,0,480,224,1,0,0,0,33,0,0,0,0,0,0,0,0,0,0,4736,0],"FLAG":0,"BASE":1}
```   
ein, hakst Aktivieren "an" und klickst auf Speichern. Du kannst natürlich auch noch Device und Friendly Name vergeben
![image](https://user-images.githubusercontent.com/102996011/189354526-51aa1b0d-43d5-4c0d-8cc7-bdff0de29e24.png)

b) Unter Logging fügst du die IP von deinem ioBroker unter Sys-Log Host () ein und klickst auf Speichern.

c) Unter Konsolen/Konsole kannst du natürlich auch noch weitere Einstellungen vornehmen (ipaddress1 192.168.X.X für statische IP’s, setOption’s, etc.)  
  
d) **Hinweis**: Unter Umständen macht es Sinn, die NSPanel Temperatursensoren noch zu konfiguirieren/kalibrieren. Wir haben dies in einer eignen [FAQ](https://github.com/joBr99/nspanel-lovelace-ui/wiki/NSPanel-Tasmota-FAQ#2-sensoren) bereits erklärt.  
  
***

## **3.) Berry-Treiber installieren**
Im Tasmota findest du unter „Konsolen“ den Button „Verwalte Dateisystem“. Wenn du diesen anklickst, siehst du einen weiteren Button „Datei erstellen und bearbeiten“. Du änderst den Dateinamen „neue-datei.txt“ in „autoexec.be“ und fügst den Inhalt aus dem folgenden Link ein:
**https://raw.githubusercontent.com/joBr99/nspanel-lovelace-ui/main/tasmota/autoexec.be**  
  
![image](https://user-images.githubusercontent.com/102996011/189356139-54888313-987c-47dd-86c5-3cac7a8b5e88.png)  

Danach klickst du auf „Speichern“ und dann solltest du Tasmota rebooten.

Wenn das Panel bereits unter einer anderen Variante (z.B. [haus-automatisierung.com](http://haus-automatisierung.com/)) installiert war, dann bitte alle Dateien (insbesondere [autoexec.be](http://autoexec.be/) und autoexec.bec) vorher über das Flammensymbol hinter dem Dateinamen löschen. Und von vorne mit dem Punkt 3 beginnen

![image](https://user-images.githubusercontent.com/102996011/189356257-6b84c45e-1d00-4039-96b4-6787c3d2f671.png)

***

## **4.) MQTT (Tasmota) Config**

Im Tasmota unter „Einstellungen/MQTT konfigurieren“:  
a) Host deines ioBrokers vergeben  
b) Den Port deiner ioBroker-MQTT-Adapter-Instanz eingeben (für mqtt.0.). Wenn du noch keinen MQTT-Adapter installiert hast, dann verwende bitte nicht unbedingt den Standard-Port 1883. Dieser Port wird auch von anderen Pseudo-MQTT-Adaptern (Sonoff/Shelly/etc.) ebenfalls verwendet und führt im parallelen Betrieb mit anderen MQTT-Devices später unweigerlich zu Komplikationen. Ich verwende für die MQTT-Instanzen gerne einen Port ab 1886 oder 1887 oder 1888 oder höher. Das Problem zeigt sich in der Regel ab dem Zeitpunkt, an dem der „CustomSend“ nicht von deiner mqtt.0.-Instanz abonniert wird.  
c) Benutzer und Passwort aus der ioBroker-MQTT-Instanz eintragen  
d) Bei Client und topic trage ich in der Regel „NSPanel_X“ ein. (X = 1, 2, 3 oder WZ für Wohnzimmer, etc.)  
e) Für den full topic verwende ich in der Regel „SmartHome/%topic%/%prefix%/“.  
f) Speichern klicken und Einstellungen verlassen  
![image](https://user-images.githubusercontent.com/102996011/189357302-39068cae-94c9-4c5d-a9b4-fc399cea04f7.png)  

***

## **5.) TFT-Firmware flashen**
  
> **Achtung !!! Die aktuellsten Versionen (4.3.1 könnte nicht mehr aktuell sein) befinden sich "immer" am Ende des ioBroker TypeScript Header (TS-Skript) unter:**
> https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/NsPanelTs.ts  

Tasmota „Konsolen/Konsole“ öffnen und in die Kommandozeile  
`FlashNextion http://nspanel.pky.eu/lovelace-ui/github/nspanel-v4.3.1.tft`  
eingeben, mit Enter bestätigen. Das Panel installiert jetzt die TFT-Firmware (Kann beim ersten Mal ein paar Minuten dauern – Fortschritt beobachten – am Ende erfolgt ein Reboot und das Panel wechselt in einen Screen – „Waiting for Content“

![image](https://user-images.githubusercontent.com/102996011/189360485-1941baa7-c10a-4fb3-9dad-9c91124c47ad.png)
  

***

## **6.) MQTT (ioBroker) Config**
Wenn du bereits eine Instanz des MQTT-Adapters (z.B. mqtt.0.) nutzt, dann bitte den Port der MQTT-Adapter-Instanz auch im Tasmota-MQTT verwenden. Bitte auch hier den Hinweis aus Punkt 4b beachten und ggf. einen anderen Port für die Kommunikation eintragen.  
Ansonsten wählst du im ioBroker-Menü unter „Adapter“ den mqtt-Adapter aus und erstellst wie gewohnt eine Instanz des Adapters. Du kannst dir natürlich auch eine zusätzliche Instanz (z.B. mqtt.1. oder mqtt.2. etc.) erstellen.  

Meine Einstellungen im Reiter Verbindung sind z.B.:  
a) IP = Server/Broker  
b) WebSockets benutzen (angehakt)  
c) IP Adresse des ioBrokers (wahrscheinlich eth0 oder eth1) auswählen  
d) Port 1886 (analog Port aus Tasmota/MQTT)  
e) Benutzer (analog Benutzer aus Tasmota/MQTT)  
f) Kennwort + Kennwort wiederholen (analog Passwort aus Tasmota/MQTT)  
![image](https://user-images.githubusercontent.com/102996011/189360666-24c33c5a-64f2-4992-b957-2bba75c5768b.png)
Meine Einstellungen im Reiter MQTT-Einstellungen sind:  
a) Maske zum Bekanntgeben eigener States: mqtt.0.* (Bei zusätzlicher Instanz entsprechend höher (mqtt.1.* etc.)  
b) Eigene States beim Verbinden publizieren (angehakt)  
c) States bei subscribe publizieren (angehakt)  
d) Leere Session erzwingen: Client-Einstellungen verwenden  
![image](https://user-images.githubusercontent.com/102996011/189360742-6b1f39c6-64b0-4744-b4ee-3205666b1852.png)

> **!!! ACHTUNG: !!!**  
> Der haken bei "**Nur bei Änderungen publizieren**" darf nicht aktiv sein, da es sonst zu Problemen in der Navigation kommen kann!

***

## **7.) CustomSend anlegen**

Der MQTT Datenpunkt wird benötigt und muss vom MQTT-Adapter angelegt werden. Ein manuelles Anlegen unter „Objekte“ oder „createState“ ist im ioBroker „nicht mehr“ möglich. 

**Es gibt drei Varianten um diesen Datenpunkt zu erzeugen:**

Variante 1:  
Du gehst in das Objeckt-Verzeichnis "**mqtt.0.SmartHome.NSPanel_1.cmnd**" und legst in diesem Verzeichnis mit Hilfe des "Expertenmodus" einen Datenpunkt **CustomSend** (Achtung auf korrekte Schreibweise achten) an. Nachdem der Datenpunkt angelegt wurde, sollte der Expertenmodus wieder deaktiviert werden.

Variante 2:
Um den Datenpunkt zu erzeugen, öffnest du im Tasmota die Konsole und gibst ohne die Anführungszeichen  
`„CustomSend time~12:00“`  
ein.  

Variante 3:
Alternativ kann auch der MQTT-Explorer (http://mqtt-explorer.com/) genutzt werden und ein payload unter .../cmnd abgesendet werden.  
![image](https://user-images.githubusercontent.com/102996011/189361956-3fb08b4a-edd7-4845-a9c9-4a685738c9f6.png)
Danach sollte im MQTT-Adapter unter Objekte ein Datenpunkt: „SmartHome/NSPanel_X/cmnd/CustomSend“ erscheinen. Falls nicht, solange wiederholen bis dieser Datenpunkt abonniert wurde, oder ggfs. Nochmals die MQTT-Einstellungen überprüfen. In den Vergangenen Fragen dieses Topics ging es häufiger um diesen Punkt.

> Im Video wird die Variante 1 direkt in den Objekten des mqtt.0. gezeigt!

***

## **8.)  Einstellungen in JS-Adapter Instanz**  

Für den erfolgreichen Start des NSPanelTs.ts (siehe Punkt 10) TypeScript sind noch nachfolgende Einstellungen in der JavaScript-Adapter-Instanz erforderlich:  
  
* Hinzufügen der npm Module: `moment` und `moment-parseformat` (Wird in nächststen Versionen durch dayjs ersetzt, ist aktuell aber noch erforderlich!)
* Hinzufügen des npm Moduls: `dayjs`
* Aktivierung der Option `Kommando "setObject" erlauben`
* Aktivierung der Option `Kommando "exec" erlauben`
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/01c9bc15-f644-44e2-8c7e-b288bc68987b)

  
***  

## **9.)  Icon „TypeScript“ anlegen**

Wie bereits in der Einleitung erwähnt, werden zwei TypeScripts (TS) benötigt. Das erste ist das Icon-Skript. Das Icon-Skript dient zur Übersetzung von Schriftzeichensymbolen zwischen dem Skript und der TFT-Firmware.  
Unter dem grünen Vezeichnisbaum „global“ im ioBroker-Menüpunkt Skripte erzeugst du ein Skript mit dem Namen „IconsSelector“ vom Typ: TypeScript (TS). Dort fügst du den Inhalt der Datei:  
**https://raw.githubusercontent.com/joBr99/nspanel-lovelace-ui/main/ioBroker/icon_mapping.ts**  
ein und startest das Skript.

**Nur zur Info:**  
Du kannst die einzelnen Icon-Symbolnamen (aktuell 6896 unterschiedliche Icon-Symbole) auf  
**https://htmlpreview.github.io/?https://github.com/jobr99/Generate-HASP-Fonts/blob/master/cheatsheet.html**  
einsehen und später (kommen wir bei der Alias-Erstellung noch zu) auch jedes Icon in deinem Panel an entsprechender Stelle verwenden. Für die Einbindung sind die „Namen“ der Icons wichtig.  

***

## **10.)  „NSPanelTs.ts“ anlegen**
Unter dem regulären Vezeichnisbaum „common“ im ioBroker-Menüpunkt Skripte erzeugst du (gerne auch in weiteren Unterverzeichnissen) ein weiteres TypeScript mit dem Inhalt:  
**https://raw.githubusercontent.com/joBr99/nspanel-lovelace-ui/main/ioBroker/NsPanelTs.ts**  
  
Dieses Script enthält nur die Grundstruktur und ist nach der Parametereinstellung lauffähig. 
  
Für jedes einzelne NSPanel das du konfigurieren möchtest, musst du dieses Skript anlegen und speziell für dieses jeweilige NSPanel entsprechende Einstellungen vornehmen. Für den Skriptnamen verwende ich in der Regel eine Kombination aus Panel und Skriptversion, wie z.B.: NSPANEL_1_3.9.0

(Es kommen in regelmäßigen Abständen weitere NSPanel-Features und Bug-Fixes in das GitHub-Skript in denen dann nur noch der untere Teil (--- ab hier keine Konfiguration mehr ---) ausgetauscht werden muss und die NSPanel-Parameter erhalten bleiben)

Im oberen Teil des Skripts sind die grundsätzlichen Teile der zu erstellenden Aliase, Konstanten und Variablen (auch Seiten) enthalten. An dieser Stelle ist zunächst wichtig, die Kommunikationsparameter für die MQTT-Kommunikation anzupassen, beginnend mit

```typescript
const NSPanel_Path = '0_userdata.0.NSPanel.1.';       // Anpassen an das jeweilige NSPanel
const NSPanel_Alarm_Path = '0_userdata.0.NSPanel.';     // Pfad für gemeinsame Nutzung durch mehrere Panels (bei Nutzung der cardAlarm)


export const config = <Config> {
     panelRecvTopic: 'mqtt.0.SmartHome.NSPanel_1.tele.RESULT',       // Bitte anpassen
     panelSendTopic: 'mqtt.0.SmartHome.NSPanel_1.cmnd.CustomSend',   // Bitte anpassen
```  

Bitte starte das Skript. Alle weiteren Parameter stellen wir später ein. Ab jetzt sollte der Startup-Screen „Waiting for Connection“ in den Sreensaver wechseln und minütlich die Uhrzeit an den Screensaver übertragen und das Datum aktualisiert werden.

***

## **11.)  „NSPanelTs.ts“ konfigurieren**

Im Punkt 9 haben wir zunächst die nur Kommunikation zwischen Panel und Skript über MQTT hergestellt. Jetzt kommen wir zum Inhalt des Panels:  

**a) Screensaver einstellen**  

das Aussehen des Screensaver kannst du ganz nach deinen Wüschen gestallten. Dafür haben wir im Wiki ein eigenes Thema erstellt, da sich im Laufe der Zeit die Möglichkeiten immer erweitert haben.  [Hier lang zu den Einstellungen](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-Config-Screensaver)  

 
**b) Diverse Datenpunkte**  
Beim ersten Start des Scripts erzeugt das Skript unter 0_userdata diverse Datenpunkte für Screensaver Dimmode, interne Sensoren, Tasmota-Statuswerte, etc.  
Der Pfad kann im Skript unter „NSPanel_Path“ angepasst werden.

> **Achtung!**  
> Ab TS-Script-Version 3.5.0.5 und mit installiertem JavaScript-Adapter ab Version v6.1.3 können auch weitere Alias automatisch erzeugt werden, wenn die Konstante **autoCreateAlias** auf **true** steht.

**c) Alexa**  
Wenn du Alexa-Devices mit dem Media-Player nutzen möchtest, dann stelle noch das Standard-Alexa-Device (Seriennummer unter „var alexaDevice“) ein.
Ebenso kannst du unter alexaSpeakerList eine Liste mit vorhandenen Alexa-Devices (und/oder Gruppen) anlegen, die von diesem NSPanel-MediaPlayer aus bedient werden sollen. Bleibt diese Liste leer, werden automatisch alle Devices aus dem Alexa2-Adapter importiert.  

***

## **12.)  Aliase Anlegen**
Jetzt kommt der eigentliche Teil der Seitengestaltung. Es werden keine Datenpunkte benötigt, sondern Aliase.  
Ein Alias ist „kein“ Datenpunkt, sondern ein Objekt mit mehreren Datenpunkten.  
Das Skript setzt entsprechende Trigger auf die Alias-Datenpunkte .SET, .GET, .ACTUAL usw. Deshalb werden deine Steuerelemente im Panel nicht greifen, wenn du mit einzelnen Datenpunkten aus den verschiedenen Adaptern arbeitest.  
Ich habe im Verlauf diverse Aliase erzeugt und auch in den ChangeLogs der jeweiligen Skript-Version sind die möglichen Aliase aufgeführt, daher gehe ich hier nicht (würde die Anleitung hier auch sprengen) im Detail auf die Aliase ein. Eine genaue Beschreibung für die diversen Pages und Möglichkeiten findest du [hier.](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen) 
 

***

## **13.)  Seitengestaltung**
Die Seitengestaltung ist nun in einen eigenen Bereich hier in der Wiki gewandert.  
Die unten aufgeführten Beispiele sind **nicht** mehr im Skript enthalten.

[Bitte hier klicken](https://github.com/joBr99/nspanel-lovelace-ui/wiki/NSPanel-Page-%E2%80%90-Typen_How-2_Beispiele)
  
  
***  
**Der Folgende bereich stammt aus einer früheren Version der Wiki, bitte den Link oben beachten!**
Am Besten benutzt ihr die Beispiele im Skript und legt entsprechende Aliase hierzu an, die auch in diesem ioBroker-Community-Topic innerhalb der letzten Wochen beschrieben wurden.

cardEntities mit Alias Lampe/Dimmer/Switch  
![image](https://user-images.githubusercontent.com/102996011/189372243-fceb8f9d-d020-4640-a064-3f8134fef24b.png)  

cardEntities mit RGB und HUE Aliasen (Color)  
![image](https://user-images.githubusercontent.com/102996011/189372280-67b05750-2e2d-4093-b708-542363d8e56f.png)    

popupLight mit Farbtemperatur und Brightness  
![image](https://user-images.githubusercontent.com/102996011/189372471-f0abcade-8c00-46fc-9aa3-f445ea4764b1.png)  

popupLight mit ColorWheel  
![image](https://user-images.githubusercontent.com/102996011/189372558-cf411bba-5143-4c1f-b27c-4b64f22ca834.png)  

cardGrid mit Radiosendern/Playlists (Alias Taste)  
![image](https://user-images.githubusercontent.com/102996011/189372592-de0962ee-9015-4ce8-80e9-126669c61d97.png)  

cardEntities mit Aliasen Lautstärke und Info  
![image](https://user-images.githubusercontent.com/102996011/189372790-c6f1ea6f-1f24-4ba8-8bde-0459da1f2ab7.png)  

cardEntities mit Fenster, Tür, Jalousie und Verschluss  
![image](https://user-images.githubusercontent.com/102996011/189372858-3232a079-e4f1-4077-b947-6ba50fdfeb09.png)  

cardEntities mit Abfallkalender  
![image](https://user-images.githubusercontent.com/102996011/189372953-51ded00a-68ad-4cb8-b8c3-c85b0f8d3da5.png)  

cardMedia  
![image](https://user-images.githubusercontent.com/102996011/189373030-31692512-f934-418a-9c2f-e7624c8cb09f.png)  

cardAlarm  
![image](https://user-images.githubusercontent.com/102996011/189373105-e46f8872-3b3c-4365-8113-0a44570a03a7.png)  

cardGrid  
![image](https://user-images.githubusercontent.com/102996011/189373286-c5ad72d0-5e10-4c59-b691-f4bfd1ba354f.png)  

cardEntities  
![image](https://user-images.githubusercontent.com/102996011/189373401-42696c89-0d65-48f8-9cdf-a4c9a84073d6.png)  

cardEntities als Subpage unter cardEntities (verschachtelt)  
![image](https://user-images.githubusercontent.com/102996011/189373454-c6aa9236-1fad-47ef-915f-fb6356a4a613.png)  

cardNotify  
![image](https://user-images.githubusercontent.com/102996011/189373507-41a10711-afc0-4186-b94b-690bc1805a7f.png)  

Steuerung von Klimageräten/Klimaanlagen  
![image](https://user-images.githubusercontent.com/102996011/189373662-1aade2a6-3ccd-4cff-831c-c6c0a90ce999.png)  

QR-Code für z.B. Gäste WLAN  
![image](https://user-images.githubusercontent.com/102996011/189373730-1ceecc65-e503-47dc-8639-c29bb93b8eb1.png)  

Neues Design für Thermostate  
![image](https://user-images.githubusercontent.com/102996011/189373785-6d1870ef-4544-4099-8fc5-fd4b7f546d74.png)  

***