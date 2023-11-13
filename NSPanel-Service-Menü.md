# Servicemenü  

> ab v3.9.0  

**Das Menü ist in den Variablendefinitionen des TS-Script v3.9.0 enthalten, dient als Beispiel für eine Subpage-Gestaltung und kann beliebig angepasst werden. Die Aliase für dieses Beispiel legt das TS-Script, sofern setOption in der JavaScript-Adapter-Instanz angehakt ist, automatisch an.**  
Im Zuge der weiteren Releases wird es sukzessive um künftige Funktionalitäten erweitert

## Service-Menü-Beispiel aus dem TypeScript (NSPanelTs.ts)   

![Nextion_Editor_4keKWucXc4](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/09eb0cca-5d15-48a5-a522-6d7eceaae42d)

## Aufbau des Service-Menüs  
 
<img width="763" alt="Bildschirmfoto 2023-09-22 um 11 53 08" src="https://github.com/joBr99/nspanel-lovelace-ui/assets/101348966/edc6157c-3b70-4e1c-b544-d5e3d4c60fcf">
  
## TypeScript (NSPanel.ts) Konstanten  

nachfolgende Konstante ist für die Menüfarbe reserviert und kann individuell durch eigene RGB-Farbwerte angepasst werden.
```typescript  
//Menu Icon Colors
const Menu:             RGB = { red: 150, green: 150, blue: 100 };
```

## PageItem - Parameter  
### colorScale  

