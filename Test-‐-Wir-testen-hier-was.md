Auf dieser Seite testen wir was für die zukünftige Wiki

# Einleitung
  
  
  
# Geblubber
  
  
# Page Aufbau
  
Eine Page, also eine Seite des NSPanles hat einen bestimmten Aufbau.  
Es gibt Teile, die sind bei jeder Seite gleich, es gibt Teile die immer da sein müssen, es gibt Teile die sind optional und je nach Typ der Seite variiert der Aufbau ein wenig.

## Page Typ  
Beginnen wir damit, dass man sich, bevor man eine Seite "zusammenstellet" / programmiert darüber Gedanken machen muss, wie die Seite aussehen soll. In den allermeisten Fällen wird es auf eine Seite vom Typ **PageEntities** oder **PageGrid(2)** hinauslaufen.  
gegenwärtig haben wir folgende Page Typen zur Auswahl:  
  
### PageEntities:
Auf dieser Seite hat man bis zu 4 Zeilen zur Verfügung.  
Links kann man ein Icon platzieren, in der Mitte folgt ein Text/Beschreibung und rechts folgt ein Switch, Ein Wert, ein Regler oder ein Button (PRESS).  
Je nach Alias, kann man über den Touch/Klick auf den Eintrag zu einer Unterseite, einem sogenannten Popup gelangen.
  
### PageGrid(2):
Beim PageGrid steht das Icon im Vordergrund. Man hat hier ein Raster, man kann es sich auch wie eine Tabelle vorstellen. Diese hat zwei Zeilen und entweder 3 Spalten (bei der CardGrid) oder 4Spalten (bei der CardGrid2).  
In jeder Zelle der Tabelle kann man ein Icon platzieren mit einer Beschriftung.
  
### PageMedia:
PageMedia ist letztlich ein Player, der es ermöglicht Streams auf spezifischen Geräten abzuspielen. Der Umfang ist hier stark vom Service abhängig.  
Auf der pageMedia lassen sich an bestimmten Stellen das sogenannte **InSelPopup** integrieren, um beispielsweise Abspielgeräte, Playlists oder Senderlisten, etc. aufzulisten.  
  
### PageThermo:
Egal ob Thermostate, Klimaanlagen, Wärmepumpen, Smarte Ventilatoren, etc. - mit der CardThermo lässt sich vieles Steuern was eine Temperaturregelung hat. je nach Alias-Einstellungen können die Unterschiedlichsten MODE und Informationen abgebildet werden.  
  
### PageAlarm:
Die Alarmanlage über das NSPanel steuern?  
Mit der PageAlarm kann man sie zumindest ein- und ausschalten und unterschiedliche Level schalten.  
  
### PageUnlock:
Man möchte den Zugriff auf das NSPanel kontrollieren / limitieren?  
Kein Problem mit der PageUnlock bestimmen sie, wer das smarte Zuahause steuern darf ;-)  
  
### PageChart:
Für alle die Diagramme und Statistiken lieben und auch auf diese nicht auf dem 4" großen Display verzichten möchten, gibt es die **CardChart** und **CardLChart** zur Darstellunf von Säulen- und Linien-Diagramm.  
  
### PagePower:
Sie haben eine PV-Anlage und möchten den Stromfluss darstellen? Dafür haben wir die PagePower.  
  
### PageQR:
Gäste sollen einfach und easy ins Gäste-WLAN rein kommen? Am besten mit dem Scann eines QR-Codes? Voila, dafür haben wir die PageQR.
  
## How 2 Page:
  
### Basisseite
Der Rahmen einer Seite  besteht aus einem Frame wie folgend:  
```
let name = <PageType>
{
    'type': 'cardType',
    'heading': 'Seiten Überschrift',
    'useColor': true,
    'items': []
};  
```  
  
* `let name =` : Das Wort name ist hier ein Platzhalter. Man gibt der Seite hier einen eindeutigen Namen, allerdings bitte ohne Leerzeichen bei mehreren Worten und vermeide Sonderzeichen. Dieser Name muss im weiteren Verlauf des Skriptes noch einmal aufgeführt werden (Wichtig für die Darstellung und Navigation)  
* `<PageType>` : Type muss durch den richtigen Seiten Typ (Entities, Chart, Power, Grid, etc.) ersetzt werden. Page davor bleibt bestehen, so dass man dann zum Beispiel ein <PageEntities> oder <PageGrid> erhält. Wichtig, PageType ist immer von einer Spitzen Klammer eingefasst.  
* `type` : Der Typ der Seite, wie zuvor schon beschrieben. PageType und type haben immer den gleichen Postfix. Bei type ist es aber CardType stattPageType. Folglich haben wir hier in Hochkomma eingefasst 'cardEntities' oder 'cardGrid', etc.  
* `heading` :  Der Seitenname oder auch Überschrift, der auf der Seite auf dem NSPanel oben in der Mitte dargestellt wird. er ist in Hochkommas zu fassen.  
* `useColor` :  Wird in der Regel mit `true` angegeben  
* `items` :  Hier wird der eigentliche Inhalt der Seite eingetragen. Pro dazustellendem Element erfasst man hier ein sogenanntes `<PageItem>` welches dann die darzustellenden Parameter erhält.  
  
