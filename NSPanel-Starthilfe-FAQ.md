Starthilfe - Die häufigsten User-Fehler
  
## Hilfe bei Update / Upgrade   

Variante für ein Update der NSPanelTS.ts  

1. aktuelle Script anhalten
2. unter [diesen Link](https://raw.githubusercontent.com/joBr99/nspanel-lovelace-ui/main/ioBroker/NsPanelTs.ts) das aktuelle Script kopieren
3. ein neues TS Script anlegen, als Name nutze ich immer NSPanel+Version z.B. NSPanel43310
4. diese Parameter müssen als erstes angepasst werden  
```typescript
/***** 1. Tasmota-Config *****/

    // DE: Anpassen an die Verzeichnisse der MQTT-Adapter-Instanz
    // EN: Adapt to the MQTT adapter instance directories
    const NSPanelReceiveTopic: string = 'mqtt.0.SmartHome.NSPanel_1.tele.RESULT';
    const NSPanelSendTopic: string = 'mqtt.0.SmartHome.NSPanel_1.cmnd.CustomSend';

/***** 2. Directories in 0_userdata.0... *****/

    // DE: Anpassen an das jeweilige NSPanel
    // EN: Adapt to the respective NSPanel
    const NSPanel_Path = '0_userdata.0.NSPanel.1.';
```

5. jetzt starten wir zum erstenmal die neue Script Version, sie sollte ohne Fehlermeldung starten.
6. jetzt kopieren wir die eigenen Seiten aus den alten Script, vorher wird das neue Script gestoppt  
    Die eigenen Seiten werden zwischen diesen zwei Zeilen eingefügt.      
```typescript    
//-- Anfang für eigene Seiten -- z.T. selbstdefinierte Aliase erforderlich ----------------
//-- Start for your own pages -- some self-defined aliases required ----------------
  
	//-- https://github.com/joBr99/nspanel-lovelace-ui/wiki/NSPanel-Page-%E2%80%90-Typen_How-2_Beispiele

//-- ENDE für eigene Seiten -- z.T. selbstdefinierte Aliase erforderlich -------------------------
//-- END for your own pages -- some self-defined aliases required ------------------------
```  
    
dann müssen die Pages auch in diesen Bereich eingefügt werden. Hauptseiten kommen zu den pages und die Unterseiten zu den subPages
    
```typescript
    // Seiteneinteilung / Page division
    // Hauptseiten / Mainpages
    pages: [
 
        NSPanel_Service         	//Auto-Alias Service Page
	    //Unlock_Service            //Auto-Alias Service Page (Service Pages used with cardUnlock)
    ],

    // Unterseiten / Subpages
    subPages: [
	    
                NSPanel_Service_SubPage,                //Auto-Alias Service Page (only used with cardUnlock)
                NSPanel_Infos,                          //Auto-Alias Service Page
```

7. das Script starten und prüfen auf Fehlermeldungen, danach wird es wieder gestop.
8. jetzt kopieren wir noch die ScreensaverEntity und erstzen die im neuen Script

9. das Script wieder starten und es sollte jetzt wieder wie früher sein.
  
****  
   
Seht in den [Changelogs](https://github.com/joBr99/nspanel-lovelace-ui/wiki/Changelog) nach, ob es Änderungen im Config-Teil gegeben hat, ggf. müsst ihr eure Pages oder sonstigen Einstellungen anpassen. Prüft, ob das neue Script eine andere TFT-Firmware benötig bzw. einen anderen Berry-Treiber. Diese Info findet ihr in der zweiten Zeile des Scripts.  
Wenn es zu diesen Änderungen kommt, weisen wir im Forum auch explizit darauf hin.  
    
Deaktiviert das alte Script und behaltet es als Fallback.  
  
Beim Start des neuen Script kann es eventuell zu Warnungen im Log kommen, wenn neue Datenpunkte angelegt werden. Startet das Script nochmal neu, dann sollte es ohne Warnungen starten.   
   
## "Waiting for Content" - es geht nicht weiter 
  
Hier liegt der Fehler sehr oft in den Einstellungen zur MQTT - Verbindung.  
* Prüft als erstes die Einstellungen im MQTT - Adapter, vor allem der Port, dieser darf nicht doppelt genutzt werden, z.B. durch einen zweiten Adapter. Dazu gibt es im Script auch eine Funktion, die ein Portscan durchführt und das Ergebnis im Log ausgibt. Diesen Scan könnt ihr über das Servicemenü am Panel aktivieren (Einstellungen -> Script -> Port-Check) oder direkt im ioBroker unter 0_userdata.0.NSPanel.X.Config.MQTT.portCheck auf True setzen. Danach das Script neu starten und das Log auswerten.  
* Vergleicht die Pfade im ioBroker vom MQTT - Adapter mit den Einstellungen im Script unter.  
```typescript
    const NSPanelReceiveTopic: string = 'mqtt.0.SmartHome.NSPanel_1.tele.RESULT';
    const NSPanelSendTopic: string = 'mqtt.0.SmartHome.NSPanel_1.cmnd.CustomSend';
```  
Weiter unten findet ihr nochmal die Einstellung vom MQTT-Adapter und Tasmota.  
  
## Berry-Driver nicht oder falsch installiert

## MQTT-Adapter Einstellungen  
Bilder sagen meistens mehr als Worte. Wichtig ist, wenn User und Passwort vergeben worden sind, diese auch in Tasmota eingetragen werden müssen.  
  
<img width="1186" alt="Bildschirmfoto 2023-09-26 um 18 08 54" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/70d8d600-d385-412d-8db2-17206509be55">
  
<img width="1186" alt="Bildschirmfoto 2023-09-26 um 18 09 05" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/bdc61937-2ea8-4dbf-9fad-472c893c0a77">
  
<img width="1186" alt="Bildschirmfoto 2023-09-26 um 18 09 22" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/f2c4e065-8c46-44d5-9aa7-a79096a3fc15">
  
## MQTT-Tasmota Einstellungen  
  
<img width="402" alt="Bildschirmfoto 2023-09-26 um 18 10 44" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/6b67720c-eeaa-43db-84b6-05f953aba6e1">
  
* Host -> IP-Adresse vom ioBroker
* Port -> der Port welcher im MQTT-Adapter eingestellt wurde
* Client -> Name der in der Connect Meldung vom MQTT-Adapter angezeigt wird (mqtt.0.info.connection)  
* User, Password -> siehe MQTT-Adapter  
* topic -> Name für die Variable, diese wird für die Hierarchie im MQTT genutzt 
* full topic -> für eine sinnvolle Hierarchie sollte nicht die Vorgabe %prefix%/%topic% nutzen, sondern umgekehrt. Seht euch die beiden Bilder unten an.  

***

Hierarchie mit **Smarthome/%topic%/%prefix%**   
<img width="402" alt="Bildschirmfoto 2023-09-26 um 18 38 06" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/7597c582-200f-4ace-baca-4acc5eff53cd">

Hierarchie mit **Smarthome/%prefix%/%topic%**  
<img width="414" alt="Bildschirmfoto 2023-09-26 um 18 39 40" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/213d3d4a-0f72-423e-b5ff-273ed85d220a">

## "CustomSend" fehlt
[In der Basisinstallation gibt es drei Möglichkeiten](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---Basisinstallation#7-customsend-anlegen)
***