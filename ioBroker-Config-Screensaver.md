Der überarbeitete Screensaver **ab v3.4.0**  


# Screensaver 1 Layout (Standard)  

Ansicht Weather-Forecast:  
![image](https://user-images.githubusercontent.com/102996011/215202503-b4a407a9-c44e-4c05-8bb5-e4525db48ae3.png)  

Ansicht Screensaver-Entities:  
![image](https://user-images.githubusercontent.com/102996011/190849281-0ef61e4f-3d92-4959-a66b-92dd292ec407.png)  
  
# Screensaver 1 Layout (Alternativ)
  
Ansicht Weather-Forecast:  
![image](https://user-images.githubusercontent.com/102996011/190611272-c3bf9f34-c9c0-400d-ae03-c05bdfa8071b.png)  

Ansicht Screensaver-Entities:  
![image](https://user-images.githubusercontent.com/102996011/190849999-48ed259b-7c1b-4a4f-887d-f354d7bab07d.png)  

![image](https://user-images.githubusercontent.com/102996011/217248632-ac7394ec-26d3-47d3-8d2b-fd547955220b.png)   
Das alternative Screensaver-Layout lässt sich im Servicemenü aktivieren.  

# Screensaver 2 Layout

> ab v4.0.0
  

# Screensaver Colors
```
//Screensaver Default Theme Colors
const scbackground:     RGB = { red:   0, green:    0, blue:   0};
const sctime:           RGB = { red: 255, green:  255, blue: 255};
const sctimeAMPM:       RGB = { red: 255, green:  255, blue: 255};
const scdate:           RGB = { red: 255, green:  255, blue: 255};
const sctMainIcon:      RGB = { red: 255, green:  255, blue: 255};
const sctMainText:      RGB = { red: 255, green:  255, blue: 255};
const sctForecast1:     RGB = { red: 255, green:  255, blue: 255};
const sctForecast2:     RGB = { red: 255, green:  255, blue: 255};
const sctForecast3:     RGB = { red: 255, green:  255, blue: 255};
const sctForecast4:     RGB = { red: 255, green:  255, blue: 255};
const sctF1Icon:        RGB = { red: 255, green:  235, blue: 156};
const sctF2Icon:        RGB = { red: 255, green:  235, blue: 156};
const sctF3Icon:        RGB = { red: 255, green:  235, blue: 156};
const sctF4Icon:        RGB = { red: 255, green:  235, blue: 156};
const sctForecast1Val:  RGB = { red: 255, green:  255, blue: 255};
const sctForecast2Val:  RGB = { red: 255, green:  255, blue: 255};
const sctForecast3Val:  RGB = { red: 255, green:  255, blue: 255};
const sctForecast4Val:  RGB = { red: 255, green:  255, blue: 255};
const scbar:            RGB = { red: 255, green:  255, blue: 255};
const sctMainIconAlt:   RGB = { red: 255, green:  255, blue: 255};
const sctMainTextAlt:   RGB = { red: 255, green:  255, blue: 255};
const sctTimeAdd:       RGB = { red: 255, green:  255, blue: 255};
```
Wenn die automatischen Farben der Weather-Forcast nicht verwendet werden sollen:
```
export const config: Config = {
    ...
    autoWeatherColorScreensaverLayout: false,
```

![image](https://user-images.githubusercontent.com/102996011/190623367-70ebe988-f467-49cf-8e81-2275a8db259b.png)

Ansonsten greifen diese Farben
```
//Auto-Weather-Colors
const swClearNight:     RGB = { red: 150, green: 150, blue: 100};
const swCloudy:         RGB = { red:  75, green:  75, blue:  75};
const swExceptional:    RGB = { red: 255, green:  50, blue:  50};
const swFog:            RGB = { red: 150, green: 150, blue: 150};
const swHail:           RGB = { red: 200, green: 200, blue: 200};
const swLightning:      RGB = { red: 200, green: 200, blue:  0};
const swLightningRainy: RGB = { red: 200, green: 200, blue: 150};
const swPartlycloudy:   RGB = { red: 150, green: 150, blue: 150};
const swPouring:        RGB = { red:  50, green:  50, blue: 255};
const swRainy:          RGB = { red: 100, green: 100, blue: 255};
const swSnowy:          RGB = { red: 150, green: 150, blue: 150};
const swSnowyRainy:     RGB = { red: 150, green: 150, blue: 255};
const swSunny:          RGB = { red: 255, green: 255, blue:   0};
const swWindy:          RGB = { red: 150, green: 150, blue: 150};
```

# Screensaver Icons

## Großes Wetter Icon

![image](https://user-images.githubusercontent.com/102996011/189405373-8ea44dd3-a073-40e8-8379-faab8a836d12.png)  

siehe https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#wettervorhersage

> **Achtung:**  
> **Dieser Alias "muss" korrekt erstellt werden, damit die 4 kleineren Entity-Status-Icons (Weather-Forecast und/oder 4 Sensordatenpunkte) im unteren Screensaver visualisiert werden können.**  
 
> Ab TS-Script-Version 3.5.0.5 und mit installiertem JavaScript-Adapter ab Version v6.1.3 kann dieser Alias u.a. automatisch erzeugt werden, wenn die Konstante **autoCreateAlias** auf **true** steht.

Die Dargestellten Wetter-Icons (groß und klein) werden im NSPanel TS-Script ermittelt. Daher ist die Installation von Accuweather zwingend erforderlich.  Weitere Hinweise zur Installation des Accuweather Adapters hier: https://github.com/iobroker-community-adapters/ioBroker.accuweather

## Relais-Status Icons

![image](https://user-images.githubusercontent.com/102996011/190625454-181092a5-83ea-4ac7-bff5-10274ec98ad5.png)

**Folgende 4 Einstellungs-Varianten sind möglich:**

**1. Die Icons visualisieren den Relais-Zustand der Hardware-Buttons:**  
```
export const config: Config = {
    ...
    mrIcon1ScreensaverEntity: { ScreensaverEntity: 'mqtt.0.SmartHome.NSPanel_1.stat.POWER1', ScreensaverEntityIcon: 'light-switch', ScreensaverEntityOnColor: On, ScreensaverEntityOffColor: Off  },
    mrIcon2ScreensaverEntity: { ScreensaverEntity: 'mqtt.0.SmartHome.NSPanel_1.stat.POWER2', ScreensaverEntityIcon: 'lightbulb', ScreensaverEntityOnColor: On, ScreensaverEntityOffColor: Off  },
```
Die mqtt.0. Datenpunkte entsprechend deiner mqtt-Komfiguration anpassen  
  
**2. Die Icons sind nicht sichtbar:**  
```
export const config: Config = {
    ...
    mrIcon1ScreensaverEntity: { ScreensaverEntity: null, ScreensaverEntityIcon: null, ScreensaverEntityOnColor: On, ScreensaverEntityOffColor: Off  },
    mrIcon2ScreensaverEntity: { ScreensaverEntity: null, ScreensaverEntityIcon: null, ScreensaverEntityOnColor: On, ScreensaverEntityOffColor: Off  },
```


**3. Die Icons werden mit anderen Datenpunkten vom Typ "boolean" (true/false) belegt:**  
```
export const config: Config = {
    ...
    mrIcon1ScreensaverEntity: { ScreensaverEntity: "0_userdata.0.NSPanel.1.Buttons.MRHWBTN1", ScreensaverEntityIcon: "light-switch", ScreensaverEntityOnColor: On, ScreensaverEntityOffColor: Off  },
    mrIcon2ScreensaverEntity: { ScreensaverEntity: "0_userdata.0.NSPanel.1.Buttons.MRHWBTN2", ScreensaverEntityIcon: "lightbulb", ScreensaverEntityOnColor: On, ScreensaverEntityOffColor: Off  },
```

**4. Beliebig im Mix der 3 Varianten**   
> ScreensaverEntityIcon kann für alle 4 Varianten frei gewählt werden: siehe https://htmlpreview.github.io/?https://github.com/jobr99/Generate-HASP-Fonts/blob/master/cheatsheet.html
---

## Erweiterung der Relay/Status Icons (ab v3.9.0)  

![image](https://user-images.githubusercontent.com/102996011/215198305-3c1d7b6d-18bc-481c-86ed-c30eabb46f23.png)  

Ab v3.9.0 ist es möglich auch Werte (z.B. Temoperatur-Sensor) in den Status-Icons anzuzeigen Nachfolgende Beispiele zeigen:
1. eine Einstellung zur Nutzung der Relais
2. eine Einstellung zur Nutzung individueller Datenpunkte mit Nachkommastelle und Einheit des Wertes

```  
    // Indikator Icons im oberen Teil des Screensavers
    // Mit 3.9.0 neue Parameter - Bitte anpassen - siehe auch Wiki
    mrIcon1ScreensaverEntity: { ScreensaverEntity: 'mqtt.0.SmartHome.NSPanel_1.stat.POWER1', 
                                ScreensaverEntityIconOn: 'lightbulb',                           //Rename
                                ScreensaverEntityIconOff: null, 
                                ScreensaverEntityValue: null,                                   //New
                                ScreensaverEntityValueDecimalPlace : 0,                         //New
                                ScreensaverEntityValueUnit: null,                               //New
                                ScreensaverEntityOnColor: On, 
                                ScreensaverEntityOffColor: HMIOff },
    mrIcon2ScreensaverEntity: { ScreensaverEntity: 'deconz.0.Sensors.5.open', 
                                ScreensaverEntityIconOn: 'heat-wave',
                                ScreensaverEntityIconOff: null, 
                                ScreensaverEntityValue: 'deconz.0.Sensors.65.temperature',
                                ScreensaverEntityValueDecimalPlace : 1,
                                ScreensaverEntityValueUnit: '°', 
                                ScreensaverEntityOnColor: MSRed, 
                                ScreensaverEntityOffColor: Yellow },
```  
In Beispiel 2 wird statt des Relais, ein Fenstersensor (open = true/false) als Indikator verwendet. Der Wert kann über `ScreensaverEntityValue` eingeblendet werden. Darüber hinaus ist es möglich, die Nachkommastelle mit `ScreensaverEntityValueDecimalPlace` anzugeben und eine Einheit des Wertes mit `ScreensaverEntityValueUnit` zu visualisieren.  


## Entity-Status Icons  

![image](https://user-images.githubusercontent.com/102996011/190727328-175a5a2d-48ba-4370-911e-c6e2029ef9cc.png)  


> **Achtung: neuer Parameter "ScreensaverEntityIconColor"**. Bei Bestehenden Skripten (Migration) **unbedingt analog der nachfolgenden Zeilen erweitern!**
  
```
export const config: Config = {
    ...
    firstScreensaverEntity:   { ScreensaverEntity: 'accuweather.0.Hourly.h0.PrecipitationProbability',
                                ScreensaverEntityFactor: 1,                                 //New
                                ScreensaverEntityDecimalPlaces: 0,                          //New 
                                ScreensaverEntityIcon: 'weather-pouring', 
                                ScreensaverEntityText: 'Regen', 
                                ScreensaverEntityUnitText: '%', 
                                ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 100} 
                              },
    secondScreensaverEntity:  { ScreensaverEntity: 'accuweather.0.Current.WindSpeed', 
                                ScreensaverEntityFactor: (1000/3600),                       //New
                                ScreensaverEntityDecimalPlaces: 1,                          //New 
                                ScreensaverEntityIcon: 'weather-windy', 
                                ScreensaverEntityText: "Wind", 
                                ScreensaverEntityUnitText: 'm/s', 
                                ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 35} 
                              },
    thirdScreensaverEntity:   { ScreensaverEntity: 'accuweather.0.Current.UVIndex',
                                ScreensaverEntityFactor: 1,                                 //New
                                ScreensaverEntityDecimalPlaces: 0,                          //New  
                                ScreensaverEntityIcon: 'solar-power', 
                                ScreensaverEntityText: 'UV', 
                                ScreensaverEntityUnitText: '', 
                                ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 9} 
                              },//
    fourthScreensaverEntity:  { ScreensaverEntity: 'accuweather.0.Current.RelativeHumidity',
                                ScreensaverEntityFactor: 1,                                 //New
                                ScreensaverEntityDecimalPlaces: 0,                          //New 
                                ScreensaverEntityIcon: 'water-percent', 
                                ScreensaverEntityText: 'Luft', 
                                ScreensaverEntityUnitText: '%', 
                                ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 100, 'val_best': 65} 
                              },
```  

Der letzte Parameter **ScreensaverEntityIconColor** der first- fourthScreensaverEntity

**Wie kann ich die Farben definieren?**
Folgende Varianten stehen zur Verfügung:

```
ScreensaverEntityIconColor: undefined 
//Die Default-Farbe wird gewählt.
```

```
ScreensaverEntityIconColor: MSGreen  
//Eine definierte Farbe wird gewählt.
```

```
ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 100}  
//Berechnung einer Farbe über über Skala z.B. Regenwahrscheinlichkeit
```  

```
ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 9}  
//Berechnung einer Farbe über über Skala z.B. UV-Skala
```  

```
ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 100, 'val_best': 65}  
//Berechnung einer Farbe über über Skala mit Idealwert
```  
z.B. für Luftfeuchte: Der Idealwert liegt zwischen 0 und 100 hier im Beispiel bei 65% (also grün). Die Abschwächung geht zu beiden Seiten (65 zu 0) und (65 zu 100) über gelb nach rot.


> **Im Alternativen Layout können nur 3 Entities visualisiert werden. Für die Darstellung  der Luftfeuchte wird die fourthScreensaverEntity verwendet!**

## Wechsel zwischen Entity-Status-Icons und WeatherForecast  

Es lässt sich über 2 Datenpunkte in 0_userdata.0. steuern ob:  
* nur die 4 Entity-Status-Icons visualisiert wird  
* nur die Wettervorhersage visualisiert wird  
* die 4 Entity-Status-Icons und die Wettervorhersage (60 Sekunden abwechselnd) visualisiert wird  

Wenn ein Wechsel stattfinden soll, dann muss:  
**0_userdata.0.NSPanel.X.ScreensaverInfo.weatherForecastTimer** den Wert **true** haben  

In diesem Fall ist keine weitere Einstellung erforderlich. Es wird ein Wechsel über das TS-Skript initiiert.  

Wenn kein Wechsel stattfinden soll, dann muss:  
**0_userdata.0.NSPanel.X.ScreensaverInfo.weatherForecastTimer** den Wert **false** haben  

Wenn die 4 Wetter Icons sichtbar sein sollen (Timer für Wechsel deaktiviert)  
**0_userdata.0.NSPanel.X.ScreensaverInfo.weatherForecast** den Wert **true** haben  

Wenn die 4 Entity Icons sichtbar sein sollen (Timer für Wechsel deaktiviert)  
**0_userdata.0.NSPanel.X.ScreensaverInfo.weatherForecast** den Wert **false** haben  