Bis hier her haben wir eine leere Seite erstellt. Wenn ich meinen Page/Card Type festgelegt habe, der Seite einen Namen gegeben, eine Überschrift definiert habe, kann ich mich nun daran machen den Inhalt der Seite aufzubauen.  
Als Zwischen-Test kann man den definierten `name` im Skript unter **pages** hinzufügen, das Skript neu starten und dann auf dem NSPanel schauen, ob die neue Seite (ohne Inhalt) schon angezeigt wird.  
  
### Optionale Parameter  
Bevor wir aber zur Erstellung der **PageItem** kommen, noch optionale Parameter, die man hier setzen kann:  
* `subPage` :  Wird, sofern man mit Unterseite arbeiten möchte, mit `true` gefasst in Hochkommas gesetzt. Der Parameter `subPage = true` definiert diese Seite als eine Unterseite von XY
* `parent` :  Wird `subPage = true` definiert, dann kann man mit **parent** den Namen der höher gelegenen Seite definieren. Dies hat Auswirkung auf die Steuerung und die Blätterpfeile oben auf der Seite. Der Name der höher gelegenen Seite ist in Hochkommas zu fassen  
  
Es gibt noch weitere optionale Parameter, jedoch gehören Die alle zum Thema Navigation. Hierzu gibt es [hier](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-Navigation) in der Wiki eine Beschreibung, so dass wir an dieser Stelle nicht noch einmal darauf eingehen möchten.
  
### Seiteninhalt - PageItem - definieren  
Das `<PageItem>` -  wenn man es mal frei übersetzt , das Seiten-Gegenstand definiert einen auf der Seite Sichtbaren Wert / Schalter. Was ein **PageItem** relativ immer mit sich bringt, ist eine **ID**, ein **Name** und eine **Farbdefinition**.  
```
<PageItem>{ id: 'alias.0.NSPanel_1.Luftreiniger', name: 'Luftreiniger', icon: 'power', icon2: 'power',offColor: MSRed, onColor: MSGreen},
```
Das `<PageItem>` wird gefolgt von `{},`. Innerhalb der geschweiften Klammern folgt die weitere Konfiguration:  
 
**Mindestangabe**:   
* `id` :  Pfad zum Alias, der verwendet wird, in Hochkomma eingefasst
* `name` :  Text der als Label auf dem Display zu einem PageItem dargestellt wird
  
>[!IMPORTANT]
>`name` ist kein muss, wenn der Alias richtig konfiguriert ist. Dann wird der Name aus dem `common.name.de` gezogen.
  
Optionale / spezifische Angaben:  
  
**Angaben für icon-Farbe**:  
* `offColor` :  Farbe für ausgeschaltet
* `onColor` :  Farbe für eingeschaltet
* `useColor` :  wird mit  `true` oder `false` angegeben und verwendet bei `true` die definierten Config-Parameter **defaultOnColor** und **defaultOffColor**, sofern keine `onColor` oder `offColor` im `<PageItem>` als Parameter definiert sind  
* `colorScale` :  Colorscale ist ein Farbverlauf von Rot über Gelb nach Grün mit einem Bereich von 0 bis 10.
  * val_min -> Rot
  * val_max -> Grün
  * in Verbindung mit val_best, ist val_best Grün und val_min und val_max Rot  
  
>[!IMPORTANT]  
>Sofern keine icon-Farbe definiert wird, gibt es eine Default Farbkombination. Kann unter **defaultColor** (**defaultOnColor** & **defaultOffColor**) in der Konfiguration festgelegt werden.  
  
**Angaben für Label**:
* `prefixName` : Erweiterung für `name`. Setzt einen Text als Prefix vor  `name`
* `suffixName` : Erweiterung für `name`. Setzt einen Text als Postfix nach  `name` 
* `buttonText` : ersetzt den Standard Text “PRESS” auf der cardEntities 
* `fontSize` : Auf der **cardGrid(2)** kann man mit diesem Attribut die Schriftgröße auf  einen Wert zw. **0** und **5** gesetzt werden.  
  * Font 0 - Default - Size 24 (No Icons, Support for various special chars from different langs)
  * Font 1 - Size 32 (Icons and limited chars)  
  * Font 2 - Size 32 (No Icons, Support for various special chars from different langs)  
  * Font 3 - Size 48 (Icons and limited chars)  
  * Font 4 - Size 80 (Icons and limited chars)  
  * Font 5 - Size 128 (ascii only)  
  
**Definition Icons**:
* `icon` : Ein Icon für den An-Status
* `icon2` : Ein Icon für den Aus-Status. `icon2` wird nicht bei allen Alias unterstützt
 
