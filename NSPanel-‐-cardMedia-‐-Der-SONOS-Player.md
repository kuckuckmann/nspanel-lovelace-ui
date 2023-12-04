**Inhalt:**
* [Aufbau des SONOS Players](#aufbau-des-sonos-players)   
   * [Player im Live-Betrieb](#player-im-live-betrieb)
   * [Bedienungselemente / Anzeigen](#bedienungselemente--anzeigen)
* [Erstellung der Seitenvariable für die cardMedia](#erstellung-der-seitenvariable-f%C3%BCr-die-cardmedia)
   * [Variablen Beispiele](#variablen-beispiele)
      * [Standard Beispielvorlage für AlwaysOnDisplay](#standard-beispielvorlage-f%C3%BCr-alwaysondisplay)
      * [Standard Beispielvorlage ohne AlwaysOnDisplay](#standard-beispielvorlage-ohne-alwaysondisplay)
* [Erstellung der Sonos Listen](#erstellung-der-sonos-listen)
   * [Speaker Liste (Array speakerList)](#speaker-liste-array-speakerlist)
   * [Favoriten Liste](#favoriten-liste)
   * [Individuelle Wiedergabe Liste (Array playList)](#individuelle-wiedergabe-liste-array-playlist)
* [Der Auto-Alias](#der-auto-alias)



# Aufbau des SONOS Players 
**(vollständig ab NSPanelTs.ts - Version 4.3.3.17)**

![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/da9d3b70-8ed2-4009-a79d-0df76903f4cf)

## Player im Live-Betrieb:

![Nextion_Editor_fsSVjRpc9f](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/2848f8ec-3575-4332-a4ba-be2230cfc856)

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
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/2cedade5-89ca-46bf-a8d8-5e4e4c2c3573)

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
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/66ef5685-e7de-43e5-a574-84e15779799f)

* Innerhalb des `PageItem` wird der `Equalizer` und in diesem Beispiel ebenfalls der Parameter `crossfade` definiert:  
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
>                 crossfade:       true,
>                 alwaysOnDisplay: true,
>                 autoCreateALias: true
>              }]
> };
> ```

> [!IMPORTANT]
> Die Sonos Adapterinstanz verfügt nicht über Klangsteuerungs-Datenpunkte. Es kann jedoch die SONOS HTTP API https://github.com/jishi/node-sonos-http-api#usage genutzt werden.  
>
> Für den Fall, dass der Equalizer zum Einsatz kommt, bitte weiteren Link befolgen: https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#12-equalizer-f%C3%BCr-cardmedia

> [!Note]
> siehe auch Erstellung der Sonos Favoriten

### 10. Track Liste
* Sofern der Datenpunkt `sonos.0.root.<DEVICE_IP>.queue` Daten enthält und die abspielbaren Medien eine Trackliste enthalten, so wird diese automatisch geladen.
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/44c5b0b6-7bbd-4372-ad8e-244f5e9bb729)
> [!NOTE]
> Sollten weitere Tracks vorhanden sein, so können diese über den rechtsangeordneten Pfeil erreicht werden  

### 11. SONOS Playlist
* Das Array playList im PageItem wird genutzt. Die Playlists sind dort manuell einzutragen  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/7a544d32-7fe1-45f8-b9fb-50ad5a259628)  

> [!NOTE]
> siehe auch Erstellung einer Sonos Playlist

### 12. SONOS Speaker Liste
* Das Array speakerList im PageItem wird genutzt. Die Wiedergabegeräte sind dort manuell einzutragen
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/da4e95e3-9091-43da-9712-744e85a30c0c)
> [!NOTE]
> siehe auch Erstellung einer speakerList

### 13. Nächster Track
* Sofern ein weiterer Titel in der Track Liste verfügbar ist, so wird dieser ausgewählt --> `sonos.0.root.<DEVICE_IP>.next`

### 14. Play / Pause   
* Umschaltung zwischen den Datenpunkten `sonos.0.root.<DEVICE_IP>.play` und `sonos.0.root.<DEVICE_IP>.pause`    

### 15. Volume leiser
* Die Feinjustierung der aktuellen Lautstärke in Einerschritten (-1) --> Datenpunkt: `sonos.0.root.<DEVICE_IP>.volume`  

### 16. Shuffle
* Umschaltung zwischen den Datenpunkten `sonos.0.root.<DEVICE_IP>.shuffle` als wahr/falsch (true/false)
> [!NOTE]
> Diese Funktion ist nicht steuerbar, wenn Radiosender abgespielt werden

### 17. Vorheriger Track
* Sofern ein weiterer Track vor dem aktuell abgespielten Titel in der Track Liste verfügbar ist, so wird dieser ausgewählt --> `sonos.0.root.<DEVICE_IP>.prev`

### 18. Player Logo / Seek Funktion (Alternativ Crossfade)
Per Standard ist der Seek-Modus aktiv. Dieser wird mit Klick auf das Logo des Players aufgerufen:  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/f78a8093-351f-4a5f-b58b-415f78bf4e2d)  

Jetzt ist es möglich eine Position des Tracks (Titels) in 10% Schritten zu erreichen (vor- und zurückspulen).  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/ee9ce338-5c0e-465d-935c-df55adf8642c)  

> [!NOTE]
> Wird im PageItem der Parameter  
> `crossfade: true`  
> verwendet, dann wird statt der Seek-Funktion Crossfade zur Auswahl aktiv  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/7d2387fa-b943-4540-ae7e-efbb2c98b763)

### 19. Navigation zur vorherigen Seite  
* siehe [Navigation](ioBroker-Navigation)  

# Erstellung der Seitenvariable für die cardMedia

![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/e87fd566-af21-475e-80dd-81e6225e52e9)

## Variablen Beispiele:
### Standard Beispielvorlage für AlwaysOnDisplay
In diesem Beispiel wird der Screensaver nach eingestellter nicht aufgeschaltet. Der Player bleibt geöffnet bis zu einer Seite ohne alwaysOnDisplay navigiert wird.
```typescript
let Sonos = <PageMedia>
{
    'type': 'cardMedia',
    'heading': 'Sonos Player',
    'useColor': true,
    'items': [<PageItem>{   
                id: AliasPath + 'Media.PlayerSonos', 
                adapterPlayerInstance: 'sonos.0.',
                mediaDevice: '192_168_1_212',
                speakerList: ['Wohnzimmer', 'Küche', Büro],
                playList: ['Hartmann','Armilars Playlist'],
                colorMediaIcon: colorSonos,
                colorMediaArtist: Yellow,
                colorMediaTitle: Yellow,
                alwaysOnDisplay: true,
                autoCreateALias: true
             }]
};
```

### Standard Beispielvorlage ohne AlwaysOnDisplay
In diesem Beispiel wird der Screensaver nach eingestellter Zeit aufgerufen. Der Player wird geschlossen.
```typescript
let Sonos = <PageMedia>
{
    'type': 'cardMedia',
    'heading': 'Sonos Player',
    'useColor': true,
    'items': [<PageItem>{   
                id: AliasPath + 'Media.PlayerSonos', 
                adapterPlayerInstance: 'sonos.0.',
                mediaDevice: '192_168_1_212',
                speakerList: ['Wohnzimmer', 'Küche', Büro],
                playList: ['Hartmann','Armilars Playlist'],
                colorMediaIcon: colorSonos,
                colorMediaArtist: Yellow,
                colorMediaTitle: Yellow,
                autoCreateALias: true
             }]
};
```

mediaDevice ist hierbei die mit '_' getrennte IP des primären Wiedergabegerätes und muss angepasst werden. Der Inhalt ist analog des Datenpunktes `sonos.0.root.<DEVICE_IP>.coordinator`
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/6de74a6c-0aed-480e-9a07-196148d01a25)

> [!CAUTION]
> Nicht zu empfehlen!!!: Der Parameter autoCreateALias kann ebenfalls entfernt werden, jedoch muss ein korrekter Media-Alias mit dem Channel "media" und den vom NSPanelTs.ts - Skript erwarteten Datenpunkten dann "per Hand" erstellt werden. Da es nahezu unmöglich ist unter ioBroker einen korrekten und vollständigen Media-Alias zu erstellen, übernimmt das Skript mit diesem Parameter diese Aufgabe.  

# Erstellung der Sonos Listen
## Speaker Liste (Array speakerList)
Diese List sollte die Wiedergabegeräte des primären Sonos und ggfs. optionale Geräte aus dem Datenpunkt `sonos.0.root.<DEVICE_IP>.members` enthalten.

## Favoriten Liste
Die Einstellung erfolgt über die App des Smartphones oder über z.B. dem "Sonos Controller für PC" wie im nachfolgenden Beispiel:  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/9dc179a1-acf4-4e29-b642-171c2f6407a1)  
  
Die Favoriten können unter Sonos-Favoriten eingesehen werden:  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/8564c777-f148-475f-be27-228196495183)  
  
Sonos Favoriten hinzufügen:  
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/671bbcca-f42a-49ec-9774-3c2f5ffa58c6)  

## Individuelle Wiedergabe Liste (Array playList)
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/10a05428-dac9-4bc9-8ab0-52af9a7fd5bb)  
  
Dann entweder zu einer besehenden Playlist hinzufügen oder eine neue Playlist mit neuem Namen erstellen:    
![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/607403ee-9f77-409d-895b-d9bf2a7e6a26)  

Die Namen der individuellen Playlisten für diesen Player werden dann in das Array (Beispiel): `playList: ['Hartmann','Armilars Playlist'],` des PageItem eingetragen.

# Der Auto-Alias
Der nachfolgende Alias wird komplett und vollständig angelegt, wenn der Parameter `autoCreateALias: true` im PageItem definiert ist:

![image](https://github.com/joBr99/nspanel-lovelace-ui/assets/102996011/5f51762a-f648-4cdb-9b75-80065019a4a9)


