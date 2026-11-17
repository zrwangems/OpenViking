---
type: simulink-block
title: 'Generate Run Script'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Flight Simulator Interfaces'
documentation_page: 'generaterunscript'
documentation_source_path: 'generaterunscript.html'
language: en
---

# Generate Run Script

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Select target architecture
  summary: Target platform to run script Default (default) | Win64 | Linux | Mac
  group: ''
  block_parameter: Architecture
  type: character vector
  values: '''Win64'' | ''Linux'' | ''Mac'''
  default: '''Default'''
- name: Select FlightGear data flow
  summary: FlightGear data flow Send (default) | Receive | Send-Receive
  group: ''
  block_parameter: dataFlow
  type: character vector
  values: '''Receive'' | ''Send-Receive'''
  default: '''Send'''
- name: FlightGear geometry model name
  summary: Folder containing FlightGear geometry HL20 (default)
  group: ''
  block_parameter: GeometryModelName
  type: character vector
  values: '''HL20'''
  default: '''HL20'''
- name: Airport ID
  summary: ID of supported airport KSFO (default)
  group: ''
  block_parameter: '''AirportId'''
  type: character vector
  values: '''KSFO'''
  default: '''KSFO'''
- name: Runway ID
  summary: ID of supported runway 10L (default)
  group: ''
  block_parameter: RunwayId
  type: character vector
  values: '''10L'''
  default: '''10L'''
- name: Initial altitude (ft)\*
  summary: Initial aircraft altitude 7224 | numeric
  group: ''
  block_parameter: InitialAltitude
  type: character vector
  values: '''7224'''
  default: '''7224'''
- name: Initial heading (deg)\*
  summary: Initial aircraft heading 113 | numeric
  group: ''
  block_parameter: InitialHeading
  type: character vector
  values: '''113'''
  default: '''113'''
- name: Offset distance (miles)\*
  summary: Offset distance 4.72 | numeric
  group: ''
  block_parameter: OffsetDistance
  type: character vector
  values: '''4.72'''
  default: '''4.72'''
- name: Offset azimuth (deg)\*
  summary: Aircraft offset azimuth 0 | numeric
  group: ''
  block_parameter: OffsetAzimuth
  type: character vector
  values: '''0'''
  default: '''0'''
- name: Install FlightGear scenery during simulation (requires Internet connection)
  summary: Install FlightGear scenery off (default) | on
  group: ''
  block_parameter: InstallScenery
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Disable FlightGear shader options
  summary: Disable FlightGear shader off (default) | on
  group: ''
  block_parameter: DisableShaders
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Destination/Origin IP address
  summary: Network IP address of machine running MATLAB 127.0.0.1
  group: ''
  block_parameter: OriginAddress
  type: character vector
  values: '''127.0.0.1'''
  default: '''127.0.0.1'''
- name: Destination port
  summary: Destination port of FlightGear machine 5502
  group: ''
  block_parameter: DestinationPort
  type: character vector
  values: '''5502'''
  default: '''5502'''
- name: Origin port
  summary: Origin port of FlightGear machine 5505
  group: ''
  block_parameter: OriginPort
  type: character vector
  values: '''5505'''
  default: '''5505'''
- name: Network IP address
  summary: Network IP address of FlightGear machine 127.0.0.1
  group: ''
  block_parameter: LocalAddress
  type: character vector
  values: '''127.0.0.1'''
  default: '''127.0.0.1'''
- name: Output file name
  summary: Output file runfg.bat
  group: ''
  block_parameter: OutputFileName
  type: character vector
  values: '''runfg.bat'''
  default: '''runfg.bat'''
- name: FlightGear base directory
  summary: FlightGear base directory C:\Program Files\FlightGear
  group: ''
  block_parameter: FlightGearBaseDirectory
  type: character vector
  values: '''C:\Program Files\FlightGear'''
  default: '''C:\Program Files\FlightGear'''
- name: Generate Script
  summary: Generate Script button button
  group: ''
```

### **Select target architecture** — Target platform to run script `Default` (default) | `Win64` | `Linux` | `Mac`

From the list, select the target platform on which you want to execute the
run script. This platform can differ from the platform on which you create
the run script. Select `Default` if you want to generate a
run script to run on the platform from which you create the run
script.

- `Win64`
- `Linux`
- `Mac`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Architecture` |
| **Type**: character vector |
| **Values:** `'Win64' | 'Linux' | 'Mac'` |
| **Default**: `'Default'` |

### **Select FlightGear data flow** — FlightGear data flow `Send` (default) | `Receive` | `Send-Receive`

From the list, select the direction of the data flow:

- `Send`

  Creates the run script to set up the sending of the
  `net_fdm` control model from Simulink to FlightGear.
- `Receive`

  Creates the run script to set up the receiving of the
  `net_ctrl` control model from FlightGear to
  Simulink.
- `Send-Receive`

  Creates the run script to set up FlightGear to receive and
  broadcast data to and from Simulink.

  **Note**

  Selecting the `Send-Receive` option does not
  mean that you receive the same data that you sent (for example,
  you might not see control surface position data). With this
  option, you see primarily user input (such as data input via
  joystick) and environmental data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `dataFlow` |
| **Type**: character vector |
| **Values:** `'Receive' | 'Send-Receive'` |
| **Default**: `'Send'` |

