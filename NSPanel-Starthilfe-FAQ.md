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
Bilder sagen meistens mehr als Worte. Wichtig ist, wenn User und Passwort vergeben worden sind, diese auch in Tasmota eingetragen werden müssen.  
  
<img width="1186" alt="Bildschirmfoto 2023-09-26 um 18 08 54" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/70d8d600-d385-412d-8db2-17206509be55">
  
<img width="1186" alt="Bildschirmfoto 2023-09-26 um 18 09 05" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/bdc61937-2ea8-4dbf-9fad-472c893c0a77">
  
<img width="1186" alt="Bildschirmfoto 2023-09-26 um 18 09 22" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/f2c4e065-8c46-44d5-9aa7-a79096a3fc15">
  
## MQTT-Tasmota Einstellungen  
  
<img width="402" alt="Bildschirmfoto 2023-09-26 um 18 10 44" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/6b67720c-eeaa-43db-84b6-05f953aba6e1">
  
* Host -> IP-Adresse vom ioBroker
* Port -> der Port welcher im MQTT-Adapter eingestellt wurde
* Client -> Name der in der Connect Meldung Von MQTT-Adapter angezeigt wird (mqtt.0.info.connection)  
* User, Password -> siehe MQTT-Adapter  
* topic -> Name für die Variable, diese wird für die Hierarchie im MQTT genutzt 
* full topic -> für eine sinnvolle Hierarchie sollte nicht laut Vorgabe %prefix%/%topic% sondern umgekehrt.  

***

Hierarchie mit **Smarthome/%topic%/%prefix%**   
<img width="402" alt="Bildschirmfoto 2023-09-26 um 18 38 06" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/7597c582-200f-4ace-baca-4acc5eff53cd">

Hierarchie mit **Smarthome/%prefix%/%topic%**  
<img width="414" alt="Bildschirmfoto 2023-09-26 um 18 39 40" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/213d3d4a-0f72-423e-b5ff-273ed85d220a">

## "CustomSend" fehlt

***