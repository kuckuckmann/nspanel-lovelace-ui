**Neues Video Tutorial** von [haus-automatisierung.com](http://haus-automatisierung.com/)
https://www.youtube.com/watch?v=ZPLJk2ZLo_8 - NSPanel mit Lovelace UI - so habe ich mir das vorgestellt!

**Aktuelle Anleitung auch unter**: https://forum.iobroker.net/post/807730:

# Step für Step - Anleitung 
Anleitung zur Einrichtung eines Sonoff NSPanel mit Lovelace UI unter ioBroker
![image](https://user-images.githubusercontent.com/102996011/189348764-ab78fb87-942f-4c8a-a8e6-bc9240e6a74b.png)

# **Index**

 **1.)** [ioBroker Voraussetzungen](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#1-voraussetzungen-f%C3%BCr-den-iobroker)  
 **2.)** [NSPanel mit Tasmota flashen](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#2-panel-mit-tasmota-flashen)  
 **3.)** Berry-Treiber installieren  
 **4.)** MQTT im Tasmota konfigurieren  
 **5.)** TFT-Firmware auf das Panel flashen  
 **6.)** MQTT im ioBroker installieren und konfigurieren  
 **7.)** CustomSend anlegen  
 **8.)** Icon „TypeScript“ unter „Skripte“ im Verzeichnis „global“ anlegen  
 **9.)** TypeScript „NSPanelTs.ts“ anlegen  
**10.)** TypeScript konfigurieren  
**11.)** Aliase Anlegen  
**12.)** Seitengestaltung  

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

## **2.) [Panel mit Tasmota flashen](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#2-panel-mit-tasmota-flashen)**
Hierzu eignet sich für den "Hardwareteil" die Anleitung von [haus-automatisierung.com](http://haus-automatisierung.com/)

(https://www.youtube.com/watch?v=uqPz08ZpFW8). Video bis 11 Minuten und 30 Sekunden befolgen!

Die Beschreibung, wie man das Panel mit Tasmota flashen kann, ohne einen Kurzschluss zu erzeugen, ist schon sehr gut erklärt.
Du installierst gleich einen „abweichenden“ Berry-Treiber ([autoexec.be](https://raw.githubusercontent.com/joBr99/nspanel-lovelace-ui/main/tasmota/autoexec.be)) als in der Video-Beschreibung genannt. Wenn du Tasmota und „noch nicht der Berry-Treiber“ installiert hast, bitte mit der Youtube-Video-Anleitung von Matthias ab Zeit=11:30 aufhören. Ich verwende in meinen Panels die Version „tasmota32-DE.bin“. Du kannst aber auch die „tasmota32-nspanel.bin“ verwenden.
Zur MQTT-Konfiguration kommen wir im Punkt 4
An dieser Stelle solltest du aber bereits die grundsätzliche Tasmota Konfiguration vornehmen:

a) Unter „Sonstige Einstellungen“ trägst du im Feld Vorlage  
`{"NAME":"NSPanel","GPIO":[0,0,0,0,3872,0,0,0,0,0,32,0,0,0,0,225,0,480,224,1,0,0,0,33,0,0,0,0,0,0,0,0,0,0,4736,0],"FLAG":0,"BASE":1}`  
ein, hakst Aktivieren "an" und klickst auf Speichern. Du kannst natürlich auch noch Device und Friendly Name vergeben
![image](https://user-images.githubusercontent.com/102996011/189354526-51aa1b0d-43d5-4c0d-8cc7-bdff0de29e24.png)

b) Unter Logging fügst du die IP von deinem ioBroker unter Sys-Log Host () ein und klickst auf Speichern.

c) Unter Konsolen/Konsole kannst du natürlich auch noch weitere Einstellungen vornehmen (ipaddress1 192.168.X.X für statische IP’s, setOption’s, etc.)

***

## **3.) Berry-Treiber installieren**
Im Tasmota findest du unter „Konsolen“ den Button „Verwalte Dateisystem“. Wenn du diesen anklickst, siehst du einen weiteren Button „Datei erstellen und bearbeiten“. Du änderst den Dateinamen „neue-datei.txt“ in „autoexec.be“ und fügst den Inhalt aus dem folgenden Link ein:
**https://raw.githubusercontent.com/joBr99/nspanel-lovelace-ui/main/tasmota/autoexec.be**
![image](https://user-images.githubusercontent.com/102996011/189356139-54888313-987c-47dd-86c5-3cac7a8b5e88.png)
Danach klickst du auf „Speichern“ und dann solltest du Tasmota rebooten.

Wenn das Panel bereits unter einer anderen Variante (z.B. [haus-automatisierung.com](http://haus-automatisierung.com/)) installiert war, dann bitte alle Dateien (insbesondere [autoexec.be](http://autoexec.be/) und autoexec.bec) vorher über das Flammensymbol hinter dem Dateinamen löschen. Und von vorne mit dem Punkt 3 beginnen
![image](https://user-images.githubusercontent.com/102996011/189356257-6b84c45e-1d00-4039-96b4-6787c3d2f671.png)

***