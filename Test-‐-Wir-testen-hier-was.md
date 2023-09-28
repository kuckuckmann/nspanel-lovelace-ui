Auf dieser Seite testen wir was für die zukünftige Wiki

# Einleitung
  
  
  
# Geblubber


# **Index**  
  
* Color Aliase 1
* Stromzähler L1+L2+L3
* Büro Temperatur
* cardPower Emulator
* Color Aliase 2
* Sonstige Aliase
* Büro
* Fenster und Türen
* Button Aliase
* Test Subpages
* Abfallkalender
* Gäste WLAN
* Büro 2
* Radiosender
* WLED Stripes WZ
* Sensor Werte
* Alexa
* Sonos
* Spotify-Premium
* SqueezeboxRPC
* Test Thermostat
* Test Klimaanlage
* Pool Wärmepumpe
* Alarmanlage
* Service Pages
* Radio
* Büro 
  
  
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
  
  
***

