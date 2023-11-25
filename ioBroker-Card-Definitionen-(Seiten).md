# cardEntities
![image](https://user-images.githubusercontent.com/102996011/190120141-13da0024-261d-4cd9-a104-13416c224004.png)  

4 vertikal angeordnete Steuerelemente (Erstellung der "PageItem" siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen))  

```typescript  
var Sprechender_eindeutiger_Seitenname = <PageEntities>
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
![image](https://user-images.githubusercontent.com/102996011/216006497-24b09a3c-28a9-41f0-b822-2b8e56491703.png)   
 
![image](https://user-images.githubusercontent.com/102996011/216006611-32155c9c-84ba-48eb-8b07-2485d80eb99b.png)  

6 horizontal angeordnete Steuerelemente (in 2 Reihen je 3 Steuerelemente) (Erstellung der "PageItem" siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen))  

```typescript  
var Sprechender_eindeutiger_Seitenname = <PageGrid>
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

# cardUnlock (ab v4.3.3)  

Die cardUnlock dient der Absicherung spezieller Seiten, die vor unbefugtem Zugriff (ggfs. Service Pages) geschützt werden sollen:  
![image](https://user-images.githubusercontent.com/102996011/221621287-55987efd-143b-4ad0-b7bb-d35d58436b12.png)  

> Bei Benutzung der cardUnlock wird die Zielseite aus dem Page-Array herausgenommen. Die Target-Page sollte nicht als Top-Level-Page, sondern als Subpage definiert sein.  

im Datenpunkt **0_userdata.0.NSPanel.Unlock.UnlockPin** kann eine PIN vergeben werden. Default wird diese PIN als **0000** definiert.  

Erstellung des Alias:  
Die cardUnlock wird ab Version `4.3.3.3` mit einem Alias vom Gerätetyp `Feueralarm` automatisch erstellt. Die Erstellung des Alias und der zugehörigen Datenpunkte erfolgt, `sobald die cardUnlock erstmals eingebunden und aufgerufen` wird.  

Unter 0_userdata.0... werden folgende Datenpunkte automatisch angelegt:
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/46f63c7c-154e-4c47-8caa-41bed30bcf70)
Die angelegte PIN-Nummer lässt sich unter "Wert" von "0000" in (siehe Beispiel) z.B. "1234" ändern.

Unter alias.0... wird folgender Alias automatisch angelegt:
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/39313dbb-3561-4f73-8352-63995ae7b8be)

**Beispiel der Seitenerstellung:** (im Service-Menü enthalten)  
```typescript  
//Level 0 (if service pages are used with cardUnlock)
let Unlock_Service = <PageUnlock>
{
    'type': 'cardUnlock',
    'heading': 'Service Pages',
    'useColor': true,
    'items': [<PageItem>{ id: 'alias.0.NSPanel.Unlock',
                          targetPage: 'NSPanel_Service_SubPage',
                          autoCreateALias: true }
    ]
};
```

siehe auch:  
* https://github.com/joBr99/nspanel-lovelace-ui/wiki/NSPanel-Service-Men%C3%BC und 
* https://github.com/joBr99/nspanel-lovelace-ui/wiki/NSPanel-Page-%E2%80%90-Typen_How-2_Beispiele#page-beispiele

Da die cardUnlock innerhalb eines "Smart Home" nur einmal erforderlich sein sollte, teilt sie die Datenpunkte mit allen weiteren NSPanels im Haus. Es ist darüber hinaus jedoch auch möglich, `weitere Seiten` über die `cardUnlock` nach dem gleichen Schema vor unbefugten Zugriffen mit dem vergebenen `PIN` zu schützen.

Hierzu muss lediglich eine weitere `Page` vom Typ `cardUnlock` definiert werden und das Ziel `targetPage` auf eine `vorhandene subPage` zeigen:  
```
let Unlock_PageXYZ = <PageUnlock>
{
    'type': 'cardUnlock',
    'heading': 'Titel der Page',
    'useColor': true,
    'items': [<PageItem>{ id: 'alias.0.NSPanel.Unlock',
                          targetPage: 'Eine_weitere_Subpage',
                          autoCreateALias: true }
    ]
};
```

