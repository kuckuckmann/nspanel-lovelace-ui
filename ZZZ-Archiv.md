**CardEntities**  
  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/99131208/4071b1ba-688e-4fa0-be47-d551141b7964)
  
``` 

``` 

***
  
  
<html xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:x="urn:schemas-microsoft-com:office:excel"
xmlns="http://www.w3.org/TR/REC-html40">

<head>

<meta name=ProgId content=Excel.Sheet>
<meta name=Generator content="Microsoft Excel 15">
<link id=Main-File rel=Main-File
href="file:///C:/Users/Kuckuck/AppData/Local/Temp/msohtmlclip1/01/clip.htm">
<link rel=File-List
href="file:///C:/Users/Kuckuck/AppData/Local/Temp/msohtmlclip1/01/clip_filelist.xml">
<style>
<!--table
	{mso-displayed-decimal-separator:"\,";
	mso-displayed-thousand-separator:"\.";}
@page
	{margin:.79in .7in .79in .7in;
	mso-header-margin:.3in;
	mso-footer-margin:.3in;}
.font5
	{color:black;
	font-size:14.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:Calibri, sans-serif;
	mso-font-charset:0;}
.font6
	{color:red;
	font-size:14.0pt;
	font-weight:700;
	font-style:normal;
	text-decoration:none;
	font-family:"Calibri \(Textkörper\)";
	mso-generic-font-family:auto;
	mso-font-charset:0;}
.font7
	{color:red;
	font-size:14.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:"Calibri \(Textkörper\)";
	mso-generic-font-family:auto;
	mso-font-charset:0;}
.font8
	{color:windowtext;
	font-size:14.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:"Calibri \(Textkörper\)";
	mso-generic-font-family:auto;
	mso-font-charset:0;}
tr
	{mso-height-source:auto;}
col
	{mso-width-source:auto;}
br
	{mso-data-placement:same-cell;}
td
	{padding-top:1px;
	padding-right:1px;
	padding-left:1px;
	mso-ignore:padding;
	color:black;
	font-size:12.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:Calibri, sans-serif;
	mso-font-charset:0;
	mso-number-format:General;
	text-align:general;
	vertical-align:bottom;
	border:none;
	mso-background-source:auto;
	mso-pattern:auto;
	mso-protection:locked visible;
	white-space:nowrap;
	mso-rotate:0;}
.xl63
	{font-size:14.0pt;
	mso-number-format:"\@";
	text-align:center;
	vertical-align:top;
	white-space:normal;}
.xl64
	{font-size:14.0pt;
	mso-number-format:"\@";
	text-align:left;
	vertical-align:top;
	white-space:normal;}
.xl65
	{font-size:14.0pt;}
.xl66
	{font-size:14.0pt;
	mso-number-format:"\@";
	text-align:center;
	vertical-align:middle;
	border:.5pt solid windowtext;
	white-space:normal;}
.xl67
	{font-size:14.0pt;
	text-align:center;
	vertical-align:middle;}
.xl68
	{font-size:14.0pt;
	mso-number-format:"\@";
	text-align:center;
	vertical-align:top;
	border:.5pt solid windowtext;
	white-space:normal;}
.xl69
	{font-size:14.0pt;
	mso-number-format:"\@";
	text-align:left;
	vertical-align:top;
	border:.5pt solid windowtext;
	white-space:normal;}
.xl70
	{font-size:14.0pt;
	text-align:center;
	vertical-align:top;
	white-space:normal;}
.xl71
	{font-size:14.0pt;
	text-align:center;
	white-space:normal;}
.xl72
	{font-size:14.0pt;
	mso-number-format:"\@";
	text-align:left;
	vertical-align:top;
	border:.5pt solid windowtext;
	background:yellow;
	mso-pattern:black none;
	white-space:normal;}
.xl73
	{font-size:14.0pt;
	mso-number-format:"\@";
	text-align:center;
	vertical-align:top;
	border-top:.5pt solid windowtext;
	border-right:.5pt solid windowtext;
	border-bottom:none;
	border-left:.5pt solid windowtext;
	white-space:normal;}