> [!NOTE]  
> Die Icon-Namen müssen aus der [Icondatei](https://htmlpreview.github.io/?https://github.com/jobr99/Generate-HASP-Fonts/blob/master/cheatsheet.html) stammen. `icon` bzw. `icon2` übersteuern ein Icon welches per Default vom Alias kommt. Bei vielen Alias ist es nicht notwendig ein `icon(2)` zu definieren. Die Option steht einem aber jederzeit zur Verfügung.  
  
**Einheiten und Werte**:
* `unit` :  in Hochkomma gesetzte Einheit (z.B. °C) gilt nicht für alle Rollen
* `useValue` :  muss auf ‘true’, wenn fontSize genutzt wird
* `minValue` :  legt den Startwert für den Slider fest
* `maxValue` :  legt den Endwert für den Slider fest
* `modeList` :  Ermöglicht ein **InSelPopup** für die Auswahl weiterer Werte. Wird in `[``, ``, ``]` gefasst und enthält eine Kommaseparierte Liste an Werten 
  
**Angaben für Licht**:  
* `interpolateColor` :  wird mit  `true` oder `false` angegeben und errechnet bei `true` die aktuelle Farbe des Leuchtmittels  
  
  **Angaben für PopupLight**  
  * `minValueBrightness` :  legt den Startwert für den Slider Helligkeit fest
  * `maxValueBrightness` :  legt den Endwert für den Slider Helligkeit fest
  * `minValueColorTemp` :  legt den Startwert für den Slider Farbtemperatur fest
  * `maxValueColorTemp` :  legt den Endwert für den Slider Farbtemperatur fest
  
**Angabe für Rolladen (PopupShutter)**
* `secondRow` : gehört zur popupPage Shutter (Text für die zweite Zeile)  
  
Angaben für Navigation und Subpages:  
* `navigate` :  Ersetzt `id` und wird mit `true` gesetzt und benötigt **targetPage**. Öffnet eine Subpage
* `targetPage` :  Zielseite die geöffnet wird, wenn man eine in navigate definierte SubPage öffnen will  
  
**CardChart** speziefische Angabe:  
* `yAxis` :  name der y-Achse
* `yAxisTicks` :  Werte-Skala der yAchse Wird in `[``, ``, ``]` gefasst und enthält eine Kommaseparierte Liste an Werten
* `onColor` : Farbe der Balken
  
**CardQR** speziefische Angabe:  
* `hidePassword` :  
  
**CardMedia** speziefische Konfiguration:
* `adapterPlayerInstance` :  
* `mediaDevice` :  
* `speakerList` :  
* `playList` :  
* `equalizerList` :  
* `colorMediaIcon` :  
* `colorMediaArtist` :  
* `colorMediaTitle` :  
* `autoCreateALias` :  
  
**CardThermo** speziefische Konfiguration
* `stepValue` :  
* `iconArray` :  
* `popupThermoMode1` :  
* `popupThermoMode2` :  
* `popupThermoMode3` :  
* `popUpThermoName` :  
* `setThermoAlias` :  
  

  
***  
  
  
# Page Beispiele  
 
<details>
  <summary>Übersicht der Beispiele</summary>  
  
* PageEntities:  
  * **cardEntities:** Color Aliase 1
  * **cardEntities:** Color Aliase 2
  * **cardEntities:** Sonstige Aliase
  * **cardEntities:** Büro
  * **cardEntities:** Fenster und Türen
  * **cardEntities:** Button Aliase
  * **cardEntities:** Test Subpages
  * **cardEntities:** Abfallkalender
  * **cardEntities:** Büro  

* PageGrid2:
  * **cardGrid2:** Büro 2

* PageGrid:
  * **cardGrid:** Radiosender
  * **cardGrid:** WLED Stripes WZ
  * **cardGrid:** Sensor Werte
  * **cardGrid:** Radio

* PageMedia:
  * **cardMedia:** Alexa
  * **cardMedia:** Sonos
  * **cardMedia:** Spotify-Premium
  * **cardMedia:** SqueezeboxRPC

* PageThermo:
  * **cardThermo:** Test Thermostat
  * **cardThermo:** Test Klimaanlage
  * **cardThermo:** Pool Wärmepumpe

* PageAlarm:
  * **cardAlarm:** Alarmanlage  

* PageUnlock:
  * **cardUnlock:** Service Pages

* PageChart:
  * **cardChart:** Stromzähler L1+L2+L3
  * **cardLChart:** Büro Temperatur

* PagePower:
  * **cardPower:** cardPower Emulator
  
* PageQR:  
  * **cardQR:** Gäste WLAN 
</details>  
  
***
   
<details>
  <summary>PageEntities</summary> 
  
## CardEntities 
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/16930a8e-88cd-468d-9502-4c6c51293434)
  
``` 
let Buero_Seite_1 = <PageEntities>
{
    'type': 'cardEntities',
    'heading': 'Büro',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel_1.Schreibtischlampe', interpolateColor: true},
        <PageItem>{ id: 'alias.0.NSPanel_1.Deckenbeleuchtung', interpolateColor: true},
        <PageItem>{ id: 'alias.0.NSPanel_1.ShellyDuoTest', name: 'Shelly Duo GU10', minValueBrightness: 0, maxValueBrightness: 100, minValueColorTemp: 6465, maxValueColorTemp: 3000, interpolateColor: true, modeList: ['Color','White'], inSel_ChoiceState: true},
        <PageItem>{ id: 'alias.0.NSPanel_1.Luftreiniger', icon: 'power', icon2: 'power',offColor: MSRed, onColor: MSGreen}
    ]
};
```  
  
## CardEntities - Color Aliase 1
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/bc21c636-d12f-4a5b-8c75-ac1483fa5ead)
  
``` 
let Test_Licht1 = <PageEntities>
{
    'type': 'cardEntities',
    'heading': 'Color Aliase 1',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel_1.TestRGBLichteinzeln', name: 'RGB-Licht Hex-Color', interpolateColor: true},
        <PageItem>{ id: 'alias.0.NSPanel_1.TestRGBLicht', name: 'RGB-Licht', minValueBrightness: 0, maxValueBrightness: 100, interpolateColor: true},
        <PageItem>{ id: 'alias.0.NSPanel_1.TestCTmitHUE', name: 'HUE-Licht-CT', minValueBrightness: 0, maxValueBrightness: 70, minValueColorTemp: 500, maxValueColorTemp: 6500, interpolateColor: true},
        <PageItem>{ id: 'alias.0.NSPanel_1.TestHUELicht', name: 'HUE-Licht-Color', minValueColorTemp: 500, maxValueColorTemp: 6500, interpolateColor: true}
    ]
};
```  
  
