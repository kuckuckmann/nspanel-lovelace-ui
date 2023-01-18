# Servicemenü

ab v3.9.0

## Menü-Beispiel aus dem TS-Script
![Nextion_Editor_nK462BYmWw](https://user-images.githubusercontent.com/102996011/213283615-860de2a8-1e1b-4d09-892c-c2119aba234c.gif)

Das Menü ist in den Variablendefinitionen des TS-Script enthalten, dient als Beispiel für eine Subpage-Gestaltung und kann beliebig angepasst werden. Die Aliase für dieses Beispiel legt das TS-Script, sofern setOption in der JavaScript-Adapter-Instanz angehakt ist, automatisch an.

## Menüaufbau




## Variablendefinition des Beispiel-Service Menüs
```
/********************************************************************************************************** */
//Service Pages mit Auto-Alias (Nachfolgende Seiten werden mit Alias automatisch angelegt)
/********************************************************************************************************** */

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
        <PageItem>{ id: AliasPath + 'Config.rebootNSPanel', name: 'Reboot NSPanel' ,icon: 'refresh', offColor: White, onColor: MSGreen, buttonText: 'Start'},
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
                    'home': 'NSPanel_Service',
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
                    'parent': NSPanel_Infos,
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
                    'heading': 'Sensoren',
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
                    'heading': 'Hardware',
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
        let NSPanel_Einstellungen = <PageEntities>
            {
                'type': 'cardEntities',
                'heading': 'Einstellungen',
                'useColor': true,
                'subPage': true,
                'parent': NSPanel_Service,
                'home': 'NSPanel_Service',
                'items': [
                    <PageItem>{ navigate: true, id: 'NSPanel_Screensaver', icon: 'wifi', onColor: MSYellow, name: 'Screensaver', buttonText: 'mehr...'},
                    <PageItem>{ navigate: true, id: 'NSPanel_Relays', icon: 'monitor-edit', onColor: MSYellow, name: 'Relais', buttonText: 'mehr...'}
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
                        <PageItem>{ navigate: true, id: 'NSPanel_ScreensaverDimmode', icon: 'wifi', onColor: MSYellow, name: 'Dimmode/Brightness', buttonText: 'mehr...'},
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
                            'next': 'NSPanel_ScreensaverBrightness',
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'Dimmode.brightnessDay', name: 'Brightness Tag', icon: 'brightness-5', offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 5, maxValue: 10},
                                <PageItem>{ id: AliasPath + 'Dimmode.brightnessNight', name: 'Brightness Nacht', icon: 'brightness-4', offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 0, maxValue: 4},
                                <PageItem>{ id: AliasPath + 'Dimmode.hourDay', name: 'Stunde Tag', icon: 'sun-clock', offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 0, maxValue: 23},
                                <PageItem>{ id: AliasPath + 'Dimmode.hourNight', name: 'Stunde Nacht', icon: 'sun-clock-outline', offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 0, maxValue: 23}
                            ]
                        };

                        //Level_3
                        let NSPanel_ScreensaverBrightness = <PageEntities>
                        {
                            'type': 'cardEntities',
                            'heading': 'Helligkeit (2)',
                            'useColor': true,
                            'subPage': true,
                            'parent': NSPanel_Screensaver,
                            'prev': 'NSPanel_ScreensaverDimmode',
                            'home': 'NSPanel_Service',
                            'items': [
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.activeBrightness', name: 'Display bei Nutzung', icon: 'brightness-5', offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 20, maxValue: 100},
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
                                <PageItem>{ id: AliasPath + 'ScreensaverInfo.entityChangeTime', name: 'Wechselzeit/s', icon: 'cog-sync', offColor: MSYellow, onColor: MSYellow, useColor: true, minValue: 15, maxValue: 60}
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
