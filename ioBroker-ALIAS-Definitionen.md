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
* Sonoff-Adapter: **.power** (aus Tasmota übertragen)
* MQTT-Adapter: **.power** (aus Tasmota übertragen) 
* Shelly-Adapter: **.switch**
* KNX-Adapter: **.switch**
* Deconz-Adapter: **.on**
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
### Dimmer (channel dimmer)

Der Alias "Dimmer" hat 2 relevante Eigenschaften.   
* Schalter (an/aus) über Adapter-Datenpunkte on, switch, power, etc.  
* Helligkeit (dunkel/hell) über Adapter-Datenpunkte level, brightness, bri, etc.  

**Im Beispiel ist eine dimmbare Deckenbeleuchtung über den DeConz-Adapter (Zigbee)**  

Der Schalter im DeConz wird über den Datenpunkt "on" (true/false), d.h Datentyp "boolean" gesteuert.
Die Helligkeit wird im Deconz-Adapter über "level" 0-100 oder "bri" 0-255 gesteuert. Für uns bietet sich also der Datenpunkt **level** an, da dieser bereits die Helligkeit in % von 0% bis 100% beinhaltet. Jedoch könnten wir auch mit dem Datentyp **bri** arbeiten und im TypeScript die Umrechnung von 255 (absolut) auf 100 (%) parametrieren.  

