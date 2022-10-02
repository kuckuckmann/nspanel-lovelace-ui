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
 

<details>
  <summary>Blockly</summary>

```
<xml xmlns="https://developers.google.com/blockly/xml">
<variables>
<variable id="LwJJoNeQC4K?A;BW5:o">nspanelAlarmPath</variable>
<variable id=".d{cc!R.4y2U9N+gLY1K">dpAlarmState</variable>
</variables>
<block type="comment" id="I^BpP.H=p^7Vj|-sy!%" x="-937" y="-162"> <field name="COMMENT">Bitte nspanelAlarmPath anpassen</field> <next> <block type="comment" id="JL[C{;Q}PF[TQ_BfpN$c"> <field name="COMMENT">Der Rest wird dynamisch für das jeweilige Panel ermittelt</field> <next> <block type="variables_set" id="2}X9[s}b1IDUV{6QPzh?"> <field name="VAR" id="LwJJoNeQC4K?A;BW5:_o">nspanelAlarmPath</field> <value name="VALUE"> <block type="text" id="in2z;TR0jhq1QI85qO8">
<field name="TEXT">0_userdata.0.NSPanel.Alarm.</field>
</block>
</value>
<next>
<block type="variables_set" id="+tlGEcYI17~KL5S%%1O">
<field name="VAR" id=".d{cc!R.4y2U9N+gLY1K">dpAlarmState</field>
<value name="VALUE">
<block type="text_join" id="PWihVQn3v+ef7aPA%zyx">
<mutation items="2"></mutation>
<value name="ADD0">
<block type="variables_get" id="v2AT~!{!0Qc0BI2!SgN"> <field name="VAR" id="LwJJoNeQC4K?A;BW5:_o">nspanelAlarmPath</field> </block> </value> <value name="ADD1"> <block type="text" id="78{g[~wI2yQXnYZvL4}t"> <field name="TEXT">AlarmState</field> </block> </value> </block> </value> <next> <block type="on_ext" id="q!?(x}z/f~TClQnNmbyU"> <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation> <field name="CONDITION">ne</field> <field name="ACK_CONDITION"></field> <value name="OID0"> <shadow type="field_oid" id="]~f@4kO$zmxdg=}/810C"> <field name="oid">0_userdata.0.NSPanel.Alarm.AlarmState</field> </shadow> <block type="variables_get" id="vCPAx:V[ZG~6IkkFu/r">
<field name="VAR" id=".d{cc!R.4y2U9N+gLY1K">dpAlarmState</field>
</block>
</value>
<statement name="STATEMENT">
<block type="controls_if" id="=e7bf!Q]$tg*0U1_2F"> <mutation elseif="2"></mutation> <value name="IF0"> <block type="logic_compare" id="0_9gv(MmSSJ{2a$j{}(P"> <field name="OP">EQ</field> <value name="A"> <block type="on_source" id="H$WWrxxX|NaWkT%W]g!Z"> <field name="ATTR">state.val</field> </block> </value> <value name="B"> <block type="text" id="_TnyjJ5x!)JY~rQ:Opj)"> <field name="TEXT">arming</field> </block> </value> </block> </value> <statement name="DO0"> <block type="comment" id="=w_/N]5Tu)B)NwyTbxSp"> <field name="COMMENT">weitere ioBroker-Überprüfung - z.B. Fenster offen</field> <next> <block type="control_ex" id="FGZ}]#=@X?IJ3ddc[9rP" inline="true"> <field name="TYPE">false</field> <field name="CLEAR_RUNNING">TRUE</field> <value name="OID"> <shadow type="field_oid" id="=EKIKVg=5v+fyd:5J3]B"> <field name="oid">Object ID</field> </shadow> <block type="variables_get" id="Y,]v4(aeLZ~(@alJ-8;D"> <field name="VAR" id=".d{cc!R.4y2U9N+gLY1K">dpAlarmState</field> </block> </value> <value name="VALUE"> <shadow type="logic_boolean" id="2A;g]]ox]cFCoGeBOge">
<field name="BOOL">TRUE</field>
</shadow>
<block type="text" id="WOt(NkkB-R9/-Xho,6}-">
<field name="TEXT">armed</field>
</block>
</value>
<value name="DELAY_MS">
<shadow type="math_number" id="M@|2SGg8%@2nZdqU51f">
<field name="NUM">0</field>
</shadow>
<block type="math_number" id=".e9qh.?F@m)/t(HM7|M"> <field name="NUM">1000</field> </block> </value> </block> </next> </block> </statement> <value name="IF1"> <block type="logic_compare" id="]p3s+ouB~BJkfd:e)G:("> <field name="OP">EQ</field> <value name="A"> <block type="on_source" id=":n]Z,t6+q#-l_hP+MEI@"> <field name="ATTR">state.val</field> </block> </value> <value name="B"> <block type="text" id="([Ep{MPBu5s.C-lOdHgr"> <field name="TEXT">pending</field> </block> </value> </block> </value> <statement name="DO1"> <block type="control_ex" id="FI3q9?nQ|FDT]dY;djZz" inline="true"> <field name="TYPE">false</field> <field name="CLEAR_RUNNING">TRUE</field> <value name="OID"> <shadow type="field_oid"> <field name="oid">Object ID</field> </shadow> <block type="variables_get" id=":8ls:Akgxi%bWPgrIJT}"> <field name="VAR" id=".d{cc!R.4y2U9N+gLY1K">dpAlarmState</field> </block> </value> <value name="VALUE"> <shadow type="logic_boolean"> <field name="BOOL">TRUE</field> </shadow> <block type="text" id="MH!9j:G.S:mOaq31i!aM"> <field name="TEXT">disarmed</field> </block> </value> <value name="DELAY_MS"> <shadow type="math_number"> <field name="NUM">0</field> </shadow> <block type="math_number" id="zO=:KFH/FH-zc4ob5b7^"> <field name="NUM">1000</field> </block> </value> </block> </statement> <value name="IF2"> <block type="logic_compare" id="pHUmm^o8GqFji*VULm*Z"> <field name="OP">EQ</field> <value name="A"> <block type="on_source" id="ques8D:5Hge-)^s,XBR!"> <field name="ATTR">state.val</field> </block> </value> <value name="B"> <block type="text" id="3Hd)Fn4g#;XPXSWwe-$">
<field name="TEXT">triggered</field>
</block>
</value>
</block>
</value>
<statement name="DO2">
<block type="comment" id="c%VR#jE+K$AoZ2m%HuY_">
<field name="COMMENT">Wenn der PIN bei der Deaktivierung falsch war</field>
<next>
<block type="comment" id="I-Iasuh.K$wmTE`(e!;K">
<field name="COMMENT">Zum Beispiel MEldung an Telegram oder popupNotify </field>
<next>
<block type="comment" id="j_U/cfS;e3c]-j}Bie,7">
<field name="COMMENT">an Panel senden</field>
</block>
</next>
</block>
</next>
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
</xml>  
```
</details>  
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
* Datenpunkt AlarmPIN: Hier muss der Pfad zu dem Datenpunkt konfiguriert werden, der die original PIN enthält. Gegen diese wird bei der Eingabe vom Skript verglichen.  **Wichtig**: Dieser Datenpunkt muss manuell im ioBroker erzeugt werden. Es handelt sich nicht um den Datenpunkt **0_userdata.0.NSPanel.Alarm.AlarmPin** **!!!**
* Anzahl_NSPanles: Die Anzahl der NSPanels, die mit dem ioBroker verbunden sind  
* Notifay_OnOff: Soll es eine Information mit der **popupNotify Page** geben? wahr=an und falsch=aus.  
* Notify_Interaktion: An einem Panel wird eine Eigabe gemacht, manipulation versucht o.ä. Wer soll eine **popupNotify Page** erhalten? jeweils=nur das Panel an dem gerade eine Eingabe erfolgt oder global=alle angeschlossenen Panels  
* Notify_Event: Ein Alarm wird ausgelöst, wer soll mit einer **popupNotify Page** informiert werden? jeweils=nur das Panel an dem gerade eine Eingabe erfolgt oder global=alle angeschlossenen Panels  

<details>
  <summary>Blockly</summary>

```
<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="V^}bTjic-qB=}R30,AU7">ArlamPIN</variable>
    <variable id="z21BCrAcSmJl;/ADq)~[">NotifyText</variable>
    <variable id="MeI_x!lr~]|C?%wcOHNE">von_NSP</variable>
    <variable id="#td|(KTY]s^*yaPWKs8v">i</variable>
    <variable id="P,ZB-6|3PMPw0?#JVodG">bis_NSP</variable>
    <variable id=":X)h@$QHfe%dTO-$EY#G">Notify_OnOff</variable>
    <variable id="f9QWZ*Bv.y1Kj#nA`o{1">Anzahl_NSPanels</variable>
    <variable id="{t%:hZxc;c[vb3rv$kJk">Notify_Interaktion</variable>
    <variable id="eY_f#*}D+!2^%Orz$wy%">Notify_Event</variable>
  </variables>
  <block type="procedures_defnoreturn" id="k-sWDzSc5$UR}]Z@B._M" x="-2288" y="-512">
    <field name="NAME">Basissettings</field>
    <comment pinned="false" h="80" w="160">Beschreibe diese Funktion …</comment>
    <statement name="STACK">
      <block type="comment" id="F(ZHFr!Y$VGSMN`Ip)Lw">
        <field name="COMMENT">Bitte den Pfad zum Datenpunkt angeben:</field>
        <next>
          <block type="variables_set" id="v_e7~Lk7$*5noE:kN4:%">
            <field name="VAR" id="V^}bTjic-qB=}R30,AU7">ArlamPIN</field>
            <value name="VALUE">
              <block type="get_value" id="8AR)w}^B+x{yq1Ip.:,e">
                <field name="ATTR">val</field>
                <field name="OID">0_userdata.0.NSPanelOwn.Alarm_PIN</field>
              </block>
            </value>
            <next>
              <block type="comment" id=")86]5@KK{%rsD)5?~5UQ">
                <field name="COMMENT">Bitte geben Sie die Anzahl der Panels ein:</field>
                <next>
                  <block type="variables_set" id="g-N~0E%i@sR/wu-:e7Yy">
                    <field name="VAR" id="f9QWZ*Bv.y1Kj#nA`o{1">Anzahl_NSPanels</field>
                    <value name="VALUE">
                      <block type="math_number" id="OhIPwDGN_e?w61~~m=vY">
                        <field name="NUM">1</field>
                      </block>
                    </value>
                    <next>
                      <block type="comment" id=";0KFXJCNw439T.yy1I]w">
                        <field name="COMMENT">Soll es Popup Informationen geben?</field>
                        <next>
                          <block type="variables_set" id="}]iUGVAnHY;z={:Hse`(">
                            <field name="VAR" id=":X)h@$QHfe%dTO-$EY#G">Notify_OnOff</field>
                            <value name="VALUE">
                              <block type="logic_boolean" id="|V~EHSUO,[Hx;coEFdq$">
                                <field name="BOOL">TRUE</field>
                              </block>
                            </value>
                            <next>
                              <block type="comment" id="fauBuepr!3pC,k5ODL!O">
                                <field name="COMMENT">Wer soll alarmiert werden wenn jemand am Panel</field>
                                <next>
                                  <block type="comment" id="!1lo#]1V0/]^^KhccRyy">
                                    <field name="COMMENT">eigaben macht? (alle / jeweils)</field>
                                    <next>
                                      <block type="variables_set" id="XTuZYnfXSvGWfxOM9m1C">
                                        <field name="VAR" id="{t%:hZxc;c[vb3rv$kJk">Notify_Interaktion</field>
                                        <value name="VALUE">
                                          <block type="text" id="$Ib^BiL([$4?-}SKDU#)">
                                            <field name="TEXT">jeweils</field>
                                          </block>
                                        </value>
                                        <next>
                                          <block type="comment" id="#lIE}k||EIWU`_{{l)ix">
                                            <field name="COMMENT">Wer soll bei einem Ereigniss alarmiet werden?</field>
                                            <next>
                                              <block type="comment" id="Lq023,%.WU6mN?BDsph_">
                                                <field name="COMMENT">(alle / jeweils)</field>
                                                <next>
                                                  <block type="variables_set" id="DG8bVK-r#`$?.;eeb2:f">
                                                    <field name="VAR" id="eY_f#*}D+!2^%Orz$wy%">Notify_Event</field>
                                                    <value name="VALUE">
                                                      <block type="text" id="yt38Oa1=[`3|-VYUc[$m">
                                                        <field name="TEXT">alle</field>
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
  <block type="procedures_callnoreturn" id="$].n(^os*LrsQ+O6On([" x="-1237" y="-437">
    <mutation name="Basissettings"></mutation>
    <next>
      <block type="on_ext" id="q!?(x}z/f~TClQnNmbyU">
        <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
        <field name="CONDITION">ne</field>
        <field name="ACK_CONDITION"></field>
        <value name="OID0">
          <shadow type="field_oid" id="]~f@4kO$zmxdg=}/810C">
            <field name="oid">0_userdata.0.NSPanel.Alarm.AlarmState</field>
          </shadow>
        </value>
        <statement name="STATEMENT">
          <block type="variables_set" id="!bn8_fHJcG_-fzc_Ka)2">
            <field name="VAR" id="z21BCrAcSmJl;/ADq)~[">NotifyText</field>
            <value name="VALUE">
              <block type="text" id="EM3|V^QO@NfUB8s6?5G9">
                <field name="TEXT">.</field>
              </block>
            </value>
            <next>
              <block type="debug" id="PK!LWn;hH~-~0Voq?[E[">
                <field name="Severity">log</field>
                <value name="TEXT">
                  <shadow type="text" id="$AGq9V4ieV+V{sJ:xme?">
                    <field name="TEXT">Logpunkt: EOS</field>
                  </shadow>
                  <block type="get_value" id="shNE,X8dZ#|#JuUo0]XY">
                    <field name="ATTR">val</field>
                    <field name="OID">0_userdata.0.NSPanel.Alarm.AlarmState</field>
                  </block>
                </value>
                <next>
                  <block type="timeouts_wait" id=")UmGSw@Q(`%k^S+:-a_0">
                    <field name="DELAY">300</field>
                    <field name="UNIT">ms</field>
                    <next>
                      <block type="controls_if" id="9q977cS+cyMEB$/*D*ul">
                        <mutation elseif="3"></mutation>
                        <value name="IF0">
                          <block type="logic_operation" id="Qi_-nMKc~w;D=t4;6Mtb" inline="false">
                            <field name="OP">AND</field>
                            <value name="A">
                              <block type="logic_compare" id="aepYG60!2x|-)FcICpF8">
                                <field name="OP">EQ</field>
                                <value name="A">
                                  <block type="get_value" id="IBI6^,tt6bxnkvh2Mo@H">
                                    <field name="ATTR">val</field>
                                    <field name="OID">0_userdata.0.NSPanel.Alarm.AlarmState</field>
                                  </block>
                                </value>
                                <value name="B">
                                  <block type="text" id="W9Z5@]@$8wlW}J`R3ni~">
                                    <field name="TEXT">arming</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <value name="B">
                              <block type="logic_compare" id="z9hpZKtoM^70A7Sr;8WU" inline="false">
                                <field name="OP">NEQ</field>
                                <value name="A">
                                  <block type="get_value" id="XW/dC_x+g}-MzNT9TISq">
                                    <field name="ATTR">val</field>
                                    <field name="OID">0_userdata.0.NSPanel.Alarm.AlarmPin</field>
                                  </block>
                                </value>
                                <value name="B">
                                  <block type="variables_get" id="1vuNE@|Dx](KsJ%MFZ~E">
                                    <field name="VAR" id="V^}bTjic-qB=}R30,AU7">ArlamPIN</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                          </block>
                        </value>
                        <statement name="DO0">
                          <block type="variables_set" id=")gJKgRZ*j$=rS?u)NBo0">
                            <field name="VAR" id="z21BCrAcSmJl;/ADq)~[">NotifyText</field>
                            <value name="VALUE">
                              <block type="text_join" id="1]U2/5i@v%[sDn,EF_@A">
                                <mutation items="7"></mutation>
                                <value name="ADD0">
                                  <block type="text_multiline" id="VXJAm_V+(9+L5M6Ya!LX">
                                    <field name="TEXT">PIN-Prüfung für die Alarm Aktivierung ist fehl-geschlagen. </field>
                                  </block>
                                </value>
                                <value name="ADD1">
                                  <block type="text_newline" id="wt/QLG4y`?2L6d1w-$gW">
                                    <field name="Type">\r\n</field>
                                  </block>
                                </value>
                                <value name="ADD2">
                                  <block type="text_newline" id="j$DlHivy}5A#z%lQNZ1p">
                                    <field name="Type">\r\n</field>
                                  </block>
                                </value>
                                <value name="ADD3">
                                  <block type="text" id="p3(R.$]@}P,2`RI$^S]7">
                                    <field name="TEXT">Bitte geben Sie die richtige PIN ein. </field>
                                  </block>
                                </value>
                                <value name="ADD4">
                                  <block type="text_newline" id="byjnvx;%?[O,^6l:PH;I">
                                    <field name="Type">\r\n</field>
                                  </block>
                                </value>
                                <value name="ADD5">
                                  <block type="text_newline" id="Tq`46BlXWH/k_xjWp%+u">
                                    <field name="Type">\r\n</field>
                                  </block>
                                </value>
                                <value name="ADD6">
                                  <block type="text" id="gf_|G?Y]T)my1-+U-_cg">
                                    <field name="TEXT">Die Alarm-Funktion wird nicht aktiviert!!!</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <next>
                              <block type="debug" id=";K,gLAfyec`Hk!yt=3oI">
                                <field name="Severity">log</field>
                                <value name="TEXT">
                                  <shadow type="text" id=",Y8hu}9qWKZ$]^B7A^.Y">
                                    <field name="TEXT">Logpunkt: EOS</field>
                                  </shadow>
                                </value>
                                <next>
                                  <block type="control" id="rY{t}:)PL;jRe2{BFjqN">
                                    <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="true"></mutation>
                                    <field name="OID">0_userdata.0.NSPanel.Alarm.AlarmState</field>
                                    <field name="WITH_DELAY">TRUE</field>
                                    <field name="DELAY_MS">1000</field>
                                    <field name="UNIT">ms</field>
                                    <field name="CLEAR_RUNNING">TRUE</field>
                                    <value name="VALUE">
                                      <block type="text" id="@w%s+j7C27NHj)7)PTi{">
                                        <field name="TEXT">disarmed</field>
                                      </block>
                                    </value>
                                    <next>
                                      <block type="procedures_callnoreturn" id="finSt)zuwe0gk[/xTWis">
                                        <mutation name="Define_Notify_jeweils"></mutation>
                                        <next>
                                          <block type="timeouts_wait" id="cqF_/Gv6}_Ja:kn$,TgI">
                                            <field name="DELAY">1000</field>
                                            <field name="UNIT">ms</field>
                                            <next>
                                              <block type="procedures_callnoreturn" id="8Wz)b{s9GWBk8phr_v?+">
                                                <mutation name="PopupNotifyPage"></mutation>
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
                        <value name="IF1">
                          <block type="logic_operation" id="rac/`EKn}ES5217UOdNj" inline="false">
                            <field name="OP">AND</field>
                            <value name="A">
                              <block type="logic_compare" id=":FH~8jpIy^[Wq5m7I2#i">
                                <field name="OP">EQ</field>
                                <value name="A">
                                  <block type="get_value" id="R3_D.M$myMPZXOQKc*93">
                                    <field name="ATTR">val</field>
                                    <field name="OID">0_userdata.0.NSPanel.Alarm.AlarmState</field>
                                  </block>
                                </value>
                                <value name="B">
                                  <block type="text" id="grZhueq]1YSoGF}Q#4|B">
                                    <field name="TEXT">arming</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <value name="B">
                              <block type="logic_compare" id="08(3wUt:|2D6[BkR!nDO" inline="false">
                                <field name="OP">EQ</field>
                                <value name="A">
                                  <block type="get_value" id="]t28}qbL1);v`*zw2|Tg">
                                    <field name="ATTR">val</field>
                                    <field name="OID">0_userdata.0.NSPanel.Alarm.AlarmPin</field>
                                  </block>
                                </value>
                                <value name="B">
                                  <block type="variables_get" id="{VF5vN3n~XLz|I`eC#uX">
                                    <field name="VAR" id="V^}bTjic-qB=}R30,AU7">ArlamPIN</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                          </block>
                        </value>
                        <statement name="DO1">
                          <block type="variables_set" id="^C=Fv%^sId|JDUb?m_|%">
                            <field name="VAR" id="z21BCrAcSmJl;/ADq)~[">NotifyText</field>
                            <value name="VALUE">
                              <block type="text_join" id="v?{;Awxx;^IMifLi35fy">
                                <mutation items="4"></mutation>
                                <value name="ADD0">
                                  <block type="text_multiline" id="k.E$_-{Bi_c9(bA)^/Y;">
                                    <field name="TEXT">PIN-Prüfung für die Alarm Aktivierung war erfolgreich.</field>
                                  </block>
                                </value>
                                <value name="ADD1">
                                  <block type="text_newline" id="2,BRyz!Jl.zt^7vzlK3L">
                                    <field name="Type">\r\n</field>
                                  </block>
                                </value>
                                <value name="ADD2">
                                  <block type="text_newline" id="N^Z_EAaBtkiwyaSJmLfG">
                                    <field name="Type">\r\n</field>
                                  </block>
                                </value>
                                <value name="ADD3">
                                  <block type="text" id="e%:caDOXegY.yG0Hw(xm">
                                    <field name="TEXT">Die Alarm-Funktion wird aktiviert!!!</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <next>
                              <block type="debug" id="c@wu^=Q4}`{8k1{DJaGH">
                                <field name="Severity">log</field>
                                <value name="TEXT">
                                  <shadow type="text" id="B}H;fXknaEp0U`,R@%$T">
                                    <field name="TEXT">Logpunkt: PIN OK</field>
                                  </shadow>
                                </value>
                                <next>
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
                                        <field name="OID">0_userdata.0.NSPanel.Alarm.AlarmState</field>
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
                                        <field name="OID">0_userdata.0.NSPanel.Alarm.AlarmState</field>
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
                                    <next>
                                      <block type="procedures_callnoreturn" id="*N7CkM)1$0rW^r(fDp*`">
                                        <mutation name="Define_Notify_alle"></mutation>
                                        <next>
                                          <block type="timeouts_wait" id="bQ.:4P}@:,=bW3yP)wmF">
                                            <field name="DELAY">1000</field>
                                            <field name="UNIT">ms</field>
                                            <next>
                                              <block type="procedures_callnoreturn" id="q|j}Y|dPB1vuaMb1:Qeq">
                                                <mutation name="PopupNotifyPage"></mutation>
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
                        <value name="IF2">
                          <block type="logic_compare" id="83@!o]ZfR%d/+HrM:?Px">
                            <field name="OP">EQ</field>
                            <value name="A">
                              <block type="get_value" id="Z3#uE]AwqWO+@u!)RIjk">
                                <field name="ATTR">val</field>
                                <field name="OID">0_userdata.0.NSPanel.Alarm.AlarmState</field>
                              </block>
                            </value>
                            <value name="B">
                              <block type="text" id="2~~va?/IDi^Ypc,}KiuX">
                                <field name="TEXT">pending</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <statement name="DO2">
                          <block type="variables_set" id=")P;l6HQGS6E,,{DcCmDH">
                            <field name="VAR" id="z21BCrAcSmJl;/ADq)~[">NotifyText</field>
                            <value name="VALUE">
                              <block type="text_join" id="C`~=:fBHFHPTK$5!Do?Y">
                                <mutation items="4"></mutation>
                                <value name="ADD0">
                                  <block type="text_multiline" id="`8(`S*ZU#er6xK.uSyQy">
                                    <field name="TEXT">PIN-Prüfung für die Alarm Deaktivierung war erfolgreich.</field>
                                  </block>
                                </value>
                                <value name="ADD1">
                                  <block type="text_newline" id="N$9=1_Y_d`jG}z_ezHDw">
                                    <field name="Type">\r\n</field>
                                  </block>
                                </value>
                                <value name="ADD2">
                                  <block type="text_newline" id="aa+.*ucZi~n./QFb[Q6E">
                                    <field name="Type">\r\n</field>
                                  </block>
                                </value>
                                <value name="ADD3">
                                  <block type="text" id="HG6r-m8hCZn+m{Q#roy/">
                                    <field name="TEXT">Die Alarm-Funktion wird deaktiviert!!!</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <next>
                              <block type="debug" id="LD5HfUw{K0zCgSC$5~Ar">
                                <field name="Severity">log</field>
                                <value name="TEXT">
                                  <shadow type="text" id="h|bFzIP|UcnWd`9c*5K!">
                                    <field name="TEXT">Logpunkt: Alarm AUS</field>
                                  </shadow>
                                </value>
                                <next>
                                  <block type="controls_if" id="dFwBp8[eCMd(@G1,T4.y">
                                    <mutation elseif="1"></mutation>
                                    <value name="IF0">
                                      <block type="logic_compare" id="=8kjS[uW}NL);z}QvB^g">
                                        <field name="OP">EQ</field>
                                        <value name="A">
                                          <block type="on_source" id="2SA1/;Y5^hEGyqGJP_d(">
                                            <field name="ATTR">state.val</field>
                                          </block>
                                        </value>
                                        <value name="B">
                                          <block type="text" id="T:dwGd$$/2a0dyOohVx%">
                                            <field name="TEXT">arming</field>
                                          </block>
                                        </value>
                                      </block>
                                    </value>
                                    <statement name="DO0">
                                      <block type="control" id="Ja${;k%.vJPh2q+:kynt">
                                        <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="true"></mutation>
                                        <field name="OID">0_userdata.0.NSPanel.Alarm.AlarmState</field>
                                        <field name="WITH_DELAY">TRUE</field>
                                        <field name="DELAY_MS">1000</field>
                                        <field name="UNIT">ms</field>
                                        <field name="CLEAR_RUNNING">TRUE</field>
                                        <value name="VALUE">
                                          <block type="text" id="rkhkv?PiK-=:z?VZ1lmo">
                                            <field name="TEXT">armed</field>
                                          </block>
                                        </value>
                                      </block>
                                    </statement>
                                    <value name="IF1">
                                      <block type="logic_compare" id="7qD(L!UIQAXA/Ob)gaC.">
                                        <field name="OP">EQ</field>
                                        <value name="A">
                                          <block type="on_source" id="18v(}qF.UI}t]J[*]1dD">
                                            <field name="ATTR">state.val</field>
                                          </block>
                                        </value>
                                        <value name="B">
                                          <block type="text" id="lj/OD_Bw;l3n?}OTYkA.">
                                            <field name="TEXT">pending</field>
                                          </block>
                                        </value>
                                      </block>
                                    </value>
                                    <statement name="DO1">
                                      <block type="control" id="|:m({E)piC98ogW[zzv(">
                                        <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="true"></mutation>
                                        <field name="OID">0_userdata.0.NSPanel.Alarm.AlarmState</field>
                                        <field name="WITH_DELAY">TRUE</field>
                                        <field name="DELAY_MS">1000</field>
                                        <field name="UNIT">ms</field>
                                        <field name="CLEAR_RUNNING">TRUE</field>
                                        <value name="VALUE">
                                          <block type="text" id="dv6kxsV6jco(_c1UhG,Z">
                                            <field name="TEXT">disarmed</field>
                                          </block>
                                        </value>
                                      </block>
                                    </statement>
                                    <next>
                                      <block type="procedures_callnoreturn" id="$fp1xO#t#{)iiA@l30{k">
                                        <mutation name="Define_Notify_alle"></mutation>
                                        <next>
                                          <block type="timeouts_wait" id="{mk+%a]D|4}``9ka#(Mf">
                                            <field name="DELAY">1000</field>
                                            <field name="UNIT">ms</field>
                                            <next>
                                              <block type="procedures_callnoreturn" id="0V:m,*]:gbCAxBt:^={C">
                                                <mutation name="PopupNotifyPage"></mutation>
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
                        <value name="IF3">
                          <block type="logic_compare" id="g!1Zc_+uo4!B%%PopX/_">
                            <field name="OP">EQ</field>
                            <value name="A">
                              <block type="get_value" id="4)_D9M*J]kYbaD%+)OVA">
                                <field name="ATTR">val</field>
                                <field name="OID">0_userdata.0.NSPanel.Alarm.AlarmState</field>
                              </block>
                            </value>
                            <value name="B">
                              <block type="text" id="Zh(;x:*Au`j93^f~F/)V">
                                <field name="TEXT">triggered</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <statement name="DO3">
                          <block type="debug" id="-n`b@$}Fb8%n9;Z7[pbW">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text" id="[^))u|]1{g5PG0K..rR9">
                                <field name="TEXT">Logpunkt: Alarm Deaktivierung failed</field>
                              </shadow>
                            </value>
                            <next>
                              <block type="variables_set" id="QKRrSppBo.n7ouVDEJbv">
                                <field name="VAR" id="z21BCrAcSmJl;/ADq)~[">NotifyText</field>
                                <value name="VALUE">
                                  <block type="text_join" id="9O](,e_+R-W@5/qfJz.:">
                                    <mutation items="7"></mutation>
                                    <value name="ADD0">
                                      <block type="text_multiline" id="lS--}tPmt+B|]kPIjQ|b">
                                        <field name="TEXT">PIN-Prüfung für die Alarm De-Aktivierung ist fehlgeschlagen. </field>
                                      </block>
                                    </value>
                                    <value name="ADD1">
                                      <block type="text_newline" id="49JpPPr_tw80M+F1b5j5">
                                        <field name="Type">\r\n</field>
                                      </block>
                                    </value>
                                    <value name="ADD2">
                                      <block type="text_newline" id="Z/)?eTtW)rr(tVW[+{4S">
                                        <field name="Type">\r\n</field>
                                      </block>
                                    </value>
                                    <value name="ADD3">
                                      <block type="text" id="-Xyr?gxErWcW}K*g!-)t">
                                        <field name="TEXT">Bitte geben Sie die richtige PIN ein. </field>
                                      </block>
                                    </value>
                                    <value name="ADD4">
                                      <block type="text_newline" id="=+)Q$ly4X~/]]Y_|~H0_">
                                        <field name="Type">\r\n</field>
                                      </block>
                                    </value>
                                    <value name="ADD5">
                                      <block type="text_newline" id="?fO|6mUc|Phf].lPTj!T">
                                        <field name="Type">\r\n</field>
                                      </block>
                                    </value>
                                    <value name="ADD6">
                                      <block type="text" id="0cR|bU.~7Jv2ZSp,mQSu">
                                        <field name="TEXT">Die Alarm-Funktion bleibt aktiviert!!!</field>
                                      </block>
                                    </value>
                                  </block>
                                </value>
                                <next>
                                  <block type="procedures_callnoreturn" id="5F:91409H8F_BQT:J]n9">
                                    <mutation name="Define_Notify_jeweils"></mutation>
                                    <next>
                                      <block type="timeouts_wait" id="KJu72f^CD7p3|TR:k,Kd">
                                        <field name="DELAY">1000</field>
                                        <field name="UNIT">ms</field>
                                        <next>
                                          <block type="procedures_callnoreturn" id="F*/F}`N`[3Oi$vHFmsRp">
                                            <mutation name="PopupNotifyPage"></mutation>
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
        </statement>
      </block>
    </next>
  </block>
  <block type="procedures_defnoreturn" id="Xd+cmfHTG`d$dB[4jSsv" x="-2287" y="-62">
    <field name="NAME">Define_Notify_jeweils</field>
    <comment pinned="false" h="80" w="160">Beschreibe diese Funktion …</comment>
    <statement name="STACK">
      <block type="controls_if" id="yeOz*:rj%ziH+6sD0_PQ">
        <value name="IF0">
          <block type="logic_operation" id="pXbO/EN-|qJ%_[|a369J" inline="false">
            <field name="OP">OR</field>
            <value name="A">
              <block type="logic_compare" id="?;B0m3{TYTVQKx8e`hk_">
                <field name="OP">EQ</field>
                <value name="A">
                  <block type="variables_get" id="kyvyO^CLozO1ln-4iKG|">
                    <field name="VAR" id="{t%:hZxc;c[vb3rv$kJk">Notify_Interaktion</field>
                  </block>
                </value>
                <value name="B">
                  <block type="text" id="uYwk;$%uv9Iz;zdK9MhP">
                    <field name="TEXT">jeweils</field>
                  </block>
                </value>
              </block>
            </value>
            <value name="B">
              <block type="logic_compare" id="v=$w[o)sTMh,X7?*Ed5p">
                <field name="OP">EQ</field>
                <value name="A">
                  <block type="variables_get" id="A[ru[]3EOo]|~UW)8(#Y">
                    <field name="VAR" id="eY_f#*}D+!2^%Orz$wy%">Notify_Event</field>
                  </block>
                </value>
                <value name="B">
                  <block type="text" id="Nar}c$ZKP:=fZkx![l`9">
                    <field name="TEXT">jeweils</field>
                  </block>
                </value>
              </block>
            </value>
          </block>
        </value>
        <statement name="DO0">
          <block type="variables_set" id="9(Js/pa+cy*@Oj$%dWs|">
            <field name="VAR" id="MeI_x!lr~]|C?%wcOHNE">von_NSP</field>
            <value name="VALUE">
              <block type="text_charAt" id="e)3;e0XQJCd,[+BvUpDS" inline="false">
                <mutation at="true"></mutation>
                <field name="WHERE">FROM_END</field>
                <value name="VALUE">
                  <block type="get_value" id="?m+eOB!MslRD`Vre6TeJ">
                    <field name="ATTR">val</field>
                    <field name="OID">0_userdata.0.NSPanel.Alarm.PANEL</field>
                  </block>
                </value>
                <value name="AT">
                  <block type="math_number" id="?|[u@KOd4mF/0IdmEfY|">
                    <field name="NUM">2</field>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="variables_set" id="xMT}9v0/_JeYrfbmZg0(">
                <field name="VAR" id="P,ZB-6|3PMPw0?#JVodG">bis_NSP</field>
                <value name="VALUE">
                  <block type="text_charAt" id="m17$HL~,=+^LeLf5Iycg" inline="false">
                    <mutation at="true"></mutation>
                    <field name="WHERE">FROM_END</field>
                    <value name="VALUE">
                      <block type="get_value" id="x[1q8.|XAvC/iz_|QjSC">
                        <field name="ATTR">val</field>
                        <field name="OID">0_userdata.0.NSPanel.Alarm.PANEL</field>
                      </block>
                    </value>
                    <value name="AT">
                      <block type="math_number" id="V/I@Cc`$(jMInmN19XH;">
                        <field name="NUM">2</field>
                      </block>
                    </value>
                  </block>
                </value>
              </block>
            </next>
          </block>
        </statement>
      </block>
    </statement>
  </block>
  <block type="procedures_defnoreturn" id="lH#8*[d@k%$BgU%8XV]U" x="-2287" y="363">
    <field name="NAME">Define_Notify_alle</field>
    <comment pinned="false" h="80" w="160">Beschreibe diese Funktion …</comment>
    <statement name="STACK">
      <block type="controls_if" id="!wi6cs;rP*q:=Hf4Wx1z">
        <value name="IF0">
          <block type="logic_operation" id="-3JhDry!`O,~yTug?QwG" inline="false">
            <field name="OP">OR</field>
            <value name="A">
              <block type="logic_compare" id="vJ!t,E$iFdxIT%CRe@Pa">
                <field name="OP">EQ</field>
                <value name="A">
                  <block type="variables_get" id="3izSk]Dyd`#W.vN-kcF{">
                    <field name="VAR" id="{t%:hZxc;c[vb3rv$kJk">Notify_Interaktion</field>
                  </block>
                </value>
                <value name="B">
                  <block type="text" id="zDJuQ!z?$xT^*I}F[@G$">
                    <field name="TEXT">alle</field>
                  </block>
                </value>
              </block>
            </value>
            <value name="B">
              <block type="logic_compare" id="JYaI:[3du21WaVf5Rh+e">
                <field name="OP">EQ</field>
                <value name="A">
                  <block type="variables_get" id="ukrgMPx0xYX=#Zz66FI#">
                    <field name="VAR" id="eY_f#*}D+!2^%Orz$wy%">Notify_Event</field>
                  </block>
                </value>
                <value name="B">
                  <block type="text" id="xVu+!M,rR[4m9BLzQ$(x">
                    <field name="TEXT">alle</field>
                  </block>
                </value>
              </block>
            </value>
          </block>
        </value>
        <statement name="DO0">
          <block type="variables_set" id=".jNoC73XV7W!`{n5oT5y">
            <field name="VAR" id="MeI_x!lr~]|C?%wcOHNE">von_NSP</field>
            <value name="VALUE">
              <block type="math_number" id=")8`6(NG;YRqXTGvI9gcJ">
                <field name="NUM">1</field>
              </block>
            </value>
            <next>
              <block type="variables_set" id="M#@2U_+@xP^P[K#5n^x:">
                <field name="VAR" id="P,ZB-6|3PMPw0?#JVodG">bis_NSP</field>
                <value name="VALUE">
                  <block type="variables_get" id="q+)Ad7%:m7(pJL18%U%C">
                    <field name="VAR" id="f9QWZ*Bv.y1Kj#nA`o{1">Anzahl_NSPanels</field>
                  </block>
                </value>
              </block>
            </next>
          </block>
        </statement>
      </block>
    </statement>
  </block>
  <block type="procedures_defnoreturn" id="d@]*oWnF~Qy+?%ICZT60" x="-2288" y="562">
    <field name="NAME">PopupNotifyPage</field>
    <comment pinned="false" h="80" w="160">Beschreibe diese Funktion …</comment>
    <statement name="STACK">
      <block type="controls_if" id="0$T/J1pQ0Bu|l_r-eiT7">
        <value name="IF0">
          <block type="logic_compare" id="t00`dP]4!xU.mx!09Emk">
            <field name="OP">EQ</field>
            <value name="A">
              <block type="variables_get" id="iF@W)OFbwsFP8c/wZ0qz">
                <field name="VAR" id=":X)h@$QHfe%dTO-$EY#G">Notify_OnOff</field>
              </block>
            </value>
            <value name="B">
              <block type="logic_boolean" id="-Kd$a%1~)%hjgzRiDhOZ">
                <field name="BOOL">TRUE</field>
              </block>
            </value>
          </block>
        </value>
        <statement name="DO0">
          <block type="controls_for" id=")svr8HYs)cRokOHJwSnp">
            <field name="VAR" id="#td|(KTY]s^*yaPWKs8v">i</field>
            <value name="FROM">
              <shadow type="math_number" id="T5dgh=caUCsv}qcKoRPo">
                <field name="NUM">1</field>
              </shadow>
              <block type="variables_get" id="nM-cXh4F|y=#ppGw;^#3">
                <field name="VAR" id="MeI_x!lr~]|C?%wcOHNE">von_NSP</field>
              </block>
            </value>
            <value name="TO">
              <shadow type="math_number" id="[Pr}%moU|NGz_~ly#*mv">
                <field name="NUM">1</field>
              </shadow>
              <block type="variables_get" id="qSHt+sYSu3Dg`Y6?Kq}{">
                <field name="VAR" id="P,ZB-6|3PMPw0?#JVodG">bis_NSP</field>
              </block>
            </value>
            <value name="BY">
              <shadow type="math_number" id="=*`$tg+B@.kmh=x%A`:m">
                <field name="NUM">1</field>
              </shadow>
            </value>
            <statement name="DO">
              <block type="control_ex" id="%ixt}0-_BS8RK/E*j9=l">
                <field name="TYPE">true</field>
                <field name="CLEAR_RUNNING">FALSE</field>
                <value name="OID">
                  <shadow type="field_oid" id="_]Nw+No=[IC(]-nTYRzC">
                    <field name="oid">Object ID</field>
                  </shadow>
                  <block type="text_join" id="bQheA_|HSN{kpOuizb[L" inline="false">
                    <mutation items="4"></mutation>
                    <value name="ADD0">
                      <block type="text" id="pL:i[^RQk,8N%q`@XJ4Y">
                        <field name="TEXT">0_userdata.0.NSPanel.</field>
                      </block>
                    </value>
                    <value name="ADD1">
                      <block type="variables_get" id="?$$3nXw50U${I_kpwQP*">
                        <field name="VAR" id="#td|(KTY]s^*yaPWKs8v">i</field>
                      </block>
                    </value>
                    <value name="ADD2">
                      <block type="text" id="fBT}2zaC$?bKMD8hpwxP">
                        <field name="TEXT">.popupNotify.</field>
                      </block>
                    </value>
                    <value name="ADD3">
                      <block type="text" id="vydvDzB8l{!gF5!E[#|u">
                        <field name="TEXT">popupNotifyHeading</field>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="VALUE">
                  <shadow type="logic_boolean" id="iPo49!.y!/8BvEp0_f(i">
                    <field name="BOOL">TRUE</field>
                  </shadow>
                  <block type="text" id="PWqQYl^EYacUuX5fM^Z#">
                    <field name="TEXT">PIN Prüfung</field>
                  </block>
                </value>
                <value name="DELAY_MS">
                  <shadow type="math_number" id="I{[WgP6u8x)};8lQvfUG">
                    <field name="NUM">0</field>
                  </shadow>
                </value>
                <next>
                  <block type="control_ex" id="2V`@aoNscFi*ag?|~ih3">
                    <field name="TYPE">true</field>
                    <field name="CLEAR_RUNNING">FALSE</field>
                    <value name="OID">
                      <shadow type="field_oid" id="ZZ(Sf2Zus6q!zIaO_:(4">
                        <field name="oid">Object ID</field>
                      </shadow>
                      <block type="text_join" id="Fb!8XI^(8NY#hDmr:6-z" inline="false">
                        <mutation items="4"></mutation>
                        <value name="ADD0">
                          <block type="text" id="JeiGE7Gi|f$x2C?07%,h">
                            <field name="TEXT">0_userdata.0.NSPanel.</field>
                          </block>
                        </value>
                        <value name="ADD1">
                          <block type="variables_get" id="0lj^,2[$|2X,4r1N-$iU">
                            <field name="VAR" id="#td|(KTY]s^*yaPWKs8v">i</field>
                          </block>
                        </value>
                        <value name="ADD2">
                          <block type="text" id="0zug@aeCaimUqBz|I^mM">
                            <field name="TEXT">.popupNotify.</field>
                          </block>
                        </value>
                        <value name="ADD3">
                          <block type="text" id="oR12T83doJ5^gO/.J~r/">
                            <field name="TEXT">popupNotifyText</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <value name="VALUE">
                      <shadow type="logic_boolean" id="]z?R/Sen^TgiWnNF8#wY">
                        <field name="BOOL">TRUE</field>
                      </shadow>
                      <block type="variables_get" id="C7$#ZI-Mb2uSKQX:r$JB">
                        <field name="VAR" id="z21BCrAcSmJl;/ADq)~[">NotifyText</field>
                      </block>
                    </value>
                    <value name="DELAY_MS">
                      <shadow type="math_number" id="639Gs09jN8*8Z$p!,b?N">
                        <field name="NUM">0</field>
                      </shadow>
                    </value>
                    <next>
                      <block type="control_ex" id="}FY*}#^,k*gw8T#EW^nM">
                        <field name="TYPE">true</field>
                        <field name="CLEAR_RUNNING">FALSE</field>
                        <value name="OID">
                          <shadow type="field_oid" id="7qxmx0%[Pmg.O{3hvAo3">
                            <field name="oid">Object ID</field>
                          </shadow>
                          <block type="text_join" id="46blI{i^JHCi/3#{KpH2" inline="false">
                            <mutation items="4"></mutation>
                            <value name="ADD0">
                              <block type="text" id="T**;n.-OQ})wjL_F^Fnb">
                                <field name="TEXT">0_userdata.0.NSPanel.</field>
                              </block>
                            </value>
                            <value name="ADD1">
                              <block type="variables_get" id="faC`%lJS~OWARmB0JboO">
                                <field name="VAR" id="#td|(KTY]s^*yaPWKs8v">i</field>
                              </block>
                            </value>
                            <value name="ADD2">
                              <block type="text" id="~d/4?qF,K-a+,`)g9Yq2">
                                <field name="TEXT">.popupNotify.</field>
                              </block>
                            </value>
                            <value name="ADD3">
                              <block type="text" id="!9R@]Skk9v8G)cs#%(Si">
                                <field name="TEXT">popupNotifyInternalName</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <value name="VALUE">
                          <shadow type="logic_boolean" id="I4PsJQb;6k+70^g*Xt/}">
                            <field name="BOOL">TRUE</field>
                          </shadow>
                          <block type="math_random_float" id="C5/h)jq=yPM?,9J=(w65"></block>
                        </value>
                        <value name="DELAY_MS">
                          <shadow type="math_number" id="+6#n%fO}e4h%;FhKPV0c">
                            <field name="NUM">0</field>
                          </shadow>
                        </value>
                        <next>
                          <block type="control_ex" id="eW#GY^jo23l+eN#CoT$M">
                            <field name="TYPE">true</field>
                            <field name="CLEAR_RUNNING">FALSE</field>
                            <value name="OID">
                              <shadow type="field_oid" id="3o8k@mP?7Ywt6*jB!,8]">
                                <field name="oid">Object ID</field>
                              </shadow>
                              <block type="text_join" id="=Jbr9H[#fd:BXDJE;!~g" inline="false">
                                <mutation items="4"></mutation>
                                <value name="ADD0">
                                  <block type="text" id="Dkw9*R%h3UC@_6JdEoou">
                                    <field name="TEXT">0_userdata.0.NSPanel.</field>
                                  </block>
                                </value>
                                <value name="ADD1">
                                  <block type="variables_get" id="{b_,T@_J-F1^#Q:nUV!$">
                                    <field name="VAR" id="#td|(KTY]s^*yaPWKs8v">i</field>
                                  </block>
                                </value>
                                <value name="ADD2">
                                  <block type="text" id="YR.Hj!%h7S+~o,)`a47l">
                                    <field name="TEXT">.popupNotify.</field>
                                  </block>
                                </value>
                                <value name="ADD3">
                                  <block type="text" id="vDwU)eC8@zGy`HbGhs`9">
                                    <field name="TEXT">popupNotifyButton1Text</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <value name="VALUE">
                              <shadow type="logic_boolean" id=",+yQK0~%FlOBhJOW`}c;">
                                <field name="BOOL">TRUE</field>
                              </shadow>
                              <block type="text" id="kkpU;l:U$Q!c1.sZGGn0">
                                <field name="TEXT"></field>
                              </block>
                            </value>
                            <value name="DELAY_MS">
                              <shadow type="math_number" id="4kn(ykK1x^=+f^[6?eL.">
                                <field name="NUM">0</field>
                              </shadow>
                            </value>
                            <next>
                              <block type="control_ex" id="srm~vP#V^(_NS+Z5!586">
                                <field name="TYPE">true</field>
                                <field name="CLEAR_RUNNING">FALSE</field>
                                <value name="OID">
                                  <shadow type="field_oid" id="B9$OLw-N4tH^.U[@6^MG">
                                    <field name="oid">Object ID</field>
                                  </shadow>
                                  <block type="text_join" id="0;/IVbs0HM0%B3,Szv=p" inline="false">
                                    <mutation items="4"></mutation>
                                    <value name="ADD0">
                                      <block type="text" id="Ru|Wv=5Z0tRBZHi!:)*p">
                                        <field name="TEXT">0_userdata.0.NSPanel.</field>
                                      </block>
                                    </value>
                                    <value name="ADD1">
                                      <block type="variables_get" id="Sm-s5MM(b]yKxJ.Q9r$@">
                                        <field name="VAR" id="#td|(KTY]s^*yaPWKs8v">i</field>
                                      </block>
                                    </value>
                                    <value name="ADD2">
                                      <block type="text" id="[`o53K4sK^WeMg7WTg:o">
                                        <field name="TEXT">.popupNotify.</field>
                                      </block>
                                    </value>
                                    <value name="ADD3">
                                      <block type="text" id="PdMpY!OV[.4HbO#HaF?q">
                                        <field name="TEXT">popupNotifyButton2Text</field>
                                      </block>
                                    </value>
                                  </block>
                                </value>
                                <value name="VALUE">
                                  <shadow type="logic_boolean" id="m@1+5uV%afa{==^;ZiJW">
                                    <field name="BOOL">TRUE</field>
                                  </shadow>
                                  <block type="text" id="azRNP@I}sP9P$[xv!(V=">
                                    <field name="TEXT">OK</field>
                                  </block>
                                </value>
                                <value name="DELAY_MS">
                                  <shadow type="math_number" id=":3mTg{8T3T`fE#+dN;mU">
                                    <field name="NUM">0</field>
                                  </shadow>
                                </value>
                                <next>
                                  <block type="control_ex" id="s/?G;GJ?v*M`uM8rRH`b">
                                    <field name="TYPE">true</field>
                                    <field name="CLEAR_RUNNING">FALSE</field>
                                    <value name="OID">
                                      <shadow type="field_oid" id="]1i8~,0zj|KA/,gG@;@q">
                                        <field name="oid">Object ID</field>
                                      </shadow>
                                      <block type="text_join" id="2Kb}#zGe_]w|2fAP+m-)" inline="false">
                                        <mutation items="4"></mutation>
                                        <value name="ADD0">
                                          <block type="text" id="U+f.W80f^rZrb6ZG[Ls)">
                                            <field name="TEXT">0_userdata.0.NSPanel.</field>
                                          </block>
                                        </value>
                                        <value name="ADD1">
                                          <block type="variables_get" id="+Wj{ik8}5Es3R1CZ+HR+">
                                            <field name="VAR" id="#td|(KTY]s^*yaPWKs8v">i</field>
                                          </block>
                                        </value>
                                        <value name="ADD2">
                                          <block type="text" id="|EccNLcd6iBLEIAr/]?)">
                                            <field name="TEXT">.popupNotify.</field>
                                          </block>
                                        </value>
                                        <value name="ADD3">
                                          <block type="text" id="q0{i6PD]jyrAI1XBmu.c">
                                            <field name="TEXT">popupNotifySleepTimeout</field>
                                          </block>
                                        </value>
                                      </block>
                                    </value>
                                    <value name="VALUE">
                                      <shadow type="logic_boolean" id="!xR.7uuf7p}qgw/}r/.c">
                                        <field name="BOOL">TRUE</field>
                                      </shadow>
                                      <block type="math_number" id="VH-ysksu6V8,2E#pI~~#">
                                        <field name="NUM">0</field>
                                      </block>
                                    </value>
                                    <value name="DELAY_MS">
                                      <shadow type="math_number" id="f4i[r~rI4+/!%szgP=xz">
                                        <field name="NUM">0</field>
                                      </shadow>
                                    </value>
                                    <next>
                                      <block type="control_ex" id="P/H8{MR@:scdemX?(6x4">
                                        <field name="TYPE">true</field>
                                        <field name="CLEAR_RUNNING">FALSE</field>
                                        <value name="OID">
                                          <shadow type="field_oid" id=")SxK}$m:CoWOV!.|1r$n">
                                            <field name="oid">Object ID</field>
                                          </shadow>
                                          <block type="text_join" id="8OpvNb(tX).Liui9s~tO" inline="false">
                                            <mutation items="4"></mutation>
                                            <value name="ADD0">
                                              <block type="text" id="=7plLs/vl;1(TVF1s2S4">
                                                <field name="TEXT">0_userdata.0.NSPanel.</field>
                                              </block>
                                            </value>
                                            <value name="ADD1">
                                              <block type="variables_get" id="XZm]p,d-`^CbrUzwJur5">
                                                <field name="VAR" id="#td|(KTY]s^*yaPWKs8v">i</field>
                                              </block>
                                            </value>
                                            <value name="ADD2">
                                              <block type="text" id="IBcU;^bN+J9yQ:%.astu">
                                                <field name="TEXT">.popupNotify.</field>
                                              </block>
                                            </value>
                                            <value name="ADD3">
                                              <block type="text" id="o(%lzZ@76pI^|5N,oRJ#">
                                                <field name="TEXT">popupNotifyAction</field>
                                              </block>
                                            </value>
                                          </block>
                                        </value>
                                        <value name="VALUE">
                                          <shadow type="logic_boolean" id="`5lH.U,vv{X)?c%w_OlQ">
                                            <field name="BOOL">TRUE</field>
                                          </shadow>
                                        </value>
                                        <value name="DELAY_MS">
                                          <shadow type="math_number" id="{-`eG8LdS_9GTK)Z*w~:">
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
                </next>
              </block>
            </statement>
          </block>
        </statement>
      </block>
    </statement>
  </block>
</xml> 
```
</details> 

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

**11.) PV-Daten Info Seite**  

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
