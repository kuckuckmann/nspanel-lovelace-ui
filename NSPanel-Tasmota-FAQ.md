
# Index
## 1.) Hardware-Buttons  
### 1.1) Rules  
### 1.2) Multipress Mode  
### 1.3) Shutter Mode  
### 1.4) Switchmode  
## 2.) Sensoren  
  **2.1)**    Analoger Raum-Temperatur-Sensor  
  **2.2)**    ESP-Temperartur-Sensor  


## 1. Hardware-Buttons

***

### 1.1  Tasmota Rules
Tasmota verfügt über optional zu definierende Regeln (rules), die das System besonders flexibel einsetzbar machen.

https://tasmota.github.io/docs/Rules/

#### 1.1.1    Rule2 - Favoriten Seiten

**Beide Hardware-Buttons als Dialog - Die internen Relais werden dabei nicht geschaltet**  
`Rule2 on Button1#state do Publish SmartHome/%topic%/tele/RESULT {"CustomRecv":"event,button1"} endon on Button2#state do Publish SmartHome/%topic%/tele/RESULT {"CustomRecv":"event,button2"} endon`  

**Rechter Button Dialog - Linker Button Schalter**  
`Rule2 on Button1#state do Publish SmartHome/%topic%/tele/RESULT {"CustomRecv":"event,button1"} endon`  

**Rechter Button Schalter - Linker Button Dialog**  
`Rule2 on Button2#state do Publish SmartHome/%topic%/tele/RESULT {"CustomRecv":"event,button2"} endon`  

Zum Anschalten der Rule  
`Rule2` 1 oder `Rule2 On`  

Zum Ausschalten der Rule  
`Rule2` 0 oder `Rule2 Off`  

**Nutzung in ioBroker:**  
Die Seiten können über die button1Page und/oder button2Page definiert werden (Hier im Beispiel eine Schnell-Auswahl an Radiosendern oder Playlists):  
 