![image](https://user-images.githubusercontent.com/102996011/215083583-a4fca20b-6994-4146-b8e1-b484dfcaed91.png)  
 
innerhalb des PageItems kann das Icon im Alias des Gerätetypen "info" ebenfalls einen Indikatorwert annehmen:  
> _**Wenn colorScale im PageItem vorhanden ist, werden gesetzte `offColor` und `onColor` dabei ignoriert. Es wird dann auschließlich der Parameter colorScale ausgewertet.**_
```typescript  
colorScale: {'val_min': 0, 'val_max': 100, 'val_best': 50 }  
```
> _**val_best ist hierbei Optional und stellt den Idealwert dar!**_ 

weiter Beispiele:
```typescript  
<PageItem>{ id: AliasPath + 'Tasmota.Wifi.RSSI', name: 'RSSI', icon: 'signal', unit: '%', colorScale: {'val_min': 100, 'val_max': 0} },
<PageItem>{ id: AliasPath + 'Tasmota.Wifi.Signal', name: 'Wifi-Signal', icon: 'signal-distance-variant', unit: 'dBm', colorScale: {'val_min': 0, 'val_max': -100} },
<PageItem>{ id: AliasPath + 'Sensor.ANALOG.Temperature', name: 'Raum Temperatur', icon: 'home-thermometer-outline', unit: '°C', colorScale: {'val_min': 0, 'val_max': 40, 'val_best': 22 } },
<PageItem>{ id: AliasPath + 'Sensor.ESP32.Temperature', name: 'ESP Temperatur', icon: 'thermometer', unit: '°C', colorScale: {'val_min': 0, 'val_max': 100, 'val_best': 50 } },
```

## TypeScript (NSPanel.ts) Variablendefinition

nachfolgend die Seiten- und Menüdefinition aus dem TS-Script ab v4.3.1 
```typescript  
/***********************************************************************************************
 **  Service Pages mit Auto-Alias (Nachfolgende Seiten werden mit Alias automatisch angelegt) **
 **  https://github.com/joBr99/nspanel-lovelace-ui/wiki/NSPanel-Service-Men%C3%BC             **
 ***********************************************************************************************/

/* Wenn das Service Menü abgesichert werden soll, kann eine cardUnlock vorgeschaltet werden. 
   Für diesen Fall ist folgende Vorgehensweise erforderlich:
   - cardUnlock Seite "Unlock_Service" in der Config unter pages auskommentieren ("//" entfernen)
   - Servicemenü aus pages "NSPanel_Service" unter pages kommentieren ("//" hinzufügen)
*/ 

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

//Level_0 (if service pages are used without cardUnlock)
let NSPanel_Service = <PageEntities>
{
    'type': 'cardEntities',
    'heading': 'NSPanel Service',
    'useColor': true,
    'items': [
        <PageItem>{ navigate: true, id: 'NSPanel_Infos', icon: 'information-outline', offColor: Menu, onColor: Menu, name: 'Infos', buttonText: 'mehr...'},
        <PageItem>{ navigate: true, id: 'NSPanel_Einstellungen', icon: 'monitor-edit', offColor: Menu, onColor: Menu, name: 'Einstellungen', buttonText: 'mehr...'},
        <PageItem>{ navigate: true, id: 'NSPanel_Firmware', icon: 'update', offColor: Menu, onColor: Menu, name: 'Firmware', buttonText: 'mehr...'},
        <PageItem>{ id: AliasPath + 'Config.rebootNSPanel', name: 'Reboot NSPanel' ,icon: 'refresh', offColor: MSRed, onColor: MSGreen, buttonText: 'Start'},
    ]
};

//Level_0 (if service pages are used with cardUnlock)
let NSPanel_Service_SubPage = <PageEntities>
{
    'type': 'cardEntities',
    'heading': 'NSPanel Service',
    'useColor': true,
    'subPage': true,
    'parent': Unlock_Service,
    'home': 'Unlock_Service', 
    'items': [
        <PageItem>{ navigate: true, id: 'NSPanel_Infos', icon: 'information-outline', offColor: Menu, onColor: Menu, name: 'Infos', buttonText: 'mehr...'},
        <PageItem>{ navigate: true, id: 'NSPanel_Einstellungen', icon: 'monitor-edit', offColor: Menu, onColor: Menu, name: 'Einstellungen', buttonText: 'mehr...'},
        <PageItem>{ navigate: true, id: 'NSPanel_Firmware', icon: 'update', offColor: Menu, onColor: Menu, name: 'Firmware', buttonText: 'mehr...'},
        <PageItem>{ id: AliasPath + 'Config.rebootNSPanel', name: 'Reboot NSPanel' ,icon: 'refresh', offColor: MSRed, onColor: MSGreen, buttonText: 'Start'},
    ]
};

        //Level_1
        let NSPanel_Infos = <PageEntities>
        {
            'type': 'cardEntities',
            'heading': 'NSPanel Infos',
            'useColor': true,
            'subPage': true,
            'parent': NSPanel_Service,
            'home': 'NSPanel_Service',        
            'items': [
                <PageItem>{ navigate: true, id: 'NSPanel_Wifi_Info_1', icon: 'wifi', offColor: Menu, onColor: Menu, name: 'Wifi/WLAN', buttonText: 'mehr...'},
                <PageItem>{ navigate: true, id: 'NSPanel_Sensoren', icon: 'memory', offColor: Menu, onColor: Menu, name: 'Sensoren/Hardware', buttonText: 'mehr...'}
            ]
        };
                //Level_2
                let NSPanel_Wifi_Info_1 = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': 'NSPanel Wifi (1)',
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Infos,
                    'next': 'NSPanel_Wifi_Info_2',
                    'items': [
                        <PageItem>{ id: AliasPath + 'ipAddress', name: 'IP-Adresse', icon: 'ip-network-outline', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.BSSId', name: 'MAC Adresse', icon: 'check-network', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.RSSI', name: 'RSSI', icon: 'signal', unit: '%', colorScale: {'val_min': 100, 'val_max': 0} },
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.Signal', name: 'Wifi-Signal', icon: 'signal-distance-variant', unit: 'dBm', colorScale: {'val_min': 0, 'val_max': -100} },
                    ]
                };

                let NSPanel_Wifi_Info_2 = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': 'NSPanel Wifi (2)',
                    'useColor': true,
                    'subPage': true,
                    'prev': 'NSPanel_Wifi_Info_1',
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: 'alias.0.Test.Wiki_SSID', name: 'SSId', icon: 'signal-distance-variant', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.Mode', name: 'Modus', icon: 'signal-distance-variant', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.Channel', name: 'Kanal', icon: 'timeline-clock-outline', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.AP', name: 'AP', icon: 'router-wireless-settings', offColor: Menu, onColor: Menu },
                    ]
                };

                let NSPanel_Sensoren = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': 'Sensoren (1)',
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Infos,
                    'next': 'NSPanel_Hardware',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Sensor.ANALOG.Temperature', name: 'Raum Temperatur', icon: 'home-thermometer-outline', unit: '°C', colorScale: {'val_min': 0, 'val_max': 40, 'val_best': 22 } },
                        <PageItem>{ id: AliasPath + 'Sensor.ESP32.Temperature', name: 'ESP Temperatur', icon: 'thermometer', unit: '°C', colorScale: {'val_min': 0, 'val_max': 100, 'val_best': 50 } },
                        <PageItem>{ id: AliasPath + 'Sensor.TempUnit', name: 'Temperatur Einheit', icon: 'temperature-celsius', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Sensor.Time', name: 'Aktualisierung', icon: 'clock-check-outline', offColor: Menu, onColor: Menu },
                    ]
                };

                let NSPanel_Hardware = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': 'Hardware (2)',
                    'useColor': true,
                    'subPage': true,
                    'prev': 'NSPanel_Sensoren',
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Tasmota.Product', name: 'Produkt', icon: 'devices', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Hardware', name: 'ESP32 Hardware', icon: 'memory', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Display.Model', name: 'NSPanel Version', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Uptime', name: 'Betriebszeit', icon: 'timeline-clock-outline', offColor: Menu, onColor: Menu },
                    ]
                };

        //Level_1
        let NSPanel_Einstellungen = <PageGrid>
            {
                'type': 'cardGrid',
                'heading': 'Einstellungen',
                'useColor': true,
                'subPage': true,
                'parent': NSPanel_Service,
                'home': 'NSPanel_Service',
                'items': [
                    <PageItem>{ navigate: true, id: 'NSPanel_Screensaver', icon: 'monitor-dashboard',offColor: Menu, onColor: Menu, name: 'Screensaver', buttonText: 'mehr...'},
                    <PageItem>{ navigate: true, id: 'NSPanel_Relays', icon: 'electric-switch', offColor: Menu, onColor: Menu, name: 'Relais', buttonText: 'mehr...'},
                    <PageItem>{ id:AliasPath + 'Config.temperatureUnitNumber', icon: 'gesture-double-tap', name: 'Temp. Einheit', offColor: Menu, onColor: Menu, 
                    modeList: ['°C', '°F', 'K']},
                    <PageItem>{ id: AliasPath + 'Config.localeNumber', icon: 'select-place', name: 'Sprache', offColor: Menu, onColor: Menu, 
                    modeList: ['en-US', 'de-DE', 'nl-NL', 'da-DK', 'es-ES', 'fr-FR', 'it-IT', 'ru-RU', 'nb-NO', 'nn-NO', 'pl-PL', 'pt-PT', 'af-ZA', 'ar-SY', 
                               'bg-BG', 'ca-ES', 'cs-CZ', 'el-GR', 'et-EE', 'fa-IR', 'fi-FI', 'he-IL', 'hr-xx', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'lb-xx', 
                               'lt-LT', 'ro-RO', 'sk-SK', 'sl-SI', 'sv-SE', 'th-TH', 'tr-TR', 'uk-UA', 'vi-VN', 'zh-CN', 'zh-TW']},
                   <PageItem>{ navigate: true, id: 'NSPanel_Script', icon: 'code-json',offColor: Menu, onColor: Menu, name: 'Script', buttonText: 'mehr...'},            
                ]
            };

                //Level_2
                let NSPanel_Screensaver = <PageGrid>
                {
                    'type': 'cardGrid',
                    'heading': 'Einstellungen',
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Einstellungen,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverDimmode', icon: 'sun-clock', offColor: Menu, onColor: Menu, name: 'Dimmode'},
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverBrightness', icon: 'brightness-5', offColor: Menu, onColor: Menu, name: 'Brightness'},
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverLayout', icon: 'page-next-outline', offColor: Menu, onColor: Menu, name: 'Layout'},
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverWeather', icon: 'weather-partly-rainy', offColor: Menu, onColor: Menu, name: 'Wetter'},
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverDateformat', icon: 'calendar-expand-horizontal', offColor: Menu, onColor: Menu, name: 'Datumsformat'},
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverIndicators', icon: 'monitor-edit', offColor: Menu, onColor: Menu, name: 'Indikatoren'}
                    ]
                };
                            
                        //Level_3
                        let NSPanel_ScreensaverDimmode = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': 'Dimmode',
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'Dimmode.brightnessDay', name: 'Brightness Tag', icon: 'brightness-5', offColor: Menu, onColor: Menu, minValue: 5, maxValue: 10},
                                <PageItem>{ id: AliasPath + 'Dimmode.brightnessNight', name: 'Brightness Nacht', icon: 'brightness-4', offColor: Menu, onColor: Menu, minValue: 0, maxValue: 4},
                                <PageItem>{ id: AliasPath + 'Dimmode.hourDay', name: 'Stunde Tag', icon: 'sun-clock', offColor: Menu, onColor: Menu, minValue: 0, maxValue: 23},
                                <PageItem>{ id: AliasPath + 'Dimmode.hourNight', name: 'Stunde Nacht', icon: 'sun-clock-outline', offColor: Menu, onColor: Menu, minValue: 0, maxValue: 23}
                            ]
                        };

                        //Level_3
                        let NSPanel_ScreensaverBrightness = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': 'Brightness',
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.activeBrightness', name: 'Helligkeit Aktiv', icon: 'brightness-5', offColor: Menu, onColor: Menu, minValue: 20, maxValue: 100},
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.timeoutScreensaver', name: 'Screensaver Timeout', icon: 'clock-end', offColor: Menu, onColor: Menu, minValue: 0, maxValue: 60},
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.screenSaverDoubleClick', name: 'Doppelklick Weakup' ,icon: 'gesture-two-double-tap', offColor: HMIOff, onColor: HMIOn}
                            ]
                        };

                        //Level_3
                        let NSPanel_ScreensaverLayout = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': 'Layout',
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.alternativeScreensaverLayout', name: 'Alternativ Layout' ,icon: 'page-previous-outline', offColor: HMIOff, onColor: HMIOn},
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.ScreensaverAdvanced', name: 'Advanced Layout' ,icon: 'page-next-outline', offColor: HMIOff, onColor: HMIOn},
                            ]
                        };

                        //Level_3
                        let NSPanel_ScreensaverWeather = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': 'Wetter Parameter',
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.weatherForecast', name: 'Vorhersage Aus/An' ,icon: 'weather-sunny-off', offColor: HMIOff, onColor: HMIOn},
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.weatherForecastTimer', name: 'Vorhersage Wechsel' ,icon: 'devices', offColor: HMIOff, onColor: HMIOn},
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.entityChangeTime', name: 'Wechselzeit/s', icon: 'cog-sync', offColor: Menu, onColor: Menu, minValue: 15, maxValue: 60},
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.autoWeatherColorScreensaverLayout', name: 'Symbolfarben' ,icon: 'format-color-fill', offColor: HMIOff, onColor: HMIOn},
                            ]
                        };

                        //Level_3
                        let NSPanel_ScreensaverDateformat = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': 'Datumsformat',
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'Config.Dateformat.Switch.weekday', name: 'Wochentag (lang)' ,icon: 'calendar-expand-horizontal', offColor: HMIOff, onColor: HMIOn},
                                <PageItem>{ id: AliasPath + 'Config.Dateformat.Switch.month', name: 'Monat (lang)' ,icon: 'calendar-expand-horizontal', offColor: HMIOff, onColor: HMIOn},
                            ]
                        };

                        //Level_3
                        let NSPanel_ScreensaverIndicators = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': 'Indikatoren',
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'Config.MRIcons.alternateMRIconSize.1', name: 'Icon 1 (klein/groß)' ,icon: 'format-size', offColor: HMIOff, onColor: HMIOn},
                                <PageItem>{ id: AliasPath + 'Config.MRIcons.alternateMRIconSize.2', name: 'Icon 2 (klein/groß)' ,icon: 'format-size', offColor: HMIOff, onColor: HMIOn},
                            ]
                        };

                //Level_2
                let NSPanel_Relays = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': 'Relais',
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Einstellungen,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Relay.1', name: 'Relais 1 (aus/an)' ,icon: 'power', offColor: HMIOff, onColor: HMIOn},
                        <PageItem>{ id: AliasPath + 'Relay.2', name: 'Relais 2 (aus/an)' ,icon: 'power', offColor: HMIOff, onColor: HMIOn},
                    ]
                };

                //Level_2
                let NSPanel_Script = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': 'Script',
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Einstellungen,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Config.ScripgtDebugStatus', name: 'Debugmode (aus/an)' ,icon: 'code-tags-check', offColor: HMIOff, onColor: HMIOn},
                        <PageItem>{ id: AliasPath + 'Config.MQTT.portCheck', name: 'Port-Check (aus/an)' ,icon: 'check-network', offColor: HMIOff, onColor: HMIOn},
                    ]
                };

        //Level_1
        let NSPanel_Firmware = <PageEntities>
            {
                'type': 'cardEntities',
                'heading': 'Firmware',
                'useColor': true,
                'subPage': true,
                'parent': NSPanel_Service,
                'home': 'NSPanel_Service',
                'items': [
                    <PageItem>{ id: AliasPath + 'autoUpdate', name: 'Auto-Updates' ,icon: 'power', offColor: HMIOff, onColor: HMIOn},
                    <PageItem>{ navigate: true, id: 'NSPanel_FirmwareTasmota', icon: 'usb-flash-drive', offColor: Menu, onColor: Menu, name: 'Tasmota Firmware', buttonText: 'mehr...'},
                    <PageItem>{ navigate: true, id: 'NSPanel_FirmwareBerry', icon: 'usb-flash-drive', offColor: Menu, onColor: Menu, name: 'Berry-Driver', buttonText: 'mehr...'},
                    <PageItem>{ navigate: true, id: 'NSPanel_FirmwareNextion', icon: 'cellphone-cog', offColor: Menu, onColor: Menu, name: 'Nextion TFT', buttonText: 'mehr...'}
                ]
            };

                let NSPanel_FirmwareTasmota = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': 'Tasmota',
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Firmware,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Tasmota.Version', name: 'Installierte Version', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota_Firmware.onlineVersion', name: 'Verfügbare Version', offColor: Menu, onColor: Menu },                        
                        <PageItem>{ id: 'Divider' },
                        <PageItem>{ id: AliasPath + 'Config.Update.UpdateTasmota', name: 'Tasmota Update' ,icon: 'refresh', offColor: HMIOff, onColor: MSGreen, buttonText: 'Start'},
                    ]
                };

                let NSPanel_FirmwareBerry = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': 'Berry-Driver',
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Firmware,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Display.BerryDriver', name: 'Installierte Version', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Berry_Driver.onlineVersion', name: 'Verfügbare Version', offColor: Menu, onColor: Menu},                        
                        <PageItem>{ id: 'Divider' },
                        <PageItem>{ id: AliasPath + 'Config.Update.UpdateBerry', name: 'Berry-Driver Update' ,icon: 'refresh', offColor: HMIOff, onColor: MSGreen, buttonText: 'Start'},
                    ]
                };

                let NSPanel_FirmwareNextion = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': 'Nextion TFT',
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Firmware,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Display_Firmware.TFT.currentVersion', name: 'Installierte Version', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Display_Firmware.TFT.desiredVersion', name: 'Benötigte Version', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Display.Model', name: 'NSPanel Version', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Config.Update.UpdateNextion', name: 'Nextion TFT Update' ,icon: 'refresh', offColor: HMIOff, onColor: MSGreen, buttonText: 'Start'},
                    ]
                };

// Ende der Service Pages

```

## TypeScript (NSPanel.ts) Config  
```typescript  
export const config = <Config> {
    
    ...
    Config Parameter
    ...
    
    pages: [
            ...
            Diverse Top Level Pages
            ...

            //Unlock_Service,         //Servicemenü mit cardUnlock
            NSPanel_Service         //Servicemenü ohne cardUnlock
    ],
    subPages: [
                ...
                Diverse Subpages
                ...

                NSPanel_Service_SubPage,                //Auto-Alias Service Page (used with cardUnlock)
                NSPanel_Infos,                          //Auto-Alias Service Page
                    NSPanel_Wifi_Info_1,                //Auto-Alias Service Page
                    NSPanel_Wifi_Info_2,                //Auto-Alias Service Page
                    NSPanel_Sensoren,                   //Auto-Alias Service Page
                    NSPanel_Hardware,                   //Auto-Alias Service Page
                NSPanel_Einstellungen,                  //Auto-Alias Service Page
                    NSPanel_Screensaver,                //Auto-Alias Service Page
                        NSPanel_ScreensaverDimmode,     //Auto-Alias Service Page
                        NSPanel_ScreensaverBrightness,  //Auto-Alias Service Page
                        NSPanel_ScreensaverLayout,      //Auto-Alias Service Page
                        NSPanel_ScreensaverWeather,     //Auto-Alias Service Page
                        NSPanel_ScreensaverDateformat,  //Auto-Alias Service Page
                        NSPanel_ScreensaverIndicators,  //Auto-Alias Service Page
                    NSPanel_Relays,                     //Auto-Alias Service Page
                    NSPanel_Script,                     //Auto-Alias Service Page
                NSPanel_Firmware,                       //Auto-Alias Service Page
                    NSPanel_FirmwareTasmota,            //Auto-Alias Service Page
                    NSPanel_FirmwareBerry,              //Auto-Alias Service Page
                    NSPanel_FirmwareNextion,            //Auto-Alias Service Page
    ],
    button1: {
        mode: null,     // Mögliche Werte wenn Rule2 definiert: 'page', 'toggle', 'set' - Wenn nicht definiert --> mode: null
        page: null,     // Zielpage - Verwendet wenn mode = page (bisher button1Page)
        entity: null,   // Zielentity - Verwendet wenn mode = set oder toggle
        setValue: null  // Zielwert - Verwendet wenn mode = set
    },
    button2: {
        mode: null,     // Mögliche Werte wenn Rule2 definiert: 'page', 'toggle', 'set' - Wenn nicht definiert --> mode: null
        page: null,     // Zielpage - Verwendet wenn mode = page (bisher button2Page)
        entity: null,   // Zielentity - Verwendet wenn mode = set oder toggle
        setValue: null  // Zielwert - Verwendet wenn mode = set
    }
};

```