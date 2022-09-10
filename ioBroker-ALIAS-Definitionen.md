Ziel dieser Seite ist, jeden Alias-Typen zu  beschreiben

#Einleitung: 

## Alias-Hilfsmittel
**Welche Hilfsmittel werden zur Erstellung eines Alias benötigt?:**

Der "Geräte verwalten"-Adapter für die meisten Alias-Typen:  
![image](https://user-images.githubusercontent.com/102996011/189475521-07d78146-e49d-406a-95bc-804b3302caa2.png)

Der "Alias-Manager"-Adapter für spezielle Alias-Typen, wie dem Alias "Media":  
![image](https://user-images.githubusercontent.com/102996011/189475471-26f0ed04-4715-4eed-8924-cf6d7be879a9.png)  

**Was sind Aliase:**  
Aliase (Pseudonyme) sind die virtuellen Zustandsobjekte, die mit realen Zuständen (Datenpunkten) verknüpft sind.  

**Warum benötige ich im TS-Skript überhaupt Aliase und keine Datenpunkte?**
Das TS-Script für das Sonoff NSPanel ist so aufgebaut, dass eigentlich jeder Adapter zur Steuerung benutzt werden kann. Hierbei haben die Entwickler von Adaptern für gleiche Funktionen unterschiedliche Namen verwendet:

Beispiel: 
* Sonoff-Adapter: **Power** (aus Tasmota übertragen)
* MQTT-Adapter: **Power** (aus Tasmota übertragen) 
* Shelly-Adapter: **Switch**
* KNX-Adapter: **Switch**
* etc.
In speziellen Licht-Adaptern wird das noch deutlicher

Der Alias benötigt also anstatt * .Power oder * .Switch nur einen **.SET**, damit der Zustand des Sensors oder Aktors unabhängig von installierten Adapter geschaltet werden kann.

# Index

## Alarm - cardAlarm

siehe auch das Beispiel zur vollständigen Integration der cardAlarm in den ioBroker:  
https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#2-alarm-page
   
![image](https://user-images.githubusercontent.com/102996011/189404542-81735372-7bbd-4c1a-8cad-73d1a62bd735.png)

***
## Dimmer
***
## Farbtemperatur
***
## Fenster 
![image](https://user-images.githubusercontent.com/102996011/189404690-69e61c60-88f3-4ea7-b5ad-0c423094eb11.png)

![image](https://user-images.githubusercontent.com/102996011/189403796-ab118db1-fb38-49ae-bbdf-199717e77bbe.png)

***
## Feuchtigkeit
![image](https://user-images.githubusercontent.com/102996011/189403392-4ba6c9b6-5d33-4bdb-abfb-36c85e99eebf.png)
***
## HUE-Licht
![image](https://user-images.githubusercontent.com/102996011/189403062-a5fed1f9-8c6b-49b5-ad94-82c344603d5a.png)
![image](https://user-images.githubusercontent.com/102996011/189402777-0937bfbf-6695-4768-9123-d61546175726.png)
![image](https://user-images.githubusercontent.com/102996011/189402911-7a9edf50-bb22-4211-9117-5b55e4ecba56.png)

***
## Info
![image](https://user-images.githubusercontent.com/102996011/189403645-a9511303-c873-469c-9e92-136809162728.png)
![image](https://user-images.githubusercontent.com/102996011/189404981-bbd544b0-1019-48d7-a5eb-8f38616bb8b4.png)

***
## Jalousien
![image](https://user-images.githubusercontent.com/102996011/189403904-914ff6ad-a7df-4859-a523-ff5ec02f2381.png)

***
## Klimaanlage - cardThermo
![image](https://user-images.githubusercontent.com/102996011/189401952-86b47d90-69f2-4229-909c-8d4c2ee84d20.png)
***
## Lautstärke
![image](https://user-images.githubusercontent.com/102996011/189403220-a2540eb2-4b47-4947-9258-a7687403710c.png)

***
## Lautstärke-Gruppe
***
## Licht
***
## Medien - cardMedia
![image](https://user-images.githubusercontent.com/102996011/189404434-6a5da814-fd1e-4ca7-8f42-4e03461b8675.png)

***
## RGB-Licht 
***
## RGB-Licht-einzeln
***
## Schieberegler
***
## Steckdose
***
## Taste
![image](https://user-images.githubusercontent.com/102996011/189404781-7fe9c2b0-e81d-446f-9aab-50865cc39a40.png)

***
## Tastensensor
***
## Temperatur
![image](https://user-images.githubusercontent.com/102996011/189403527-4a94e690-9a5d-4121-8dcb-5636951a7df6.png)
***
## Thermostat - cardThermo
![image](https://user-images.githubusercontent.com/102996011/189402503-c25994b5-d16d-46f7-b34b-0620122f07fc.png)
***
## Tür
![image](https://user-images.githubusercontent.com/102996011/189403985-7eed8829-ea85-4785-88f9-610edaeb9485.png)

***
## Verschluss
![image](https://user-images.githubusercontent.com/102996011/189404088-9a2cd3ea-5c43-4c3f-9bd9-e58eac2e6fd6.png)
***
## Warnung
![image](https://user-images.githubusercontent.com/102996011/189405183-22b51c18-3b92-44e3-bd84-c23359f2783d.png)

***
## Wettervorhersage
![image](https://user-images.githubusercontent.com/102996011/189405373-8ea44dd3-a073-40e8-8379-faab8a836d12.png)