# cardAlarm
![image](https://user-images.githubusercontent.com/102996011/190120272-82c6b418-c9dc-4338-a0a3-53da8bec0bac.png)

(Erstellung des alias.0.Alarm siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen))  

```typescript  
let Alarmseite = <PageAlarm>
{
    "type": "cardAlarm",
    "heading": "Alarm",
    "useColor": true,
    "subPage": false,
    "items": [
         <PageItem>{ id: 'alias.0.NSPanel.Alarm' }
                     actionStringArray: ['Vollschhutz','Zuhause','Nacht','Besuch','Ausschalten'], // Optional - ansonsten aus Sprachdatei
                     autoCreateALias: true }
         ]
};
```
# cardMedia v2.0 (ab Release v3.9.0)
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

> **Definition ab TS-Version 3.9.0** (Breaking Changes)  

**alexa2-Adapter**
```typescript  
let Alexa = <PageMedia> 
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
```typescript  
let SpotifyPremium = <PageMedia> 
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
  
```typescript  
let VolumioBoss = <PageMedia> 
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

# cardQR
![image](https://user-images.githubusercontent.com/102996011/190121115-436dc34d-3a89-4809-a3c6-2c6132938fd1.png)

> Beispiel: Erstellung des "PageItem" und Alias vom Typ "Info" siehe (https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#5-qr-code-page) by Kuckuckmann
```typescript  
var Sprechender_eindeutiger_Seitenname = <PageQR> 
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
```
hidePassword: true/false
``` 

# cardThermo  
  
(Erstellung der "PageItem" siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen)) 
  
> Für Thermostat und Klimaanlage (Unterschied im zu erstellenden Alias)

