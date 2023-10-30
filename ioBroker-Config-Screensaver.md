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
  
# Screensaver 2 Layout (Advanced)

> ab v4.0.0  
  
![image](https://user-images.githubusercontent.com/102996011/221548005-f95c0949-2f51-4fca-8c31-08ec9083096c.png)  

![image](https://user-images.githubusercontent.com/102996011/221548499-c50d1101-a6a3-468f-82e9-ae83fb870655.png)  

![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/7c5d28bd-08ce-44f9-aab1-55430890099f)  
  
Das Screensaver-Layout lässt sich im Servicemenü Einstellungen -> Screensaver -> Layout aktivieren.  
Es darf nur ein Layout aktiviert sein, sonst kommt es zu unerwünschten Effekten.  
Wenn kein Layout aktiv ist, wird das Layout 1 Standard genutzt.  
    
# Screensaver Colors
```typescript  
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
```typescript  
    mrIcon1ScreensaverEntity: { ScreensaverEntity: 'mqtt.0.SmartHome.NSPanel_1.stat.POWER1', ScreensaverEntityIcon: 'light-switch', ScreensaverEntityOnColor: On, ScreensaverEntityOffColor: Off  },
    mrIcon2ScreensaverEntity: { ScreensaverEntity: 'mqtt.0.SmartHome.NSPanel_1.stat.POWER2', ScreensaverEntityIcon: 'lightbulb', ScreensaverEntityOnColor: On, ScreensaverEntityOffColor: Off  },
```
Die mqtt.0. Datenpunkte entsprechend deiner mqtt-Komfiguration anpassen  
  
**2. Die Icons sind nicht sichtbar:**  
```typescript  
    mrIcon1ScreensaverEntity: { ScreensaverEntity: null, ScreensaverEntityIcon: null, ScreensaverEntityOnColor: On, ScreensaverEntityOffColor: Off  },
    mrIcon2ScreensaverEntity: { ScreensaverEntity: null, ScreensaverEntityIcon: null, ScreensaverEntityOnColor: On, ScreensaverEntityOffColor: Off  },
```


**3. Die Icons werden mit anderen Datenpunkten vom Typ "boolean" (true/false) belegt:**  
```typescript  
    mrIcon1ScreensaverEntity: { ScreensaverEntity: "0_userdata.0.NSPanel.1.Buttons.MRHWBTN1", ScreensaverEntityIcon: "light-switch", ScreensaverEntityOnColor: On, ScreensaverEntityOffColor: Off  },
    mrIcon2ScreensaverEntity: { ScreensaverEntity: "0_userdata.0.NSPanel.1.Buttons.MRHWBTN2", ScreensaverEntityIcon: "lightbulb", ScreensaverEntityOnColor: On, ScreensaverEntityOffColor: Off  },
```

**4. Beliebig im Mix der 3 Varianten**   
> ScreensaverEntityIcon kann für alle 3 Varianten frei gewählt werden: siehe https://htmlpreview.github.io/?https://github.com/jobr99/Generate-HASP-Fonts/blob/master/cheatsheet.html
---

## Erweiterung der Relay/Status Icons (ab v3.9.0)  

![image](https://user-images.githubusercontent.com/102996011/215198305-3c1d7b6d-18bc-481c-86ed-c30eabb46f23.png)  

Ab v3.9.0 ist es möglich auch Werte (z.B. Temoperatur-Sensor) in den Status-Icons anzuzeigen Nachfolgende Beispiele zeigen:
1. Icon (mrIcon1ScreensaverEntity) eine Einstellung zur Nutzung der Relais
2. Icon (mrIcon2ScreensaverEntity) eine Einstellung zur Nutzung individueller Datenpunkte mit Nachkommastelle und Einheit des Wertes

```typescript  
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

**Erweiterung ab Version 4.0.5**  
es besteht jetzt die Möglichkeit bis zu 10 Zeichen zu visualisieren und auch die Steuerung der Visualisierung hat sich erweitert.  
Die 10 Zeichen werden über `ScreensaverEntityValue` übergeben. Wenn der Datenpunkt von `ScreensaverEntity` vom Typ _**String**_ ist, dann besteht die Möglichkeit mit einem "Leerstring" den Zustand _OFF_ und mit "Text" den Zustand _ON_ zu erzeugen. Dadurch wird das entsprechende **ICON** für ON oder OFF gesetzt, wenn sie definiert sind. Zusätzlich kann man mit dem Text "ON" die Farbe der Visualisierung von `ScreensaverEntityOffColor` auf `ScreensaverEntityOnColor` wechseln.  
`ScreensaverEntityValue` und `ScreensaverEntity` müssen nicht der selbe Datenpunkt sein.  
  
Des Weiteren gibt es noch die Variante `ScreensaverEntity` vom Typ _**boolean**_ (True/False).  
Es ist auch möglich `ScreensaverEntity` auf null zu setzen, dann wird nur `ScreensaverEntityValue` ausgewertet. Wenn `ScreensaverEntityOnColor` und `ScreensaverEntityIconOn` definiert sind, werden diese mit visualisiert.


## Entity-Status Icons (ab v4.0.0) 

### Einfacher Screensaver:  
![image](https://user-images.githubusercontent.com/102996011/221557849-6caa1fce-b4a1-432f-b4e1-d862dbccb04e.png)  


**Beispiel:**  
```typescript  
export const config = <Config> {
    ...
    leftScreensaverEntity:
        [],

    bottomScreensaverEntity :  
        [
            // bottomScreensaverEntity 1
            {
                ScreensaverEntity: 'accuweather.0.Daily.Day1.Sunrise',
                ScreensaverEntityFactor: 1,
                ScreensaverEntityDecimalPlaces: 0,
                ScreensaverEntityDateFormat: { hour: '2-digit', minute: '2-digit' }, // Description at Wiki-Pages
                ScreensaverEntityIconOn: 'weather-sunset-up',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'Sonne',
                ScreensaverEntityIconColor: MSYellow
            },
            // bottomScreensaverEntity 2
            {
                ScreensaverEntity: 'accuweather.0.Current.WindSpeed',
                ScreensaverEntityFactor: (1000/3600),
                ScreensaverEntityDecimalPlaces: 1,
                ScreensaverEntityIconOn: 'weather-windy',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: "Wind",
                ScreensaverEntityUnitText: 'm/s',
                ScreensaverEntityIconColor: { 'val_min': 0, 'val_max': 120 }
            },
            // bottomScreensaverEntity 3
            {
                ScreensaverEntity: 'accuweather.0.Current.WindGust',
                ScreensaverEntityFactor: (1000/3600),
                ScreensaverEntityDecimalPlaces: 1,
                ScreensaverEntityIconOn: 'weather-tornado',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'Böen',
                ScreensaverEntityUnitText: 'm/s',
                ScreensaverEntityIconColor: { 'val_min': 0, 'val_max': 120 }
            },
            // bottomScreensaverEntity 4
            {
                ScreensaverEntity: '0_userdata.0.wetter.Windrichtung',
                ScreensaverEntityFactor: 0,
                ScreensaverEntityDecimalPlaces: 0,
                ScreensaverEntityIconOn: 'windsock',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'Windr.',
                ScreensaverEntityUnitText: '°',
                ScreensaverEntityIconColor: White
            }
        ],

    indicatorScreensaverEntity:
        [],
```  

**Wie kann ich das Format eines Datums oder einer Uhrzeit ändern?**  
  
Beispiel 1: Uhrzeit  
```typescript  
ScreensaverEntityDateFormat: { hour: '2-digit', minute: '2-digit' },
```  
  
Beispiel 2: Datum  
```typescript  
ScreensaverEntityDateFormat: { year: 'numeric', month: '2-digit', day: '2-digit' },
```  
  
Beispiel 3: Datum/Uhrzeit  
```typescript  
ScreensaverEntityDateFormat: { weekday: 'long', year: 'numeric', month: '2-digit', day: '2-digit', hour: '2-digit', minute: '2-digit' },
```    

### Erweiterter Screensaver:  
![image](https://user-images.githubusercontent.com/102996011/221555760-4805cc37-30ae-4485-a219-bdbe75f78c05.png)
  
**Beispiel:**  
```typescript  
export const config = <Config> {
    ...
    leftScreensaverEntity:
        [
            // leftScreensaverEntity 1 (only Advanced Screensaver)
            {
                ScreensaverEntity: NSPanel_Path + 'Sensor.ANALOG.Temperature',
                ScreensaverEntityFactor: 1,
                ScreensaverEntityDecimalPlaces: 1,
                ScreensaverEntityIconOn: 'thermometer',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'Temperatur',
                ScreensaverEntityUnitText: '°C',
                ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 35, 'val_best': 22}
            },
            // leftScreensaverEntity 2 (only Advanced Screensaver)
            {
                ScreensaverEntity: 'sonoff.0.DZG_DWSB20_2H.DZG_Leistung_Aktuell',
                ScreensaverEntityFactor: 1,
                ScreensaverEntityDecimalPlaces: 0,
                ScreensaverEntityIconOn: 'counter',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'L1-L3',
                ScreensaverEntityUnitText: ' W',
                ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 5000}
            },
            // leftScreensaverEntity 3 (only Advanced Screensaver)
        	{
                ScreensaverEntity: '0_userdata.0.Abfallkalender.1.date',
                ScreensaverEntityFactor: 1,
                ScreensaverEntityDecimalPlaces: 0,
                ScreensaverEntityIconOn: 'trash-can',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'Abfall',
                ScreensaverEntityUnitText: '',
                ScreensaverEntityIconColor: '0_userdata.0.Abfallkalender.1.color'
            },
        ],

    bottomScreensaverEntity :  
        [
            // bottomScreensaverEntity 1
            {
                ScreensaverEntity: 'accuweather.0.Hourly.h0.PrecipitationProbability',
                ScreensaverEntityFactor: 1,
                ScreensaverEntityDecimalPlaces: 0,
                ScreensaverEntityIconOn: 'weather-pouring',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'Regen',
                ScreensaverEntityUnitText: '%',
                ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 100}
            },
            // bottomScreensaverEntity 2
            {
                ScreensaverEntity: 'accuweather.0.Current.WindSpeed',
                ScreensaverEntityFactor: (1000/3600),
                ScreensaverEntityDecimalPlaces: 1,
                ScreensaverEntityIconOn: 'weather-windy',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: "Wind",
                ScreensaverEntityUnitText: 'm/s',
                ScreensaverEntityIconColor: { 'val_min': 0, 'val_max': 120 }
            },
            // bottomScreensaverEntity 3
            {
                ScreensaverEntity: 'accuweather.0.Current.WindGust',
                ScreensaverEntityFactor: (1000/3600),
                ScreensaverEntityDecimalPlaces: 1,
                ScreensaverEntityIconOn: 'weather-tornado',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'Böen',
                ScreensaverEntityUnitText: 'm/s',
                ScreensaverEntityIconColor: { 'val_min': 0, 'val_max': 120 }
            },
            // bottomScreensaverEntity 4
            {
                ScreensaverEntity: '0_userdata.0.wetter.Windrichtung',
                ScreensaverEntityFactor: 0,
                ScreensaverEntityDecimalPlaces: 0,
                ScreensaverEntityIconOn: 'windsock',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'Windr.',
                ScreensaverEntityUnitText: '°',
                ScreensaverEntityIconColor: White
            },
            // bottomScreensaverEntity 5 (only Advanced Screensaver)
            {
                ScreensaverEntity: 'accuweather.0.Current.RelativeHumidity',
                ScreensaverEntityFactor: 1,
                ScreensaverEntityDecimalPlaces: 1,
                ScreensaverEntityIconOn: 'water-percent',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'Feuchte',
                ScreensaverEntityUnitText: '%',
                ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 100, 'val_best': 65}
            },
            // bottomScreensaverEntity 6 (only Advanced Screensaver)
            {
                ScreensaverEntity: 'accuweather.0.Current.UVIndex',
                ScreensaverEntityFactor: 1,
                ScreensaverEntityDecimalPlaces: 0,
                ScreensaverEntityIconOn: 'solar-power',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'UV',
                ScreensaverEntityUnitText: '',
                ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 9}
            }
        ],

    indicatorScreensaverEntity:
        [
            // indicatorScreensaverEntity 1 (only Advanced Screensaver)
            { 
                ScreensaverEntity: '0_userdata.0.NSPanel.Indicators.Haus',
                ScreensaverEntityFactor: 1,
                ScreensaverEntityDecimalPlaces: 0,
                ScreensaverEntityIconOn: 'window-closed-variant',
                ScreensaverEntityIconOff: 'window-open-variant',
                ScreensaverEntityText: 'Fenster',
                ScreensaverEntityUnitText: '%',
                ScreensaverEntityIconColor: { 'val_min': 0, 'val_max': 1 }
            },
            // indicatorScreensaverEntity 2 (only Advanced Screensaver)
            { 
                ScreensaverEntity: 'alias.0.Haus.Erdgeschoss.Buero.Sensoren.Bewegung.ACTUAL',
                ScreensaverEntityFactor: 1,
                ScreensaverEntityDecimalPlaces: 0,
                ScreensaverEntityIconOn: 'motion-sensor',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'Bewegung',
                ScreensaverEntityUnitText: '',
                ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 1}
            },
            // indicatorScreensaverEntity 3 (only Advanced Screensaver)
            { 
                ScreensaverEntity: '0_userdata.0.NSPanel.Indicators.Garage',
                ScreensaverEntityFactor: 1,
                ScreensaverEntityDecimalPlaces: 0,
                ScreensaverEntityIconOn: 'garage-variant-lock',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'Garage',
                ScreensaverEntityUnitText: '',
                ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 1}
            },
            // indicatorScreensaverEntity 4 (only Advanced Screensaver)
            { 
                ScreensaverEntity: 'worx.0.202130267302000866BF.mower.state',
                ScreensaverEntityFactor: 1,
                ScreensaverEntityDecimalPlaces: 0,
                ScreensaverEntityIconOn: 'robot-mower-outline',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'Mäher',
                ScreensaverEntityUnitText: '%',
                ScreensaverEntityIconColor: { 'val_min': 0, 'val_max': 1 }
            },
            // indicatorScreensaverEntity 5 (only Advanced Screensaver)
            { 
                ScreensaverEntity: '0_userdata.0.Wasserstand.KNOCK.Wert',
                ScreensaverEntityFactor: 1,
                ScreensaverEntityDecimalPlaces: 1,
                ScreensaverEntityIconOn: 'waves-arrow-up',
                ScreensaverEntityIconOff: null,
                ScreensaverEntityText: 'Feuchte',
                ScreensaverEntityUnitText: '%',
                ScreensaverEntityIconColor: {'val_min': 0, 'val_max': 985, 'val_best': 500}
            }
        ],
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
    
```typescript  
//Dynamische Indikatoren (Abstufung grün nach gelb nach rot)
const colorScale0:      RGB = { red:  99, green: 190, blue: 123 };
const colorScale1:      RGB = { red: 129, green: 199, blue: 126 };
const colorScale2:      RGB = { red: 161, green: 208, blue: 127 };
const colorScale3:      RGB = { red: 129, green: 217, blue: 126 };
const colorScale4:      RGB = { red: 222, green: 226, blue: 131 };
const colorScale5:      RGB = { red: 254, green: 235, blue: 132 };
const colorScale6:      RGB = { red: 255, green: 210, blue: 129 };
const colorScale7:      RGB = { red: 251, green: 185, blue: 124 };
const colorScale8:      RGB = { red: 251, green: 158, blue: 117 };
const colorScale9:      RGB = { red: 248, green: 131, blue: 111 };
const colorScale10:     RGB = { red: 248, green: 105, blue: 107 };
``` 
  
Für Alias-Punkte vom Type boolean, wählt man mit val_best ob Rot oder Grün bei True kommen soll.
```
ScreensaverEntityIconColor: {'val_best': 1}  
//Bei True = Grün
```  


> **Im Alternativen Layout können nur 3 Entities visualisiert werden. Für die Darstellung  der Luftfeuchte wird die fourthScreensaverEntity verwendet!**

## Entity-Status-Icons und WeatherForecast  
  
Es lässt sich über Datenpunkte in 0_userdata.0. steuern ob:  
* nur die Entity-Status-Icons visualisiert wird  
* nur die Wettervorhersage visualisiert wird  
* die Entity-Status-Icons und die Wettervorhersage abwechselnd visualisiert wird und in welcher Zeit der Wechsel stattfinden soll 

Wenn die **Wetter Icons** sichtbar sein sollen (Timer für Wechsel deaktiviert)  
**0_userdata.0.NSPanel.X.ScreensaverInfo.weatherForecast** den Wert **true** haben  

Wenn die **Entity Icons** sichtbar sein sollen (Timer für Wechsel deaktiviert)  
**0_userdata.0.NSPanel.X.ScreensaverInfo.weatherForecast** den Wert **false** haben  
  
Wenn ein Wechsel stattfinden soll, dann muss:  
**0_userdata.0.NSPanel.X.ScreensaverInfo.weatherForecastTimer** den Wert **true** haben  
  
Wenn kein Wechsel stattfinden soll, dann muss:  
**0_userdata.0.NSPanel.X.ScreensaverInfo.weatherForecastTimer** den Wert **false** haben  
  
In wieviel **Sekunden** soll der Wechsel stattfinden  
**0_userdata.0.NSPanel.Büro.ScreensaverInfo.entityChangeTime** ein Wert zwischen **15 - 60** Sekunden  
    
Wenn die automatischen Farben der Weather-Forcast **nicht** verwendet werden sollen:
**0_userdata.0.NSPanel.1.Config.Screensaver.autoWeatherColorScreensaverLayout** den Wert **false** haben  
  
Die Einstellungen lassen sich auch am Panel einstellen unter "Einstellungen -> Screensaver -> Wetter"  
  
![Wetter](https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/9f9b7f69-e23d-4768-b768-4293766ad84f)  
    
### Weather-Forcast-Farben

![image](https://user-images.githubusercontent.com/102996011/190623367-70ebe988-f467-49cf-8e81-2275a8db259b.png)  
  
```typescript  
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
  
  
# Screensaver Dimmode  

## Automatischer Dimmode:  

Über die Parameter (auch im Servicemenü verfügbar), lassen sich die Helligkeit des Screensavers zur Uhrzeit einstellen.  

* 0_userdata.0.NSPanel.1.NSPanel_Dimmode_brightnessDay  - Die Helligkeit (0-100) in der der Screensaver tagsüber gedimmt wird (im Menü 0-10)  
* 0_userdata.0.NSPanel.1.NSPanel_Dimmode_brightnessNight - Die Helligkeit (0-100) in der der Screensaver nachts gedimmt wird (im Menü 0-10)  
* 0_userdata.0.NSPanel.1.NSPanel_Dimmode_hourDay - Die Stunde in der der Tag Dimm-Modus aktiv werden soll  
* 0_userdata.0.NSPanel.1.NSPanel_Dimmode_hourNight - Die Stunde in der der Nacht Dimm-Modus aktiv werden soll   
  
 
![Dimmode](https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/192f8d01-83b1-4457-98b4-d83620a9a934)


## Manueller Dimmode:  

0_userdata.0.NSPanel.1.ScreensaverInfo.activeDimmodeBrightness  

* null = automatischer Dimmode aktiv  
* 0-100 = manuelle Dimmstufe (automatischer Dimmode inaktiv)  

## bestimme Seite nach den Aufwecken  
unter 0_userdata.0.NSPanel.ScreensaverInfo.bExitPage könnt ihr eine Seite festlegen die nach dem tippen auf das Panel geöffnet werden soll.  
Der Wert 'null' öffnet wieder die letzte offene Seite. Wenn ihr eine Bestimmte Seite öffnen wollt, müsst ihr den Index der Seite eingeben ( Beginn bei 0). Diesen bekommt ihr aus der Pageauflistung in der Config raus.

