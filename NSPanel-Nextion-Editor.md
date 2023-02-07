# Das ioBroker Skript auch ohne NSPanel ausprobieren

## Einleitung

Wenn man sein NSPanel schon fest verbaut hat und dann z.B. eine neue Seite konfigurieren muss, dann ist man ständig zwischen seinem Rechner und dem Panel am hin-und-her laufen um die Funktionalität zu testen. Die Bewegung als solches mag gut tun, ist aber hier der Effizienz in der Entwicklung der neuen Seite nicht zuträglich.
Auch nach einem Update des ioBroker Skripts kann man mit dieser Lösung einfach im Emulator testen, ob noch alles klappt, bevor man das Skript in seiner Live-Instanz aktualisiert.
Und Last but not least ist diese Möglichkeit auch für all diejenigen Interessant, die noch kein NSPanel haben, aber selbiges vor dem Kauf einmal testen möchten.

![image](https://user-images.githubusercontent.com/102996011/217221513-8fd9bb71-f54f-43d9-bdc1-48df30918387.png)  


## Voraussetzungen

Ihr braucht:  
* einen PC (ich habe es mit Windows 11 bei mir aktuell vertestet)  
* einen ESP32 mit Tasmota32  
* den Nextion Editor  
* und eine ioBroker-Installation.  

![image](https://user-images.githubusercontent.com/102996011/217230894-09253765-c5d7-47a2-9040-19fe00c6b061.png)  

> Der ESP32 bleibt mit einem Datenkabel mit dem USB-Port des PC's verbunden.


## Vorbereitungen

Nachdem Euer ESP32 angekommen ist, müsst Ihr diesen via USB an den PC anschließen. Ich musste mir für meinen ESP32 noch den passenden Treiber installieren (CP210x_Universal_Windows_Driver). Nachdem ich den Treiber installiert hatte, taucht im Gerätemanager unter Anschlüsse bei mir ein _Silicon Labs CP210x USB to UART Bridge_ an _COM3_ auf.  

Nun installieren wir Tasmota über den Webinstaller auf dem ESP: Dazu ruft Ihr die Seite https://tasmota.github.io/install/ im Browser auf. Lt. Dokumentation von Tasmota müsst Ihr hierfür den Browser Edge oder Chrome nehmen. Dort wählt Ihr rechts im Auswahlmenü _ESP32_ und links im Auswahlmenü _Tasmota DE_. Anschließend klickt Ihr auf _CONNECT_ und wählt den COM-Port von Eurer CP210x USB to UART Bridge aus.  

Nachdem die Verbindung hergestellt wurde, installiert ihr Tasmota auf dem EPS32. War die Installation erfolgreich, könnt Ihr im nächsten Schritt Eure WLAN-Daten eintragen.  
Nachdem die WLAN-Daten hinterlegt sind, gelangt Ihr mit einem weiteren Klick direkt auf die Tasmota Seite vom Gerät. War dies Erfolgreich, schließen wir die Tasmota Installation Seite und trennen kurz die USB Verbindung.  

Nachdem nun der ESP wieder erreichbar ist, prüft man in den Einstellungen unter _Gerät konfigurieren_, ob RX (GPIO3) und TX (GPIO1) auf none stehen.

![image](https://user-images.githubusercontent.com/102996011/217224220-78b859d6-a4ca-4217-ba15-c1ab6b0d8f23.png)  

Anschließend installiert man den Berry-Treiber und konfiguriert MQTT (nach der Anleitung hier im Wiki: https://github.com/joBr99/nspanel-lovelace-ui/wiki/ioBroker---Basisinstallation#3-berry-treiber-installieren).  

## Berry-Driver für Emulation  

**ACHTUNG:** Nicht den Berry Treiber hier aus dem Wiki nehmen, sondern hier aus dem nachfolgenden Code-Block  

```
# Nextion Serial Protocol driver by joBr99 + nextion upload protocol 1.2 (the fast one yay) implementation using http range and tcpclient
# based on;
# Sonoff NSPanel Tasmota driver v0.47 | code by blakadder and s-hadinger
 
class Nextion : Driver
 
    var ser
	var flash_size
	var flash_mode
	var flash_skip
	var flash_current_byte
	var tftd
	var progress_percentage_last
	static header = bytes('55BB')
 
    def init()
        log("NSP: Initializing Driver")
        self.ser = serial(3, 1, 115200, serial.SERIAL_8N1)
        self.flash_mode = 0
		self.flash_skip = false
		tasmota.add_driver(self)
    end
	
    def crc16(data, poly)
      if !poly  poly = 0xA001 end
      # CRC-16 MODBUS HASHING ALGORITHM
      var crc = 0xFFFF
      for i:0..size(data)-1
        crc = crc ^ data[i]
        for j:0..7
          if crc & 1
            crc = (crc >> 1) ^ poly
          else
            crc = crc >> 1
          end
        end
      end
      return crc
    end
	
    def split_55(b)
      var ret = []
      var s = size(b)   
      var i = s-2   # start from last
      while i > 0
        if b[i] == 0x55 && b[i+1] == 0xBB           
          ret.push(b[i..s-1]) # push last msg to list
          b = b[(0..i-1)]   # write the rest back to b
        end
        i -= 1
      end
      ret.push(b)
      return ret
    end
 
	# encode using custom protocol 55 BB [payload length] [payload] [crc] [crc]
    def encode(payload)
      var b = bytes()
      b += self.header
      b.add(size(payload), 2)   # add size as 1 byte
      b += bytes().fromstring(payload)
      var msg_crc = self.crc16(b)
      b.add(msg_crc, 2)       # crc 2 bytes, little endian
      return b
    end
	
	# send a nextion payload
	def encodenx(payload)
		var b = bytes().fromstring(payload)
		b += bytes('FFFFFF')
		return b
	end
	
	def sendnx(payload)
		var payload_bin = self.encodenx(payload)
		self.ser.write(payload_bin)
		 print("NSP: Sent =", payload_bin)
		log("NSP: Nextion command sent = " + str(payload_bin), 3)
	end
  
    def send(payload)
        var payload_bin = self.encode(payload)
        if self.flash_mode==1
            log("NSP: skipped command becuase still flashing", 3)
        else 
            self.ser.write(payload_bin)
            log("NSP: payload sent = " + str(payload_bin), 3)
        end
    end
		
	def every_100ms()
        import string
        if self.ser.available() > 0
            var msg = self.ser.read()
            if size(msg) > 0
                print("NSP: Received Raw =", msg)
                if self.flash_mode==1
                    log("no flashing in this version")
                else
					# Recive messages using custom protocol 55 BB [payload length] [payload length] [payload] [crc] [crc]
					if msg[0..1] == self.header
						var lst = self.split_55(msg)
						for i:0..size(lst)-1
							msg = lst[i]
							#var j = msg[2]+2
							var j = size(msg) - 3
							msg = msg[4..j]
							if size(msg) > 2
								var jm = string.format("{\"CustomRecv\":\"%s\"}",msg.asstring())
								tasmota.publish_result(jm, "RESULT")
							end
						end
					elif msg == bytes('000000FFFFFF88FFFFFF')
						log("NSP: Screen Initialized")
					else
                        var jm = string.format("{\"nextion\":\"%s\"}",str(msg[0..-4]))
						tasmota.publish_result(jm, "RESULT")
					end       			
                end
            end
        end
    end
end
 
var nextion = Nextion()

def get_current_version(cmd, idx, payload, payload_json)
    import string
    var version_of_this_script = 8
    var jm = string.format("{\"nlui_driver_version\":\"%s\"}", version_of_this_script)
    tasmota.publish_result(jm, "RESULT")
end

tasmota.add_cmd('GetDriverVersion', get_current_version)
 
def send_cmd(cmd, idx, payload, payload_json)
    nextion.sendnx(payload)
    tasmota.resp_cmnd_done()
end
 
tasmota.add_cmd('Nextion', send_cmd)
 
def send_cmd2(cmd, idx, payload, payload_json)
    nextion.send(payload)
    tasmota.resp_cmnd_done()
end
 
tasmota.add_cmd('CustomSend', send_cmd2)
```  

Nachdem die autoexec.be erstellt wurde, den ESP32 einmal rebooten und nun MQTT einrichten. Ich habe hierbei anstelle der Nummerierung der NSPanels DEV geschrieben, also NSPanel_DEV als client und topic.

> **Den Schritt 5 der Anleitung (TFT-Flashen mit FlashNextion...) benötigt man nicht, da der ESP32 nicht mit einem Nextion-Display ausgestattet ist. Ab hier geht es dann mit Schritt 6 der normalen Anleitung weiter.**

Ich habe bei mir, um das ganze voneinander zu trennen, eine zweite JavaScript Instanz im ioBroker installiert. In diese zweite Instanz habe ich bei mir das NSPanel.TS Skript hinterlegt (Mit DEV im Dateinamen, damit man es sofort als DEV-Skript erkennt). In dem DEV-Skript müssen nun noch die folgenden Änderungen vorgenommen werden:

`const NSPanel_Path = '0_userdata.0.NSPanel.1.';` muss genändert werden. Ich habe bei mir die 1 durch DEV ersetzt. Weiterhin im Codeblock `export const config: Config` die folgenden Werte korrekt eintragen:

_panelRecvTopic_, _panelSendTopic_, _mrIcon1ScreensaverEntity_, _mrIcon2ScreensaverEntity_ (bei den beiden letzten entweder 'none' als Entity eintragen oder die POWER1 und POWER2 Endpunkte des echten NSPanels.

Das Skript nun speichern aber noch nicht ausführen.

## Installation des Nextion Editor

Zunächst braucht man noch den Nextion Editor: 
> ~~https://nextion.tech/nextion-editor/~~  (Nextion-Editor-Version aktuell defekt)  
>  
> https://nextion.tech/download/nextion-setup-v1-63-3.exe oder https://nextion.tech/download/nextion-setup-v1-63-3.zip  
> **Bitte ältere Version des Nextion-Editor 1.63.3 benutzen und keine Updates durchführen!**

sowie die HMI-Datei hier aus dem Repository (liegt im Verzeichnis HMI). Nachdem der Editor installiert ist, diesen Starten und die Datei nspanel.hmi im Nextion Editor öffnen. Anschließend im Editor oben auf Debug klicken. Es öffnet sich ein neues Fenster. Dort unten links von _Keyboard Input_ auf _User MCU Input_ umstellen, den COM-Port des ESP auswählen und die Baud-Rate auf 115200 stellen. Mit Start verbindet man sich nun zum ESP.

![image](https://user-images.githubusercontent.com/102996011/217225521-64546ca6-2b14-482d-b120-a9d5b5b93208.png)  

Nun kann das DEV-Skript im ioBroker ausgeführt werden. Hat man alles richtig gemacht, erscheint nach kurzer Zeit die erste Seite im Nextion Editor.

Abschließend sollte man der noch den Kontrast für das DEV-Panel erhöhen:
Dazu im ioBroker den DP 0_userdata.0.NSPanel.DEV.NSPanel_Dimmode_brightnessDay auf 80 stellen (und ggf auch die brightnessNight). Ansonsten ist der Screensaver im Editor zu dunkel.

Nun hab Ihr ein vollständig klickbares, emuliertes NSPanel, in welchem Ihr eure neuen Seiten ohne Zugriff auf Euer echtes Panel bequem entwerfen und vertesten könnt. Wenn man dann mit seinen Änderungen zufrieden ist, kann man die Änderungen vom Skript nun in das Produktionsskript eintragen!

## Hinweise

**Noch ein paar Hinweise**:  
* Die ESP32 Temperatur mit setOptions146 1 einschalten.  
  
* Im Gengensatz zum "echten" NSPanel hat der Emulator-ESP32 keinen eingebauten Temperatursensor und auch keine eingebauten Buttons/Relais. Es kann somit keine Daten hierfür in die Datenpunkte transportieren. Um Fehler zu vermeiden, sollte im Datenpunkt:
`0_userdate.0.NSPanel.Dev.Sensor.ANALOG.Temperature`
ein Temperaturwert für die Raumtemperatur (z.B. 21) eingetragen werden.

* Ebenfalls sind die Werte für die Status Icons im Screensaver nicht vorhanden. Da der Emulator in der Regel ein bereits  vorhandenes physisches NSPanel emuliert, können die MQTT-Pfade für die Relais-Icons auch auf das physische NSPanel verweisen.

**Viel Spaß mit dem Emulator!**