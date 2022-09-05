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

# **Changelog**

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


***


# **1.) Button entkoppeln**

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

# **2.) Alarm Page**


* **Quelle**:
Post [1087](https://forum.iobroker.net/topic/50888/sonoff-nspanel/1087) hier im Forum


* **Im IoBroker**
Im IoBroker wird unter 0_userdata.0.NSPanel.1.Alarm die drei Datenpunkte **AlarmPin**, **AlarmState** und **AlarmType** benötigt. Diese werden i.d.R. generisch erzeugt (Typ String).

![image](https://user-images.githubusercontent.com/99131208/188514512-67b6400f-30db-4adc-b92c-9359d21d97d9.png)
(Bild by @Armilar)

Bei Aktivierung oder Deaktivierung der Alarmanlage wechselt der Status in "arming" oder "pending". Da die Verarbeitung der Alarmlogik außerhalb des Skriptes stattfindet, müssen die Datenpunkte auch entsprechend durch das externe Skript weiter getaktet werden


* **Aliase**:
Die drei Datenpunkte **AlarmPin**, **AlarmState** und **AlarmType** werden in einem Alias vom Typ Feueralarm im Gerätemanager oder Alias Adapter angelet und dieser Alias wird dann im Konfigurationsskript auf der Alarm-Page verwendet.

![image](https://user-images.githubusercontent.com/99131208/188514578-43f08178-b8f0-4d09-8e76-02cbe55d5557.png)

Alias-Typ Feueralarm:  
ACTUAL = 0_userdata.0.NSXXXX.Alarm.AlarmState  
PIN = 0_userdata.0.NSXXXX.Alarm.PIN  
TYPE = 0_userdata.0.NSXXXX.Alarm.AlarmType  

Falls ein Wert im Alias nicht vorhanden ist, dann separat hinzufügen

* **Konfigurationsskript**

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

![image](https://user-images.githubusercontent.com/99131208/188514613-8a5b356b-1c47-47aa-a80c-91f30edf1fe8.png)
 

<details>
  <summary>Blockly</summary>

 ```
<xml xmlns="https://developers.google.com/blockly/xml">
 <block type="on_ext" id="q!?(x}z/f~TClQnNmbyU" x="113" y="38">
   <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
   <field name="CONDITION">ne</field>
   <field name="ACK_CONDITION"></field>
   <value name="OID0">
     <shadow type="field_oid" id="]~f@4kO$zmxdg=}/810C">
       <field name="oid">0_userdata.0.NSPanel.1.Alarm.AlarmState</field>
     </shadow>
   </value>
   <statement name="STATEMENT">
     <block type="controls_if" id="=_e7bf!`Q]$tg*0U1_2F">
       <mutation elseif="1"></mutation>
       <value name="IF0">
         <block type="logic_compare" id="0_9gv(MmSSJ{2a$j{}(P">
           <field name="OP">EQ</field>
           <value name="A">
             <block type="on_source" id="H$WWrxxX|NaWkT%W]g!Z">
               <field name="ATTR">state.val</field>
             </block>
           </value>
           <value name="B">
             <block type="text" id="_TnyjJ5x!)JY~rQ:Opj)">
               <field name="TEXT">arming</field>
             </block>
           </value>
         </block>
       </value>
       <statement name="DO0">
         <block type="control" id="eO}0c$0s~08Di)?sMM0(">
           <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="true"></mutation>
           <field name="OID">0_userdata.0.NSPanel.1.Alarm.AlarmState</field>
           <field name="WITH_DELAY">TRUE</field>
           <field name="DELAY_MS">1000</field>
           <field name="UNIT">ms</field>
           <field name="CLEAR_RUNNING">TRUE</field>
           <value name="VALUE">
             <block type="text" id="J(va8~n[/dogNBn!W].I">
               <field name="TEXT">armed</field>
             </block>
           </value>
         </block>
       </statement>
       <value name="IF1">
         <block type="logic_compare" id="]p3s+ouB~BJkfd:e)G:(">
           <field name="OP">EQ</field>
           <value name="A">
             <block type="on_source" id=":n]Z,t6+q#-l_hP+MEI@">
               <field name="ATTR">state.val</field>
             </block>
           </value>
           <value name="B">
             <block type="text" id="([Ep{MPBu5s.C-lOdHgr">
               <field name="TEXT">pending</field>
             </block>
           </value>
         </block>
       </value>
       <statement name="DO1">
         <block type="control" id="s77gpG^9o0A)T{f}{#,c">
           <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="true"></mutation>
           <field name="OID">0_userdata.0.NSPanel.1.Alarm.AlarmState</field>
           <field name="WITH_DELAY">TRUE</field>
           <field name="DELAY_MS">1000</field>
           <field name="UNIT">ms</field>
           <field name="CLEAR_RUNNING">TRUE</field>
           <value name="VALUE">
             <block type="text" id="4DC5l(?mcdlhZ/jIumty">
               <field name="TEXT">disarmed</field>
             </block>
           </value>
         </block>
       </statement>
     </block>
   </statement>
  </block>
</xml>   
```
</details>  
(Bild & Blockly by @Armilar)

Test-Blockly starten

Alarm-Code in die cardAlarm eingeben --> Schutz auswählen --> aktiviert
Alarm-Code in die cardAlarm eingeben --> Deaktivieren --> deaktiviert


* **Offene Punkte**: 
Ich habe dieses Grid nicht selbst getestet. Ich wäre dankbar für Zusatz Informationen.  
--> Wo definiert man den PIN der verwendet wird?  
--> Wie ist das mit den Aliasen  
--> gibt es eine Karenzzeitspanne nach dem Aktivieren oder bis zum Deaktivieren?  