## CardEntities 
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
``` 

```  
  
## CardEntities - Color Aliase 2
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/d5cb9173-042c-4ef1-89de-a84b3a646b3f)
  
``` 
let Test_Licht2 = <PageEntities>
{
    'type': 'cardEntities',
    'heading': 'Color Aliase 2',
    'useColor': true,
    'items': [
        //Beispiel für RGB Light mit neuem PageItem-Parameter colormode: "xy" alternativ colormode: "rgb" oder weglassen
        //Steuert im z.B. DeConz Adapter unter Lampen die Farben per CIE (XY)
        <PageItem>{ id: "alias.0.NSPanel_2.WZ_E14_Fenster_rechts", name: 'Fensterbank rechts', minValueBrightness: 0, maxValueBrightness: 100, minValueColorTemp: 500, maxValueColorTemp: 150, interpolateColor: true, colormode: 'xy'},
        <PageItem>{ id: "alias.0.NSPanel_1.TestFarbtemperatur", name: 'Farbtemperatur', interpolateColor: true},
        <PageItem>{ id: "alias.0.NSPanel_1.TestFarbtemperatur", prefixName: 'Büro: ', name: "getState('0_userdata.0.Test.Wiki_Router').val", suffixName: '%', interpolateColor: true},
    ]
};
```  
  
## CardEntities - Sonstige Aliase
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/09ddd04f-24af-40b4-9960-882576464c1f)
  
``` 
let Test_Funktionen = <PageEntities>
{
    'type': 'cardEntities',
    'heading': 'Sonstige Aliase',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel_1.TestLautstärke', offColor: MSRed, onColor: MSGreen, name: 'Echo Spot Büro', minValue: 0, maxValue: 100 },
        <PageItem>{ id: 'alias.0.NSPanel_1.TestTemperatur',name: 'Temperatur außen', icon: 'thermometer', onColor: White , colorScale: {'val_min': -20, 'val_max': 40, 'val_best': 20} },
        <PageItem>{ id: 'alias.0.NSPanel_1.TestFeuchtigkeit', name: 'Luftfeuchte außen', icon: 'water-percent', unit: '%H', onColor: White, colorScale: {'val_min': 0, 'val_max': 100, 'val_best': 65} },
        //<PageItem>{ id: 'alias.0.NSPanel_1.TestInfo', name: 'Windstärke', icon: 'wind-power-outline', offColor: MSRed, onColor: MSGreen, unit: 'bft', minValue: 0, maxValue: 12, interpolateColor: true, useColor: true },
        <PageItem>{ id: 'alias.0.NSPanel_1.Ventilator.Fan_1',name: 'Ventilator', icon: 'fan', onColor: On, offColor: HMIOff, modeList: ['Low', 'Medium', 'High', 'Move', 'Sleep', 'Auto', 'Manual']},
    ]
};
```  
  
## CardEntities - Diverses
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
``` 
let Buero_Seite_1 = <PageEntities>
{
    'type': 'cardEntities',
    'heading': 'Büro',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel_1.Schreibtischlampe', interpolateColor: true},
        <PageItem>{ id: 'alias.0.NSPanel_1.Deckenbeleuchtung', interpolateColor: true},
        <PageItem>{ id: 'alias.0.NSPanel_1.Testlampe2', name: 'Filamentlampe', minValueBrightness: 0, maxValueBrightness: 70, interpolateColor: true},
        <PageItem>{ id: 'alias.0.NSPanel_1.Luftreiniger', icon: 'power', icon2: 'power',offColor: MSRed, onColor: MSGreen}
    ]
};
```  
  
## CardEntities - Fenster und Türen
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/7893e23e-b9cc-437b-8690-48fb5813cca3)
  
``` 
let Fenster_1 = <PageEntities>
{
    'type': 'cardEntities',
    'heading': 'Fenster und Türen',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel_1.TestFenster', offColor: MSRed, onColor: MSGreen, name: 'Büro Fenster'},
        <PageItem>{ id: 'alias.0.NSPanel_1.Haustuer', offColor: MSRed, onColor: MSGreen, name: 'Haustür'},
        <PageItem>{ id: 'alias.0.NSPanel_1.TestBlind', icon: "blinds-horizontal", offColor: White, onColor: Yellow, name: 'Büro', secondRow: 'Hier Text für 2. Zeile'},
        <PageItem>{ id: 'alias.0.NSPanel_1.TestDoorlock', offColor: MSRed, onColor: MSGreen, name: 'Türschloss'},
    ]
};
```  
  
## CardEntities - Button Aliase
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
``` 
let Button_1 = <PageEntities>
{
    'type': 'cardEntities',
    'heading': 'Button Aliase',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel_1.TestTastensensor', name: 'Tastensensor (FFN)'},
        <PageItem>{ id: 'alias.0.NSPanel_1.Radio.NDR2', icon: 'radio', name: 'Taste (NDR2)', onColor: colorRadio, buttonText: 'starten'},
        <PageItem>{ id: 'alias.0.NSPanel_1.TestVentil1', icon: 'valve-open', icon2: 'valve-closed',offColor: MSRed, onColor: MSGreen, name: 'Test-Ventil 1'},
        <PageItem>{ id: 'alias.0.NSPanel_1.Radio.NDR2', icon: 'alarm-light', name: 'Alert mit Zielseite', offColor: MSGreen, onColor: MSRed, targetPage: 'Abfall', buttonText: 'Popup'},
    ]
};
```  
  
