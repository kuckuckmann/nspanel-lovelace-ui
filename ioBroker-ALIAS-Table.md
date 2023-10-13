**Tabelle nach rechts scrollen!!!**

<table border="1">
	<thead>
		<tr>
			<th>Nr.</th>
			<th>Alias-Type (german)</th>
			<th>Rolle (channel)</th>
			<th>Alias Datenpunkt</th>
			<th>required</th>
			<th>Datentyp</th>
			<th>Rolle (state)</th>
			<th>Datenpunkt (typisch)</th>
			<th>On-Icon</th>
			<th>Off-Icon</th>
			<th>Usericon</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1</td>
			<td>Bewegung</td>
			<td>motion</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>boolean</td>
			<td>sensor.motion</td>
			<td>Open</td>
			<td>motion-sensor</td>
			<td>&nbsp;</td>
			<td style="text-align:center">X</td>
		</tr>
		<tr>
			<td rowspan="5">2</td>
			<td rowspan="5">CIE Farblicht</td>
			<td rowspan="5">cie</td>
			<td>CIE</td>
			<td>X</td>
			<td>number</td>
			<td>level.color.cie</td>
			<td>&nbsp;</td>
			<td colspan="1" rowspan="5">lightbulb</td>
			<td colspan="1" rowspan="5">&nbsp;</td>
			<td colspan="1" rowspan="5">&nbsp;</td>
		</tr>
		<tr>
			<td>DIMMER</td>
			<td>X</td>
			<td>boolean</td>
			<td>level.dimmer</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>ON</td>
			<td>X</td>
			<td>boolean</td>
			<td>switch.light</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>ON_ACTUAL</td>
			<td>X</td>
			<td>boolean</td>
			<td>state.light</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>TEMPERATURE</td>
			<td>X</td>
			<td>number</td>
			<td>level.color.temperature</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="4">3</td>
			<td rowspan="4">Dimmer</td>
			<td rowspan="4">dimmer</td>
			<td>SET</td>
			<td>X</td>
			<td>number</td>
			<td>level.dimmer</td>
			<td>Level/Brightness</td>
			<td rowspan="4">lightbulb</td>
			<td rowspan="4">&nbsp;</td>
			<td rowspan="4">&nbsp;</td>
		</tr>
		<tr>
			<td>ACTUAL</td>
			<td>X</td>
			<td>number</td>
			<td>value.dimmer</td>
			<td>Level/Brightness</td>
		</tr>
		<tr>
			<td>ON_SET</td>
			<td>X</td>
			<td>boolean</td>
			<td>switch.light</td>
			<td>On/Switch/Power (Tasmota)</td>
		</tr>
		<tr>
			<td>ON_ACTUAL</td>
			<td>X</td>
			<td>boolean</td>
			<td>switch.light</td>
			<td>On/Switch/Power (Tasmota)</td>
		</tr>
		<tr>
			<td rowspan="4">4</td>
			<td rowspan="4">Fahrplan</td>
			<td rowspan="4">timeTable</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>string</td>
			<td>state</td>
			<td>&nbsp;</td>
			<td rowspan="4">&nbsp;</td>
			<td rowspan="4">&nbsp;</td>
			<td rowspan="4">&nbsp;</td>
		</tr>
		<tr>
			<td>VEHICLE</td>
			<td>X</td>
			<td>string</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>DIRECTION</td>
			<td>X</td>
			<td>string</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>DELAY</td>
			<td>X</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="3">5</td>
			<td rowspan="3">Farbtemperatur</td>
			<td rowspan="3">ct</td>
			<td>DIMMER</td>
			<td>X</td>
			<td>number</td>
			<td>level.dimmer</td>
			<td>Level/Brightness</td>
			<td colspan="1" rowspan="3">lightbulb</td>
			<td colspan="1" rowspan="3">&nbsp;</td>
			<td colspan="1" rowspan="3">&nbsp;</td>
		</tr>
		<tr>
			<td>ON</td>
			<td>X</td>
			<td>boolean</td>
			<td>&nbsp;</td>
			<td>On/Switch/Power (Tasmota)</td>
		</tr>
		<tr>
			<td>TEMPERATURE</td>
			<td>X</td>
			<td>number</td>
			<td>level.color.temperature</td>
			<td>Level/Color</td>
		</tr>
		<tr>
			<td>6</td>
			<td>Fenster</td>
			<td>window</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>boolean</td>
			<td>sensor.window</td>
			<td>Open</td>
			<td>information-outline</td>
			<td>&nbsp;</td>
			<td style="text-align:center">X</td>
		</tr>
		<tr>
			<td>7</td>
			<td>Feuchtigkeit</td>
			<td>humidity</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>number</td>
			<td>value.humidity</td>
			<td>Humidity</td>
			<td>information-outline</td>
			<td>&nbsp;</td>
			<td style="text-align:center">X</td>
		</tr>
		<tr>
			<td rowspan="5">8</td>
			<td rowspan="5">HUE-Licht</td>
			<td rowspan="5">hue</td>
			<td>DIMMER</td>
			<td>X</td>
			<td>number</td>
			<td>level.dimmer</td>
			<td>Level/Brightness</td>
			<td colspan="1" rowspan="5">lightbulb</td>
			<td colspan="1" rowspan="5">&nbsp;</td>
			<td colspan="1" rowspan="5">&nbsp;</td>
		</tr>
		<tr>
			<td>HUE</td>
			<td>&nbsp;</td>
			<td>number</td>
			<td>level.color.hue</td>
			<td>Hue</td>
		</tr>
		<tr>
			<td>ON</td>
			<td>X</td>
			<td>boolean</td>
			<td>switch.light</td>
			<td>On/Switch/Power (Tasmota)</td>
		</tr>
		<tr>
			<td>ON_ACTUAL</td>
			<td>X</td>
			<td>boolean</td>
			<td>state.light</td>
			<td>On/Switch/Power (Tasmota)</td>
		</tr>
		<tr>
			<td>TEMPERATURE</td>
			<td>X</td>
			<td>number</td>
			<td>level.color.temperature</td>
			<td>Level/Color</td>
		</tr>
		<tr>
			<td>9</td>
			<td>Info</td>
			<td>info</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>string</td>
			<td>state</td>
			<td>Alle Werte</td>
			<td>information-outline</td>
			<td>&nbsp;</td>
			<td style="text-align:center">X</td>
		</tr>
		<tr>
			<td rowspan="10">10</td>
			<td rowspan="10">Jalousien</td>
			<td rowspan="10">blind</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>number</td>
			<td>value.blind</td>
			<td>&nbsp;</td>
			<td colspan="1" rowspan="10">window-open</td>
			<td colspan="1" rowspan="10">&nbsp;</td>
			<td colspan="1" rowspan="10">&nbsp;</td>
		</tr>
		<tr>
			<td>CLOSE</td>
			<td>X</td>
			<td>boolean</td>
			<td>button.close.blind</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>OPEN</td>
			<td>X</td>
			<td>boolean</td>
			<td>button.open.blind</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SET</td>
			<td>X</td>
			<td>number</td>
			<td>level.blind</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>STOP</td>
			<td>X</td>
			<td>boolean</td>
			<td>button.stop.blind</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>TILT_ACTUAL</td>
			<td></td>
			<td>number</td>
			<td>value.blind</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>TILT_CLOSE</td>
			<td></td>
			<td>boolean</td>
			<td>button.close.blind</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>TILT_OPEN</td>
			<td></td>
			<td>boolean</td>
			<td>button.open.blind</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>TILT_SET</td>
			<td></td>
			<td>number</td>
			<td>level.blind</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>TILT_STOP</td>
			<td></td>
			<td>boolean</td>
			<td>button.stop.blind</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="15">11</td>
			<td rowspan="15">Klimaanlage</td>
			<td rowspan="15">airCondition</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>number</td>
			<td>value.temperature</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>AUTO</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>BOOST</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>switch.boost</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>COOL</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>ERROR</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>indicator.error</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>HEAT</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>HUMIDITY</td>
			<td>&nbsp;</td>
			<td>number</td>
			<td>value.humidity</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>MAINTAIN</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>indicator.maintainance</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>MODE</td>
			<td>X</td>
			<td>number</td>
			<td>level.mode.aircondition</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>OFF</td>
			<td>X</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>POWER</td>
			<td>X</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SET</td>
			<td>X</td>
			<td>number</td>
			<td>level.temperatur</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SPEED</td>
			<td>&nbsp;</td>
			<td>number</td>
			<td>level.mode.fan</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SWING</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>sitch.mode.swing</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>UNREACH</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>indicator.maintainance</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="3">12</td>
			<td rowspan="3">Lautst&auml;rke</td>
			<td rowspan="3">volume</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>number</td>
			<td>value.volume</td>
			<td>alexa2.0.Player.volume</td>
			<td colspan="1" rowspan="3">volume-low/<br>volume-medium/<br>volume-high/volume-mute</td>
			<td colspan="1" rowspan="3">&nbsp;</td>
			<td colspan="1" rowspan="3">&nbsp;</td>
		</tr>
		<tr>
			<td>MUTE</td>
			<td>X</td>
			<td>boolean</td>
			<td>media.mute</td>
			<td>alexa2.0.Player.muted</td>
		</tr>
		<tr>
			<td>SET</td>
			<td>X</td>
			<td>number</td>
			<td>level.volume</td>
			<td>alexa2.0.Player.volume</td>
		</tr>
		<tr>
			<td rowspan="3">13</td>
			<td rowspan="3">Lautst&auml;rkegruppe</td>
			<td rowspan="3">volumeGroup</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>number</td>
			<td>value.volume</td>
			<td>&nbsp;</td>
			<td colspan="1" rowspan="3">volume-low/<br>volume-medium/<br>volume-high/volume-mute</td>
			<td colspan="1" rowspan="3">&nbsp;</td>
			<td colspan="1" rowspan="3">&nbsp;</td>
		</tr>
		<tr>
			<td>MUTE</td>
			<td>X</td>
			<td>boolean</td>
			<td>media.mute</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SET</td>
			<td>X</td>
			<td>number</td>
			<td>level.volume</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>14</td>
			<td>Licht</td>
			<td>light</td>
			<td>SET</td>
			<td>X</td>
			<td>boolean</td>
			<td>switch.light</td>
			<td>On/Switch/Power (Tasmota)</td>
			<td>lightbulb</td>
			<td>lightbulb</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="16">15</td>
			<td rowspan="16">Medien</td>
			<td rowspan="16">media</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>number</td>
			<td>value.volume</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>ALBUM</td>
			<td>X</td>
			<td>string</td>
			<td>media.album</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>ARTIST</td>
			<td>X</td>
			<td>string</td>
			<td>media.artist</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>CONTENT_DESCRIPTION</td>
			<td>X</td>
			<td>string</td>
			<td>media.station</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>NEXT</td>
			<td>X</td>
			<td>boolean</td>
			<td>button.next</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>PAUSE</td>
			<td>X</td>
			<td>boolean</td>
			<td>button.pause</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>PLAY</td>
			<td>X</td>
			<td>boolean</td>
			<td>button.play</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>PREV</td>
			<td>X</td>
			<td>boolean</td>
			<td>button.prev</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SHUFFLE</td>
			<td>X</td>
			<td>boolean</td>
			<td>media.mode.shuffle</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>REPEAT</td>
			<td>X</td>
			<td>boolean</td>
			<td>media.mode.repeat</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>STATE</td>
			<td>X</td>
			<td>boolean</td>
			<td>media.state</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>status</td>
			<td>X</td>
			<td>string</td>
			<td>media.state</td>
			<td>
            	<ul>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>STOP</td>
			<td>X</td>
			<td>boolean</td>
			<td>button.stop</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>TITLE</td>
			<td>X</td>
			<td>string</td>
			<td>media.title</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>VOLUME</td>
			<td>X</td>
			<td>number</td>
			<td>level.volume</td>
			<td>
            	<ul>
                	<li>alexa2</li>
                    <li>spotify-premium</li>
                    <li>sonos</li>
                    <li>squeezeboxrpc</li>
                    <li>volumio</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>VOLUME_ACTUAL</td>
			<td>X</td>
			<td>number</td>
			<td>value.volume</td>
			<td>
            	<ul>
                    <li>squeezeboxrpc</li>
                </ul>
            </td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="8">16</td>
			<td rowspan="8">RGB-Licht</td>
			<td rowspan="8">rgb</td>
			<td>BLUE</td>
			<td>X</td>
			<td>number</td>
			<td>level.color.blue</td>
			<td>&nbsp;</td>
			<td colspan="1" rowspan="8">lightbulb</td>
			<td colspan="1" rowspan="8">&nbsp;</td>
			<td colspan="1" rowspan="8">&nbsp;</td>
		</tr>
		<tr>
			<td>DIMMER</td>
			<td>X</td>
			<td>number</td>
			<td>level.dimmer</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>GREEN</td>
			<td>X</td>
			<td>number</td>
			<td>level.color.green</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>ON</td>
			<td>X</td>
			<td>boolean</td>
			<td>switch.light</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>ON_ACTUAL</td>
			<td>X</td>
			<td>boolean</td>
			<td>state.light</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>RED</td>
			<td>X</td>
			<td>number</td>
			<td>level.color.red</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>TEMPERATURE</td>
			<td>X</td>
			<td>number</td>
			<td>level.color.temperature</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>WHITE</td>
			<td>&nbsp;</td>
			<td>number</td>
			<td>level.color.white</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="5">17</td>
			<td rowspan="5">RGB-Licht-einzeln</td>
			<td rowspan="5">rgbSingle</td>
			<td>DIMMER</td>
			<td>X</td>
			<td>number</td>
			<td>level.dimmer</td>
			<td>&nbsp;</td>
			<td colspan="1" rowspan="5">lightbulb</td>
			<td colspan="1" rowspan="5">&nbsp;</td>
			<td colspan="1" rowspan="5">&nbsp;</td>
		</tr>
		<tr>
			<td>ON</td>
			<td>X</td>
			<td>boolean</td>
			<td>switch.light</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>ON_ACTUAL</td>
			<td>X</td>
			<td>boolean</td>
			<td>state.light</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>RGB</td>
			<td>X</td>
			<td>string</td>
			<td>level.color.rgb</td>
			<td>HEX Color like #da43ff</td>
		</tr>
		<tr>
			<td>TEMPERATURE</td>
			<td>X</td>
			<td>number</td>
			<td>level.color.temperature</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="2">18</td>
			<td rowspan="2">Schieberegler</td>
			<td rowspan="2">slider</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>number</td>
			<td>value</td>
			<td>&nbsp;</td>
			<td colspan="1" rowspan="2">plus-minus-variant</td>
			<td colspan="1" rowspan="2">&nbsp;</td>
			<td colspan="1" rowspan="2">&nbsp;</td>
		</tr>
		<tr>
			<td>SET</td>
			<td>X</td>
			<td>number</td>
			<td>level</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="2">19</td>
			<td rowspan="2">Steckdose</td>
			<td rowspan="2">socket</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>boolean</td>
			<td>switch</td>
			<td>&nbsp;</td>
			<td colspan="1" rowspan="2">power-socket-de</td>
			<td colspan="1" rowspan="2">power-socket-de</td>
			<td colspan="1" rowspan="2">&nbsp;</td>
		</tr>
		<tr>
			<td>SET</td>
			<td>X</td>
			<td>boolean</td>
			<td>switch</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>20</td>
			<td>Taste</td>
			<td>button</td>
			<td>SET</td>
			<td>X</td>
			<td>boolean</td>
			<td>button</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>21</td>
			<td>Tastensensor</td>
			<td>buttonSensor</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
			<td>gesture-tap-button</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="2">22</td>
			<td rowspan="2">Temperatur</td>
			<td rowspan="2">temperature oder value.temperature</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>number</td>
			<td>value.temperature</td>
			<td>&nbsp;</td>
			<td colspan="1" rowspan="2">information-outline</td>
			<td colspan="1" rowspan="2">&nbsp;</td>
			<td colspan="1" rowspan="2">&nbsp;</td>
		</tr>
		<tr>
			<td>SECOND</td>
			<td>&nbsp;</td>
			<td>number</td>
			<td>value.humidity</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="15">23</td>
			<td rowspan="15">Thermostat</td>
			<td rowspan="15">thermostat</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>number</td>
			<td>value.temperature</td>
			<td>&nbsp;</td>
			<td colspan="1" rowspan="15">thermometer</td>
			<td colspan="1" rowspan="15">&nbsp;</td>
			<td colspan="1" rowspan="15" style="text-align:center">X</td>
		</tr>
		<tr>
			<td>AUTOMATIC</td>
			<td>X</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>BOOST</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>ERROR</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>HUMIDITY</td>
			<td>&nbsp;</td>
			<td>number</td>
			<td>value.humidity</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>LOWBAT</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>indicator.maintainance</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>MANUAL</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>MODE</td>
			<td>X</td>
			<td>number</td>
			<td>level.mode.thermostat</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>PARTY</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>POWER</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SET</td>
			<td>X</td>
			<td>number</td>
			<td>level.temperature</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>UNREACH</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>indicator.maintainance</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>VACATION</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>WINDOWOPEN</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>WORKING</td>
			<td>&nbsp;</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="2">24</td>
			<td rowspan="2">Timer</td>
			<td rowspan="2">level.timer</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>number</td>
			<td>timestamp</td>
			<td>&nbsp;</td>
			<td colspan="1" rowspan="2">&nbsp;</td>
			<td colspan="1" rowspan="2">&nbsp;</td>
			<td colspan="1" rowspan="2">&nbsp;</td>
		</tr>
		<tr>
			<td>STATE</td>
			<td>X</td>
			<td>string</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="3">25</td>
			<td rowspan="3">Tor</td>
			<td rowspan="3">gate</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>boolean</td>
			<td>switch.gate</td>
			<td>&nbsp;</td>
			<td colspan="1" rowspan="3">garage</td>
			<td colspan="1" rowspan="3">garage-open</td>
			<td colspan="1" rowspan="3">&nbsp;</td>
		</tr>
		<tr>
			<td>SET</td>
			<td>X</td>
			<td>boolean</td>
			<td>switch.gate</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>STOP</td>
			<td>X</td>
			<td>boolean</td>
			<td>button.stop</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>26</td>
			<td>T&uuml;r</td>
			<td>door</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>boolean</td>
			<td>sensor.door</td>
			<td>Open</td>
			<td>door-open</td>
			<td>door-closed</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="4">27</td>
			<td rowspan="4">Ventilator</td>
			<td rowspan="4">level.mode.fan</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
			<td rowspan="4">fan</td>
			<td rowspan="4">&nbsp;</td>
			<td rowspan="4">&nbsp;</td>
		</tr>
		<tr>
			<td>MODE</td>
			<td>X</td>
			<td>number</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SET</td>
			<td>X</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SPEED</td>
			<td>X</td>
			<td>number</td>
			<td>state</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="3">28</td>
			<td rowspan="3">Verschluss</td>
			<td rowspan="3">lock</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>boolean</td>
			<td>state</td>
			<td>&nbsp;</td>
			<td colspan="1" rowspan="3">lock</td>
			<td colspan="1" rowspan="3">lock-open-variant</td>
			<td colspan="1" rowspan="3">&nbsp;</td>
		</tr>
		<tr>
			<td>OPEN</td>
			<td>X</td>
			<td>boolean</td>
			<td>button</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SET</td>
			<td>X</td>
			<td>boolean</td>
			<td>switch.lock</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="3">29</td>
			<td rowspan="3">Warnung</td>
			<td rowspan="3">warning</td>
			<td>INFO</td>
			<td>X</td>
			<td>string</td>
			<td>weather.title</td>
			<td>&nbsp;</td>
			<td colspan="1" rowspan="3">&nbsp;</td>
			<td colspan="1" rowspan="3">&nbsp;</td>
			<td colspan="1" rowspan="3">&nbsp;</td>
		</tr>
		<tr>
			<td>LEVEL</td>
			<td>X</td>
			<td>number</td>
			<td>value.warning</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>TITLE</td>
			<td>X</td>
			<td>string</td>
			<td>weather.title.short</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td rowspan="2">30</td>
			<td rowspan="2">Wettervorhersage</td>
			<td rowspan="2">weatherforecast</td>
			<td>ICON</td>
			<td>X</td>
			<td>number</td>
			<td>weather.icon.forecast.0</td>
			<td>accuweather.0.Current.WeatherIcon</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>TEMP</td>
			<td>X</td>
			<td>number</td>
			<td>value.temperature.forecast.0</td>
			<td>accuweather.0.Current.Temperature</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
		<tr>
			<td>31</td>
			<td>Wifi</td>
			<td>info</td>
			<td>ACTUAL</td>
			<td>X</td>
			<td>string</td>
			<td>state</td>
			<td>Example 0_userdata.0.Datapoint:<br />
			&quot;WIFI:T:WPA;S:Test-SSID-Guest;P:guestaccess;H:;&quot;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
			<td>&nbsp;</td>
		</tr>
	</tbody>
</table>
