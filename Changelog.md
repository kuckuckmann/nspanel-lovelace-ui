# v3.8.1

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

# v3.8.3

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
![ea00f217-d220-4d72-a5f9-a37f475a1f01-image.png](/assets/uploads/files/1673007025441-ea00f217-d220-4d72-a5f9-a37f475a1f01-image.png) 

Im oberen Teil des Skriptes sind zwei Konstanten enthalten. 
```
const tasmota_web_admin_user: string = 'admin'; // ändern, falls der User im Tasmota vor dem Kompilieren umbenannt wurde (Standard Tasmota: admin)
const tasmota_web_admin_password: string = '';  // setzten, falls "Web Admin Password" in Tasmote vergeben
```
Bitte nicht vergessen, diese bei der Erweiterung zu berücksichtigen. Wer möchte, kann im Tasmota dann ein Kennwort für den Web Admin vergeben. 
![c574d8f4-56a3-452f-9328-1c12e8c9a794-image.png](/assets/uploads/files/1673005668537-c574d8f4-56a3-452f-9328-1c12e8c9a794-image.png) 

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