# **FAQ & Anleitungen**

In diesem Thread möchte ich damit beginnen, Einstellungen und Konfigurationen an einem Platz zu sammeln. Jeder von Euch der etwas beitragen möchte, kann dies sehr gerne tun. Ich hoffe, dass wir damit die [Installationsanleitung](https://forum.iobroker.net/topic/50888/sonoff-nspanel/612) um viele spezielle Konfigurationen ergänzen können.

# **Index**

**1.)** Button entkoppeln  
**2.)** Alarm Page  
**3.)** Info Popup auf Request  
**4.)** Abfallkalender  
**5.)** QR-Code page  
**6.)** Alias Definitionen  
**7.)** Hardware-Buttons im Multipress-Mode  
**8.)** Rolladen / Jalousie / Shutter  
**9.)** Alias "Taste" für Auswahl eines Radiosenders  
**10.)** DWD Daten an verschiedene NSPanels schicken  
**11.)** PV-Daten Info Seite  
**12.)** Platzhalter  
**13.)** Blätterprobleme & direkter Seitenaufruf  
**14.)** NSPanel Temperatursensor für MQTT  
**15.)** Zeiteinstellung Host System  
 
# **Changelog**
<details>
  <summary>Changelog</summary> 
 
01.09.2022 - Thread erstellt  
01.09.2022 - Button entkoppeln - erstellt  
01.09.2022 - Alarm Page - erstellt  
01.09.2022 - Info Popup auf Request - erstellt  
01.09.2022 - Alarm Page - @Armilar s Input ergänzt  
01.09.2022 - Abfallkalender - erstellt  
02.09.2022 - QR Code Page - erstellt  
02.09.2022 - Alias Definitionen - erstellt  
02.09.2022 - Hardware-Buttons im Multipress-Mode - erstellt  
03.09.2022 - Alarm Page - kleine Korrektur / Reperatur Blockly Skript  
05.09.2022 - Übertrag vom IoBroker Forum nach Github Wiki  
06.09.2022 - Rolladen / Jalousie / Shutter - In erstellung  
06.09.2022 - Abfallkalender - Überarbeitetes JS und neuen Screenshot + Textanpassungen  
06.09.2022 - Alarm Page - Neuerungen v3.3.1 eingepflegt  
07.09.2022 - QR Code Page - Beschreibung erweitert  
09.09.2022 - Alias "Taste" für Auswahl eines Radiosenders - Erstellt  
09.09.2022 - Alias "Media" für cardMedia - in Erstellung  
14.09.2022 - bug im js-script Abfall behoben  
24.09.2022 - DWD Blockly - erstellt  
24.09.2022 - PV-Daten Info Seite - erstellt  
18.11.2022 - Abfallkalender - Beispielpage für TS-Scrpit angepasst 
27.12.2022 - Skripte (Blocklys und JS) wurde in Repository ausgelagert und sind nun in der Wiki nur noch verlinkt
28.12.2022 - Blätterprobleme & Direkter Seitenaufruf - Erstellt  
28.12.2022 - NSPanel Temperatursensor für MQTT - Erstellt 
28.12.2022 - Zeiteinstellung Host System - Erstellt   
</details>  


***
# Anleitungen

## **1.) Button entkoppeln**