### **FlightGear geometry model name** — Folder containing FlightGear geometry HL20 (default)

Specify the name of the folder containing the model geometry that you want
in the
*`FlightGear`*`\data\Aircraft`
folder.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `GeometryModelName` |
| **Type**: character vector |
| **Values:**`'HL20'` |
| **Default**: `'HL20'` |

### **Airport ID** — ID of supported airport KSFO (default)

ID of supported airport, selected from a list of supported airports
available in the FlightGear interface, under **Location**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `'AirportId'` |
| **Type**: character vector |
| **Values:**`'KSFO'` |
| **Default**: `'KSFO'` |

### **Runway ID** — ID of supported runway 10L (default)

Specify the runway ID.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `RunwayId` |
| **Type**: character vector |
| **Values:**`'10L'` |
| **Default**: `'10L'` |

### **Initial altitude (ft)\*** — Initial aircraft altitude 7224 | numeric

Initial altitude of the aircraft, in feet.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialAltitude` |
| **Type**: character vector |
| **Values:**`'7224'` |
| **Default**: `'7224'` |

### **Initial heading (deg)\*** — Initial aircraft heading 113 | numeric

Initial heading of the aircraft, in degrees.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialHeading` |
| **Type**: character vector |
| **Values:**`'113'` |
| **Default**: `'113'` |

### **Offset distance (miles)\*** — Offset distance 4.72 | numeric

Offset distance of the aircraft from the airport, in miles.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OffsetDistance` |
| **Type**: character vector |
| **Values:**`'4.72'` |
| **Default**: `'4.72'` |

### **Offset azimuth (deg)\*** — Aircraft offset azimuth 0 | numeric

Offset azimuth of the aircraft, in degrees.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OffsetAzimuth` |
| **Type**: character vector |
| **Values:**`'0'` |
| **Default**: `'0'` |

### **Install FlightGear scenery during simulation (requires Internet connection)** — Install FlightGear scenery `off` (default) | `on`

Select this check box to direct FlightGear to automatically install required scenery
while the simulator is running. Selecting this check box requires a stable
Internet connection. For Windows® systems, you may encounter an error message while launching
FlightGear with this option enabled. For more information, see Install Additional FlightGear Scenery.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InstallScenery` |
| **Type**: character vector |
| **Values:**`'off' | 'on'` |
| **Default**: `'off'` |

### **Disable FlightGear shader options** — Disable FlightGear shader `off` (default) | `on`

Select this check box to disable FlightGear shader options. Your computer
built-in video card, such as NVIDIA® cards, can conflict with FlightGear shaders. Consider
selecting this check box if you have this conflict.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DisableShaders` |
| **Type**: character vector |
| **Values:**`'off' | 'on'` |
| **Default**: `'off'` |

### **Destination/Origin IP address** — Network IP address of machine running MATLAB 127.0.0.1

Network IP address of the machine on which MATLAB runs. This value is read-only.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OriginAddress` |
| **Type**: character vector |
| **Values:**`'127.0.0.1'` |
| **Default**: `'127.0.0.1'` |

### **Destination port** — Destination port of FlightGear machine 5502

Network flight dynamics model (fdm) port. For more information, see the
Send net\_fdm Packet to FlightGear block reference.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DestinationPort` |
| **Type**: character vector |
| **Values:**`'5502'` |
| **Default**: `'5502'` |

### **Origin port** — Origin port of FlightGear machine 5505

Network control (`ctrl`) port. For more information, see
the Receive net\_ctrl Packet from
FlightGear block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OriginPort` |
| **Type**: character vector |
| **Values:**`'5505'` |
| **Default**: `'5505'` |

### **Network IP address** — Network IP address of FlightGear machine 127.0.0.1

Network IP address of the machine on which the MATLAB software runs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LocalAddress` |
| **Type**: character vector |
| **Values:**`'127.0.0.1'` |
| **Default**: `'127.0.0.1'` |

### **Output file name** — Output file `runfg.bat`

Output file name. The file name is the name of the command that you use to
start FlightGear with these initial parameters.

**Note**

The run script file name must be composed of ASCII characters.

Use these file extensions:

| Platform | Extension |
| --- | --- |
| Windows | `.bat` |
| Linux® and macOS | `.sh` |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputFileName` |
| **Type**: character vector |
| **Values:**`'runfg.bat'` |
| **Default**: `'runfg.bat'` |

### **FlightGear base directory** — FlightGear base directory `C:\Program Files\FlightGear`

Specify the name of the FlightGear installation folder.

**Note**

FlightGear must be installed in a folder path name composed of ASCII
characters.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `FlightGearBaseDirectory` |
| **Type**: character vector |
| **Values:**`'C:\Program Files\FlightGear'` |
| **Default**: `'C:\Program Files\FlightGear'` |

### **Generate Script** — Generate Script button button

Click **Generate Script** to generate a run script for
FlightGear. Do not click this button until you have entered the correct
information in the dialog box parameters.
## Libraries

Aerospace Blockset / Animation / Flight Simulator Interfaces

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Generate FlightGear run script on current platform

The Generate Run Script block generates a customized FlightGear run script on the current platform.

To generate the run script, fill in the required information
in the Parameters fields, then click **Generate Script**.

In the dialog box, fields marked with an asterisk (\*) are evaluated
as MATLAB® expressions. The other fields are treated as literal text.
