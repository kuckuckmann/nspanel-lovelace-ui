# Servicemenü  

> ab v3.9.0  

**Das Menü ist in den Variablendefinitionen des TS-Script v3.9.0 enthalten, dient als Beispiel für eine Subpage-Gestaltung und kann beliebig angepasst werden. Die Aliase für dieses Beispiel legt das TS-Script, sofern setOption in der JavaScript-Adapter-Instanz angehakt ist, automatisch an.**  
Im Zuge der weiteren Releases wird es sukzessive um künftige Funktionalitäten erweitert

## Service-Menü-Beispiel aus dem TypeScript (NSPanel.ts)   
![Nextion_Editor_jc3M2TasjY](https://user-images.githubusercontent.com/102996011/215077776-20e7a3f8-3a87-43c4-ae24-7e237e0a9646.gif) 

## Aufbau des Service-Menüs  

![image](https://user-images.githubusercontent.com/102996011/213807909-c7d3ce47-4f0d-48af-b3e9-437c44b2f95b.png)  

##  TypeScript (NSPanel.ts) Variablendefinition

nachfolgend die Seiten- und Menüdefinition aus dem TS-Script ab v3.9.0 
```
/***********************************************************************************************
 **  Service Pages mit Auto-Alias (Nachfolgende Seiten werden mit Alias automatisch angelegt) **
 **  https://github.com/joBr99/nspanel-lovelace-ui/wiki/NSPanel-Service-Men%C3%BC             **
 ***********************************************************************************************/

//Level_0 
let NSPanel_Service = <PageEntities>
{
    'type': 'cardEntities',
    'heading': 'NSPanel Service',
    'useColor': true,
    'items': [
        <PageItem>{ navigate: true, id: 'NSPanel_Infos', icon: 'information-outline', onColor: MSYellow, name: 'Infos', buttonText: 'mehr...'},
        <PageItem>{ navigate: true, id: 'NSPanel_Einstellungen', icon: 'monitor-edit', onColor: MSYellow, name: 'Einstellungen', buttonText: 'mehr...'},
        <PageItem>{ navigate: true, id: 'NSPanel_Firmware', icon: 'update', onColor: MSYellow, name: 'Firmware', buttonText: 'mehr...'},
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
                <PageItem>{ navigate: true, id: 'NSPanel_Wifi_Info_1', icon: 'wifi', onColor: MSYellow, name: 'Wifi/WLAN', buttonText: 'mehr...'},
                <PageItem>{ navigate: true, id: 'NSPanel_Sensoren', icon: 'memory', onColor: MSYellow, name: 'Sensoren/Hardware', buttonText: 'mehr...'}
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
                        <PageItem>{ id: AliasPath + 'ipAddress', name: 'IP-Adresse', icon: 'ip-network-outline', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.BSSId', name: 'MAC Adresse', icon: 'check-network', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.RSSI', name: 'RSSI', icon: 'signal', unit: '%', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.Signal', name: 'Wifi-Signal', icon: 'signal-distance-variant', unit: 'dBm', offColor: MSYellow, onColor: MSYellow, useColor: true},
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
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.SSId', name: 'SSId', icon: 'signal-distance-variant', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.Mode', name: 'Modus', icon: 'signal-distance-variant', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.Channel', name: 'Kanal', icon: 'timeline-clock-outline', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.AP', name: 'AP', icon: 'router-wireless-settings', offColor: MSYellow, onColor: MSYellow, useColor: true},
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
                        <PageItem>{ id: AliasPath + 'Sensor.ANALOG.Temperature', name: 'Raum Temperatur', icon: 'home-thermometer-outline', unit: '°C', offColor: MSYellow, onColor: MSYellow},
                        <PageItem>{ id: AliasPath + 'Sensor.ESP32.Temperature', name: 'ESP Temperatur', icon: 'thermometer', unit: '°C', offColor: MSYellow, onColor: MSYellow},
                        <PageItem>{ id: AliasPath + 'Sensor.TempUnit', name: 'Temperatur Einheit', icon: 'temperature-celsius', offColor: MSYellow, onColor: MSYellow},
                        <PageItem>{ id: AliasPath + 'Sensor.Time', name: 'Aktualisierung', icon: 'clock-check-outline', offColor: MSYellow, onColor: MSYellow},
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
                        <PageItem>{ id: AliasPath + 'Tasmota.Product', name: 'Produkt', icon: 'devices', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Tasmota.Hardware', name: 'ESP32 Hardware', icon: 'memory', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Display.Model', name: 'NSPanel Version', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Tasmota.Uptime', name: 'Betriebszeit', icon: 'timeline-clock-outline', offColor: MSYellow, onColor: MSYellow, useColor: true},
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
                    <PageItem>{ navigate: true, id: 'NSPanel_Screensaver', icon: 'monitor-dashboard', onColor: MSYellow, name: 'Screensaver', buttonText: 'mehr...'},
                    <PageItem>{ navigate: true, id: 'NSPanel_Relays', icon: 'electric-switch', onColor: MSYellow, name: 'Relais', buttonText: 'mehr...'},
                    <PageItem>{ id:AliasPath + 'Config.temperatureUnitNumber', icon: 'gesture-double-tap', name: 'Temp. Einheit', onColor: MSYellow, 
                    modeList: ['°C', '°F', 'K']},
                    <PageItem>{ id: AliasPath + 'Config.localeNumber', icon: 'select-place', name: 'Sprache', onColor: MSYellow, 
                    modeList: ['en-US', 'de-DE', 'nl-NL', 'da-DK', 'es-ES', 'fr-FR', 'it-IT', 'ru-RU', 'nb-NO', 'nn-NO', 'pl-PL', 'pt-PT', 'af-ZA', 'ar-SY', 
                               'bg-BG', 'ca-ES', 'cs-CZ', 'el-GR', 'et-EE', 'fa-IR', 'fi-FI', 'he-IL', 'hr-xx', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'lb-xx', 
                               'lt-LT', 'ro-RO', 'sk-SK', 'sl-SI', 'sv-SE', 'th-TH', 'tr-TR', 'uk-UA', 'vi-VN', 'zh-CN', 'zh-TW']},
                                
                ]
            };

                //Level_2
                let NSPanel_Screensaver = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': 'Einstellungen',
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Einstellungen,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverDimmode', icon: 'wifi', onColor: MSYellow, name: 'Dimmode/Sonstige', buttonText: 'mehr...'},
                        <PageItem>{ navigate: true, id: 'NSPanel_Weather', icon: 'weather-partly-rainy', onColor: MSYellow, name: 'Wetter', buttonText: 'mehr...'},
                        <PageItem>{ navigate: true, id: 'NSPanel_Dateformat', icon: 'calendar-expand-horizontal', onColor: MSYellow, name: 'Datumsformat', buttonText: 'mehr...'},
                        <PageItem>{ navigate: true, id: 'NSPanel_Indicators', icon: 'monitor-edit', onColor: MSYellow, name: 'Indikatoren', buttonText: 'mehr...'}
                    ]
                };
                            
                        //Level_3
                        let NSPanel_ScreensaverDimmode = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': 'Dimmode (1)',
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'next': 'NSPanel_ScreensaverOther',
                            'items': [
                                <PageItem>{ id: AliasPath + 'Dimmode.brightnessDay', name: 'Brightness Tag', icon: 'brightness-5', offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 5, maxValue: 10},
                                <PageItem>{ id: AliasPath + 'Dimmode.brightnessNight', name: 'Brightness Nacht', icon: 'brightness-4', offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 0, maxValue: 4},
                                <PageItem>{ id: AliasPath + 'Dimmode.hourDay', name: 'Stunde Tag', icon: 'sun-clock', offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 0, maxValue: 23},
                                <PageItem>{ id: AliasPath + 'Dimmode.hourNight', name: 'Stunde Nacht', icon: 'sun-clock-outline', offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 0, maxValue: 23}
                            ]
                        };

                        //Level_3
                        let NSPanel_ScreensaverOther = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': 'Sonstige (2)',
                            'useColor': true,
                            'subPage': true,
                            'prev': 'NSPanel_ScreensaverDimmode',
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.activeBrightness', name: 'Helligkeit Aktiv', icon: 'brightness-5', offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 20, maxValue: 100},
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.timeoutScreensaver', name: 'Screensaver Timeout', icon: 'clock-end', offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 0, maxValue: 60},
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.screenSaverDoubleClick', name: 'Doppelklick Weakup' ,icon: 'gesture-two-double-tap', offColor: HMIOff, onColor: On},                                            
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.alternativeScreensaverLayout', name: 'Alternativ Layout' ,icon: 'page-previous-outline', offColor: HMIOff, onColor: On},            
                            ]
                        };

                        //Level_3
                        let NSPanel_Weather = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': 'Wetter Parameter',
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.weatherForecast', name: 'Vorhersage Aus/An' ,icon: 'weather-sunny-off', offColor: HMIOff, onColor: On},
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.weatherForecastTimer', name: 'Vorhersage Wechsel' ,icon: 'devices', offColor: HMIOff, onColor: On},
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.entityChangeTime', name: 'Wechselzeit/s', icon: 'cog-sync', offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 15, maxValue: 60},
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.autoWeatherColorScreensaverLayout', name: 'Symbolfarben' ,icon: 'format-color-fill', offColor: HMIOff, onColor: On},
                            ]
                        };

                        //Level_3
                        let NSPanel_Dateformat = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': 'Datumsformat',
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'Config.Dateformat.Switch.weekday', name: 'Wochentag (lang)' ,icon: 'calendar-expand-horizontal', offColor: HMIOff, onColor: On},
                                <PageItem>{ id: AliasPath + 'Config.Dateformat.Switch.month', name: 'Monat (lang)' ,icon: 'calendar-expand-horizontal', offColor: HMIOff, onColor: On},
                            ]
                        };

                        //Level_3
                        let NSPanel_Indicators = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': 'Indikatoren',
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'Config.MRIcons.alternateMRIconSize.1', name: 'Icon 1 (klein/groß)' ,icon: 'format-size', offColor: HMIOff, onColor: On},
                                <PageItem>{ id: AliasPath + 'Config.MRIcons.alternateMRIconSize.2', name: 'Icon 2 (klein/groß)' ,icon: 'format-size', offColor: HMIOff, onColor: On},
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
                        <PageItem>{ id: AliasPath + 'Relay.1', name: 'Relais 1 (aus/an)' ,icon: 'power', offColor: HMIOff, onColor: On},
                        <PageItem>{ id: AliasPath + 'Relay.2', name: 'Relais 2 (aus/an)' ,icon: 'power', offColor: HMIOff, onColor: On},
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
                    <PageItem>{ id: AliasPath + 'autoUpdate', name: 'Auto-Updates' ,icon: 'power', offColor: HMIOff, onColor: MSGreen},
                    <PageItem>{ navigate: true, id: 'NSPanel_FirmwareTasmota', icon: 'usb-flash-drive', onColor: MSYellow, name: 'Tasmota Firmware', buttonText: 'mehr...'},
                    <PageItem>{ navigate: true, id: 'NSPanel_FirmwareBerry', icon: 'usb-flash-drive', onColor: MSYellow, name: 'Berry-Driver', buttonText: 'mehr...'},
                    <PageItem>{ navigate: true, id: 'NSPanel_FirmwareNextion', icon: 'cellphone-cog', onColor: MSYellow, name: 'Nextion TFT', buttonText: 'mehr...'}
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
                        <PageItem>{ id: AliasPath + 'Tasmota.Version', name: 'Installierte Version', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Tasmota_Firmware.onlineVersion', name: 'Verfügbare Version', offColor: MSYellow, onColor: MSYellow, useColor: true},                        
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
                        <PageItem>{ id: AliasPath + 'Display.BerryDriver', name: 'Installierte Version', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Berry_Driver.onlineVersion', name: 'Verfügbare Version', offColor: MSYellow, onColor: MSYellow, useColor: true},                        
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
                        <PageItem>{ id: AliasPath + 'Display_Firmware.TFT.currentVersion', name: 'Installierte Version', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Display_Firmware.TFT.desiredVersion', name: 'Benötigte Version', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Display.Model', name: 'NSPanel Version', offColor: MSYellow, onColor: MSYellow, useColor: true},
                        <PageItem>{ id: AliasPath + 'Config.Update.UpdateNextion', name: 'Nextion TFT Update' ,icon: 'refresh', offColor: HMIOff, onColor: MSGreen, buttonText: 'Start'},
                    ]
                };
```

## TypeScript (NSPanel.ts) Config  
```
export const config: Config = {
    
    ...
    Config Parameter
    ...
    
    pages: [
            ...
            Diverse Top Level Pages
            ...
            
            NSPanel_Service         //Auto-Alias Service Page
    ],
    subPages: [
                ...
                Diverse Subpages
                ...

                NSPanel_Infos,                          //Auto-Alias Service Page
                    NSPanel_Wifi_Info_1,                //Auto-Alias Service Page
                    NSPanel_Wifi_Info_2,                //Auto-Alias Service Page
                    NSPanel_Sensoren,                   //Auto-Alias Service Page
                    NSPanel_Hardware,                   //Auto-Alias Service Page
                NSPanel_Einstellungen,                  //Auto-Alias Service Page
                    NSPanel_Screensaver,                //Auto-Alias Service Page
                        NSPanel_ScreensaverDimmode,     //Auto-Alias Service Page
                        NSPanel_ScreensaverOther,       //Auto-Alias Service Page
                        NSPanel_Weather,                //Auto-Alias Service Page
                        NSPanel_Dateformat,             //Auto-Alias Service Page
                        NSPanel_Indicators,             //Auto-Alias Service Page
                        NSPanel_Relays,                 //Auto-Alias Service Page
                NSPanel_Firmware,                       //Auto-Alias Service Page
                    NSPanel_FirmwareTasmota,            //Auto-Alias Service Page
                    NSPanel_FirmwareBerry,              //Auto-Alias Service Page
                    NSPanel_FirmwareNextion,            //Auto-Alias Service Page
    ],
    button1Page: button1Page,   //Beispiel-Seite auf Button 1, wenn Rule2 definiert - Wenn nicht definiert --> button1Page: null, 
    button2Page: button2Page    //Beispiel-Seite auf Button 2, wenn Rule2 definiert - Wenn nicht definiert --> button1Page: null,
};
```