## CardEntities - Navigate für Subpages
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
``` 
let Subpages_1 = <PageEntities>
{
    'type': 'cardEntities',
    'heading': 'Test Subpages',
    'useColor': true,
    'items': [
        <PageItem>{ navigate: true, id: 'alias.0.NSPanel_1.Abfall.event1', targetPage: 'Abfall', name: 'Abfallkalender'},
        <PageItem>{ navigate: true, id: null, targetPage: 'WLAN', onColor: White, name: 'Gäste WLAN'},
    ]
};
```  
  
## CardEntities - Abfallkalender
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/124622d2-1b02-4ced-8045-62ba04c62c95)
  
``` 
let Abfall = <PageEntities>
{
	'type': 'cardEntities',
	'heading': 'Abfallkalender',
	'useColor': true,
	'subPage': true,
	'parent': Subpages_1,
	'items': [
		<PageItem>{ id: 'alias.0.NSPanel_1.Abfall.event1',icon: 'trash-can'},
		<PageItem>{ id: 'alias.0.NSPanel_1.Abfall.event2',icon: 'trash-can'},
		<PageItem>{ id: 'alias.0.NSPanel_1.Abfall.event3',icon: 'trash-can'},
		<PageItem>{ id: 'alias.0.NSPanel_1.Abfall.event4',icon: 'trash-can'}
	]
};
```  

</details>  
  
***  
  
<details>
  <summary>PageGrid(2)</summary> 
  
## CardGrid für Sensorwerte  
  
![](https://user-images.githubusercontent.com/102996011/216006611-32155c9c-84ba-48eb-8b07-2485d80eb99b.png)  
  
``` 
let SensorGrid = <PageGrid>{
    'type': 'cardGrid',
    'heading': 'Sensor Werte',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel_1.TestTemperatur', name: 'Außentemp. °C', offColor: MSRed, onColor: MSGreen, useValue: true, colorScale: {'val_min': -20, 'val_max': 40, 'val_best': 20} },
        <PageItem>{ id: 'alias.0.NSPanel_1.TestFeuchtigkeit', name: 'Luftfeuchte %', offColor: MSYellow, onColor: MSYellow , useValue: true, colorScale: {'val_min': 0, 'val_max': 100, 'val_best': 65} },
        <PageItem>{ id: 'alias.0.NSPanel_1.Taupunkt', name: 'Taupunkt °C', offColor: MSRed, onColor: MSGreen, useValue: true, colorScale: {'val_min': -20, 'val_max': 40, 'val_best': 20} },
        <PageItem>{ id: 'alias.0.NSPanel_1.UV_Index', name: 'UV Index', offColor: White , onColor: White, useValue: true, colorScale: {'val_min': 0, 'val_max': 12} },
        <PageItem>{ id: 'alias.0.NSPanel_1.Windstaerke', name: 'Windstärke bft', offColor: White , onColor: White, useValue: true, colorScale: {'val_min': 0, 'val_max': 9} },
        <PageItem>{ id: 'alias.0.NSPanel_1.Luftdruck', name: 'Luftdruck hPa', offColor: White , onColor: White, useValue: true, colorScale: {'val_min': 950, 'val_max': 1050, 'val_best': 1013} },
    ]};
```
  
## CardCrid2 - 8 statt 6 PageItems  
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
``` 
let Buero_Seite_2 = <PageGrid2>
{
    'type': 'cardGrid2',
    'heading': 'Büro 2',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel_1.Schreibtischlampe', name: 'Schreibtisch'},
        <PageItem>{ id: 'alias.0.NSPanel_1.Deckenbeleuchtung', name: 'Deckenlampe'},
        <PageItem>{ id: 'alias.0.NSPanel_1.TestFenster', offColor: MSRed, onColor: MSGreen, name: 'Büro Fenster'},
        <PageItem>{ id: 'alias.0.NSPanel_1.Luftreiniger', icon: 'power', offColor: MSRed, onColor: MSGreen},
        <PageItem>{ id: 'alias.0.NSPanel_1.TestBlind', icon: 'projector-screen', onColor: White, name: 'Beamer', secondRow: 'auch Text'},
        <PageItem>{ id: 'alias.0.NSPanel_1.Kippfenster', useValue: true },
        <PageItem>{ id: 'alias.0.NSPanel_1.Radio.Bob', icon: 'play', onColor: White, name: 'TuneIn'}
    ]
};
```  
  
## CardCrid2 - 8 statt 6 PageItems  
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/f1d2c2dd-01f6-4b68-a14e-0d774bcc49a7)
  
