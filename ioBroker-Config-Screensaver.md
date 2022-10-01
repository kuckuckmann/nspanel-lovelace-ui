Der überarbeitete Screensaver **ab v3.4.0**

# Screensaver Layout (Standard)  

```
export const config: Config = {
    ...
    alternativeScreensaverLayout: false,
    autoWeatherColorScreensaverLayout: true,
```

Ansicht Weather-Forecast:  
![image](https://user-images.githubusercontent.com/102996011/190608554-a5719dfa-076c-46f5-9b01-30234493b035.png)  
Ansicht Screensaver-Entities:  
![image](https://user-images.githubusercontent.com/102996011/190849281-0ef61e4f-3d92-4959-a66b-92dd292ec407.png)  
  
# Screensaver Layout (Alternativ)

```
export const config: Config = {
    ...
    alternativeScreensaverLayout: true,
    autoWeatherColorScreensaverLayout: true,
```
  
Ansicht Weather-Forecast:  
![image](https://user-images.githubusercontent.com/102996011/190611272-c3bf9f34-c9c0-400d-ae03-c05bdfa8071b.png)  
Ansicht Screensaver-Entities:  
![image](https://user-images.githubusercontent.com/102996011/190849999-48ed259b-7c1b-4a4f-887d-f354d7bab07d.png)  


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


## Entity-Status Icons  

![image](https://user-images.githubusercontent.com/102996011/190727328-175a5a2d-48ba-4370-911e-c6e2029ef9cc.png)  


> **Achtung: neuer Parameter "ScreensaverEntityIconColor"**. Bei Bestehenden Skripten (Migration) **unbedingt analog der nachfolgenden Zeilen erweitern!**
  
```
export const config: Config = {
    ...
    firstScreensaverEntity: { ScreensaverEntity: "accuweather.0.Daily.Day1.Day.PrecipitationProbability", ScreensaverEntityIcon: "weather-pouring", ScreensaverEntityText: "Regen", ScreensaverEntityUnitText: "%", ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 100} },
    secondScreensaverEntity: { ScreensaverEntity: "accuweather.0.Current.WindSpeed", ScreensaverEntityIcon: "weather-windy", ScreensaverEntityText: "Wind", ScreensaverEntityUnitText: "km/h", ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 180}},
    thirdScreensaverEntity: { ScreensaverEntity: "accuweather.0.Current.UVIndex", ScreensaverEntityIcon: "solar-power", ScreensaverEntityText: "UV", ScreensaverEntityUnitText: "", ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 9} },
    fourthScreensaverEntity: { ScreensaverEntity: "accuweather.0.Current.RelativeHumidity", ScreensaverEntityIcon: "water-percent", ScreensaverEntityText: "Luft", ScreensaverEntityUnitText: "%", ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 100} },
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