* **Quellen**:  
Post [884](https://forum.iobroker.net/topic/50888/sonoff-nspanel/884) und Post [754](https://forum.iobroker.net/topic/50888/sonoff-nspanel/754) hier im Forum

* **Zusammenfassung**:  
Wenn man auf einen der beiden Buttons eine Funktion legen möchte, die eine Steuerung in der Oberfläche übernimmt und dabei nicht das Relay geschaltet werden soll, dann muss man das Relay vom Button entkoppeln. 

* **Tasmota**:  
Über die Tasmota Konsole muss man für den Button oder beide Buttons eine Rule definieren und aktivieren, welche für die Entkopplung sorgt.
Tasmota konsole:  
--> öffnen der Tasmota Konfigurationsoberfläche des Panels, dann auf Konsole und noch einmal auf Konsole  
--> Rule definieren   

  ```
  Rule2 on Button1#state do Publish %topic%/%prefix%/RESULT {"CustomRecv":"event,button1"} endon on Button2#state do Publish %topic%/%prefix%/RESULT {"CustomRecv":"event,button2"} endon
  ```
  Dies ist die Rule für beide Buttons. Möchte man nur einen entkoppeln muss man "**on Button......**" bis zum nächsten "**...endon**" entfernen. **Button1 = der linke Button, Button2 = der rechte Button**.  
  **Wichtig:** **%topic%**/**%prefix%**/RESULT gilt es dabei so anzupassen, dass der Struktur in Eurem MQTT Adapter entspricht:  

  mqtt.0.SmartHome.nspanel_7C14FC.tele.RESULT  

  **%topic%** entspricht hier **nspanel_7C14FC** und **%prefix%**  entspricht **tele**  

  --> Rule aktivieren: 
  ```
  Rule2 1
  ```
  --> Rule deaktivieren: 
  ```
  Rule2 0
   ```

* **Konfigurationsskript**:  
Im Konfigurationsskript benötigt Ihr nun unter der **pages** Definition **buttonxPage**: (x=Nummer des Buttons).
Entweder gebt Ihr hier nun den var/const Name eines bestehenden Grid mit, damit kann man einen Button quasi als Home-Button nutzen, oder man legt einen eigenen Grid auf den Button, welcher dann zuvor definiert werden muss.


* **FAQ**:  
Hintergrund: Die Buttons geben keinen definierten Page-Index zurück, daher werden im Skript negative Page-Indizes verwendet (damit man weiß, dass es ein externer Button war). Dieser Seiten-Button (nach oben zeigend) führt auf die Page 0 (also immer auf die erste Seite)


***

## **2.) Alarm Page**


* **Quelle**:  
Post [1087](https://forum.iobroker.net/topic/50888/sonoff-nspanel/1087), [1265](https://forum.iobroker.net/topic/50888/sonoff-nspanel/1265)+[1270](https://forum.iobroker.net/topic/50888/sonoff-nspanel/1270) im ioBroker Forum.  

* **Voraussetzung**:  
Konfigurationsskript **NsPanelTs.ts** mindestens in der Version: _04.09.2022 - V3.3.1 - Überarbeitung und BugFix für cardAlarm_

* **Im IoBroker**  
Im IoBroker wird unter **0_userdata.0.NSPanel.Alarm** die Datenpunkte **AlarmPin**, **AlarmState**, **AlarmType**, **PANEL** und **PIN_Failed** benötigt. Diese werden i.d.R. generisch erzeugt (Typ String), sobald der Code der Alarm Page das erste Mal geladen wird.

  ![image](https://user-images.githubusercontent.com/99131208/188733210-7bb901dd-0246-4c3b-b5b9-5d02deb6a00c.png)  
  
  **Wichtig**: Mit der Version v3.3.1 hat sich der Default-Pfad von der Ebene **0_userdata.0.NSPanel.1.Alarm** nach **0_userdata.0.NSPanel.Alarm** geändert. Da wir im Alarmverhalten / Informations-Popup unterscheiden wollen zwischen Meldung an alle NSPanel oder nur an ein speziefisches, ist es logisch den Alarm Ordner aus dem Ordner des NSPanel Nr. 1 auf die nächst höhere globalere Ebene darüber zu verschieben.

  Bei Aktivierung oder Deaktivierung der Alarmanlage wechselt der Status in **arming** oder **pending**. Im Falle einer PIN Falscheingabe gibt es nun auch **triggered**. Da die Verarbeitung der Alarmlogik außerhalb des Skriptes stattfindet, müssen die Datenpunkte auch entsprechend durch das externe Skript weiter getaktet werden


* **Aliase**:  
Die drei Datenpunkte **AlarmPin**, **AlarmState** und **AlarmType** werden in einem Alias vom Typ Feueralarm im Gerätemanager oder Alias Adapter angelegt und dieser Alias wird dann im Konfigurationsskript auf der Alarm-Page verwendet.

  ![image](https://user-images.githubusercontent.com/99131208/188514578-43f08178-b8f0-4d09-8e76-02cbe55d5557.png)

  Alias-Typ Feueralarm:  
  ACTUAL = 0_userdata.0.NSXXXX.Alarm.AlarmState  
  PIN = 0_userdata.0.NSXXXX.Alarm.PIN  
  TYPE = 0_userdata.0.NSXXXX.Alarm.AlarmType  

  Falls ein Wert im Alias nicht vorhanden ist, dann separat hinzufügen

* **Konfigurationsskript**  
**Allgemeine Einstellung**:  
Es gibt nun eine neue Konstante, die den Pfad definiert, in dem der Ordner Alarm angelgt wird. Default wie wir schon zuvor gelernt haben ist **0_userdata.0.NSPanel.**  

`
const NSPanel_Alarm_Path = '0_userdata.0.NSPanel.'; 
//Neuer Pfad für gemeinsame Nutzung durch mehrere Panels
`

**Page Type**: Die Alarmfunktion kann nur auf einer **PageAlarm** verwendet werden  

**Beispiel**:  
  ```
  var Buero_Alarm: PageAlarm =
  {
  "type": "cardAlarm",
  "heading": "Alarm",
  "useColor": true,
  "subPage": false,
  "parent": undefined,
  "items": [<PageItem>{ id: "alias.0.NSPanel_1.Alarm" }]
  };
  ``` 


* **Blockly Testskript**  
Nachfolgend ein kurzes Emulationsskript für die Weiterverarbeitung. Diese Logik sollte auch in dein eigenes externes Alarm-Skript übernommen werden.

  ![image](https://user-images.githubusercontent.com/99131208/188735860-880e0a81-407e-454e-b7d2-05cf8f57acfb.png)  
 

  [Zum Blocky](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/Alarm_Page_Testskript.xml)   
  (Bild & Blockly by @Armilar)  

  
  Test-Blockly starten:  
  
  Alarm-Code in die cardAlarm eingeben --> Schutz auswählen --> aktiviert  
  Alarm-Code in die cardAlarm eingeben --> Deaktivieren --> deaktiviert  
  
**Ablauf**:  
1. Ablauf Alarm Aktivierung:  
PIN eingeben und dann Alarm-Modus (Vollschutz, Zuhause, Nacht oder Besuch) auswählen. Im Datenpunkt AlarmType wird das als A1, A2, A3 oder A4 interpretiert und kann extern weiterverarbeitet werden.  

![image](https://user-images.githubusercontent.com/99131208/188736479-e56f574b-5ab3-442b-90d1-384672779ec9.png)  

Das Panel wechselt in den Status (AlarmState) "arming" (Icon = gelbes blinkendes Schild/Keine Tastatur)  

![image](https://user-images.githubusercontent.com/99131208/188736544-3a3e7e12-b28d-476a-bb97-3b2e9a1cc1e0.png)  

Wenn durch das externe Skript (oder Emulator) der Status "armed" in den Datenpunkt AlarmState eingetragen wird (vorausgesetzt das externe Skript findet z.B, keine offenen Fenster) wird das Icon rot:  

![image](https://user-images.githubusercontent.com/99131208/188736580-0a8c8a8d-5c6c-40d5-ab64-a305a05da70e.png)  

Der AlarmType ist jetzt D1, die Tastatur ist wieder eingeblendet und die card Alarm bereit für die Deaktivierung.  
  
2. Ablauf Alarm Deaktivierung:  
PIN-Eingabe zur Deaktivierung und Bestätigung durch den Button "Deaktivieren". 
 
![image](https://user-images.githubusercontent.com/99131208/188736732-324c0cb7-f638-4bf7-80cb-b5b631bc1360.png)  

Das Panel vergleicht jetzt den Aktivierungs-PIN mit dem Deaktivierungs-PIN. Stimmen die PIN's überein, dann wird der AlarmState auf "pending" gesetzt.  

![image](https://user-images.githubusercontent.com/99131208/188736794-73d106c4-263a-4e4b-9b41-cb53ca1e457f.png)  

Das externe Alarm-Skript macht seine restlichen Aufgaben und setzt dann den Status auf "disarmed"  

![image](https://user-images.githubusercontent.com/99131208/188736826-ba9c0373-248e-4762-8b11-c5c66d540d8a.png) 
 
Sollte der Pin nicht übereinstimmen, so setzt das Panel den AlarmState "triggered" (Icon blinkt)  

![image](https://user-images.githubusercontent.com/99131208/188736871-5d91b8b3-83bf-435b-9346-07c419aee21c.png) 


**Neues**:
Neu ist in diesem Zusammenhang der Alias "PIN_Failed" (state/number)
Das TS-Skript zählt die missglückten Anmeldeversuche und trägt sie hier ein. Könnte man also auch für einen Trigger mit Meldung an Telegram nutzen. Außerdem wird bei Fehlerhaften PIN-Eingaben der Datenpunkt AlarmState auf "triggered" gesetzt. Im Panel sieht das dann so aus (das Icon blinkt):  

![image](https://user-images.githubusercontent.com/99131208/188736871-5d91b8b3-83bf-435b-9346-07c419aee21c.png) 
  
Status "triggered":  
Durch das externe Skript (alternativ der Alarm-Emulator) kann ein Status "triggered" gesetzt werden.  
Zum Beispiel wenn der Alarm ausgelöst wurde, Die Deaktivierung der cardAlarm funktioniert somit auch bei dem Status "triggered".  

**Erweitertes Blockly mit popupNotify Page**:  
Voraussetzung: Ein neuer Datepunkt mit einer vodefinierten PIN.  
Definieren der Basiseinstellungen in der gleichnamigen Funktion:  
 
![image](https://user-images.githubusercontent.com/99131208/188738657-6e322211-b5d8-4528-9623-747813c5780f.png)  

 Es gibt fünf Basiseinstellungen:  
* Datenpunkt AlarmPIN: Hier muss der Pfad zu dem Datenpunkt konfiguriert werden, der die original PIN enthält. Gegen diese wird bei der Eingabe vom Skript verglichen.  **Wichtig**: Dieser Datenpunkt muss manuell im ioBroker erzeugt werden. Es handelt sich **nicht** um den Datenpunkt **0_userdata.0.NSPanel.Alarm.AlarmPin** **!!!**
* Anzahl_NSPanles: Die Anzahl der NSPanels, die mit dem ioBroker verbunden sind  
* Notifay_OnOff: Soll es eine Information mit der **popupNotify Page** geben? wahr=an und falsch=aus.  
* Notify_Interaktion: An einem Panel wird eine Eigabe gemacht, manipulation versucht o.ä. Wer soll eine **popupNotify Page** erhalten? jeweils=nur das Panel an dem gerade eine Eingabe erfolgt oder global=alle angeschlossenen Panels  
* Notify_Event: Ein Alarm wird ausgelöst, wer soll mit einer **popupNotify Page** informiert werden? jeweils=nur das Panel an dem gerade eine Eingabe erfolgt oder global=alle angeschlossenen Panels  
  
**Hinweis**:  Wenn Ihr eine Anpassung am Skript oder an einem Datenpunkt vornehmet, startet bitte das Skript einmal neu.  

[Zum Blockly](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/Alarm_Page_Erweitertes_Skript_mit_PopupNotifyPage.xml)

***

## **3.) Info Screensaver-Info auf Request**  

* **Beschreibung**:  
Gedanke war es, die Funktion der screensaver Notify zu nutzen um beim drücken eines Buttons eine bestimmte Ausgabe zurück zu bekommen. 


* **Quelle**:  
Als Vorlage und Beispiel diente mir der Post [288](https://forum.iobroker.net/topic/50888/sonoff-nspanel/288) hier im Forum


* **IoBroker**  
Wenn man so wie ich, das ganze über einen Button vom NSPanel aus Anfragen möchte, benötigt meinen Datenpunkt (Boolean) zur Steuerung.  Ich habe mir dafür im **0_userdata.0.NSPanel.1.** einen neuen Ordner angelegt mit einem entsprechenden Datenpunkt.


* **Alias**  
Im Geräte Adapter habe ich mir auf den Hilfs-Datenpunkt einen Alias vom Typ Taste gelegt, damit ich den Button auf dem NSPanel darauf ansteuern kann.

* **Blockly**:  
Dann habe ich mir ein Blockly gebaut, welches den Status des Hilfs-Datenpunktes ausliest. Sobald dieser durch drücken des Buttons auf dem NSPanel auf true wechselt, wird das Skript ausgeführt.
Das Skript füttert die beiden Datenpunkte für die NotifyPopupPage im ordner **0_userdata.0.NSPanel.1.ScreensaverInfo.**:
**popupNotifyHeading** und **popupNotifyText**  
 
  **Wichtig:**  
  Die Info wird nur angezeigt, wenn der Screensaver wieder aktiv ist. Deshalb muss das erste Timeout im Skript etwas größer sein als **timeoutScreensaver** im Konfigurationsskript.  

  ![image](https://user-images.githubusercontent.com/99131208/188515089-64d9a284-65bf-4561-91bf-47ecc215f2d9.png) 

  [Zum Blockly](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/Screensaver-Info_auf_Request.xml)


  Mein Blockly gibt hie einfach nur fest definierten Text zurück. Möglichkeiten dies nun dynamisch zu gestalten, gibt es viele. Tobt Euch aus!  

* **Konfigurationsskript**:  
Im Konfigurationsskript habe ich mir nun einen Button definiert 

  ```
  <PageItem>{ id: "alias.0.InfoRQ", icon: "comment-question" ,name: "InfoScreen"},
  ```

***  

## **4.) Abfallkalender**  

* **Generell**  
Um das Thema Abfallkalender Umsetzen zu können gibt es verschiedene Herangehensweisen.  Die Minimum Punkte sind unter den Voraussetzungen aufgelistet. 
Ob man nun direkt mit einem Kalender arbeitet der vom Entsorger bereitgestellt wird oder ob man sich die Mühe macht sich einen eigenen Kalender anzulegen - jeder wie er möchte.  
Die Basis für meine Dokumentation ist ein Google Kalender, der dann via einem ICal Adapter verbunden ist. Weiterhin nutze ich den Adapter Trashschedule von @haus-automatisierung. Das positive daran ist, [Matthias](@haus-automatisierung ) hat ein [Video](https://www.youtube.com/watch?v=v9-6LJph_8Q) zur Einrichtung gemacht, bei der die Grundlage eben genau ein Google Kalender ist. Ich finde das eine schöne Basis.  
  
  
* **Voraussetzungen**
--> Abfallkalender des Entsorgers / der Entsorger  
--> ICal Adapter  
--> @Armilar s Skript zur Verarbeitung  
--> Datenpunkte  


* **IoBroker**
Ich setze an der Stelle nun voraus, dass es bereits einen ICal Adapter gibt und dieser mit einem Kalender verbunden ist.

**Datenpunkte**:  
Unter 0_userdata.0. einen Ordner Abfallkalender anlegen. Darunter vier Unterordner 1-4. In jedem Unterordner gibt es dann drei Datenpunkte anzulegen: **color**, **date** und **event**

![image](https://user-images.githubusercontent.com/99131208/188515709-424f2b14-2814-4c45-a4ef-fc445b51dfb2.png) 
(Bild by @Armilar )

**Aliase**:
Im Geräte Adapter oder Alias Adapter einen Ordner für die Aliase des Abfallkalenders anlegen. 
Darunter dann 4 generische Einträge event1 - event4 vom **Typ Warnung**.  
  
![image](https://user-images.githubusercontent.com/99131208/188515685-9c932e4b-fb02-4121-91fb-834c24985e3d.png)  
(Bild by @Armilar )  

**Wichtig**:  
**LEVEL** --> geht auf Datenpunkt **color**  
**TITEL** --> geht auf Datenpunkt **event**  
**INFO** --> geht auf Datenpunkt **date**  

![image](https://user-images.githubusercontent.com/99131208/188515669-b8bcba34-2803-4a9d-a286-f6310afe25c4.png) 
(Bild by @Armilar )



* JS / Blockly:
Es steht für die Umsetzung / Aufbereitung der Kalenderdaten nach NSPanel ein JS und ein Blockly zur Verfügung. Man benötigt nur eines davon. Es spricht aber nichts dagegen, beide mal zu testen ;-)

Java Skript (by @TT-Tom):

1 = Hier muss der Pfad zum ICal Adapter zum Punkt **ical.0.data.table** eigestellt werden. Achtet auf die Instanznummer beim Adapter  
2 = Muss nur angepasst werden, wenn Eure Datenpunkte nicht unter **0_userdata.0.Abfallkalender.** liegen (jede Stelle im Skript)  
2.1 = Script prüft die Existenz der Datenpunkte unter **0_userdata.0** und legt sie ggf. selber an    
3 = Die Bezeichnungen der Abfallbehälter in Eurem Kalender. Die Namen müssen passen, das mit das Parsen funktioniert. Tipp: Die Ziffern bei "setze Color auf ....." sind die Farbcodierungen im Dezimalsystem.  
4 = Zeichen links vom String abziehen, wenn vor dem Eventname noch Text steht z.B. Strassenname; Standard = 0.  
  
![image](https://user-images.githubusercontent.com/99131208/188730795-357f1a2d-3bf6-4808-b394-093d3f4015a8.png)  
[Zum JS-Skript](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/Abfallkalender.js)

Blockly Skript (by @Armilar):  
  
1 = Hier muss der Pfad zum ICal Adapter zum Punkt **ical.0.data.table** eigestellt werden. Achtet auf die Instanznummer beim Adapter  
2 = Muss nur angepasst werden, wenn Eure Datenpunkte nicht unter **0_userdata.0.Abfallkalender.** liegen  
3 = Die Bezeichnungen der Abfallbehälter in Eurem Kalender. Die Namen müssen passen, das mit das Parsen funktioniert. Tipp: Die Ziffern bei "setze Color auf ....." sind die Farbcodierungen im Dezimalsystem.  
4 = Zeichen links vom String abziehen, wenn vor dem Eventname noch Text steht z.B. Strassenname; Standard = 1.  

![image](https://user-images.githubusercontent.com/99131208/188515546-1c2b3048-0d5c-427a-b70c-aab035eeaab4.png)
![image](https://user-images.githubusercontent.com/99131208/188515563-bc6a65a2-4e07-454c-8038-f04366d20516.png)  

[Zum Blockly](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/Abfallkalender.xml)

* **Konfigurationsskript**
Im Konfigurationsskript muss ein Grid passend zu den Aliasen angelegt werden. Hier das Bsp. aus dem Default:
```
let Abfall: PageEntities =
{
    "type": "cardEntities",
    "heading": "Abfallkalender",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [
        <PageItem>{ id: AliasPath + 'Abfall.event1',icon: 'trash-can'},  
        <PageItem>{ id: AliasPath + 'Abfall.event2',icon: 'trash-can'},  
        <PageItem>{ id: AliasPath + 'Abfall.event3',icon: 'trash-can'},  
        <PageItem>{ id: AliasPath + 'Abfall.event4',icon: 'trash-can'}  
    ]
};
```

* **Fazit**:
Eine vermeintlich einfache Sache, die aber ziemlich knifflig werden kann. 


***


## **5.) QR-Code Page**
* **Quelle:**
Die Anleitung kommt aus dem Post [620](https://forum.iobroker.net/topic/50888/sonoff-nspanel/620) hier im Forum.

* **ioBroker:**
Legt Euch unter **0_userdata.0.** einen neuen Datenpunkt vom Typ String an. Dieser Datenpunkt erhält die Daten aus dem sich der QR Code erstellt. Außerdem werden SSID und das Passwort separat auf der Page angezeigt.  

Bsp.: WIFI:**T**:WPA;**S**:Test-Guest-SSID;**P**:guest-accecess;**H**:;  

T = Verschlüsselung  
S = SSID  
P = Password  
H = Hidden (nur erforderlich wenn versteckt)  

![image](https://user-images.githubusercontent.com/99131208/188515951-c5350270-de2f-4526-b337-9fd9c60bf6d8.png)  
(Bild by @Armilar )     

* **Alias:**
Für den erstellten Datenpunkt nun einen Alias vom Typ Info anlegen.
![image](https://user-images.githubusercontent.com/99131208/188515935-344deccc-c00f-48c1-9770-83ab432c34d3.png)  
(Bild by @Armilar )    

* **Konfigurationsskript:**
Im Script müsst ihr im Konfigurationsbereich nun eine PageQR hinzufügen. 

```
var WLAN: PageQR = 
{
    "type": "cardQR",
    "heading": "Gäste WLAN",
    "useColor": true,
    "subPage": false,
    "parent": WLAN,
    "items": [
		<PageItem>{ id: "alias.0.NPanel_EMU.TestGuestWifi" }
	
	]
};
```
Zusätzlich muss im Script im Bereich des Page Arrays bzw. Subpage Arrays die Page mit ihrem Namen eintragen.
```
    pages: [
              Buero_Seite_2,
              Buero_Seite_1,
              WLAN,
              ...
 
```
* **Bekannte Probleme**
Der QR Code funktioniert auf manchen Android Geräten nicht.


***


## **6.)** Alias Definitionen

* **Quelle**  
Gefunden hier im Thread im Post [687](https://forum.iobroker.net/topic/50888/sonoff-nspanel/687).

* **Ein Erklärungsversuch**  
Die genaue Definition eines Alias, dafür gibt es im Internet sicherlich ausreichend Beschreibungen. ich möchte mich hier auf den Fall des ioBrokers reduzieren.  
Für viele ist es DAS Hinderniss, wenn Sie mit der Installtion des NSPanels und der Verbindung in richtung iobroker und des Konfigurationsskriptes beginnen. Was ist das mit dem Alias? Wie funktioniert es? warum benötigt man es? Aber am wichtigsten: was mucss ich machen?  
  
  Genau letzteres hoffe ich hier zu erschließen. Wir haben im ioBroker von Haus aus Datenpunkte unter den Objekten. Diese kann man aus dem Konfigurationsskript aber nicht direkt ansteuern. Bei dieser Übergabe geht es um eine Art Einheitlichkeit, nennen wir es Standadisierung und Übersetzung. Ein Alias ist im Sinne des ioBroker ein neuer Datenpunkt, unter dem man sogar teilweise mehrere Datenpunkte zusammenfassen kann. Jeder Datenpunkt wird in einem Alias einem Indikator zugewiesen. So liest man immer wieder von beispielsweise SET oder ACTUAL und noch ein paar mehr. Diese Indikatoren werden dann vom Konfigurationsskript verstanden und unter einem PageItem dann angzeigt.  
  
  Wollen wir das ganze mal am Bsp. einer Rolladensteuerung darstellen:
* Wir haben im ioBroker z.B. einen Shelly 2.5, mit wir einen Rolladen schon steuern können. Dort gibt es Datenpunkte wie z.B. CLOSE, OPEN, PAUSE und POSITION und noch ein paar mehr.
* Aus der unten aufgeführten Definitionsliste (oder aus dem Konfigurationsskript) müssen wir nun einen passenden Alias Typ suchen. In dem Fall 
  Jalousie. 
* Man beachte die Spalte required, das sind die Datenpunkte, die man mindestens füllen muss.
* Unter Jalousie finden wir Begriffe wie ACTUAL, CLOSE, OPEN, SET und STOP. Diese müssen nun mit den passenden Datenpunkte aus den Shelly Objekten verknüpft werden
* Voila, haben einen konfigurierten Alias

  Schauen wir uns noch den Alias Wettervorhersage an. Diesen benötigen wir ja bei der Installation, damit auf dem Screensaver auch Wetterinfos angezeigt werden. Die Definitionsliste gibt hier ja nur ICON und TEMP an. Wenn man die Wettervorhersage auf dem Screensaver aber aktiviert, gibt es noch viel mehr, was angezeigt werden kann wie: Windgeschwindigkeit, Luftdruck, Regen, UV,.....  
  **Wichtig**: Man kan auch mehr konfigurieren, da wo unterstützt werden die zusätzlichen Datenpunkte dann auch verwendet.

  **Fazit**:  
1. Anhand meines Vorhabens den richtigen Alias-Typ definieren
2. In der Definitionsliste und/oder im Konfigurartionsskript nach dem richtigen Alias suchen
3. Alias anlagen und Datenpunkte verknüpfen, ggf. zusätzliche hinzufügen
4. PageItem konfigurieren

  Wenn ich was vergessen habe, gerne berichten (Kuckuck).

* **Definitionsliste**
![image](https://user-images.githubusercontent.com/99131208/188516164-b0970739-84df-422a-85c2-eb53d444144e.png)  
(Bild & Liste by @Armilar  )


***


## **7.) Hardware-Buttons im Multipress-Mode**

* **Quelle**:
Post [1228](https://forum.iobroker.net/topic/50888/sonoff-nspanel/1228) hier in diesem Thread


* **Beschreibung**:
Man kann die physische Hardware-Buttons auch im Multi-Press Modus betreiben. Es besteht die Möglichkeit Aktionen zu definieren vom Einfachen drücken bis hin zum 5fach drücken.  
Jeder Button sendet per /stat/RESULT "SINGLE", "DOUBLE", "TRIPLE", "QUAD" oder "PENTA". Somit hat man 5 mögliche Schaltzustände pro Button.  

* **Tasmota**: 
Über die Tasmota Konsole muss man für den gewünschten Button einen bestimmten Tasmota Befehl aktivieren, welche die Multipress Funktion aktiviert.  

**Wichtig**:  Ist für den gewünschten Button eine **Rule2** aktiv, muss diese vorher deaktiviert werden.  

Tasmota konsole:  
--> öffnen der Tasmota Konfigurationsoberfläche des Panels, dann auf Konsole und noch einmal auf Konsole 
--> Funktion aktivieren  

```
SetOption73 1
```
![image](https://user-images.githubusercontent.com/99131208/188516304-af95f827-37f0-42c2-8452-87d4ce840efc.png)  
 
(Bild by @Armilar) 

**Wichtig**:  Da ein sechster Klick das WifiConfig 2 ausführt, sollte dabei ebenfalls
```
SetOption1 1
```
zusätzlich ausgeführt werden, um zu verhindern, dass der Wifi Manager ausgeführt wird.  


* **Blockly Skript** (Bild & Skript by @Armilar)
Falls du diese Funktion nutzen möchtest, kannst du das nachfolgende Blockly (siehe Spoiler) gerne verwenden. In der ersten Zeile musst du lediglich deine stat/RESULT anpassen und an den entsprechenden Kommentaren deine Aktoren einbauen.

![image](https://user-images.githubusercontent.com/99131208/188516274-7dff43ae-6534-4ef8-ab04-22f8627ae87f.png) 

[Zum Blockly](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/Hardware-Buttons_Multipress.xml)


**Hinweis**:  Da das Hardware-Buttons sind werden diese extern verarbeitet und nicht über das Konfigurationsskript.  


***

## **8.) Rolladen / Jalousie / Shutter**  
* **Quelle**  
Post [1214](https://forum.iobroker.net/topic/50888/sonoff-nspanel/1214) oder [1301](https://forum.iobroker.net/topic/50888/sonoff-nspanel/1301) und ggf. noch andere im ioBroker Forum.

* **Voraussetzung**  
Ein Bindeglied wie z.B. ein Shelly 2.5 (Pro) ist bereits mit dem ioBroker verbunden un die Datenpunkte dafür sind vorhanden.  
Man findet hierfür diverse Videos, die einem helfen eine Aktor vorzubereiten und mit dem ioBroker zu verbinden.
**Zusätzlich & wichtig**: Der Rolladen lässt sich manuell über die Datenpunkte im ioBroker bereits steuern (siehe Bsp. [1306](https://forum.iobroker.net/topic/50888/sonoff-nspanel/1306)).

* **Alias**  
Wir benötigen einen Alias vom Typ Jalousie mit den Punkten **ACTUAL**, **CLOSE**, **OPEN**, **SET** und **STOP**.
![image](https://user-images.githubusercontent.com/99131208/188631199-7bd4f44c-4992-4e19-8cb2-90e7ef4aab95.png)  
(Bild by @tklein)  


* **Konfigurationsskript**  
Im Konfigurationsskript kann man ein PageItem auf einer **cardEntities** oder **cardGrid hinzufügen**.  
  
  `<PageItem>{ id: "alias.0.Shelly.ShellyShutterTest", icon: "window-shutter", name: "Rolladen test", interpolateColor: true},`  

  
  Auf einer **cardEntities** hat man dqann direkt links drei Symbole für **OPEN**, **STOP** und **CLOSE**. Mit Klick auf den Text gelangt man in eine Subpage (**popupShutter Page***) die zusätzlich einen Slider hat um eine prozentuale Position zu fahren.  

  
  Auf der **cardGrid** hingegen, sieht man das konfigurierte Icon und man gelangt beim Öffnen auf die **popupShutter Page** zur Steuerung.  


***


## **9.) Alias "Taste" für Auswahl eines Radiosenders**

![image](https://user-images.githubusercontent.com/102996011/189345241-471ad500-58ef-4d02-a9c5-90f06d177d39.png)


Hier im Beispiel über den Alexa2-Adapter:

**Anlegen des Alias:**

![image](https://user-images.githubusercontent.com/102996011/189340405-93b83fc7-991b-4098-be2c-eff3ef55b4dd.png)

Es wird im Geräte-Manager ein Alias "Taste erstellt:
![image](https://user-images.githubusercontent.com/102996011/189339115-ed87baba-4893-4ffd-9ae4-cac8f2a8a493.png)

Im Reiter Zustände wird der .SET mit einem Command-Datenpunkt aus dem Alexa2-Adapter verknüpft (XXXXXX für dein Alexa-Device)
![image](https://user-images.githubusercontent.com/102996011/189339841-f26384fe-029c-40af-b233-4b1313185196.png)
Im Anschluss klickst du auf fx (am Ende des Eintrags) und trägst den Sender ein:
![image](https://user-images.githubusercontent.com/102996011/189340836-0027269d-7f1c-47c3-90cf-ca23ef8dfc06.png)

**Einbindung in das TS-Skript:**
![image](https://user-images.githubusercontent.com/102996011/189342043-83ad8834-9326-4fd9-846b-2147f33da723.png)
`<PageItem>{ id: "alias.0.NSPanel_1.Radio.WDR2", icon: "radio", name: "WDR2", onColor: colorRadio}`

***

## **10.) DWD Daten an verschiedene NSPanels schicken**
* **Quelle:**  
Post [1407](https://forum.iobroker.net/topic/50888/sonoff-nspanel/1407) im ioBroker Forum.
* **Voraussetzung:**  
Adapter DWD muss installiert sein.    

* **Blockly:**  

![image](https://user-images.githubusercontent.com/99131208/192108541-d7ad26de-7086-40b7-95e8-c4272f76a4b4.png)  

[Zum Blockly](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/DWD_Daten_Broadcast.xml)  


***

## **11.) PV-Daten Info Seite**  

* **Quelle:**  
Post [1435](https://forum.iobroker.net/topic/50888/sonoff-nspanel/1435?_=1663104710126#) im ioBroker Forum.

* **Die Idee:**
Mit einer PageEntitie eine Infoseite bauen auf der die Daten eine PV-Anlage / Balkonkraftwerk abgebildert werden können.  

* **ioBroker**  
Die Datenpunkte, in der die Daten der PV-Anlage abgegriffen werden können müssen vorhanden sein.  

* **Alias:**  
Für jeden Wert, der auf der Card angezeigt werden soll muss ein Alias vom Typ Info angelgt werden.  
  
![1663099652639-a4dd55ec-79d8-4adb-be2f-5085d7e516aa-image](https://user-images.githubusercontent.com/99131208/192109306-d4683cc4-b6cf-4ca2-9c1e-2c47368bfb40.png)  
  
![1663099722144-a97c0755-8cee-4456-9602-dcb1d5dfc977-image](https://user-images.githubusercontent.com/99131208/192109326-a69db521-9f00-4912-84c9-164bc482ae76.png)  
  
* **Konfigurationsskript:**  
Hier das beispiel, wie die Card dann im Konfigurationsskript hinzugefügt werden muss. Man beachte hier die Besonderheit "**unit: "Wert der Einheit"**", welche dann am Ende der zeile angezeigt wird:  
  
``` 
var PV_Anlage: PageEntities =
{
    "type": "cardEntities",
    "heading": "PV Anlage",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [
        <PageItem>{ id: "alias.0.NSPanel_1.ErsterWertderPVAnlage", name: "aktuelle PV-Leistung", unit: "kWh"},
        <PageItem>{ id: "alias.0.NSPanel_1.ZweiterWertderPVAnlage"},
        <PageItem>{ id: "alias.0.NSPanel_1.DritterWertderPVAnlage"},
        <PageItem>{ id: "alias.0.NSPanel_1.VierterWertderPVAnlage", name: "Mein PV Wert", icon: "solar-power", unit: "W", offColor: MSYellow, onColor: MSYellow, useColor: true}
    ]
};
``` 
  
![image](https://user-images.githubusercontent.com/99131208/192109664-af10660d-923b-4706-b1d4-78431162730a.png)  
  


***

## **12.) Equalizer für cardMedia**

![image](https://user-images.githubusercontent.com/102996011/209372488-1960898c-03a5-4bda-baae-f95e5a0100bd.png)  

Über das Panel werden die in der Liste enthaltenen Werte in einen Datenpunkt (wird durch das TS-Script erzeugt) in 0_userdata geschrieben:
![image](https://user-images.githubusercontent.com/102996011/209374619-c34daff7-5564-4239-a857-f417231bde36.png)  
Das nachfolgende Blockly wertet die Änderungen in diesem Datenpunkt aus und steuert das entsprechende Device.

Die cardMedia ab Release 3.7.0 verfügt über eine Liste zur Steuerung der Klangprofile. Folgendes Beispiel soll verdeutlichen, wie die EQ Steuerung bei Alexa Echo-Devices erfolgen kann. Da jeder ein unterschiedliches Klangverständnis hat oder die Klangkarakteristik der einelnen Speaker sehr unterschiedlich sein kann, sollte der entsprechende Wert für bass/mid/treble je Speaker und Profil entsprechend eingestellt bzw. angepasst werden:

![image](https://user-images.githubusercontent.com/102996011/209371972-5d515c8a-d4f2-407c-8cf7-0364d3fc3528.png)  

[Zum Blockly](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/CardMedia_Equalizer.xml)  
  
  
***

## **13.) Blätterprobleme & direkter Seitenaufruf**  
  
### **13a) Blätterprobleme**  
  
* **Quelle:**  
Gefunden beispielsweise im ioBroker Forum in den Posts [507](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/507) und [610](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/610).
  
* **Problemstellung:**  
Beim durchblättern der Seiten kommt man über die Seite zwei nicht hinaus und man kann auch nicht mehr zurück auf die Seite 1. Man muss immer warten bis der Screensaver aktiv wird und dann kann man mit Glück weiter blättern auf eine andere Unterseite. beim zurückblättern bleibt man aber wieder auf der Seite 2 hängen.  
  
* **Lösung:**  
 
  Im MQTT Adapter des ioBroker prüfen, ob der Haken bei "Nur bei Änderungen publizieren" gesetzt ist oder nicht.  
    
  ![mqtt_publizieren_setting](https://user-images.githubusercontent.com/99131208/209814386-9d5b1f8c-bc71-4b39-80d8-07df1edc4713.png) 
     
  Der haken darf **nicht** gesetzt sein!
  
  
***  
  
### **13b) Seitenaufruf im Alarmfall**  
  
* **Anfrage und Quelle:**  
Aus dem Post [643](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/643) des ioBroker Forums die Anfrage ob es eine Möglichkeit gibt die Seite CardAlarm mit der Pin Eingabe auf dem Panel einzublenden, wenn es zu einem Alarmfall kommt.  
  
* **Lösungsmöglichkeit**  
  
  * Es wird ein Datenpunkt benötigt, in den man via ioBroker eine Anweosung schreiben kann:  
    ![1668112813553-85f91472-8033-4197-a007-99dba1a2d362-image](https://user-images.githubusercontent.com/99131208/209816688-9cc99664-c96e-4929-96b6-36ee650defe2.png)  
  * Ein externes Script muss eine Zeile zusammenbauen (JSON), wobei die 14 im Beispiel eine pageID ist.  
    `{"pagetype": "page", "pageId": 14}`  
    das ganze geht auch für Subpages:  
    `{"pagetype": "subpage","pageId": 2}`  
  * Wie findest du die pageID der z.B. cardAlarm? Du zählst in deiner "export const Config" die Seiten ab 0 beginnend.  
    ![1668113129126-b0a095f5-fab8-48ca-a38d-3483f5949e44-image](https://user-images.githubusercontent.com/99131208/209816873-4f1061a1-abd3-4cf5-b56c-e8a3f6e75af9.png)  
  
Wenn man dieses JSON nun so zusammenbaut und in den Datenpunkt schreibt, dann wird die gewünschte Seite auf dem Panel angezeigt.  
  
  
***
  
### **13c) Seitenaufruf mit einem Hardwarebutton**  
  
Dies wurde bereits im [Punkt 1 - Button entkoppeln](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#1-button-entkoppeln) erklärt.  
  
***  
  
## **14.) NSPanel Temperatursensor für MQTT**    
  
* **Quelle:**  
Post [536](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/536) im ioBroker Forum.  
  
* **FAQ:**  
  Falls jemand den internen Sensor nutzen möchte, mit dieser Regel kann man ihn als MQTT-Objekt anzeigen lassen und im Alias zuordnen:  
  `Rule1 ON ANALOG#Temperature1!=%Var1% DO backlog publish %topic%/stat/Temperature %value%; Var1 %value% ENDON`  
  
  **Aber:** Per Default ist der Temperatursensor bereits in den ursprünglichen Anlage in den Objekten verfügbar:  
  **0_userdata.0.NSPanel.1.Sensor.ANALOG.Temperature**  
  
***
  
## **15.) Zeiteinstellung Host System**  
  
* **Quelle:**  
Post [498](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/498) im ioBroker Forum.  
  
* **FAQ:**  
  * Raspberry:  
    `sudo raspi-config`  
    Punkt 1 und Punkt 3. kann auch [hier](https://www.elektronik-kompendium.de/sites/raspberry-pi/1906291.htm) nachgesehen werden.  
  
***
  
