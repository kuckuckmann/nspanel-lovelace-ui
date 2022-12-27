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



<details>
  <summary>Java Skript</summary>  

```
const idAbfalliCal = 'ical.1'; // iCal Instanz zum Abfallkalender
const idZeichenLoeschen = 14; // x Zeichen links vom String abziehen, wenn vor dem Eventname noch Text steht z.B. Strassenname; Standard = 0
const idRestmuellName ='Hausmüll'; // Schwarze Tonne
const idWertstoffName = 'Gelber Sack'; // Gelbe Tonne / Sack
const idPappePapierName = 'Papier';  // Blaue Tonne
const idBioabfaelleName = 'Biomüll'; // Braune Tonne
 
 
var i, Muell_JSON, Event2, Color = 0;
 
for (i = 1; i <= 4; i++) {
    if (!existsState('0_userdata.0.Abfallkalender.' + parseFloat(i) + '.date')) {
        log(i + '.date nicht vorhanden, wurde erstellt');
        createState('0_userdata.0.Abfallkalender.' + parseFloat(i) + '.date', '',
            {
                name: parseFloat(i) + '.date',
                role: 'state',
                type: 'string',
                read: true,
                write: true,
                def: ''
            });
    };
    if (!existsState('0_userdata.0.Abfallkalender.' + parseFloat(i) + '.event')) {
        log(i + '.event nicht vorhanden, wurde erstellt');
        createState('0_userdata.0.Abfallkalender.' + parseFloat(i) + '.event', '',
            {
                name: parseFloat(i) + '.event',
                role: 'state',
                type: 'string',
                read: true,
                write: true,
                def: ''
            });
    };
    if (!existsState('0_userdata.0.Abfallkalender.' + parseFloat(i) + '.color')) {
        log(i + '.color nicht vorhanden, wurde erstellt');
        createState('0_userdata.0.Abfallkalender.' + parseFloat(i) + '.color', 0,
            {
                name: parseFloat(i) + '.color',
                role: 'state',
                type: 'number',
                read: true,
                write: true,
                def: 0
            });
    };
}
 
function subsequenceFromStartLast(sequence, at1) {
    var start = at1;
    var end = sequence.length;
    return sequence.slice(start, end);
}
 
on({ id: idAbfalliCal + '.data.table', change: "ne" }, async function () {
 
    for (i = 0; i <= 3; i++) {
        Muell_JSON = getState(idAbfalliCal + '.data.table').val;
        setStateDelayed((['0_userdata.0.Abfallkalender.', parseFloat(i) + 1, '.date'].join('')), getAttr(Muell_JSON, (String(i) + '.date')), false, parseInt(((0) || "").toString(), 10), false);
        Event2 = subsequenceFromStartLast(getAttr(Muell_JSON, (String(i) + '.event')), idZeichenLoeschen);
        setStateDelayed((['0_userdata.0.Abfallkalender.', parseFloat(i) + 1, '.event'].join('')), Event2, false, parseInt(((0) || "").toString(), 10), false);
        if (Event2 == idRestmuellName) {
            Color = 33840;
        } else if (Event2 == idBioabfaelleName) {
            Color = 2016;
        } else if (Event2 == idPappePapierName) {
            Color = 31;
        } else if (Event2 == idWertstoffName) {
            Color = 65504;
        }
        setStateDelayed((['0_userdata.0.Abfallkalender.', parseFloat(i) + 1, '.color'].join('')), Color, false, parseInt(((0) || "").toString(), 10), false);
    }
});
```
</details>  



Blockly Skript (by @Armilar):  
  
1 = Hier muss der Pfad zum ICal Adapter zum Punkt **ical.0.data.table** eigestellt werden. Achtet auf die Instanznummer beim Adapter  
2 = Muss nur angepasst werden, wenn Eure Datenpunkte nicht unter **0_userdata.0.Abfallkalender.** liegen  
3 = Die Bezeichnungen der Abfallbehälter in Eurem Kalender. Die Namen müssen passen, das mit das Parsen funktioniert. Tipp: Die Ziffern bei "setze Color auf ....." sind die Farbcodierungen im Dezimalsystem.  
4 = Zeichen links vom String abziehen, wenn vor dem Eventname noch Text steht z.B. Strassenname; Standard = 1.  

