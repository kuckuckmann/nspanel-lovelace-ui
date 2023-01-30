ioBroker Changelog (TypeScript)

# v3.9.0  

![image](https://user-images.githubusercontent.com/102996011/215470528-f4a9581a-9973-49a9-b472-3153d91f2c89.png)


# v3.8.3

![image](https://user-images.githubusercontent.com/102996011/212193107-c2e88e5d-43d0-4727-bacf-38d13d9e2dcd.png)

**Achtung Breaking Changes:**

```
FlashNextion http://nspanel.pky.eu/lovelace-ui/github/nspanel-v3.8.3.tft
```

**Diese Release beinhaltet:**  
* neue Funktionen des Volumio-Media-Players
* die Vorbereitung für die carLCharts (Linien Diagramme siehe Vorschau unten)
* Funktionen für den "echten Taster" (Mono-Button)
* Hotfix für die farbigen Licht-Typen (Funktion Off)
* Das €-Zeichen in Strings
* Individuelle Navigations-Icons bei parent/prev/next/home

**Update-Anleitung (von v3.8.1 ausgehend):**
* Unteren Teil (ab hier keine Änderungen...) komplett ersetzen.
* In den Variablen muss eine Änderung vorgenommen werden
  * die 1 Zeile der Variable jeder Seite muss von:
    ```
    let Test_Licht1: PageEntities =
    ```
    in 
    ```
    let Test_Licht1 = <PageEntities>
    ```
    geändert werden.
    also:

    let `Variablenname` = <`Seitentyp`>

    **Dadurch ergeben sich folgende Vorteile:**

    Es müssen nicht mehr alle Seitenparameter angegeben werden, wie z.B.:

    ```
     let CardPowerExample = <PagePower>
        {
            'type': 'cardPower',
            'heading': 'cardPower Emulator',
            'items': [
                <PageItem>{ id: 'alias.0.NSPanel_1.Power.PowerCard' },
            ]
        };
    ``` 
    d.h. alle optionalen Seitenparameter mit `undefined` oder `false` können entfallen.

    Zusätzlich können weitere Typen verwendet werden:

    ```
    
         let CardPowerExample = <PagePower>
            {
                'type': 'cardPower',
                'heading': 'cardPower Emulator',
                'useColor': true oder false
                'subPage': true oder false
                'parent': undefined oder Page
                'parentIcon': undefined oder Icon als String, z.B. 'alert'
                'prev': undefined oder 'Page'
                'prevIcon': undefined oder Icon als String
                'next': undefined oder 'Page'
                'nextIcon': undefined oder Icon als String
                'home': undefined oder 'Page' 
                'homeIcon': undefined oder Icon als String
                'items': [
                    <PageItem>{ id: 'alias.0.NSPanel_1.Power.PowerCard' },
                ]
            };
    ```

Das TS-Script findet ihr hier:
https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/NsPanelTs.ts

Mit v3.9.0 kommt demnächst die carLChart hinzu (aktuell noch nicht in der stable TFT):
![image](https://user-images.githubusercontent.com/102996011/212189531-103e384a-d403-4ed1-a99f-fa3d29c72523.png)


***

# v3.8.1

![image](https://user-images.githubusercontent.com/102996011/212193039-2a5503b6-cb25-4110-af76-90d9e2b1d8f3.png)

**Achtung Breaking Changes:**
Um die Menüstruktur derart zu flexibilisieren, mussten in die Seitendeklaration weitere Parameter eingeführt werden. Es ist daher zwingend erforderlich, folgende Erweiterung je Seite vorzunehmen ( **prev**, **next**, **home** ) :

```
let Test_Licht1: PageEntities =
{
    'type': 'cardEntities',
    'heading': 'Color Aliase 1',
    'useColor': true,
    'subPage': false,
    'parent': undefined,
    'prev': undefined,        //Neu - bitte in jede Seite einfügen
    'next': undefined,        //Neu - bitte in jede Seite einfügen
    'home': undefined,        //Neu - bitte in jede Seite einfügen
    'items': [
        <PageItem>{ ... }
    ]
};
```

Was kann man mit der neuen Navigation anstellen? :
@TT-Tom hat eine **ausführliche Anleitung** geschrieben :+1: . Ihr findet Sie in der gestern noch erweiterten Wiki:
https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-Navigation  
![image](https://user-images.githubusercontent.com/102996011/212190944-abfe4a8f-d31c-4dde-aa25-5c49718277dc.png)  

Im oberen Teil des Skriptes sind zwei Konstanten enthalten. 
```
const tasmota_web_admin_user: string = 'admin'; // ändern, falls der User im Tasmota vor dem Kompilieren umbenannt wurde (Standard Tasmota: admin)
const tasmota_web_admin_password: string = '';  // setzten, falls "Web Admin Password" in Tasmote vergeben
```
Bitte nicht vergessen, diese bei der Erweiterung zu berücksichtigen. Wer möchte, kann im Tasmota dann ein Kennwort für den Web Admin vergeben.   
![image](https://user-images.githubusercontent.com/102996011/212191091-cd3cff39-1e81-45e0-aac8-84d72ac7a6fb.png)  

Darüber hinaus hat @egal den **Volumio-Player** implementiert :+1: 
Dieser ist ebenfalls in der Wiki enthalten.
https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-Card-Definitionen-(Seiten)#cardmedia-v20-ab-release-v370

** Ansonsten wie immer den unteren Teil komplett ersetzten. **

Um die neuen Funktionen nutzen zu können, muss ein:
```
FlashNextion http://nspanel.pky.eu/lovelace-ui/github/nspanel-v3.8.1.tft
```
durchgeführt werden.

Sollte der BerryDriver noch nicht auf Version 8 sein, dann vorher:
```
Backlog UpdateDriverVersion https://raw.githubusercontent.com/joBr99/nspanel-lovelace-ui/main/tasmota/autoexec.be; Restart 1
```
durchführen...


***

# v3.7.3.1

![image](https://user-images.githubusercontent.com/102996011/212192718-d7f8ca7b-5bc5-4fc4-ba1f-a81028da1f50.png)

**Hotfix**

Unteren Teil ersetzen:
https://raw.githubusercontent.com/joBr99/nspanel-lovelace-ui/main/ioBroker/NsPanelTs.ts

Das TS-Script legt 2 neue Datenpunkte an:
![image](https://user-images.githubusercontent.com/102996011/212191694-4f80f1e8-f6b6-4fe4-aad1-efb71afb0182.png)


In Weekday oder Month short eintragen. Dann sollte es ein kurzes Datumsformat geben.

EDIT: Funktioniert natürlich auch mit der eu Version. Nur da ist es nicht wirklich erforderlich...


***

# v3.7.3.0

![image](https://user-images.githubusercontent.com/102996011/212191982-f4ad562f-3451-4427-bd6d-01c10bfe70b4.png)


***

# v3.7.0

![image](https://user-images.githubusercontent.com/102996011/212192231-a9052edf-3d16-44a5-be10-6a01a6639b12.png)

Es gibt ein paar Änderungen im oberen Teil des Scriptes (Bitte entsprechend einfügen): 

Neue Konstanten:
```
const weatherAdapterInstance: string = 'accuweather.0.';  //Möglich 'accuweather.0.' oder 'daswetter.0.'
const weatherScreensaverTempMinMax: string = 'MinMax';      // Mögliche Werte: 'Min', 'Max' oder 'MinMax'
...
const HMIOn:            RGB = { red:   3, green: 169, blue: 244 };     // Blau-On
```

Bitte folgende Parameter (Zeilen) aus der Config löschen:
 ```
    dimmode: 20,
    active: 100, //Standard-Brightness TFT
    ...
    timeFormat: '%H:%M',                // currently not used 
    dateFormat: '%A, %d. %B %Y',        // currently not used
``` 

Die Aliase für die cardMedia haben jetzt Repeat und Shuffle als zusätzliche Datenpunkte. Den alten bei alexa2, spotify-premium oder sonos einfach löschen. Das Script wird die wieder neu anlegen.

Version mit Beispielen:
https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/NsPanelTs.ts

Version ohne Beispiele:
https://github.com/joBr99/nspanel-lovelace-ui/blob/main/ioBroker/NsPanelTs_without_Examples.ts

```
FlashNextion http://nspanel.pky.eu/lovelace-ui/github/nspanel-v3.7.0.tft
```

