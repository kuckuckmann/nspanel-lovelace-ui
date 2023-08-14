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
**16.)** NSPanel Relais via Skript steuern  
**17.)** Farben für das TS-Skript  
**18.)** Tasmota Datenpunkte im ioBroker werden nicht gefüllt  
**19.)** Abweichende Uhrzeit  
**20.)** Homatic nonIP Thermostate mit der CardThermo  
**21.)** WLED  
**22.)** Fahrplananzeiger  
**23.)** Shelly DUO Lampen  

  
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
18.11.2022 - Abfallkalender - Beispielpage für TS-Skrpit angepasst  
27.12.2022 - Skripte (Blocklys und JS) wurde in Repository ausgelagert und sind nun in der Wiki nur noch verlinkt  
28.12.2022 - Blätterprobleme & Direkter Seitenaufruf - Erstellt  
28.12.2022 - NSPanel Temperatursensor für MQTT - Erstellt  
28.12.2022 - Zeiteinstellung Host System - Erstellt  
28.12.2022 - NSPanel Relais via Skript steuern - Erstellt  
28.12.2022 - Farben für das TS-Skript - Erstellt  
01.01.2023 - Tasmota Datenpunkte im ioBroker werden nicht gefüllt - Erstellt  
01.01.2023 - Abweichende Uhrzeit - Erstellt  
03.01.2023 - Homatic nonIP Thermostate mit der CardThermo - Erstellt  
04.03.2023 - WLED Konfiguration - Erstellt  
12.03.2023 - Anpassung Hardwarebutton Rule2  
09.04.2023 - Fahrplananzeiger  
14.08.2023 - Shelly DUO lampen  
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

**Beide Hardware-Buttons als Dialog - Die internen Relais werden dabei nicht geschaltet**  
```
Rule2 on Button1#state do Publish SmartHome/%topic%/tele/RESULT {"CustomRecv":"event,button1"} endon on Button2#state do Publish SmartHome/%topic%/tele/RESULT {"CustomRecv":"event,button2"} endon
```  

**Rechter Button Dialog - Linker Button Schalter**  
```
Rule2 on Button1#state do Publish SmartHome/%topic%/tele/RESULT {"CustomRecv":"event,button1"} endon
``` 

**Rechter Button Schalter - Linker Button Dialog**  
```
Rule2 on Button2#state do Publish SmartHome/%topic%/tele/RESULT {"CustomRecv":"event,button2"} endon
```  

Zum Anschalten der Rule  
`Rule2` 1 oder `Rule2 On`  

Zum Ausschalten der Rule  
`Rule2` 0 oder `Rule2 Off`  