![image](https://user-images.githubusercontent.com/99131208/188515546-1c2b3048-0d5c-427a-b70c-aab035eeaab4.png)
![image](https://user-images.githubusercontent.com/99131208/188515563-bc6a65a2-4e07-454c-8038-f04366d20516.png)



<details>
  <summary>Blockly Skript</summary>  

 ```
<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="h}CE-n1l`S|gRf(0K%./">i</variable>
    <variable id="j5C=K+Z.E:im1#q:;A=6">Muell_JSON</variable>
    <variable id="^:v=Yb?;aM;Z[}4jCF3-">Event</variable>
    <variable id="9^)S?J=tLkC7cUWc-u9w">Color</variable>
  </variables>
  <block type="on_ext" id="aFeZac36,?)=rfMg%3T|" x="38" y="-287">
    <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
    <field name="CONDITION">ne</field>
    <field name="ACK_CONDITION"></field>
    <value name="OID0">
      <shadow type="field_oid" id="GSzQ}epUa))me3m8yyuD">
        <field name="oid">ical.1.data.table</field>
      </shadow>
    </value>
    <statement name="STATEMENT">
      <block type="controls_for" id="wduAM(OBPzLJ@bfYAK5%">
        <field name="VAR" id="h}CE-n1l`S|gRf(0K%./">i</field>
        <value name="FROM">
          <shadow type="math_number" id="HK~R2U|`xb$U5W+tsHpN">
            <field name="NUM">0</field>
          </shadow>
        </value>
        <value name="TO">
          <shadow type="math_number" id="Ed[L/:1e9-cwxrRaZiIv">
            <field name="NUM">3</field>
          </shadow>
        </value>
        <value name="BY">
          <shadow type="math_number" id="o@5kngFiPpvl5dGo@Q$9">
            <field name="NUM">1</field>
          </shadow>
        </value>
        <statement name="DO">
          <block type="variables_set" id="0T)vK0k8aikvg7mF6XHo">
            <field name="VAR" id="j5C=K+Z.E:im1#q:;A=6">Muell_JSON</field>
            <value name="VALUE">
              <block type="get_value" id="1~kG;UHn$nw2zzbfOIT]">
                <field name="ATTR">val</field>
                <field name="OID">ical.1.data.table</field>
              </block>
            </value>
            <next>
              <block type="control_ex" id="UAu,2OBRJp9~Nzyxouyu">
                <field name="TYPE">false</field>
                <field name="CLEAR_RUNNING">FALSE</field>
                <value name="OID">
                  <shadow type="field_oid" id="J_|uu;{e44n5Z-;qE+hP">
                    <field name="oid">Object ID</field>
                  </shadow>
                  <block type="text_join" id="8/|eHqk))j9Po-O*mK`e">
                    <mutation items="3"></mutation>
                    <value name="ADD0">
                      <block type="text" id="Zp8GRfdfXujkeM41=PeZ">
                        <field name="TEXT">0_userdata.0.Abfallkalender.</field>
                      </block>
                    </value>
                    <value name="ADD1">
                      <block type="math_arithmetic" id="$!!l@[eJ~4Kdb5/Imo.X">
                        <field name="OP">ADD</field>
                        <value name="A">
                          <shadow type="math_number" id="zaU15{yD43xkuY@?)RY(">
                            <field name="NUM">1</field>
                          </shadow>
                          <block type="variables_get" id="o3pJ(+3KE~Co%u-dy.:W">
                            <field name="VAR" id="h}CE-n1l`S|gRf(0K%./">i</field>
                          </block>
                        </value>
                        <value name="B">
                          <shadow type="math_number" id="_LBb[#z%M$n0~1Y}~8w+">
                            <field name="NUM">1</field>
                          </shadow>
                        </value>
                      </block>
                    </value>
                    <value name="ADD2">
                      <block type="text" id="Vt#-b{iDzusQQx]#0%0,">
                        <field name="TEXT">.date</field>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="VALUE">
                  <shadow type="logic_boolean" id="/y1w}eely@o.gl$]#)o=">
                    <field name="BOOL">TRUE</field>
                  </shadow>
                  <block type="get_attr" id="p~0A1{eb$lD~.9`9R4K)">
                    <value name="PATH">
                      <shadow type="text">
                        <field name="TEXT">0.date</field>
                      </shadow>
                      <block type="text_join" id="DDs!.^n(V7=A_TK}DFQt">
                        <mutation items="2"></mutation>
                        <value name="ADD0">
                          <block type="variables_get" id="k1+Dybgb:u2y9v57OrCg">
                            <field name="VAR" id="h}CE-n1l`S|gRf(0K%./">i</field>
                          </block>
                        </value>
                        <value name="ADD1">
                          <block type="text" id="EXgB=?B}IKiUdQ.2tKoa">
                            <field name="TEXT">.date</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="OBJECT">
                      <block type="variables_get" id="dzLb1f^T!(MM,d=cYU9y">
                        <field name="VAR" id="j5C=K+Z.E:im1#q:;A=6">Muell_JSON</field>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="DELAY_MS">
                  <shadow type="math_number" id="f8q~r@+q|8Kov#3EufsI">
                    <field name="NUM">0</field>
                  </shadow>
                </value>
                <next>
                  <block type="variables_set" id="E[W-)N[vKeufX{v$B[]p">
                    <field name="VAR" id="^:v=Yb?;aM;Z[}4jCF3-">Event</field>
                    <value name="VALUE">
                      <block type="text_getSubstring" id="YU_Q05y^+I.IzV[c9h9B" inline="false">
                        <mutation at1="true" at2="false"></mutation>
                        <field name="WHERE1">FROM_START</field>
                        <field name="WHERE2">LAST</field>
                        <value name="STRING">
                          <block type="get_attr" id=":/^m9o]3:=L%$4[9$f]7">
                            <value name="PATH">
                              <shadow type="text">
                                <field name="TEXT">0.event</field>
                              </shadow>
                              <block type="text_join" id="*MaT-W83R/Y5`?QCQNec">
                                <mutation items="2"></mutation>
                                <value name="ADD0">
                                  <block type="variables_get" id="l5d$/glqMm3~+YA`5]wg">
                                    <field name="VAR" id="h}CE-n1l`S|gRf(0K%./">i</field>
                                  </block>
                                </value>
                                <value name="ADD1">
                                  <block type="text" id="$+g0XH}$`2`+{B}s3ID@">
                                    <field name="TEXT">.event</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <value name="OBJECT">
                              <block type="variables_get" id="nSDdx_!gO45lc4.$`wI`">
                                <field name="VAR" id="j5C=K+Z.E:im1#q:;A=6">Muell_JSON</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <value name="AT1">
                          <block type="math_number" id="ic:P:#_w68q^w]#/;w+K">
                            <field name="NUM">9</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <next>
                      <block type="control_ex" id="^[032{A//-EpUE6lh7ml">
                        <field name="TYPE">false</field>
                        <field name="CLEAR_RUNNING">FALSE</field>
                        <value name="OID">
                          <shadow type="field_oid">
                            <field name="oid">Object ID</field>
                          </shadow>
                          <block type="text_join" id="`@U%x4KdNV~Y0I`#+,BB">
                            <mutation items="3"></mutation>
                            <value name="ADD0">
                              <block type="text" id="Rk[N`gae|lr/9FXmY!no">
                                <field name="TEXT">0_userdata.0.Abfallkalender.</field>
                              </block>
                            </value>
                            <value name="ADD1">
                              <block type="math_arithmetic" id="=RY5pU%/0M!J;{^z81qr">
                                <field name="OP">ADD</field>
                                <value name="A">
                                  <shadow type="math_number">
                                    <field name="NUM">1</field>
                                  </shadow>
                                  <block type="variables_get" id="TbkkwM2BKh^+;KTQY3C]">
                                    <field name="VAR" id="h}CE-n1l`S|gRf(0K%./">i</field>
                                  </block>
                                </value>
                                <value name="B">
                                  <shadow type="math_number" id="e,-Pz1Hy!V:=8S,tHo`:">
                                    <field name="NUM">1</field>
                                  </shadow>
                                </value>
                              </block>
                            </value>
                            <value name="ADD2">
                              <block type="text" id="SApnes6}k9wDi243W2xp">
                                <field name="TEXT">.event</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <value name="VALUE">
                          <shadow type="logic_boolean" id="70uxCt~?y`hOTCs:tJ^~">
                            <field name="BOOL">TRUE</field>
                          </shadow>
                          <block type="variables_get" id="}@7(YP=fmA0l@:FJS$v#">
                            <field name="VAR" id="^:v=Yb?;aM;Z[}4jCF3-">Event</field>
                          </block>
                        </value>
                        <value name="DELAY_MS">
                          <shadow type="math_number" id="@JEhP_3fysDQ6a_x:ILm">
                            <field name="NUM">0</field>
                          </shadow>
                        </value>
                        <next>
                          <block type="controls_if" id="r,.`4GPI|(([[.76Cft~">
                            <mutation elseif="3"></mutation>
                            <value name="IF0">
                              <block type="logic_compare" id="d4g.Ts.`^;_R!bu)T_~|">
                                <field name="OP">EQ</field>
                                <value name="A">
                                  <block type="variables_get" id="tC!eDI_BV-hGgDc@kuPc">
                                    <field name="VAR" id="^:v=Yb?;aM;Z[}4jCF3-">Event</field>
                                  </block>
                                </value>
                                <value name="B">
                                  <block type="text" id="?3tZotX[hHq9HGFsA(x|">
                                    <field name="TEXT">Reststoff</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <statement name="DO0">
                              <block type="variables_set" id="FXPSk]#;ZliNOBw7bVC8">
                                <field name="VAR" id="9^)S?J=tLkC7cUWc-u9w">Color</field>
                                <value name="VALUE">
                                  <block type="math_number" id="-6AJ8U932(j5LuWN@Sp,">
                                    <field name="NUM">33840</field>
                                  </block>
                                </value>
                              </block>
                            </statement>
                            <value name="IF1">
                              <block type="logic_compare" id=":{8uXg8tzuFNCxedDJ:F">
                                <field name="OP">EQ</field>
                                <value name="A">
                                  <block type="variables_get" id="0A}m@W~711B2u){_B8uP">
                                    <field name="VAR" id="^:v=Yb?;aM;Z[}4jCF3-">Event</field>
                                  </block>
                                </value>
                                <value name="B">
                                  <block type="text" id="x,Cz(O2e|co^a7rJEdO7">
                                    <field name="TEXT">Biotonne</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <statement name="DO1">
                              <block type="variables_set" id="Y#|WXlt|w+`5h3B`VI]*">
                                <field name="VAR" id="9^)S?J=tLkC7cUWc-u9w">Color</field>
                                <value name="VALUE">
                                  <block type="math_number" id="BVnWo|iSfirB?Vw*M7;o">
                                    <field name="NUM">2016</field>
                                  </block>
                                </value>
                              </block>
                            </statement>
                            <value name="IF2">
                              <block type="logic_compare" id="Q0ejJ+ovU#35l7SaPd`7">
                                <field name="OP">EQ</field>
                                <value name="A">
                                  <block type="variables_get" id="/EhoIt{trOOc3*+k5m4C">
                                    <field name="VAR" id="^:v=Yb?;aM;Z[}4jCF3-">Event</field>
                                  </block>
                                </value>
                                <value name="B">
                                  <block type="text" id="BVzI8#S#S*Yqk5v;$?kD">
                                    <field name="TEXT">Blaue Tonne</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <statement name="DO2">
                              <block type="variables_set" id="R7DF(c~|*~pR_D]JqW7c">
                                <field name="VAR" id="9^)S?J=tLkC7cUWc-u9w">Color</field>
                                <value name="VALUE">
                                  <block type="math_number" id="#A]b|UX(@QPk*SM_q)RZ">
                                    <field name="NUM">31</field>
                                  </block>
                                </value>
                              </block>
                            </statement>
                            <value name="IF3">
                              <block type="logic_compare" id="MjEHt,7LG#}DST*Iuc.R">
                                <field name="OP">EQ</field>
                                <value name="A">
                                  <block type="variables_get" id="(WzO?43I0:YSK;VgFmnX">
                                    <field name="VAR" id="^:v=Yb?;aM;Z[}4jCF3-">Event</field>
                                  </block>
                                </value>
                                <value name="B">
                                  <block type="text" id="![3nA.95iLG[3]m5%GYS">
                                    <field name="TEXT">Gelbe Tonne</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <statement name="DO3">
                              <block type="variables_set" id="959t9eG^*uj2c;pF^HGP">
                                <field name="VAR" id="9^)S?J=tLkC7cUWc-u9w">Color</field>
                                <value name="VALUE">
                                  <block type="math_number" id="{*68t/i/Q7}6cb+0$`6Y">
                                    <field name="NUM">65504</field>
                                  </block>
                                </value>
                              </block>
                            </statement>
                            <next>
                              <block type="control_ex" id="^c0LOh0WChe-1QNTGVAy">
                                <field name="TYPE">false</field>
                                <field name="CLEAR_RUNNING">FALSE</field>
                                <value name="OID">
                                  <shadow type="field_oid" id="7gi,zaI;54L/Ek{e9,I@">
                                    <field name="oid">Object ID</field>
                                  </shadow>
                                  <block type="text_join" id="J|nD$KZ,I6q=mt,xW@:X">
                                    <mutation items="3"></mutation>
                                    <value name="ADD0">
                                      <block type="text" id="kwm[DP}25YD]Te=}p`S0">
                                        <field name="TEXT">0_userdata.0.Abfallkalender.</field>
                                      </block>
                                    </value>
                                    <value name="ADD1">
                                      <block type="math_arithmetic" id="pj~|`_~%6}=?B^fK4@;L">
                                        <field name="OP">ADD</field>
                                        <value name="A">
                                          <shadow type="math_number">
                                            <field name="NUM">1</field>
                                          </shadow>
                                          <block type="variables_get" id="To0?Cg*f2pZ(Z`zK|=?M">
                                            <field name="VAR" id="h}CE-n1l`S|gRf(0K%./">i</field>
                                          </block>
                                        </value>
                                        <value name="B">
                                          <shadow type="math_number" id="=Q|k5qeOIy1ya}{CVNF@">
                                            <field name="NUM">1</field>
                                          </shadow>
                                        </value>
                                      </block>
                                    </value>
                                    <value name="ADD2">
                                      <block type="text" id="If6$$63npGW3OazEE^46">
                                        <field name="TEXT">.color</field>
                                      </block>
                                    </value>
                                  </block>
                                </value>
                                <value name="VALUE">
                                  <shadow type="logic_boolean" id=")+b01E8B2-c#vcsGmA+Y">
                                    <field name="BOOL">TRUE</field>
                                  </shadow>
                                  <block type="variables_get" id="/5*6z@-R5w^1i2*XphN|">
                                    <field name="VAR" id="9^)S?J=tLkC7cUWc-u9w">Color</field>
                                  </block>
                                </value>
                                <value name="DELAY_MS">
                                  <shadow type="math_number" id="79qt?j;aoK%i)roQkfoE">
                                    <field name="NUM">0</field>
                                  </shadow>
                                </value>
                              </block>
                            </next>
                          </block>
                        </next>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </statement>
      </block>
    </statement>
  </block>
</xml>
```
</details>  


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

<details>
  <summary>Blockly Skript</summary>  

 ```
<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="$%h)IyP*A]i!w|o;@^u~">PanelResult</variable>
    <variable id="iG,DhTT3ntIL)6jkdBSx">Action</variable>
  </variables>
  <block type="on_ext" id="Z*WW:Hq=V/0/+D.7sBGj" x="88" y="63">
    <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
    <field name="CONDITION">any</field>
    <field name="ACK_CONDITION"></field>
    <value name="OID0">
      <shadow type="field_oid" id="s?5LPlVoKvrW,Gf/,d6(">
        <field name="oid">default</field>
      </shadow>
      <block type="field_oid" id=";VZs-nq`+#GL`5jVspo^">
        <field name="oid">mqtt.0.SmartHome.NSPanel_1.stat.RESULT</field>
      </block>
    </value>
    <statement name="STATEMENT">
      <block type="variables_set" id="W*-eYA4LLj$WMX1vlx9+">
        <field name="VAR" id="$%h)IyP*A]i!w|o;@^u~">PanelResult</field>
        <value name="VALUE">
          <block type="convert_json2object" id="H}rYz*|_N_r:7lN6kRq)">
            <value name="VALUE">
              <block type="on_source" id="ks};I#sE9{y$Os12X3%`">
                <field name="ATTR">state.val</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="controls_if" id="|e+,CBW1}SywJvnEFroP">
            <mutation elseif="1"></mutation>
            <value name="IF0">
              <block type="logic_compare" id="tkA^fRI!3FU^2Tiqlahc">
                <field name="OP">EQ</field>
                <value name="A">
                  <block type="text_getSubstring" id="k}-`K]@kua~8fg*?I[t#">
                    <mutation at1="true" at2="true"></mutation>
                    <field name="WHERE1">FROM_START</field>
                    <field name="WHERE2">FROM_START</field>
                    <value name="STRING">
                      <block type="on_source" id="qCOa@52xDIv4(R#:]Yzp">
                        <field name="ATTR">state.val</field>
                      </block>
                    </value>
                    <value name="AT1">
                      <block type="math_number" id="Ncm@lgRgVYVBF~^yWKRE">
                        <field name="NUM">3</field>
                      </block>
                    </value>
                    <value name="AT2">
                      <block type="math_number" id="Gov$3|Qrd91N~RUzWea=">
                        <field name="NUM">9</field>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="B">
                  <block type="text" id="2~EGhvBs4KIPXXMcNVkx">
                    <field name="TEXT">Button1</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO0">
              <block type="variables_set" id="G!Z=C5KTj-Nl+XFa0RU_">
                <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                <value name="VALUE">
                  <block type="get_attr" id="Ed}{-}B{X+obkb^Mmk8O">
                    <value name="PATH">
                      <shadow type="text">
                        <field name="TEXT">Button2.Action</field>
                      </shadow>
                      <block type="text" id="-XSmbNSLD2q^JU.3)[(^">
                        <field name="TEXT">Button1.Action</field>
                      </block>
                    </value>
                    <value name="OBJECT">
                      <block type="variables_get" id="-%8e}:rqW1kj_iUDQyyf">
                        <field name="VAR" id="$%h)IyP*A]i!w|o;@^u~">PanelResult</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="controls_if" id="729?J2a__sAP*2PmMN2%">
                    <mutation elseif="4"></mutation>
                    <value name="IF0">
                      <block type="logic_compare" id="u9lV/l]c1,yVRl3(21(L">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="kG0ARQ1j%HKz(I=l}`:P">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="v?m}nM1~E8zR0,Ja+if+">
                            <field name="TEXT">SINGLE</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO0">
                      <block type="comment" id="iqFwhe!^P0z9-W9D[tyh">
                        <field name="COMMENT">Schalte etwas: Button1 1x gedrückt</field>
                        <next>
                          <block type="debug" id="F22M/f@lJ_xQ$t2#QW[#">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="?r3.Wy5c@$3DxmvbIGr}">
                                <field name="TEXT">Button1 SINGLE wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF1">
                      <block type="logic_compare" id="[Vpq7B,RWb4k)Bhwq{nh">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="|Whz!$I5#Iym52Pg8N?p">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="~f_cI8hrs;I)wJ-S.G3r">
                            <field name="TEXT">DOUBLE</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO1">
                      <block type="comment" id="D;PPB54t87N)%F{.hQAx">
                        <field name="COMMENT">Schalte etwas: Button1 2x gedrückt</field>
                        <next>
                          <block type="debug" id="xoG/r3;33`8/j$QeZHW5">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="9PgW|#6f8``brbWQM9q7">
                                <field name="TEXT">Button1 DOUBLE wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF2">
                      <block type="logic_compare" id="t)8drGw=u/q0Pl+ul^43">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="-lf~?Q^H8o}J:cf@I5aN">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="Z!={5~.hF?V-NFw73|BL">
                            <field name="TEXT">TRIPLE</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO2">
                      <block type="comment" id="xjdh~X8eM8ab/a/JuIM/">
                        <field name="COMMENT">Schalte etwas: Button1 3x gedrückt</field>
                        <next>
                          <block type="debug" id="n$kU%^k3$wHN/L**K=jA">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="SA^R/OJX#a7JDhE7LwL[">
                                <field name="TEXT">Button1 TRIPLE wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF3">
                      <block type="logic_compare" id="ZCUeBK[Sc08KKQVMF)tC">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id=":Jlhv9(rM!D5H*eM|Gw-">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="6NH!g[HN7f=7_q%U10M!">
                            <field name="TEXT">QUAD</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO3">
                      <block type="comment" id="77*X9-*|mO]|P0$Jw=K`">
                        <field name="COMMENT">Schalte etwas: Button1 4x gedrückt</field>
                        <next>
                          <block type="debug" id="qE@`G.#9s!UAtrlMJ/yi">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="G:19{lKn)m`B!x(NUx5S">
                                <field name="TEXT">Button1 QUAD wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF4">
                      <block type="logic_compare" id="fz#2[~sK=iF%wd=4`hB,">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="ROFyrrPZn5KJg7?Hs),Z">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="a]-o=$vOr9JDr(T!#SmL">
                            <field name="TEXT">PENTA</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO4">
                      <block type="comment" id="fxPE82.Ci3L`ME=X3nl|">
                        <field name="COMMENT">Schalte etwas: Button1 5x gedrückt</field>
                        <next>
                          <block type="debug" id="7GbZ650het?k*+CCO:nr">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="*[}-a1hl?2pc^*@4E*hI">
                                <field name="TEXT">Button1 PENTA wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                  </block>
                </next>
              </block>
            </statement>
            <value name="IF1">
              <block type="logic_compare" id="8Ev:iPPfN3B?L^Q]oOIc">
                <field name="OP">EQ</field>
                <value name="A">
                  <block type="text_getSubstring" id="xx:q0nC7,q8A8~v?PC#s">
                    <mutation at1="true" at2="true"></mutation>
                    <field name="WHERE1">FROM_START</field>
                    <field name="WHERE2">FROM_START</field>
                    <value name="STRING">
                      <block type="on_source" id="JWC4m9/7dS^!]+xQ-I0Y">
                        <field name="ATTR">state.val</field>
                      </block>
                    </value>
                    <value name="AT1">
                      <block type="math_number" id="k7=j)18I6TmB%)upvAVJ">
                        <field name="NUM">3</field>
                      </block>
                    </value>
                    <value name="AT2">
                      <block type="math_number" id=",EKn%h/uX3}ZjCvmW1KE">
                        <field name="NUM">9</field>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="B">
                  <block type="text" id="Uuj{UrX@-3nNjw{n!H/@">
                    <field name="TEXT">Button2</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO1">
              <block type="variables_set" id="U~1k_f;62_-QkRvGZz=)">
                <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                <value name="VALUE">
                  <block type="get_attr" id="izCz6K1Y;L.7M7MlHA$c">
                    <value name="PATH">
                      <shadow type="text">
                        <field name="TEXT">Button2.Action</field>
                      </shadow>
                      <block type="text" id="y1)^1#)QjYVVA7)mWdvM">
                        <field name="TEXT">Button2.Action</field>
                      </block>
                    </value>
                    <value name="OBJECT">
                      <block type="variables_get" id="TIg$Lr%^Fuk`fxDLC:,^">
                        <field name="VAR" id="$%h)IyP*A]i!w|o;@^u~">PanelResult</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="controls_if" id="tC_APU:6jW5063/l=sR1">
                    <mutation elseif="4"></mutation>
                    <value name="IF0">
                      <block type="logic_compare" id="P9XXNXzc+3H{*^w1P_@q">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="sua/L8[qi8e:U#m}d^pi">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="E^e9/nh{n@)S6e:4q3_h">
                            <field name="TEXT">SINGLE</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO0">
                      <block type="comment" id="qoOw*}O|E06w[5[cXWLo">
                        <field name="COMMENT">Schalte etwas: Button2 1x gedrückt</field>
                        <next>
                          <block type="debug" id=",tE:-UWz(0Zqlc8KBLqO">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text" id="!waPZV$J9fR+dq462%h+">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="{3#KVO|*86E:3pR/!%WP">
                                <field name="TEXT">Button2 SINGLE wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF1">
                      <block type="logic_compare" id="_Z+eBL!Zj.|LQL+_s|Ld">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="15Tx7/a!(wJ;FO+x!4JW">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="}l%?@L+:Ma!=:d2Ky/%*">
                            <field name="TEXT">DOUBLE</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO1">
                      <block type="comment" id="~72fN$sZV!.O{%*0+awy">
                        <field name="COMMENT">Schalte etwas: Button2 2x gedrückt</field>
                        <next>
                          <block type="debug" id="-T4*$n8-_X_{@6!Ga5FQ">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="LFX2j}Pr:o,{$YxQVcp2">
                                <field name="TEXT">Button2 DOUBLE wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF2">
                      <block type="logic_compare" id="6-2Eew1,aoyC]Th*AaJ5">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="4Nl6[tYm2pL@rL7v8vLI">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="zthA#*kib2r|xv+,A{Sh">
                            <field name="TEXT">TRIPLE</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO2">
                      <block type="comment" id="?OI)q#8XL#1)x.E=*m~~">
                        <field name="COMMENT">Schalte etwas: Button2 3x gedrückt</field>
                        <next>
                          <block type="debug" id="%6ZLfC`!6?Z%jXlF:mFa">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="eh|tY,l}uz:WTx}4_G_E">
                                <field name="TEXT">Button2 TRIPLE wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF3">
                      <block type="logic_compare" id="*~f.cy|6d8U0s?|^%:8R">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="tiZ6%x5iuvhh:Yi*9qB9">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="I|K0m__6/:.kuBtYQE5l">
                            <field name="TEXT">QUAD</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO3">
                      <block type="comment" id="ToQ_dt~n$Ef|8-fb|__O">
                        <field name="COMMENT">Schalte etwas: Button2 4x gedrückt</field>
                        <next>
                          <block type="debug" id="qyb7DL~:^6|r@9~KOb+A">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="tb4wo7_n@J)Q9$FLf|rV">
                                <field name="TEXT">Button2 QUAD wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF4">
                      <block type="logic_compare" id="M:x`b;I}a8;jJU=g}u)[">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="Yh,)fk$+WmVXS=iwbzK{">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="1FMk3I`mfaAfEhMd$D#e">
                            <field name="TEXT">PENTA</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO4">
                      <block type="comment" id="5+tVGCf{MdkG(OBDmuy|">
                        <field name="COMMENT">Schalte etwas: Button2 5x gedrückt</field>
                        <next>
                          <block type="debug" id="}{-PVi#AL#[EGD,eb?M#">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="HuBkD3zi|o@.S3w.Qh7n">
                                <field name="TEXT">Button2 PENTA wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                  </block>
                </next>
              </block>
            </statement>
          </block>
        </next>
      </block>
    </statement>
  </block>
</xml>
```
</details>  


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

  
<details>
  <summary>Blockly Skript</summary>  

``` 
<xml xmlns="https://developers.google.com/blockly/xml">
<variables>
<variable id="VC{%szTBZ]@G*_Z1kd=p">NSPanel_Path</variable>
<variable id="7-~%q%O+i,p)gd]2E]u%">i</variable>
</variables>
<block type="comment" id=".H8cu)X4;0/ELXg0~!2" x="-212" y="-137"> <field name="COMMENT">1.) DWD-Adapter muss installiert sein!</field> <next> <block type="comment" id="cMAJA*6Mucx!}~#*FItV"> <field name="COMMENT">2.) Anpassen: Pfade deiner NSPanel 1-n</field> <next> <block type="comment" id="I,l}p*+|7)O*7iDhs{C{"> <field name="COMMENT">wenn mehr NSPanel dann Liste erweitern</field> <next> <block type="comment" id="z#bI#s:k[=wnRjs?t=M">
<field name="COMMENT">wenn weniger NSPanel dann Liste verkürzen</field>
<next>
<block type="variables_set" id="IZv),n_W8%BJqvjwFH60">
<field name="VAR" id="VC{%szTBZ]@G*Z1kd=p">NSPanel_Path</field>
<value name="VALUE">
<block type="lists_create_with" id="hbVUA-n,wK$8EN8v9M2x">
<mutation items="3"></mutation>
<value name="ADD0">
<block type="text" id="^nQ3=mooLvr$lZ;cPu!t">
<field name="TEXT">0.userdata.0.NSPanel.1.</field>
</block>
</value>
<value name="ADD1">
<block type="text" id="X!Pp5k{{2N5^~VZ24!X{">
<field name="TEXT">0.userdata.0.NSPanel.2.</field>
</block>
</value>
<value name="ADD2">
<block type="text" id="htgZqn!7]yOK?I%{#m9D">
<field name="TEXT">0.userdata.0.NSPanel.EMU.</field>
</block>
</value>
</block>
</value>
<next>
<block type="comment" id="}C)!uPDDrlP+Z_ZZxCTP">
<field name="COMMENT">Trigger auf dwd.0.warning.headline</field>
<next>
<block type="on_ext" id="?o?W:(X@bTJ~te|=L*A"> <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation> <field name="CONDITION">any</field> <field name="ACK_CONDITION"></field> <value name="OID0"> <shadow type="field_oid" id="o;@Yb+8-u0:)}3FV/ayZ"> <field name="oid">default</field> </shadow> <block type="field_oid" id="en?eq5J4w5-U^CGl=+Iq"> <field name="oid">dwd.0.warning.headline</field> </block> </value> <statement name="STATEMENT"> <block type="controls_forEach" id="cY44Jgg1PYPJ54ee{d2t"> <field name="VAR" id="7-~%q%O+i,p)gd]2E]u%">i</field> <value name="LIST"> <block type="variables_get" id="g.tPwvave?zcNnhoj#.o"> <field name="VAR" id="VC{%szTBZ]@G*_Z1kd=p">NSPanel_Path</field> </block> </value> <statement name="DO"> <block type="controls_if" id="QPGGF3MVC*NdY!,Moey?"> <value name="IF0"> <block type="logic_compare" id="}r2=99u*N|9-V+V=o?E">
<field name="OP">GT</field>
<value name="A">
<block type="text_length" id="(TJ!yd2sS0(/Sk_iE1;">
<value name="VALUE">
<shadow type="text" id="ynMYy4ITGRb%9Q-7A6^n">
<field name="TEXT">abc</field>
</shadow>
<block type="on_source" id=";)N~d3E+|T|z{Fyxp%#">
<field name="ATTR">state.val</field>
</block>
</value>
</block>
</value>
<value name="B">
<block type="math_number" id="Vw,J0v/)7719Hc@+Fi=x">
<field name="NUM">0</field>
</block>
</value>
</block>
</value>
<statement name="DO0">
<block type="comment" id="PX+4_x%y+g1GWg+Ug6R">
<field name="COMMENT">ScreensaverInfo.popupNotifyHeading</field>
<next>
<block type="control_ex" id="o7P*;1Ttxs*C/e.0Pn88" inline="true">
<field name="TYPE">false</field>
<field name="CLEAR_RUNNING">FALSE</field>
<value name="OID">
<shadow type="field_oid" id="@?zbekjnHNiqZ.?:UZ,"> <field name="oid">Object ID</field> </shadow> <block type="text_join" id="VAdQl$ZWG@WOy_,rcu6%"> <mutation items="2"></mutation> <value name="ADD0"> <block type="variables_get" id="YT;mRR_H6+t{J~}QU_E/"> <field name="VAR" id="7-~%q%O+i,p)gd]2E]u%">i</field> </block> </value> <value name="ADD1"> <block type="text" id="^7!wIf6=?EvYr$SoR^P">
<field name="TEXT">ScreensaverInfo.popupNotifyHeading</field>
</block>
</value>
</block>
</value>
<value name="VALUE">
<shadow type="logic_boolean" id="4]C|sQYZbuEUMP]xH-Ab">
<field name="BOOL">TRUE</field>
</shadow>
<block type="text" id="+(i@.kA,fI(I2w-ZHuo">
<field name="TEXT">Deutscher Wetterdienst</field>
</block>
</value>
<value name="DELAY_MS">
<shadow type="math_number" id="rDN^aNATSKF-a=?gO?Ww">
<field name="NUM">0</field>
</shadow>
</value>
<next>
<block type="comment" id="TG}L5iTO?~|;AN-yf?NV">
<field name="COMMENT">ScreensaverInfo.popupNotifyText</field>
<next>
<block type="control_ex" id="q/ci(sG(Vxs+s07bvr]b" inline="true">
<field name="TYPE">false</field>
<field name="CLEAR_RUNNING">FALSE</field>
<value name="OID">
<shadow type="field_oid">
<field name="oid">Object ID</field>
</shadow>
<block type="text_join" id="IoU]L/3.jrEgMe=(I)K">
<mutation items="2"></mutation>
<value name="ADD0">
<block type="variables_get" id="EXcC{bR:k@EwC!QkJ)YQ">
<field name="VAR" id="7-~%q%O+i,p)gd]2E]u%">i</field>
</block>
</value>
<value name="ADD1">
<block type="text" id="+Zex[j7epd,T21~*k6-"> <field name="TEXT">ScreensaverInfo.popupNotifyText</field> </block> </value> </block> </value> <value name="VALUE"> <shadow type="logic_boolean" id="0{J_-SZvB.zu]ETOXlH/"> <field name="BOOL">TRUE</field> </shadow> <block type="on_source" id="5?IF}*4XhhK0PN3[wD!z"> <field name="ATTR">state.val</field> </block> </value> <value name="DELAY_MS"> <shadow type="math_number" id="pJ2jr~?.G0YB;6r]?S=">
<field name="NUM">0</field>
</shadow>
</value>
</block>
</next>
</block>
</next>
</block>
</next>
</block>
</statement>
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
</next>
</block>
</next>
</block>
</next>
</block>
</xml>
``` 
</details>   

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

<details>
  <summary>Blockly Skript</summary>  

```
<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="RQf9z?083u1F$Iftay#6">NSPanelPath</variable>
    <variable id="{S2zDfJyyDqtc7LCT{Cs">spotifyDevice</variable>
    <variable id="5+Rdog2z8jghQAiAiYYy">spotifyDeviceType</variable>
    <variable id="%x[#|V9wA+|-Bz?lfh/V">alexaDeviceName</variable>
    <variable id="LRbq1Xp|U)?4[rxV;bg)">alexaDeviceSerial</variable>
    <variable id="J.CO8~E12.?n61gPRaQs">alexaDevice</variable>
    <variable id="/=n55{ZY$7xP},:Z!mHQ">alexaIndex</variable>
    <variable id="dfaFn%x.~/f,a3h{+Loa">EQ</variable>
  </variables>
  <block type="comment" id="OjTw$Cljv/PF!U%Q@2Rg" x="38" y="-662">
    <field name="COMMENT">Pfad zum Datenpunkt der NSPanel cardMedia</field>
    <next>
      <block type="variables_set" id="Pbz9{tbu;NSH(s+M?~Ip">
        <field name="VAR" id="RQf9z?083u1F$Iftay#6">NSPanelPath</field>
        <value name="VALUE">
          <block type="text" id=".JdUhG=QxyATV~x:w;l*">
            <field name="TEXT">0_userdata.0.NSPanel.EMU.Media.Player.</field>
          </block>
        </value>
        <next>
          <block type="comment" id="W_3~1^}~M;pZ)?-@40#@">
            <field name="COMMENT">auf Änderung der EQ-Einstellungen warten</field>
            <next>
              <block type="on_ext" id=":bfiilk62nrc2F4wk:9n">
                <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                <field name="CONDITION">any</field>
                <field name="ACK_CONDITION"></field>
                <value name="OID0">
                  <shadow type="field_oid" id="aUQgC%E2=zxO(1_;z5J8">
                    <field name="oid">default</field>
                  </shadow>
                  <block type="text_join" id=")IgRNCSniUyEs2i_pRcD">
                    <mutation items="2"></mutation>
                    <value name="ADD0">
                      <block type="variables_get" id="3Y(7HNIX],1^%D`{rdz-">
                        <field name="VAR" id="RQf9z?083u1F$Iftay#6">NSPanelPath</field>
                      </block>
                    </value>
                    <value name="ADD1">
                      <block type="text" id=")*~_KCvl3nt7$C3eo?-d">
                        <field name="TEXT">PlayerSpotifyPremium.EQ.activeMode</field>
                      </block>
                    </value>
                  </block>
                </value>
                <statement name="STATEMENT">
                  <block type="comment" id="g{?yme(ocVOQXOlM`}M:">
                    <field name="COMMENT">Durch spotify genutzter Speaker</field>
                    <next>
                      <block type="variables_set" id="CG7N.*4@wzpE08BfIP^1">
                        <field name="VAR" id="{S2zDfJyyDqtc7LCT{Cs">spotifyDevice</field>
                        <value name="VALUE">
                          <block type="get_value_var" id="Nh1T7oc[{6U;pFY@Dj-`">
                            <field name="ATTR">val</field>
                            <value name="OID">
                              <shadow type="text" id="a/YSrxPuy0+absU2@nln">
                                <field name="TEXT"></field>
                              </shadow>
                              <block type="text" id="KbtO.buuZ:2T}c`Ro3`_">
                                <field name="TEXT">spotify-premium.0.player.device.name</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <next>
                          <block type="comment" id="Vb#r-@!y)s8FHM_:aaA-">
                            <field name="COMMENT">Computer, Smartphone oder Speaker</field>
                            <next>
                              <block type="variables_set" id="_f}HI.XUAkb5Y,Pw@LJE">
                                <field name="VAR" id="5+Rdog2z8jghQAiAiYYy">spotifyDeviceType</field>
                                <value name="VALUE">
                                  <block type="get_value_var" id="~KRLXxfp1_,Y}OUv|}2%">
                                    <field name="ATTR">val</field>
                                    <value name="OID">
                                      <shadow type="text">
                                        <field name="TEXT"></field>
                                      </shadow>
                                      <block type="text" id="D2]a~?#T;0+:e0=h:3pH">
                                        <field name="TEXT">spotify-premium.0.player.device.type</field>
                                      </block>
                                    </value>
                                  </block>
                                </value>
                                <next>
                                  <block type="comment" id=")D4/i=^oY/],h-oi18.w">
                                    <field name="COMMENT">Ermitteln der Seriennummer zum Device-Namen</field>
                                    <next>
                                      <block type="variables_set" id="u$}jB=-a.Y/D0fCv)}5-">
                                        <field name="VAR" id="%x[#|V9wA+|-Bz?lfh/V">alexaDeviceName</field>
                                        <value name="VALUE">
                                          <block type="selector" id="L%gp8/bO{.pi:SYk4Ldt">
                                            <field name="TEXT">alexa2.0.Echo-Devices.*.Info.name</field>
                                          </block>
                                        </value>
                                        <next>
                                          <block type="variables_set" id="ux4`hY8Cfw~P,}n6*MMe">
                                            <field name="VAR" id="LRbq1Xp|U)?4[rxV;bg)">alexaDeviceSerial</field>
                                            <value name="VALUE">
                                              <block type="selector" id="1=fnxtFk9Xwb^Rkl^uGG">
                                                <field name="TEXT">alexa2.0.Echo-Devices.*.Info.serialNumber</field>
                                              </block>
                                            </value>
                                            <next>
                                              <block type="controls_if" id="Q0k7$^MKMP/hY?@J}%]J">
                                                <mutation else="1"></mutation>
                                                <value name="IF0">
                                                  <block type="logic_compare" id="Y-#%-7l$1i?oV7tP}xeQ">
                                                    <field name="OP">EQ</field>
                                                    <value name="A">
                                                      <block type="variables_get" id="z{t`lM[,=g%W7}GXS2P8">
                                                        <field name="VAR" id="5+Rdog2z8jghQAiAiYYy">spotifyDeviceType</field>
                                                      </block>
                                                    </value>
                                                    <value name="B">
                                                      <block type="text" id="uf?d^[ev-}5/^NG6K}$i">
                                                        <field name="TEXT">Speaker</field>
                                                      </block>
                                                    </value>
                                                  </block>
                                                </value>
                                                <statement name="DO0">
                                                  <block type="variables_set" id="#quE9B-vvQ~y{OB[yno]">
                                                    <field name="VAR" id="J.CO8~E12.?n61gPRaQs">alexaDevice</field>
                                                    <value name="VALUE">
                                                      <block type="logic_null" id="P%0Ae*+?7Dc034C~Xm5j"></block>
                                                    </value>
                                                    <next>
                                                      <block type="controls_for" id="QpQH}c0!Nj`Fpdk-%NFT">
                                                        <field name="VAR" id="/=n55{ZY$7xP},:Z!mHQ">alexaIndex</field>
                                                        <value name="FROM">
                                                          <shadow type="math_number" id=",e--_IL7Y/])rUE*?)|o">
                                                            <field name="NUM">1</field>
                                                          </shadow>
                                                          <block type="math_number" id="RQ2OQ^S*6h0X,UaG9I9y">
                                                            <field name="NUM">1</field>
                                                          </block>
                                                        </value>
                                                        <value name="TO">
                                                          <shadow type="math_number" id="dd{s7vY;}3w$G{%E3lON">
                                                            <field name="NUM">10</field>
                                                          </shadow>
                                                          <block type="lists_length" id="9wJ9sGK_pRAdC^E4)Qh(">
                                                            <value name="VALUE">
                                                              <block type="variables_get" id="pCH9CwlzRT)hIygy*ybZ">
                                                                <field name="VAR" id="%x[#|V9wA+|-Bz?lfh/V">alexaDeviceName</field>
                                                              </block>
                                                            </value>
                                                          </block>
                                                        </value>
                                                        <value name="BY">
                                                          <shadow type="math_number" id="07xY}Hnik`q9|as8F+|C">
                                                            <field name="NUM">1</field>
                                                          </shadow>
                                                          <block type="math_number" id="SG+^JJ@yG.`1Z6EGO01A">
                                                            <field name="NUM">1</field>
                                                          </block>
                                                        </value>
                                                        <statement name="DO">
                                                          <block type="controls_if" id="r$JDE0RrV(U/DpelIX_3">
                                                            <value name="IF0">
                                                              <block type="logic_compare" id="iwc~wAOT;%3,VN8mUM$;">
                                                                <field name="OP">EQ</field>
                                                                <value name="A">
                                                                  <block type="get_value_var" id="QO(34U@,Dbws-4Waf-qJ">
                                                                    <field name="ATTR">val</field>
                                                                    <value name="OID">
                                                                      <shadow type="text" id="/j0eNhkQ5dXmgj}Y`mT3">
                                                                        <field name="TEXT"></field>
                                                                      </shadow>
                                                                      <block type="lists_getIndex" id="EU^g{WbI6RzVQFeL,oB8">
                                                                        <mutation statement="false" at="true"></mutation>
                                                                        <field name="MODE">GET</field>
                                                                        <field name="WHERE">FROM_START</field>
                                                                        <value name="VALUE">
                                                                          <block type="variables_get" id="6o{+zFm8/!SvyfJ7kmhr">
                                                                            <field name="VAR" id="%x[#|V9wA+|-Bz?lfh/V">alexaDeviceName</field>
                                                                          </block>
                                                                        </value>
                                                                        <value name="AT">
                                                                          <block type="variables_get" id="q-]Od(49#%Q/-*+pbg,+">
                                                                            <field name="VAR" id="/=n55{ZY$7xP},:Z!mHQ">alexaIndex</field>
                                                                          </block>
                                                                        </value>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </value>
                                                                <value name="B">
                                                                  <block type="variables_get" id="#Y9q2D5qwHQY7,^JJJSt">
                                                                    <field name="VAR" id="{S2zDfJyyDqtc7LCT{Cs">spotifyDevice</field>
                                                                  </block>
                                                                </value>
                                                              </block>
                                                            </value>
                                                            <statement name="DO0">
                                                              <block type="variables_set" id="q||Xk]Cqz@5XgAs0Oo=7">
                                                                <field name="VAR" id="J.CO8~E12.?n61gPRaQs">alexaDevice</field>
                                                                <value name="VALUE">
                                                                  <block type="get_value_var" id="CJ8l7N]p*CP-.+XKR_#N">
                                                                    <field name="ATTR">val</field>
                                                                    <value name="OID">
                                                                      <shadow type="text">
                                                                        <field name="TEXT"></field>
                                                                      </shadow>
                                                                      <block type="lists_getIndex" id="X%5D5~#Xe5WO81P2@$A2">
                                                                        <mutation statement="false" at="true"></mutation>
                                                                        <field name="MODE">GET</field>
                                                                        <field name="WHERE">FROM_START</field>
                                                                        <value name="VALUE">
                                                                          <block type="variables_get" id="bD`A8@U3@gNq?+_KtPs|">
                                                                            <field name="VAR" id="LRbq1Xp|U)?4[rxV;bg)">alexaDeviceSerial</field>
                                                                          </block>
                                                                        </value>
                                                                        <value name="AT">
                                                                          <block type="variables_get" id="*Ay*H[yM89j@uR/rgUS2">
                                                                            <field name="VAR" id="/=n55{ZY$7xP},:Z!mHQ">alexaIndex</field>
                                                                          </block>
                                                                        </value>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </value>
                                                              </block>
                                                            </statement>
                                                          </block>
                                                        </statement>
                                                        <next>
                                                          <block type="controls_if" id="uamH!cPrG0_7)OhDuj3Q">
                                                            <mutation else="1"></mutation>
                                                            <value name="IF0">
                                                              <block type="logic_compare" id="nnsC;#[8*Y%=3UA.a=Kt">
                                                                <field name="OP">NEQ</field>
                                                                <value name="A">
                                                                  <block type="variables_get" id="/auszg3HM._vs_Z*)mMO">
                                                                    <field name="VAR" id="J.CO8~E12.?n61gPRaQs">alexaDevice</field>
                                                                  </block>
                                                                </value>
                                                                <value name="B">
                                                                  <block type="logic_null" id="8%~1x}Q_wqf{3pt@Tdx}"></block>
                                                                </value>
                                                              </block>
                                                            </value>
                                                            <statement name="DO0">
                                                              <block type="debug" id="h7c,d*nF+%^yBGIu*%$x">
                                                                <field name="Severity">log</field>
                                                                <value name="TEXT">
                                                                  <shadow type="text" id="##f.6$7l4R8.i?;5W~@k">
                                                                    <field name="TEXT">test</field>
                                                                  </shadow>
                                                                  <block type="text_join" id="8%!izMb,n1HwBqVQBJ6U">
                                                                    <mutation items="3"></mutation>
                                                                    <value name="ADD0">
                                                                      <block type="text" id="yHG_B}=kj7!f|`9:{;X7">
                                                                        <field name="TEXT">Alexa-Device: </field>
                                                                      </block>
                                                                    </value>
                                                                    <value name="ADD1">
                                                                      <block type="variables_get" id="}y?;*}+lh.m6f9x3@j?`">
                                                                        <field name="VAR" id="J.CO8~E12.?n61gPRaQs">alexaDevice</field>
                                                                      </block>
                                                                    </value>
                                                                    <value name="ADD2">
                                                                      <block type="text" id="8S/C}!_oHeWL8Rng._mc">
                                                                        <field name="TEXT"> für Klangsteuerung gefunden</field>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </value>
                                                                <next>
                                                                  <block type="comment" id="RI:Y*~o8Q!tpW|SW*_[X">
                                                                    <field name="COMMENT">EQ-Einstellungen global. Kann auch über alle Räume</field>
                                                                    <next>
                                                                      <block type="logic_switch_case" id="^kt(DQ|VFk|O706je)BD">
                                                                        <mutation xmlns="http://www.w3.org/1999/xhtml" case="2" default="1"></mutation>
                                                                        <value name="CONDITION">
                                                                          <block type="variables_get" id="#6Sdf]A|!xspwoG=uP?m">
                                                                            <field name="VAR" id="{S2zDfJyyDqtc7LCT{Cs">spotifyDevice</field>
                                                                          </block>
                                                                        </value>
                                                                        <value name="CASECONDITION0">
                                                                          <block type="text" id="B]SQd{gq+H8pjhY_N{v}">
                                                                            <field name="TEXT">Echo Spot Buero</field>
                                                                          </block>
                                                                        </value>
                                                                        <statement name="CASE0">
                                                                          <block type="logic_switch_case" id="FBiXBpryB{R{Ss#=*GyW">
                                                                            <mutation xmlns="http://www.w3.org/1999/xhtml" case="14" default="1"></mutation>
                                                                            <value name="CONDITION">
                                                                              <block type="on_source" id="8qCMhPfZ|mvBq%C6b|i(">
                                                                                <field name="ATTR">state.val</field>
                                                                              </block>
                                                                            </value>
                                                                            <value name="CASECONDITION0">
                                                                              <block type="text" id="YB5_,n[5OYUz1=bZE]!K">
                                                                                <field name="TEXT">Bassboost</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE0">
                                                                              <block type="variables_set" id="]2DV@ve!KSf(Q$.Nw=e3">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="]oYh{ZD:k]^T$L|1cb1a">
                                                                                    <field name="TEXT">{"bass": 6, "mid": 3, "treble": 4}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION1">
                                                                              <block type="text" id="edcLKq1E!P@uo~g:a3#{">
                                                                                <field name="TEXT">Klassik</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE1">
                                                                              <block type="variables_set" id="M9w1@%cQTSucKU=8bY@d">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="]uZ:L$$p^0}~B`zl791y">
                                                                                    <field name="TEXT">{"bass": 2, "mid": 0, "treble": 1}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION2">
                                                                              <block type="text" id="L1trMnV2HZ(DUHhNQTWt">
                                                                                <field name="TEXT">Dance</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE2">
                                                                              <block type="variables_set" id="Var@YY`JC,N19?L$gEsE">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="Qf[^sA*:%gX5y0%:*M7o">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION3">
                                                                              <block type="text" id="PFmTu~VS0Cm+w8S_wKK3">
                                                                                <field name="TEXT">Deep</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE3">
                                                                              <block type="variables_set" id="?6J0;m4Ig{X9%%ZzPY5e">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="wA1H5%6V4^iH;~Njc!kv">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION4">
                                                                              <block type="text" id="}Ycy38J?bdip%=YuTZSJ">
                                                                                <field name="TEXT">Electronic</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE4">
                                                                              <block type="variables_set" id="e$JG=UT/,.v@cgFKEUN0">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="h`w(z_lau[Cp*@k0:dRk">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION5">
                                                                              <block type="text" id="{4M50x1xJhK#3Jt)AX5/">
                                                                                <field name="TEXT">Flat</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE5">
                                                                              <block type="variables_set" id="NB7%*?+}}]ID|^I0i#2Q">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="=W(khzr+pmCbNx[k6N+,">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION6">
                                                                              <block type="text" id="7YsikWk{A+b_:j:BZ^q2">
                                                                                <field name="TEXT">Hip-Hop</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE6">
                                                                              <block type="variables_set" id="d3F@J`*BteDPjb.6=U6?">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="D:7rso!6yxn+#~AhrNv%">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION7">
                                                                              <block type="text" id="6yk;kM!YF4fZZY@sCu}H">
                                                                                <field name="TEXT">Rock</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE7">
                                                                              <block type="variables_set" id="5T,0W5QJ2{/fd6y#!6Ng">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="IOVP:%~:wom5muAJF2{x">
                                                                                    <field name="TEXT">{"bass": 4, "mid": 3, "treble": 4}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION8">
                                                                              <block type="text" id="lc8=qVCRPC$TiX=tMUup">
                                                                                <field name="TEXT">Metal</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE8">
                                                                              <block type="variables_set" id="})18-%xHG^B,wGI+!dcS">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="]hVCrO1Y8l2fCesjIej/">
                                                                                    <field name="TEXT">{"bass": 5, "mid": 3, "treble": 4}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION9">
                                                                              <block type="text" id="~mP4R|%e3iiNaj}{:})c">
                                                                                <field name="TEXT">Jazz</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE9">
                                                                              <block type="variables_set" id="1}?H!D1qbic!SH8~7#Fq">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="9=unZO-$I4OIYX#W}ofa">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION10">
                                                                              <block type="text" id="2pT?ZbY^A7t.O$BiEY;C">
                                                                                <field name="TEXT">Latin</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE10">
                                                                              <block type="variables_set" id="oPOEe{Q4EeBu0wqb%h]U">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="U#fHdQ6D`t@SsXYIEl#S">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION11">
                                                                              <block type="text" id="wI~A[cu|D1fu(m!iu8@N">
                                                                                <field name="TEXT">Tonstärke</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE11">
                                                                              <block type="variables_set" id="jVH:OnfMpB0Jylo#bo[}">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="!kv`@^Xv2jwto5S}B]N3">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION12">
                                                                              <block type="text" id="hcMQ}OT|sP})uZUFXv_T">
                                                                                <field name="TEXT">Lounge</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE12">
                                                                              <block type="variables_set" id="8C6jRh=7@aqOnA9PwoKU">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="2y9lg`UEe-xR%hLv1VR]">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION13">
                                                                              <block type="text" id="5-._HJ;Uk3?~pz){rl9~">
                                                                                <field name="TEXT">Piano</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE13">
                                                                              <block type="variables_set" id="+YdbblBuGF;K/*k@.?Tl">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="t_h~x`boN7QOdp`6LJrD">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION14">
                                                                              <block type="text" id="F*U.q/Loo*k^b5Y{A.52">
                                                                                <field name="TEXT">beliebig analog listEqualizer erweitern</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE14">
                                                                              <block type="variables_set" id="Sp+f#1$5Eioo!JWDsg89">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="(#%ruXTh?xJ[/FUFrgNi">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <statement name="ONDEFAULT">
                                                                              <block type="comment" id="5E*I[=aH$hNw6H65YXQ]">
                                                                                <field name="COMMENT">Falls Wert aus Panel nicht vorhanden</field>
                                                                                <next>
                                                                                  <block type="variables_set" id="2vMu^S7U}hk|BjnOT;mT">
                                                                                    <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="text" id="`(xl3]h-M`~vLej:c{hw">
                                                                                        <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </next>
                                                                              </block>
                                                                            </statement>
                                                                          </block>
                                                                        </statement>
                                                                        <value name="CASECONDITION1">
                                                                          <block type="text" id="z(l@`p%yRS;g4I*OkIC[">
                                                                            <field name="TEXT">Echo Esszimmer</field>
                                                                          </block>
                                                                        </value>
                                                                        <statement name="CASE1">
                                                                          <block type="logic_switch_case" id="B)agzn@1p~,1=kX|N~6S">
                                                                            <mutation xmlns="http://www.w3.org/1999/xhtml" case="14" default="1"></mutation>
                                                                            <value name="CONDITION">
                                                                              <block type="on_source" id="*uIBl)nWQk9G/tEx0u^p">
                                                                                <field name="ATTR">state.val</field>
                                                                              </block>
                                                                            </value>
                                                                            <value name="CASECONDITION0">
                                                                              <block type="text" id=",^YgXu-Wp5`^$Mp)FHEC">
                                                                                <field name="TEXT">Bassboost</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE0">
                                                                              <block type="variables_set" id="yYcMb?h!iHeM@o0ksewQ">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="p#qNth%y=dQv.p^sU=%;">
                                                                                    <field name="TEXT">{"bass": 6, "mid": 3, "treble": 4}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION1">
                                                                              <block type="text" id="lN266lALwST:|+o3(Inw">
                                                                                <field name="TEXT">Klassik</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE1">
                                                                              <block type="variables_set" id="$Z.1y7PXrqK!!pZ2!Z0J">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="q|A*3PBJ?Z70PGEEb)Lz">
                                                                                    <field name="TEXT">{"bass": 2, "mid": 0, "treble": 1}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION2">
                                                                              <block type="text" id="[U)n_@OF/NGU$W;KPka1">
                                                                                <field name="TEXT">Dance</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE2">
                                                                              <block type="variables_set" id="Iu%Q{Z#ZPA_}56,2DSai">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="^f.{qsV~gg1SB{Yt@J:8">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION3">
                                                                              <block type="text" id="[Bl2Q|?U#a_E%Vn17FU|">
                                                                                <field name="TEXT">Deep</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE3">
                                                                              <block type="variables_set" id="[Rl9_$@nfy_]I`j*:8aE">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="_MnDF_Q;lKl5!]}L-E`f">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION4">
                                                                              <block type="text" id="!y@-Qu%S]{sm4J~USI_6">
                                                                                <field name="TEXT">Electronic</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE4">
                                                                              <block type="variables_set" id="C$A#LW^/7C-H}h~+mwkR">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="39k~Q{}]5k8X0Lno|r!d">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION5">
                                                                              <block type="text" id="JE5PGHkewQ9,Qyj*t*.$">
                                                                                <field name="TEXT">Flat</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE5">
                                                                              <block type="variables_set" id="Fusj@g8AKG]B{L)a[Rb3">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="-yEvMj0uLSB]v=SF+}ml">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION6">
                                                                              <block type="text" id="ol4U`60mJpTN?r@:fD(y">
                                                                                <field name="TEXT">Hip-Hop</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE6">
                                                                              <block type="variables_set" id="rTsJKO/jBgeSusyZq[6B">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="Vh_QXRD)~7ZEi1!ylSV_">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION7">
                                                                              <block type="text" id="EW8W(xfE+$^!jV1PJm0l">
                                                                                <field name="TEXT">Rock</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE7">
                                                                              <block type="variables_set" id="YU=V@=Ij(n)XuQ^xdtYZ">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="}n3sPV6,#zXZ;Q4cgN@|">
                                                                                    <field name="TEXT">{"bass": 4, "mid": 3, "treble": 4}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION8">
                                                                              <block type="text" id="Dh6N@|M}wI.j*8-zpRb{">
                                                                                <field name="TEXT">Metal</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE8">
                                                                              <block type="variables_set" id="2zz@*GJ7*Z|)pg4u.-bq">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="e1jWlA/j|B[Z@HblaUpv">
                                                                                    <field name="TEXT">{"bass": 5, "mid": 3, "treble": 4}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION9">
                                                                              <block type="text" id="QX~.)005m)y|Tdx;]Y:L">
                                                                                <field name="TEXT">Jazz</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE9">
                                                                              <block type="variables_set" id="+c6j`]=w.Vx9n/(caLL^">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="cl%4{kV)z)4@/,T/+QLh">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION10">
                                                                              <block type="text" id="JeFA:69yj@oNJKHiG)c5">
                                                                                <field name="TEXT">Latin</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE10">
                                                                              <block type="variables_set" id="~_1[yxJS=Em8aDap?ji(">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="?S]y~hsxEAh:?z4W:Rlx">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION11">
                                                                              <block type="text" id="Af!aQk+(nak:LA*$oS/x">
                                                                                <field name="TEXT">Tonstärke</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE11">
                                                                              <block type="variables_set" id="9y=b$Uwj(D]H8$8ZklDE">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="m|zC9oqb!CIQ%:3.d1$B">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION12">
                                                                              <block type="text" id="!3WHW=Ai9w:4L0?KVh%1">
                                                                                <field name="TEXT">Lounge</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE12">
                                                                              <block type="variables_set" id="(s7a81fCwy{wVizTFB{!">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="3+hP@wkGBw4?0xE^),a7">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION13">
                                                                              <block type="text" id="]Uh7pBiur.zm?;Ch1^|m">
                                                                                <field name="TEXT">Piano</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE13">
                                                                              <block type="variables_set" id="P/9Nm,Xw7Iv~Vv#n@|DX">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="me}5~olLzJZ?rzC(XQ}c">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <value name="CASECONDITION14">
                                                                              <block type="text" id="}`#Wry@bB?_cxE@IG:M7">
                                                                                <field name="TEXT">beliebig analog listEqualizer erweitern</field>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="CASE14">
                                                                              <block type="variables_set" id="nGBU0l831A)~1LB7fGUc">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="Pte@t!gF#QJ4,sWo/gA`">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <statement name="ONDEFAULT">
                                                                              <block type="comment" id=";s|?.pdU2Ef{tV]5e6fT">
                                                                                <field name="COMMENT">Falls Wert aus Panel nicht vorhanden</field>
                                                                                <next>
                                                                                  <block type="variables_set" id="3b!kGgc[7wFyoFR:Es^R">
                                                                                    <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="text" id="Ahva+_K:PeB3NmK:Iq`Y">
                                                                                        <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </next>
                                                                              </block>
                                                                            </statement>
                                                                          </block>
                                                                        </statement>
                                                                        <value name="CASECONDITION2">
                                                                          <block type="text" id="6e$Sg(!+T)Eo}1)+1kAU">
                                                                            <field name="TEXT">Echo ... weitere Speaker</field>
                                                                          </block>
                                                                        </value>
                                                                        <statement name="CASE2">
                                                                          <block type="comment" id="WSg?8_[}USzh:0%^1%z`">
                                                                            <field name="COMMENT">Hier einfach Liste für andere Speaker erweitern</field>
                                                                          </block>
                                                                        </statement>
                                                                        <statement name="ONDEFAULT">
                                                                          <block type="comment" id="(0%g*;iRepVhdM~K0-GX">
                                                                            <field name="COMMENT">Falls Speaker hier nicht berücksichtigt</field>
                                                                            <next>
                                                                              <block type="variables_set" id="_*sN.-y?m9IjquPib+R@">
                                                                                <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="*OPRR`T/.hm|8q1u(Ekk">
                                                                                    <field name="TEXT">{"bass": 0, "mid": 0, "treble": 0}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </next>
                                                                          </block>
                                                                        </statement>
                                                                        <next>
                                                                          <block type="control_ex" id="JIQallubl}WWqFmkrYq." inline="true">
                                                                            <field name="TYPE">false</field>
                                                                            <field name="CLEAR_RUNNING">FALSE</field>
                                                                            <value name="OID">
                                                                              <shadow type="field_oid" id=";13LB9.0=8*h(m$FT2Q1">
                                                                                <field name="oid">Object ID</field>
                                                                              </shadow>
                                                                              <block type="text_join" id="~(127^)Bw7[VL(6dLJ~+">
                                                                                <mutation items="3"></mutation>
                                                                                <value name="ADD0">
                                                                                  <block type="text" id="(HV]6?{?vXgU5,a~}mb|">
                                                                                    <field name="TEXT">alexa2.0.Echo-Devices.</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD1">
                                                                                  <block type="variables_get" id="Q}Np)T`Q|YcYIf4jLiD*">
                                                                                    <field name="VAR" id="J.CO8~E12.?n61gPRaQs">alexaDevice</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD2">
                                                                                  <block type="text" id="7@nmX-e}+]vdQ^qV==OO">
                                                                                    <field name="TEXT">.Preferences.equalizerBass</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <value name="VALUE">
                                                                              <shadow type="logic_boolean" id="3$|`sP1IFPlAGPS99G6_">
                                                                                <field name="BOOL">TRUE</field>
                                                                              </shadow>
                                                                              <block type="get_attr" id="A^.tit7EUU-FcB=|e;-h">
                                                                                <value name="PATH">
                                                                                  <shadow type="text" id="4_CZwRl~$n4mal#Ycn|!">
                                                                                    <field name="TEXT"></field>
                                                                                  </shadow>
                                                                                  <block type="text" id="RFc6F0M0wv/5^.X{zfz(">
                                                                                    <field name="TEXT">bass</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="OBJECT">
                                                                                  <block type="variables_get" id="[ohch-yp;y-TaS6wa/Tn">
                                                                                    <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <value name="DELAY_MS">
                                                                              <shadow type="math_number" id="CM,@I:Dl8$x!jKV+F2Y%">
                                                                                <field name="NUM">0</field>
                                                                              </shadow>
                                                                            </value>
                                                                            <next>
                                                                              <block type="control_ex" id="2#GcQ,6~**^~$1CB+}TE" inline="true">
                                                                                <field name="TYPE">false</field>
                                                                                <field name="CLEAR_RUNNING">FALSE</field>
                                                                                <value name="OID">
                                                                                  <shadow type="field_oid">
                                                                                    <field name="oid">Object ID</field>
                                                                                  </shadow>
                                                                                  <block type="text_join" id="NHBbz/JIcymvN=~Bxhd+">
                                                                                    <mutation items="3"></mutation>
                                                                                    <value name="ADD0">
                                                                                      <block type="text" id="IRo7uj$hwm`?#)4dtP#x">
                                                                                        <field name="TEXT">alexa2.0.Echo-Devices.</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="ADD1">
                                                                                      <block type="variables_get" id="xYPndfL4rvRi!cNNGta=">
                                                                                        <field name="VAR" id="J.CO8~E12.?n61gPRaQs">alexaDevice</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="ADD2">
                                                                                      <block type="text" id="V:`ond73X|Cv/D:O[)0!">
                                                                                        <field name="TEXT">.Preferences.equalizerMidRange</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="VALUE">
                                                                                  <shadow type="logic_boolean" id="@o9s_3g33602y7mg,?VV">
                                                                                    <field name="BOOL">TRUE</field>
                                                                                  </shadow>
                                                                                  <block type="get_attr" id="K^]{d9OiQRvoCtZ3]fg^">
                                                                                    <value name="PATH">
                                                                                      <shadow type="text">
                                                                                        <field name="TEXT"></field>
                                                                                      </shadow>
                                                                                      <block type="text" id="3b}Of~R)n;]dBR)Ou?[?">
                                                                                        <field name="TEXT">mid</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="OBJECT">
                                                                                      <block type="variables_get" id="X2:,j0Q^vOkh%O9UOt/N">
                                                                                        <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="DELAY_MS">
                                                                                  <shadow type="math_number" id="sik*FLy+v*5pY|))Dy`]">
                                                                                    <field name="NUM">0</field>
                                                                                  </shadow>
                                                                                </value>
                                                                                <next>
                                                                                  <block type="control_ex" id="2l-c/})!GMZbVHtZF86a" inline="true">
                                                                                    <field name="TYPE">false</field>
                                                                                    <field name="CLEAR_RUNNING">FALSE</field>
                                                                                    <value name="OID">
                                                                                      <shadow type="field_oid">
                                                                                        <field name="oid">Object ID</field>
                                                                                      </shadow>
                                                                                      <block type="text_join" id="`0OJnY}r9u.X6//thv.2">
                                                                                        <mutation items="3"></mutation>
                                                                                        <value name="ADD0">
                                                                                          <block type="text" id="EkxU12(RL).D(`TrpVI1">
                                                                                            <field name="TEXT">alexa2.0.Echo-Devices.</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD1">
                                                                                          <block type="variables_get" id="v,Q}Q1VEC!@xF`y9rj1d">
                                                                                            <field name="VAR" id="J.CO8~E12.?n61gPRaQs">alexaDevice</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD2">
                                                                                          <block type="text" id="dtz=JX;$GZ`?6r*9w(,,">
                                                                                            <field name="TEXT">.Preferences.equalizerTreble</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="VALUE">
                                                                                      <shadow type="logic_boolean" id=".K^ARcwUua~^|jj`}*`q">
                                                                                        <field name="BOOL">TRUE</field>
                                                                                      </shadow>
                                                                                      <block type="get_attr" id="n,3,!g#~z61BQVIHGu?:">
                                                                                        <value name="PATH">
                                                                                          <shadow type="text">
                                                                                            <field name="TEXT"></field>
                                                                                          </shadow>
                                                                                          <block type="text" id="~XplZ,SIC%8KRRzH6!lA">
                                                                                            <field name="TEXT">treble</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="OBJECT">
                                                                                          <block type="variables_get" id="[:#8*a-W?nm(YxU87q1~">
                                                                                            <field name="VAR" id="dfaFn%x.~/f,a3h{+Loa">EQ</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="DELAY_MS">
                                                                                      <shadow type="math_number" id=";hLXS{2(/)}fKkb)!p#x">
                                                                                        <field name="NUM">0</field>
                                                                                      </shadow>
                                                                                    </value>
                                                                                  </block>
                                                                                </next>
                                                                              </block>
                                                                            </next>
                                                                          </block>
                                                                        </next>
                                                                      </block>
                                                                    </next>
                                                                  </block>
                                                                </next>
                                                              </block>
                                                            </statement>
                                                            <statement name="ELSE">
                                                              <block type="debug" id="bl6M5h-#~g=?.T86tB2_">
                                                                <field name="Severity">log</field>
                                                                <value name="TEXT">
                                                                  <shadow type="text">
                                                                    <field name="TEXT"></field>
                                                                  </shadow>
                                                                  <block type="text_join" id="X`m8Uf)5xi)Ij3Nm0XzQ">
                                                                    <mutation items="5"></mutation>
                                                                    <value name="ADD0">
                                                                      <block type="text" id="-IvCc#$oQ,w$T^.QAm_6">
                                                                        <field name="TEXT">Device-Type: </field>
                                                                      </block>
                                                                    </value>
                                                                    <value name="ADD1">
                                                                      <block type="variables_get" id="?7*kuSiT#S8u)8gU.r}-">
                                                                        <field name="VAR" id="5+Rdog2z8jghQAiAiYYy">spotifyDeviceType</field>
                                                                      </block>
                                                                    </value>
                                                                    <value name="ADD2">
                                                                      <block type="text" id="$b/+LVc5rlr)D`{8:!7m">
                                                                        <field name="TEXT"> hat keine Klangsteuerung (</field>
                                                                      </block>
                                                                    </value>
                                                                    <value name="ADD3">
                                                                      <block type="variables_get" id="DI97y)F9*gxZ=0F!S|#j">
                                                                        <field name="VAR" id="{S2zDfJyyDqtc7LCT{Cs">spotifyDevice</field>
                                                                      </block>
                                                                    </value>
                                                                    <value name="ADD4">
                                                                      <block type="text" id="3/WX`YZ__.C8HI+k=Z(6">
                                                                        <field name="TEXT">)</field>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </value>
                                                              </block>
                                                            </statement>
                                                          </block>
                                                        </next>
                                                      </block>
                                                    </next>
                                                  </block>
                                                </statement>
                                                <statement name="ELSE">
                                                  <block type="debug" id="/v*WPuz%Nd+=%e]rpQ@)">
                                                    <field name="Severity">log</field>
                                                    <value name="TEXT">
                                                      <shadow type="text" id="Dv/.RIwd-C}f+fOEi-9*">
                                                        <field name="TEXT"></field>
                                                      </shadow>
                                                      <block type="text_join" id="8`YyWEu*,C]+^VY7`O/X">
                                                        <mutation items="5"></mutation>
                                                        <value name="ADD0">
                                                          <block type="text" id="}![KG+WYj2q7kO/Abnz7">
                                                            <field name="TEXT">Device-Type: </field>
                                                          </block>
                                                        </value>
                                                        <value name="ADD1">
                                                          <block type="variables_get" id="/B~7-/!rkoJ?)9k+LK;F">
                                                            <field name="VAR" id="5+Rdog2z8jghQAiAiYYy">spotifyDeviceType</field>
                                                          </block>
                                                        </value>
                                                        <value name="ADD2">
                                                          <block type="text" id="b=pvAd/G8j/_6JiS`aTw">
                                                            <field name="TEXT"> hat keine Klangsteuerung (</field>
                                                          </block>
                                                        </value>
                                                        <value name="ADD3">
                                                          <block type="variables_get" id="PJw:8U}qLR]AR1HXYwaL">
                                                            <field name="VAR" id="{S2zDfJyyDqtc7LCT{Cs">spotifyDevice</field>
                                                          </block>
                                                        </value>
                                                        <value name="ADD4">
                                                          <block type="text" id=";4dMP8F/OdJDS9zPUx1j">
                                                            <field name="TEXT">)</field>
                                                          </block>
                                                        </value>
                                                      </block>
                                                    </value>
                                                  </block>
                                                </statement>
                                              </block>
                                            </next>
                                          </block>
                                        </next>
                                      </block>
                                    </next>
                                  </block>
                                </next>
                              </block>
                            </next>
                          </block>
                        </next>
                      </block>
                    </next>
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