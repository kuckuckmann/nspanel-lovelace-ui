!!! Diese Seite befindet sich noch im Aufbau !!!

# Aufbau des SONOS Players 
**(vollständig ab NSPanelTs.ts - Version 4.3.3.17)**

![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/92b349c7-6a85-4903-8911-61000f5144d6)

## Bedienungselemente / Anzeigen
### 1. Seitentitel  
Der Seitentitel steht auf:   
* Sonos Player, wenn keine Wiedergabe erfolgt oder wenn das Wiedergabegerät über die Sonos-Adapterinstanz (z.B. sonos.0.) im Datenpunkt `sonos.0.root.<DEVICE_IP>.current_type` auf track(0) steht  
* `sonos.0.root.<DEVICE_IP>.current_station` wenn ein Radiosender gewählt wurde  

### 2. Navigation zur nächsten Seite  
* siehe [Navigation](ioBroker-Navigation)  

### 3. Track (Elapsed|Duration)  
Zeigt die folgenden Datenpunkte der aktiven Sonos Adapterinstanz wenn der Wert des Datenpunktes `sonos.0.root.<DEVICE_IP>.current_type` auf track(0) steht:  
* Titel --> sonos.0.root.<DEVICE_IP>.current_title  
* Verstrichene Zeit (Minuten/Sekunden) des aktuell abgespielten Titels (nicht bei Radio) --> `sonos.0.root.<DEVICE_IP>.current_elapsed_s`  
* Gesamtlänge (Minuten/Sekunden) des aktuell abgespielten Titels (nicht bei Radio) --> `sonos.0.root.<DEVICE_IP>.current_duration_s`  
> [!IMPORTANT]  
> Die Aktualisierung in Sekunden steht in Abhängigkeit zur Sonos Adapterinstanz `Aktualisierung des Lied-Timers` und steht per Default auf 2000ms.  
> ![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/6770fd4c-271f-499e-a935-7e2217631ea9)
### 4. Interpret | Album  
Folgende Datenpunkte der Sonos Adapterinstanz werden berücksichtigt:  
* Interpret --> `sonos.0.root.<DEVICE_IP>.current_artist` (beim Abspielen von Radiosendern abweichende Informationen zum Sender)  
* Album --> `sonos.0.root.<DEVICE_IP>.current_album` (beim Abspielen von Radiosendern abweichende Informationen zum Sender)  

### 5. Player An/Aus (Stop)   
* Stop (Icon blau) --> `sonos.0.root.<DEVICE_IP>.stop` (beim Abspielen weiß)  

### 6. Volume lauter
* Die Feinjustierung der aktuellen Lautstärke in Einerschritten (+1) --> Datenpunkt: `sonos.0.root.<DEVICE_IP>.volume`  

### 7. Volume zwischen 0% und 100%
* Die Feinjustierung der aktuellen Lautstärke erfolgt stufenlos zwischen 0% und 100% --> Datenpunkt: `sonos.0.root.<DEVICE_IP>.volume`
> [!NOTE]  
> Volume zieht das Volumen einer Gruppe beim Einsatz einer Sonos-Box mit. Wenn das Group-Volume (`sonos.0.root.<DEVICE_IP>.group_volume`) benötigt wird, so ist der Datenpunkt nach Erstellung des Auto-Alias entsprechend zu ändern.  
> ![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/27165f31-9d25-4921-98b9-1c3a7e46cf82)  
> ![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/ca9c5cd2-1fa0-467e-ae01-5dc968b26e63)  

### 8. Repeat-Funktion  
> [!NOTE]  
> Dieses Steuerelement kann unterschiedliche Eigenschaften annehmen    
* Es sind keine weiteren Einstellungen zu berücksichtigen. Der Datenpunkt `sonos.0.root.<DEVICE_IP>.repeat` wird genutzt und inkrementiert die Werte `none(0)`, `all(1)` und `one(2)`  

### 9. SONOS Favoriten (Alternativ Equalizer)
#### Steuerelement als SONOS Favoriten:
Das PageItem enthält keinen equalizerString --> Die Favoriten werden automatisch aus dem Datenpunkt: `sonos.0.root.<DEVICE_IP>.favorites_list_array` extrahiert:
> [!CAUTION]
> ```typescript
> let Sonos = <PageMedia>
> {
>     'type': 'cardMedia',
>     'heading': 'Sonos',
>     'useColor': true,
>     'items': [<PageItem>{   
>                 id: AliasPath + 'Media.PlayerSonos', 
>                 adapterPlayerInstance: 'sonos.0.',
>                 mediaDevice: '192_168_1_212',
>                 speakerList: ['Terrasse'],
>                 playList: ['Hartmann','Armilars Playlist'],
>                 colorMediaIcon: colorSonos,
>                 colorMediaArtist: Yellow,
>                 colorMediaTitle: Yellow,
>                 alwaysOnDisplay: true,
>                 autoCreateALias: true
>              }]
> };
> ```
#### Steuerelement als Equalizer:
* Innerhalb des PageItem wird der Equalizer definiert:  
> [!CAUTION]
> ```typescript
> let Sonos = <PageMedia>
> {
>     'type': 'cardMedia',
>     'heading': 'Sonos',
>     'useColor': true,
>     'items': [<PageItem>{   
>                 id: AliasPath + 'Media.PlayerSonos', 
>                 adapterPlayerInstance: 'sonos.0.',
>                 mediaDevice: '192_168_1_212',
>                 speakerList: ['Terrasse'],
>                 playList: ['Hartmann','Armilars Playlist'],
>                 equalizerList: ['Bassboost','Klassik','Dance', 'Deep', 'Electronic', 'Flat', 'Hip-Hop', 'Rock', 
>                                 'Metal', 'Jazz', 'Latin', 'Tonstärke', 'Lounge', 'Piano'],
>                 colorMediaIcon: colorSonos,
>                 colorMediaArtist: Yellow,
>                 colorMediaTitle: Yellow,
>                 alwaysOnDisplay: true,
>                 autoCreateALias: true
>              }]
> };
> ```

> [!IMPORTANT]
> Die Sonos Adapterinstanz verfügt nicht über Klangsteuerungs-Datenpunkte. Es kann jedoch die SONOS HTTP API https://github.com/jishi/node-sonos-http-api#usage genutzt werden.  
>
> Für den Fall, dass der Equalizer zum Einsatz kommt, bitte weiteren Link befolgen: https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#12-equalizer-f%C3%BCr-cardmedia

 
  
