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
  
  
# Page Beispiele  
  
<details>
  <summary>PageEntities</summary> 
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

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
  
## Card  
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card  
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
</details>  
  
***
    
<details>
  <summary>PageMedia</summary> 
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
</details>  
  
***  
  
<details>
  <summary>PageThermo</summary> 
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
</details>  
  
***
    
<details>
  <summary>PageAlarm & PageUnlock</summary> 
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
</details>  
  
***  
  
<details>
  <summary>PageChart</summary> 
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
</details>  
  
***  
  
<details>
  <summary>PagePower</summary> 
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
</details>  
  
***  
  
<details>
  <summary>PageQR</summary> 
  
## Card
  
<PLATZHALTER PICTURE>
  
``` 

```  
</details>  
  
***

