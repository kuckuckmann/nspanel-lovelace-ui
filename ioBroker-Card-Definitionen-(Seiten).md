# cardEntities
![image](https://user-images.githubusercontent.com/102996011/190120141-13da0024-261d-4cd9-a104-13416c224004.png)  

4 vertikal angeordnete Steuerelemente (Erstellung der "PageItem" siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen))  

```
var Sprechender_eindeutiger_Seitenname: PageEntities =
{
    "type": "cardEntities",
    "heading": "Deine Überschrift",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [
        <PageItem>{ id: "Dein_Erstellter_Alias_1", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_2", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_3", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_4", Weitere Parameter siehe Alias Definition }
    ]
};
```


# cardGrid
![image](https://user-images.githubusercontent.com/102996011/190120023-c9e0477c-0d06-4484-af27-be2f6fe810d3.png)

6 horizontal angeordnete Steuerelemente (in 2 Reihen je 3 Steuerelemente) (Erstellung der "PageItem" siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen))  

```
var Sprechender_eindeutiger_Seitenname: PageGrid =
{
    "type": "cardGrid",
    "heading": "Deine Überschrift",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [
        <PageItem>{ id: "Dein_Erstellter_Alias_1", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_2", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_3", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_4", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_5", Weitere Parameter siehe Alias Definition },
        <PageItem>{ id: "Dein_Erstellter_Alias_6", Weitere Parameter siehe Alias Definition }
    ]
};
```

# cardAlarm
![image](https://user-images.githubusercontent.com/102996011/190120272-82c6b418-c9dc-4338-a0a3-53da8bec0bac.png)

(Erstellung des alias.0.Alarm siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen))  

