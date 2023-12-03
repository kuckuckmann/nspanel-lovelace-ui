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

nachfolgend die Seiten- und Menüdefinition aus dem TS-Script ab v4.3.3 
```typescript  
/***********************************************************************************************
 **  Service Pages mit Auto-Alias (Nachfolgende Seiten werden mit Alias automatisch angelegt) **
 **  https://github.com/joBr99/nspanel-lovelace-ui/wiki/NSPanel-Service-Men%C3%BC             **
 ***********************************************************************************************/

/* DE: German
   Wenn das Service Menü abgesichert werden soll, kann eine cardUnlock vorgeschaltet werden. 
   Für diesen Fall ist folgende Vorgehensweise erforderlich:
   - cardUnlock Seite "Unlock_Service" in der Config unter pages auskommentieren ("//" entfernen)
   - Servicemenü aus pages "NSPanel_Service" unter pages kommentieren ("//" hinzufügen)
*/ 

/*************************************************************************************************
  ** Service pages with auto alias (subsequent pages are automatically created with alias)      **
  ** https://github.com/joBr99/nspanel-lovelace-ui/wiki/NSPanel-Service-Men%C3%BC               **
  ************************************************************************************************/

/* EN: English
    If the service menu needs to be secured, a cardUnlock can be installed upstream.
    In this case, the following procedure is required:
    - comment out cardUnlock page "Unlock_Service" in the config under pages (remove "//")
    - Comment service menu from pages "NSPanel_Service" under pages (add "//")
*/

//Level 0 (if service pages are used with cardUnlock)
let Unlock_Service = <PageUnlock>
{
    'type': 'cardUnlock',
    'heading': findLocaleServMenu('service_pages'),
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
    'heading': findLocaleServMenu('service_menu'),
    'useColor': true,
    'items': [
        <PageItem>{ navigate: true, id: 'NSPanel_Infos', icon: 'information-outline', offColor: Menu, onColor: Menu, name: findLocaleServMenu('infos'), buttonText: findLocaleServMenu('more')},
        <PageItem>{ navigate: true, id: 'NSPanel_Einstellungen', icon: 'monitor-edit', offColor: Menu, onColor: Menu, name: findLocaleServMenu('settings'), buttonText: findLocaleServMenu('more')},
        <PageItem>{ navigate: true, id: 'NSPanel_Firmware', icon: 'update', offColor: Menu, onColor: Menu, name: findLocaleServMenu('firmware'), buttonText: findLocaleServMenu('more')},
        <PageItem>{ id: AliasPath + 'Config.rebootNSPanel', name: findLocaleServMenu('reboot') ,icon: 'refresh', offColor: MSRed, onColor: MSGreen, buttonText: findLocaleServMenu('start')},
    ]
};

//Level_0 (if service pages are used with cardUnlock)
let NSPanel_Service_SubPage = <PageEntities>
{
    'type': 'cardEntities',
    'heading': findLocaleServMenu('service_menu'),
    'useColor': true,
    'subPage': true,
    'parent': Unlock_Service,
    'home': 'Unlock_Service', 
    'items': [
        <PageItem>{ navigate: true, id: 'NSPanel_Infos', icon: 'information-outline', offColor: Menu, onColor: Menu, name: findLocaleServMenu('infos'), buttonText: findLocaleServMenu('more')},
        <PageItem>{ navigate: true, id: 'NSPanel_Einstellungen', icon: 'monitor-edit', offColor: Menu, onColor: Menu, name: findLocaleServMenu('settings'), buttonText: findLocaleServMenu('more')},
        <PageItem>{ navigate: true, id: 'NSPanel_Firmware', icon: 'update', offColor: Menu, onColor: Menu, name: findLocaleServMenu('firmware'), buttonText: findLocaleServMenu('more')},
        <PageItem>{ id: AliasPath + 'Config.rebootNSPanel', name: findLocaleServMenu('reboot') ,icon: 'refresh', offColor: MSRed, onColor: MSGreen, buttonText: findLocaleServMenu('start')},
    ]
};

        //Level_1
        let NSPanel_Infos = <PageEntities>
        {
            'type': 'cardEntities',
            'heading': findLocaleServMenu('nspanel_infos'),
            'useColor': true,
            'subPage': true,
            'parent': NSPanel_Service,
            'home': 'NSPanel_Service',        
            'items': [
                <PageItem>{ navigate: true, id: 'NSPanel_Wifi_Info_1', icon: 'wifi', offColor: Menu, onColor: Menu, name: findLocaleServMenu('wifi'), buttonText: findLocaleServMenu('more')},
                <PageItem>{ navigate: true, id: 'NSPanel_Sensoren', icon: 'memory', offColor: Menu, onColor: Menu, name: findLocaleServMenu('sensors_hardware'), buttonText: findLocaleServMenu('more')},
                <PageItem>{ navigate: true, id: 'NSPanel_IoBroker', icon: 'information-outline', offColor: Menu, onColor: Menu, name: findLocaleServMenu('info_iobroker'), buttonText: findLocaleServMenu('more')}
            ]
        };
                //Level_2
                let NSPanel_Wifi_Info_1 = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': findLocaleServMenu('nspanel_wifi1'),
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Infos,
                    'next': 'NSPanel_Wifi_Info_2',
                    'items': [
                        <PageItem>{ id: AliasPath + 'ipAddress', name: findLocaleServMenu('ip_address'), icon: 'ip-network-outline', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.BSSId', name: findLocaleServMenu('mac_address'), icon: 'check-network', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.RSSI', name: findLocaleServMenu('rssi'), icon: 'signal', unit: '%', colorScale: {'val_min': 100, 'val_max': 0} },
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.Signal', name: findLocaleServMenu('wifi_signal'), icon: 'signal-distance-variant', unit: 'dBm', colorScale: {'val_min': 0, 'val_max': -100} },
                    ]
                };

                let NSPanel_Wifi_Info_2 = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': findLocaleServMenu('nspanel_wifi2'),
                    'useColor': true,
                    'subPage': true,
                    'prev': 'NSPanel_Wifi_Info_1',
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.SSId', name: findLocaleServMenu('ssid'), icon: 'signal-distance-variant', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.Mode', name: findLocaleServMenu('mode'), icon: 'signal-distance-variant', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.Channel', name: findLocaleServMenu('channel'), icon: 'timeline-clock-outline', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Wifi.AP', name: findLocaleServMenu('accesspoint'), icon: 'router-wireless-settings', offColor: Menu, onColor: Menu },
                    ]
                };

                let NSPanel_Sensoren = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': findLocaleServMenu('sensors1'),
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Infos,
                    'next': 'NSPanel_Hardware',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Sensor.ANALOG.Temperature', name: findLocaleServMenu('room_temperature'), icon: 'home-thermometer-outline', unit: '°C', colorScale: {'val_min': 0, 'val_max': 40, 'val_best': 22 } },
                        <PageItem>{ id: AliasPath + 'Sensor.ESP32.Temperature', name: findLocaleServMenu('esp_temperature'), icon: 'thermometer', unit: '°C', colorScale: {'val_min': 0, 'val_max': 100, 'val_best': 50 } },
                        <PageItem>{ id: AliasPath + 'Sensor.TempUnit', name: findLocaleServMenu('temperature_unit'), icon: 'temperature-celsius', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Sensor.Time', name: findLocaleServMenu('refresh'), icon: 'clock-check-outline', offColor: Menu, onColor: Menu },
                    ]
                };

                let NSPanel_Hardware = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': findLocaleServMenu('hardware2'),
                    'useColor': true,
                    'subPage': true,
                    'prev': 'NSPanel_Sensoren',
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Tasmota.Product', name: findLocaleServMenu('product'), icon: 'devices', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Hardware', name: findLocaleServMenu('esp32_hardware'), icon: 'memory', offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Display.Model', name: findLocaleServMenu('nspanel_version'), offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota.Uptime', name: findLocaleServMenu('operating_time'), icon: 'timeline-clock-outline', offColor: Menu, onColor: Menu },
                    ]
                };

                let NSPanel_IoBroker = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': findLocaleServMenu('info_iobroker'),
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Infos,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'IoBroker.ScriptVersion', name: findLocaleServMenu('script_version_nspanelts'), offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'IoBroker.NodeJSVersion', name: findLocaleServMenu('nodejs_version'), offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'IoBroker.JavaScriptVersion', name: findLocaleServMenu('instance_javascript'), offColor: Menu, onColor: Menu },
                    ]
                };

        //Level_1
        let NSPanel_Einstellungen = <PageGrid>
            {
                'type': 'cardGrid',
                'heading': findLocaleServMenu('settings'),
                'useColor': true,
                'subPage': true,
                'parent': NSPanel_Service,
                'home': 'NSPanel_Service',
                'items': [
                    <PageItem>{ navigate: true, id: 'NSPanel_Screensaver', icon: 'monitor-dashboard',offColor: Menu, onColor: Menu, name: findLocaleServMenu('screensaver'), buttonText: findLocaleServMenu('more')},
                    <PageItem>{ navigate: true, id: 'NSPanel_Relays', icon: 'electric-switch', offColor: Menu, onColor: Menu, name: findLocaleServMenu('relays'), buttonText: findLocaleServMenu('more')},
                    <PageItem>{ id:AliasPath + 'Config.temperatureUnitNumber', icon: 'gesture-double-tap', name: findLocaleServMenu('temp_unit'), offColor: Menu, onColor: Menu, 
                    modeList: ['°C', '°F', 'K']},
                    <PageItem>{ id: AliasPath + 'Config.localeNumber', icon: 'select-place', name: findLocaleServMenu('language'), offColor: Menu, onColor: Menu, 
                    modeList: ['en-US', 'de-DE', 'nl-NL', 'da-DK', 'es-ES', 'fr-FR', 'it-IT', 'ru-RU', 'nb-NO', 'nn-NO', 'pl-PL', 'pt-PT', 'af-ZA', 'ar-SY', 
                               'bg-BG', 'ca-ES', 'cs-CZ', 'el-GR', 'et-EE', 'fa-IR', 'fi-FI', 'he-IL', 'hr-xx', 'hu-HU', 'hy-AM', 'id-ID', 'is-IS', 'lb-xx', 
                               'lt-LT', 'ro-RO', 'sk-SK', 'sl-SI', 'sv-SE', 'th-TH', 'tr-TR', 'uk-UA', 'vi-VN', 'zh-CN', 'zh-TW']},
                   <PageItem>{ navigate: true, id: 'NSPanel_Script', icon: 'code-json',offColor: Menu, onColor: Menu, name: findLocaleServMenu('script'), buttonText: findLocaleServMenu('more')},            
                ]
            };

                //Level_2
                let NSPanel_Screensaver = <PageGrid>
                {
                    'type': 'cardGrid',
                    'heading': findLocaleServMenu('screensaver'),
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Einstellungen,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverDimmode', icon: 'sun-clock', offColor: Menu, onColor: Menu, name: findLocaleServMenu('dimmode')},
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverBrightness', icon: 'brightness-5', offColor: Menu, onColor: Menu, name: findLocaleServMenu('brightness')},
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverLayout', icon: 'page-next-outline', offColor: Menu, onColor: Menu, name: findLocaleServMenu('layout')},
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverWeather', icon: 'weather-partly-rainy', offColor: Menu, onColor: Menu, name: findLocaleServMenu('weather')},
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverDateformat', icon: 'calendar-expand-horizontal', offColor: Menu, onColor: Menu, name: findLocaleServMenu('date_format')},
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverIndicators', icon: 'monitor-edit', offColor: Menu, onColor: Menu, name: findLocaleServMenu('indicators')}
                    ]
                };
                            
                        //Level_3
                        let NSPanel_ScreensaverDimmode = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': findLocaleServMenu('dimmode'),
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'Dimmode.brightnessDay', name: findLocaleServMenu('brightness_day'), icon: 'brightness-5', offColor: Menu, onColor: Menu, minValue: 5, maxValue: 10},
                                <PageItem>{ id: AliasPath + 'Dimmode.brightnessNight', name: findLocaleServMenu('brightness_night'), icon: 'brightness-4', offColor: Menu, onColor: Menu, minValue: 0, maxValue: 4},
                                <PageItem>{ id: AliasPath + 'Dimmode.hourDay', name: findLocaleServMenu('hour_day'), icon: 'sun-clock', offColor: Menu, onColor: Menu, minValue: 0, maxValue: 23},
                                <PageItem>{ id: AliasPath + 'Dimmode.hourNight', name: findLocaleServMenu('hour_night'), icon: 'sun-clock-outline', offColor: Menu, onColor: Menu, minValue: 0, maxValue: 23}
                            ]
                        };

                        //Level_3
                        let NSPanel_ScreensaverBrightness = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': findLocaleServMenu('brightness'),
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.activeBrightness', name: findLocaleServMenu('brightness_activ'), icon: 'brightness-5', offColor: Menu, onColor: Menu, minValue: 20, maxValue: 100},
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.timeoutScreensaver', name: findLocaleServMenu('screensaver_timeout'), icon: 'clock-end', offColor: Menu, onColor: Menu, minValue: 0, maxValue: 60},
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.screenSaverDoubleClick', name: findLocaleServMenu('wakeup_doublecklick') ,icon: 'gesture-two-double-tap', offColor: HMIOff, onColor: HMIOn}
                            ]
                        };

                        //Level_3
                        let NSPanel_ScreensaverLayout = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': findLocaleServMenu('layout'),
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.alternativeScreensaverLayout', name: findLocaleServMenu('alternative_layout') ,icon: 'page-previous-outline', offColor: HMIOff, onColor: HMIOn},
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.ScreensaverAdvanced', name: findLocaleServMenu('advanced_layout') ,icon: 'page-next-outline', offColor: HMIOff, onColor: HMIOn},
                            ]
                        };

                        //Level_3
                        let NSPanel_ScreensaverWeather = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': findLocaleServMenu('weather_parameters'),
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.weatherForecast', name: findLocaleServMenu('weather_forecast_offon') ,icon: 'weather-sunny-off', offColor: HMIOff, onColor: HMIOn},
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.weatherForecastTimer', name: findLocaleServMenu('weather_forecast_change_switch') ,icon: 'devices', offColor: HMIOff, onColor: HMIOn},
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.entityChangeTime', name: findLocaleServMenu('weather_forecast_change_time'), icon: 'cog-sync', offColor: Menu, onColor: Menu, minValue: 15, maxValue: 60},
                                <PageItem>{ id: AliasPath + 'Config.Screensaver.autoWeatherColorScreensaverLayout', name: findLocaleServMenu('weather_forecast_icon_colors') ,icon: 'format-color-fill', offColor: HMIOff, onColor: HMIOn},
                            ]
                        };

                        //Level_3
                        let NSPanel_ScreensaverDateformat = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': findLocaleServMenu('date_format'),
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'Config.Dateformat.Switch.weekday', name: findLocaleServMenu('weekday_large') ,icon: 'calendar-expand-horizontal', offColor: HMIOff, onColor: HMIOn},
                                <PageItem>{ id: AliasPath + 'Config.Dateformat.Switch.month', name: findLocaleServMenu('month_large') ,icon: 'calendar-expand-horizontal', offColor: HMIOff, onColor: HMIOn},
                            ]
                        };

                        //Level_3
                        let NSPanel_ScreensaverIndicators = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': findLocaleServMenu('indicators'),
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'Config.MRIcons.alternateMRIconSize.1', name: findLocaleServMenu('mr_icon1_size') ,icon: 'format-size', offColor: HMIOff, onColor: HMIOn},
                                <PageItem>{ id: AliasPath + 'Config.MRIcons.alternateMRIconSize.2', name: findLocaleServMenu('mr_icon2_size') ,icon: 'format-size', offColor: HMIOff, onColor: HMIOn},
                            ]
                        };

                //Level_2
                let NSPanel_Relays = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': findLocaleServMenu('relays'),
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Einstellungen,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Relay.1', name: findLocaleServMenu('relay1_onoff'), icon: 'power', offColor: HMIOff, onColor: HMIOn},
                        <PageItem>{ id: AliasPath + 'Relay.2', name: findLocaleServMenu('relay2_onoff'), icon: 'power', offColor: HMIOff, onColor: HMIOn},
                    ]
                };

                //Level_2
                let NSPanel_Script = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': findLocaleServMenu('script'),
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Einstellungen,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Config.ScripgtDebugStatus', name: findLocaleServMenu('debugmode_offon') ,icon: 'code-tags-check', offColor: HMIOff, onColor: HMIOn},
                        <PageItem>{ id: AliasPath + 'Config.MQTT.portCheck', name: findLocaleServMenu('port_check_offon') ,icon: 'check-network', offColor: HMIOff, onColor: HMIOn},
                    ]
                };

        //Level_1
        let NSPanel_Firmware = <PageEntities>
            {
                'type': 'cardEntities',
                'heading': findLocaleServMenu('firmware'),
                'useColor': true,
                'subPage': true,
                'parent': NSPanel_Service,
                'home': 'NSPanel_Service',
                'items': [
                    <PageItem>{ id: AliasPath + 'autoUpdate', name: findLocaleServMenu('automatically_updates') ,icon: 'power', offColor: HMIOff, onColor: HMIOn},
                    <PageItem>{ navigate: true, id: 'NSPanel_FirmwareTasmota', icon: 'usb-flash-drive', offColor: Menu, onColor: Menu, name: findLocaleServMenu('tasmota_firmware'), buttonText: findLocaleServMenu('more')},
                    <PageItem>{ navigate: true, id: 'NSPanel_FirmwareBerry', icon: 'usb-flash-drive', offColor: Menu, onColor: Menu, name: findLocaleServMenu('berry_driver'), buttonText: findLocaleServMenu('more')},
                    <PageItem>{ navigate: true, id: 'NSPanel_FirmwareNextion', icon: 'cellphone-cog', offColor: Menu, onColor: Menu, name: findLocaleServMenu('nextion_tft_firmware'), buttonText: findLocaleServMenu('more')}
                ]
            };

                let NSPanel_FirmwareTasmota = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': findLocaleServMenu('tasmota'),
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Firmware,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Tasmota.Version', name: findLocaleServMenu('installed_release'), offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Tasmota_Firmware.onlineVersion', name: findLocaleServMenu('available_release'), offColor: Menu, onColor: Menu },                        
                        <PageItem>{ id: 'Divider' },
                        <PageItem>{ id: AliasPath + 'Config.Update.UpdateTasmota', name: findLocaleServMenu('update_tasmota') ,icon: 'refresh', offColor: HMIOff, onColor: MSGreen, buttonText: findLocaleServMenu('start')},
                    ]
                };

                let NSPanel_FirmwareBerry = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': findLocaleServMenu('berry_driver'),
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Firmware,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Display.BerryDriver', name: findLocaleServMenu('installed_release'), offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Berry_Driver.onlineVersion', name: findLocaleServMenu('available_release'), offColor: Menu, onColor: Menu},                        
                        <PageItem>{ id: 'Divider' },
                        <PageItem>{ id: AliasPath + 'Config.Update.UpdateBerry', name: findLocaleServMenu('update_berry_driver') ,icon: 'refresh', offColor: HMIOff, onColor: MSGreen, buttonText: findLocaleServMenu('start')},
                    ]
                };

                let NSPanel_FirmwareNextion = <PageEntities>
                {
                    'type': 'cardEntities',
                    'heading': findLocaleServMenu('nextion_tft'),
                    'useColor': true,
                    'subPage': true,
                    'parent': NSPanel_Firmware,
                    'home': 'NSPanel_Service',
                    'items': [
                        <PageItem>{ id: AliasPath + 'Display_Firmware.TFT.currentVersion', name: findLocaleServMenu('installed_release'), offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Display_Firmware.TFT.desiredVersion', name: findLocaleServMenu('desired_release'), offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Display.Model', name: findLocaleServMenu('nspanel_model'), offColor: Menu, onColor: Menu },
                        <PageItem>{ id: AliasPath + 'Config.Update.UpdateNextion', name: 'Nextion TFT Update' ,icon: 'refresh', offColor: HMIOff, onColor: MSGreen, buttonText: findLocaleServMenu('start')},
                    ]
                };

// End of Service Pages

```

## TypeScript (NSPanel.ts) Config  
```typescript  
export const config = <Config> {

    // Seiteneinteilung / Page division
    // Hauptseiten / Mainpages
    pages: [

        NSPanel_Service,         	//Auto-Alias Service Page
	    //Unlock_Service            //Auto-Alias Service Page (Service Pages used with cardUnlock)
    ],

    // Unterseiten / Subpages
    subPages: [
	    
                NSPanel_Service_SubPage,                //Auto-Alias Service Page (only used with cardUnlock)
                NSPanel_Infos,                          //Auto-Alias Service Page
                    NSPanel_Wifi_Info_1,                //Auto-Alias Service Page
                    NSPanel_Wifi_Info_2,                //Auto-Alias Service Page
                    NSPanel_Sensoren,                   //Auto-Alias Service Page
                    NSPanel_Hardware,                   //Auto-Alias Service Page
                    NSPanel_IoBroker,                   //Auot-Alias Service Page
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


```