``` 
let Sensor_FontSize = <PageGrid2>
{
    'type': 'cardGrid2',
    'heading': 'Sensorwerte und FontSize',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel_1.TestTemperatur', name: 'Außentemp. °C', offColor: MSRed, onColor: MSGreen, useValue: true, fontSize: 0, colorScale: {'val_min': -20, 'val_max': 40, 'val_best': 20} },
        <PageItem>{ id: 'alias.0.NSPanel_1.TestFeuchtigkeit', name: 'Luftfeuchte %', offColor: MSYellow, onColor: MSYellow , useValue: true, fontSize: 1, colorScale: {'val_min': 0, 'val_max': 100, 'val_best': 65} },
        <PageItem>{ id: 'alias.0.NSPanel_1.Taupunkt', name: 'Taupunkt °C', offColor: MSRed, onColor: MSGreen, useValue: true, fontSize: 2, colorScale: {'val_min': -20, 'val_max': 40, 'val_best': 20} },
        <PageItem>{ id: 'alias.0.NSPanel_1.UV_Index', name: 'UV Index', offColor: White , onColor: White, useValue: true, fontSize: 3,colorScale: {'val_min': 0, 'val_max': 12} },
        <PageItem>{ id: 'alias.0.NSPanel_1.Windstaerke', name: 'Windstärke bft', offColor: White , onColor: White, useValue: true, fontSize: 4, colorScale: {'val_min': 0, 'val_max': 9} },
        <PageItem>{ id: 'alias.0.NSPanel_1.Luftdruck', name: 'Luftdruck hPa', offColor: White , onColor: White, useValue: true, colorScale: {'val_min': 950, 'val_max': 1050, 'val_best': 1013} },
    ]
};
``` 
  
## CardGrid - Radiosender
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
``` 
let Radiosender = <PageGrid>
{
    'type': 'cardGrid',
    'heading': 'Büro 2',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel_1.Radio.Bob', icon: 'radio', name: 'Radio BOB', onColor: colorRadio},
        <PageItem>{ id: 'alias.0.NSPanel_1.Countdown', icon: 'timer-outline', name: 'Timer', onColor: White}
    ]
};
```  
  
## CardGrid - WLED
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
``` 
let WLED = <PageGrid>
{
    'type': 'cardGrid',
    'heading': 'WLED Stripes WZ',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel_1.WLED.Example.On', name: 'Power', icon: 'power', onColor: HMIOn, offColor: HMIOff},
        <PageItem>{ id: 'alias.0.NSPanel_1.WLED.Example.Sync', name: 'Sync', icon: 'sync', onColor: HMIOn, offColor: White},
        <PageItem>{ id: 'alias.0.NSPanel_1.WLED.Example.Presets', icon: 'heart-outline', name: 'Presets', onColor: White, modeList: ['Preset 0', 'Add Preset']},
        <PageItem>{ id: 'alias.0.NSPanel_1.WLED.Example.Colors', icon: 'palette', name: 'Colors', onColor: White, 
                    modeList: ['Default', '* Color 1', '* Color Gradient', '* Colors 1&2', '* Colors Only', '* Random Cycle', 'Analogus','April Night', 'Aqua Flash', 'Atlantica', 'Aurora', 
                               'Beach', 'Beech', 'Blink Red', 'Breeze', 'C9', 'C9 New', 'Candy', 'Candy2', 'Cloud', 
                               'Cyane', 'Departure', 'Drywet', 'Fairy Reaf', 'Fire', 'Forest', 'etc'
                              ]},
        <PageItem>{ id: 'alias.0.NSPanel_1.WLED.Example.Effects', icon: 'emoticon-outline', name: 'Effects', onColor: White, 
                    modeList: ['Solid', 'Android', 'Aurora', 'Blends', 'Blink', 'Blink Rainbow', 'Bouncing Balls','Bpm', 'Breathe', 'Candle', 'Candle Multi', 
                               'Candy Cane', 'Chase', 'Chase 1', 'Chase 2', 'Chase 3', 'Chase Flash', 'Chase Flash Rnd', 'Chase Rainbow', 'Chase Random', 
                               'Chunchun', 'Colorful', 'Colorloop', 'Colortwinkles', 'Colorwaves', 'Dancing Shadows', 'etc'
                              ]},
        <PageItem>{ id: 'alias.0.NSPanel_1.WLED.Example.Segments', icon: 'layers', name: 'Segments', onColor: White, modeList: ['Segment 0', 'Add Segment']},
    ]
};
```  
</details>  
  
***
    
<details>
  <summary>PageMedia</summary> 
  
## CardMedia - Alexa
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/9f02d436-e2ce-4e28-956b-a521330e1747)

**Button-Menü:**  

SpeakerList:  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/33a8d3da-1624-4e87-9b5c-2b1fb1d86e1a)  
  
PlayList:  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/85174456-9a8e-43f1-bb1b-551714b4e7a7)  
  
Equalizer:  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/f5033d44-bf2f-4cb3-bf12-77b43b58623d)  