![image](https://user-images.githubusercontent.com/102996011/189394576-f470cba5-0fe6-4a46-97f6-0cd6c48a613b.png)

#### 1.1.2    Rule3 - ESP-Buzzer 

Der eingebaute Buzzer des ESP32 kann auch Geräusche zur Unterstützung der Tastenbetätigung erzeugen Hierzu muss folgende Rule angelegt und aktiviert werden:  

`rule3 on CustomRecv do Buzzer 1 endon`  
`rule3 1`  

Alternativ gibt Tasmota noch folgende Befehle per Default mit:  

`Buzzer 1`
oder  
`Buzzer 1,2,3,0xF54`  

> Weitere Infos:  
> https://tasmota.github.io/docs/Buzzer/

***

### 1.2  Multipress Mode

Man kann die physische Hardware-Buttons auch im (Multi-Press Functions) betreiben.  

`SetOption73 1`  

![image](https://user-images.githubusercontent.com/102996011/189387787-664790aa-6db2-4322-98e3-6de77f4062fe.png)  

Jeder Button sendet per /stat/RESULT "SINGLE", "DOUBLE", "TRIPLE", "QUAD" oder "PENTA". Somit hat man 5 mögliche Schaltzustände pro Button.  

Da ein sechster Klick das WifiConfig 2 ausführt, sollte dabei ebenfalls  
`SetOption1 1`  
ausgeführt werden, um zu verhindern, dass der Wifi Manager ausgeführt wird.  

> **(Rule2 dabei ausschalten)**

Falls du diese Funktion nutzen möchtest, kannst du das nachfolgende Blockly (siehe Spoiler) gerne verwenden:  

![image](https://user-images.githubusercontent.com/102996011/189388435-a3c7177b-29ca-4808-a2a5-abde22ff4209.png) 

<details>
  <summary>Blockly Skript</summary>  

 ```
<xml xmlns="https://developers.google.com/blockly/xml">
  <variables>
    <variable id="$%h)IyP*A]i!w|o;@^u~">PanelResult</variable>
    <variable id="iG,DhTT3ntIL)6jkdBSx">Action</variable>
  </variables>
  <block type="on_ext" id="Z*WW:Hq=V/0/+D.7sBGj" x="88" y="63">
    <mutation xmlns="http://www.w3.org/1999/xhtml" items="1"></mutation>
    <field name="CONDITION">any</field>
    <field name="ACK_CONDITION"></field>
    <value name="OID0">
      <shadow type="field_oid" id="s?5LPlVoKvrW,Gf/,d6(">
        <field name="oid">default</field>
      </shadow>
      <block type="field_oid" id=";VZs-nq`+#GL`5jVspo^">
        <field name="oid">mqtt.0.SmartHome.NSPanel_1.stat.RESULT</field>
      </block>
    </value>
    <statement name="STATEMENT">
      <block type="variables_set" id="W*-eYA4LLj$WMX1vlx9+">
        <field name="VAR" id="$%h)IyP*A]i!w|o;@^u~">PanelResult</field>
        <value name="VALUE">
          <block type="convert_json2object" id="H}rYz*|_N_r:7lN6kRq)">
            <value name="VALUE">
              <block type="on_source" id="ks};I#sE9{y$Os12X3%`">
                <field name="ATTR">state.val</field>
              </block>
            </value>
          </block>
        </value>
        <next>
          <block type="controls_if" id="|e+,CBW1}SywJvnEFroP">
            <mutation elseif="1"></mutation>
            <value name="IF0">
              <block type="logic_compare" id="tkA^fRI!3FU^2Tiqlahc">
                <field name="OP">EQ</field>
                <value name="A">
                  <block type="text_getSubstring" id="k}-`K]@kua~8fg*?I[t#">
                    <mutation at1="true" at2="true"></mutation>
                    <field name="WHERE1">FROM_START</field>
                    <field name="WHERE2">FROM_START</field>
                    <value name="STRING">
                      <block type="on_source" id="qCOa@52xDIv4(R#:]Yzp">
                        <field name="ATTR">state.val</field>
                      </block>
                    </value>
                    <value name="AT1">
                      <block type="math_number" id="Ncm@lgRgVYVBF~^yWKRE">
                        <field name="NUM">3</field>
                      </block>
                    </value>
                    <value name="AT2">
                      <block type="math_number" id="Gov$3|Qrd91N~RUzWea=">
                        <field name="NUM">9</field>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="B">
                  <block type="text" id="2~EGhvBs4KIPXXMcNVkx">
                    <field name="TEXT">Button1</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO0">
              <block type="variables_set" id="G!Z=C5KTj-Nl+XFa0RU_">
                <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                <value name="VALUE">
                  <block type="get_attr" id="Ed}{-}B{X+obkb^Mmk8O">
                    <value name="PATH">
                      <shadow type="text">
                        <field name="TEXT">Button2.Action</field>
                      </shadow>
                      <block type="text" id="-XSmbNSLD2q^JU.3)[(^">
                        <field name="TEXT">Button1.Action</field>
                      </block>
                    </value>
                    <value name="OBJECT">
                      <block type="variables_get" id="-%8e}:rqW1kj_iUDQyyf">
                        <field name="VAR" id="$%h)IyP*A]i!w|o;@^u~">PanelResult</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="controls_if" id="729?J2a__sAP*2PmMN2%">
                    <mutation elseif="4"></mutation>
                    <value name="IF0">
                      <block type="logic_compare" id="u9lV/l]c1,yVRl3(21(L">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="kG0ARQ1j%HKz(I=l}`:P">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="v?m}nM1~E8zR0,Ja+if+">
                            <field name="TEXT">SINGLE</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO0">
                      <block type="comment" id="iqFwhe!^P0z9-W9D[tyh">
                        <field name="COMMENT">Schalte etwas: Button1 1x gedrückt</field>
                        <next>
                          <block type="debug" id="F22M/f@lJ_xQ$t2#QW[#">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="?r3.Wy5c@$3DxmvbIGr}">
                                <field name="TEXT">Button1 SINGLE wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF1">
                      <block type="logic_compare" id="[Vpq7B,RWb4k)Bhwq{nh">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="|Whz!$I5#Iym52Pg8N?p">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="~f_cI8hrs;I)wJ-S.G3r">
                            <field name="TEXT">DOUBLE</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO1">
                      <block type="comment" id="D;PPB54t87N)%F{.hQAx">
                        <field name="COMMENT">Schalte etwas: Button1 2x gedrückt</field>
                        <next>
                          <block type="debug" id="xoG/r3;33`8/j$QeZHW5">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="9PgW|#6f8``brbWQM9q7">
                                <field name="TEXT">Button1 DOUBLE wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF2">
                      <block type="logic_compare" id="t)8drGw=u/q0Pl+ul^43">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="-lf~?Q^H8o}J:cf@I5aN">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="Z!={5~.hF?V-NFw73|BL">
                            <field name="TEXT">TRIPLE</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO2">
                      <block type="comment" id="xjdh~X8eM8ab/a/JuIM/">
                        <field name="COMMENT">Schalte etwas: Button1 3x gedrückt</field>
                        <next>
                          <block type="debug" id="n$kU%^k3$wHN/L**K=jA">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="SA^R/OJX#a7JDhE7LwL[">
                                <field name="TEXT">Button1 TRIPLE wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF3">
                      <block type="logic_compare" id="ZCUeBK[Sc08KKQVMF)tC">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id=":Jlhv9(rM!D5H*eM|Gw-">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="6NH!g[HN7f=7_q%U10M!">
                            <field name="TEXT">QUAD</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO3">
                      <block type="comment" id="77*X9-*|mO]|P0$Jw=K`">
                        <field name="COMMENT">Schalte etwas: Button1 4x gedrückt</field>
                        <next>
                          <block type="debug" id="qE@`G.#9s!UAtrlMJ/yi">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="G:19{lKn)m`B!x(NUx5S">
                                <field name="TEXT">Button1 QUAD wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF4">
                      <block type="logic_compare" id="fz#2[~sK=iF%wd=4`hB,">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="ROFyrrPZn5KJg7?Hs),Z">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="a]-o=$vOr9JDr(T!#SmL">
                            <field name="TEXT">PENTA</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO4">
                      <block type="comment" id="fxPE82.Ci3L`ME=X3nl|">
                        <field name="COMMENT">Schalte etwas: Button1 5x gedrückt</field>
                        <next>
                          <block type="debug" id="7GbZ650het?k*+CCO:nr">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="*[}-a1hl?2pc^*@4E*hI">
                                <field name="TEXT">Button1 PENTA wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                  </block>
                </next>
              </block>
            </statement>
            <value name="IF1">
              <block type="logic_compare" id="8Ev:iPPfN3B?L^Q]oOIc">
                <field name="OP">EQ</field>
                <value name="A">
                  <block type="text_getSubstring" id="xx:q0nC7,q8A8~v?PC#s">
                    <mutation at1="true" at2="true"></mutation>
                    <field name="WHERE1">FROM_START</field>
                    <field name="WHERE2">FROM_START</field>
                    <value name="STRING">
                      <block type="on_source" id="JWC4m9/7dS^!]+xQ-I0Y">
                        <field name="ATTR">state.val</field>
                      </block>
                    </value>
                    <value name="AT1">
                      <block type="math_number" id="k7=j)18I6TmB%)upvAVJ">
                        <field name="NUM">3</field>
                      </block>
                    </value>
                    <value name="AT2">
                      <block type="math_number" id=",EKn%h/uX3}ZjCvmW1KE">
                        <field name="NUM">9</field>
                      </block>
                    </value>
                  </block>
                </value>
                <value name="B">
                  <block type="text" id="Uuj{UrX@-3nNjw{n!H/@">
                    <field name="TEXT">Button2</field>
                  </block>
                </value>
              </block>
            </value>
            <statement name="DO1">
              <block type="variables_set" id="U~1k_f;62_-QkRvGZz=)">
                <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                <value name="VALUE">
                  <block type="get_attr" id="izCz6K1Y;L.7M7MlHA$c">
                    <value name="PATH">
                      <shadow type="text">
                        <field name="TEXT">Button2.Action</field>
                      </shadow>
                      <block type="text" id="y1)^1#)QjYVVA7)mWdvM">
                        <field name="TEXT">Button2.Action</field>
                      </block>
                    </value>
                    <value name="OBJECT">
                      <block type="variables_get" id="TIg$Lr%^Fuk`fxDLC:,^">
                        <field name="VAR" id="$%h)IyP*A]i!w|o;@^u~">PanelResult</field>
                      </block>
                    </value>
                  </block>
                </value>
                <next>
                  <block type="controls_if" id="tC_APU:6jW5063/l=sR1">
                    <mutation elseif="4"></mutation>
                    <value name="IF0">
                      <block type="logic_compare" id="P9XXNXzc+3H{*^w1P_@q">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="sua/L8[qi8e:U#m}d^pi">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="E^e9/nh{n@)S6e:4q3_h">
                            <field name="TEXT">SINGLE</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO0">
                      <block type="comment" id="qoOw*}O|E06w[5[cXWLo">
                        <field name="COMMENT">Schalte etwas: Button2 1x gedrückt</field>
                        <next>
                          <block type="debug" id=",tE:-UWz(0Zqlc8KBLqO">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text" id="!waPZV$J9fR+dq462%h+">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="{3#KVO|*86E:3pR/!%WP">
                                <field name="TEXT">Button2 SINGLE wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF1">
                      <block type="logic_compare" id="_Z+eBL!Zj.|LQL+_s|Ld">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="15Tx7/a!(wJ;FO+x!4JW">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="}l%?@L+:Ma!=:d2Ky/%*">
                            <field name="TEXT">DOUBLE</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO1">
                      <block type="comment" id="~72fN$sZV!.O{%*0+awy">
                        <field name="COMMENT">Schalte etwas: Button2 2x gedrückt</field>
                        <next>
                          <block type="debug" id="-T4*$n8-_X_{@6!Ga5FQ">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="LFX2j}Pr:o,{$YxQVcp2">
                                <field name="TEXT">Button2 DOUBLE wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF2">
                      <block type="logic_compare" id="6-2Eew1,aoyC]Th*AaJ5">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="4Nl6[tYm2pL@rL7v8vLI">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="zthA#*kib2r|xv+,A{Sh">
                            <field name="TEXT">TRIPLE</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO2">
                      <block type="comment" id="?OI)q#8XL#1)x.E=*m~~">
                        <field name="COMMENT">Schalte etwas: Button2 3x gedrückt</field>
                        <next>
                          <block type="debug" id="%6ZLfC`!6?Z%jXlF:mFa">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="eh|tY,l}uz:WTx}4_G_E">
                                <field name="TEXT">Button2 TRIPLE wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF3">
                      <block type="logic_compare" id="*~f.cy|6d8U0s?|^%:8R">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="tiZ6%x5iuvhh:Yi*9qB9">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="I|K0m__6/:.kuBtYQE5l">
                            <field name="TEXT">QUAD</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO3">
                      <block type="comment" id="ToQ_dt~n$Ef|8-fb|__O">
                        <field name="COMMENT">Schalte etwas: Button2 4x gedrückt</field>
                        <next>
                          <block type="debug" id="qyb7DL~:^6|r@9~KOb+A">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="tb4wo7_n@J)Q9$FLf|rV">
                                <field name="TEXT">Button2 QUAD wurde gedrückt</field>
                              </block>
                            </value>
                          </block>
                        </next>
                      </block>
                    </statement>
                    <value name="IF4">
                      <block type="logic_compare" id="M:x`b;I}a8;jJU=g}u)[">
                        <field name="OP">EQ</field>
                        <value name="A">
                          <block type="variables_get" id="Yh,)fk$+WmVXS=iwbzK{">
                            <field name="VAR" id="iG,DhTT3ntIL)6jkdBSx">Action</field>
                          </block>
                        </value>
                        <value name="B">
                          <block type="text" id="1FMk3I`mfaAfEhMd$D#e">
                            <field name="TEXT">PENTA</field>
                          </block>
                        </value>
                      </block>
                    </value>
                    <statement name="DO4">
                      <block type="comment" id="5+tVGCf{MdkG(OBDmuy|">
                        <field name="COMMENT">Schalte etwas: Button2 5x gedrückt</field>
                        <next>
                          <block type="debug" id="}{-PVi#AL#[EGD,eb?M#">
                            <field name="Severity">log</field>
                            <value name="TEXT">
                              <shadow type="text">
                                <field name="TEXT">Button</field>
                              </shadow>
                              <block type="text" id="HuBkD3zi|o@.S3w.Qh7n">
                                <field name="TEXT">Button2 PENTA wurde gedrückt</field>
                              </block>
                            </value>
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
    </statement>
  </block>
</xml>
```
</details>  


In der ersten Zeile musst du lediglich deine stat/RESULT anpassen und an den entsprechenden Kommentaren deine Aktoren einbauen.  

Da das Hardware-Buttons sind werden die extern verarbeitet (nicht über das TS-Skript)  

***

### 1.3  Shuttermode

Um die zwei Hardware-Buttons direkt in eine Rollladensteuerung umzuwandeln sind folgende Schritte erforderlich 

In der Tasmota-Konsole folgende Konfigurationen einstellen:
> `SetOption80 1`  
> `ShutterRelay1 1`  
> `Interlock 1,2`  
> `Interlock ON`  

![image](https://user-images.githubusercontent.com/102996011/189386244-7d4fa7d3-de96-4608-975d-8c5853e2e721.png)

Für Shutter mode 1:
> `Rule2 0`  
> `SetOption73 0`  
> `SetOption114 0`  

Wenn du einen anderen brauchst, dann entsprechend der Anleitung vorgehen:
https://tasmota.github.io/docs/Blinds-and-Shutters/

Da kann man die auch kalibrieren.

***

### 1.4  Switchmode

Die Hardware Buttons sind im Blakadder-Template als "Buttons" konfiguriert.  
![image](https://user-images.githubusercontent.com/102996011/189384620-7bd59a70-d807-451b-84d3-bf40b9b0c1d8.png)

> **SwitchMode gilt, wie der Name schon sagt, NUR für GPIO, das in Tasmota als Switch<x>-Komponente konfiguriert ist. SwitchMode hat KEINEN Einfluss auf das Verhalten von GPIO, das als Button<x>-Komponenten konfiguriert ist.**

**Der GPIO14 und der GPIO27 sind "Button<x>" (x=1 und 2)**

Um die Tasmota-Switchmode-Funktion für die Hardware-Buttons zu nutzen, müssen die Button GPIO's in Tasmota zu Switch GPIO's umkonfiguriert werden:  
![image](https://user-images.githubusercontent.com/102996011/189382319-3830b438-2e4c-40c8-930e-46177d48b146.png)  

![image](https://user-images.githubusercontent.com/102996011/189382449-5d870f37-10b8-4f59-8ea1-8a38aa8d3a0b.png)  

Für einen ganz normalen Taster (gedrückt an/loslassen aus) wären optional folgende Einstellungen notwendig  

Alternativ folgendes Template aktivieren  
`{"NAME":"NSPanel_1","GPIO":[0,0,0,0,3872,0,0,0,0,0,160,0,0,0,0,225,0,480,224,1,0,0,0,161,0,0,0,0,0,0,0,0,0,0,4736,0],"FLAG":0,"BASE":1}`  

Danach in der Tasmota-Konsole  
> `switchmode1 2`  
> `switchmode2 2`  
ausführen  

***  

## 2. Sensoren  

***  
### 2.1  Interner Raum-Temperatursensor  

Um den internen Temperatursensor benutzen zu können, muss dieser in der Regel zuerst kalibriert werden. Hierzu benötigst du ein Thermometer, welches dir die Referenztemperatur liefert.  

Die Werte können in der Tasmota-Console mit AdcParam<x> justiert werden. Folgende Einstellungen konnten bisher brauchbare Ergebnisse liefern (ggfs. weiter anpassen):  

`adcparam 2,14600,10000,3950`  

oder  

`adcparam 2,15880,10000,3950`  

> siehe auch: https://tasmota.github.io/docs/ADC/  

***  

### 2.2  Interner ESP-Temperatursensor  

Der interne ESP-Temperatursensor war bis zur Tasmota Version < 12.2.0 noch per "default" angeschaltet.  

Um diese Temperatur mit den Sensordaten zu übertragen ist jetzt eine zusätzliche Konfiguration über die Tasmota-Console erforderlich:  

`setOption146 1`  

***  


