Ziel dieser Seite ist, jeden Alias-Typen zu  beschreiben

# Einleitung: 

## Alias-Hilfsmittel
**Welche Hilfsmittel werden zur Erstellung eines Alias benötigt?:**  

Der "Geräte verwalten"-Adapter für die meisten Alias-Typen:  
![image](https://user-images.githubusercontent.com/102996011/189475521-07d78146-e49d-406a-95bc-804b3302caa2.png)

Der "Alias-Manager"-Adapter für spezielle Alias-Typen, wie dem Alias "Media":  
![image](https://user-images.githubusercontent.com/102996011/189475471-26f0ed04-4715-4eed-8924-cf6d7be879a9.png)  

**Ich habe die zwei Adapter installiert. Wie bekomme ich die in das ioBroker-Menü:**  
Über das Stift-Symbol im ioBroker-Hauptmenü lassen sich die Adapter individuell für jeden Benutzer ein- oder ausschalten.
![image](https://user-images.githubusercontent.com/102996011/189476871-85b18ead-f032-4bd0-b8a4-310742b778fc.png)
![image](https://user-images.githubusercontent.com/102996011/189476923-59ef3397-543f-43ef-9ab9-e839b9eba9cb.png)

Es sollte ein Haken bei Geräte und Alias-Manager gesetzt sein.

**Was sind Aliase:**  
Aliase (Pseudonyme) sind die virtuellen Zustandsobjekte, die mit realen Zuständen (Datenpunkten) verknüpft sind.  

**Warum benötige ich im TS-Skript überhaupt Aliase und keine Datenpunkte?**  
Das TS-Script für das Sonoff NSPanel ist so aufgebaut, dass eigentlich jeder Adapter zur Steuerung benutzt werden kann. Hierbei haben die Entwickler von Adaptern für gleiche Funktionen unterschiedliche Namen verwendet:

Beispiel: 
* Sonoff-Adapter: **Power** (aus Tasmota übertragen)
* MQTT-Adapter: **Power** (aus Tasmota übertragen) 
* Shelly-Adapter: **Switch**
* KNX-Adapter: **Switch**
* Deconz-Adapter: **On**
* etc.  

Also immer der Wunsch, einen Zustand eines Aktors mit true/false zu verändern.  

> Innerhalb der Licht-Adapter wird das später noch deutlicher

Der Alias benötigt also anstatt **.Power** oder **.Switch** oder **.On** immer nur ein **.SET**, damit der Zustand des Schalt-Aktor's unabhängig vom installierten Adapter geschaltet werden kann. In diesem Fall meldet der im Skript eingebundene Alias ein true oder false in den Alias-Datenpunkt .SET und reicht den Zustandswert an den zugewiesenen spezifischen Adapter-Datenpunkt (ganz egal welcher Typ erwartet wird) weiter.

# "Geräte verwalten"-Adapter
Zunächst sollt man sich überlegen, welche Aliase nur für ein bestimmtes NSPanel gelten sollen oder für mehrere NSPanels oder sogar innerhalb anderer Visualisierungsarten z.B. ioBroker VIS mitverwendet werden sollen. Dann kann man die Alias Struktur entsprechend mit Ordnern und Unterordnern verfeinern. Das Bürolicht soll z.B. nur über NSPanel_1 geschaltet werden, aber nicht über NS_Panel_2. Das Wetter hingegen ist für alle NSPanel gleich.  
![image](https://user-images.githubusercontent.com/102996011/189477432-2c814d56-7c37-41c2-b371-31b06e6fe2aa.png)

## Alias erzeugen - Schritt 1 - Tab "Allgemein"
Der erste Schritt in der Alias Erstellung mit dem "Geräte verwalten"-Adapter ist fast immer der gleiche.

Es wird über die "+" Schaltfläche folgender Dialog aufgeschaltet:  
![image](https://user-images.githubusercontent.com/102996011/189480182-02d50b01-53ba-4c83-baa6-9bd5f10bc671.png)  
Jetzt gibst vergibst du einen "sprechenden Namen" für den Alias in der Zeile "Gerätename" und wählst einen der nachfolgenden "Alias-Typen" unter Gerätetyp aus (Auswahlliste wird aufgeschaltet und beinhaltet auch noch weitere Typen als im Bild gezeigt (Momentaufnahme)):     

![image](https://user-images.githubusercontent.com/102996011/189480322-0441c5b7-fc7e-4fd4-9920-72915753a802.png)  

> Achtung:  
> Nicht jeder Gerätetyp (Alias-Typ) funktioniert mit dem NSPanel, sondern nur die, die entweder im weiteren Verlauf benannt sin, oder die im Header des TypeScript definiert sind.  

Die Zeilen Funktion und Raum können ebenfalls ausgewählt werden, haben jedoch keinen Einfluss auf die Funktionalität des NSPAnel's

## Alias erzeugen - Schritt 2 - Tab "Zustände"

### Alarm - cardAlarm

siehe auch das Beispiel zur vollständigen Integration der cardAlarm in den ioBroker:  
https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#2-alarm-page
   
![image](https://user-images.githubusercontent.com/102996011/189404542-81735372-7bbd-4c1a-8cad-73d1a62bd735.png)

***
### Dimmer
Der Dimmer hat 2 Zustände. 
* Schalter (an/aus)
* Helligkeit (dunkel/hell)

Im Beispiel ist eine dimmbare Deckenbeleuchtung über den DeConz-Adapter (Zigbee)

![image](https://user-images.githubusercontent.com/102996011/189492309-e678414a-21b9-417f-b6a5-bdd769db7fc4.png)  
![image](https://user-images.githubusercontent.com/102996011/189492261-48519b87-3210-4bb9-a039-489e57bc21de.png)  

![image](https://user-images.githubusercontent.com/102996011/189492446-1c530407-cac3-4f3e-ab06-258dcd88629c.png)

***
### Farbtemperatur
***
### Fenster 
![image](https://user-images.githubusercontent.com/102996011/189404690-69e61c60-88f3-4ea7-b5ad-0c423094eb11.png)

![image](https://user-images.githubusercontent.com/102996011/189403796-ab118db1-fb38-49ae-bbdf-199717e77bbe.png)

***
### Feuchtigkeit
![image](https://user-images.githubusercontent.com/102996011/189403392-4ba6c9b6-5d33-4bdb-abfb-36c85e99eebf.png)
***
### HUE-Licht
![image](https://user-images.githubusercontent.com/102996011/189403062-a5fed1f9-8c6b-49b5-ad94-82c344603d5a.png)
![image](https://user-images.githubusercontent.com/102996011/189402777-0937bfbf-6695-4768-9123-d61546175726.png)
![image](https://user-images.githubusercontent.com/102996011/189402911-7a9edf50-bb22-4211-9117-5b55e4ecba56.png)

***
### Info
![image](https://user-images.githubusercontent.com/102996011/189403645-a9511303-c873-469c-9e92-136809162728.png)
![image](https://user-images.githubusercontent.com/102996011/189404981-bbd544b0-1019-48d7-a5eb-8f38616bb8b4.png)

***
### Jalousien
![image](https://user-images.githubusercontent.com/102996011/189403904-914ff6ad-a7df-4859-a523-ff5ec02f2381.png)

***
### Klimaanlage - cardThermo
![image](https://user-images.githubusercontent.com/102996011/189401952-86b47d90-69f2-4229-909c-8d4c2ee84d20.png)
***
### Lautstärke
![image](https://user-images.githubusercontent.com/102996011/189403220-a2540eb2-4b47-4947-9258-a7687403710c.png)

***
### Lautstärke-Gruppe
***
### Licht
***
### Medien - cardMedia
![image](https://user-images.githubusercontent.com/102996011/189404434-6a5da814-fd1e-4ca7-8f42-4e03461b8675.png)

***
### RGB-Licht 
***
### RGB-Licht-einzeln
***
### Schieberegler
***
### Steckdose
***
### Taste
![image](https://user-images.githubusercontent.com/102996011/189404781-7fe9c2b0-e81d-446f-9aab-50865cc39a40.png)

***
### Tastensensor
***
### Temperatur
![image](https://user-images.githubusercontent.com/102996011/189403527-4a94e690-9a5d-4121-8dcb-5636951a7df6.png)
***
### Thermostat - cardThermo
![image](https://user-images.githubusercontent.com/102996011/189402503-c25994b5-d16d-46f7-b34b-0620122f07fc.png)
***
### Tür
![image](https://user-images.githubusercontent.com/102996011/189403985-7eed8829-ea85-4785-88f9-610edaeb9485.png)

***
### Verschluss
![image](https://user-images.githubusercontent.com/102996011/189404088-9a2cd3ea-5c43-4c3f-9bd9-e58eac2e6fd6.png)
***
### Warnung
Dieser Alias dient nur der Einbindung des dynamischen Abfallkalenders. Dieser ist hier ausführlich beschrieben:  
https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#4-abfallkalender

![image](https://user-images.githubusercontent.com/102996011/189405183-22b51c18-3b92-44e3-bd84-c23359f2783d.png)

***
### Wettervorhersage
![image](https://user-images.githubusercontent.com/102996011/189405373-8ea44dd3-a073-40e8-8379-faab8a836d12.png)

![image](https://user-images.githubusercontent.com/102996011/189480728-116bd2fb-f23a-4158-85cc-0a9bed85024c.png)
und die Temperatur (etwas tiefer). Weitere Datenpunkte, wie z.B. Min- und Max-Temperatur können ebenfalls verknüpft werden, finden jedoch im TypeScript keine Berücksichtigung.  
![image](https://user-images.githubusercontent.com/102996011/189480739-3d10df44-c7dc-43d2-af0d-58e492579d32.png)
In diesem Fall wird die Temperatur aus einem Datenpunkt einer Wetterstation visualisiert. Es kann natürlich auch ein Datenpunkt mit der aktuellen Außentemperatur aus einem anderen Adapter daswetter.0.xxxxx, accuweather.0.xxxxx, openweathermap.0.xxxxx, etc. ausgewählt werden.

> **Achtung:**  
> **Dieser Alias muss erstellt werden, damit die 4 kleineren Icons (Weather-Forecast und/oder 4 Sensordatenpunkte) im unteren Screensaver visualisiert werden können.**  
