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
![image](https://user-images.githubusercontent.com/102996011/190608902-6cf53114-3fb8-453f-bf87-f13731d9a71f.png)  
  
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
![image](https://user-images.githubusercontent.com/102996011/190611031-c2d5e638-dd45-42d3-9dfc-e058e1b0140f.png)  


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

**Folgende Einstellungen sind möglich:**

**1. Die Icons visualisieren den Relais-Zustand der Hardware-Buttons:**  
```
export const config: Config = {
    ...
    mrIcon1ScreensaverEntity: { ScreensaverEntity: "mqtt.0.SmartHome.NSPanel_1.stat.POWER1", ScreensaverEntityIcon: "light-switch" },
    mrIcon2ScreensaverEntity: { ScreensaverEntity: "mqtt.0.SmartHome.NSPanel_1.stat.POWER2", ScreensaverEntityIcon: "lightbulb" },
```
Die mqtt.0. Datenpunkte entsprechend deiner mqtt-Komfiguration anpassen  
  
**2. Die Icons sind nicht sichtbar:**  
```
export const config: Config = {
    ...
    mrIcon1ScreensaverEntity: { ScreensaverEntity: null, ScreensaverEntityIcon: null },
    mrIcon2ScreensaverEntity: { ScreensaverEntity: null, ScreensaverEntityIcon: null },
```


**3. Die Icons werden mit anderen Datenpunkten vom Typ "boolean" (true/false) belegt:**  
```
export const config: Config = {
    ...
    mrIcon1ScreensaverEntity: { ScreensaverEntity: "0_userdata.0.NSPanel.1.Buttons.MRHWBTN1", ScreensaverEntityIcon: "light-switch" },
    mrIcon2ScreensaverEntity: { ScreensaverEntity: "0_userdata.0.NSPanel.1.Buttons.MRHWBTN2", ScreensaverEntityIcon: "lightbulb" },
```

**4. Beliebig im Mix der 3 Varianten**

## Entity-Status Icons