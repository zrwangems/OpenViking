---
type: simulink-block
title: 'Radio Control Transmitter'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'radiocontroltransmitter'
documentation_source_path: 'px4/ref/radiocontroltransmitter.html'
language: en
---

# Radio Control Transmitter

## Ports

### Output

### **Ch *`x`*** — Measured pulse width value from the specified radio communication channel scalar | time in the range [1, 2] ms

Pulse width values obtained from the selected channels of the Radio Control
Transmitter. Connect these output values to the flight control logic in the Simulink
model.

**Data Types:** `uint16`

### **Num Ch** — Count of channels that are actually being seen scalar

The count of channels that are actually being seen based on the communication with
the Radio Control Transmitter

#### Dependencies

This output appears only if you have selected the **Number of channels
actually being seen** parameter.

**Data Types:** `uint32`

### **RSSI** — RSSI value from the RC Transmitter negative | `0` | positive

RSSI (Receive Signal Strength Indicator ) value obtained from the Radio Control
Transmitter.

The value is negative for an undefined signal, 0 for no signal, and positive for
full reception.

#### Dependencies

This output appears only if you have selected the **Receive Signal
Strength Indicator (RSSI)** parameter.

**Data Types:** `int32`

### **RC Source** — Input source of RC communication scalar

Identify the input source of RC communication. The value ranges from
`0` to `13` (these correspond to the same values
as mentioned in the `input_rc.msg` file in
`Firmare/msg` directory).

#### Dependencies

This output appears only if you have selected the **Radio control input
source** parameter.

**Data Types:** `uint8`

### **Last valid time** — Timestamp of the last valid reception time

Timestamp of the last valid reception from the Radio Control Transmitter.

#### Dependencies

This output appears only if you have selected the **Last valid reception
time** parameter.

**Data Types:** `uint64`

### **Timestamp** — Current timestamp time

Current timestamp of the value received from the Radio Control Transmitter.

#### Dependencies

This output appears only if you have selected the **Timestamp**
parameter.

**Data Types:** `double`

### **Status** — Status of the data read from input\_rc uORB topic integer in [`0,7`]

The Status output indicates if the data was received during a previous time step
or not. A value of `0` indicates that the data at the
`Ch` output is the latest and the communication with the Radio
Control Transmitter is valid.

A value between 1 and 7 indicates the following:

- No value was read by the uORB topic during the current time step
- Communication loss with Radio Control Transmitter
- Radio Control Transmitter went to failsafe mode

This output can be used to trigger subsystems for processing the new data received
from the RC Transmitter.

**Data Types:** `uint8`

## Parameters

#### Main tab

### **Channel Selection** — Radio channels from which you want to receive values channels

Select the channels from which you want to receive values, as read from the Radio
Control Transmitter. The `Ch` outputs of the block appear based on the
selection in this parameter list.

### **Number of channels actually being seen** — Count of channels that are actually being seen `off` (default) | `on`

Select this option to obtain the count of channels that are actually being seen
based on the communication with the Radio Control Transmitter.

### **Receive Signal Strength Indicator (RSSI)** — RSSI value from the RC Transmitter `off` (default) | `on`

Select this option to obtain the RSSI value as received from the Radio Control
Transmitter

### **Radio control input source** — Input source of RC communication `off` (default) | `on`

Select this option to identify the input source of RC communication.

### **Last valid reception time** — Timestamp of the last valid reception `off` (default) | `on`

Select this option to obtain the timestamp of the last valid reception from the
Radio Control Transmitter.

### **Timestamp** — Current timestamp `off` (default) | `on`

Select this option to obtain the current timestamp of the channel value from the
Radio Control Transmitter.

### **Sample time** — Interval at which the block reads values `1/250` seconds (default) | any non-negative value that is a multiple of 1/250 | -1

Enter the time interval at which the block reads values from the RC
Transmitter.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

#### Advanced tab

### **Wait until data received** — Wait until requested data is available off (default) | on

- When you select this option, the read operation runs in Blocking Mode. The read
  operation is blocked while waiting for the requested data to be available.

  A task overrun occurs if the target hardware is still waiting for the data to be
  available when the next read operation is scheduled to begin.

  To fix overruns, increase the time step by using the **Sample
  time** parameter.
- When you clear this option, the read operation runs in Non-Blocking Mode. In
  this mode, the block does not wait for the requested data to be available.

### **Timeout in seconds** — Time to wait until the data is received `5` (default) | (0, 2^32/1000]

Specify the amount of time that the block waits for the data during each time step,
if the **Wait until data received** parameter is selected. If timeout
occurs, the read operation is aborted.

#### Dependencies

This parameter appears only when you select the **Wait until data
received** parameter.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 Sensor Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Read input_rc uORB topic to obtain data from Radio Control Transmitter

The Radio Control Transmitter block reads the input\_rc uORB topic to obtain
the signals sent from a Radio Control Transmitter at the specified channels.

During Normal mode simulation, the block outputs zeroes.

During Connected I/O simulation, this block reads data from the peripherals of the
hardware.