Der Dimmer kann in einer cardEntities oder in einer cardGrid platziert werden. (Nachfolgende Abb. cardEntities):   
![image](https://user-images.githubusercontent.com/102996011/189492309-e678414a-21b9-417f-b6a5-bdd769db7fc4.png)  
 
Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ Dimmer an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des DeConz-Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/189492261-48519b87-3210-4bb9-a039-489e57bc21de.png)  

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung.
![image](https://user-images.githubusercontent.com/102996011/189492446-1c530407-cac3-4f3e-ab06-258dcd88629c.png)  

Der Schaltzustand (Lampe an/aus) kann direkt aus der cardEntities oder carGrid erfolgen. Für die Regelung der Helligkeit hat der Alias-Gerätetyp "Dimmer" bereits eine Unterseite (siehe nachfolgende Abb.). Diese kann über einen Klick auf den Dimmer-Bezeichner (in diesem Fall "Deckenbeleuchtung") aufgeschaltet werden:  

![image](https://user-images.githubusercontent.com/102996011/189493396-b94fdccb-61ee-4c1d-97d2-8732e7c1d9ae.png)  

Das zugehörige PageItem im TypeScript:  
![image](https://user-images.githubusercontent.com/102996011/189493609-51ebffec-c119-4a58-bb85-bdf253383548.png)  
Mit dem Parameter "name" legen wir den Anzeigenamen fest.  
Mit dem Parameter "interpolateColor" (optional), soll die abgebildete Lampe (Icon) den An/Aus und die Helligkeit emulieren.  
  
Es können noch weitere Parameter übergeben werden:
* icon  
* onColor  
* offColor  
* minValueBrightness (Default = 0)
* maxValueBrightness (Default = 100; im Beispiel mit dem Datenpunkt "bri" also 255)

***

### Farbtemperatur (channel ct)  

Der Alias "Farbtemperatur" hat 3 relevante Eigenschaften.   
* Schalter (an/aus) über Adapter-Datenpunkte on, switch, power, etc.  
* Helligkeit (dunkel/hell) über Adapter-Datenpunkte level, brightness, bri, etc. 
* Farbtemperatur (K = Kelvin) über Adapter-Datenpunkte ct, colortemp, etc.  

Der Alias "Farbtemperatur" kann in einer cardEntities oder in einer cardGrid platziert werden. (Nachfolgende Abb. cardEntities):
![image](https://user-images.githubusercontent.com/102996011/189497667-0362a360-ef6b-4d7a-98ea-de55e6b42535.png)  

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **Farbtemperatur** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  

![image](https://user-images.githubusercontent.com/102996011/189498366-2d0d8e4c-e161-4f57-a084-c2377da001c3.png)  

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung.
![image](https://user-images.githubusercontent.com/102996011/189498497-989cc054-812a-4c58-8995-5c4ccf39f4b9.png)  

Der Schaltzustand (Lampe an/aus) kann direkt aus der cardEntities oder carGrid erfolgen. Für die Regelung der Helligkeit und CT hat der Alias-Gerätetyp "Farbtemperatur" bereits eine Unterseite (siehe nachfolgende Abb.). Diese kann über einen Klick auf den Bezeichner (in diesem Fall "Farbtemperatur") aufgeschaltet werden: 
![image](https://user-images.githubusercontent.com/102996011/189497755-b3bbc89a-8b36-451e-add2-ba6c12e94330.png)  

Das zugehörige PageItem im TypeScript:  
![image](https://user-images.githubusercontent.com/102996011/189498614-4aa1dc89-cf5e-48f5-a0be-f2b0e11cc8d0.png)  
Mit dem Parameter "name" legen wir den Anzeigenamen fest.  
Mit dem Parameter "interpolateColor" (optional), soll die abgebildete Lampe (Icon) den An/Aus und die Helligkeit emulieren.  
  
Es können noch weitere Parameter übergeben werden:
* icon  
* onColor  
* offColor  
* minValueBrightness (Default = 0)
* maxValueBrightness (Default = 100; im Beispiel mit dem Datenpunkt "bri" also 255)
* minValueColorTemp  (z.B. 500  - in Abhängigkeit des jeweiligen Adapters) 
* maxValueColorTemp: (z.B. 6500 - in Abhängigkeit des jeweiligen Adapters)

> Hinweis: Es kann auch der HUE-CT verwendet werden

***

### Fenster (channel window)

Der Alias "Fenster" hat 1 relevante Eigenschaft.   
* Zustand (offen/geschlossen) über Adapter-Datenpunkte open, etc.  

Darstellung in einer "cardGrid"  
![image](https://user-images.githubusercontent.com/102996011/189404690-69e61c60-88f3-4ea7-b5ad-0c423094eb11.png)
Darstellung in einer "cardEntities"  
![image](https://user-images.githubusercontent.com/102996011/189403796-ab118db1-fb38-49ae-bbdf-199717e77bbe.png)

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **Fenster** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt den Datenpunkt des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/189498976-965bae49-3643-4c23-820f-e1540b3b28a2.png)  
Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:  
![image](https://user-images.githubusercontent.com/102996011/189499063-f0fa5d5a-4302-46ec-802c-0c99626f908a.png)  

Das zugehörige PageItem im TypeScript:  
![image](https://user-images.githubusercontent.com/102996011/189498910-6d64cfdd-faa6-448c-9542-43410866dfa2.png)

***

### Feuchtigkeit (channel humidity)

Der Alias "Feuchtigkeit" hat 1 relevante Eigenschaft.   
* Zustand (Sensorwert) 

![image](https://user-images.githubusercontent.com/102996011/189403392-4ba6c9b6-5d33-4bdb-abfb-36c85e99eebf.png)

**Im Beispiel ist ein Homatic IP Sensor über den hmip-Adapter (Funk).** Es kann aber auch jeder andere Sensor (z.B. Zigbee oder WLAN) oder ein Datenpunkt aus einem Wetter-Adapter verwendet werden.  

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **Feuchtigkeit** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/189499807-aba39d1c-5a83-4e50-ba04-8cc972f76208.png)  

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:  

![image](https://user-images.githubusercontent.com/102996011/189499784-2b3dc3c5-3196-4b8e-93d0-cf1c57452f8a.png)  

Das zugehörige PageItem im TypeScript:  
![image](https://user-images.githubusercontent.com/102996011/189499885-ace4b001-0c9c-4d0d-9667-d7c808d1f8fc.png)

Folgende Parameter können verwendet werden:  
* name: legt den Anzeigenamen fest
* icon: Symbol
* unit: Einheit der Luftfeuchte
* onColor: Farbe des Icons

`<PageItem>{ id: "alias.0.NSPanel_1.TestFeuchtigkeit", name: "Luftfeuchte außen", icon: "water-percent", unit: "%H", onColor: White}`  

> **Hinweis**  
> **Alternativ kann auch der Alias-Typ "Info" verwendet werden.**  

***

### HUE-Licht (channel hue)

Der Alias Geräte-Typ HUE-Licht funktioniert mit und ohne dem Wert ".HUE". Wenn der Datenpunkt HUE nicht vorhanden ist, wird durch das TypeScript automatisch eine CT (ColorTemperature-Steuerung emuliert)  

![image](https://user-images.githubusercontent.com/102996011/189403062-a5fed1f9-8c6b-49b5-ad94-82c344603d5a.png)

Zunächst legen wir analog "[Schritt 1](https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker-ALIAS-Definitionen#alias-erzeugen---schritt-1---tab-allgemein)" (Tab Allgemein) einen Alias vom Typ **HUE-Licht** an. Im "Schritt 2" (Tab Zustände) weisen wir jetzt die Datenpunkte des Adapters zu:  
![image](https://user-images.githubusercontent.com/102996011/189500932-7d2f043a-f279-4525-ba98-3fe11cece1d5.png)

Jetzt speicherst du den neu erstellten Alias. Unter ioBroker Objekte (Verzeichnisbaum alias.0.NSPanel.X...) siehst du jetzt folgende Darstellung:  
![image](https://user-images.githubusercontent.com/102996011/189500907-e527fc9b-b8d2-49d0-bc89-ba729cfe65b4.png)


![image](https://user-images.githubusercontent.com/102996011/189402777-0937bfbf-6695-4768-9123-d61546175726.png)
![image](https://user-images.githubusercontent.com/102996011/189402911-7a9edf50-bb22-4211-9117-5b55e4ecba56.png)


***

### Info
![image](https://user-images.githubusercontent.com/102996011/189403645-a9511303-c873-469c-9e92-136809162728.png)
![image](https://user-images.githubusercontent.com/102996011/189404981-bbd544b0-1019-48d7-a5eb-8f38616bb8b4.png)

***

### Jalousien
![image](https://user-images.githubusercontent.com/102996011/189403904-914ff6ad-a7df-4859-a523-ff5ec02f2381.png)  
  
Bereits in der FAQ & Anleitung beschrieben: https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---FAQ-&-Anleitungen#8-rolladen--jalousie--shutter

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

***
