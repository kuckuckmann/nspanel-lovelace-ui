# NSPanel Tasmota Configs

# Index
**1.)** Hardware-Buttons  
**2.)** Rules  
**3.)** Multipress Mode  
**4.)** Switchmode


## 1. Hardware-Buttons

***

## 2. Rules

***

## 3. Multipress Mode

***

## 4. Switchmode

Um die Tasmota-Switchmode (momentary switch) Funktion für die Hardware-Buttons zu nutzen müssen die Button GPIO's in Tasmota zu Switch GPIO's umkonfiguriert werden:  
![image](https://user-images.githubusercontent.com/102996011/189382319-3830b438-2e4c-40c8-930e-46177d48b146.png)  

![image](https://user-images.githubusercontent.com/102996011/189382449-5d870f37-10b8-4f59-8ea1-8a38aa8d3a0b.png)  

Für einen ganz normalen Taster (gedrückt an/loslassen aus) wären optional folgende Einstellungen notwendig  

Alternativ folgendes Template aktivieren  
`{"NAME":"NSPanel_1","GPIO":[0,0,0,0,3872,0,0,0,0,0,160,0,0,0,0,225,0,480,224,1,0,0,0,161,0,0,0,0,0,0,0,0,0,0,4736,0],"FLAG":0,"BASE":1}`  

> `switchmode1 2`  
> `switchmode2 2`

***

