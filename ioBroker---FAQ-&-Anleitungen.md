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
**X.)** Anleitung by Armilar  

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

  
  Test-Blockly starten:  
  
  Alarm-Code in die cardAlarm eingeben --> Schutz auswählen --> aktiviert  
  Alarm-Code in die cardAlarm eingeben --> Deaktivieren --> deaktiviert  
  
  
* **Offene Punkte**:  
Ich habe dieses Grid nicht selbst getestet. Ich wäre dankbar für Zusatz Informationen.  
--> Wo definiert man den PIN der verwendet wird?  
--> Wie ist das mit den Aliasen  
--> gibt es eine Karenzzeitspanne nach dem Aktivieren oder bis zum Deaktivieren?  

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

<details>
  <summary>Blockly Skript</summary> 
 
 ```
<xml xmlns="https://developers.google.com/blockly/xml">
  <block type="on" id="^D-c/jQ8.N);=7Ic~rAw" x="-238" y="-237">
    <field name="OID">0_userdata.0.NSPanel.1.DP_RQ.NSPanel_InfoRQ</field>
    <field name="CONDITION">ne</field>
    <field name="ACK_CONDITION"></field>
    <statement name="STATEMENT">
      <block type="controls_if" id="NA-Iy%xl.-1qP}_ntm-K">
        <value name="IF0">
          <block type="logic_compare" id="xU6_pkIHp:+an:llYxO7">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="get_value" id="zt-oj}9|^lz$y0Y+uX{z">
                <field name="ATTR">val</field>
                <field name="OID">0_userdata.0.NSPanel.1.DP_RQ.NSPanel_InfoRQ</field>
              </block>
            </value>
            <value name="B">
              <block type="logic_boolean" id="W*,0+F8r{1lGvOZRLqR!">
                <field name="BOOL">TRUE</field>
              </block>
            </value>
          </block>
        </value>
        <statement name="DO0">
          <block type="timeouts_wait" id="PWh;}}r)zb#ugpv6*sj|">
            <field name="DELAY">20</field>
            <field name="UNIT">sec</field>
            <next>
              <block type="control" id="oiUfnP)ms6:HeZU2e|;u">
                <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="false"></mutation>
                <field name="OID">0_userdata.0.NSPanel.1.ScreensaverInfo.popupNotifyHeading</field>
                <field name="WITH_DELAY">FALSE</field>
                <value name="VALUE">
                  <block type="text" id="k:,q%UL1r6loKc@D}r+(">
                    <field name="TEXT">INFO</field>
                  </block>
                </value>
                <next>
                  <block type="control" id="Ma4m/8_a28*A7/`%`*0X">
                    <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="false"></mutation>
                    <field name="OID">0_userdata.0.NSPanel.1.ScreensaverInfo.popupNotifyText</field>
                    <field name="WITH_DELAY">FALSE</field>
                    <value name="VALUE">
                      <block type="text" id="ng-xB),UUycdg4GI2|K{">
                        <field name="TEXT">Heute ist es ganz schön heiß!</field>
                      </block>
                    </value>
                    <next>
                      <block type="toggle" id="qUH1D!wwJXiYr[KQ,.}A">
                        <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="false"></mutation>
                        <field name="OID">0_userdata.0.NSPanel.1.DP_RQ.NSPanel_InfoRQ</field>
                        <field name="WITH_DELAY">FALSE</field>
                        <next>
                          <block type="timeouts_wait" id=";93SSUfV69!-h_CWkA.@">
                            <field name="DELAY">20</field>
                            <field name="UNIT">sec</field>
                            <next>
                              <block type="control" id="}fxN7f3*x$HF9#ePhL3i">
                                <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="false"></mutation>
                                <field name="OID">0_userdata.0.NSPanel.1.ScreensaverInfo.popupNotifyHeading</field>
                                <field name="WITH_DELAY">FALSE</field>
                                <value name="VALUE">
                                  <block type="text" id="b0jBsnk@!YwX~cuxkgOi">
                                    <field name="TEXT"></field>
                                  </block>
                                </value>
                                <next>
                                  <block type="control" id="C}QMk;?Qtx^ZviUKh-}9">
                                    <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="false"></mutation>
                                    <field name="OID">0_userdata.0.NSPanel.1.ScreensaverInfo.popupNotifyText</field>
                                    <field name="WITH_DELAY">FALSE</field>
                                    <value name="VALUE">
                                      <block type="text" id="m;bIZ!Y7H`e|BikGQ$%S">
                                        <field name="TEXT"></field>
                                      </block>
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
            </next>
          </block>
        </statement>
      </block>
    </statement>
  </block>
</xml>
```
</details>  


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



* JS / Blockly (Alle Skripte by @Armilar):
Es steht für die Umsetzung / Aufbereitung der Kalenderdaten nach NSPanel ein JS und ein Blockly zur Verfügung. Man benötigt nur eines davon. Es spricht aber nichts dagegen, beide mal zu testen ;-)

Java Skript:

1 = Hier muss der Pfad zum ICal Adapter zum Punkt **ical.0.data.table** eigestellt werden. Achtet auf die Instanznummer beim Adapter  
2 = Muss nur angepasst werden, wenn Eure Datenpunkte nicht unter **0_userdata.0.Abfallkalender.** liegen  
3 = Die Bezeichnungen der Abfallbehälter in Eurem Kalender. Die Namen müssen passen, das mit das Parsen funktioniert. Tipp: Die Ziffern bei "setze Color auf ....." sind die Farbcodierungen im Dezimalsystem.  
4 = Für's parsen wichtig. Bei funktioniert die 0, es kann sein dass dies bei euch anders ist.  
  
![image](https://user-images.githubusercontent.com/99131208/188515648-9fe879b9-fe5c-402b-8924-47710f4baa95.png)  



<details>
  <summary>Java Skript</summary>  

 ```
