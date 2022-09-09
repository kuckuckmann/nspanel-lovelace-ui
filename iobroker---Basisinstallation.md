**Neues Video Tutorial** von [haus-automatisierung.com](http://haus-automatisierung.com/)
https://www.youtube.com/watch?v=ZPLJk2ZLo_8 - NSPanel mit Lovelace UI - so habe ich mir das vorgestellt!

**Aktuelle Anleitung auch unter**: https://forum.iobroker.net/post/807730:

# Step für Step - Anleitung 
Anleitung zur Einrichtung eines Sonoff NSPanel mit Lovelace UI unter ioBroker
![image](https://user-images.githubusercontent.com/102996011/189348764-ab78fb87-942f-4c8a-a8e6-bc9240e6a74b.png)

# **Index**

**1.)** Voraussetzungen für den ioBroker  
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
* MQTT-Adapter
![image](https://user-images.githubusercontent.com/102996011/189351691-41cfbd56-cd3d-4340-9ab3-8a9d514eace7.png)
Die Kommunikation zwischen dem NSPanel und ioBroker erfolgt mittels MQTT über Tasmota. Da der Datenpunkt „CustomSend“ erforderlich ist und dieser nicht im Sonoff-Adapter vorhanden ist und auch nicht durch das Skript angelegt werden kann, erfolgt die Kommunikation „nicht“ über den Sonoff-Adapter --> später mehr …
***