```
var Sprechender_eindeutiger_Seitenname: PageAlarm =
{
    "type": "cardAlarm",
    "heading": "Deine Überschrift",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [
        <PageItem>{ id: alias.0.Alarm}
    ]
};
```
# cardMedia v2.0 (ab Release v3.7.0)
![image](https://user-images.githubusercontent.com/102996011/209344233-c7d700c4-eb87-4c51-9441-b51368c88096.png)

**Neue Elemente**
* Shuffle (nach verfügbarkeit des Adapters)  
  ![image](https://user-images.githubusercontent.com/102996011/209348879-59575912-b9c6-452f-885c-0cbb2791f750.png)

* Neue Auswahl für Speakerauswahl/-wechsel  
  ![image](https://user-images.githubusercontent.com/102996011/209346590-f265353e-a35a-42d4-9d1f-48426e47eb44.png)

* Playlist  
  ![image](https://user-images.githubusercontent.com/102996011/209347004-5d20ac06-b5c2-472e-aeb8-4e9bbb0082e9.png)

* Tracklist (Bei Playlist und falls verfügbar)  
  ![image](https://user-images.githubusercontent.com/102996011/209347405-f33dbd6d-ce7d-4dba-9744-73835f7c1c81.png)

* Equalizer-Profile  
  ![image](https://user-images.githubusercontent.com/102996011/209347576-809eaabe-c853-476f-82f8-6536694ba404.png)  
  [Link: Blockly für Klangsteuerung in der cardMedia](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#12-equalizer-f%C3%BCr-cardmedia)

* Repeat (nach Verfügbarkeit des Adapters)  
  ![image](https://user-images.githubusercontent.com/102996011/209348242-264737e4-7b31-488e-a4db-10e0f6bd6e08.png)

(Erstellung des "PageItem" siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen))   

> **Definition ab TS-Version 3.7.0** (Breaking Changes)  

**alexa2-Adapter**
```
let Alexa: PageMedia = 
{
    'type': 'cardMedia',
    'heading': 'Alexa',
    'useColor': true,
    'subPage': false,
    'parent': undefined,
    'items': [<PageItem>{   
                id: AliasPath + 'Media.PlayerAlexa', 
                adapterPlayerInstance: 'alexa2.0.',
                mediaDevice: 'G0XXXXXXXXXXXXXX', // Eigene Seriennummer des primären Device einstellen
                speakerList: ['Überall','Gartenhaus','Esszimmer','Heimkino','Echo Dot Küche','Echo Spot Buero'],
                //analog alexa2 Music-Provider
                //Mögliche Playlists:
                playList: ['Spotify-Playlist.Party Playlist',
                           'Amazon-Music-Playlist.Mein Discovery Mix',
                           'My-Library-Playlist.2020',
                           'My-Library-Playlist.2021',
                           'TuneIn.Radio Bob Rock',
                           'TuneIn.NDR2',
                           'Spotify-Playlist.Sabaton Radio',
                           'Spotify-Playlist.Rock Party',
                           'Spotify-Playlist.This Is Nightwish',
                           'Spotify-Playlist.Metal Christmas'],
                equalizerList: ['Bassboost','Klassik','Dance', 'Deep', 'Electronic', 'Flat', 'Hip-Hop', 'Rock', 
                                'Metal', 'Jazz', 'Latin', 'Tonstärke', 'Lounge', 'Piano'],
                colorMediaIcon: colorAlexa,
                colorMediaArtist: Yellow,
                colorMediaTitle: Yellow,
                autoCreateALias : true
             }]
};
```

**spotify-premium Adapter**
```
let SpotifyPremium: PageMedia = 
{
    "type": "cardMedia",
    "heading": "Spotify-Premium",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{ 
                id: AliasPath + 'Media.PlayerSpotifyPremium', 
                adapterPlayerInstance: "spotify-premium.0.",
                speakerList: ['LENOVO-W11-01','Terrasse','Überall','Gartenhaus','Esszimmer','Heimkino','Echo Dot Küche',
                              'Echo Spot Buero'],
                //Favoriten Playlists aus Spotify in Liste eintragen 
                playList: ['Party Playlist','Sabaton Radio','Rock Party','This Is Nightwish','Metal Christmas'],
                repeatList: ['off','context','track'],
                equalizerList: ['Bassboost','Klassik','Dance', 'Deep', 'Electronic', 'Flat', 'Hip-Hop', 'Rock', 
                                'Metal', 'Jazz', 'Latin', 'Tonstärke', 'Lounge', 'Piano'],
                colorMediaIcon: colorSpotify,
                colorMediaArtist: Yellow,
                colorMediaTitle: Yellow,
                autoCreateALias : true
             }]
};
```

# cardMedia v1.0 (bis Release v3.6.0)
![image](https://user-images.githubusercontent.com/102996011/204136831-afe5bde8-5046-495b-8ea7-68bc91e3a57c.png)  

(Erstellung des "PageItem" siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen))  

> **Definition ab TS-Version 3.1.1.3** (Breaking Changes)
```
var Sprechender_eindeutiger_Seitenname: PageMedia = 
{
    "type": "cardMedia",
    "heading": "Deine Überschrift",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{   
                id: "alias.0.NSPanel_X.Media.PlayerAlexa", 
                adapterPlayerInstance: "alexa2.0.",
                mediaDevice: "G0XXXXXXXXXXXXXXXX", 
                speakerList: ['Überall','Gartenhaus','Esszimmer','Heimkino','Echo Dot Küche','Echo Spot Buero']
             }]
};
```  
oder
```  
let SpotifyPremium: PageMedia = 
{
    "type": "cardMedia",
    "heading": "Spotify-Premium",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{ 
                id: AliasPath + 'Media.PlayerSpotifyPremium', 
                adapterPlayerInstance: "spotify-premium.0.",
                speakerList: ['LENOVO-W11-JB','Terrasse','Überall','Gartenhaus','Esszimmer','Heimkino','Echo Dot Küche','Echo Spot Buero'],
                colorMediaIcon: colorSpotify,
                colorMediaArtist: Yellow,
                colorMediaTitle: Yellow,
                autoCreateALias : true
             }] 
};
```  

### Parameter  
  
**adapterPlayerInstance:** "alexa.0." oder "spotify-premium.0." oder "sonos.0." oder "chromecast.0." oder "squeezeboxrpc.0.Players.DeinPlayer. 
  
**mediaDevice:**
* für "alexa.0.": Seriennummer oder Gruppennummer des primären Alexa-Device
* für "sonos.0.": IP-Adresse des Sonsos primären Sonos-Device (getrennt mit "_") --> Beispiel: 192_168_1_250  
* für "spotify-premium.0.": Zeile kann gelöscht werden, da Spotify immer nur einen Speaker oder Gruppe steuern kann (automatische Ermittlung)
* für "chromecast.0.": Zeile kann gelöscht werden, da GoogleHome keine Funktionalitäten zum Wechseln von Lautsprechern zur Verfügung stellt 
* für "squeezeboxrpc.0.": Zeile kann gelöscht werden, da squeezeboxrpc keine Funktionalitäten zum Wechseln von Lautsprechern zur Verfügung stellt  

**speakerList:** (Namen und Reihenfolge der Speaker selbst bestimmen)
* für "alexa.0.": Device-Namen aus alexa2 möglich. Wenn leer [] , dann alle Devices des alexa2-Adapter 
* für "sonos.0.": Zeile kann gelöscht werden, da Funktionalität zum schieben auf andere Devices im Sonos-Adapter nicht möglich  
* für "spotify-premium.0.": Alle SmartDevice-Namen aus Spotify möglich (Im Gegensatz zu Alexa auch Smartphones und Rechner)
* für "chromecast.0.": Zeile kann gelöscht werden, da GoogleHome keine Funktionalitäten zum Wechseln von Lautsprechern zur Verfügung stellt 
* für "squeezeboxrpc.0.": "Bekannte Player unter Players (aktuell keine Funktion)

> **Definition bis TS-Version 3.1.1.3**
```
var Sprechender_eindeutiger_Seitenname: PageMedia = 
{
    "type": "cardMedia",
    "heading": "Deine Überschrift",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{ id: "alias.0.NSPanel_X.Media.PlayerAlexa" }]
};
```

# cardQR
![image](https://user-images.githubusercontent.com/102996011/190121115-436dc34d-3a89-4809-a3c6-2c6132938fd1.png)

> Beispiel: Erstellung des "PageItem" und Alias vom Typ "Info" siehe (https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#5-qr-code-page) by Kuckuckmann
```
var Sprechender_eindeutiger_Seitenname: PageQR = 
{
    "type": "cardQR",
    "heading": "Deine Überschrift",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{ id: "alias.0.NSPanel_1.Guest_Wifi" }] // Beispiel
};
```  
  
**Parameter:**  
keine

# cardThermo  
  
(Erstellung der "PageItem" siehe [ioBroker ALIAS Definition](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen)) 
  
> Für Thermostat und Klimaanlage (Unterschied im zu erstellenden Alias)

![image](https://user-images.githubusercontent.com/102996011/204626750-bbeffe48-c9cd-44bf-8dfd-b90c6c3b7422.png)  
  

![image](https://user-images.githubusercontent.com/102996011/204623942-ca5a1e74-23f7-4b10-a65a-d2397ab67c72.png)  
  
![image](https://user-images.githubusercontent.com/102996011/204626323-a5df2e57-378f-4939-8a45-1a83277e23a2.png)  
  
![image](https://user-images.githubusercontent.com/102996011/204627014-03173d87-22ba-44fb-b07c-40b7be6366ac.png)  
  
```  
var Sprechender_eindeutiger_Seitenname: PageThermo = 
{
    "type": "cardThermo",
    "heading": "Test Klimaanlage",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{   
                id: "alias.0.NSPanel_1.TestKlimaanlage", 
                minValue: 50, 
                maxValue: 250,
                popupThermoMode1: ['Auto','0','1','2','3'],
                popupThermoMode2: ['Auto','0','1','2','3','4','5'],
                popupThermoMode3: ['Auto','Manual','Boost',],
                popUpThermoName: ["Schwenk-Modus", 'Speed', 'Temperatur'],
                icon: 'fan',
                setThermoAlias: ['MODE1','MODE2','MODE3'],
                setThermoDestTemp2: 'ACTUAL2'
             }]
};
```  

**Parameter:**  
minValue: Minimale einzustellende Temperatur (Beispiel: 17°C entspricht 170)  
maxValue: Maximale einzustellende Temperatur (Beispiel: 30,5°C entspricht 305)  

# cardPower (ab TS-Script v.3.4.1) 
  
![Nextion_Editor_9AYbpowjZS](https://user-images.githubusercontent.com/102996011/194641145-660e1218-f559-4f25-83ca-984cc677e0d8.gif)  

Beispiel: Erstellung des "PageItem" und Alias vom Typ "Info"

```  
var CardPowerExample: PagePower =
{
    "type": "cardPower",
    "heading": "cardPower Emulator",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [
        <PageItem>{ id: "alias.0.NSPanel_1.Power.PowerCard" },
    ]
};
```  


**Parameter:**  
Es gibt nur einen einzigen externen Datenpunkt (anzulegen in **0_userdata.0.**), auf den ein Alias vom Typ "**Info**" zugreift. Dieser muss mit einem JSON-Objekt in nachfolgender Struktur befüllt werden. Der Alias-Datenpunkt "**ACTUAL**" sollte hierbei auf diesen neuen Datenpunkt in "**0_userdata.0.**) gebunden sein.  
  
```  
[
  {
    "id": 1,
    "value": 3,
    "unit": "kW",
    "direction": "in",
    "icon": "battery-charging-60",
    "iconColor": 10,
    "speed": -3
  },
  {
    "id": 2,
    "value": 6.1,
    "unit": "kW",
    "direction": "in",
    "icon": "solar-power-variant",
    "iconColor": 1,
    "speed": 3
  },
  {
    "id": 3,
    "value": 4.9,
    "unit": "kW",
    "direction": "in",
    "icon": "wind-turbine",
    "iconColor": 0,
    "speed": 3
  },
  {
    "id": 4,
    "value": 1.6,
    "unit": "kW",
    "direction": "in",
    "icon": "shape",
    "iconColor": 10,
    "speed": 3
  },
  {
    "id": 5,
    "value": 6.4,
    "unit": "kW",
    "direction": "in",
    "icon": "transmission-tower",
    "iconColor": 0,
    "speed": 2
  },
  {
    "id": 6,
    "value": 0,
    "unit": "kW",
    "direction": "in",
    "icon": "car",
    "iconColor": 0,
    "speed": 3
  }
]
```  

**cardPower Emulator (Blockly)**  

<details>
  <summary>ioBroker Blockly Script</summary>

  ```
<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="N(P#!imDf$+p`U1atsq-">Debug</variable>
    <variable id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</variable>
    <variable id="2qF4}%9QgN#!2:7fs}B#">dpValuesMax</variable>
    <variable id="cqo]H%;{[I_)-Jq;Y8jl">valueDirection</variable>
    <variable id="?wzEQN^Kk/mY4n0,{$/u">iconString</variable>
    <variable id="E`|=%twhb7vm1+r?}VX?">dpValueUnit</variable>
    <variable id="LlRz2eBS(B:~7Uz*A=$6">iconColors</variable>
    <variable id="E57P;3$~H@U7xnh3-3~T">j</variable>
    <variable id="uN(6R6f#q):2R%dR_YQ}">vSpeed</variable>
    <variable id="ka?!8/C5fALo,cmSVoD;">outJSON</variable>
    <variable id="B2:D:XW|l:N~aV}wAHVT">i</variable>
    <variable id="=J?O~NeDtbS/i^;4)HAs">bat_loading</variable>
    <variable id="DeFZ=AKn8o[,ad:-P/+#">bat_temp</variable>
  </variables>
  <block type="variables_set" id="a:p]1@b2l}C.4IF7nvei" x="-287" y="-188">
    <field name="VAR" id="N(P#!imDf$+p`U1atsq-">Debug</field>
    <value name="VALUE">
      <block type="logic_boolean" id="|G*D[0Z`96lGI]7}tbWV">
        <field name="BOOL">TRUE</field>
      </block>
    </value>
    <next>
      <block type="schedule" id="r9xy%Y+vv_z4b-=9?o#6">
        <field name="SCHEDULE">* * * * *</field>
        <statement name="STATEMENT">
          <block type="control" id="DooKEECuKVI~j{eLYEs^">
            <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="false"></mutation>
            <field name="OID">0_userdata.0.Test.CardPowerExample.DP2Value</field>
            <field name="WITH_DELAY">FALSE</field>
            <value name="VALUE">
              <block type="math_rndfixed" id="!H7+1!*bIKx}8;5c8A1(">
                <field name="n">1</field>
                <value name="x">
                  <shadow type="math_number" id="8~pyf;JpF$pguDndi=/9">
                    <field name="NUM">3.1234</field>
                  </shadow>
                  <block type="math_arithmetic" id="hV%Ff[r@+SVmIR~qE.sv" inline="false">
                    <field name="OP">ADD</field>
                    <value name="A">
                      <shadow type="math_number" id="Y$qc}+2j*J3S%M%?F_*n">
                        <field name="NUM">1</field>
                      </shadow>
                      <block type="math_random_int" id="b4yv:KLBk4ldrNCL}hpW">
                        <value name="FROM">
                          <shadow type="math_number" id="BG|u=f48#9RCZ.5kzin^">
                            <field name="NUM">4</field>
                          </shadow>
                        </value>
                        <value name="TO">
                          <shadow type="math_number" id="(-:TecP9tj?+Y%g!~UUw">
                            <field name="NUM">6</field>
                          </shadow>
                        </value>
                      </block>
                    </value>
                    <value name="B">
                      <shadow type="math_number" id="sf#DH/Sv:5pLZ$KCE8pt">
                        <field name="NUM">1</field>
                      </shadow>
                      <block type="math_random_float" id="-D7d2MQ$*%:H9`PUjjkF"></block>
                    </value>
                  </block>
                </value>
              </block>
            </value>
            <next>
              <block type="control" id="POQ;0e|EI0gW,B3:b66k">
                <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="false"></mutation>
                <field name="OID">0_userdata.0.Test.CardPowerExample.DP3Value</field>
                <field name="WITH_DELAY">FALSE</field>
                <value name="VALUE">
                  <block type="math_rndfixed" id="bD).z4#qj.HA*!jjlfF,">
                    <field name="n">1</field>
                    <value name="x">
                      <shadow type="math_number" id="LJSiJ?trq~{-Imj:E%Ah">
                        <field name="NUM">3.1234</field>
                      </shadow>
                      <block type="math_arithmetic" id="x_sH;+aha`#_l8W:4y::" inline="false">
                        <field name="OP">ADD</field>
                        <value name="A">
                          <shadow type="math_number" id="xGSCe*c)-Tj7a$=:cfAf">
                            <field name="NUM">1</field>
                          </shadow>
                          <block type="math_random_int" id="Y+#:bC|vh@`;O0hw$i)F">
                            <value name="FROM">
                              <shadow type="math_number" id="u{tFIP$+T@=9*ULDi{Ni">
                                <field name="NUM">3</field>
                              </shadow>
                            </value>
                            <value name="TO">
                              <shadow type="math_number" id="XF.D(V)mNnVU$Lm0o!V*">
                                <field name="NUM">4</field>
                              </shadow>
                            </value>
                          </block>
                        </value>
                        <value name="B">
                          <shadow type="math_number">
                            <field name="NUM">1</field>
                          </shadow>
                          <block type="math_random_float" id="@pdPH]Vb]pgzh[+p[)sI"></block>
                        </value>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="control" id="RFfvsL~7i_=8VKHca,nJ">
                    <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="false"></mutation>
                    <field name="OID">0_userdata.0.Test.CardPowerExample.DP4Value</field>
                    <field name="WITH_DELAY">FALSE</field>
                    <value name="VALUE">
                      <block type="math_rndfixed" id="b59):EKpCh6mx=,^-)WP">
                        <field name="n">1</field>
                        <value name="x">
                          <shadow type="math_number" id="s:qBd+=Coyyu~ll`I%(k">
                            <field name="NUM">3.1234</field>
                          </shadow>
                          <block type="math_arithmetic" id="=6qlf~3?#L^zC1Ld@aM=" inline="false">
                            <field name="OP">ADD</field>
                            <value name="A">
                              <shadow type="math_number">
                                <field name="NUM">1</field>
                              </shadow>
                              <block type="math_random_int" id="4Q;G[F6V^e-oZOs+M-%|">
                                <value name="FROM">
                                  <shadow type="math_number" id="sjxN3Q.,3#|6%P%mE8]E">
                                    <field name="NUM">0</field>
                                  </shadow>
                                </value>
                                <value name="TO">
                                  <shadow type="math_number" id="(6c}17w*}-#rF/O!:@@4">
                                    <field name="NUM">6</field>
                                  </shadow>
                                </value>
                              </block>
                            </value>
                            <value name="B">
                              <shadow type="math_number">
                                <field name="NUM">1</field>
                              </shadow>
                              <block type="math_random_float" id="1=No%7-_JAoaQ:.0bhw-"></block>
                            </value>
                          </block>
                        </value>
                      </block>
                    </value>
                    <next>
                      <block type="control" id="Dr9D%Kp}?^VG/HI_:;DQ">
                        <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="false"></mutation>
                        <field name="OID">0_userdata.0.Test.CardPowerExample.DP6Value</field>
                        <field name="WITH_DELAY">FALSE</field>
                        <value name="VALUE">
                          <block type="math_rndfixed" id="1`B)t)uNUV.W9nvRsQ~B">
                            <field name="n">1</field>
                            <value name="x">
                              <shadow type="math_number" id="=iu.=fFNZ8.]a5KMa?n9">
                                <field name="NUM">3.1234</field>
                              </shadow>
                              <block type="math_arithmetic" id="#=f]~.`:5M$lc~4?5l5S" inline="false">
                                <field name="OP">ADD</field>
                                <value name="A">
                                  <shadow type="math_number">
                                    <field name="NUM">1</field>
                                  </shadow>
                                  <block type="math_random_int" id="gB.t#^SL8`m0-G(rVxK.">
                                    <value name="FROM">
                                      <shadow type="math_number" id="o/xD.{}!tol#Z]Od,oUl">
                                        <field name="NUM">0</field>
                                      </shadow>
                                    </value>
                                    <value name="TO">
                                      <shadow type="math_number" id="mGR-M;cK/XQ~i{@H]~Bo">
                                        <field name="NUM">2</field>
                                      </shadow>
                                    </value>
                                  </block>
                                </value>
                                <value name="B">
                                  <shadow type="math_number" id="Tb2d;9t1*K5Ytm3g@M2o">
                                    <field name="NUM">1</field>
                                  </shadow>
                                  <block type="math_random_float" id="FGe_;_*E(w|lksx*p{U`"></block>
                                </value>
                              </block>
                            </value>
                          </block>
                        </value>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </statement>
        <next>
          <block type="on_ext" id="W|0+}C[A/mBDR@0Afbs]">
            <mutation xmlns="http://www.w3.org/1999/xhtml" items="6"></mutation>
            <field name="CONDITION">any</field>
            <field name="ACK_CONDITION"></field>
            <value name="OID0">
              <shadow type="field_oid" id="wO*nq4wWdE;f$cUtNoTa">
                <field name="oid">default</field>
              </shadow>
              <block type="field_oid" id="m62Ey*u`IvtP92JmY*z_">
                <field name="oid">0_userdata.0.Test.CardPowerExample.DP1Value</field>
              </block>
            </value>
            <value name="OID1">
              <shadow type="field_oid" id="3xd``Bszbo1=zA!bvsZ)">
                <field name="oid">default</field>
              </shadow>
              <block type="field_oid" id="DS4:ae%Pqis9jAk-TK/8">
                <field name="oid">0_userdata.0.Test.CardPowerExample.DP2Value</field>
              </block>
            </value>
            <value name="OID2">
              <shadow type="field_oid" id="G?xj1Mz*iul}^R8Fs[A_">
                <field name="oid">default</field>
              </shadow>
              <block type="field_oid" id=":9nM,f6!CVS$18%/KS@z">
                <field name="oid">0_userdata.0.Test.CardPowerExample.DP3Value</field>
              </block>
            </value>
            <value name="OID3">
              <shadow type="field_oid" id="9o?N9]+379#b)`sYo6hV">
                <field name="oid">default</field>
              </shadow>
              <block type="field_oid" id="`xVoo}%NbVYwFBkc#HV(">
                <field name="oid">0_userdata.0.Test.CardPowerExample.DP4Value</field>
              </block>
            </value>
            <value name="OID4">
              <shadow type="field_oid" id="[tFjGqu{)GE2y4=Y(2W)">
                <field name="oid">default</field>
              </shadow>
              <block type="field_oid" id="eD#O+m+a=@rY.P(vEt^=">
                <field name="oid">0_userdata.0.Test.CardPowerExample.DP5Value</field>
              </block>
            </value>
            <value name="OID5">
              <shadow type="field_oid" id="5w${U:U)0m~#TLsVU}K*">
                <field name="oid">default</field>
              </shadow>
              <block type="field_oid" id="ive+FtP:uPK[r[r%BYGM">
                <field name="oid">0_userdata.0.Test.CardPowerExample.DP6Value</field>
              </block>
            </value>
            <statement name="STATEMENT">
              <block type="variables_set" id=":a:|I$~,EynHv)!Dpq!q">
                <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                <value name="VALUE">
                  <block type="lists_create_with" id="LP;bm@IeZHvbV2zDr0,C">
                    <mutation items="6"></mutation>
                    <value name="ADD0">
                      <block type="get_value" id="uLS`nab.$wpI2_6Udd]%">
                        <field name="ATTR">val</field>
                        <field name="OID">0_userdata.0.Test.CardPowerExample.DP1Value</field>
                      </block>
                    </value>
                    <value name="ADD1">
                      <block type="get_value" id="(W^eYyE!x6r23f_{eijy">
                        <field name="ATTR">val</field>
                        <field name="OID">0_userdata.0.Test.CardPowerExample.DP2Value</field>
                      </block>
                    </value>
                    <value name="ADD2">
                      <block type="get_value" id="h`;Z}lIOUg!tIyW#WBQ6">
                        <field name="ATTR">val</field>
                        <field name="OID">0_userdata.0.Test.CardPowerExample.DP3Value</field>
                      </block>
                    </value>
                    <value name="ADD3">
                      <block type="get_value" id="@fg(}9S-xos%UELU$#o)">
                        <field name="ATTR">val</field>
                        <field name="OID">0_userdata.0.Test.CardPowerExample.DP4Value</field>
                      </block>
                    </value>
                    <value name="ADD4">
                      <block type="get_value" id="*?CN!aC@?Hhdm~l%X=d=">
                        <field name="ATTR">val</field>
                        <field name="OID">0_userdata.0.Test.CardPowerExample.DP5Value</field>
                      </block>
                    </value>
                    <value name="ADD5">
                      <block type="get_value" id="RbraYRc5lMv_2nBn]s|j">
                        <field name="ATTR">val</field>
                        <field name="OID">0_userdata.0.Test.CardPowerExample.DP6Value</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="variables_set" id="EXJGQ{s2^,Wn|^v;D53_">
                    <field name="VAR" id="2qF4}%9QgN#!2:7fs}B#">dpValuesMax</field>
                    <value name="VALUE">
                      <block type="lists_create_with" id="RoIiqrqyZp}cEXhETNr%">
                        <mutation items="6"></mutation>
                        <value name="ADD0">
                          <block type="math_number" id="o+a`|L*:@r6d`NBuPk^d">
                            <field name="NUM">3</field>
                          </block>
                        </value>
                        <value name="ADD1">
                          <block type="math_number" id="VrFGW+;s#5YuhL~GY+}3">
                            <field name="NUM">7</field>
                          </block>
                        </value>
                        <value name="ADD2">
                          <block type="math_number" id="}[uR.(^hV.*pn@xZn/dg">
                            <field name="NUM">5</field>
                          </block>
                        </value>
                        <value name="ADD3">
                          <block type="math_number" id=")ALX-Iz6|@6_%Rd/%djO">
                            <field name="NUM">0</field>
                          </block>
                        </value>
                        <value name="ADD4">
                          <block type="math_number" id="@5cK2W*-u.?lAY#:`8w`">
                            <field name="NUM">0</field>
                          </block>
                        </value>
                        <value name="ADD5">
                          <block type="math_number" id="TQvEpDpN[Y*_Bjx)Ir9a">
                            <field name="NUM">4.6</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <next>
                      <block type="variables_set" id="H4-;]={kR*gZ[8]H!!]7">
                        <field name="VAR" id="cqo]H%;{[I_)-Jq;Y8jl">valueDirection</field>
                        <value name="VALUE">
                          <block type="lists_create_with" id="Qf4JWYEW}SBEh?Xuc[rZ">
                            <mutation items="6"></mutation>
                            <value name="ADD0">
                              <block type="text" id="J,:HYjH`vqGRWp5*`M:L">
                                <field name="TEXT">both</field>
                              </block>
                            </value>
                            <value name="ADD1">
                              <block type="text" id="bPYSMNO~l84K#PIns~L9">
                                <field name="TEXT">in</field>
                              </block>
                            </value>
                            <value name="ADD2">
                              <block type="text" id="N:m^U1uL~$NMVm}ReOn8">
                                <field name="TEXT">in</field>
                              </block>
                            </value>
                            <value name="ADD3">
                              <block type="text" id="zKz!ga+YM1SYE0ZecGMl">
                                <field name="TEXT">out</field>
                              </block>
                            </value>
                            <value name="ADD4">
                              <block type="text" id="/-BkYtI?z4$W7Bu5hAbX">
                                <field name="TEXT">both</field>
                              </block>
                            </value>
                            <value name="ADD5">
                              <block type="text" id="Y;O/5C6/:DD{Kq{U7FN?">
                                <field name="TEXT">out</field>
                              </block>
                            </value>
                          </block>
                        </value>
                        <next>
                          <block type="variables_set" id="p0|lV1)BG?(}o}uotZRz">
                            <field name="VAR" id="?wzEQN^Kk/mY4n0,{$/u">iconString</field>
                            <value name="VALUE">
                              <block type="lists_create_with" id="3E{]?|8WaGL_AZnBKBa5">
                                <mutation items="6"></mutation>
                                <value name="ADD0">
                                  <block type="text" id="`khss9NumH_2/(YFcKy)">
                                    <field name="TEXT">battery-charging-60</field>
                                  </block>
                                </value>
                                <value name="ADD1">
                                  <block type="text" id=")Zjz333zV:9d%v;,i[Oy">
                                    <field name="TEXT">solar-power-variant</field>
                                  </block>
                                </value>
                                <value name="ADD2">
                                  <block type="text" id="HFSg3z!52]|T4[jB9LZ!">
                                    <field name="TEXT">wind-turbine</field>
                                  </block>
                                </value>
                                <value name="ADD3">
                                  <block type="text" id=")3HwrJMIuC7EYs:Cwg78">
                                    <field name="TEXT">shape</field>
                                  </block>
                                </value>
                                <value name="ADD4">
                                  <block type="text" id="vYK)Flxhl5m3n/.j),N6">
                                    <field name="TEXT">transmission-tower</field>
                                  </block>
                                </value>
                                <value name="ADD5">
                                  <block type="text" id="OTjIrp6Ktp[tZ-:SXY/l">
                                    <field name="TEXT">car</field>
                                  </block>
                                </value>
                              </block>
                            </value>
                            <next>
                              <block type="variables_set" id="p6/9c@4Yg@f#u[G-h@c2">
                                <field name="VAR" id="E`|=%twhb7vm1+r?}VX?">dpValueUnit</field>
                                <value name="VALUE">
                                  <block type="lists_create_with" id="lG5w-:08GcGgt~lJ`E`D">
                                    <mutation items="6"></mutation>
                                    <value name="ADD0">
                                      <block type="text" id="@(Nb04/E(iEr](Qrd7?,">
                                        <field name="TEXT">kW</field>
                                      </block>
                                    </value>
                                    <value name="ADD1">
                                      <block type="text" id="MNF#Z!=fPkcl$oCSHc!;">
                                        <field name="TEXT">kW</field>
                                      </block>
                                    </value>
                                    <value name="ADD2">
                                      <block type="text" id="(uRQC@57$Eh0$x4u~UH{">
                                        <field name="TEXT">kW</field>
                                      </block>
                                    </value>
                                    <value name="ADD3">
                                      <block type="text" id="YvoqM?Vh=#:CVw;yQ3;J">
                                        <field name="TEXT">kW</field>
                                      </block>
                                    </value>
                                    <value name="ADD4">
                                      <block type="text" id="@n$2BsR0E5RHr_mdQ01x">
                                        <field name="TEXT">kW</field>
                                      </block>
                                    </value>
                                    <value name="ADD5">
                                      <block type="text" id="A=VzrMjHqC2.X.uMZ-3H">
                                        <field name="TEXT">kW</field>
                                      </block>
                                    </value>
                                  </block>
                                </value>
                                <next>
                                  <block type="variables_set" id="t:{?7[oytX,YX#1@[H.{">
                                    <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                    <value name="VALUE">
                                      <block type="lists_create_with" id="R!_U^6djhs}lxzUF=FiD">
                                        <mutation items="0"></mutation>
                                      </block>
                                    </value>
                                    <next>
                                      <block type="variables_set" id="DwK_Qat1c9Dd1Nwhbt(i">
                                        <field name="VAR" id="E57P;3$~H@U7xnh3-3~T">j</field>
                                        <value name="VALUE">
                                          <block type="math_number" id="zej=5Ps{AUPWp9x7p*~r">
                                            <field name="NUM">0</field>
                                          </block>
                                        </value>
                                        <next>
                                          <block type="variables_set" id="E)0RSe?/pawksih3Q.62">
                                            <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                            <value name="VALUE">
                                              <block type="math_number" id="%XvIDn2_Y;EO?[Hc%1aN">
                                                <field name="NUM">1</field>
                                              </block>
                                            </value>
                                            <next>
                                              <block type="variables_set" id="s2I$8(di$Xsj_LkfzXph">
                                                <field name="VAR" id="ka?!8/C5fALo,cmSVoD;">outJSON</field>
                                                <value name="VALUE">
                                                  <block type="text" id="(S^Q.m@M@ptBZ86-qaML">
                                                    <field name="TEXT">[</field>
                                                  </block>
                                                </value>
                                                <next>
                                                  <block type="controls_forEach" id="i,+?$we^rwX?@iRGoMUh">
                                                    <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                    <value name="LIST">
                                                      <block type="variables_get" id="Or{G}^YOwN:TBXPFj$uF">
                                                        <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                                                      </block>
                                                    </value>
                                                    <statement name="DO">
                                                      <block type="variables_set" id="7}d)qbeMnK/VjAhN,-W0">
                                                        <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                        <value name="VALUE">
                                                          <block type="math_number" id="tS_-*q`vXVT0c%Pv9gx!">
                                                            <field name="NUM">10</field>
                                                          </block>
                                                        </value>
                                                        <next>
                                                          <block type="math_change" id="nb?3Tvif2Y*EL=TZB.82">
                                                            <field name="VAR" id="E57P;3$~H@U7xnh3-3~T">j</field>
                                                            <value name="DELTA">
                                                              <shadow type="math_number" id="CVG7es.lfu1?K2?j6cyY">
                                                                <field name="NUM">1</field>
                                                              </shadow>
                                                              <block type="math_number" id="]6G;QIMf#wEdwowgf,tT">
                                                                <field name="NUM">1</field>
                                                              </block>
                                                            </value>
                                                            <next>
                                                              <block type="variables_set" id="f0%@7Fpd+`sn,qC=-Z_F">
                                                                <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                                                <value name="VALUE">
                                                                  <block type="math_number" id="^NS.)ChZGsdo-kLc)3DV">
                                                                    <field name="NUM">1</field>
                                                                  </block>
                                                                </value>
                                                                <next>
                                                                  <block type="logic_switch_case" id="?rc8fAT.%$n9TAi*}/FS">
                                                                    <mutation xmlns="http://www.w3.org/1999/xhtml" case="5"></mutation>
                                                                    <value name="CONDITION">
                                                                      <block type="variables_get" id="P@oKS=~atXPe?.*eq4Eb">
                                                                        <field name="VAR" id="E57P;3$~H@U7xnh3-3~T">j</field>
                                                                      </block>
                                                                    </value>
                                                                    <value name="CASECONDITION0">
                                                                      <block type="math_number" id="2|u@}]*)IbKVakgtkM_G">
                                                                        <field name="NUM">1</field>
                                                                      </block>
                                                                    </value>
                                                                    <statement name="CASE0">
                                                                      <block type="variables_set" id="XB3XeSabF]hS.ZZe~M!7">
                                                                        <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                        <value name="VALUE">
                                                                          <block type="math_arithmetic" id="lo{9PjyIE]RYJ3Avp;ps" inline="false">
                                                                            <field name="OP">MINUS</field>
                                                                            <value name="A">
                                                                              <shadow type="math_number" id="S1*u]!+Otl8=c?RI~Mxf">
                                                                                <field name="NUM">1</field>
                                                                              </shadow>
                                                                              <block type="math_arithmetic" id="m?U`+;K2@C1zTl2}3iB_" inline="false">
                                                                                <field name="OP">ADD</field>
                                                                                <value name="A">
                                                                                  <shadow type="math_number">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="lists_getIndex" id="%]iyQX%3$;i4Ux`X62nh">
                                                                                    <mutation statement="false" at="true"></mutation>
                                                                                    <field name="MODE">GET</field>
                                                                                    <field name="WHERE">FROM_START</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="variables_get" id="qJe@:jj|=AuCaTIJpc/a">
                                                                                        <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="AT">
                                                                                      <block type="math_number" id="?TMiQp][7|p*@A.f+KwP">
                                                                                        <field name="NUM">2</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <shadow type="math_number">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="lists_getIndex" id="2EaQP[V7J28JKJHntM~S">
                                                                                    <mutation statement="false" at="true"></mutation>
                                                                                    <field name="MODE">GET</field>
                                                                                    <field name="WHERE">FROM_START</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="variables_get" id="qERh?9nzPAPA3KCs$?%/">
                                                                                        <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="AT">
                                                                                      <block type="math_number" id="J3jdHM+]h;r[w#g?cETV">
                                                                                        <field name="NUM">3</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <value name="B">
                                                                              <shadow type="math_number" id="O?_#:A*4daH|)-N1^[!X">
                                                                                <field name="NUM">1</field>
                                                                              </shadow>
                                                                              <block type="math_arithmetic" id="B$.c.g=Mi,:?ITuSCT8[" inline="false">
                                                                                <field name="OP">ADD</field>
                                                                                <value name="A">
                                                                                  <shadow type="math_number">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="lists_getIndex" id="-RYZVsYoe:QgBLr_FgIa">
                                                                                    <mutation statement="false" at="true"></mutation>
                                                                                    <field name="MODE">GET</field>
                                                                                    <field name="WHERE">FROM_START</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="variables_get" id="2saVMP2gSyK%{kZt-l~M">
                                                                                        <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="AT">
                                                                                      <block type="math_number" id=",Bl!+UOx2Tg10b}BBiKj">
                                                                                        <field name="NUM">4</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <shadow type="math_number">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="lists_getIndex" id="gNT]MTajRNmsI@QquY@L">
                                                                                    <mutation statement="false" at="true"></mutation>
                                                                                    <field name="MODE">GET</field>
                                                                                    <field name="WHERE">FROM_START</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="variables_get" id=".0k2K{H%~tOBfnblTyHp">
                                                                                        <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="AT">
                                                                                      <block type="math_number" id="VvvGCgZ2iaUQ].85k)4L">
                                                                                        <field name="NUM">6</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                        <next>
                                                                          <block type="controls_if" id="ePtVD?cf;Qehe7+U7~#C">
                                                                            <mutation else="1"></mutation>
                                                                            <value name="IF0">
                                                                              <block type="logic_compare" id="MZmZ0yHAWR/Y{C8Hl1f{">
                                                                                <field name="OP">LT</field>
                                                                                <value name="A">
                                                                                  <block type="variables_get" id="[tBv?;RiMir6Wg?p.~(e">
                                                                                    <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <block type="math_number" id="%jiuT/A:`DWvx[wDKv$x">
                                                                                    <field name="NUM">0</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="DO0">
                                                                              <block type="variables_set" id="W_nkkduHvFW94R@D5K.#">
                                                                                <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                <value name="VALUE">
                                                                                  <block type="math_arithmetic" id="}(Wj(K+t@sEqVu}a*]@h">
                                                                                    <field name="OP">MULTIPLY</field>
                                                                                    <value name="A">
                                                                                      <shadow type="math_number" id="D|HWWie|JnMj1/WaDLRg">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="variables_get" id="*Cb8Fo.SFm-5gnX62$h(">
                                                                                        <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <shadow type="math_number" id="=tZPERd`UtDNEF[2/4:?">
                                                                                        <field name="NUM">-1</field>
                                                                                      </shadow>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <next>
                                                                                  <block type="variables_set" id="Zwq%-VbD;)8^]IQ10fld">
                                                                                    <field name="VAR" id="cqo]H%;{[I_)-Jq;Y8jl">valueDirection</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="text" id="%Kjxc;t=Q(4LE}T[hQ{,">
                                                                                        <field name="TEXT">out</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <next>
                                                                                      <block type="variables_set" id="3h]L(Cp1vQ,{QTk}=$YG">
                                                                                        <field name="VAR" id="=J?O~NeDtbS/i^;4)HAs">bat_loading</field>
                                                                                        <value name="VALUE">
                                                                                          <block type="logic_boolean" id="kgIE[wl2VnRess0?(^2@">
                                                                                            <field name="BOOL">FALSE</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </next>
                                                                                  </block>
                                                                                </next>
                                                                              </block>
                                                                            </statement>
                                                                            <statement name="ELSE">
                                                                              <block type="variables_set" id="%fyc7qvk%p?9[OR3;R@j">
                                                                                <field name="VAR" id="cqo]H%;{[I_)-Jq;Y8jl">valueDirection</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="ozP{s~Z/S:D0)Gj/bbot">
                                                                                    <field name="TEXT">in</field>
                                                                                  </block>
                                                                                </value>
                                                                                <next>
                                                                                  <block type="variables_set" id="%q^Vqp_a(v+V:/^cIUv2">
                                                                                    <field name="VAR" id="=J?O~NeDtbS/i^;4)HAs">bat_loading</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="logic_boolean" id="a9aJI.jBrZ4bvHVzk$+I">
                                                                                        <field name="BOOL">TRUE</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </next>
                                                                              </block>
                                                                            </statement>
                                                                            <next>
                                                                              <block type="controls_if" id=")b;}hpIm[3[al26Ru_%r">
                                                                                <value name="IF0">
                                                                                  <block type="logic_compare" id="-T!W98kc|IH}=[0]^{m)">
                                                                                    <field name="OP">GT</field>
                                                                                    <value name="A">
                                                                                      <block type="variables_get" id="q/bfoi41{$F6{sWF#pR)">
                                                                                        <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <block type="lists_getIndex" id="QYeDMA_nD}eTGrf*a~M/">
                                                                                        <mutation statement="false" at="true"></mutation>
                                                                                        <field name="MODE">GET</field>
                                                                                        <field name="WHERE">FROM_START</field>
                                                                                        <value name="VALUE">
                                                                                          <block type="variables_get" id="rOmD1p21}}MR,CnM1Fxv">
                                                                                            <field name="VAR" id="2qF4}%9QgN#!2:7fs}B#">dpValuesMax</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="AT">
                                                                                          <block type="math_number" id="`*OM*KhvC)e#]-R[s#6H">
                                                                                            <field name="NUM">1</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <statement name="DO0">
                                                                                  <block type="variables_set" id="gS+iQn-R=vr^F3F(g#s(">
                                                                                    <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="lists_getIndex" id="4l4Sea1CPV=uo@sEnA5-">
                                                                                        <mutation statement="false" at="true"></mutation>
                                                                                        <field name="MODE">GET</field>
                                                                                        <field name="WHERE">FROM_START</field>
                                                                                        <value name="VALUE">
                                                                                          <block type="variables_get" id="-EFq80^?KF/3Ucc7wnQt">
                                                                                            <field name="VAR" id="2qF4}%9QgN#!2:7fs}B#">dpValuesMax</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="AT">
                                                                                          <block type="math_number" id=",7?MT}/(D0S?$laH1B$/">
                                                                                            <field name="NUM">1</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </statement>
                                                                                <next>
                                                                                  <block type="variables_set" id="0L%oUl9TNg@h^ZzaVxjb">
                                                                                    <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="math_arithmetic" id="MLr9S1~X`5Gby2r{ef$|" inline="false">
                                                                                        <field name="OP">DIVIDE</field>
                                                                                        <value name="A">
                                                                                          <shadow type="math_number">
                                                                                            <field name="NUM">1</field>
                                                                                          </shadow>
                                                                                          <block type="math_arithmetic" id="8ZtpxsqXfaUzOK)|7ew`">
                                                                                            <field name="OP">MULTIPLY</field>
                                                                                            <value name="A">
                                                                                              <shadow type="math_number">
                                                                                                <field name="NUM">1</field>
                                                                                              </shadow>
                                                                                              <block type="variables_get" id="?]UN94!At.EdQW5]qZ!y">
                                                                                                <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                              </block>
                                                                                            </value>
                                                                                            <value name="B">
                                                                                              <shadow type="math_number" id="(*[Fz$!09Hy=Sq*4nmd.">
                                                                                                <field name="NUM">10</field>
                                                                                              </shadow>
                                                                                            </value>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="B">
                                                                                          <shadow type="math_number">
                                                                                            <field name="NUM">1</field>
                                                                                          </shadow>
                                                                                          <block type="lists_getIndex" id="U%DuNj?0S/B(#_dbr^cY">
                                                                                            <mutation statement="false" at="true"></mutation>
                                                                                            <field name="MODE">GET</field>
                                                                                            <field name="WHERE">FROM_START</field>
                                                                                            <value name="VALUE">
                                                                                              <block type="variables_get" id="adx6n:*#?r^wzsgLxrEC">
                                                                                                <field name="VAR" id="2qF4}%9QgN#!2:7fs}B#">dpValuesMax</field>
                                                                                              </block>
                                                                                            </value>
                                                                                            <value name="AT">
                                                                                              <block type="math_number" id="+~#d%Vj9PkIL70)lwyY@">
                                                                                                <field name="NUM">1</field>
                                                                                              </block>
                                                                                            </value>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                    <next>
                                                                                      <block type="controls_if" id="iMW=MDlZwFZ8X2TNnR8m">
                                                                                        <mutation else="1"></mutation>
                                                                                        <value name="IF0">
                                                                                          <block type="logic_compare" id=";J3D^rUqCI/a#%w`_NPq">
                                                                                            <field name="OP">EQ</field>
                                                                                            <value name="A">
                                                                                              <block type="variables_get" id="pQ?`6^N:/q35Its/]-V-">
                                                                                                <field name="VAR" id="cqo]H%;{[I_)-Jq;Y8jl">valueDirection</field>
                                                                                              </block>
                                                                                            </value>
                                                                                            <value name="B">
                                                                                              <block type="text" id="6]MPI5om6#Na)#nRf.e}">
                                                                                                <field name="TEXT">out</field>
                                                                                              </block>
                                                                                            </value>
                                                                                          </block>
                                                                                        </value>
                                                                                        <statement name="DO0">
                                                                                          <block type="variables_set" id="/RVN66aJvVUHok],DmRT">
                                                                                            <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                                                                            <value name="VALUE">
                                                                                              <block type="variables_get" id="`|2svc_ow*,=xGh4+)?}">
                                                                                                <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                                              </block>
                                                                                            </value>
                                                                                          </block>
                                                                                        </statement>
                                                                                        <statement name="ELSE">
                                                                                          <block type="variables_set" id="YK+X$p;}J2#ysWtfaA_R">
                                                                                            <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                                                                            <value name="VALUE">
                                                                                              <block type="math_arithmetic" id="]B9*|_4lCY;7LYod4OK8">
                                                                                                <field name="OP">DIVIDE</field>
                                                                                                <value name="A">
                                                                                                  <shadow type="math_number">
                                                                                                    <field name="NUM">1</field>
                                                                                                  </shadow>
                                                                                                  <block type="variables_get" id="W[?GomIwqdldCqU:__aY">
                                                                                                    <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                                                  </block>
                                                                                                </value>
                                                                                                <value name="B">
                                                                                                  <shadow type="math_number" id="}b([$tpWcos,QU-s(SCf">
                                                                                                    <field name="NUM">-1</field>
                                                                                                  </shadow>
                                                                                                </value>
                                                                                              </block>
                                                                                            </value>
                                                                                          </block>
                                                                                        </statement>
                                                                                        <next>
                                                                                          <block type="variables_set" id="@;ue{Kv[xX_,3qF`]aZ?">
                                                                                            <field name="VAR" id="DeFZ=AKn8o[,ad:-P/+#">bat_temp</field>
                                                                                            <value name="VALUE">
                                                                                              <block type="variables_get" id="xExW$E6,c?c?YU|lA!7c">
                                                                                                <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                              </block>
                                                                                            </value>
                                                                                          </block>
                                                                                        </next>
                                                                                      </block>
                                                                                    </next>
                                                                                  </block>
                                                                                </next>
                                                                              </block>
                                                                            </next>
                                                                          </block>
                                                                        </next>
                                                                      </block>
                                                                    </statement>
                                                                    <value name="CASECONDITION1">
                                                                      <block type="math_number" id="MxHl!taWA{F#LhV}oo8`">
                                                                        <field name="NUM">2</field>
                                                                      </block>
                                                                    </value>
                                                                    <statement name="CASE1">
                                                                      <block type="variables_set" id="Kxhtz@lg5Z{G!m6j+qT2">
                                                                        <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                        <value name="VALUE">
                                                                          <block type="math_arithmetic" id="9CqpV4[%]ajvk~[tqK6P">
                                                                            <field name="OP">MINUS</field>
                                                                            <value name="A">
                                                                              <shadow type="math_number" id="k}*a:)({$%.cR3dec{/W">
                                                                                <field name="NUM">10</field>
                                                                              </shadow>
                                                                            </value>
                                                                            <value name="B">
                                                                              <shadow type="math_number" id="nSZ]jB@1^iAo3q#;yB}j">
                                                                                <field name="NUM">1</field>
                                                                              </shadow>
                                                                              <block type="math_arithmetic" id="KLXnNe~}$8BHA`[ZG3Sh" inline="false">
                                                                                <field name="OP">DIVIDE</field>
                                                                                <value name="A">
                                                                                  <shadow type="math_number">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="math_arithmetic" id="|.gcQPAmnbFoNtZ7jgMu">
                                                                                    <field name="OP">MULTIPLY</field>
                                                                                    <value name="A">
                                                                                      <shadow type="math_number">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="variables_get" id="]o{Y^NLma(Xr3JJOB8qp">
                                                                                        <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <shadow type="math_number" id="cD:UFl{p`-m+HP|uUn6e">
                                                                                        <field name="NUM">10</field>
                                                                                      </shadow>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <shadow type="math_number">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="lists_getIndex" id="M:|^GAvKnEM_*xhA6)vA">
                                                                                    <mutation statement="false" at="true"></mutation>
                                                                                    <field name="MODE">GET</field>
                                                                                    <field name="WHERE">FROM_START</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="variables_get" id="Hq/TJX50rl%u.IqrAn_@">
                                                                                        <field name="VAR" id="2qF4}%9QgN#!2:7fs}B#">dpValuesMax</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="AT">
                                                                                      <block type="math_number" id="[}ZuT|F#+C=PBTZ$Yyw*">
                                                                                        <field name="NUM">2</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                        <next>
                                                                          <block type="variables_set" id="uT%zaCD?tu6TRurpr{^.">
                                                                            <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                                                            <value name="VALUE">
                                                                              <block type="math_arithmetic" id="1=il62~qQ8#,5lbVSK|.">
                                                                                <field name="OP">MINUS</field>
                                                                                <value name="A">
                                                                                  <shadow type="math_number" id="-GZr4?{Afnt6^^dioSvj">
                                                                                    <field name="NUM">10</field>
                                                                                  </shadow>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <shadow type="math_number" id="L[C_ist8[LY%iQ`YI#g$">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="variables_get" id="mv}_7z}v2C_)8!6h,ky.">
                                                                                    <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <next>
                                                                              <block type="controls_if" id="A?hV/T5EpUg=]7=qjW]N">
                                                                                <value name="IF0">
                                                                                  <block type="logic_compare" id="!Dq:Q;L6uABTDLM#=HA^">
                                                                                    <field name="OP">EQ</field>
                                                                                    <value name="A">
                                                                                      <block type="variables_get" id="~{(#NRMNGAW[4E8CCcrt">
                                                                                        <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <block type="math_number" id="1W4nrudv!m]mr0MF@IUT">
                                                                                        <field name="NUM">0</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <statement name="DO0">
                                                                                  <block type="variables_set" id="(Y(]6OB6,8]AaSh%#CX(">
                                                                                    <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="math_number" id="bjRrfm}!yQtR2iYFxdH0">
                                                                                        <field name="NUM">0</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </statement>
                                                                              </block>
                                                                            </next>
                                                                          </block>
                                                                        </next>
                                                                      </block>
                                                                    </statement>
                                                                    <value name="CASECONDITION2">
                                                                      <block type="math_number" id="6(d?X4C(idDhgX1rQk#V">
                                                                        <field name="NUM">3</field>
                                                                      </block>
                                                                    </value>
                                                                    <statement name="CASE2">
                                                                      <block type="variables_set" id="ubanKD%4vS?dzQDrF+Kp">
                                                                        <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                        <value name="VALUE">
                                                                          <block type="math_arithmetic" id="o-x?2[I?~G/m5}~CPZ1O">
                                                                            <field name="OP">MINUS</field>
                                                                            <value name="A">
                                                                              <shadow type="math_number" id="FdObrHNLMM,7eeo2^)/r">
                                                                                <field name="NUM">10</field>
                                                                              </shadow>
                                                                            </value>
                                                                            <value name="B">
                                                                              <shadow type="math_number" id="GyS5#[!vr1VYV-PYM4@l">
                                                                                <field name="NUM">1</field>
                                                                              </shadow>
                                                                              <block type="math_arithmetic" id="gAD2zFm}yCw([3(Sc_jy" inline="false">
                                                                                <field name="OP">DIVIDE</field>
                                                                                <value name="A">
                                                                                  <shadow type="math_number">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="math_arithmetic" id="Owr47y?;NX~9Guw52itr">
                                                                                    <field name="OP">MULTIPLY</field>
                                                                                    <value name="A">
                                                                                      <shadow type="math_number">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="variables_get" id=":6`uCgW6^WlWFI+dO||Z">
                                                                                        <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <shadow type="math_number" id="fVca?BhMKp.$Oj8m2KN#">
                                                                                        <field name="NUM">10</field>
                                                                                      </shadow>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <shadow type="math_number">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="lists_getIndex" id="zK2,Q``HmXYJPB4H$K:N">
                                                                                    <mutation statement="false" at="true"></mutation>
                                                                                    <field name="MODE">GET</field>
                                                                                    <field name="WHERE">FROM_START</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="variables_get" id="IH/UO7W@5ly-Xzx@q=HB">
                                                                                        <field name="VAR" id="2qF4}%9QgN#!2:7fs}B#">dpValuesMax</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="AT">
                                                                                      <block type="math_number" id="{)4b]!e6!d`J8J5RWEQq">
                                                                                        <field name="NUM">3</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                        <next>
                                                                          <block type="variables_set" id="Qgr=;`@LejLmaj{(]tNT">
                                                                            <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                                                            <value name="VALUE">
                                                                              <block type="math_arithmetic" id="IyJ`B5oiVYo:I9_44sZg">
                                                                                <field name="OP">MINUS</field>
                                                                                <value name="A">
                                                                                  <shadow type="math_number" id="6!a(Q;LOn7f)`sZNm/Ze">
                                                                                    <field name="NUM">10</field>
                                                                                  </shadow>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <shadow type="math_number">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="variables_get" id=":g`p=Z?[aJf%`.3-W}hl">
                                                                                    <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <next>
                                                                              <block type="controls_if" id="X5t+k;DgtQd}W~*.r-et">
                                                                                <value name="IF0">
                                                                                  <block type="logic_compare" id="ws@t@D.nPvH:qL:|usMH">
                                                                                    <field name="OP">EQ</field>
                                                                                    <value name="A">
                                                                                      <block type="variables_get" id="q0HVHa-.zEdQV{`~r!]u">
                                                                                        <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <block type="math_number" id="pOEvz#j]W[~1+Hul(2y,">
                                                                                        <field name="NUM">0</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <statement name="DO0">
                                                                                  <block type="variables_set" id="*w.3$i6d8CHYNk[qA`%U">
                                                                                    <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="math_number" id="J6qFhe!yIIq;9%iv+]2u">
                                                                                        <field name="NUM">0</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </statement>
                                                                              </block>
                                                                            </next>
                                                                          </block>
                                                                        </next>
                                                                      </block>
                                                                    </statement>
                                                                    <value name="CASECONDITION3">
                                                                      <block type="math_number" id="VtXUq9z9s)wfZlR5V,A.">
                                                                        <field name="NUM">4</field>
                                                                      </block>
                                                                    </value>
                                                                    <statement name="CASE3">
                                                                      <block type="variables_set" id="KTaYVs%y35N$QjeoBf@B">
                                                                        <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                        <value name="VALUE">
                                                                          <block type="math_arithmetic" id="J5R%1F*)Vho(9YB:tt?3" inline="false">
                                                                            <field name="OP">DIVIDE</field>
                                                                            <value name="A">
                                                                              <shadow type="math_number">
                                                                                <field name="NUM">1</field>
                                                                              </shadow>
                                                                              <block type="math_arithmetic" id="(ERR6]Q(mKIb6no/MM3r">
                                                                                <field name="OP">MULTIPLY</field>
                                                                                <value name="A">
                                                                                  <shadow type="math_number">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="variables_get" id="~p#d8Eaz!//cK1u{4-7d">
                                                                                    <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <shadow type="math_number" id="v`;vNaP:-$v7(Yxx~u9i">
                                                                                    <field name="NUM">10</field>
                                                                                  </shadow>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <value name="B">
                                                                              <shadow type="math_number" id="0xheCy(ow;0!$ROAW$xZ">
                                                                                <field name="NUM">1</field>
                                                                              </shadow>
                                                                              <block type="variables_get" id="g~eh|T]-t:C.0N-74BE%">
                                                                                <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                        <next>
                                                                          <block type="variables_set" id="-z$]GmFNPf;0gQx4WEVU">
                                                                            <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                                                            <value name="VALUE">
                                                                              <block type="variables_get" id="$HpZL0FA)Gne7N1E}GoO">
                                                                                <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </next>
                                                                      </block>
                                                                    </statement>
                                                                    <value name="CASECONDITION4">
                                                                      <block type="math_number" id="C}ssF_5_]6G6#CN{D]N`">
                                                                        <field name="NUM">5</field>
                                                                      </block>
                                                                    </value>
                                                                    <statement name="CASE4">
                                                                      <block type="controls_if" id="kidnBzfOa;t)6/A:+3J8">
                                                                        <mutation else="1"></mutation>
                                                                        <value name="IF0">
                                                                          <block type="variables_get" id="Q7A$Ou6)sHsRr@+=N76C">
                                                                            <field name="VAR" id="=J?O~NeDtbS/i^;4)HAs">bat_loading</field>
                                                                          </block>
                                                                        </value>
                                                                        <statement name="DO0">
                                                                          <block type="variables_set" id="Nct,[abOBG3mm(%wE_Be">
                                                                            <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                            <value name="VALUE">
                                                                              <block type="math_arithmetic" id="7lG-_Gybe2eA.@S:GMtR" inline="false">
                                                                                <field name="OP">MINUS</field>
                                                                                <value name="A">
                                                                                  <shadow type="math_number" id="byg3Oby*KtP[a~!@`tc|">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="math_arithmetic" id="ObkVJ?0R?eN_UqT]!)`S" inline="false">
                                                                                    <field name="OP">ADD</field>
                                                                                    <value name="A">
                                                                                      <shadow type="math_number">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="lists_getIndex" id="c`@[^X)S,xkqrvp9$h-t">
                                                                                        <mutation statement="false" at="true"></mutation>
                                                                                        <field name="MODE">GET</field>
                                                                                        <field name="WHERE">FROM_START</field>
                                                                                        <value name="VALUE">
                                                                                          <block type="variables_get" id="lXf6JKORVnyHF}Za];Og">
                                                                                            <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="AT">
                                                                                          <block type="math_number" id="yXAC|B++,+(t.7r8G-.a">
                                                                                            <field name="NUM">2</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <shadow type="math_number">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="lists_getIndex" id="G(Rv__o9M9VUla?6Z.Rd">
                                                                                        <mutation statement="false" at="true"></mutation>
                                                                                        <field name="MODE">GET</field>
                                                                                        <field name="WHERE">FROM_START</field>
                                                                                        <value name="VALUE">
                                                                                          <block type="variables_get" id=":cjXxYAC5|NQ$+Pj6s[l">
                                                                                            <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="AT">
                                                                                          <block type="math_number" id="g{GByPhj#tP3!GH[p4z.">
                                                                                            <field name="NUM">3</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <shadow type="math_number">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="math_arithmetic" id="5my{5;P^Q!ge3|Q5Dv$P" inline="false">
                                                                                    <field name="OP">ADD</field>
                                                                                    <value name="A">
                                                                                      <shadow type="math_number" id="X(-TQhrWU?D@kz:oR,WC">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="variables_get" id="hWhHT@dkoLlT1AE/j/ko">
                                                                                        <field name="VAR" id="DeFZ=AKn8o[,ad:-P/+#">bat_temp</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <shadow type="math_number" id="{aa($w3?;KKH)zEn@(vj">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="math_arithmetic" id="q^iOGe6B.:h+~3U#z2b/" inline="false">
                                                                                        <field name="OP">ADD</field>
                                                                                        <value name="A">
                                                                                          <shadow type="math_number">
                                                                                            <field name="NUM">1</field>
                                                                                          </shadow>
                                                                                          <block type="lists_getIndex" id="wVuS-jRE,=ZwF4:nI~$=">
                                                                                            <mutation statement="false" at="true"></mutation>
                                                                                            <field name="MODE">GET</field>
                                                                                            <field name="WHERE">FROM_START</field>
                                                                                            <value name="VALUE">
                                                                                              <block type="variables_get" id="b#gjn5Gu!CfB2Q7Q!eeQ">
                                                                                                <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                                                                                              </block>
                                                                                            </value>
                                                                                            <value name="AT">
                                                                                              <block type="math_number" id="qwTtUtri[3r]9.M[x!Tp">
                                                                                                <field name="NUM">4</field>
                                                                                              </block>
                                                                                            </value>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="B">
                                                                                          <shadow type="math_number">
                                                                                            <field name="NUM">1</field>
                                                                                          </shadow>
                                                                                          <block type="lists_getIndex" id="i$4Zrw;{De(j.V=}1Ost">
                                                                                            <mutation statement="false" at="true"></mutation>
                                                                                            <field name="MODE">GET</field>
                                                                                            <field name="WHERE">FROM_START</field>
                                                                                            <value name="VALUE">
                                                                                              <block type="variables_get" id="AhV[qz8fBopbl9;zM.G!">
                                                                                                <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                                                                                              </block>
                                                                                            </value>
                                                                                            <value name="AT">
                                                                                              <block type="math_number" id="b#sR_9Ccu+%_WQ6Dx3*Z">
                                                                                                <field name="NUM">6</field>
                                                                                              </block>
                                                                                            </value>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </statement>
                                                                        <statement name="ELSE">
                                                                          <block type="variables_set" id="PDJ9=JoZ9ED}}Hb*hi:N">
                                                                            <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                            <value name="VALUE">
                                                                              <block type="math_arithmetic" id="_=bNG+Sm!+OFqoX_8vQY" inline="false">
                                                                                <field name="OP">MINUS</field>
                                                                                <value name="A">
                                                                                  <shadow type="math_number" id="#fex1Sb-H!]PJ0-r;-N/">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="math_arithmetic" id="!JeqJ-UBPW`v/6dQZb*=" inline="false">
                                                                                    <field name="OP">ADD</field>
                                                                                    <value name="A">
                                                                                      <shadow type="math_number" id="~=M,Ei386FAu}=T7Yn3(">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="variables_get" id="CEI!s:[*TS`=4LCD2-6R">
                                                                                        <field name="VAR" id="DeFZ=AKn8o[,ad:-P/+#">bat_temp</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <shadow type="math_number" id=",:l(4if{jWbKdBmu#B7C">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="math_arithmetic" id="2PIcDWxOlRQ;j1c:`lAm" inline="false">
                                                                                        <field name="OP">ADD</field>
                                                                                        <value name="A">
                                                                                          <shadow type="math_number">
                                                                                            <field name="NUM">1</field>
                                                                                          </shadow>
                                                                                          <block type="lists_getIndex" id="XJbU=P[y-yYg1}Nb^0r5">
                                                                                            <mutation statement="false" at="true"></mutation>
                                                                                            <field name="MODE">GET</field>
                                                                                            <field name="WHERE">FROM_START</field>
                                                                                            <value name="VALUE">
                                                                                              <block type="variables_get" id="3DewSIkM(/*?gY5jN_O,">
                                                                                                <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                                                                                              </block>
                                                                                            </value>
                                                                                            <value name="AT">
                                                                                              <block type="math_number" id="^=W)sZhHn[L@zHby2:sl">
                                                                                                <field name="NUM">2</field>
                                                                                              </block>
                                                                                            </value>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="B">
                                                                                          <shadow type="math_number">
                                                                                            <field name="NUM">1</field>
                                                                                          </shadow>
                                                                                          <block type="lists_getIndex" id="6|([^@9YD)W+D!qfY%Ph">
                                                                                            <mutation statement="false" at="true"></mutation>
                                                                                            <field name="MODE">GET</field>
                                                                                            <field name="WHERE">FROM_START</field>
                                                                                            <value name="VALUE">
                                                                                              <block type="variables_get" id="wLM?GVx2c?g^]aW*B,?=">
                                                                                                <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                                                                                              </block>
                                                                                            </value>
                                                                                            <value name="AT">
                                                                                              <block type="math_number" id="LU:,WI!7~WVA:?pF5GmY">
                                                                                                <field name="NUM">3</field>
                                                                                              </block>
                                                                                            </value>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <shadow type="math_number">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="math_arithmetic" id="B1=:E08^zB_0BdsGD1n*" inline="false">
                                                                                    <field name="OP">ADD</field>
                                                                                    <value name="A">
                                                                                      <shadow type="math_number">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="lists_getIndex" id="b]h!v2di=u=f-:PTQzI.">
                                                                                        <mutation statement="false" at="true"></mutation>
                                                                                        <field name="MODE">GET</field>
                                                                                        <field name="WHERE">FROM_START</field>
                                                                                        <value name="VALUE">
                                                                                          <block type="variables_get" id="H1mbBTzr40*v[%!4.o3~">
                                                                                            <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="AT">
                                                                                          <block type="math_number" id="tl9`P)[:DpprxVO0@C}g">
                                                                                            <field name="NUM">4</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <shadow type="math_number">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="lists_getIndex" id="~X*iE4@S:-iCTS[oC4`O">
                                                                                        <mutation statement="false" at="true"></mutation>
                                                                                        <field name="MODE">GET</field>
                                                                                        <field name="WHERE">FROM_START</field>
                                                                                        <value name="VALUE">
                                                                                          <block type="variables_get" id="eNE_pSv$ZlU[ek*qIiH1">
                                                                                            <field name="VAR" id="6G7iw;bW2Tp2Y9U~#eDE">dpValues</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="AT">
                                                                                          <block type="math_number" id="m!Wo)*6Nz;!cch{r2_F-">
                                                                                            <field name="NUM">6</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </statement>
                                                                        <next>
                                                                          <block type="controls_if" id="[jKrsCx$*uxIV3d4=f^$">
                                                                            <mutation else="1"></mutation>
                                                                            <value name="IF0">
                                                                              <block type="logic_compare" id="!~E4ax?aNGuIapS9o$QO">
                                                                                <field name="OP">LT</field>
                                                                                <value name="A">
                                                                                  <block type="variables_get" id="o|3IQ6yrMK(`*^)zQY1B">
                                                                                    <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <block type="math_number" id="UtN)0v*Yr6kTAEz.0AYy">
                                                                                    <field name="NUM">0</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="DO0">
                                                                              <block type="variables_set" id="$_uET%Jfqx|q;rH6GBlR">
                                                                                <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                <value name="VALUE">
                                                                                  <block type="math_arithmetic" id="Ow_k29;Jo{7D!~0x6t(t">
                                                                                    <field name="OP">MULTIPLY</field>
                                                                                    <value name="A">
                                                                                      <shadow type="math_number">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="variables_get" id="e*@3~H77|g,bw8eUfSiJ">
                                                                                        <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <shadow type="math_number" id="@rm_)sP^@YcA#^ZhM5_T">
                                                                                        <field name="NUM">-1</field>
                                                                                      </shadow>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <next>
                                                                                  <block type="variables_set" id="4B]YzCNL1(k$%Dn79Mon">
                                                                                    <field name="VAR" id="cqo]H%;{[I_)-Jq;Y8jl">valueDirection</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="text" id="y8NtQiFC-g[7XUHwbf/1">
                                                                                        <field name="TEXT">out</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </next>
                                                                              </block>
                                                                            </statement>
                                                                            <statement name="ELSE">
                                                                              <block type="variables_set" id="-FZlp4wh:.5KXIB24;R1">
                                                                                <field name="VAR" id="cqo]H%;{[I_)-Jq;Y8jl">valueDirection</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text" id="o.2y56B=}Ye$~*QNvi=t">
                                                                                    <field name="TEXT">in</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                            <next>
                                                                              <block type="controls_if" id=",`?KBwKD!cHL%B#cza8u">
                                                                                <mutation else="1"></mutation>
                                                                                <value name="IF0">
                                                                                  <block type="logic_compare" id="q~2@%6,4$IOI3@JQuMr5">
                                                                                    <field name="OP">EQ</field>
                                                                                    <value name="A">
                                                                                      <block type="variables_get" id="i*6Ekv+X)_3Xm0L.u-Ms">
                                                                                        <field name="VAR" id="cqo]H%;{[I_)-Jq;Y8jl">valueDirection</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <block type="text" id=")@x@#~qgZ1^%B/n/O(tb">
                                                                                        <field name="TEXT">in</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <statement name="DO0">
                                                                                  <block type="variables_set" id="G#:2vJNix!V|5cT(}u*h">
                                                                                    <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="math_number" id="-2@;o[A4~)]iER;Jyz;T">
                                                                                        <field name="NUM">0</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <next>
                                                                                      <block type="variables_set" id="B7RD@H_X=Muti*[*gAR7">
                                                                                        <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                                                                        <value name="VALUE">
                                                                                          <block type="math_number" id="c^I-e0Gdrc3bg?i{F~0z">
                                                                                            <field name="NUM">5</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </next>
                                                                                  </block>
                                                                                </statement>
                                                                                <statement name="ELSE">
                                                                                  <block type="variables_set" id=",baev2Xhh70p{~%4#I#Z">
                                                                                    <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="math_number" id="X0z1rLojD1kRx/rh|#j5">
                                                                                        <field name="NUM">10</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <next>
                                                                                      <block type="variables_set" id="zVxggC%lsX2FeIIBVL=-">
                                                                                        <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                                                                        <value name="VALUE">
                                                                                          <block type="math_number" id=",ttB{esR+:;EGpC@I:GN">
                                                                                            <field name="NUM">-5</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </next>
                                                                                  </block>
                                                                                </statement>
                                                                                <next>
                                                                                  <block type="controls_if" id="bIyc/%3DylYIAkPl,Pv:">
                                                                                    <value name="IF0">
                                                                                      <block type="logic_compare" id="+.w](zc[!.bw~g=qr]n3">
                                                                                        <field name="OP">EQ</field>
                                                                                        <value name="A">
                                                                                          <block type="variables_get" id="1lu[N7=x9m}Cd$Xc|Uok">
                                                                                            <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="B">
                                                                                          <block type="math_number" id="iFBqvru$i5H/_MW@O@^Z">
                                                                                            <field name="NUM">0</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                    <statement name="DO0">
                                                                                      <block type="variables_set" id="}ia_(-[~~sBEPkK9VhjO">
                                                                                        <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                                                                        <value name="VALUE">
                                                                                          <block type="math_number" id="Cr(5|5}DuI$-JKREkyAW">
                                                                                            <field name="NUM">0</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </statement>
                                                                                  </block>
                                                                                </next>
                                                                              </block>
                                                                            </next>
                                                                          </block>
                                                                        </next>
                                                                      </block>
                                                                    </statement>
                                                                    <value name="CASECONDITION5">
                                                                      <block type="math_number" id="S!oaLH-.O@;nXJ^S+Rwr">
                                                                        <field name="NUM">6</field>
                                                                      </block>
                                                                    </value>
                                                                    <statement name="CASE5">
                                                                      <block type="variables_set" id="LhLB894EMkZhRJG0BlHl">
                                                                        <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                        <value name="VALUE">
                                                                          <block type="math_arithmetic" id="-_=KZZy#Dy`wqkd=qO[n" inline="false">
                                                                            <field name="OP">DIVIDE</field>
                                                                            <value name="A">
                                                                              <shadow type="math_number">
                                                                                <field name="NUM">1</field>
                                                                              </shadow>
                                                                              <block type="math_arithmetic" id="C8%e.OVR];$Z!3pc_{TJ">
                                                                                <field name="OP">MULTIPLY</field>
                                                                                <value name="A">
                                                                                  <shadow type="math_number">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="variables_get" id="q_e2IvcJuhX3`?[(/8%!">
                                                                                    <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <shadow type="math_number" id="c8;vm:Cs($+;]qy`.w[B">
                                                                                    <field name="NUM">10</field>
                                                                                  </shadow>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <value name="B">
                                                                              <shadow type="math_number">
                                                                                <field name="NUM">1</field>
                                                                              </shadow>
                                                                              <block type="lists_getIndex" id="+4k-7adO))/P;9@~a*9M">
                                                                                <mutation statement="false" at="true"></mutation>
                                                                                <field name="MODE">GET</field>
                                                                                <field name="WHERE">FROM_START</field>
                                                                                <value name="VALUE">
                                                                                  <block type="variables_get" id="$Mwg1_2VU~L$09y6Al)O">
                                                                                    <field name="VAR" id="2qF4}%9QgN#!2:7fs}B#">dpValuesMax</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="AT">
                                                                                  <block type="math_number" id=")~T,+LN`cP6n,nT-^f{B">
                                                                                    <field name="NUM">6</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                        <next>
                                                                          <block type="variables_set" id="yP5@YEG$$1@M|x$%wOn4">
                                                                            <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                                                            <value name="VALUE">
                                                                              <block type="math_arithmetic" id="2pEf65{$^bgX;B|X5r)v">
                                                                                <field name="OP">MINUS</field>
                                                                                <value name="A">
                                                                                  <shadow type="math_number" id="VFCRPUvQ6_S?(%!I/$x/">
                                                                                    <field name="NUM">10</field>
                                                                                  </shadow>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <shadow type="math_number" id="5;v~$RjMzItsT+l]IhO9">
                                                                                    <field name="NUM">1</field>
                                                                                  </shadow>
                                                                                  <block type="math_arithmetic" id="wHDB{Vz]10:/2a?CB~T%">
                                                                                    <field name="OP">DIVIDE</field>
                                                                                    <value name="A">
                                                                                      <shadow type="math_number">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="variables_get" id="bnMXP;O+.Dcs-$L/PHqy">
                                                                                        <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <shadow type="math_number" id="Hqk/bqsm{|VDUHPG!num">
                                                                                        <field name="NUM">2</field>
                                                                                      </shadow>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </next>
                                                                      </block>
                                                                    </statement>
                                                                    <next>
                                                                      <block type="variables_set" id="8n],JJL$zA{gPA~=$oj{">
                                                                        <field name="VAR" id="ka?!8/C5fALo,cmSVoD;">outJSON</field>
                                                                        <value name="VALUE">
                                                                          <block type="text_join" id="5xL#;w1O_$N13lGp%V_8">
                                                                            <mutation items="2"></mutation>
                                                                            <value name="ADD0">
                                                                              <block type="variables_get" id="eMeRx?fOF:x8e3;~o|V.">
                                                                                <field name="VAR" id="ka?!8/C5fALo,cmSVoD;">outJSON</field>
                                                                              </block>
                                                                            </value>
                                                                            <value name="ADD1">
                                                                              <block type="text_join" id="M^RsI*6fkXU(6{P_@ZxJ">
                                                                                <mutation items="15"></mutation>
                                                                                <value name="ADD0">
                                                                                  <block type="text" id="{%z6@x@GlB!LOAiCqSc@">
                                                                                    <field name="TEXT">{ "id" : </field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD1">
                                                                                  <block type="variables_get" id="C%R{G{QdN1ibc0ISc-T*">
                                                                                    <field name="VAR" id="E57P;3$~H@U7xnh3-3~T">j</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD2">
                                                                                  <block type="text" id=";^4oaT.sf)J9Oe?|MQ7l">
                                                                                    <field name="TEXT">, "value": </field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD3">
                                                                                  <block type="math_rndfixed" id="11so9L)?-SY#$f*dl=^i">
                                                                                    <field name="n">1</field>
                                                                                    <value name="x">
                                                                                      <shadow type="math_number" id="~/gWwu}?ovQaQ3KuM,r!">
                                                                                        <field name="NUM">3.1234</field>
                                                                                      </shadow>
                                                                                      <block type="variables_get" id="l7+y6bW{@HJD@-r,`TlR">
                                                                                        <field name="VAR" id="B2:D:XW|l:N~aV}wAHVT">i</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD4">
                                                                                  <block type="text" id="7mzD[d[)OM,TklX@g)#i">
                                                                                    <field name="TEXT">, "unit": "</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD5">
                                                                                  <block type="lists_getIndex" id="09(6caW1KP;6no91S^?S">
                                                                                    <mutation statement="false" at="true"></mutation>
                                                                                    <field name="MODE">GET</field>
                                                                                    <field name="WHERE">FROM_START</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="variables_get" id="#{9RAOOJDmTLX]ZgOSC4">
                                                                                        <field name="VAR" id="E`|=%twhb7vm1+r?}VX?">dpValueUnit</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="AT">
                                                                                      <block type="variables_get" id="sE|;{vs38H;$ay3?I+B9">
                                                                                        <field name="VAR" id="E57P;3$~H@U7xnh3-3~T">j</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD6">
                                                                                  <block type="text" id="et%T#xFZj}t;K)Ky?)CK">
                                                                                    <field name="TEXT">" , "direction" :  "</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD7">
                                                                                  <block type="variables_get" id="yk:E,GkHE$8Ak`g0-w,]">
                                                                                    <field name="VAR" id="cqo]H%;{[I_)-Jq;Y8jl">valueDirection</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD8">
                                                                                  <block type="text" id="r18:zw~bDMHDWRhdV}9+">
                                                                                    <field name="TEXT">" , "icon" : "</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD9">
                                                                                  <block type="lists_getIndex" id=".F4](Vtao?bnRGZ`oxw=">
                                                                                    <mutation statement="false" at="true"></mutation>
                                                                                    <field name="MODE">GET</field>
                                                                                    <field name="WHERE">FROM_START</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="variables_get" id="33uzbj3c2awR}hXgf1Af">
                                                                                        <field name="VAR" id="?wzEQN^Kk/mY4n0,{$/u">iconString</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="AT">
                                                                                      <block type="variables_get" id="3QlNvqs./;/!SRvOH`U^">
                                                                                        <field name="VAR" id="E57P;3$~H@U7xnh3-3~T">j</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD10">
                                                                                  <block type="text" id="FZGSKcT6/EoN~;A7QF(|">
                                                                                    <field name="TEXT">" , "iconColor" : </field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD11">
                                                                                  <block type="math_round" id="~dTf:AE=_`eUo`aqj-ln">
                                                                                    <field name="OP">ROUND</field>
                                                                                    <value name="NUM">
                                                                                      <shadow type="math_number" id="@[c8vVH;b7t=}}+gz4E7">
                                                                                        <field name="NUM">3.1</field>
                                                                                      </shadow>
                                                                                      <block type="variables_get" id="JT^tsJ#jCG2z9l$M76^2">
                                                                                        <field name="VAR" id="LlRz2eBS(B:~7Uz*A=$6">iconColors</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD12">
                                                                                  <block type="text" id="PJQ37w`cTLcQ8#]Mf4sI">
                                                                                    <field name="TEXT"> , "speed" : </field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD13">
                                                                                  <block type="math_round" id="CHT$~Z?+g3r4?mw^#|jQ">
                                                                                    <field name="OP">ROUND</field>
                                                                                    <value name="NUM">
                                                                                      <shadow type="math_number" id="^}w}ao7-8glg:_Q;W0uL">
                                                                                        <field name="NUM">3.1</field>
                                                                                      </shadow>
                                                                                      <block type="math_arithmetic" id="zSZ[P?*L5{2,WSyQz=]W">
                                                                                        <field name="OP">DIVIDE</field>
                                                                                        <value name="A">
                                                                                          <shadow type="math_number" id="jB,});;Upj=|m{PBsqBU">
                                                                                            <field name="NUM">1</field>
                                                                                          </shadow>
                                                                                          <block type="variables_get" id="(-)/_2g))Ez}d8]d.#[x">
                                                                                            <field name="VAR" id="uN(6R6f#q):2R%dR_YQ}">vSpeed</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="B">
                                                                                          <shadow type="math_number" id="y,Xwh4sdHznwt)B])VRV">
                                                                                            <field name="NUM">3</field>
                                                                                          </shadow>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD14">
                                                                                  <block type="text" id="~3z-WAg!xY,63A_^%czc">
                                                                                    <field name="TEXT">}</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                        <next>
                                                                          <block type="controls_if" id="d1GgE1,V]OqJ8,,u36P-">
                                                                            <value name="IF0">
                                                                              <block type="logic_compare" id="joK.(6Q]ERs#6c+p6S5,">
                                                                                <field name="OP">LT</field>
                                                                                <value name="A">
                                                                                  <block type="variables_get" id="R,?;%bi,uBw/c5Z=$]Ur">
                                                                                    <field name="VAR" id="E57P;3$~H@U7xnh3-3~T">j</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <block type="math_number" id="0.vK4sitmh,7K)Ey8Pe%">
                                                                                    <field name="NUM">6</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="DO0">
                                                                              <block type="variables_set" id="a8+`v3+0k?AoASfs;t%u">
                                                                                <field name="VAR" id="ka?!8/C5fALo,cmSVoD;">outJSON</field>
                                                                                <value name="VALUE">
                                                                                  <block type="text_join" id="L**at,dxmXO${6dXd-%T">
                                                                                    <mutation items="2"></mutation>
                                                                                    <value name="ADD0">
                                                                                      <block type="variables_get" id="u~NcAcCS:;l2g;t?MuPc">
                                                                                        <field name="VAR" id="ka?!8/C5fALo,cmSVoD;">outJSON</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="ADD1">
                                                                                      <block type="text" id="1`TO`1NiT=W_5Uj5P8r%">
                                                                                        <field name="TEXT">, </field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </statement>
                                                                          </block>
                                                                        </next>
                                                                      </block>
                                                                    </next>
                                                                  </block>
                                                                </next>
                                                              </block>
                                                            </next>
                                                          </block>
                                                        </next>
                                                      </block>
                                                    </statement>
                                                    <next>
                                                      <block type="variables_set" id="2^Jp:pF[|yJR;mN;sx-0">
                                                        <field name="VAR" id="ka?!8/C5fALo,cmSVoD;">outJSON</field>
                                                        <value name="VALUE">
                                                          <block type="text_join" id="jcPxQ![x-,w!=+l!apJi">
                                                            <mutation items="2"></mutation>
                                                            <value name="ADD0">
                                                              <block type="variables_get" id="2Umzu3qT;FY7vJri9A`D">
                                                                <field name="VAR" id="ka?!8/C5fALo,cmSVoD;">outJSON</field>
                                                              </block>
                                                            </value>
                                                            <value name="ADD1">
                                                              <block type="text" id="^9Gbx,aU`ifVfhY~}?Kx">
                                                                <field name="TEXT">]</field>
                                                              </block>
                                                            </value>
                                                          </block>
                                                        </value>
                                                        <next>
                                                          <block type="control" id="DvGZU,8kz0%D.8Mj41K9">
                                                            <mutation xmlns="http://www.w3.org/1999/xhtml" delay_input="false"></mutation>
                                                            <field name="OID">0_userdata.0.Test.CardPowerExample.cardPower_1_JSON</field>
                                                            <field name="WITH_DELAY">FALSE</field>
                                                            <value name="VALUE">
                                                              <block type="variables_get" id="WD,NlTpKl{Q~R3Wmi/IP">
                                                                <field name="VAR" id="ka?!8/C5fALo,cmSVoD;">outJSON</field>
                                                              </block>
                                                            </value>
                                                            <next>
                                                              <block type="controls_if" id="1z;X0ItbCP`CRZTs)2ZY">
                                                                <value name="IF0">
                                                                  <block type="variables_get" id="M:}[?BO`:FP;cVRwm*GO">
                                                                    <field name="VAR" id="N(P#!imDf$+p`U1atsq-">Debug</field>
                                                                  </block>
                                                                </value>
                                                                <statement name="DO0">
                                                                  <block type="debug" id="YSvYRzW%3f+JGK_re^$/">
                                                                    <field name="Severity">log</field>
                                                                    <value name="TEXT">
                                                                      <shadow type="text" id="r=2V8Z@E;#e8B8N^ci(I">
                                                                        <field name="TEXT">test</field>
                                                                      </shadow>
                                                                      <block type="variables_get" id="yZ0Tf$]o1CFa5atzfP0B">
                                                                        <field name="VAR" id="ka?!8/C5fALo,cmSVoD;">outJSON</field>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </statement>
                                                              </block>
                                                            </next>
                                                          </block>
                                                        </next>
                                                      </block>
                                                    </next>
                                                  </block>
                                                </next>
                                              </block>
                                            </next>
                                          </block>
                                        </next>
                                      </block>
                                    </next>
                                  </block>
                                </next>
                              </block>
                            </next>
                          </block>
                        </next>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </statement>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>

  ```
</details>  

**Kurze Anleitung:**  
Der Code dient nur der Orientierung und stellt keine Lösung für die eigene Visualisierung dar. Somit soll z.B. der Aufbau des JSON-Objektes verdeutlicht werden.

Für dieses Beispiel sind in 0_userdata für die 6 Werte in der cardPower entsprechende Datenpunkte (number) manuell angelegt worden:  
![image](https://user-images.githubusercontent.com/102996011/194373014-3dfc240c-ce7a-42ca-8d95-925b0a01b19f.png)  

Im oberen Teil des Blocklys wird lediglich eine Emulation auf 4 von 6 Datenpunkten je Minute erzeugt. Bei Produktivnutzung sollte dieses Codeobjekt gelöscht (deaktiviert) werden.

![image](https://user-images.githubusercontent.com/102996011/194373795-e3d5e889-10fd-48e6-8a51-cc56c9eadc35.png)

**Produktivnutzung:**  

Die Datenpunkte zu den entsprechenden Piktogrammen (id's) sollten mit den jeweiligen eigenen Adapter-Datenpunkten ersetzt werden. Im Beispiel werden folgende Datenpunkte zugewiesen:

1 - Batteriespeicher (Einspeisung/Bezug)  
2 - Photovoltaik Ertrag  
3 - Windenergieanlage Ertrag  
4 - Sämtliche aktiven Verbraucher des Hauses  
5 - Energielieferant (Netz-Einspeisung/Netz-Bezug)  
6 - Ladestation Verbrauch (E-Car)  
  
Für eine abweichende Darstellung ist das JSON entsprechend zu befüllen. Wenn eine Entität nicht visualisiert werden soll, so sollte in allen Werten zur id ein leerer String **""** übergeben werden. Beispiel:

```
  {
    "id": 3,
    "value": "",
    "unit": "",
    "direction": "",
    "icon": "",
    "iconColor": "",
    "speed": ""
  },
```

> Das Skript stellt nur eine exemplarische Möglichkeit der Befüllung dar. Es kann frei definiert und auf eigene Bedürfnisse angepasst werden, soll aber keine finale Lösung für jede Smart Home Situation abbilden!
> Ebenso kann die Erstellung des JSON natürlich auch über JavaScript oder TypeScript erfolgen.

# cardChart (ab TS-Script v.3.7.0)  

> ab Release v3.7.0

![image](https://user-images.githubusercontent.com/102996011/204631969-dfd8b8e9-09d0-45c2-a243-5e047f09ab05.png)  
   
> Für das unten abgebildete Blockly-Script wurden die Werte eines Datenpunktes "sonoff.0.DZG_DWSB20_2H.DZG_Leistung_Aktuell" in einer Influx 2.0 Datenbank gespeichert.  

Es wird für das Skript ein Datenpunkt (hier im Beispiel "0_userdata.0.Test.cardChart.txt") benötigt, um das Chart für die cardChart aufzubereiten.

**Alias-Erstellung:**  
Es wird lediglich ein Alias vom Gerätetyp "Info" benötigt:
![image](https://user-images.githubusercontent.com/102996011/209008594-36da27fb-cde2-4964-bcd8-3b406f4656cb.png)

**PageItem Beispiel:**
```
let CardChartExample: PageChart =
{
    "type": "cardChart",
    "heading": "Stromzähler L1+L2+L3",
    "useColor": true,
    "subPage": false,
    "parent": undefined,
    "items": [<PageItem>{ 
                id: 'alias.0.NSPanel_1.cardChart', 
                yAxis: 'Leistung [kW]', 
                yAxisTicks: [2,4,6,8,10,2,4,6,8,20,2], 
                onColor: Yellow
             }]
};
```  

![image](https://user-images.githubusercontent.com/102996011/209009144-1b82e7df-1a58-412a-a304-14a5cf987a4c.png)  

**Blockly für Influx 2.0**
![image](https://user-images.githubusercontent.com/102996011/209006326-c8036709-2235-4ef8-aa14-00798e09fce7.png)

<details>
  <summary>ioBroker Blockly Script</summary>

```
<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id=";7d1NODEunxn(R(kK*f=">sourceDP</variable>
    <variable id="YH0NB9:6eZ9eFq:C](Zk">targetDP</variable>
    <variable id="qmC4{i5;_ZCpInQr};^K">AxisXHours</variable>
    <variable id="+Zu]|)A/$l?Zp[x%5@^+">AxisXTicks</variable>
    <variable id="lGZ3XJ7}x8tLG|?0du(Q">Debug</variable>
    <variable id="fYyJ=y.Qe_5LkMTl8V]">flux</variable>
    <variable id="Ow]/GM_.lMrwSdIR[S*Z">AxisTickCounter</variable>
    <variable id="1Nf6J@P?M|2X?Po0#,F@">i</variable>
    <variable id="$|*Q:b}!fv28l6vg#z(Y">queryStunde</variable>
    <variable id="xnC#93sMF3Exd~jlOYt(">queryOutput</variable>
    <variable id="{(1Z0Pr};hMs+7G:j%j*">queryValue</variable>
    <variable id="?LaH161y!66.OJe+g+R*">AxisTicksBool</variable>
    <variable id="N,zaD%}Jd:vQKKFbFFom">result</variable>
  </variables>
  <block type="comment" id="wkWe{We!g7,qW.!~JkMK" x="-638" y="-312">
    <field name="COMMENT">Example String</field>
    <next>
      <block type="comment" id="0UP24=E28ipyLcEjQvF-">
        <field name="COMMENT">7^2:00~7~6^4:00~6~7^6:00~0~7^8:00~5~1^10:00~1~10^12:00~5~6^14:00~8</field>
        <next>
          <block type="comment" id="Jibhz,.R178)fWS=[$/4">
            <field name="COMMENT">Start Parameter</field>
            <next>
              <block type="variables_set" id="VN-e=u7{hEeqE{e^xdN;">
                <field name="VAR" id=";7d1NODEunxn(R(kK*f=">sourceDP</field>
                <value name="VALUE">
                  <block type="text" id="3l*sfN6[o{u/zaS./DjO">
                    <field name="TEXT">sonoff.0.DZG_DWSB20_2H.DZG_Leistung_Aktuell</field>
                  </block>
                </value>
                <next>
                  <block type="variables_set" id="k7=176;,*CD:8UDb/f2G">
                    <field name="VAR" id="YH0NB9:6eZ9eFq:C](Zk">targetDP</field>
                    <value name="VALUE">
                      <block type="text" id=".?Cc/K5}d0$lh~,p)jfm">
                        <field name="TEXT">0_userdata.0.Test.cardChart.txt</field>
                      </block>
                    </value>
                    <next>
                      <block type="variables_set" id="WPJ_@tOGD#-D-:Jumd7m">
                        <field name="VAR" id="qmC4{i5;_ZCpInQr};^K">AxisXHours</field>
                        <value name="VALUE">
                          <block type="math_number" id="}d6:akvZohJ1)i-d`2Go">
                            <field name="NUM">24</field>
                          </block>
                        </value>
                        <next>
                          <block type="variables_set" id="k]IpircrS|EKhTI={wlF">
                            <field name="VAR" id="+Zu]|)A/$l?Zp[x%5@^+">AxisXTicks</field>
                            <value name="VALUE">
                              <block type="math_number" id="f~y|4BVEQ)FNM4:]rI^J">
                                <field name="NUM">5</field>
                              </block>
                            </value>
                            <next>
                              <block type="variables_set" id="8v0y2i{_e=;y6*|avE7[">
                                <field name="VAR" id="lGZ3XJ7}x8tLG|?0du(Q">Debug</field>
                                <value name="VALUE">
                                  <block type="logic_boolean" id="^_?/X}Fm%e:D?iV]9:3E">
                                    <field name="BOOL">FALSE</field>
                                  </block>
                                </value>
                                <next>
                                  <block type="comment" id="Tqk|AM`Mu.GXY4UJ2xT|">
                                    <field name="COMMENT">Ende Parameter</field>
                                    <next>
                                      <block type="on_ext" id="ks8x]yI8Qf20+w:b!^52">
                                        <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
                                        <field name="CONDITION">ne</field>
                                        <field name="ACK_CONDITION"></field>
                                        <value name="OID0">
                                          <shadow type="field_oid" id="8A.JZN9y5y6[arj0Vj^l">
                                            <field name="oid">default</field>
                                          </shadow>
                                          <block type="variables_get" id="$I#;?pm;mn,:kIyvCiYz">
                                            <field name="VAR" id=";7d1NODEunxn(R(kK*f=">sourceDP</field>
                                          </block>
                                        </value>
                                        <statement name="STATEMENT">
                                          <block type="variables_set" id="U@DE;=Am$0u0zf=QocVY">
                                            <field name="VAR" id="fYyJ=y.Qe_5LkMTl8V]">flux</field>
                                            <value name="VALUE">
                                              <block type="text_join" id="^wVY,!j8|XAXxZ~u|I]?">
                                                <mutation items="8"></mutation>
                                                <value name="ADD0">
                                                  <block type="text" id="?Wz=]TXWJi1|K|eLCv).">
                                                    <field name="TEXT">from(bucket: "iobroker")</field>
                                                  </block>
                                                </value>
                                                <value name="ADD1">
                                                  <block type="text" id="[O){s@j%{{`U[gX;hGo;">
                                                    <field name="TEXT">|&gt; range(start: -24h, stop: now())</field>
                                                  </block>
                                                </value>
                                                <value name="ADD2">
                                                  <block type="text" id="4%9GPSSInNc.RRMZ2H#-">
                                                    <field name="TEXT">|&gt; filter(fn: (r) =&gt; r["_measurement"] == "</field>
                                                  </block>
                                                </value>
                                                <value name="ADD3">
                                                  <block type="variables_get" id="1$2YKrW$BR=m1R+c};@,">
                                                    <field name="VAR" id=";7d1NODEunxn(R(kK*f=">sourceDP</field>
                                                  </block>
                                                </value>
                                                <value name="ADD4">
                                                  <block type="text" id="Uv3)99m(M0kwiYEom+AH">
                                                    <field name="TEXT">")</field>
                                                  </block>
                                                </value>
                                                <value name="ADD5">
                                                  <block type="text" id="?|)Iu}YksZ%O)t-]ki32">
                                                    <field name="TEXT">|&gt; filter(fn: (r) =&gt; r["_field"] == "value")</field>
                                                  </block>
                                                </value>
                                                <value name="ADD6">
                                                  <block type="text" id="P];z*fmF{dsEVopJC]hc">
                                                    <field name="TEXT">|&gt; aggregateWindow(every: 1h, fn: mean, createEmpty: false)</field>
                                                  </block>
                                                </value>
                                                <value name="ADD7">
                                                  <block type="text" id="b,./zRV/Rmud0j!=G$9G">
                                                    <field name="TEXT">|&gt; yield(name: "mean")</field>
                                                  </block>
                                                </value>
                                              </block>
                                            </value>
                                            <next>
                                              <block type="sendto_custom" id="]Z_xq8=!F4a-E1,RBDD2">
                                                <mutation xmlns="http://www.w3.org/1999/xhtml" items="" with_statement="true"></mutation>
                                                <field name="INSTANCE">influxdb.1</field>
                                                <field name="COMMAND">query</field>
                                                <field name="LOG"></field>
                                                <field name="WITH_STATEMENT">TRUE</field>
                                                <value name="ARG0">
                                                  <shadow type="text" id="yv_a*bq^?@[:)e,1?#6">
                                                    <field name="TEXT"></field>
                                                  </shadow>
                                                  <block type="variables_get" id="JOt^(8s6}Ee!0+.V[[#">
                                                    <field name="VAR" id="fYyJ=y.Qe_5LkMTl8V]">flux</field>
                                                  </block>
                                                </value>
                                                <statement name="STATEMENT">
                                                  <block type="variables_set" id=",IBFSX,3Y-ZMl3fA4=}M">
                                                    <field name="VAR" id="Ow]/GM_.lMrwSdIR[S*Z">AxisTickCounter</field>
                                                    <value name="VALUE">
                                                      <block type="math_number" id="HWBy6dA.volh]^mxt5P9">
                                                        <field name="NUM">0</field>
                                                      </block>
                                                    </value>
                                                    <next>
                                                      <block type="controls_for" id="{$qw^{lXn8L6M7b*7Fr$">
                                                        <field name="VAR" id="1Nf6J@P?M|2X?Po0#,F@">i</field>
                                                        <value name="FROM">
                                                          <shadow type="math_number" id="md-KTdJ_(DIC??]Dg-`d">
                                                            <field name="NUM">1</field>
                                                          </shadow>
                                                          <block type="math_number" id="dMpL|%R;2N9mu6Ij^da`">
                                                            <field name="NUM">1</field>
                                                          </block>
                                                        </value>
                                                        <value name="TO">
                                                          <shadow type="math_number" id="|$C.`SsIiT*vwn`Z05VD">
                                                            <field name="NUM">24</field>
                                                          </shadow>
                                                          <block type="variables_get" id="NYP8S3(??dGUL/G2-OU]">
                                                            <field name="VAR" id="qmC4{i5;_ZCpInQr};^K">AxisXHours</field>
                                                          </block>
                                                        </value>
                                                        <value name="BY">
                                                          <shadow type="math_number" id="qn4Hre5oCJ)uf}:Frf]u">
                                                            <field name="NUM">1</field>
                                                          </shadow>
                                                        </value>
                                                        <statement name="DO">
                                                          <block type="math_change" id="NQ~5@b3X|mdi$a)i$=}z">
                                                            <field name="VAR" id="Ow]/GM_.lMrwSdIR[S*Z">AxisTickCounter</field>
                                                            <value name="DELTA">
                                                              <shadow type="math_number" id="_}MNUh_Mq_gFC1zUFo]+">
                                                                <field name="NUM">1</field>
                                                              </shadow>
                                                              <block type="math_number" id="k52lIOyN0Z`qv)Xg%|dQ">
                                                                <field name="NUM">1</field>
                                                              </block>
                                                            </value>
                                                            <next>
                                                              <block type="variables_set" id="A@H]-Ve}k7U2u7=D?[n#">
                                                                <field name="VAR" id="$|*Q:b}!fv28l6vg#z(Y">queryStunde</field>
                                                                <value name="VALUE">
                                                                  <block type="convert_from_date" id="H+}#b$rG()d)P.*@|7h?">
                                                                    <mutation xmlns="http://www.w3.org/1999/xhtml" format="false" language="false"></mutation>
                                                                    <field name="OPTION">h</field>
                                                                    <value name="VALUE">
                                                                      <block type="get_attr" id="I#)[#q^O10d*_g+o}cf2">
                                                                        <value name="PATH">
                                                                          <shadow type="text">
                                                                            <field name="TEXT">result.0.0._value</field>
                                                                          </shadow>
                                                                          <block type="text_join" id="Qw$6nILPYcHFVSEZr/w:">
                                                                            <mutation items="3"></mutation>
                                                                            <value name="ADD0">
                                                                              <block type="text" id="o6m^u,!iX#sh.Qc75zPQ">
                                                                                <field name="TEXT">result.0.</field>
                                                                              </block>
                                                                            </value>
                                                                            <value name="ADD1">
                                                                              <block type="variables_get" id="^RM~n?nXM:/OJt[/NY$9">
                                                                                <field name="VAR" id="1Nf6J@P?M|2X?Po0#,F@">i</field>
                                                                              </block>
                                                                            </value>
                                                                            <value name="ADD2">
                                                                              <block type="text" id="hB~m0VIdsK,]vV7+oCcA">
                                                                                <field name="TEXT">._time</field>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                        <value name="OBJECT">
                                                                          <block type="convert_object2json" id="DU6l$m)RB%|l~y9RnA5U">
                                                                            <field name="PRETTIFY">TRUE</field>
                                                                            <value name="VALUE">
                                                                              <block type="variables_get" id="/v9}|bsSI%A,NE%uAbR#">
                                                                                <field name="VAR" id="N,zaD%}Jd:vQKKFbFFom">result</field>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </value>
                                                                <next>
                                                                  <block type="variables_set" id="`z!}x2oI3Mf2y+A[Dr_=">
                                                                    <field name="VAR" id="{(1Z0Pr};hMs+7G:j%j*">queryValue</field>
                                                                    <value name="VALUE">
                                                                      <block type="math_round" id="C[%LfaasYPH=xa064S!3">
                                                                        <field name="OP">ROUND</field>
                                                                        <value name="NUM">
                                                                          <shadow type="math_number" id="W,7BwFhH68eCan-4iv_J">
                                                                            <field name="NUM">3.1</field>
                                                                          </shadow>
                                                                          <block type="math_arithmetic" id="rRK|686XgVGyM(FDKMI7">
                                                                            <field name="OP">DIVIDE</field>
                                                                            <value name="A">
                                                                              <shadow type="math_number" id="W$$H@Kl;8,2X[Q:D():U">
                                                                                <field name="NUM">1</field>
                                                                              </shadow>
                                                                              <block type="convert_tonumber" id="dk@3yGhr1G^5^LS(;V">
                                                                                <value name="VALUE">
                                                                                  <block type="get_attr" id=",G;cxxz[Lf]xXm)^p:X+">
                                                                                    <value name="PATH">
                                                                                      <shadow type="text" id="o+=S7dn|/OY#6Wcc9pdM">
                                                                                        <field name="TEXT">result.0.0._value</field>
                                                                                      </shadow>
                                                                                      <block type="text_join" id="q2ryv}1jI?!G`;h0=p(d">
                                                                                        <mutation items="3"></mutation>
                                                                                        <value name="ADD0">
                                                                                          <block type="text" id="i=WVO)n/G}+TVe!Rw:$P">
                                                                                            <field name="TEXT">result.0.</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD1">
                                                                                          <block type="variables_get" id="528p7%T)$J64Y}XO,[zV">
                                                                                            <field name="VAR" id="1Nf6J@P?M|2X?Po0#,F@">i</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD2">
                                                                                          <block type="text" id="|1)N]).,yaTGOktgZFmy">
                                                                                            <field name="TEXT">._value</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="OBJECT">
                                                                                      <block type="convert_object2json" id="|Ta;,0qe?ZtKwOO)dD,$">
                                                                                        <field name="PRETTIFY">TRUE</field>
                                                                                        <value name="VALUE">
                                                                                          <block type="variables_get" id="ch!DPazljsLz1:R(edb]">
                                                                                            <field name="VAR" id="N,zaD%}Jd:vQKKFbFFom">result</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <value name="B">
                                                                              <shadow type="math_number" id="q7c[8MB5sjlM!9o7WV-h">
                                                                                <field name="NUM">100</field>
                                                                              </shadow>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                      </block>
                                                                    </value>
                                                                    <next>
                                                                      <block type="controls_if" id="(,IE/`t3aVgV{H+#]PA7">
                                                                        <mutation elseif="1" else="1"></mutation>
                                                                        <value name="IF0">
                                                                          <block type="logic_compare" id="tV;dZ/IHWT5E4x}%87JT">
                                                                            <field name="OP">EQ</field>
                                                                            <value name="A">
                                                                              <block type="variables_get" id="x`ZE}QKrxtHpi83BC*%*">
                                                                                <field name="VAR" id="1Nf6J@P?M|2X?Po0#,F@">i</field>
                                                                              </block>
                                                                            </value>
                                                                            <value name="B">
                                                                              <block type="math_number" id="eo!y;fdOxOZ%./Pg+DK:">
                                                                                <field name="NUM">1</field>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                        <statement name="DO0">
                                                                          <block type="variables_set" id="a8)vt2i8.9MAj7?=Zmxv">
                                                                            <field name="VAR" id="?LaH161y!66.OJe+g+R*">AxisTicksBool</field>
                                                                            <value name="VALUE">
                                                                              <block type="logic_boolean" id="R{I5#aCW}jqjakagHkW8">
                                                                                <field name="BOOL">TRUE</field>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </statement>
                                                                        <value name="IF1">
                                                                          <block type="logic_compare" id="eM^tI;vd|sr{R1`ccxiH">
                                                                            <field name="OP">EQ</field>
                                                                            <value name="A">
                                                                              <block type="variables_get" id="XVgFr@cabe%dK0J-=.k$">
                                                                                <field name="VAR" id="Ow]/GM_.lMrwSdIR[S*Z">AxisTickCounter</field>
                                                                              </block>
                                                                            </value>
                                                                            <value name="B">
                                                                              <block type="variables_get" id="DL^G^o~1`4N7P0B{|-^7">
                                                                                <field name="VAR" id="+Zu]|)A/$l?Zp[x%5@^+">AxisXTicks</field>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </value>
                                                                        <statement name="DO1">
                                                                          <block type="variables_set" id="inpPrsBe%J3q(asZK!f~">
                                                                            <field name="VAR" id="?LaH161y!66.OJe+g+R*">AxisTicksBool</field>
                                                                            <value name="VALUE">
                                                                              <block type="logic_boolean" id="X}J/g+-elB;iIiNN6kTd">
                                                                                <field name="BOOL">TRUE</field>
                                                                              </block>
                                                                            </value>
                                                                            <next>
                                                                              <block type="variables_set" id="?OTYd?4N2yU!]I|AJnkG">
                                                                                <field name="VAR" id="Ow]/GM_.lMrwSdIR[S*Z">AxisTickCounter</field>
                                                                                <value name="VALUE">
                                                                                  <block type="math_number" id="Q7pZkxcD?T=Rs%7e=o|#">
                                                                                    <field name="NUM">1</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </next>
                                                                          </block>
                                                                        </statement>
                                                                        <statement name="ELSE">
                                                                          <block type="variables_set" id="O!Z{qF79n$B@5asE|.Fq">
                                                                            <field name="VAR" id="?LaH161y!66.OJe+g+R*">AxisTicksBool</field>
                                                                            <value name="VALUE">
                                                                              <block type="logic_boolean" id="+va#+zpdik~K(^~H%dDl">
                                                                                <field name="BOOL">FALSE</field>
                                                                              </block>
                                                                            </value>
                                                                          </block>
                                                                        </statement>
                                                                        <next>
                                                                          <block type="controls_if" id="(#Ac`oPyRV--tDrLjb[D">
                                                                            <mutation else="1"></mutation>
                                                                            <value name="IF0">
                                                                              <block type="logic_compare" id="4XqOzFnbdGbH$?sP=n?C">
                                                                                <field name="OP">EQ</field>
                                                                                <value name="A">
                                                                                  <block type="variables_get" id="YWWM)!uH}MR9O8j@S~vp">
                                                                                    <field name="VAR" id="1Nf6J@P?M|2X?Po0#,F@">i</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="B">
                                                                                  <block type="variables_get" id="Y8@$l}$@Z2gMN`!ff;YS">
                                                                                    <field name="VAR" id="qmC4{i5;_ZCpInQr};^K">AxisXHours</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <statement name="DO0">
                                                                              <block type="controls_if" id="8BlMu(La/dEdOiI336]$">
                                                                                <mutation else="1"></mutation>
                                                                                <value name="IF0">
                                                                                  <block type="variables_get" id="Hu5YR|`#%|V~NU99xfz5">
                                                                                    <field name="VAR" id="?LaH161y!66.OJe+g+R*">AxisTicksBool</field>
                                                                                  </block>
                                                                                </value>
                                                                                <statement name="DO0">
                                                                                  <block type="variables_set" id="dh65}MMXtDunBL6mAk@s">
                                                                                    <field name="VAR" id="xnC#93sMF3Exd~jlOYt(">queryOutput</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="text_join" id="8fo[$zsvjpz#~_c|XgQ8">
                                                                                        <mutation items="5"></mutation>
                                                                                        <value name="ADD0">
                                                                                          <block type="variables_get" id="sK5_][sn:J|i*obw-V$U">
                                                                                            <field name="VAR" id="xnC#93sMF3Exd~jlOYt(">queryOutput</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD1">
                                                                                          <block type="variables_get" id="W8Qx.b[qRX/(VqtX}J7.">
                                                                                            <field name="VAR" id="{(1Z0Pr};hMs+7G:j%j*">queryValue</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD2">
                                                                                          <block type="text" id="$D(B*v*BGW}k#Rh89pqD">
                                                                                            <field name="TEXT">^</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD3">
                                                                                          <block type="variables_get" id="fKP`g4vz-f~=M|em+DP$">
                                                                                            <field name="VAR" id="$|*Q:b}!fv28l6vg#z(Y">queryStunde</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD4">
                                                                                          <block type="text" id="1@uaN?vTyjWWniIuiuC+">
                                                                                            <field name="TEXT">:00</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </statement>
                                                                                <statement name="ELSE">
                                                                                  <block type="variables_set" id="BXEq*ZK7sqd?ci@GO(?}">
                                                                                    <field name="VAR" id="xnC#93sMF3Exd~jlOYt(">queryOutput</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="text_join" id="$4p;!(0dDim]=2A%E)n1">
                                                                                        <mutation items="2"></mutation>
                                                                                        <value name="ADD0">
                                                                                          <block type="variables_get" id="8.,C*.;i!u~(H#?D9lt]">
                                                                                            <field name="VAR" id="xnC#93sMF3Exd~jlOYt(">queryOutput</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD1">
                                                                                          <block type="variables_get" id="~pRL+,zS1m7w?#J3fc1y">
                                                                                            <field name="VAR" id="{(1Z0Pr};hMs+7G:j%j*">queryValue</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </statement>
                                                                              </block>
                                                                            </statement>
                                                                            <statement name="ELSE">
                                                                              <block type="controls_if" id="~2S9VH/AHE:,A%!w]+:t">
                                                                                <mutation else="1"></mutation>
                                                                                <value name="IF0">
                                                                                  <block type="variables_get" id="[4BIh{$U[:+%N[~[rc%-">
                                                                                    <field name="VAR" id="?LaH161y!66.OJe+g+R*">AxisTicksBool</field>
                                                                                  </block>
                                                                                </value>
                                                                                <statement name="DO0">
                                                                                  <block type="variables_set" id="`}E=fYR/VXYqe4.TJ|@o">
                                                                                    <field name="VAR" id="xnC#93sMF3Exd~jlOYt(">queryOutput</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="text_join" id="}E?T?bGDhyVDfK4U/i;K">
                                                                                        <mutation items="6"></mutation>
                                                                                        <value name="ADD0">
                                                                                          <block type="variables_get" id="H4jv7eyLo_;bsR.$$!yh">
                                                                                            <field name="VAR" id="xnC#93sMF3Exd~jlOYt(">queryOutput</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD1">
                                                                                          <block type="variables_get" id="XL|RbFT(}u#U7x@DcvKO">
                                                                                            <field name="VAR" id="{(1Z0Pr};hMs+7G:j%j*">queryValue</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD2">
                                                                                          <block type="text" id="`?r.5%PR+1m7T}S-sZhT">
                                                                                            <field name="TEXT">^</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD3">
                                                                                          <block type="variables_get" id="|)./@c@-#U;a89o;,eV}">
                                                                                            <field name="VAR" id="$|*Q:b}!fv28l6vg#z(Y">queryStunde</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD4">
                                                                                          <block type="text" id="XB5y5jf[}Wk-t%v7~oAo">
                                                                                            <field name="TEXT">:00</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD5">
                                                                                          <block type="text" id="Sgn7o[am{*(oK`Wu*jCd">
                                                                                            <field name="TEXT">~</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </statement>
                                                                                <statement name="ELSE">
                                                                                  <block type="variables_set" id="i4B33cC-m]8*ka2b~2Hv">
                                                                                    <field name="VAR" id="xnC#93sMF3Exd~jlOYt(">queryOutput</field>
                                                                                    <value name="VALUE">
                                                                                      <block type="text_join" id="x+XvH;%F|(0:q?_bAPgr">
                                                                                        <mutation items="3"></mutation>
                                                                                        <value name="ADD0">
                                                                                          <block type="variables_get" id="|k-p/4ma?V|Trj-O{cc_">
                                                                                            <field name="VAR" id="xnC#93sMF3Exd~jlOYt(">queryOutput</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD1">
                                                                                          <block type="variables_get" id="Phk4rUj9CI;T$PJ)3T/J">
                                                                                            <field name="VAR" id="{(1Z0Pr};hMs+7G:j%j*">queryValue</field>
                                                                                          </block>
                                                                                        </value>
                                                                                        <value name="ADD2">
                                                                                          <block type="text" id="90]Z5Tj3Jc1QXVxw=#lM">
                                                                                            <field name="TEXT">~</field>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </statement>
                                                                              </block>
                                                                            </statement>
                                                                            <next>
                                                                              <block type="controls_if" id="_QT3e7=mT#u6tzKV7LH{">
                                                                                <value name="IF0">
                                                                                  <block type="logic_compare" id="^j3H?q-luM9w0@G@bKdj">
                                                                                    <field name="OP">EQ</field>
                                                                                    <value name="A">
                                                                                      <block type="variables_get" id="/5#TfTmAT|/Nel+hgd37">
                                                                                        <field name="VAR" id="1Nf6J@P?M|2X?Po0#,F@">i</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <value name="B">
                                                                                      <block type="variables_get" id="kep:qt_.8LtUMyR=lay!">
                                                                                        <field name="VAR" id="qmC4{i5;_ZCpInQr};^K">AxisXHours</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </value>
                                                                                <statement name="DO0">
                                                                                  <block type="math_change" id="!HkN^c`=Ne9[PI:EW6cd">
                                                                                    <field name="VAR" id="$|*Q:b}!fv28l6vg#z(Y">queryStunde</field>
                                                                                    <value name="DELTA">
                                                                                      <shadow type="math_number" id="u5KL]z#%Vdhkpw03)}g2">
                                                                                        <field name="NUM">1</field>
                                                                                      </shadow>
                                                                                      <block type="math_number" id="_o,gHQNIv7dBzA=?Kw1|">
                                                                                        <field name="NUM">1</field>
                                                                                      </block>
                                                                                    </value>
                                                                                  </block>
                                                                                </statement>
                                                                                <next>
                                                                                  <block type="controls_if" id="8x;2cN=A3c{3akok$qPJ">
                                                                                    <value name="IF0">
                                                                                      <block type="variables_get" id="h.?LWY-xQQmWuA,J,o6c">
                                                                                        <field name="VAR" id="lGZ3XJ7}x8tLG|?0du(Q">Debug</field>
                                                                                      </block>
                                                                                    </value>
                                                                                    <statement name="DO0">
                                                                                      <block type="debug" id="!nBe#a61R!L;$Gg0yE=r">
                                                                                        <field name="Severity">log</field>
                                                                                        <value name="TEXT">
                                                                                          <shadow type="text" id="#`;@4{,7HhXAI_z0XD`_">
                                                                                            <field name="TEXT">test</field>
                                                                                          </shadow>
                                                                                          <block type="text_join" id="$)h?C/}A3d+2{;ircsVo">
                                                                                            <mutation items="5"></mutation>
                                                                                            <value name="ADD0">
                                                                                              <block type="variables_get" id="drC=n%z%cg]L/ChAQ,r(">
                                                                                                <field name="VAR" id="1Nf6J@P?M|2X?Po0#,F@">i</field>
                                                                                              </block>
                                                                                            </value>
                                                                                            <value name="ADD1">
                                                                                              <block type="text" id="T?RPZ1KdAVs@4~L?bjIQ">
                                                                                                <field name="TEXT"> - </field>
                                                                                              </block>
                                                                                            </value>
                                                                                            <value name="ADD2">
                                                                                              <block type="variables_get" id="qD/6epYv15t)29;5u^rM">
                                                                                                <field name="VAR" id="{(1Z0Pr};hMs+7G:j%j*">queryValue</field>
                                                                                              </block>
                                                                                            </value>
                                                                                            <value name="ADD3">
                                                                                              <block type="text" id=",~ZFy.irPx-D=f3=5j_*">
                                                                                                <field name="TEXT"> - </field>
                                                                                              </block>
                                                                                            </value>
                                                                                            <value name="ADD4">
                                                                                              <block type="variables_get" id="?})ZpV:e09-$Bm}zP:6M">
                                                                                                <field name="VAR" id="$|*Q:b}!fv28l6vg#z(Y">queryStunde</field>
                                                                                              </block>
                                                                                            </value>
                                                                                          </block>
                                                                                        </value>
                                                                                      </block>
                                                                                    </statement>
                                                                                  </block>
                                                                                </next>
                                                                              </block>
                                                                            </next>
                                                                          </block>
                                                                        </next>
                                                                      </block>
                                                                    </next>
                                                                  </block>
                                                                </next>
                                                              </block>
                                                            </next>
                                                          </block>
                                                        </statement>
                                                        <next>
                                                          <block type="control_ex" id="Lw=6*IJt^6=y^4UUAoaE">
                                                            <field name="TYPE">false</field>
                                                            <field name="CLEAR_RUNNING">FALSE</field>
                                                            <value name="OID">
                                                              <shadow type="field_oid" id="LF,wvJc^B098JB?jm!L+">
                                                                <field name="oid">Object ID</field>
                                                              </shadow>
                                                              <block type="variables_get" id="*_[s=|h$;uJ(/5K9pUEA">
                                                                <field name="VAR" id="YH0NB9:6eZ9eFq:C](Zk">targetDP</field>
                                                              </block>
                                                            </value>
                                                            <value name="VALUE">
                                                              <shadow type="logic_boolean" id="%*VY@2+N{ljW|1O8#Q.x">
                                                                <field name="BOOL">TRUE</field>
                                                              </shadow>
                                                              <block type="variables_get" id="QTf-s_v1[9Fd9yY!EV.l">
                                                                <field name="VAR" id="xnC#93sMF3Exd~jlOYt(">queryOutput</field>
                                                              </block>
                                                            </value>
                                                            <value name="DELAY_MS">
                                                              <shadow type="math_number" id="p]iW*DltJ@dQ/f_Z^^WN">
                                                                <field name="NUM">0</field>
                                                              </shadow>
                                                            </value>
                                                            <next>
                                                              <block type="controls_if" id="$/AV!7DH%;l*W6CAHyt]">
                                                                <value name="IF0">
                                                                  <block type="variables_get" id="ltYP1+G)`6X*g9~_(h-$">
                                                                    <field name="VAR" id="lGZ3XJ7}x8tLG|?0du(Q">Debug</field>
                                                                  </block>
                                                                </value>
                                                                <statement name="DO0">
                                                                  <block type="debug" id="Da6e+gbB[5Lh`KNrCWi6">
                                                                    <field name="Severity">log</field>
                                                                    <value name="TEXT">
                                                                      <shadow type="text" id="i3{gh~sI+^Tdgf0=ENeN">
                                                                        <field name="TEXT">test</field>
                                                                      </shadow>
                                                                      <block type="variables_get" id="aLUEHsE;Z|-=%7Ydbb2m">
                                                                        <field name="VAR" id="xnC#93sMF3Exd~jlOYt(">queryOutput</field>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </statement>
                                                                <next>
                                                                  <block type="variables_set" id="a;uA(wofssCu[/d{_/:c">
                                                                    <field name="VAR" id="xnC#93sMF3Exd~jlOYt(">queryOutput</field>
                                                                    <value name="VALUE">
                                                                      <block type="text" id="0WALNak)hre,22(Am@ny">
                                                                        <field name="TEXT"></field>
                                                                      </block>
                                                                    </value>
                                                                  </block>
                                                                </next>
                                                              </block>
                                                            </next>
                                                          </block>
                                                        </next>
                                                      </block>
                                                    </next>
                                                  </block>
                                                </statement>
                                              </block>
                                            </next>
                                          </block>
                                        </statement>
                                      </block>
                                    </next>
                                  </block>
                                </next>
                              </block>
                            </next>
                          </block>
                        </next>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>
```
</details>


  

# popUpNotify  

Status: in Erstellung:
 
Das ganze LUI Thema ist am Wachsen. Nun gibt es von der popUpNotify Page schon zwei verschiedene Varianten.
Diese wollen wir hier beschreiben:

## popUpNotify - alte Variante

**Beschreibung**:  
Die alte Variante kennt man am ehesten von Info-Popus zur Tasmota oder TFT Version.  
  
![image](https://user-images.githubusercontent.com/102996011/189373507-41a10711-afc0-4186-b94b-690bc1805a7f.png)
  
**Datenpunkte**:  
* popupNotifyHeading
* popupNotifyText
* popupNotifyInternalName
* popupNotifyButton1Text
* popupNotifyButton2Text
* popupNotifySleepTimeout
* popupNotifyAction
  
**Zuordnung Datenpunkte**:  
  
![popupnotify_v1](https://user-images.githubusercontent.com/99131208/200187862-a31a3223-0a1b-4d53-82e8-a93467dd19ce.jpg)
  
**Nutzung**:  
Vor der Version **v3.5.0** per Default nutzbar. Ab der Version **v3.5.0** bleibt die alte Version erstmal per Default nutzbar. Stellt man den Datenpunkt **popupNotifyLayout** auf 2 erhält man das neue popUpNotify, zur Nutzung des alten muss man dann den Wert 1 hinterlegen.  
  
**Beispiel**:  
  
Bei der [Anleitung der AlarmCard](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#2-alarm-page) gibt es zwei verschiedene Beispiele für die Nutzung der popUpNotify Page.  
  
  
## popUpNotify - Layout 2
  
**Beschreibung**:  
Ab Version **v3.5.0** verfügbar.  
Layout 2 bringt neue Funktionen mit sich wie Schriftgröße, Schriftfarbe, ein Icon mit definierbarer Farbe, etc.

![image](https://user-images.githubusercontent.com/99131208/200184667-88d4104c-5e6c-453b-8eb5-3f27183ef85a.png)  
    
**Neue Datenpunkte**:  
Die neuen Datenpunkte werden automatisch beim Starten des Skriptes angelegt. Zur Übersicht hier die neuen Datenpunkte aufgelistet:  
  
* popupNotifyHeadingColor
* popupNotifyTextColor
* popupNotifyButton1TextColor
* popupNotifyButton2TextColor
* popupNotifyLayout
* popupNotifyFontIdText (Schriftgröße)
* popupNotifyIcon
* popupNotifyIconColor
  
**Zuordnung Datenpunkte**:   
  
![popupnotify_v2](https://user-images.githubusercontent.com/99131208/200187887-1fbffa97-9d77-4681-bb58-384e2209c365.jpg)
  
  
**Nutzung**:  
Ab der Version **v3.5.0** bleibt die alte Version erstmal per Default nutzbar.  Stellt man den Datenpunkt **popupNotifyLayout** auf 2 erhält man das neue popUpNotify, zur Nutzung des alten muss man dann den Wert 1 hinterlegen.  
  
**Emulator (Layout 2)**:    

<details>
  <summary>ioBroker Blockly Script</summary>

  ```
<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="7Q3%H,r3WG((Q;]w,bbK">0_userdata_Path</variable>
    <variable id="UIsM8Eact}h@ZW5?xVbR">Sensor_Temperatur</variable>
    <variable id="~WSzaicRZ8#urLe2[R=k">Sensor_Lutfeuchte</variable>
    <variable id="caeHuwwu}!^U=Jns}u%t">Sensor_Luftdruck</variable>
    <variable id="+s+k$`6x!Mb[t~Ts^Zrp">Button1Text</variable>
    <variable id="iP=Bs[zV55PS82(Q$`|7">Button2Text</variable>
    <variable id="RLIY*e=6(.:_k@OJSC?Y">HeadingTextColor</variable>
    <variable id="K~gzNq|K||t-`B*`Kcr`">TextColor</variable>
    <variable id="G~p{^+hG44{B?m4L(cyH">Button1TextColor</variable>
    <variable id="QZ7wov(RrAOyZv@8lF3I">Button2TextColor</variable>
    <variable id="Db)I2;9^!VMzALbYVYNO">IconColor</variable>
    <variable id="#?MpfqBMCW|l*?q]RI[X">i</variable>
    <variable id="6sx!Ebx43k2^RFs;w0^K">HeadingText</variable>
    <variable id=")S5LKNN/K5V9|_8OXyGn">Icon</variable>
    <variable id="n%`;Bp1UH/yVByUHY*9b">FontSize</variable>
    <variable id="e%^+o,6sf9B/FYnuhoqQ">Text</variable>
  </variables>
  <block type="variables_set" id="G^=Qx9%S9Rc7#7G|=LdU" x="63" y="-87">
    <field name="VAR" id="7Q3%H,r3WG((Q;]w,bbK">0_userdata_Path</field>
    <value name="VALUE">
      <block type="text" id=";F]Cj%Y8B#%Y}*oX%rj8">
        <field name="TEXT">0_userdata.0.NSPanel.1.popupNotify.</field>
      </block>
    </value>
    <next>
      <block type="variables_set" id="LYci`3V?n:Q#XhI.5e59">
        <field name="VAR" id="UIsM8Eact}h@ZW5?xVbR">Sensor_Temperatur</field>
        <value name="VALUE">
          <block type="get_value" id="4Ijc:Qssy9cfYZVr;)0.">
            <field name="ATTR">val</field>
            <field name="OID">deconz.0.Sensors.65.temperature</field>
          </block>
        </value>
        <next>
          <block type="variables_set" id="Bt`wC{P74q3?|E+Vh%m1">
            <field name="VAR" id="~WSzaicRZ8#urLe2[R=k">Sensor_Lutfeuchte</field>
            <value name="VALUE">
              <block type="get_value" id="1Jtt.?XFKfkSR2E0`B29">
                <field name="ATTR">val</field>
                <field name="OID">deconz.0.Sensors.64.humidity</field>
              </block>
            </value>
            <next>
              <block type="variables_set" id="2{jbPU@a|To?U4W0Kh7Y">
                <field name="VAR" id="caeHuwwu}!^U=Jns}u%t">Sensor_Luftdruck</field>
                <value name="VALUE">
                  <block type="get_value" id="2;Aq(8-i$|{N0^QN(=W)">
                    <field name="ATTR">val</field>
                    <field name="OID">deconz.0.Sensors.66.pressure</field>
                  </block>
                </value>
                <next>
                  <block type="variables_set" id="{Lb:e?Hk0ZLIHgUQS0Qh">
                    <field name="VAR" id="+s+k$`6x!Mb[t~Ts^Zrp">Button1Text</field>
                    <value name="VALUE">
                      <block type="text" id="6-c,SdgQfdpE*oCAH~Pi">
                        <field name="TEXT"></field>
                      </block>
                    </value>
                    <next>
                      <block type="variables_set" id="v%1=S8_YX1_6HCM}h5y~">
                        <field name="VAR" id="iP=Bs[zV55PS82(Q$`|7">Button2Text</field>
                        <value name="VALUE">
                          <block type="text" id="EN5c[^;WQN%2qxxwI]JA">
                            <field name="TEXT">OK</field>
                          </block>
                        </value>
                        <next>
                          <block type="comment" id="35(LvkLl0Jnnh_RAMRXd">
                            <field name="COMMENT">Color Picker für RGB565</field>
                            <next>
                              <block type="comment" id="lJiiRl$j]^YDgx45TGPE">
                                <field name="COMMENT">http://www.barth-dev.de/online/rgb565-color-picker/</field>
                                <next>
                                  <block type="variables_set" id="QYSdj*q`P/1qY@o.,Y*c">
                                    <field name="VAR" id="RLIY*e=6(.:_k@OJSC?Y">HeadingTextColor</field>
                                    <value name="VALUE">
                                      <block type="text" id="`G$CYT?54r,Jz8I|6OJ]">
                                        <field name="TEXT">65535</field>
                                      </block>
                                    </value>
                                    <next>
                                      <block type="variables_set" id="/6-PAaad6dF)|FJp0fr{">
                                        <field name="VAR" id="K~gzNq|K||t-`B*`Kcr`">TextColor</field>
                                        <value name="VALUE">
                                          <block type="text" id="-PM7_=ur??KJOqX^9^?{">
                                            <field name="TEXT">65535</field>
                                          </block>
                                        </value>
                                        <next>
                                          <block type="variables_set" id="PzSv:8)o0G*q_C3EKk9A">
                                            <field name="VAR" id="G~p{^+hG44{B?m4L(cyH">Button1TextColor</field>
                                            <value name="VALUE">
                                              <block type="text" id="4)Tu5`-6dM`O5q5-[![6">
                                                <field name="TEXT">2016</field>
                                              </block>
                                            </value>
                                            <next>
                                              <block type="variables_set" id="(_?5tyOL{jA@@:(jGn.Z">
                                                <field name="VAR" id="QZ7wov(RrAOyZv@8lF3I">Button2TextColor</field>
                                                <value name="VALUE">
                                                  <block type="text" id="$IMWrRZ=n/}+S.iv~5#`">
                                                    <field name="TEXT">63488</field>
                                                  </block>
                                                </value>
                                                <next>
                                                  <block type="variables_set" id="u?h3*S@Lj|P-TA*XR?$`">
                                                    <field name="VAR" id="Db)I2;9^!VMzALbYVYNO">IconColor</field>
                                                    <value name="VALUE">
                                                      <block type="text" id="BItuXFzt@:Zwi;/BS)!p">
                                                        <field name="TEXT">2000</field>
                                                      </block>
                                                    </value>
                                                    <next>
                                                      <block type="comment" id="yAIk,I@:X#4vWvs2^Z5u">
                                                        <field name="COMMENT">Zähler für Loop</field>
                                                        <next>
                                                          <block type="variables_set" id="t96AiB0(*g^eeiww)ui{">
                                                            <field name="VAR" id="#?MpfqBMCW|l*?q]RI[X">i</field>
                                                            <value name="VALUE">
                                                              <block type="math_number" id="li[k8_)s6ZF*/K?{v3GN">
                                                                <field name="NUM">1</field>
                                                              </block>
                                                            </value>
                                                            <next>
                                                              <block type="comment" id="T0h2*mk,r8}E%%H;a03{">
                                                                <field name="COMMENT">Überschrift</field>
                                                                <next>
                                                                  <block type="variables_set" id="m$!KKv4b:6FR2;NNzm*=">
                                                                    <field name="VAR" id="6sx!Ebx43k2^RFs;w0^K">HeadingText</field>
                                                                    <value name="VALUE">
                                                                      <block type="lists_create_with" id="yk2|MrLr{x.xt!CqgB9j">
                                                                        <mutation items="4"></mutation>
                                                                        <value name="ADD0">
                                                                          <block type="text" id="qJAN7r)iM[A$,+G@WYXR">
                                                                            <field name="TEXT">Zeit</field>
                                                                          </block>
                                                                        </value>
                                                                        <value name="ADD1">
                                                                          <block type="text" id="(RK{##(fYn_L]u:BvnYw">
                                                                            <field name="TEXT">Temperatur</field>
                                                                          </block>
                                                                        </value>
                                                                        <value name="ADD2">
                                                                          <block type="text" id="--7Salv^WN%?/9`8:~R:">
                                                                            <field name="TEXT">Luftfeuchte</field>
                                                                          </block>
                                                                        </value>
                                                                        <value name="ADD3">
                                                                          <block type="text" id="-1fw|22@Uq@zv-iozeIe">
                                                                            <field name="TEXT">Luftdruck</field>
                                                                          </block>
                                                                        </value>
                                                                      </block>
                                                                    </value>
                                                                    <next>
                                                                      <block type="comment" id=")+`r*B#Fg|@X*k_!F6D@">
                                                                        <field name="COMMENT">Icons</field>
                                                                        <next>
                                                                          <block type="variables_set" id=":1y)d^LO{nG9OjG)Be6y">
                                                                            <field name="VAR" id=")S5LKNN/K5V9|_8OXyGn">Icon</field>
                                                                            <value name="VALUE">
                                                                              <block type="lists_create_with" id="Xt3m,u[dT5AVvg!Eg1H`">
                                                                                <mutation items="4"></mutation>
                                                                                <value name="ADD0">
                                                                                  <block type="text" id="Ji~6sz[EnevFbxY[jA75">
                                                                                    <field name="TEXT">clock</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD1">
                                                                                  <block type="text" id="r{^8_]O2Gd}??)v*2e,o">
                                                                                    <field name="TEXT">thermometer</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD2">
                                                                                  <block type="text" id="QxZ|xRW,2s+~Cq5d7EE=">
                                                                                    <field name="TEXT">water-percent</field>
                                                                                  </block>
                                                                                </value>
                                                                                <value name="ADD3">
                                                                                  <block type="text" id="aG59A=2KjBO$8]{*fKbx">
                                                                                    <field name="TEXT">car-speed-limiter</field>
                                                                                  </block>
                                                                                </value>
                                                                              </block>
                                                                            </value>
                                                                            <next>
                                                                              <block type="comment" id="aKv%|di[CtSIh!D`(#gX">
                                                                                <field name="COMMENT">Font 0 - Default - Size 24 (No Icons, Support for various special chars from different langs) </field>
                                                                                <next>
                                                                                  <block type="comment" id="+r5N^`^j1p[P,5J`Le^Q">
                                                                                    <field name="COMMENT">Font 1 - Size 32 (Icons and limited chars) </field>
                                                                                    <next>
                                                                                      <block type="comment" id="tUOdMlG-_thdgbYnc4nm">
                                                                                        <field name="COMMENT">Font 2 - Size 32 (No Icons, Support for various special chars from different langs) </field>
                                                                                        <next>
                                                                                          <block type="comment" id="@lerf@f9)v[4nMzqv5gt">
                                                                                            <field name="COMMENT">Font 3 - Size 48 (Icons and limited chars) </field>
                                                                                            <next>
                                                                                              <block type="comment" id="bZgk)F:jLfyS.IJvAr$V">
                                                                                                <field name="COMMENT">Font 4 - Size 80 (Icons and limited chars)</field>
                                                                                                <next>
                                                                                                  <block type="comment" id="clX[{}N_[.*S=k%*0cLW">
                                                                                                    <field name="COMMENT">Font 5 - Size 128 (ascii only)</field>
                                                                                                    <next>
                                                                                                      <block type="variables_set" id="5p9m!(nJ}iGu?9Ex7KYc">
                                                                                                        <field name="VAR" id="n%`;Bp1UH/yVByUHY*9b">FontSize</field>
                                                                                                        <value name="VALUE">
                                                                                                          <block type="lists_create_with" id="fblI%hv]`?Co1Y-+sfTP">
                                                                                                            <mutation items="4"></mutation>
                                                                                                            <value name="ADD0">
                                                                                                              <block type="math_number" id="^)oAb-m3)a2qMfx%{F6T">
                                                                                                                <field name="NUM">4</field>
                                                                                                              </block>
                                                                                                            </value>
                                                                                                            <value name="ADD1">
                                                                                                              <block type="math_number" id="wYStw[Uw2cGDsh(WMSzE">
                                                                                                                <field name="NUM">4</field>
                                                                                                              </block>
                                                                                                            </value>
                                                                                                            <value name="ADD2">
                                                                                                              <block type="math_number" id="7~NoZ:|e@5o}alTv^c:]">
                                                                                                                <field name="NUM">4</field>
                                                                                                              </block>
                                                                                                            </value>
                                                                                                            <value name="ADD3">
                                                                                                              <block type="math_number" id="XQ+MBjj`Bmb{YMj(^~$v">
                                                                                                                <field name="NUM">4</field>
                                                                                                              </block>
                                                                                                            </value>
                                                                                                          </block>
                                                                                                        </value>
                                                                                                        <next>
                                                                                                          <block type="comment" id="1|4*7{{`=6agLOA|rY}X">
                                                                                                            <field name="COMMENT">Text oder Sensordaten</field>
                                                                                                            <next>
                                                                                                              <block type="variables_set" id="42f6I36pzY%^j$dQ)P%^">
                                                                                                                <field name="VAR" id="e%^+o,6sf9B/FYnuhoqQ">Text</field>
                                                                                                                <value name="VALUE">
                                                                                                                  <block type="lists_create_with" id="SVU6Ucg![qiSxerdD+mv">
                                                                                                                    <mutation items="4"></mutation>
                                                                                                                    <value name="ADD0">
                                                                                                                      <block type="convert_tostring" id="aKsR2QJD%]jm;WWFv^d:">
                                                                                                                        <value name="VALUE">
                                                                                                                          <block type="time_get" id="o.R[,nuFt!=z^9-{;-Dl">
                                                                                                                            <mutation xmlns="http://www.w3.org/1999/xhtml" format="false" language="false"></mutation>
                                                                                                                            <field name="OPTION">hh:mm</field>
                                                                                                                          </block>
                                                                                                                        </value>
                                                                                                                      </block>
                                                                                                                    </value>
                                                                                                                    <value name="ADD1">
                                                                                                                      <block type="text_join" id="4=,76hqfY.9/g.~n[03C">
                                                                                                                        <mutation items="2"></mutation>
                                                                                                                        <value name="ADD0">
                                                                                                                          <block type="variables_get" id="Wly~BGOs02ySg1OOi,|u">
                                                                                                                            <field name="VAR" id="UIsM8Eact}h@ZW5?xVbR">Sensor_Temperatur</field>
                                                                                                                          </block>
                                                                                                                        </value>
                                                                                                                        <value name="ADD1">
                                                                                                                          <block type="text" id="VDO{sH([6L!x5#Svp7sF">
                                                                                                                            <field name="TEXT"> °C</field>
                                                                                                                          </block>
                                                                                                                        </value>
                                                                                                                      </block>
                                                                                                                    </value>
                                                                                                                    <value name="ADD2">
                                                                                                                      <block type="text_join" id="*?t?Dd~4u{w(Pz[1WBLG">
                                                                                                                        <mutation items="2"></mutation>
                                                                                                                        <value name="ADD0">
                                                                                                                          <block type="variables_get" id="BGnINq:/jfk##b11G]oh">
                                                                                                                            <field name="VAR" id="~WSzaicRZ8#urLe2[R=k">Sensor_Lutfeuchte</field>
                                                                                                                          </block>
                                                                                                                        </value>
                                                                                                                        <value name="ADD1">
                                                                                                                          <block type="text" id="wf_|6[5_]DhE%!pF=@[2">
                                                                                                                            <field name="TEXT"> %</field>
                                                                                                                          </block>
                                                                                                                        </value>
                                                                                                                      </block>
                                                                                                                    </value>
                                                                                                                    <value name="ADD3">
                                                                                                                      <block type="text_join" id="*gvlhRb5NB.d{}JF=`.V">
                                                                                                                        <mutation items="2"></mutation>
                                                                                                                        <value name="ADD0">
                                                                                                                          <block type="variables_get" id="zcu(qzk4WzJ=Zv`d!oNZ">
                                                                                                                            <field name="VAR" id="caeHuwwu}!^U=Jns}u%t">Sensor_Luftdruck</field>
                                                                                                                          </block>
                                                                                                                        </value>
                                                                                                                        <value name="ADD1">
                                                                                                                          <block type="text" id="3Y~0vG4[$iTKSHT;Mpz3">
                                                                                                                            <field name="TEXT"> hPa</field>
                                                                                                                          </block>
                                                                                                                        </value>
                                                                                                                      </block>
                                                                                                                    </value>
                                                                                                                  </block>
                                                                                                                </value>
                                                                                                                <next>
                                                                                                                  <block type="schedule" id="U-4ddK7pM21IC2DZ3*,7">
                                                                                                                    <field name="SCHEDULE">*/5 * * * * *</field>
                                                                                                                    <statement name="STATEMENT">
                                                                                                                      <block type="lists_setIndex" id="1+OL;,34r/VFKuu2zx6n">
                                                                                                                        <mutation at="true"></mutation>
                                                                                                                        <field name="MODE">SET</field>
                                                                                                                        <field name="WHERE">FROM_START</field>
                                                                                                                        <value name="LIST">
                                                                                                                          <block type="variables_get" id="J:wdR.){K9LDC|d_LH$T">
                                                                                                                            <field name="VAR" id="e%^+o,6sf9B/FYnuhoqQ">Text</field>
                                                                                                                          </block>
                                                                                                                        </value>
                                                                                                                        <value name="AT">
                                                                                                                          <block type="math_number" id="9_V=`mXu+Wm)lJ275EP[">
                                                                                                                            <field name="NUM">1</field>
                                                                                                                          </block>
                                                                                                                        </value>
                                                                                                                        <value name="TO">
                                                                                                                          <block type="convert_tostring" id="@obyv{DZy3wLv~Ysdylj">
                                                                                                                            <value name="VALUE">
                                                                                                                              <block type="time_get" id="1h,YOr;^qtt[)g]Qd:8t">
                                                                                                                                <mutation xmlns="http://www.w3.org/1999/xhtml" format="false" language="false"></mutation>
                                                                                                                                <field name="OPTION">hh:mm</field>
                                                                                                                              </block>
                                                                                                                            </value>
                                                                                                                          </block>
                                                                                                                        </value>
                                                                                                                        <next>
                                                                                                                          <block type="control_ex" id="KtA?uX2s-h=6FkK5E--N">
                                                                                                                            <field name="TYPE">false</field>
                                                                                                                            <field name="CLEAR_RUNNING">FALSE</field>
                                                                                                                            <value name="OID">
                                                                                                                              <shadow type="field_oid" id="b[-*zw~9*A3F*[]%Om~3">
                                                                                                                                <field name="oid">Object ID</field>
                                                                                                                              </shadow>
                                                                                                                              <block type="text_join" id="{0__[Pcpe!ZHo-r+*bf:">
                                                                                                                                <mutation items="2"></mutation>
                                                                                                                                <value name="ADD0">
                                                                                                                                  <block type="variables_get" id="GfgJkb;fG,c^kI[qnEc1">
                                                                                                                                    <field name="VAR" id="7Q3%H,r3WG((Q;]w,bbK">0_userdata_Path</field>
                                                                                                                                  </block>
                                                                                                                                </value>
                                                                                                                                <value name="ADD1">
                                                                                                                                  <block type="text" id="f98;yX!r.O8A3p+SP|G(">
                                                                                                                                    <field name="TEXT">popupNotifyHeading</field>
                                                                                                                                  </block>
                                                                                                                                </value>
                                                                                                                              </block>
                                                                                                                            </value>
                                                                                                                            <value name="VALUE">
                                                                                                                              <shadow type="logic_boolean" id="L_yvKy)2.4$YL1]eq;{l">
                                                                                                                                <field name="BOOL">TRUE</field>
                                                                                                                              </shadow>
                                                                                                                              <block type="lists_getIndex" id="_g`XG{z;.#`~2[Ax6|of">
                                                                                                                                <mutation statement="false" at="true"></mutation>
                                                                                                                                <field name="MODE">GET</field>
                                                                                                                                <field name="WHERE">FROM_START</field>
                                                                                                                                <value name="VALUE">
                                                                                                                                  <block type="variables_get" id="%`l~)W-tL1y=YR.4Dzi!">
                                                                                                                                    <field name="VAR" id="6sx!Ebx43k2^RFs;w0^K">HeadingText</field>
                                                                                                                                  </block>
                                                                                                                                </value>
                                                                                                                                <value name="AT">
                                                                                                                                  <block type="variables_get" id="^6gJ@h2EDap%OAfBDkyQ">
                                                                                                                                    <field name="VAR" id="#?MpfqBMCW|l*?q]RI[X">i</field>
                                                                                                                                  </block>
                                                                                                                                </value>
                                                                                                                              </block>
                                                                                                                            </value>
                                                                                                                            <value name="DELAY_MS">
                                                                                                                              <shadow type="math_number" id="OW68u!evOdS(H:ivZ#J/">
                                                                                                                                <field name="NUM">0</field>
                                                                                                                              </shadow>
                                                                                                                            </value>
                                                                                                                            <next>
                                                                                                                              <block type="control_ex" id="hG6k{T-.^N^l*f,]ZrNB">
                                                                                                                                <field name="TYPE">false</field>
                                                                                                                                <field name="CLEAR_RUNNING">FALSE</field>
                                                                                                                                <value name="OID">
                                                                                                                                  <shadow type="field_oid">
                                                                                                                                    <field name="oid">Object ID</field>
                                                                                                                                  </shadow>
                                                                                                                                  <block type="text_join" id="]xCee:h/7dD@P^Cfq,c/">
                                                                                                                                    <mutation items="2"></mutation>
                                                                                                                                    <value name="ADD0">
                                                                                                                                      <block type="variables_get" id="E(mbFtkv+6!wvR_?H6G7">
                                                                                                                                        <field name="VAR" id="7Q3%H,r3WG((Q;]w,bbK">0_userdata_Path</field>
                                                                                                                                      </block>
                                                                                                                                    </value>
                                                                                                                                    <value name="ADD1">
                                                                                                                                      <block type="text" id="TKU!xgmlF2ibxh?Nt/RL">
                                                                                                                                        <field name="TEXT">popupNotifyText</field>
                                                                                                                                      </block>
                                                                                                                                    </value>
                                                                                                                                  </block>
                                                                                                                                </value>
                                                                                                                                <value name="VALUE">
                                                                                                                                  <shadow type="logic_boolean">
                                                                                                                                    <field name="BOOL">TRUE</field>
                                                                                                                                  </shadow>
                                                                                                                                  <block type="lists_getIndex" id="!u7Zw{NnBDW~x8+_ZCHd">
                                                                                                                                    <mutation statement="false" at="true"></mutation>
                                                                                                                                    <field name="MODE">GET</field>
                                                                                                                                    <field name="WHERE">FROM_START</field>
                                                                                                                                    <value name="VALUE">
                                                                                                                                      <block type="variables_get" id="x,Us%3OwtWWi]Nd!7njK">
                                                                                                                                        <field name="VAR" id="e%^+o,6sf9B/FYnuhoqQ">Text</field>
                                                                                                                                      </block>
                                                                                                                                    </value>
                                                                                                                                    <value name="AT">
                                                                                                                                      <block type="variables_get" id="6e`5#3?`qDOGH.6q`a0P">
                                                                                                                                        <field name="VAR" id="#?MpfqBMCW|l*?q]RI[X">i</field>
                                                                                                                                      </block>
                                                                                                                                    </value>
                                                                                                                                  </block>
                                                                                                                                </value>
                                                                                                                                <value name="DELAY_MS">
                                                                                                                                  <shadow type="math_number" id="|Tr{+H=7b/qXfSTo({t~">
                                                                                                                                    <field name="NUM">0</field>
                                                                                                                                  </shadow>
                                                                                                                                </value>
                                                                                                                                <next>
                                                                                                                                  <block type="control_ex" id="F+F9Sk6]69W:)[:n@vX/">
                                                                                                                                    <field name="TYPE">false</field>
                                                                                                                                    <field name="CLEAR_RUNNING">FALSE</field>
                                                                                                                                    <value name="OID">
                                                                                                                                      <shadow type="field_oid">
                                                                                                                                        <field name="oid">Object ID</field>
                                                                                                                                      </shadow>
                                                                                                                                      <block type="text_join" id="b9GuVy.TEzA.-}/qdzZN">
                                                                                                                                        <mutation items="2"></mutation>
                                                                                                                                        <value name="ADD0">
                                                                                                                                          <block type="variables_get" id="DSjeUg9RvA2,WCaeMfd@">
                                                                                                                                            <field name="VAR" id="7Q3%H,r3WG((Q;]w,bbK">0_userdata_Path</field>
                                                                                                                                          </block>
                                                                                                                                        </value>
                                                                                                                                        <value name="ADD1">
                                                                                                                                          <block type="text" id="|wYb/ve-Y*jnE%ca!I_G">
                                                                                                                                            <field name="TEXT">popupNotifyButton1Text</field>
                                                                                                                                          </block>
                                                                                                                                        </value>
                                                                                                                                      </block>
                                                                                                                                    </value>
                                                                                                                                    <value name="VALUE">
                                                                                                                                      <shadow type="logic_boolean">
                                                                                                                                        <field name="BOOL">TRUE</field>
                                                                                                                                      </shadow>
                                                                                                                                      <block type="variables_get" id="*X6QutFAYIY$iK5V+~UD">
                                                                                                                                        <field name="VAR" id="+s+k$`6x!Mb[t~Ts^Zrp">Button1Text</field>
                                                                                                                                      </block>
                                                                                                                                    </value>
                                                                                                                                    <value name="DELAY_MS">
                                                                                                                                      <shadow type="math_number" id="Ml=_Ulq81[g69a)@|Qkm">
                                                                                                                                        <field name="NUM">0</field>
                                                                                                                                      </shadow>
                                                                                                                                    </value>
                                                                                                                                    <next>
                                                                                                                                      <block type="control_ex" id="3Z)3)(|.(hkIx3-PT@|P">
                                                                                                                                        <field name="TYPE">false</field>
                                                                                                                                        <field name="CLEAR_RUNNING">FALSE</field>
                                                                                                                                        <value name="OID">
                                                                                                                                          <shadow type="field_oid">
                                                                                                                                            <field name="oid">Object ID</field>
                                                                                                                                          </shadow>
                                                                                                                                          <block type="text_join" id="0#.$9%@5zvXChK]o?Ea-">
                                                                                                                                            <mutation items="2"></mutation>
                                                                                                                                            <value name="ADD0">
                                                                                                                                              <block type="variables_get" id="Vlqn+`oBU)ah9-3j.C/6">
                                                                                                                                                <field name="VAR" id="7Q3%H,r3WG((Q;]w,bbK">0_userdata_Path</field>
                                                                                                                                              </block>
                                                                                                                                            </value>
                                                                                                                                            <value name="ADD1">
                                                                                                                                              <block type="text" id="[#Qn_6*0:SEOF8c(e(O{">
                                                                                                                                                <field name="TEXT">popupNotifyButton2Text</field>
                                                                                                                                              </block>
                                                                                                                                            </value>
                                                                                                                                          </block>
                                                                                                                                        </value>
                                                                                                                                        <value name="VALUE">
                                                                                                                                          <shadow type="logic_boolean" id="b,d/aOuz,.z7YW9u.t)L">
                                                                                                                                            <field name="BOOL">TRUE</field>
                                                                                                                                          </shadow>
                                                                                                                                          <block type="variables_get" id="REAQ|_d7R|Nseprua+z)">
                                                                                                                                            <field name="VAR" id="iP=Bs[zV55PS82(Q$`|7">Button2Text</field>
                                                                                                                                          </block>
                                                                                                                                        </value>
                                                                                                                                        <value name="DELAY_MS">
                                                                                                                                          <shadow type="math_number" id="-hKt9zkZ)EW}2JPfUQ0P">
                                                                                                                                            <field name="NUM">0</field>
                                                                                                                                          </shadow>
                                                                                                                                        </value>
                                                                                                                                        <next>
                                                                                                                                          <block type="control_ex" id="E6Fv|5]Mo`o2V#.X:C!l">
                                                                                                                                            <field name="TYPE">false</field>
                                                                                                                                            <field name="CLEAR_RUNNING">FALSE</field>
                                                                                                                                            <value name="OID">
                                                                                                                                              <shadow type="field_oid">
                                                                                                                                                <field name="oid">Object ID</field>
                                                                                                                                              </shadow>
                                                                                                                                              <block type="text_join" id="e%zigg.})n+9kv=nF?U:">
                                                                                                                                                <mutation items="2"></mutation>
                                                                                                                                                <value name="ADD0">
                                                                                                                                                  <block type="variables_get" id="E-K;vy1^]dwA_.QTR%vY">
                                                                                                                                                    <field name="VAR" id="7Q3%H,r3WG((Q;]w,bbK">0_userdata_Path</field>
                                                                                                                                                  </block>
                                                                                                                                                </value>
                                                                                                                                                <value name="ADD1">
                                                                                                                                                  <block type="text" id="]Dfo.AuiBLRnzoy2y^5+">
                                                                                                                                                    <field name="TEXT">popupNotifyIcon</field>
                                                                                                                                                  </block>
                                                                                                                                                </value>
                                                                                                                                              </block>
                                                                                                                                            </value>
                                                                                                                                            <value name="VALUE">
                                                                                                                                              <shadow type="logic_boolean">
                                                                                                                                                <field name="BOOL">TRUE</field>
                                                                                                                                              </shadow>
                                                                                                                                              <block type="lists_getIndex" id="n)hhvq!@eP4fpgv]{t;L">
                                                                                                                                                <mutation statement="false" at="true"></mutation>
                                                                                                                                                <field name="MODE">GET</field>
                                                                                                                                                <field name="WHERE">FROM_START</field>
                                                                                                                                                <value name="VALUE">
                                                                                                                                                  <block type="variables_get" id="vnPh!svY^|ea(Qy%7D4;">
                                                                                                                                                    <field name="VAR" id=")S5LKNN/K5V9|_8OXyGn">Icon</field>
                                                                                                                                                  </block>
                                                                                                                                                </value>
                                                                                                                                                <value name="AT">
                                                                                                                                                  <block type="variables_get" id="NzDd.GJ,LAb5{:b9BKW$">
                                                                                                                                                    <field name="VAR" id="#?MpfqBMCW|l*?q]RI[X">i</field>
                                                                                                                                                  </block>
                                                                                                                                                </value>
                                                                                                                                              </block>
                                                                                                                                            </value>
                                                                                                                                            <value name="DELAY_MS">
                                                                                                                                              <shadow type="math_number" id="mwhM5`NFI5gHFUI=k?l$">
                                                                                                                                                <field name="NUM">0</field>
                                                                                                                                              </shadow>
                                                                                                                                            </value>
                                                                                                                                            <next>
                                                                                                                                              <block type="control_ex" id="e8uy*Pv6GuNS8aYQ*VK]">
                                                                                                                                                <field name="TYPE">false</field>
                                                                                                                                                <field name="CLEAR_RUNNING">FALSE</field>
                                                                                                                                                <value name="OID">
                                                                                                                                                  <shadow type="field_oid">
                                                                                                                                                    <field name="oid">Object ID</field>
                                                                                                                                                  </shadow>
                                                                                                                                                  <block type="text_join" id="z+#e[O1i?5p39o`mKa%H">
                                                                                                                                                    <mutation items="2"></mutation>
                                                                                                                                                    <value name="ADD0">
                                                                                                                                                      <block type="variables_get" id="w(,@Ea[q^648(ct7uMuu">
                                                                                                                                                        <field name="VAR" id="7Q3%H,r3WG((Q;]w,bbK">0_userdata_Path</field>
                                                                                                                                                      </block>
                                                                                                                                                    </value>
                                                                                                                                                    <value name="ADD1">
                                                                                                                                                      <block type="text" id="qe{^,D}.QwO`cVxy/0lY">
                                                                                                                                                        <field name="TEXT">popupNotifyFontIdText</field>
                                                                                                                                                      </block>
                                                                                                                                                    </value>
                                                                                                                                                  </block>
                                                                                                                                                </value>
                                                                                                                                                <value name="VALUE">
                                                                                                                                                  <shadow type="logic_boolean">
                                                                                                                                                    <field name="BOOL">TRUE</field>
                                                                                                                                                  </shadow>
                                                                                                                                                  <block type="lists_getIndex" id="~Ya(l{Klir2gjz_Rs|lU">
                                                                                                                                                    <mutation statement="false" at="true"></mutation>
                                                                                                                                                    <field name="MODE">GET</field>
                                                                                                                                                    <field name="WHERE">FROM_START</field>
                                                                                                                                                    <value name="VALUE">
                                                                                                                                                      <block type="variables_get" id="~XuGUXm/c1-u^QZwNG:?">
                                                                                                                                                        <field name="VAR" id="n%`;Bp1UH/yVByUHY*9b">FontSize</field>
                                                                                                                                                      </block>
                                                                                                                                                    </value>
                                                                                                                                                    <value name="AT">
                                                                                                                                                      <block type="variables_get" id="Y:d)mhntP8(zQP~Mhr!N">
                                                                                                                                                        <field name="VAR" id="#?MpfqBMCW|l*?q]RI[X">i</field>
                                                                                                                                                      </block>
                                                                                                                                                    </value>
                                                                                                                                                  </block>
                                                                                                                                                </value>
                                                                                                                                                <value name="DELAY_MS">
                                                                                                                                                  <shadow type="math_number" id="+H}hyUjz|NF{:PO91Amp">
                                                                                                                                                    <field name="NUM">0</field>
                                                                                                                                                  </shadow>
                                                                                                                                                </value>
                                                                                                                                                <next>
                                                                                                                                                  <block type="comment" id="?s`?D911sLmb=(!DW/H5">
                                                                                                                                                    <field name="COMMENT">Farben</field>
                                                                                                                                                    <next>
                                                                                                                                                      <block type="control_ex" id="k}pAIbU2NC6fx,ddNOy4">
                                                                                                                                                        <field name="TYPE">false</field>
                                                                                                                                                        <field name="CLEAR_RUNNING">FALSE</field>
                                                                                                                                                        <value name="OID">
                                                                                                                                                          <shadow type="field_oid">
                                                                                                                                                            <field name="oid">Object ID</field>
                                                                                                                                                          </shadow>
                                                                                                                                                          <block type="text_join" id="G7)$yw:BL.aTmiGwk/rK">
                                                                                                                                                            <mutation items="2"></mutation>
                                                                                                                                                            <value name="ADD0">
                                                                                                                                                              <block type="variables_get" id="g^@EpqGv[x[x2r|P}F4M">
                                                                                                                                                                <field name="VAR" id="7Q3%H,r3WG((Q;]w,bbK">0_userdata_Path</field>
                                                                                                                                                              </block>
                                                                                                                                                            </value>
                                                                                                                                                            <value name="ADD1">
                                                                                                                                                              <block type="text" id="8fCdKD%2+q?4?`b;lQh`">
                                                                                                                                                                <field name="TEXT">popupNotifyHeadingColor</field>
                                                                                                                                                              </block>
                                                                                                                                                            </value>
                                                                                                                                                          </block>
                                                                                                                                                        </value>
                                                                                                                                                        <value name="VALUE">
                                                                                                                                                          <shadow type="logic_boolean">
                                                                                                                                                            <field name="BOOL">TRUE</field>
                                                                                                                                                          </shadow>
                                                                                                                                                          <block type="variables_get" id="C=O+`dda7{`bqbl-n[ba">
                                                                                                                                                            <field name="VAR" id="RLIY*e=6(.:_k@OJSC?Y">HeadingTextColor</field>
                                                                                                                                                          </block>
                                                                                                                                                        </value>
                                                                                                                                                        <value name="DELAY_MS">
                                                                                                                                                          <shadow type="math_number" id="/M,.9e?A^FnpJW6dIxbh">
                                                                                                                                                            <field name="NUM">0</field>
                                                                                                                                                          </shadow>
                                                                                                                                                        </value>
                                                                                                                                                        <next>
                                                                                                                                                          <block type="control_ex" id="/3BW4FG^eXdSm7t*e!/6">
                                                                                                                                                            <field name="TYPE">false</field>
                                                                                                                                                            <field name="CLEAR_RUNNING">FALSE</field>
                                                                                                                                                            <value name="OID">
                                                                                                                                                              <shadow type="field_oid" id="_xy9Ii5CdY+F9GwFp4g+">
                                                                                                                                                                <field name="oid">Object ID</field>
                                                                                                                                                              </shadow>
                                                                                                                                                              <block type="text_join" id="/!qDhB5w,D%V:{aB_wpg">
                                                                                                                                                                <mutation items="2"></mutation>
                                                                                                                                                                <value name="ADD0">
                                                                                                                                                                  <block type="variables_get" id="3v)4.yEZ2fGbKtGX`3ey">
                                                                                                                                                                    <field name="VAR" id="7Q3%H,r3WG((Q;]w,bbK">0_userdata_Path</field>
                                                                                                                                                                  </block>
                                                                                                                                                                </value>
                                                                                                                                                                <value name="ADD1">
                                                                                                                                                                  <block type="text" id=")A@9%?K[M8wo2ZZUe?5L">
                                                                                                                                                                    <field name="TEXT">popupNotifyTextColor</field>
                                                                                                                                                                  </block>
                                                                                                                                                                </value>
                                                                                                                                                              </block>
                                                                                                                                                            </value>
                                                                                                                                                            <value name="VALUE">
                                                                                                                                                              <shadow type="logic_boolean" id="t~f!0F6^(~=qL9f6~_oc">
                                                                                                                                                                <field name="BOOL">TRUE</field>
                                                                                                                                                              </shadow>
                                                                                                                                                              <block type="variables_get" id="Df/fUIbt82CM3o2ogA,X">
                                                                                                                                                                <field name="VAR" id="K~gzNq|K||t-`B*`Kcr`">TextColor</field>
                                                                                                                                                              </block>
                                                                                                                                                            </value>
                                                                                                                                                            <value name="DELAY_MS">
                                                                                                                                                              <shadow type="math_number" id="eR{B_FXP*E3vS80#CCf:">
                                                                                                                                                                <field name="NUM">0</field>
                                                                                                                                                              </shadow>
                                                                                                                                                            </value>
                                                                                                                                                            <next>
                                                                                                                                                              <block type="comment" id="iFc,dYv9#FZk,4kqcuFk">
                                                                                                                                                                <field name="COMMENT">Zum Schuss InternalName (Trigger)</field>
                                                                                                                                                                <next>
                                                                                                                                                                  <block type="control_ex" id="L(~Pj.ix0^{Ya/r#3[0K">
                                                                                                                                                                    <field name="TYPE">false</field>
                                                                                                                                                                    <field name="CLEAR_RUNNING">FALSE</field>
                                                                                                                                                                    <value name="OID">
                                                                                                                                                                      <shadow type="field_oid">
                                                                                                                                                                        <field name="oid">Object ID</field>
                                                                                                                                                                      </shadow>
                                                                                                                                                                      <block type="text_join" id="OlxQxLn/pYGmeA_xRnO8">
                                                                                                                                                                        <mutation items="2"></mutation>
                                                                                                                                                                        <value name="ADD0">
                                                                                                                                                                          <block type="variables_get" id="Z.!S^TTi/upc/Nl*cxRY">
                                                                                                                                                                            <field name="VAR" id="7Q3%H,r3WG((Q;]w,bbK">0_userdata_Path</field>
                                                                                                                                                                          </block>
                                                                                                                                                                        </value>
                                                                                                                                                                        <value name="ADD1">
                                                                                                                                                                          <block type="text" id="Z#)T9XCNj(g@_4Gp`k2R">
                                                                                                                                                                            <field name="TEXT">popupNotifyInternalName</field>
                                                                                                                                                                          </block>
                                                                                                                                                                        </value>
                                                                                                                                                                      </block>
                                                                                                                                                                    </value>
                                                                                                                                                                    <value name="VALUE">
                                                                                                                                                                      <shadow type="logic_boolean">
                                                                                                                                                                        <field name="BOOL">TRUE</field>
                                                                                                                                                                      </shadow>
                                                                                                                                                                      <block type="lists_getIndex" id="}#tL$1].x^u5K.,%*~?+">
                                                                                                                                                                        <mutation statement="false" at="true"></mutation>
                                                                                                                                                                        <field name="MODE">GET</field>
                                                                                                                                                                        <field name="WHERE">FROM_START</field>
                                                                                                                                                                        <value name="VALUE">
                                                                                                                                                                          <block type="variables_get" id="M8w@CJqHS)q[|s?lPKLn">
                                                                                                                                                                            <field name="VAR" id="6sx!Ebx43k2^RFs;w0^K">HeadingText</field>
                                                                                                                                                                          </block>
                                                                                                                                                                        </value>
                                                                                                                                                                        <value name="AT">
                                                                                                                                                                          <block type="variables_get" id="qL@?;F_N~=WoTq:?,X.Y">
                                                                                                                                                                            <field name="VAR" id="#?MpfqBMCW|l*?q]RI[X">i</field>
                                                                                                                                                                          </block>
                                                                                                                                                                        </value>
                                                                                                                                                                      </block>
                                                                                                                                                                    </value>
                                                                                                                                                                    <value name="DELAY_MS">
                                                                                                                                                                      <shadow type="math_number" id="SLN(b%5k(a6xbm3U_cuX">
                                                                                                                                                                        <field name="NUM">0</field>
                                                                                                                                                                      </shadow>
                                                                                                                                                                    </value>
                                                                                                                                                                    <next>
                                                                                                                                                                      <block type="controls_if" id="ow;^lRZ-Ilt^t8FxHvAB">
                                                                                                                                                                        <mutation else="1"></mutation>
                                                                                                                                                                        <value name="IF0">
                                                                                                                                                                          <block type="logic_compare" id="qi}D0]*xjQ]+-@yJ8H0D">
                                                                                                                                                                            <field name="OP">EQ</field>
                                                                                                                                                                            <value name="A">
                                                                                                                                                                              <block type="variables_get" id="O@o^%WEIe5aX?5Nzk|{T">
                                                                                                                                                                                <field name="VAR" id="#?MpfqBMCW|l*?q]RI[X">i</field>
                                                                                                                                                                              </block>
                                                                                                                                                                            </value>
                                                                                                                                                                            <value name="B">
                                                                                                                                                                              <block type="lists_length" id=")65Ex%xEDX+T|[fjS6-M">
                                                                                                                                                                                <value name="VALUE">
                                                                                                                                                                                  <block type="variables_get" id=":TljLB4j,Dbg(1CbBsb`">
                                                                                                                                                                                    <field name="VAR" id="6sx!Ebx43k2^RFs;w0^K">HeadingText</field>
                                                                                                                                                                                  </block>
                                                                                                                                                                                </value>
                                                                                                                                                                              </block>
                                                                                                                                                                            </value>
                                                                                                                                                                          </block>
                                                                                                                                                                        </value>
                                                                                                                                                                        <statement name="DO0">
                                                                                                                                                                          <block type="variables_set" id="S%n3B6G2LY0/41=z[89j">
                                                                                                                                                                            <field name="VAR" id="#?MpfqBMCW|l*?q]RI[X">i</field>
                                                                                                                                                                            <value name="VALUE">
                                                                                                                                                                              <block type="math_number" id="oFB,97B}*NYW:;=)w(Sx">
                                                                                                                                                                                <field name="NUM">1</field>
                                                                                                                                                                              </block>
                                                                                                                                                                            </value>
                                                                                                                                                                          </block>
                                                                                                                                                                        </statement>
                                                                                                                                                                        <statement name="ELSE">
                                                                                                                                                                          <block type="math_change" id="s0-P!tG!UgB8t6vbR03G">
                                                                                                                                                                            <field name="VAR" id="#?MpfqBMCW|l*?q]RI[X">i</field>
                                                                                                                                                                            <value name="DELTA">
                                                                                                                                                                              <shadow type="math_number" id="7.eLfBS{0kkyTn#,I:B4">
                                                                                                                                                                                <field name="NUM">1</field>
                                                                                                                                                                              </shadow>
                                                                                                                                                                              <block type="math_number" id="v}2ivqnyQ2W`E`r@UNS0">
                                                                                                                                                                                <field name="NUM">1</field>
                                                                                                                                                                              </block>
                                                                                                                                                                            </value>
                                                                                                                                                                          </block>
                                                                                                                                                                        </statement>
                                                                                                                                                                      </block>
                                                                                                                                                                    </next>
                                                                                                                                                                  </block>
                                                                                                                                                                </next>
                                                                                                                                                              </block>
                                                                                                                                                            </next>
                                                                                                                                                          </block>
                                                                                                                                                        </next>
                                                                                                                                                      </block>
                                                                                                                                                    </next>
                                                                                                                                                  </block>
                                                                                                                                                </next>
                                                                                                                                              </block>
                                                                                                                                            </next>
                                                                                                                                          </block>
                                                                                                                                        </next>
                                                                                                                                      </block>
                                                                                                                                    </next>
                                                                                                                                  </block>
                                                                                                                                </next>
                                                                                                                              </block>
                                                                                                                            </next>
                                                                                                                          </block>
                                                                                                                        </next>
                                                                                                                      </block>
                                                                                                                    </statement>
                                                                                                                  </block>
                                                                                                                </next>
                                                                                                              </block>
                                                                                                            </next>
                                                                                                          </block>
                                                                                                        </next>
                                                                                                      </block>
                                                                                                    </next>
                                                                                                  </block>
                                                                                                </next>
                                                                                              </block>
                                                                                            </next>
                                                                                          </block>
                                                                                        </next>
                                                                                      </block>
                                                                                    </next>
                                                                                  </block>
                                                                                </next>
                                                                              </block>
                                                                            </next>
                                                                          </block>
                                                                        </next>
                                                                      </block>
                                                                    </next>
                                                                  </block>
                                                                </next>
                                                              </block>
                                                            </next>
                                                          </block>
                                                        </next>
                                                      </block>
                                                    </next>
                                                  </block>
                                                </next>
                                              </block>
                                            </next>
                                          </block>
                                        </next>
                                      </block>
                                    </next>
                                  </block>
                                </next>
                              </block>
                            </next>
                          </block>
                        </next>
                      </block>
                    </next>
                  </block>
                </next>
              </block>
            </next>
          </block>
        </next>
      </block>
    </next>
  </block>
</xml>
  ```