.xl74
	{font-size:14.0pt;
	mso-number-format:"\@";
	text-align:center;
	vertical-align:top;
	border-top:none;
	border-right:.5pt solid windowtext;
	border-bottom:none;
	border-left:.5pt solid windowtext;
	white-space:normal;}
.xl75
	{font-size:14.0pt;
	mso-number-format:"\@";
	text-align:center;
	vertical-align:top;
	border-top:none;
	border-right:.5pt solid windowtext;
	border-bottom:.5pt solid windowtext;
	border-left:.5pt solid windowtext;
	white-space:normal;}
.xl76
	{font-size:14.0pt;
	mso-number-format:"\@";
	text-align:center;
	vertical-align:top;
	border-top:none;
	border-right:none;
	border-bottom:.5pt solid windowtext;
	border-left:none;
	white-space:normal;}
-->
</style>
</head>

<body link="#0563C1" vlink="#954F72">



  |   | Datenpunkte, die   erstellt werden, wenn Prüfung nicht erfolgreich ist.     Wenn keine Prüfung vorgesehen ist, werden sie automatisch erstellt.
-- | -- | --
Script   Funktion | Prüfung | Datenpunkte   unter NSPanel_Path | Datenpunkte   unter Alias_Path
CheckDebugMode |   | Config.ScripgtDebugStatus | Config.ScripgtDebugStatus.ACTUAL        Config.ScripgtDebugStatus.SET
CheckMQTTPorts |   | Config.MQTT.portCheck | Config.MQTT.portCheck.ACTUAL     Config.MQTT.portCheck.SET
Init_Release | NSPanel_Path   + 'Display_Firmware.desiredVersion' | Display_Firmware.desiredVersion |  
NSPanel_Path + 'Config.Update.activ' | Config.Update.activ |  
NSPanel_Path +   'Display_Firmware.TFT.desiredVersion' | Display_Firmware.TFT.desiredVersion     Display_Firmware.TFT.currentVersion | Display_Firmware.TFT.currentVersion.ACTUAL     Display_Firmware.TFT.desiredVersion.ACTUAL
InitConfigParameters |   | Config.Screensaver.alternativeScreensaverLayout | Config.Screensaver.alternativeScreensaverLayout.ACTUAL     Config.Screensaver.alternativeScreensaverLayout.SET
  | Config.Screensaver.ScreensaverAdvanced | Config.Screensaver.ScreensaverAdvanced.ACTUAL     Config.Screensaver.ScreensaverAdvanced.SET
  | Config.Screensaver.autoWeatherColorScreensaverLayout | Config.Screensaver.autoWeatherColorScreensaverLayout.ACTUAL     Config.Screensaver.autoWeatherColorScreensaverLayout.SET
  | Config.Screensaver.timeoutScreensaver | Config.Screensaver.timeoutScreensaver.ACTUAL     Config.Screensaver.timeoutScreensaver.SET
  | Config.Screensaver.screenSaverDoubleClick | Config.Screensaver.screenSaverDoubleClick.ACTUAL     Config.Screensaver.screenSaverDoubleClick.SET
