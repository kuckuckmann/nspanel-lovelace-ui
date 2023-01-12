# cardEntities
![image](https://user-images.githubusercontent.com/102996011/190120141-13da0024-261d-4cd9-a104-13416c224004.png)  

4 vertikal angeordnete Steuerelemente (Erstellung der "PageItem" siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen))  

```
var Sprechender_eindeutiger_Seitenname: PageEntities =
{
    "type": "cardEntities",
    "heading": "Deine Überschrift",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [
        <PageItem>{ id: "Dein_Erstellter_Alias_1", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_2", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_3", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_4", Weitere Parameter siehe Alias Definition }
    ]
};
```


# cardGrid
![image](https://user-images.githubusercontent.com/102996011/190120023-c9e0477c-0d06-4484-af27-be2f6fe810d3.png)

6 horizontal angeordnete Steuerelemente (in 2 Reihen je 3 Steuerelemente) (Erstellung der "PageItem" siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen))  

```
var Sprechender_eindeutiger_Seitenname: PageGrid =
{
    "type": "cardGrid",
    "heading": "Deine Überschrift",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [
        <PageItem>{ id: "Dein_Erstellter_Alias_1", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_2", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_3", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_4", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_5", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_6", Weitere Parameter siehe Alias Definition }
    ]
};
```

# cardAlarm
![image](https://user-images.githubusercontent.com/102996011/190120272-82c6b418-c9dc-4338-a0a3-53da8bec0bac.png)

(Erstellung des alias.0.Alarm siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen))  

