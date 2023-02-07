# Das ioBroker Skript auch ohne NSPanel ausprobieren

## Einleitung

Wenn man sein NSPanel schon fest verbaut hat und dann z.B. eine neue Seite konfigurieren muss, dann ist man ständig zwischen seinem Rechner und dem Panel am hin-und-her laufen um die Funktionalität zu testen. Die Bewegung als solches mag gut tun, ist aber hier der Effizienz in der Entwicklung der neuen Seite nicht zuträglich.
Auch nach einem Update des ioBroker Skripts kann man mit dieser Lösung einfach im Emulator testen, ob noch alles klappt, bevor man das Skript in seiner Live-Instanz aktualisiert.
Und Last but not least ist diese Möglichkeit auch für all diejenigen Interessant, die noch kein NSPanel haben, aber selbiges vor dem Kauf einmal testen möchten.

![image](https://user-images.githubusercontent.com/102996011/217221513-8fd9bb71-f54f-43d9-bdc1-48df30918387.png)  


## Voraussetzungen

Ihr braucht einen PC (ich habe es mit Windows 11 bei mir aktuell vertestet), einen ESP32 mit Tasmota, den Nextion Editor und eine ioBroker-Installation.

## Vorbereitungen

Nachdem Euer ESP32 angekommen ist, müsst Ihr diesen via USB an den PC anschließen. Ich musste mir für meinen ESP32 noch den passenden Treiber installieren (CP210x_Universal_Windows_Driver). Nachdem ich den Treiber installiert hatte, taucht im Gerätemanager unter Anschlüsse bei mir ein _Silicon Labs CP210x USB to UART Bridge_ an _COM3_ auf.
Nun installieren wir Tasmota über den Webinstaller auf dem ESP: Dazu ruft Ihr die Seite https://tasmota.github.io/install/ im Browser auf. Lt. Dokumentation von Tasmota müsst Ihr hierfür den Browser Edge oder Chrome nehmen. Dort wählt Ihr rechts im Auswahlmenü _ESP32_ und links im Auswahlmenü _Tasmota DE_. Anschließend klickt Ihr auf _CONNECT_ und wählt den COM-Port von Eurer CP210x USB to UART Bridge aus.
Nachdem die Verbindung hergestellt wurde, installiert ihr Tasmota auf dem EPS32. War die Installation erfolgreich, könnt Ihr im nächsten Schritt Eure WLAN-Daten eintragen.
Nachdem die WLAN-Daten hinterlegt sind, gelangt Ihr mit einem weiteren Klick direkt auf die Tasmota Seite vom Gerät. War dies Erfolgreich, schließen wir die Tasmota Installation Seite und trennen kurz die USB Verbindung.
Nachdem nun der ESP wieder erreichbar ist, prüft man in den Einstellungen unter _Gerät konfigurieren_, ob RX und TX auf none stehen.

Anschließend installiert man den Berry-Treiber und konfiguriert MQTT (nach der Anleitung hier im Wiki: https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---Basisinstallation#3-berry-treiber-installieren).

**ACHTUNG:** Nicht den Berry Treiber hier aus dem Wiki nehmen, sondern hier aus dem nachfolgenden Forenbeitrag von joBr99: https://forum.iobroker.net/topic/50888/sonoff-nspanel/451 (Dort steht diese Anleitung auch nochmals verkürzt).

Nachdem die autoexec.be erstellt wurde, den ESP32 einmal rebooten und nun MQTT einrichten. Ich habe hierbei anstelle der Nummerierung der NSPanels DEV geschrieben, also NSPanel_DEV als client und topic.

Den Schritt 5 der Anleitung (TFT-Flashen) benötigt man nicht. Ab hier geht es dann mit Schritt 6 der normalen Anleitung weiter.

Ich habe bei mir, um das ganze voneinander zu trennen, eine zweite JavaScript Instanz im ioBroker installiert. In diese zweite Instanz habe ich bei mir das NSPanel.TS Skript hinterlegt (Mit DEV im Dateinamen, damit man es sofort als DEV-Skript erkennt). In dem DEV-Skript müssen nun noch die folgenden Änderungen vorgenommen werden:

`const NSPanel_Path = '0_userdata.0.NSPanel.1.';` muss genändert werden. Ich habe bei mir die 1 durch DEV ersetzt. Weiterhin im Codeblock `export const config: Config` die folgenden Werte korrekt eintragen:

_panelRecvTopic_, _panelSendTopic_, _mrIcon1ScreensaverEntity_, _mrIcon2ScreensaverEntity_ (bei den beiden letzten entweder 'none' als Entity eintragen oder die POWER1 und POWER2 Endpunkte des echten NSPanels.

Das Skript nun speichern aber noch nicht ausführen.

Zunächst braucht man noch den Nextion Editor: https://nextion.tech/nextion-editor/ sowie die HMI-Datei hier aus dem Repository (liegt im Verzeichnis HMI). Nachdem der Editor installiert ist, diesen Starten und die Datei nspanel.hmi im Nextion Editor öffnen. Anschließend im Editor oben auf Debug klicken. Es öffnet sich ein neues Fenster. Dort unten links von _Keyboard Input_ auf _User MCU Input_ umstellen, den COM-Port des ESP auswählen und die Baud-Rate auf 115200 stellen. Mit Start verbindet man sich nun zum ESP.

Nun kann das DEV-Skript im ioBroker ausgeführt werden. Hat man alles richtig gemacht, erscheint nach kurzer Zeit die erste Seite im Nextion Editor.

Abschließend sollte man der noch den Kontrast für das DEV-Panel erhöhen:
Dazu im ioBroker den DP 0_userdata.0.NSPanel.DEV.NSPanel_Dimmode_brightnessDay auf 80 stellen (und ggf auch die brightnessNight). Ansonsten ist der Screensaver im Editor zu dunkel.

Nun hab Ihr ein vollständig klickbares, emuliertes NSPanel, in welchem Ihr eure neuen Seiten ohne Zugriff auf Euer echtes Panel bequem entwerfen und vertesten könnt. Wenn man dann mit seinen Änderungen zufrieden ist, kann man die Änderungen vom Skript nun in das Produktionsskript eintragen!

Viel Spaß mit dem Emulator!