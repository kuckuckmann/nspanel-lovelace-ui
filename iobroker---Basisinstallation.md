**Neues Video Tutorial** von [haus-automatisierung.com](http://haus-automatisierung.com/)
https://www.youtube.com/watch?v=ZPLJk2ZLo_8 - NSPanel mit Lovelace UI - so habe ich mir das vorgestellt!

**Aktuelle Anleitung auch unter**: https://forum.iobroker.net/post/807730:

# Step für Step - Anleitung 
Anleitung zur Einrichtung eines Sonoff NSPanel mit Lovelace UI unter ioBroker
![image](https://user-images.githubusercontent.com/102996011/189348764-ab78fb87-942f-4c8a-a8e6-bc9240e6a74b.png)

# **Index**

**1.)** [Voraussetzungen für den ioBroker](https://github.com/joBr99/nspanel-lovelace-ui/wiki/iobroker---Basisinstallation#1-voraussetzungen-f%C3%BCr-den-iobroker)  
**2.)** NSPanel mit Tasmota flashen  
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

## **1.) Voraussetzungen für den ioBroker**

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