InitConfigParameters | NSPanel_Path   + 'Config.locale' | Config.locale |  
NSPanel_Path + 'Config.temperatureUnit' | Config.temperatureUnit |  
NSPanel_Path + 'Config.localeNumber' | Config.localeNumber | Config.localeNumber.VALUE
NSPanel_Path + 'Config.temperatureUnitNumber' | Config.temperatureUnitNumber | Config.temperatureUnitNumber.VALUE
Init_ScreensaverAdvanced | NSPanel_Path   + 'Config.Screensaver.ScreensaverAdvanced' | Config.Screensaver.ScreensaverAdvanced |  
Init_ActivePageData | NSPanel_Path   + 'ActivePage.heading' | ActivePage.heading |  
NSPanel_Path + 'ActivePage.type' | ActivePage.type |  
NSPanel_Path + 'ActivePage.id0' | ActivePage.id0 |  
Init_Screensaver_Backckground_Color_Switch | NSPanel_Path   + 'ScreensaverInfo.bgColorIndicator' | ScreensaverInfo.bgColorIndicator |  
Init_bExit_Page_Change | NSPanel_Path   + 'ScreensaverInfo.bExitPage' | ScreensaverInfo.bExitPage |  
Init_Dimmode_Trigger | NSPanel_Path   + 'ScreensaverInfo.Trigger_Dimmode' | ScreensaverInfo.Trigger_Dimmode |  
InitActiveBrightness | NSPanel_Path   + 'ScreensaverInfo.activeBrightness' oder     NSPanel_Path +   'ScreensaverInfo.activeDimmodeBrightness' | ScreensaverInfo.activeBrightness     ScreensaverInfo.activeDimmodeBrightness | ScreensaverInfo.activeBrightness.ACTUAL     ScreensaverInfo.activeBrightness.SET
InitRebootPanel | NSPanel_Path   + 'Config.rebootNSPanel' | Config.rebootNSPanel | Config.rebootNSPanel.SET
InitUpdateDatapoints | NSPanel_Path   + 'Config.Update.UpdateTasmota' | Config.Update.UpdateTasmota     Config.Update.UpdateBerry     Config.Update.UpdateNextion | Config.Update.UpdateTasmota.SET     Config.Update.UpdateBerry.SET     Config.Update.UpdateNextion.SET
Init_Relays | NSPanel_Path   + 'Relay.1' oder     NSPanel_Path + 'Relay.2' | Relay.1     Relay.2 | Relay.1.ACTUAL     Relay.1.SET     Relay.2.ACTUAL     Relay.2.SET
InitAlternateMRIconsSize | NSPanel_Path   + 'Config.MRIcons.alternateMRIconSize.1' oder     NSPanel_Path + 'Config.MRIcons.alternateMRIconSize.2' | Config.MRIcons.alternateMRIconSize.1     Config.MRIcons.alternateMRIconSize.2 | Config.MRIcons.alternateMRIconSize.1.ACTUAL     Config.MRIcons.alternateMRIconSize.1.SET     Config.MRIcons.alternateMRIconSize.2.ACTUAL     Config.MRIcons.alternateMRIconSize.2.SET
InitDateformat | NSPanel_Path   + 'Config.Dateformat.weekday' oder     NSPanel_Path + 'Config.Dateformat.month' | Config.Dateformat.weekday     Config.Dateformat.month |  
NSPanel_Path +   'Config.Dateformat.Switch.weekday' oder     NSPanel_Path + 'Config.Dateformat.Switch.month' | Config.Dateformat.Switch.weekday     Config.Dateformat.Switch.month | Config.Dateformat.Switch.weekday.ACTUAL     Config.Dateformat.Switch.weekday.SET     Config.Dateformat.Switch.month.ACTUAL     Config.Dateformat.Switch.month.SET
CreateWeatherAlias | weatherEntity   + '.ICON' und     'daswetter.X.NextHours.Location_1.Day_1.current.symbol_value' |   | weatherEntity   + '.ICON'     weatherEntity + '.TEMP'     weatherEntity + '.TEMP_MIN'     weatherEntity + '.TEMP_MAX'
CreateWeatherAlias | weatherEntity   + '.ICON' und     'accuweather.X.Current.WeatherIcon' |   | weatherEntity   + '.ICON'     weatherEntity + '.TEMP'     weatherEntity + '.TEMP_MIN'     weatherEntity + '.TEMP_MAX'
InitPageNavi | NSPanel_Path   + 'PageNavi' | PageNavi |  
InitWeatherForecast | NSPanel_Path   + "ScreensaverInfo.weatherForecast" oder     NSPanel_Path + "ScreensaverInfo.weatherForecastTimer" oder     NSPanel_Path + "ScreensaverInfo.entityChangeTime" | ScreensaverInfo.weatherForecast     ScreensaverInfo.weatherForecastTimer     ScreensaverInfo.entityChangeTime | ScreensaverInfo.weatherForecast.ACTUAL     ScreensaverInfo.weatherForecast.SET     ScreensaverInfo.weatherForecastTimer.ACTUAL     ScreensaverInfo.weatherForecastTimer.SET     ScreensaverInfo.entityChangeTime.ACTUAL     ScreensaverInfo.entityChangeTime.SET
InitDimmode | NSPanel_Path   + 'NSPanel_Dimmode_brightnessDay' | NSPanel_Dimmode_brightnessDay | Dimmode.brightnessDay.ACTUAL     Dimmode.brightnessDay.SET
NSPanel_Path + 'NSPanel_Dimmode_hourDay' | NSPanel_Dimmode_hourDay | Dimmode.hourDay.ACTUAL     Dimmode.hourDay.SET
NSPanel_Path +   'NSPanel_Dimmode_brightnessNight' | NSPanel_Dimmode_brightnessNight | Dimmode.brightnessNight.ACTUAL     Dimmode.brightnessNight.SET
NSPanel_Path + 'NSPanel_Dimmode_hourNight' | NSPanel_Dimmode_hourNight | Dimmode.hourNight.ACTUAL     Dimmode.hourNight.SET
InitPopupNotify | NSPanel_Path   + 'ScreensaverInfo.popupNotifyHeading' | ScreensaverInfo.popupNotifyHeading |  
NSPanel_Path +   'ScreensaverInfo.popupNotifyText' | ScreensaverInfo.popupNotifyText |  
  | popupNotify.popupNotifyHeading |  
  | popupNotify.popupNotifyHeading |  
  | popupNotify.popupNotifyText |  
  | popupNotify.popupNotifyTextColor |  
  | popupNotify.popupNotifyInternalName |  
  | popupNotify.popupNotifyButton1TextColor |  
  | popupNotify.popupNotifyButton1Text |  
  | popupNotify.popupNotifyButton2TextColor |  
  | popupNotify.popupNotifyButton2Text |  
  | popupNotify.popupNotifySleepTimeout |  
  | popupNotify.popupNotifyAction |  
  | popupNotify.popupNotifyLayout |  
  | popupNotify.popupNotifyFontIdText |  
  | popupNotify.popupNotifyIcon |  
  | popupNotify.popupNotifyIconColor |  
