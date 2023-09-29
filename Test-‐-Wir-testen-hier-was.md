Auf dieser Seite testen wir was für die zukünftige Wiki

# Einleitung
  
  
  
# Geblubber


# **Index**  
  
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
  
  
***
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
  
* let name = : Das Wort name ist hier ein Platzhalter. Man gibt der Seite hier einen eindeutigen Namen, allerdings bitte ohne Leerzeichen bei mehreren Worten und vermeide Sonderzeichen. Dieser Name muss im weiteren Verlauf des Skriptes noch einmal aufgeführt werden (Wichtig für die Darstellung und Navigation)  
* <PageType> : Type muss durch den richtigen Seiten Typ (Entities, Chart, Power, Grid, etc.) ersetzt werden. Page davor bleibt bestehen, so dass man dann zum Beispiel ein <PageEntities> oder <PageGrid> erhält. Wichtig, PageType ist immer von einer Spitzen Klammer eingefasst.  
* type : Der Typ der Seite, wie zuvor schon beschrieben. PageType und type haben immer den gleichen Postfix. Bei type ist es aber CardType stattPageType. Folglich haben wir hier in Hochkomma eingefasst 'cardEntities' oder 'cardGrid', etc.  

***  
  
  
# Page Beispiele  
  
<details>
  <summary>PageEntities</summary> 
  
## CardEntities 
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
``` 
let button2Page = <PageEntities>
{
    'type': 'cardEntities',
    'heading': 'Büro',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel_1.Schreibtischlampe'},
        <PageItem>{ id: 'alias.0.NSPanel_1.Deckenbeleuchtung'}
    ]
};
```  
  
## CardEntities - Color Aliase 1
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
## CardCrid - WLED
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
</details>  
  
***  
  
<details>
  <summary>PageThermo</summary> 
  
## CardThermo - Thermostat
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
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

