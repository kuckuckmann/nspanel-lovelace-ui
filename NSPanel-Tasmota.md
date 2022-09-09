# NSPanel Tasmota Configs

# Index
**1.)** Hardware-Buttons  
**1.1)**    Rules  
**1.2)**    Multipress Mode  
**1.3)**    Switchmode


## 1. Hardware-Buttons

***

## 1.1  Rules

***

## 1.2  Multipress Mode

***

## 1.3  Switchmode

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

> `switchmode1 2`  
> `switchmode2 2`

***