``` 
// NEW: Neue Definition von Medien-Aliasen
// adapterPlayerInstance = alexa2.0. or spotify-premium.0. or sonos.0. or chromecast.0.
let Alexa = <PageMedia> 
{
    'type': 'cardMedia',
    'heading': 'Alexa',
    'useColor': true,
    'items': [<PageItem>{   
                id: AliasPath + 'Media.PlayerAlexa', 
                adapterPlayerInstance: 'alexa2.0.',
                mediaDevice: 'G0XXXXXXXXXXXXXX', 
                speakerList: ['Überall','Gartenhaus','Esszimmer','Heimkino','Echo Dot Küche','Echo Spot Buero'],
                //analog alexa2 Music-Provider
                playList: ['Spotify-Playlist.PartyPlaylist',
                           'Amazon-Music-Playlist.Mein Discovery Mix',
                           'My-Library-Playlist.2020',
                           'My-Library-Playlist.2021',
                           'TuneIn.Radio Bob Rock',
                           'TuneIn.NDR2',
                           'Spotify-Playlist.Sabaton Radio',
                           'Spotify-Playlist.Rock Party',
                           'Spotify-Playlist.This Is Nightwish',
                           'Spotify-Playlist.Metal Christmas'],
                equalizerList: ['Bassboost','Klassik','Dance', 'Deep', 'Electronic', 'Flat', 'Hip-Hop', 'Rock', 
                                'Metal', 'Jazz', 'Latin', 'Tonstärke', 'Lounge', 'Piano'],
                colorMediaIcon: colorAlexa,
                colorMediaArtist: Yellow,
                colorMediaTitle: Yellow,
                autoCreateALias : true
             }]
};
```  
  
## CardMedia - Sonos
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
``` 
let Sonos = <PageMedia>
{
    'type': 'cardMedia',
    'heading': 'Sonos',
    'useColor': true,
    'items': [<PageItem>{   
                id: AliasPath + 'Media.PlayerSonos', 
                adapterPlayerInstance: 'sonos.0.',
                mediaDevice: '192_168_1_212',
                speakerList: ['Terrasse'],
                colorMediaIcon: colorSpotify,
                colorMediaArtist: Yellow,
                colorMediaTitle: Yellow,
                autoCreateALias : true
             }]
};
```  
  
## CardMedia - Spotify-Premium
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/3154c022-c5c5-4640-8b6f-e9826b289edf)
  
**Button-Menü**
  
SpeakerList  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/e599d18b-1387-4839-bdec-5499475f02ff)  
  
PlayList  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/a254be7a-510a-47e7-b405-07ba54745473)  
  
TrackList  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/c1d67362-570f-4235-9778-3bac3d492796)  
  
Equalizer  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/3ccb9714-fd0c-4162-b595-3761c27f99bf)  
  

``` 
let SpotifyPremium = <PageMedia>
{
    'type': 'cardMedia',
    'heading': 'Spotify-Premium',
    'useColor': true,
    'items': [<PageItem>{ 
                id: AliasPath + 'Media.PlayerSpotifyPremium', 
                adapterPlayerInstance: "spotify-premium.0.",
                speakerList: ['LENOVO-W11-01', 'Terrasse','Überall','Gartenhaus','Esszimmer','Heimkino','Echo Dot Küche',
                              'Echo Spot Buero'],
                playList: ['PartyPlaylist','Sabaton Radio','Rock Party','This Is Nightwish','Metal Christmas'],
                repeatList: ['off','context','track'],
                equalizerList: ['Bassboost','Klassik','Dance', 'Deep', 'Electronic', 'Flat', 'Hip-Hop', 'Rock', 
                                'Metal', 'Jazz', 'Latin', 'Tonstärke', 'Lounge', 'Piano'],
                colorMediaIcon: colorSpotify,
                colorMediaArtist: Yellow,
                colorMediaTitle: Yellow,
                autoCreateALias : true
             }]
};
```  
  
## CardMedia - SqueezeboxRPC
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
``` 
let SqueezeboxRPC = <PageMedia>
{
    'type': 'cardMedia',
    'heading': 'SqueezeboxRPC',
    'useColor': true,
    'items': [<PageItem>{ 
                id: 'alias.0.Media.LMS', 
                adapterPlayerInstance: 'squeezeboxrpc.0',
                speakerList: ['SqueezePlay'],
                mediaDevice: 'SqueezePlay',
                playList: ['Playlist'],
                autoCreateALias : true
             }]
};
```

## CardMedia - Volumio
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/3b72ecfa-07ef-42e4-88b7-b5846a6a91a2)
  
```
let VolumioBoss: PageMedia = 
{
    'type': 'cardMedia',
    'heading': 'Volumio-Büro',
    'useColor': true,
    'subPage': false,
    'parent': undefined,
    'prev': undefined,
    'next': undefined,
    'home': undefined,
    'items': [<PageItem>{   
                id: 'alias.0.NSPanel.Volumio-Boss', 
                adapterPlayerInstance: 'volumio.0.',
                speakerList: [], /* this must, no function */
                playList: [],    /* empty for dynamic reading */
                colorMediaIcon: colorSpotify,
                colorMediaTitle: colorSpotify,
                colorMediaArtist: Yellow,
                autoCreateALias : true
             }]
};
```

```
let VolumioMobil: PageMedia = 
{
    'type': 'cardMedia',
    'heading': 'Volumio-Mobil',
    'useColor': true,
    'subPage': false,
    'parent': undefined,
    'prev': undefined,
    'next': undefined,
    'home': undefined,
    'items': [<PageItem>{   
                id: 'alias.0.NSPanel.Volumio-Mobil', 
                adapterPlayerInstance: 'volumio.1.',
                speakerList: [], /* this must, no function */
                playList: [],    /* empty for dynamic reading */
                colorMediaIcon: Yellow,
                colorMediaTitle: Yellow,
                colorMediaArtist: Gray,
                autoCreateALias : true
             }]
};
```
  
</details>  
  
***  
  
<details>
  <summary>PageThermo</summary> 
  
## CardThermo - Thermostat
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/a7426ca1-600b-456e-a8a4-11f6b5c6fb11)
  
