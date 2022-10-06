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

# cardMedia
![image](https://user-images.githubusercontent.com/102996011/190164192-27491246-8e49-4c27-ba06-6cc711dd04c9.png)

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

![image](https://user-images.githubusercontent.com/102996011/190120470-f0b84f87-dc46-4cf2-8e08-598331168aab.png)  
![image](https://user-images.githubusercontent.com/102996011/190120711-59097159-847e-49d7-9545-a460dc271d13.png)  

```  
var Sprechender_eindeutiger_Seitenname: PageThermo = 
{
    "type": "cardThermo",
    "heading": "Deine Überschrift",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{ id: "alias.0.NSPanel_1.TestKlimaanlage", minValue: 170, maxValue: 250}]
};
```  

**Parameter:**  
minValue: Minimale einzustellende Temperatur (Beispiel: 17°C entspricht 170)  
maxValue: Maximale einzustellende Temperatur (Beispiel: 30,5°C entspricht 305)  

# cardPower (ab TS-Script v.3.4.1) 
  
![image](https://user-images.githubusercontent.com/102996011/194293110-0181995d-a6c8-45c8-a9a1-1eeba275598f.png)

Beschreibung folgt!

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
        <PageItem>{ id: "alias.0.NSPanel_1.Power.PowerCard.ACTUAL" },
    ]
};
```  


**Parameter:**  
Es gibt nur einen einzigen externen Datenpunkt (anzulegen in 0_userdata.0.)auf den ein Alias vom Typ "Info" zugreift. Dieser muss mit einem JSON-Objekt in nachfolgender Struktur befüllt werden. Der Alias-Datenpunkt "ACTUAL" sollte hierbei auf den Datenpunkt in "0_userdata.0.) gebunden sein.  
  
```  
[
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
    "value": 6.1,
    "unit": "kW",
    "direction": "in",
    "icon": "solar-power-variant",
    "iconColor": 1,
    "speed": 3
  },
  {
    "id": 3,
    "value": 4.9,
    "unit": "kW",
    "direction": "in",
    "icon": "wind-turbine",
    "iconColor": 0,
    "speed": 3
  },
  {
    "id": 4,
    "value": 1.6,
    "unit": "kW",
    "direction": "in",
    "icon": "shape",
    "iconColor": 10,
    "speed": 3
  },
  {
    "id": 5,
    "value": 6.4,
    "unit": "kW",
    "direction": "in",
    "icon": "transmission-tower",
    "iconColor": 0,
    "speed": 2
  },
  {
    "id": 6,
    "value": 0,
    "unit": "kW",
    "direction": "in",
    "icon": "car",
    "iconColor": 0,
    "speed": 3
  }
]
```  