```
var Sprechender_eindeutiger_Seitenname: PageAlarm =
{
    "type": "cardAlarm",
    "heading": "Deine Überschrift",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [
        <PageItem>{ id: alias.0.Alarm}
    ]
};
```
# cardMedia v2.0 (ab Release v3.7.0)
![image](https://user-images.githubusercontent.com/102996011/209344233-c7d700c4-eb87-4c51-9441-b51368c88096.png)

**Neue Elemente**
* Shuffle (nach verfügbarkeit des Adapters)  
  ![image](https://user-images.githubusercontent.com/102996011/209348879-59575912-b9c6-452f-885c-0cbb2791f750.png)

* Neue Auswahl für Speakerauswahl/-wechsel  
  ![image](https://user-images.githubusercontent.com/102996011/209346590-f265353e-a35a-42d4-9d1f-48426e47eb44.png)

* Playlist  
  ![image](https://user-images.githubusercontent.com/102996011/209347004-5d20ac06-b5c2-472e-aeb8-4e9bbb0082e9.png)

* Tracklist (Bei Playlist und falls verfügbar)  
  ![image](https://user-images.githubusercontent.com/102996011/209347405-f33dbd6d-ce7d-4dba-9744-73835f7c1c81.png)

* Equalizer-Profile  
  ![image](https://user-images.githubusercontent.com/102996011/209347576-809eaabe-c853-476f-82f8-6536694ba404.png)  
  [Link: Blockly für Klangsteuerung in der cardMedia](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#12-equalizer-f%C3%BCr-cardmedia)

* Repeat (nach Verfügbarkeit des Adapters)  
  ![image](https://user-images.githubusercontent.com/102996011/209348242-264737e4-7b31-488e-a4db-10e0f6bd6e08.png)

(Erstellung des "PageItem" siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen))   

> **Definition ab TS-Version 3.7.0** (Breaking Changes)  

**alexa2-Adapter**
```
let Alexa: PageMedia = 
{
    'type': 'cardMedia',
    'heading': 'Alexa',
    'useColor': true,
    'subPage': false,
    'parent': undefined,
    'items': [<PageItem>{   
                id: AliasPath + 'Media.PlayerAlexa', 
                adapterPlayerInstance: 'alexa2.0.',
                mediaDevice: 'G0XXXXXXXXXXXXXX', // Eigene Seriennummer des primären Device einstellen
                speakerList: ['Überall','Gartenhaus','Esszimmer','Heimkino','Echo Dot Küche','Echo Spot Buero'],
                //analog alexa2 Music-Provider
                //Mögliche Playlists:
                playList: ['Spotify-Playlist.Party Playlist',
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

**spotify-premium Adapter**
```
let SpotifyPremium: PageMedia = 
{
    "type": "cardMedia",
    "heading": "Spotify-Premium",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{ 
                id: AliasPath + 'Media.PlayerSpotifyPremium', 
                adapterPlayerInstance: "spotify-premium.0.",
                speakerList: ['LENOVO-W11-01','Terrasse','Überall','Gartenhaus','Esszimmer','Heimkino','Echo Dot Küche',
                              'Echo Spot Buero'],
                //Favoriten Playlists aus Spotify in Liste eintragen 
                playList: ['Party Playlist','Sabaton Radio','Rock Party','This Is Nightwish','Metal Christmas'],
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
**Volumio-Player**  
  
```
let VolumioBoss: PageMedia = 
{
    'type': 'cardMedia',
    'heading': 'Volumio-Büro',
    'useColor': true,
    'subPage': false,
    'parent': undefined,
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
  
# cardMedia v1.0 (bis Release v3.6.0)
![image](https://user-images.githubusercontent.com/102996011/204136831-afe5bde8-5046-495b-8ea7-68bc91e3a57c.png)  

(Erstellung des "PageItem" siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen))  

> **Definition ab TS-Version 3.1.1.3** (Breaking Changes)
```
var Sprechender_eindeutiger_Seitenname: PageMedia = 
{
    "type": "cardMedia",
    "heading": "Deine Überschrift",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{   
                id: "alias.0.NSPanel_X.Media.PlayerAlexa", 
                adapterPlayerInstance: "alexa2.0.",
                mediaDevice: "G0XXXXXXXXXXXXXXXX", 
                speakerList: ['Überall','Gartenhaus','Esszimmer','Heimkino','Echo Dot Küche','Echo Spot Buero']
             }]
};
```  
oder
```  
let SpotifyPremium: PageMedia = 
{
    "type": "cardMedia",
    "heading": "Spotify-Premium",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{ 
                id: AliasPath + 'Media.PlayerSpotifyPremium', 
                adapterPlayerInstance: "spotify-premium.0.",
                speakerList: ['LENOVO-W11-JB','Terrasse','Überall','Gartenhaus','Esszimmer','Heimkino','Echo Dot Küche','Echo Spot Buero'],
                colorMediaIcon: colorSpotify,
                colorMediaArtist: Yellow,
                colorMediaTitle: Yellow,
                autoCreateALias : true
             }] 
};
```  

### Parameter  
  
**adapterPlayerInstance:** "alexa.0." oder "spotify-premium.0." oder "sonos.0." oder "chromecast.0." oder "squeezeboxrpc.0.Players.DeinPlayer. 
  
**mediaDevice:**
* für "alexa.0.": Seriennummer oder Gruppennummer des primären Alexa-Device
* für "sonos.0.": IP-Adresse des Sonsos primären Sonos-Device (getrennt mit "_") --> Beispiel: 192_168_1_250  
* für "spotify-premium.0.": Zeile kann gelöscht werden, da Spotify immer nur einen Speaker oder Gruppe steuern kann (automatische Ermittlung)
* für "chromecast.0.": Zeile kann gelöscht werden, da GoogleHome keine Funktionalitäten zum Wechseln von Lautsprechern zur Verfügung stellt 
* für "squeezeboxrpc.0.": Zeile kann gelöscht werden, da squeezeboxrpc keine Funktionalitäten zum Wechseln von Lautsprechern zur Verfügung stellt  

**speakerList:** (Namen und Reihenfolge der Speaker selbst bestimmen)
* für "alexa.0.": Device-Namen aus alexa2 möglich. Wenn leer [] , dann alle Devices des alexa2-Adapter 
* für "sonos.0.": Zeile kann gelöscht werden, da Funktionalität zum schieben auf andere Devices im Sonos-Adapter nicht möglich  
* für "spotify-premium.0.": Alle SmartDevice-Namen aus Spotify möglich (Im Gegensatz zu Alexa auch Smartphones und Rechner)
* für "chromecast.0.": Zeile kann gelöscht werden, da GoogleHome keine Funktionalitäten zum Wechseln von Lautsprechern zur Verfügung stellt 
* für "squeezeboxrpc.0.": "Bekannte Player unter Players (aktuell keine Funktion)

> **Definition bis TS-Version 3.1.1.3**
```
var Sprechender_eindeutiger_Seitenname: PageMedia = 
{
    "type": "cardMedia",
    "heading": "Deine Überschrift",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{ id: "alias.0.NSPanel_X.Media.PlayerAlexa" }]
};
```

# cardQR
![image](https://user-images.githubusercontent.com/102996011/190121115-436dc34d-3a89-4809-a3c6-2c6132938fd1.png)

> Beispiel: Erstellung des "PageItem" und Alias vom Typ "Info" siehe (https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#5-qr-code-page) by Kuckuckmann
```
var Sprechender_eindeutiger_Seitenname: PageQR = 
{
    "type": "cardQR",
    "heading": "Deine Überschrift",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{ id: "alias.0.NSPanel_1.Guest_Wifi" }] // Beispiel
};
```  
  
**Parameter:**  
keine

# cardThermo  
  
(Erstellung der "PageItem" siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen)) 
  
> Für Thermostat und Klimaanlage (Unterschied im zu erstellenden Alias)

![image](https://user-images.githubusercontent.com/102996011/204626750-bbeffe48-c9cd-44bf-8dfd-b90c6c3b7422.png)  
  

![image](https://user-images.githubusercontent.com/102996011/204623942-ca5a1e74-23f7-4b10-a65a-d2397ab67c72.png)  
  
![image](https://user-images.githubusercontent.com/102996011/204626323-a5df2e57-378f-4939-8a45-1a83277e23a2.png)  
  
![image](https://user-images.githubusercontent.com/102996011/204627014-03173d87-22ba-44fb-b07c-40b7be6366ac.png)  
  
```  
var Sprechender_eindeutiger_Seitenname: PageThermo = 
{
    "type": "cardThermo",
    "heading": "Test Klimaanlage",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{   
                id: "alias.0.NSPanel_1.TestKlimaanlage", 
                minValue: 50, 
                maxValue: 250,
                popupThermoMode1: ['Auto','0','1','2','3'],
                popupThermoMode2: ['Auto','0','1','2','3','4','5'],
                popupThermoMode3: ['Auto','Manual','Boost',],
                popUpThermoName: ["Schwenk-Modus", 'Speed', 'Temperatur'],
                icon: 'fan',
                setThermoAlias: ['MODE1','MODE2','MODE3'],
                setThermoDestTemp2: 'ACTUAL2'
             }]
};
```  

**Parameter:**  
minValue: Minimale einzustellende Temperatur (Beispiel: 17°C entspricht 170)  
maxValue: Maximale einzustellende Temperatur (Beispiel: 30,5°C entspricht 305)  

# cardPower (ab TS-Script v.3.4.1) 
  
![Nextion_Editor_9AYbpowjZS](https://user-images.githubusercontent.com/102996011/194641145-660e1218-f559-4f25-83ca-984cc677e0d8.gif)  

Beispiel: Erstellung des "PageItem" und Alias vom Typ "Info"

```  
var CardPowerExample: PagePower =
{
    "type": "cardPower",
    "heading": "cardPower Emulator",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [
        <PageItem>{ id: "alias.0.NSPanel_1.Power.PowerCard" },
    ]
};
```  


**Parameter:**  
Es gibt nur einen einzigen externen Datenpunkt (anzulegen in **0_userdata.0.**), auf den ein Alias vom Typ "**Info**" zugreift. Dieser muss mit einem JSON-Objekt in nachfolgender Struktur befüllt werden. Der Alias-Datenpunkt "**ACTUAL**" sollte hierbei auf diesen neuen Datenpunkt in "**0_userdata.0.**) gebunden sein.  
  
```  
[
  {
    "id": 0,
    "value": 13,
    "unit": "kW",
    "icon": "emoticon-happy-outline",
    "iconColor": 0
  },
  {
    "id": 1,
    "value": 3,
    "unit": "kW",
    "direction": "in",
    "icon": "battery-charging-60",
    "iconColor": 10,
    "speed": -3
  },
  {
    "id": 2,
    "value": 4.7,
    "unit": "kW",
    "direction": "in",
    "icon": "solar-power-variant",
    "iconColor": 3,
    "speed": 2
  },
  {
    "id": 3,
    "value": 4.3,
    "unit": "kW",
    "direction": "in",
    "icon": "wind-turbine",
    "iconColor": 1,
    "speed": 3
  },
  {
    "id": 4,
    "value": 3.4,
    "unit": "kW",
    "direction": "in",
    "icon": "shape",
    "iconColor": 10,
    "speed": 3
  },
  {
    "id": 5,
    "value": 0.1,
    "unit": "kW",
    "direction": "in",
    "icon": "transmission-tower",
    "iconColor": 0,
    "speed": 2
  },
  {
    "id": 6,
    "value": 2.5,
    "unit": "kW",
    "direction": "in",
    "icon": "car",
    "iconColor": 5,
    "speed": 2
  }
]
```  

**cardPower Emulator (Blockly)**  

[Zum Blockly](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/CardPower_Emulator_Skript.xml) 

**Kurze Anleitung:**  
Der Code dient nur der Orientierung und stellt keine Lösung für die eigene Visualisierung dar. Somit soll z.B. der Aufbau des JSON-Objektes verdeutlicht werden.

Für dieses Beispiel sind in 0_userdata für die 6 Werte in der cardPower entsprechende Datenpunkte (number) manuell angelegt worden:  
![image](https://user-images.githubusercontent.com/102996011/194373014-3dfc240c-ce7a-42ca-8d95-925b0a01b19f.png)  

Im oberen Teil des Blocklys wird lediglich eine Emulation auf 4 von 6 Datenpunkten je Minute erzeugt. Bei Produktivnutzung sollte dieses Codeobjekt gelöscht (deaktiviert) werden.

![image](https://user-images.githubusercontent.com/102996011/194373795-e3d5e889-10fd-48e6-8a51-cc56c9eadc35.png)

**Produktivnutzung:**  

Die Datenpunkte zu den entsprechenden Piktogrammen (id's) sollten mit den jeweiligen eigenen Adapter-Datenpunkten ersetzt werden. Im Beispiel werden folgende Datenpunkte zugewiesen:

1 - Batteriespeicher (Einspeisung/Bezug)  
2 - Photovoltaik Ertrag  
3 - Windenergieanlage Ertrag  
4 - Sämtliche aktiven Verbraucher des Hauses  
5 - Energielieferant (Netz-Einspeisung/Netz-Bezug)  
6 - Ladestation Verbrauch (E-Car)  
  
Für eine abweichende Darstellung ist das JSON entsprechend zu befüllen. Wenn eine Entität nicht visualisiert werden soll, so sollte in allen Werten zur id ein leerer String **""** übergeben werden. Beispiel:

```
  {
    "id": 3,
    "value": "",
    "unit": "",
    "direction": "",
    "icon": "",
    "iconColor": "",
    "speed": ""
  },
```

> Das Skript stellt nur eine exemplarische Möglichkeit der Befüllung dar. Es kann frei definiert und auf eigene Bedürfnisse angepasst werden, soll aber keine finale Lösung für jede Smart Home Situation abbilden!
> Ebenso kann die Erstellung des JSON natürlich auch über JavaScript oder TypeScript erfolgen.

# cardChart (ab TS-Script v.3.7.0)  

> ab Release v3.7.0

![image](https://user-images.githubusercontent.com/102996011/204631969-dfd8b8e9-09d0-45c2-a243-5e047f09ab05.png)  
   
> Für das unten abgebildete Blockly-Script wurden die Werte eines Datenpunktes "sonoff.0.DZG_DWSB20_2H.DZG_Leistung_Aktuell" in einer Influx 2.0 Datenbank gespeichert.  

Es wird für das Skript ein Datenpunkt (hier im Beispiel "0_userdata.0.Test.cardChart.txt") benötigt, um das Chart für die cardChart aufzubereiten.

**Alias-Erstellung:**  
Es wird lediglich ein Alias vom Gerätetyp "Info" benötigt:
![image](https://user-images.githubusercontent.com/102996011/209008594-36da27fb-cde2-4964-bcd8-3b406f4656cb.png)

**PageItem Beispiel:**
```
let CardChartExample: PageChart =
{
    "type": "cardChart",
    "heading": "Stromzähler L1+L2+L3",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{ 
                id: 'alias.0.NSPanel_1.cardChart', 
                yAxis: 'Leistung [kW]', 
                yAxisTicks: [2,4,6,8,10,2,4,6,8,20,2], 
                onColor: Yellow
             }]
};
```  

![image](https://user-images.githubusercontent.com/102996011/209009144-1b82e7df-1a58-412a-a304-14a5cf987a4c.png)  

**Blockly für Influx 2.0**
![image](https://user-images.githubusercontent.com/102996011/209006326-c8036709-2235-4ef8-aa14-00798e09fce7.png)  

[Zum Blockly](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/CardChart.xml)

**Javascript für History Adapter**
```
var sourceDP = 'alias.0.Wohnzimmer.Heizung.ACTUAL';
var targetDP = '0_userdata.0.Test.chartTest';
var rangeHours = 24;
var maxXAchsisTicks = 6;
var historyInstance = 'history.0';

on({id: sourceDP, change: "any"}, async function (obj) {
    sendTo(historyInstance, 'getHistory', {
        id: sourceDP,
        options: {
            start:     Date.now() - (60 * 60 * 1000 * rangeHours),
            end:       Date.now(),
            count:     rangeHours,
            limit:     rangeHours,
            aggregate: 'average'
        }
    }, function (result) {
        var cardChartString = "";
        var stepXAchsis = rangeHours / maxXAchsisTicks;

        for (var i = 0; i < rangeHours; i++){
            var deltaHour = rangeHours - i;
            var targetDate = new Date(Date.now() - (deltaHour * 60 * 60 * 1000));

            //Check history items for requested hours
            for (var j = 0, targetValue = 0; j < result.result.length; j++) {
                var valueDate = new Date(result.result[j].ts);
                var value = (Math.round(result.result[j].val * 10) / 10);

                if (valueDate > targetDate){                        
                    if ((targetDate.getHours() % stepXAchsis) == 0){
                        cardChartString += targetValue + '^' + targetDate.getHours() + ':00' + '~';
                    } else {
                        cardChartString += targetValue + '~';
                    }
                    break;
                } else {
                    targetValue = value;
                }
            }
        }
        
        cardChartString = cardChartString.substring(0,cardChartString.length-1);
        if (existsState(targetDP) == false ) { 
            createState(targetDP, cardChartString, true, { type: 'string' });
        } else {
            setState(targetDP, cardChartString, true);
        }
    });    
});
```  

# cardLChart (Line Charts ab TS-Script v.3.8.4)  

> ab Release v3.8.4 - Beschreibung folgt  

![image](https://user-images.githubusercontent.com/102996011/212094993-b78f6a38-aab7-43fd-a6c7-fa4add274b75.png)  

**Seitendefinition**

> Der Alias unter der PageItem.id ist ein Alias vom Gerätetyp: Info

``` 
let CardLChartExample = <PageChart>
{
    "type": "cardLChart",
    "heading": "Büro Temperatur",
    "useColor": true,
    'items': [<PageItem>{ 
                id: 'alias.0.Haus.Erdgeschoss.Buero.Charts.Temperatur',
                yAxis: 'Temperatur [°C]',
                yAxisTicks: [160,170,180,190,200,210,220,230],
                onColor: Yellow
             }]
};
```  

Erklärung zum nachfolgenden Beispiel-JS-Script:

> **Wichtiger Hinweis und Voraussetzungen:**  
>Für das Beispiel muss der InfluxDB Adapter installiert sein. Ebenfalls sollte über einen Zeitraum X bereits Sensordaten an eine Infux 2.X DB übertragen worden sein, welche jetzt zum Abruf bereit stehen!

Zu definieren ist der Pfad für den Datenpunkt (im Beispiel 0.userdata.0.NSPanel.Influx2NSPanel.buero_temperature) in den das u.a. JS-Script die aufbereiteten Daten für das NSPanel schreiben kann. Für das Beispiel wurde ein Datenpunkt (deconz.0.Sensors.65.temperature) aus dem DeConz-Adapter mit einem Zigbee-Temperatursensor gewählt.

**Bei Bedarf kann das Query angepasst werden:**
Es ist darauf zu achten, die Anzahl an Werten aus der Datenbank möglichst gering zu halten. Im nachfolgenden Beispiel wurden diese nochmals aggregiert. Die Summe an Zeichen für das Payload an die HMI des NSPanels ist begrenzt. Falls zu viele Werte verarbeitet werden, wird der Payload von der HMI gekürzt und die folge wäre eine schwarze Seite resultierend aus einem Fehlerzustand.

**Javascript für Influx2**
```  
const Debug = false;  //Bei Bedarf auf true stellen, um der Datenverarbeitung zur folgen 

const NSPanel_Path = '0_userdata.0.NSPanel.'
const Path = NSPanel_Path + "Influx2NSPanel.cardLChart.";
const PathSensor = Path + "buero_temperature";

const Sensor = 'deconz.0.Sensors.65.temperature'    //Datenpunkt, der gespeicherte Daten in der Influx 2.X enthält

const numberOfHoursAgo = 24;   // Zeitraum in Stunden in dem die Daten visualisiert werden
const xAxisTicksEveryM = 60;   // Striche der Skala an der X-Achse (In diesem Fall alle 60 Minuten)
const xAxisLabelEveryM = 240;  // Uhrzeit-Label der x-Achse (In diesem Fall alle 4 Stunden = 240 Minuten)

const InfluxInstance = 'influxdb.0'  //Die Instanz des InfluxDB-Adapters

let coordinates = ''; 

createState(PathSensor, 0, {
        name: 'SensorGrid',
        desc: 'Sensor Values [~<time>:<value>]*',
        type: 'string',
        role: 'value',
    });

on({ id: Sensor, change: 'any' }, async function (obj) {

    let query =[
        'from(bucket: "iobroker")',
        '|> range(start: -' + numberOfHoursAgo + 'h)',
        '|> filter(fn: (r) => r["_measurement"] == "' + Sensor + '")',
        '|> filter(fn: (r) => r["_field"] == "value")',
        '|> drop(columns: ["from", "ack", "q"])',
        '|> aggregateWindow(every: 1h, fn: last, createEmpty: false)',
        '|> map(fn: (r) => ({ r with _rtime: int(v: r._time) - int(v: r._start)}))',
        '|> yield(name: "_result")'].join('');

    if (Debug) console.log('Query: ' + query);

    sendTo(InfluxInstance, 'query', query, function (result) {
        if (result.error) {
            console.error(result.error);
        } else {
            // show result
            if (Debug) console.log(result);
            var numResults = result.result.length;
            for (var r = 0; r < numResults; r++) 
            {
                let list = []
                var numValues = result.result[r].length;

                for (var i = 0; i < numValues; i++) 
                {
                    var time = Math.round(result.result[r][i]._rtime/1000/1000/1000/60)
                    var value = Math.round(result.result[r][i]._value * 10)
                    list.push(time + ":" + value)
                }

                coordinates = list.join("~");

                if (Debug) console.log(coordinates);
            }
        }
    });

    let timeOut = setTimeout (
        function () {
                let ticksAndLabelsList = []
            var date = new Date();
            date.setMinutes(0, 0, 0);
            var ts = Math.round(date.getTime() / 1000);
            var tsYesterday = ts - (numberOfHoursAgo * 3600);
            if (Debug) console.log("Iterate from " + tsYesterday + " to " + ts + " stepsize=" + (xAxisTicksEveryM * 60));
            for (var x = tsYesterday, i = 0; x < ts; x += (xAxisTicksEveryM * 60), i += xAxisTicksEveryM)
            {
                if ((i % xAxisLabelEveryM))
                    ticksAndLabelsList.push(i);
                else
                {
                    var currentDate = new Date(x * 1000);
                    // Hours part from the timestamp
                    var hours = "0" + currentDate.getHours();
                    // Minutes part from the timestamp
                    var minutes = "0" + currentDate.getMinutes();
                    // Seconds part from the timestamp
                    var seconds = "0" + currentDate.getSeconds();
                    var formattedTime = hours.substr(-2) + ':' + minutes.substr(-2);
                    ticksAndLabelsList.push(String(i) + "^" + formattedTime);
                }
            }
            if (Debug) console.log("Ticks & Label: " + ticksAndLabelsList);
            if (Debug) console.log("Coordinates: " + coordinates)
            setState(PathSensor, ticksAndLabelsList.join("+") + '~' + coordinates, true);
        }, 
    1500
    ) ;
});
```  

# popUpNotify  

Status: in Erstellung:
 
Das ganze LUI Thema ist am Wachsen. Nun gibt es von der popUpNotify Page schon zwei verschiedene Varianten.
Diese wollen wir hier beschreiben:

## popUpNotify - alte Variante

**Beschreibung**:  
Die alte Variante kennt man am ehesten von Info-Popus zur Tasmota oder TFT Version.  
  
![image](https://user-images.githubusercontent.com/102996011/189373507-41a10711-afc0-4186-b94b-690bc1805a7f.png)
  
**Datenpunkte**:  
* popupNotifyHeading
* popupNotifyText
* popupNotifyInternalName
* popupNotifyButton1Text
* popupNotifyButton2Text
* popupNotifySleepTimeout
* popupNotifyAction
  
**Zuordnung Datenpunkte**:  
  
![popupnotify_v1](https://user-images.githubusercontent.com/99131208/200187862-a31a3223-0a1b-4d53-82e8-a93467dd19ce.jpg)
  
**Nutzung**:  
Vor der Version **v3.5.0** per Default nutzbar. Ab der Version **v3.5.0** bleibt die alte Version erstmal per Default nutzbar. Stellt man den Datenpunkt **popupNotifyLayout** auf 2 erhält man das neue popUpNotify, zur Nutzung des alten muss man dann den Wert 1 hinterlegen.  
  
**Beispiel**:  
  
Bei der [Anleitung der AlarmCard](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#2-alarm-page) gibt es zwei verschiedene Beispiele für die Nutzung der popUpNotify Page.  
  
  
## popUpNotify - Layout 2
  
**Beschreibung**:  
Ab Version **v3.5.0** verfügbar.  
Layout 2 bringt neue Funktionen mit sich wie Schriftgröße, Schriftfarbe, ein Icon mit definierbarer Farbe, etc.

![image](https://user-images.githubusercontent.com/99131208/200184667-88d4104c-5e6c-453b-8eb5-3f27183ef85a.png)  
    
**Neue Datenpunkte**:  
Die neuen Datenpunkte werden automatisch beim Starten des Skriptes angelegt. Zur Übersicht hier die neuen Datenpunkte aufgelistet:  
  
* popupNotifyHeadingColor
* popupNotifyTextColor
* popupNotifyButton1TextColor
* popupNotifyButton2TextColor
* popupNotifyLayout
* popupNotifyFontIdText (Schriftgröße)
* popupNotifyIcon
* popupNotifyIconColor
  
**Zuordnung Datenpunkte**:   
  
![popupnotify_v2](https://user-images.githubusercontent.com/99131208/200187887-1fbffa97-9d77-4681-bb58-384e2209c365.jpg)
  
  
**Nutzung**:  
Ab der Version **v3.5.0** bleibt die alte Version erstmal per Default nutzbar.  Stellt man den Datenpunkt **popupNotifyLayout** auf 2 erhält man das neue popUpNotify, zur Nutzung des alten muss man dann den Wert 1 hinterlegen.  
  
**Emulator (Layout 2)**:    
[Zum Blockly](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/PopupNotify_layout2_Emulator.xml)