![image](https://user-images.githubusercontent.com/102996011/204626750-bbeffe48-c9cd-44bf-8dfd-b90c6c3b7422.png)  
  

![image](https://user-images.githubusercontent.com/102996011/204623942-ca5a1e74-23f7-4b10-a65a-d2397ab67c72.png)  
  
![image](https://user-images.githubusercontent.com/102996011/204626323-a5df2e57-378f-4939-8a45-1a83277e23a2.png)  
  
![image](https://user-images.githubusercontent.com/102996011/204627014-03173d87-22ba-44fb-b07c-40b7be6366ac.png)  
  
```typescript  
var Sprechender_eindeutiger_Seitenname = <PageThermo> 
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
                stepValue: 5,
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
stepValue: Schrittgröße der Temperaturänderungen (Beispiel: 0,5°C Schritte entspricht 5)

# cardPower (ab TS-Script v.3.4.1) 
  
![Nextion_Editor_9AYbpowjZS](https://user-images.githubusercontent.com/102996011/194641145-660e1218-f559-4f25-83ca-984cc677e0d8.gif)  

Beispiel: Erstellung des "PageItem" und Alias vom Typ "Info"

```typescript  
let CardPower = <PagePower>
{
    'type': 'cardPower',
    'heading': 'Energiefluss',
    'useColor': true,
    'items': [
        <PageItem>{ id: 'alias.0.NSPanel.cardPower', 
                    alwaysOnDisplay: true }
    ]
};
```  

Oder im Demo-Modus ohne Alias
```typescript  
let CardPowerExample = <PagePower>
{
    'type': 'cardPower',
    'heading': 'Energiefluss',
    'useColor': true,
    'items': [
        <PageItem>{  }
    ]
};
```


**Parameter:**  
Es gibt nur einen einzigen externen Datenpunkt (anzulegen in **0_userdata.0.**), auf den ein Alias vom Typ "**Info**" zugreift. Dieser muss mit einem JSON-Objekt in nachfolgender Struktur befüllt werden. Der Alias-Datenpunkt "**ACTUAL**" sollte hierbei auf diesen neuen Datenpunkt in "**0_userdata.0.**) gebunden sein.  
  
```json  
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
    "icon": "battery-charging-60",
    "iconColor": 10,
    "speed": 30
  },
  {
    "id": 2,
    "value": 4.7,
    "unit": "kW",
    "icon": "solar-power-variant",
    "iconColor": 3,
    "speed": -20
  },
  {
    "id": 3,
    "value": 4.3,
    "unit": "kW",
    "icon": "wind-turbine",
    "iconColor": 1,
    "speed": -30
  },
  {
    "id": 4,
    "value": 3.4,
    "unit": "kW",
    "icon": "shape",
    "iconColor": 10,
    "speed": 30
  },
  {
    "id": 5,
    "value": 0.1,
    "unit": "kW",
    "icon": "transmission-tower",
    "iconColor": 0,
    "speed": 20
  },
  {
    "id": 6,
    "value": 2.5,
    "unit": "kW",
    "icon": "car",
    "iconColor": 5,
    "speed": 20
  }
]
```  
_iconColor_ kann einen Wert von 0-10 annehmen und entspricht der ColorScale Grün -> Gelb -> Rot  
_speed_ kann positive und negative Werte annehmen, wobei positive Werte den Punkt vom Haus weggehen lassen und negative Werte zum Haus  
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

```json  
  {
    "id": 3,
    "value": "",
    "unit": "",
    "icon": "",
    "iconColor": "",
    "speed": ""
  },
```

> Das Skript stellt nur eine exemplarische Möglichkeit der Befüllung dar. Es kann frei definiert und auf eigene Bedürfnisse angepasst werden, soll aber keine finale Lösung für jede Smart Home Situation abbilden!
> Ebenso kann die Erstellung des JSON natürlich auch über JavaScript oder TypeScript erfolgen.  
  
Ein kleines einfaches Javascript von @l4rs, für die erzeugung des JSON-String.

```typescript  
/**
* generate an JSON for display Power-Card on NSPanel
* Source: https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-Card-Definitionen-(Seiten)#cardpower-ab-ts-script-v341
* Version: 0.1 - L4rs
*/
schedule("* * * * *", function () {
 
    // Definition der Datenpunkte für das JSON der POWER-Card und der anzuzeigenden Leistungswerte
    var powerCardJson = "0_userdata.0.NSPanel.Energie.PowerCard",
      pwr1 = "", // Batterie
      pwr2 = Math.round(getState("mqtt.0.SmartHome.Energie.PV.openDTU.114180710360.0.power").val),    // Solar
      pwr3 = "",    // Wind
      pwr4 = "",   // Verbraucher
      pwr5 = Math.round(getState("hm-rpc.0.MEQ0706303.1.POWER").val),    // Stromnetz
      pwr6 = 0, // Auto
      pwrHome = Math.round(pwr5 - pwr2);    // Berechnung des Energiefluss anstelle eines Datenpunktes
    
    // Definition der Keys im JSON
    var keys = ["id", "value", "unit", "icon", "iconColor", "speed"];
    
    // Definition der "Kacheln", inkl. StandardIcon. Es können alle Icon aus dem Iconmapping genutzt werden.
    // Kacheln die nicht genutzt werden sollen, müssen wie z.b. item1 formatiert sein
    var home = [0, pwrHome, "W", "home-lightning-bolt-outline", 0]; // Icon home
    var item1 = [1, pwr1, "", "", 0, ""];   // Icon battery-charging-60
    var item2 = [2, pwr2, "W", "solar-power-variant-outline", 3, pwr2 > 0 ? -2 : 0]; // Icon solar-power-variant
    var item3 = [3, pwr3, "", "", 0, ""];   // Icon wind-turbine
    var item4 = [4, pwr4, "", "", 0, ""];   // Icon shape
    var item5 = [5, pwr5, "W", "transmission-tower", 10, 10];   // Icon transmission-tower
    var item6 = [6, pwr6, "kW", "car-electric-outline", 5, 0];  // Icon car
    
    /**
     * JSON generieren und in den Datenpunkt schreiben,
     *
     *  --- ab hier keine Änderungen mehr ---
     */
    function func(tags, values) {
      return Object.assign(
        ...tags.map((element, index) => ({ [element]: values[index] }))
      );
    }
    
    setState(
      powerCardJson,
      JSON.stringify([
        func(keys, home),
        func(keys, item1),
        func(keys, item2),
        func(keys, item3),
        func(keys, item4),
        func(keys, item5),
        func(keys, item6),
      ])
    );
   });
``` 

**Hinweis:** Aktuell erfolgt die Animation gleicher Speed Werte bei der US-P Firmware durch die geänderte Orientierung in umgekehrter Reihenfolge.

# cardChart (ab TS-Script v.3.7.0)  

> ab Release v3.7.0

![image](https://user-images.githubusercontent.com/102996011/204631969-dfd8b8e9-09d0-45c2-a243-5e047f09ab05.png)  
   
> Für das unten abgebildete Blockly-Script wurden die Werte eines Datenpunktes "sonoff.0.DZG_DWSB20_2H.DZG_Leistung_Aktuell" in einer Influx 2.0 Datenbank gespeichert.  

Es wird für das Skript ein Datenpunkt (hier im Beispiel "0_userdata.0.Test.cardChart.txt") benötigt, um das Chart für die cardChart aufzubereiten.

**Alias-Erstellung:**  
Es wird lediglich ein Alias vom Gerätetyp "Info" benötigt:
![image](https://user-images.githubusercontent.com/102996011/209008594-36da27fb-cde2-4964-bcd8-3b406f4656cb.png)

**PageItem Beispiel:**
```typescript  
let CardChartExample = <PageChart>
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

## **Blockly für Influx 2.0**
![image](https://user-images.githubusercontent.com/102996011/209006326-c8036709-2235-4ef8-aa14-00798e09fce7.png)  

[Zum Blockly](https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/Blockly/CardChart.xml)

## **Javascript für History Adapter**
```typescript  
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

# cardLChart (Line Charts ab TS-Script v.3.9.0)  

> ab TS-Script Release v3.9.0

![image](https://user-images.githubusercontent.com/102996011/212094993-b78f6a38-aab7-43fd-a6c7-fa4add274b75.png)  

**Seitendefinition**  

> Der Alias unter der PageItem.id ist ein Alias vom Gerätetyp: **Info**  

* type: Für Liniendiagramme muss der Seiten-Typ "cardLChart" sein.  
* id: Es wird ein Alias vom Gerätetyp "Info" erstellt, der auf den erzeugenden Datenpunkt des unten aufgeführten Beispiel-Scriptes zeigt.  
* yAxis: Bezeichner der Y-Achse  
* yAxisTicks: Skala des Wertebereiches der Y-Achse als Array oder ObjektId zu einem Datenpunkt welcher die Skala enthält
* onColor: Farbe des Graphen  

```typescript  
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

## **Javascript für Influx2**
```javascript  
const Debug = true;

const NSPanel_Path = '0_userdata.0.NSPanel.';
const Path = NSPanel_Path + 'Influx2NSPanel.cardLChart.';
const PathSensor = Path + 'buero_temperature';

const Sensor = 'deconz.0.Sensors.65.temperature';

const numberOfHoursAgo = 24;
const xAxisTicksEveryM = 60;
const xAxisLabelEveryM = 240;

const InfluxInstance = 'influxdb.0';

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
        '|> filter(fn: (r) => r["_measurement"] == "' + Sensor+ '")',
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
            let numResults = result.result.length;
            for (let r = 0; r < numResults; r++) 
            {
                let list = []
                let numValues = result.result[r].length;

                for (let i = 0; i < numValues; i++) 
                {
                    let time = Math.round(result.result[r][i]._rtime/1000/1000/1000/60);
                    let value = Math.round(result.result[r][i]._value * 10);
                    list.push(time + ":" + value);
                }

                coordinates = list.join("~");

                if (Debug) console.log(coordinates);
            }
        }
    });

    let timeOut = setTimeout (
        function () {
            let ticksAndLabelsList = []
            let date = new Date();
            date.setMinutes(0, 0, 0);
            let ts = Math.round(date.getTime() / 1000);
            let tsYesterday = ts - (numberOfHoursAgo * 3600);
            if (Debug) console.log('Iterate from ' + tsYesterday + ' to ' + ts + ' stepsize=' + (xAxisTicksEveryM * 60));
            for (let x = tsYesterday, i = 0; x < ts; x += (xAxisTicksEveryM * 60), i += xAxisTicksEveryM)
            {
                if ((i % xAxisLabelEveryM))
                    ticksAndLabelsList.push(i);
                else
                {
                    let currentDate = new Date(x * 1000);
                    // Hours part from the timestamp
                    let hours = "0" + String(currentDate.getHours());
                    // Minutes part from the timestamp
                    let minutes = "0" + String(currentDate.getMinutes());
                    let formattedTime = hours.slice(-2) + ':' + minutes.slice(-2);

                    ticksAndLabelsList.push(String(i) + "^" + formattedTime);
                }
            }
            if (Debug) console.log('Ticks & Label: ' + ticksAndLabelsList);
            if (Debug) console.log('Coordinates: ' + coordinates);
            setState(PathSensor, ticksAndLabelsList.join("+") + '~' + coordinates, true);
        }, 
    1500
    ) ;
});
```  

## **Javascript für History adapter**
```javascript  
const sourceDP = 'alias.0.Wohnzimmer.Heizung.ACTUAL';
const targetDP = '0_userdata.0.Test.chartTest';
const numberOfHoursAgo = 24;   // Period of time in hours which shall be visualized
const xAxisTicksEveryM = 60;   // Time after x axis gets a tick  in minutes
const xAxisLabelEveryM = 240;  // Time after x axis is labeled  in minutes
const historyInstance = 'history.0';

const Debug = false;
const maxX = 1420;
const limitMeasurements = 35;

createState(targetDP, "", {
        name: 'SensorGrid',
        desc: 'Sensor Values [~<time>:<value>]*',
        type: 'string',
        role: 'value',
});

on({id: sourceDP, change: "any"}, async function (obj) {
    sendTo(historyInstance, 'getHistory', {
        id: sourceDP,
        options: {
            start:     Date.now() - (numberOfHoursAgo * 60 * 60 * 1000 ), //Time in ms: hours * 60m * 60s * 1000ms
            end:       Date.now(),
            count:     limitMeasurements,
            limit:     limitMeasurements,
            aggregate: 'average'
        }
    }, function (result) {
        var ticksAndLabels = ""
        var coordinates = "";
        var cardLChartString = "";

        let ticksAndLabelsList = []
        var date = new Date();
        date.setMinutes(0, 0, 0);
        var ts = Math.round(date.getTime() / 1000);
        var tsYesterday = ts - (numberOfHoursAgo * 3600);
        
        for (var x = tsYesterday, i = 0; x < ts; x += (xAxisTicksEveryM * 60), i += xAxisTicksEveryM)
        {
            if (i % xAxisLabelEveryM) 
            {
                ticksAndLabelsList.push(i);
            } else 
            {
                var currentDate = new Date(x * 1000);
                // Hours part from the timestamp
                var hours = "0" + currentDate.getHours();
                // Minutes part from the timestamp
                var minutes = "0" + currentDate.getMinutes();
                // Seconds part from the timestamp
                var seconds = "0" + currentDate.getSeconds();
                var formattedTime = hours.slice(-2) + ':' + minutes.slice(-2);
                ticksAndLabelsList.push(String(i) + "^" + formattedTime);
            }
        }
        ticksAndLabels = ticksAndLabelsList.join("+");        

        let list = [];
        let offSetTime = Math.round(result.result[0].ts / 1000);
        let counter = Math.round((result.result[result.result.length -1 ].ts / 1000 - offSetTime) / maxX);        
        for (var i = 0; i <  result.result.length; i++) 
        {           
            var time = Math.round(((result.result[i].ts / 1000) - offSetTime) / counter);
            var value = Math.round(result.result[i].val * 10);
            if ((value != null) && (value != 0)){
                list.push(time + ":" + value)
            }
        }

        coordinates = list.join("~");
        cardLChartString = ticksAndLabels + '~' + coordinates
        setState(targetDP, cardLChartString, true);
        
        if (Debug) console.log(cardLChartString);
    });    
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