``` 
let Buero_Themostat = <PageThermo>
{
    'type': 'cardThermo',
    'heading': 'Test Thermostat',
    'useColor': true,
    'items': [<PageItem>{ 
                id: 'alias.0.NSPanel_1.Thermostat_Buero', 
                minValue: 50, 
                maxValue: 300,
                stepValue: 5
             }]
};
```  
  
## CardThermo - Klimaanlage
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/2c5b634d-eef4-4333-8a9e-9264c1b10a21)  

oder 

![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/aeacd803-4114-441f-9882-2c1714b42d13)  

popupThermo:  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/775e6fee-e06a-4a1c-8f9d-695a8624da86)

``` 
let Buero_Klimaanlage = <PageThermo>
{
    'type': 'cardThermo',
    'heading': 'Test Klimaanlage',
    'useColor': true,
    'items': [<PageItem>{   
                id: 'alias.0.NSPanel_1.TestKlimaanlage', 
                minValue: 50, 
                maxValue: 250,
                stepValue: 5,
                iconArray: ['power-standby','air-conditioner','snowflake','fire','alpha-e-circle-outline','fan','water-percent','swap-vertical-bold'],
                popupThermoMode1: ['Auto','0','1','2','3'],
                popupThermoMode2: ['Auto','0','1','2','3','4','5'],
                popupThermoMode3: ['Auto','Manual','Boost',],
                popUpThermoName: ['Schwenk-Modus', 'Speed', 'Temperatur'],
                icon: 'fan',
                setThermoAlias: ['MODE1','MODE2','MODE3'],
                //setThermoDestTemp2: 'ACTUAL2'
             }]
};
```  
  
## CardThermo - Wärmepumpe
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/69e577bd-e56d-4411-9af0-a0dd19ba030f)
  
``` 
let Pool_Waermepumpe = <PageThermo>
{
    'type': 'cardThermo',
    'heading': 'Pool Wärmepumpe',
    'useColor': true,
    'items': [<PageItem>{   
                id: 'alias.0.NSPanel_1.Pool_Waermepumpe', 
                minValue: 100, 
                maxValue: 300,
                stepValue: 5,
                iconArray: ['power-standby','alpha-a-circle-outline','snowflake','fire'],
                //iconArray: ['power-standby','air-conditioner','snowflake','fire','alpha-e-circle-outline','fan','water-percent','swap-vertical-bold'],
             }]
};
```  
</details>  
  
***
    
<details>
  <summary>PageAlarm & PageUnlock</summary> 
  
## CardAlarm
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/8e8e353c-ca6a-43d3-85b2-ff6532283e2c)
  
``` 
let Buero_Alarm = <PageAlarm>
{
    'type': 'cardAlarm',
    'heading': 'Alarmanlage',
    'useColor': true,
    'items': [<PageItem>{ id: 'alias.0.Alarm' }]
};
```  
  
## CardUnlock
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/8f18098b-96e5-4e88-a86d-4824cc2b6299)
  
``` 
let Unlock_Service = <PageUnlock>
{
    'type': 'cardUnlock',
    'heading': 'Service Pages',
    'useColor': true,
    'items': [<PageItem>{ id: 'alias.0.Unlock', targetPage: 'NSPanel_Service' }]
};
```  
</details>  
  
***  
  
<details>
  <summary>PageChart & Power</summary> 
  
## CardChart
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/274f5742-f491-4522-ac6f-7db3661dd5e2)
  
``` 
let CardChartExample = <PageChart>
{
    'type': 'cardChart',
    'heading': 'Stromzähler L1+L2+L3',
    'useColor': true,
    'items': [<PageItem>{ 
                id: 'alias.0.NSPanel_1.cardChart', 
                yAxis: 'Leistung [kW]', 
                yAxisTicks: [2,4,6,8,10,2,4,6,8,20,2], 
                onColor: Yellow
             }]
};
```  
  
## CardLChart
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/7c99fa26-9383-45f7-a913-48ea23fb0baf)
  
``` 
let CardLChartExample = <PageChart>
{
    'type': 'cardLChart',
    'heading': 'Büro Temperatur',
    'useColor': true,
    'items': [<PageItem>{ 
                id: 'alias.0.Haus.Erdgeschoss.Buero.Charts.Temperatur',
                yAxis: 'Temperatur [°C]',
                yAxisTicks: [-250, -200, -150, -100,-50, 0, 50, 100, 150, 200, 250, 300],
                onColor: Yellow
             }]
};
```  
  
  
## CardPower
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/e4a4a619-4069-4c64-8c34-20511edc750d)
  
``` 
let CardPowerExample = <PagePower>
{
    'type': 'cardPower',
    'heading': 'cardPower Emulator',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel_1.Power.PowerCard' },
//      <PageItem>{ }  // aktivieren für Demomodus der PowerCard, dafür ersten PageItem auskommentieren
    ]
};
```  
</details>  
  
***  
  
<details>
  <summary>PageQR</summary> 
  
## CardQR
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/b855ff4a-fcf9-4c67-a45e-822cd9487437)
  
``` 
let WLAN = <PageQR> 
{
     'type': 'cardQR',
     'heading': 'Gäste WLAN',
     'useColor': true,
     'subPage': true,
     'parent': Subpages_1,
     'items': [<PageItem>{ id: 'alias.0.NSPanel_1.Guest_Wifi', hidePassword: false }]
};
```  
</details>  
  
***

