# 3.8.3

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