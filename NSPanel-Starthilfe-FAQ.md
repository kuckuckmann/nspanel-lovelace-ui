Starthilfe - Die häufigsten User-Fehler
  
## Hilfe bei Update / Upgrade   

Bei einer neuen Version des Scripts solltet ihr euch die Datei [NsPanelTs_without_Examples.ts](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/NsPanelTs_without_Examples.ts) als RAW runterladen. Erstellt ein neues Typescript und kopiert das RAW dort hinein.  

folgende Zeilen im Script müssen definitiv angepasst werden:  
`const NSPanel_Path = '0_userdata.0.NSPanel.1.';       // Anpassen an das jewilige NSPanel`  
`panelRecvTopic: 'mqtt.0.SmartHome.NSPanel_1.tele.RESULT',       // Bitte anpassen`  
`panelSendTopic: 'mqtt.0.SmartHome.NSPanel_1.cmnd.CustomSend',   // Bitte anpassen`  

Für User die den Wetter - Adapter "DasWetter.0." nutzen, müssen im in der Config im Bereich  
`bottomScreensaverEntity :  
        [
            // bottomScreensaverEntity 1
            {
                ScreensaverEntity: 'accuweather.0.Daily.Day1.Sunrise',`  
alle 4 Datenpunkte auf den Adapter umstellen.  
  

Seht in den [Changelogs](https://github.com/joBr99/nspanel-lovelace-ui/wiki/Changelog) nach, ob es Änderungen im Config-Teil gegeben hat, ggf. müsst ihr eure Pages oder sonstigen Einstellungen anpassen. Prüft, ob das neue Script eine andere TFT-Firmware benötig bzw. einen anderen Berry-Treiber. Diese Info findet ihr in der zweiten Zeile des Scripts.  
 
Deaktiviert das alte Script und behaltet es als Fallback.  

Beim Start des neuen Script kann es eventuell zu Warnungen im Log kommen, wenn neue Datenpunkte angelegt werden. Startet das Script nochmal neu, dann sollte es ohne Warnungen starten.  

Eine neue TFT-Firmware installiert ihr über die Console in Tasmota  
`FlashNextion http://nspanel.pky.eu/lovelace-ui/github/nspanel-vX.X.X.tft `  
Welche Version grade aktuell zum Script passt, findet ihr im Script.  
   
## "Waiting for Content" - es geht nicht weiter  
## Berry-Driver nicht oder falsch installiert

## MQTT-Adapter Einstellungen

## MQTT-Tasmota Einstellungen

## "CustomSend" fehlt

***