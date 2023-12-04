!!! Diese Seite befindet sich noch im Aufbau !!!

# Aufbau des SONOS Players 
**(vollständig ab NSPanelTs.ts - Version 4.3.3.17)**

![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/47d58044-744d-4de1-a450-d1fdff538527)

1. Seitentitel
Der Seitentitel steht auf: 
* Sonos Player, wenn keine Wiedergabe erfolgt oder wenn das Wiedergabegerät über die Sonos-Adapterinstanz (z.B. sonos.0.) im Datenpunkt `sonos.0.root.<DEVICE_IP>.current_type` auf Track steht
* `sonos.0.root.<DEVICE_IP>.current_station` wenn ein Radiosender gewählt wurde