* **Konfigurationsskript**:  
**Bis Version 4.0.4:**  
Im Konfigurationsskript benötigt Ihr nun unter der **pages** Definition **buttonxPage**: (x=Nummer des Buttons).
Entweder gebt Ihr hier nun den var/const Name eines bestehenden Grid mit, damit kann man einen Button quasi als Home-Button nutzen, oder man legt einen eigenen Grid auf den Button, welcher dann zuvor definiert werden muss.  
**Ab Version 4.0.4.1:**  
Im Konfigurationsskript benötigt man in der **Config** Definition die Objekte **button1/button2**.
Der Button kann nun über die Eigenschaft **mode** mit drei verschiedenen Funktionen belegt werden. Der Modus **"page"** entspricht dem Verhalten in der Version 4.0.4 und früher. Der Button ruft dann die entsprechende Page oder SubPage auf welche hier angegeben wird.
Im Modus **"toggle"** muss ein Boolean Entity im Feld **"entity"** angegeben werden. Der Button wird dann automatisch den aktuellen Zustand umkehren.
Der Modus **"set"** benötigt ebenfalls eine Zielentity im Feld **"entity"**, welche dann immer beim drücken des Buttons auf den Wert aus dem Feld **"setValue"** gesetzt wird.  
Bsp: 
  ```
  button1: {
      mode: 'toggle',                    // Mögliche Werte wenn Rule2 definiert: 'page', 'toggle', 'set' - Wenn nicht definiert --> mode: null
      page: null,                        // Zielpage - Verwendet wenn mode = page (bisher button1Page)
      entity: '0_userdata.0.zielobjekt', // Zielentity - Verwendet wenn mode = set oder toggle
      setValue: null                     // Zielwert - Verwendet wenn mode = set
  }
  ```


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

   
![Bildschirmfoto 2023-04-25 um 10 11 30](https://user-images.githubusercontent.com/101348966/234215552-92739704-bf84-4792-bccb-f130ec111fd4.png)

  Bei Aktivierung oder Deaktivierung der Alarmanlage wechselt der Status in **arming** oder **pending**. Im Falle einer PIN Falscheingabe gibt es nun auch **triggered**. Da die Verarbeitung der Alarmlogik außerhalb des Skriptes stattfindet, müssen die Datenpunkte auch entsprechend durch das externe Skript weiter getaktet werden


* **Aliase**:  
Die drei Datenpunkte **AlarmPin**, **AlarmState** und **AlarmType** werden in einem Alias vom Typ Feueralarm im Gerätemanager oder Alias Adapter angelegt und dieser Alias wird dann im Konfigurationsskript auf der Alarm-Page verwendet.

  ![image](https://user-images.githubusercontent.com/99131208/188514578-43f08178-b8f0-4d09-8e76-02cbe55d5557.png)

  Alias-Typ Feueralarm:  
  ACTUAL = 0_userdata.0.NSXXXX.Alarm.AlarmState  
  PIN = 0_userdata.0.NSXXXX.Alarm.PIN  
  TYPE = 0_userdata.0.NSXXXX.Alarm.AlarmType  
  PANEL = 0_userdata.0.NSXXXX.Alarm.PANEL  
  
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
  let Alarmseite = <PageAlarm>
    {
        "type": "cardAlarm",
        "heading": "Alarm",
        "useColor": true,
        "subPage": false,
        "items": [
            <PageItem>{ id: 'alias.0.NSPanel.Alarm' }
        ]
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

**Hinweis Verknüpfung mit Alarm - Adapter**:  
es gibt im Forum ein [Post](https://forum.iobroker.net/post/987357) @danny_v1, wo ein Blockly vorgestellt wird, welches eine Verbindung zum Alarm-Adapter herstellt. 

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

   
  ![Bildschirmfoto 2023-05-16 um 21 40 06](https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/d32f11d3-dcca-4433-a957-d899a2ca0cad)


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
let Abfall = <PageEntities>
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
var WLAN = <PageQR> 
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
[Hier ist die aktuelle Definitionsliste](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Table), sie wird stetig erweitert.


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
var PV_Anlage = <PageEntities>
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
  
### **13b) Aus dem ioBroker eine bestimmte Seite auf dem NSPanel öffnen**  
  
* **Anfrage und Quelle:**  
Aus dem Post [643](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/643) des ioBroker Forums die Anfrage ob es eine Möglichkeit gibt die Seite CardAlarm mit der Pin Eingabe auf dem Panel einzublenden, wenn es zu einem Alarmfall kommt.  
  
* **Lösungsmöglichkeit**  
  
  * Es wird ein Datenpunkt benötigt, in den man via ioBroker eine Anweisung schreiben kann. Hierzu wurde der Datenpunkt **0_userdata.0.NSPanel.1.PageNavi** geschaffen:  
    ![1668112813553-85f91472-8033-4197-a007-99dba1a2d362-image](https://user-images.githubusercontent.com/99131208/209816688-9cc99664-c96e-4929-96b6-36ee650defe2.png)  
  * Ein externes Script muss eine Zeile zusammenbauen (JSON), wobei die 14 im Beispiel eine pageID ist.  
    `{"pagetype": "page", "pageId": 14}`  
    das ganze geht auch für Subpages:  
    `{"pagetype": "subpage","pageId": 2}`  
  * Wie findest du die pageID der z.B. cardAlarm?  
    Du zählst in deiner "export const Config" die Seiten ab 0 beginnend.  
    ![209816873-4f1061a1-abd3-4cf5-b56c-e8a3f6e75af9](https://user-images.githubusercontent.com/99131208/210172380-4e58e917-20aa-4f97-8a44-015c2222afee.png)  
    Hier im Beispiel in rot die Ziffern 0 bis 14 zeigen die zu verwendenden PageIDs für **pagetype=page** an. Die cardAlarm (hier Buero_Alarm) hat dann die PageID 14.   
    Folgend dann noch das Beispiel für  **pagetype=subpage**:  
    ![2023-01-01 15_00_31-Window](https://user-images.githubusercontent.com/99131208/210173369-2b299a8d-5f36-4fe5-bed4-7f85ccbcb157.png)  
    **Wichtig**: Die Subpages fangen wieder bei 0 an.
  
Wenn man dieses JSON nun so zusammenbaut und in den Datenpunkt schreibt, dann wird die gewünschte Seite auf dem Panel angezeigt.  
  
  
***
  
### **13c) Seitenaufruf mit einem Hardwarebutton**  
  
Dies wurde bereits im [Punkt 1 - Button entkoppeln](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#1-button-entkoppeln) erklärt.  
  
***  
  
### **13d) Mit den Hardwarebuttons Vor und Zurück navigieren**  
  
* **Quelle:**  
Es gibt im ioBroker Forum verschiedene Posts die auf das Thema eingehen. Zum Beispiel erstmals in Post [1445](https://forum.iobroker.net/topic/50888/sonoff-nspanel/1445), aber auch dann Später noch einmal in Post [1490](https://forum.iobroker.net/topic/50888/sonoff-nspanel/1490).  
  
* **Lösung**:  
  * Tasmota Rule 1 anlegen:  
    `Rule1 on Button1#state do Publish %topic%/tele/RESULT {"CustomRecv":"event,buttonPress2,hwbtn,bPrev"} endon on Button2#state do Publish %topic%/tele/RESULT {"CustomRecv":"event,buttonPress2,hwbtn,bNext"} endon`  
  * Mindestvoraussetzung TS-Skript in der Version: **v3.4.0.3**  
  
*** 
  
### **13e) Seite bei ScreensaverOFF**  
  
* **Quelle:**  
Basierend auf den Post [1493](https://forum.iobroker.net/topic/50888/sonoff-nspanel/1493) des ioBroker Forums.  
  
* **Beschreibung:**  
Wenn der Screensaver nach einer bestimmten Zeit aus geht oder durch eine Aktion beendet wird, so soll die definierte Seite 1 oder eine andere definierte Seite angezeigt werden.  
  
* **Lösung:**
Im Datenpunkt **0_userdata.0.NSPanel.1.ScreensaverInfo.bExitPage** die Seiten ID der gewünschten Seite angeben.  
Die Ermittlung der Seiten ID ist in Artikel [13b](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#13b-seitenaufruf-im-alarmfall) beschrieben.  

  
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
  
## **16.) NSPanel Relais via Skript steuern**  
  
* **Quelle:**  
Post [424](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/424) im ioBroker Forum.  
  
* **Problemstellung:**
Wie kann man vom ioBroker aus die/das Relais des NSPanel (via Skript) schalten?  
  
* **Lösungsvorschlag:**  
  * Zunächst das/die Relais über die Rule 2 entkoppeln (Anleitung [hier](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#1-button-entkoppeln) zu finden)  
  * Das anschalten des Relais kann über einen Steuere-Blockly-Block  
    ![image](https://user-images.githubusercontent.com/99131208/209823415-e3607773-3878-4d09-9185-449eb874e632.png)  
    oder alternativ über setState (JS) erfolgen  
    ![image](https://user-images.githubusercontent.com/99131208/209823475-46b0f6f6-a818-41ca-9223-f610d00b39b8.png)  
    Kann je nach Konfiguration auch POWER1 oder POWER2 sein.
  
* **Erklärungen:**  
  Die Tasmota Rule2 ist dafür da, die Buttons als Favoritenseiten zu benutzen. In diesem Zusammenhang werden keine Relays genutzt. Natürlich kann man das auch auftrennen, in dem man eine ButtonPage benutzt und einen physischen Hardware-Button.  
  
  Stat ist nur der Status des Buttons - den kannst du über stat nicht verändern. Wenn der POWER1 oder/und POWER2 aktiv gesteuert werden soll, muss dass über cmnd erfolgen.  
  
  ![image](https://user-images.githubusercontent.com/99131208/209823303-08a09126-6a22-4ea7-b0c2-f49d78bddef9.png)  
  
* **Zusätzliche Infos:**  
  **Panel:** über ALIAS Thermostat  
    * Über eine Thermostatpage wird ein Setpoint (Solltemperatur) in einem Datenpunkt in 0_userdata.0... gesteuert.
    * Ebenfalls gibt es entweder den internen oder den externen Raumsensor, der die aktuelle Raumtemperatur beinhaltet.
  
  **Externes Script:**  
    * Eventuell ist ein weiterer Datenpunkt erforderlich, der einen Offset zur Temperatur beinhaltet.  
    * Wenn Ist-Raumtemperatur +- Offset < Setpoint-Temperatur --> Relay auf 1 (an)  
    * Wenn Ist-Raumtemperatur +- Offset > Setpoint-Temperatur --> Relay auf 0 (aus)  
  
***
  
## **17.) Farben für das TS-Skript**  
  
* **Quellen:**  
Hierzu gibt es mehrere Beiträge im ioBroker Forum. U.a. in den Posts [116](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/116), [419](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/419) und [458](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/458)  
  
* **Erklärung:**  
Das TS-Script benutzt so manche Umrechnung von Farben aller Art. Die von euch benötigte ist aber diese Funktion und es stimmt - es ist nicht "decimal", sondern "decimal 565". Siehe auch [https://nextion.tech/instruction-set/#s5](https://nextion.tech/instruction-set/#s5).  
  
  `function rgb_dec565(rgb: RGB): number {
    return ((Math.floor(rgb.red / 255 * 31) << 11) | (Math.floor(rgb.green / 255 * 63) << 5) | (Math.floor(rgb.blue / 255 * 31)));
}`  
  
* **Blockly farbrechner:**  
Für alle die mit dem Coding nicht klarkommen - habe ich es mal in ein Blockly geschoben. Ihr könnt es nach belieben verformen, verändern oder sonst etwas machen. Es wird aber in diesem Fall nur aus rot, grün und blau eine dec565 erzeugen (als Warnung 😉 im Log)  
  
  Farbe aussuchen in z.B. [www.rapidtables.com](https://www.rapidtables.com/web/color/RGB_Color.html), dann die Decimal Code R,G,B in die Variablen red, green, blue übertragen (Hier im Beispiel für weiß - 255 255 255).  
  ![image](https://user-images.githubusercontent.com/99131208/209830455-134355bc-39e8-4fcb-a0d9-ce48be3a83e6.png)  
  [Zum Blockly](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/RGB_Dec565_rechner.xml)
  
  Ergebnis ![image](https://user-images.githubusercontent.com/99131208/209830527-da443317-0717-4145-9dec-774c7371a72e.png)  
  16-bit 565 Colors are in decimal values from 0 to 65535  
 
* **ColorPicker:**
@Jobr99 war so nett und hat einen ColorPicker gebaut, den man [hier](https://docs.nspanel.pky.eu/notifications/#color-picker) finden kann.   
![image](https://user-images.githubusercontent.com/99131208/209831398-267de681-fb97-4a9d-87a5-abcd31b4b2a4.png)  
  
* **Decimal-Code:**  
Um herauszufinden, welche Farbe der Dezimal-Code hat kannst du [nodtem66.github.io](https://nodtem66.github.io/nextion-hmi-color-convert/index.html) verwenden  
  
***  
  
## **18.) Tasmota Datenpunkte im ioBroker werden nicht gefüllt**  
  
* **Quelle**  
ioBroker Forum Posts ab [1412](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/1412)  
  
* **Problem:**  
Die vom TS-Skript angelegten Datenpunkte im ioBroker werden nicht mit den erwarteten Werten gefüllt.  
![image](https://user-images.githubusercontent.com/99131208/210181378-28df19bb-aba9-4769-84f5-4d8f2519b05a.png)  
  
* **Ursache:**  
  Im NSPanel ist für den Tasmotazugriff ein Webpasswort gesetzt  
![image](https://user-images.githubusercontent.com/99131208/210184629-6658c17e-6bc9-43f3-bc6f-f94f6d87f0aa.png)  
  
* **Lösung:**  
In einer neuen Version wird es für Username und Passwort neue Datenpunkte geben.  
Bis dahin kann man im Skript die Zeile  
**url: `http://${get_current_tasmota_ip_address()}/cm?cmnd=Status0` **  
![image](https://user-images.githubusercontent.com/99131208/210181498-47b761a8-388c-479c-9b1a-ca74f9c71b3e.png)  
durch mit folgendem ersetzen:  
`http://${get_current_tasmota_ip_address()}/cm?user=admin&PASSWORD&cmnd=Status0`  
Dabei ist admin = gesetzter Username und PASSWORT = das gesetzte Passwort.
  
* **DEV Status:**  
In der aktuellen Dev version schon drin:  
`const tasmota_web_admin_user = 'admin'; // ändern, falls der User im Tasmota umbenannt wurde`  
`const tasmota_web_admin_password = '';  // setzten, falls "Web Admin Password" in Tasmote vergeben`
***
  
## **19.) Abweichende Uhrzeit**  
  
* **Quelle:**  
Im ioBroker Forum Post [1428](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/1428)  und ab Post [1491](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/1491), Post [1500](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/1500)  
  
* **Problem:**  
Die Uhrzeit auf dem Display weicht von der Uhrzeit in der Tasmota Console ab.  
  
* **Ursache:**  
Es wird nicht die Tasmotazeit verwendet, sondern die ioBroker-Zeit. Wenn diese anders ist, dann ist im ioBroker wahrscheinlich kein NTP-Server aktiv/eingestellt.  
Sollte keine automatische Zeitsynchronisation (NTP) gewollt sein, kann man die Betriebssystem (System) Zeit auch manuell einstellen.  
  
* **Hilfestellung:**  
![image](https://user-images.githubusercontent.com/99131208/210181801-214169c1-3923-4bed-8b47-498711da3cd3.png)  
[Zum Blockly](https://github.com/joBr99/nspanel-lovelace-ui/tree/main/ioBroker/Blockly/Uhrzeit_Logging.xml)  
  
* **Lösung:**  
  
  * NTP Zeitsynchronisation konfigurieren  
  * Bei der Verwendung einer VM (z.B. Proxmox), die Systemzeit (und Standort auf Berlin) korrigieren. In der Regel sollte danach ein Neustart des Betriebssystems erfolgen  
  * Eine veraltete nodeJS-Version könnte das Problem sein... Sollte in der Konsole mit `node -v` keine `16.19.0` herauskommen, dann sollte in jedem Fall gehandelt werden.  
    * Das Release beginnt mit 16.X.X, dann einfach durchführen:  
      1. sudo apt-get update  
      2. sudo apt-get dist-upgrade  
      3. sudo reboot  
    * Das Release beginnt mit 14.X.X oder noch kleiner:  
      Jetzt ist zwingend das nodeJS auf einen neuen Stand zu bringen:
      Anleitung siehe hier: [https://forum.iobroker.net/topic/35090/howto-nodejs-installation-und-upgrades-unter-debian](https://forum.iobroker.net/topic/35090/howto-nodejs-installation-und-upgrades-unter-debian)  
  
***
  
## **20.) Homatic nonIP Thermostate mit der CardThermo**  
  
* **Quelle:**  
Post [1220](https://forum.iobroker.net/topic/58170/sonoff-nspanel-mit-lovelace-ui/1220) im ioBroker Forum.  
Hier geht es um Homatic Homematic HM-CC-RT-DN.  
  
* **Datenpunkte:**  
Es werden mehrere Datenpunkte benötigt, um diese dann später in einem Alias zu verknüpfen. Die Datenpunkte sehen beispielsweise so aus:  
  > (DP 01) 0_userdata.0.Homatic.Thermostate.OEQ0667828.4.Automatic (boolean)  
  > (DP 02) 0_userdata.0.Homatic.Thermostate.OEQ0667828.4.Manual (boolean)  
  > (DP 03) 0_userdata.0.Homatic.Thermostate.OEQ0667828.4.Boost (boolean)  
  > (DP 04) 0_userdata.0.Homatic.Thermostate.OEQ0667828.4.Setpoint (number)  
  > (DP 05) 0_userdata.0.Homatic.Thermostate.OEQ0667828.4.Lowbat (boolean)  
  > (DP 06) 0_userdata.0.Homatic.Thermostate.OEQ0667828.4.Maintain (boolean)  
  
* **Alias:**  
Es wird ein Alias vom Typ Thermostat benötigt. Dabei müssen die zuvor erstellten Datenpunkte folgendermaßen verknüpft werden:  
  * SET auf DP 04
  * ACTUAL auf auf den bevorzugten Raumtemperatursensor
  * BOOST auf DP 03  
Zusätzlich muss angelegt werden:  
  * LOWBAT auf DP 05
  * MAINTAIN auf DP 06  
  
Weiterhin im ALIAS unter ![image](https://user-images.githubusercontent.com/99131208/210432321-10fdc06c-0675-48b2-88ff-f674d2444f64.png) auf **Control_Mode** im Adapter mappen:  
![image](https://user-images.githubusercontent.com/99131208/210432487-198cf58a-5174-4cee-af65-3b67d37d0ae4.png)  
  > 0 = AUTO  
  > 1 = MANUAL  
  > 2 = PARTY  
  > 3 = BOOST  
  
* **TS-Skript:**  
  
`let WZ_Heizung = <PageThermo>   
{  
    "type": "cardThermo",  
    "heading": "WZ Thermostat",  
    "useColor": true,  
    "subPage": false,  
    "parent": undefined,  
    "items": [<PageItem>{ id: "alias.0.NSPanel1.HeizungWZ", minValue: 50, maxValue: 300 }]  
};`  
    
* **Blocky Skript:**  
  
![image](https://user-images.githubusercontent.com/99131208/210435220-bcccdc92-d348-4f1b-9a67-e5ee0f5c0ba8.png)  
  
[Zum Blockly](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/Homatic_nonIP_Thermostate.xml)  
  
***  
  
## **21.) WLED**  
  
* **Beschreibung:**  
Hier geht es Darum die im Beispiel TS-Skript schon aufgeführte Seite **WLED**  einmal Beispielsweise zu konfigurieren.  Wer Hilfe bei der Einrichtung von WLED benötigt, der kann sich zum Beispiel an den Videos von @klein0r @haus-automatisierung  >>[Zum Youtube Kanal](https://www.youtube.com/@haus_automation/featured)<< Anregungen holen, er hat zu dem Thema schon drei Videos produziert.  
  
* **Voraussetzungen:**  
  * Funktionierender WLED Adapter im ioBroker  
  * Funktionierende WLED Leuchten, die bereits verbunden sind und sich schon über die APP, die Webseite und den ioBroker steuern lassen
  * Hilfs-Datenpunkte
  * Mehrere Aliase  
  * Ein neues JS-Skript (statt Blockly)  
  * Eine TS-Skript Seite  
  
* **Konfiguration:**  
WLED bietet eine Vielzahl an Konfigurations- und Einstellungsmöglichkeiten. Viele lassen sich auch auf dem NSPanel abbilden, aber nicht alle. Für unser Konfigurationsbeispiel haben wir uns die Funktionen **Power**, **Timer**, **Synch**, **Presets**, **Effects** und **Colors** ausgesucht. Dabei werden Presets, Effects und Colors auf Grund der Möglichen Auswahl an unterschiedlichen Funktionen mit einem inselPopup realisiert.  
  
  * **Hilfs-Datenpunkte:**  
    Für die drei inselPopup Lösungen benötigen wir jeweils einen Datenpunkt. Diese werden unter dem Hauptordner **0_userdata.<Euer Pfad>.WLED** angelegt. 
    Wir benötigen einen Datenpunkt **Colors**, **Effects** und **Presets** als nummerisch.  
    ![image](https://user-images.githubusercontent.com/99131208/210663827-fcf32d02-6971-42b0-840e-e5a4b136870b.png)  

  * **Aliase:**  
    * Die drei Hilfs-Datenpunkte werden mit einem Alias **Tastensensor** wie [hier](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#tastensensor----popupinsel-channel-buttonsensor) beschrieben verknüpft  
    * Für **Power**, **Timer** und **Synch** nutzen wir jeweils einen Alias **Licht** und verknüpfen ACTUAL und SET jeweils mit den zugehörigen WLED Objekten:  
    **Power**    -->  **wled.0.2cf43212d23c.on**  
    **Timer**    -->  **wled.0.2cf43212d23c.nl.on**  
    **Synch**    -->  **wled.0.2cf43212d23c.udpn.send**  
  
  *  **JS-Skript:**  
    [Hier](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/WLED.js) findet Ihr ein JS-Skript, welches Ihr im ioBroker unter Skripte als JS anlegen müsst. In dem Skript gibt es zwei zu konfigurierende Datenpunkte:  
    * **Pfad zum WLED-Modul**: Entspricht in unserem Beispiel hier **wled.0.2cf43212d23c.**, also dem Pfad zur WLED Objekt-Instanz.  
    * **Pfad zu 0_userdata Datenpunkten**: Der Pfad zum Ordner unter **0_userdata.0** in dem die drei Hilfs-Datenpunkte im Ordner WLED **0_userdata.0.NSPanelOwn.WLED.** angelegt wurden.  
      ![image](https://user-images.githubusercontent.com/99131208/210668387-ba3a8759-46c1-4895-ab76-ca5f2095659c.png)  
  
    Weiterhin gibt es noch die **presetList**, **colorsList** und **effectsList**, welche in den eckigen Klammern eingefasst die Werte aus WLED für die verschiedenen Funktionen beherbergt. **Wichtig**: Die Werte in den eckigen Klammern müssen hier genau denen im PageItem des TS-Skriptes entsprechen!  
    **Hinweis**: Bitte darauf achten, das die Anzahl der Zeichen innerhalb der eckigen Klammern nicht mehr als 900 Zeichen sind.  
    ![image](https://user-images.githubusercontent.com/99131208/210668543-6c12f1da-9828-4646-9f39-68c3c0326f41.png)  
  
  * **TS-Skript**  
  Im NSPanelTS.ts ist eine Beispielseite für WLED enthalten. Diese haben wir in unserer Konfiguration geringfügig abgeändert. Das Beispiel beinhaltet eine Konfiguration für verschiedene Segmente, diese haben wir erstmal durch den Timer ersetzt. Segmente folgt in einem weiteren Schritt und wird dann auch hier in der Wiki hinzugefügt. Aus dem Grund geht es mit der Konfiguration aus dem Beispiel hier weiter:  
  ```
  let WLED = <PageGrid>
  {
      "type": "cardGrid",
        "heading": "WLED",
      "useColor": true,
      "subPage": false,
      "parent": Index01,
      "items": [
          <PageItem>{ id: "alias.0.WLED.POWER", name: "Power", icon: "power", onColor: Blue, offColor: HMIOff},
          <PageItem>{ id: "alias.0.WLED.Synch", name: "Sync", icon: "sync", onColor: Blue, offColor: White},
		<PageItem>{ id: "alias.0.WLED.Timer", name: "Timer", icon: "moon-waxing-crescent", onColor: Blue, offColor: White},
          <PageItem>{ id: "alias.0.WLED.Presets", icon: "heart-outline", name: "Presets", onColor: White, modeList: ['Preset 0', 'Add Preset']},
          <PageItem>{ id: "alias.0.WLED.Colors", icon: "palette", name: "Colors", onColor: White, 
                      modeList: ['Default', '* Color 1', '* Color Gradient', '* Colors 1&2', '* Colors Only', '* Random Cycle', 'Analogus','April Night', 'Aqua Flash', 'Atlantica', 'Aurora', 'Beach', 'Beech', 'Blink Red', 'Breeze', 'C9', 'C9 New', 'Candy', 'Candy2', 'Cloud', 'Cyane', 'Departure', 'Drywet', 'Fairy Reaf', 'Fire', 'Forest', 'etc']},
          <PageItem>{ id: "alias.0.WLED.Effects", icon: "emoticon-outline", name: "Effects", onColor: White, 
                      modeList: ['Solid', 'Android', 'Aurora', 'Blends', 'Blink', 'Blink Rainbow', 'Bouncing Balls','Bpm', 'Breathe', 'Candle', 'Candle Multi', 'Candy Cane', 'Chase', 'Chase 1', 'Chase 2', 'Chase 3', 'Chase Flash', 'Chase Flash Rnd', 'Chase Rainbow', 'Chase Random', 'Chunchun', 'Colorful', 'Colorloop', 'Colortwinkles', 'Colorwaves', 'Dancing Shadows', 'etc']},
          //<PageItem>{ id: "alias.0.NSPanel_1.WLED.Example.Segments", icon: "layers", name: "Segments", onColor: White, modeList: ['Segment 0', 'Add Segment']},
      ]
  };
  ```  
  
  * **Ausblick**  
    Dies ist er erste Schritt. Wir werden noch weitere Funktion versuchen abzubilden und ein nächster Meilenstein wäre eine Unterseite mit anzubauen, in der man zum Beispiel die Helligkeit, Farbtiefe, etc. einstellen kann. Eventuell auch noch eine erweiterte Farbauswahl. Also ab und an hier mal einen Blick rein werfen ;-)
    
***
  
## **22.) Fahrplananzeiger**  
  
* **Beschreibung:**  
Der Fahrplananzeiger kann 4 aktuelle Abfahrten vom Adapter Fahrplan (Abfahrtstafel) anzeigen. Angezeigt wird das Icon je nach Fahrzeugtyp, das Ziel und die Abfahrtzeit. Zusätzlich kann eine PopupNotifypage bei Verspätung aktiviert werden.  
  
* **Voraussetzungen:**  
  * Fahrplan Adapter
  * externe TS-Script von [tt-tom17/myScript](https://github.com/tt-tom17/MyScripts/tree/main/Sonoff_NSPanel)
  
* **Datenpunkte:**  
Werden durch das externe Script angelegt.  
  
* **PageConfig:**  
```
let FahrplanEntities = <PageEntities>  
{  
    'type': 'cardEntities',  
    'heading': 'Haltestelle',  
    'useColor': true,  
    'items': [  
        <PageItem>{ id: AliasPath + 'FahrplanAnzeiger.Haltestelle0.Abfahrt0'},  
        <PageItem>{ id: AliasPath + 'FahrplanAnzeiger.Haltestelle0.Abfahrt1'},  
        <PageItem>{ id: AliasPath + 'FahrplanAnzeiger.Haltestelle0.Abfahrt2'},  
        <PageItem>{ id: AliasPath + 'FahrplanAnzeiger.Haltestelle0.Abfahrt3'},  
        <PageItem>{ id: AliasPath + 'FahrplanAnzeiger.Haltestelle0.Abfahrt4'},  
        <PageItem>{ id: AliasPath + 'FahrplanAnzeiger.Haltestelle0.Abfahrt5'}  
    ]  
};
```  
  
## **22.) Shelly DUO Lampen (@Work)**  
  
* **Beschreibung:**  
  Shelly DUO RGBW Lampen bringen eine Eigenschaft mit, dass man mit einem separaten Schalter zwischen Color und White hin- und her-schalten muss.  
  Diese Funktion wurde bisher über das popupLight nicht abgedeckt. Um dies möglich zu machen wurden Anpassungen vorgenommen. So kann man nun in der popupLight auch ein inSel Popup nutzen, in dem man beispielsweise zwischen den Modi schalten kann, aber auch um beispielsweise Presets zu definieren und via weiterer Skripte zu laden.  
  
* **Voraussetzung**  
  * Das [NsPanelTs.ts Skript](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/NsPanelTs.ts) in mindestens der Version 4.1.4.4  
  * Einen neuen manuellen Datenpunkt für das **inSelpopup**  
  * Ein blockly für die Steuerung des inSelPopups und den Switch zwischen Color und White  
  * Ein Alias für RGBW-Einzel  
  * Schalterkonfiguration im TS-Skript  

* **Konfiguration**  
  


  
***  