var i, Muell_JSON, Event2, Color;
 
function subsequenceFromStartLast(sequence, at1) {
  var start = at1;
  var end = sequence.length - 1 + 1;
  return sequence.slice(start, end);
}
 
 
on({id: 'ical.1.data.table', change: "ne"}, async function (obj) {
  var value = obj.state.val;
  var oldValue = obj.oldState.val;
  for (i = 0; i <= 3; i++) {
    Muell_JSON = getState("ical.1.data.table").val;
    setStateDelayed((['0_userdata.0.Abfallkalender.',parseFloat(i) + 1,'.date'].join('')), getAttr(Muell_JSON, (String(i) + '.date')), false, parseInt(((0) || "").toString(), 10), false);
    Event2 = subsequenceFromStartLast(getAttr(Muell_JSON, (String(i) + '.event')), 0);
    setStateDelayed((['0_userdata.0.Abfallkalender.',parseFloat(i) + 1,'.event'].join('')), Event2, false, parseInt(((0) || "").toString(), 10), false);
    if (Event2 == 'Restabfalltonne') {
      Color = 33840;
    } else if (Event2 == 'Bio
	tonne') {
      Color = 2016;
    } else if (Event2 == 'Blaue Tonne') {
      Color = 31;
    } else if (Event2 == 'Gelbe Tonne') {
      Color = 65504;
    }
    setStateDelayed((['0_userdata.0.Abfallkalender.',parseFloat(i) + 1,'.color'].join('')), Color, false, parseInt(((0) || "").toString(), 10), false);
  }
});
```
</details>  



Blockly Skript:  
  
1 = Hier muss der Pfad zum ICal Adapter zum Punkt **ical.0.data.table** eigestellt werden. Achtet auf die Instanznummer beim Adapter  
2 = Muss nur angepasst werden, wenn Eure Datenpunkte nicht unter **0_userdata.0.Abfallkalender.** liegen  
3 = Die Bezeichnungen der Abfallbehälter in Eurem Kalender. Die Namen müssen passen, das mit das Parsen funktioniert. Tipp: Die Ziffern bei "setze Color auf ....." sind die Farbcodierungen im Dezimalsystem.  
4 = Für's parsen wichtig. Bei funktioniert die 1, es kann sein dass dies bei euch anders ist.  

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
var Abfall: PageEntities =
{
    "type": "cardEntities",
    "heading": "Abfallkalender",
    "useColor": true,
    "subPage": false,
    "parent": Abfall,
    "items": [
        <PageItem>{ id: "alias.0.NSPanel_1.Abfall.event1",icon: "trash-can"},  
        <PageItem>{ id: "alias.0.NSPanel_1.Abfall.event2",icon: "trash-can"},  
        <PageItem>{ id: "alias.0.NSPanel_1.Abfall.event3",icon: "trash-can"},  
        <PageItem>{ id: "alias.0.NSPanel_1.Abfall.event4",icon: "trash-can"}  
    ]
};
```

* **Fazit**:
Eine vermeintlich einfache Sache, die aber ziemlich knifflig werden kann. 


***


## **5.) QR-Code Page**
* **Quelle**
Die Anleitung kommt aus dem Post [620](https://forum.iobroker.net/topic/50888/sonoff-nspanel/620) hier im Forum.

* **ioBroker**
Legt Euch unter **0_userdata.0.** einen neuen Datenpunkt vom Typ String an. Dieser Datenpunkt erhält die Daten aus dem sich der QR Code erstellt. Außerdem werden SSID und das Passwort separat auf der Page angezeigt.  

Bsp.: WIFI:**T**:WPA;**S**:Test-Guest-SSID;**P**:guest-accecess;**H**:;  

T = Verschlüsselung  
S = SSID  
P = Password  
H = Hidden (nur erforderlich wenn versteckt)  

![image](https://user-images.githubusercontent.com/99131208/188515951-c5350270-de2f-4526-b337-9fd9c60bf6d8.png)  
(Bild by @Armilar )

* **Alias**
Auf den erstellten Datenpunkt nun einen Alias vom Typ Info anlegen.
![image](https://user-images.githubusercontent.com/99131208/188515935-344deccc-c00f-48c1-9770-83ab432c34d3.png)  
(Bild by @Armilar )
* **Konfigurationsskript**
Auf der Konfigurationsseite müsst ihr nun eine OageQR hinzufügen:

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

* **Bekannte Probleme**
Der QR Code funktioniert auf manchen Android Geräten nicht.


***


## **6.)** Alias Definitionen

* **Quelle**
Gefunden hier im Thread im Post [687](https://forum.iobroker.net/topic/50888/sonoff-nspanel/687).

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

* **Voraussetzung**  

* **Alias**  

* **Konfigurationsskript**  


***


## **X.) Für Armilar :-)**