get_locales |   | NSPanel_locales_json |  
get_panel_update_data |   | NSPanel_autoUpdate | autoUpdate.ACTUAL     autoUpdate.SET
get_panel_update_data |   | NSPanel_ipAddress | ipAddress.ACTUAL
get_online_tasmota_firmware_version |   | Tasmota_Firmware.onlineVersion | Tasmota_Firmware.onlineVersion.ACTUAL
get_current_berry_driver_version |   | Berry_Driver.currentVersion | Display.BerryDriver.ACTUAL
get_tasmota_status0 |   | Tasmota_Firmware.currentVersion     Tasmota.Uptime     Tasmota.Version     Tasmota.Hardware     Tasmota.Wifi.AP     Tasmota.Wifi.SSId     Tasmota.Wifi.BSSId     Tasmota.Wifi.Channel     Tasmota.Wifi.Mode     Tasmota.Wifi.RSSI     Tasmota.Wifi.Signal     Tasmota.Product | Tasmota.Uptime.ACTUAL     Tasmota.Version.ACTUAL     Tasmota.Hardware.ACTUAL     Tasmota.Wifi.AP.ACTUAL     Tasmota.Wifi.SSId.ACTUAL     Tasmota.Wifi.BSSId.ACTUAL     Tasmota.Wifi.Channel.ACTUAL     Tasmota.Wifi.Mode.ACTUAL     Tasmota.Wifi.RSSI.ACTUAL     Tasmota.Wifi.Signal.ACTUAL     Tasmota.Product.ACTUAL
get_online_berry_driver_version |   | Berry_Driver.onlineVersion | Berry_Driver.onlineVersion.ACTUAL
check_version_tft_firmware |   | TFT_Firmware.onlineVersion |  
check_online_display_firmware |   | Display_Firmware.onlineVersion |  
on({ id: config.panelRecvTopic } |   | Display_Firmware.currentVersion     NSPanel_Version | Display.TFTVersion.ACTUAL     Display.Model.ACTUAL
update_tft_firmware |   | TFT_Firmware.onlineVersion |  
on({ id: config.panelRecvTopic.substring(0,   config.panelRecvTopic.length - 'RESULT'.length) + 'SENSOR' } |   | Sensor.Time     Sensor.TempUnit     Sensor.ANALOG.Temperature     Sensor.ESP32.Temperature | Sensor.Time.ACTUAL     Sensor.TempUnit.ACTUAL     Sensor.ANALOG.Temperature.ACTUAL     Sensor.ESP32.Temperature.ACTUAL



</body>

</html>
