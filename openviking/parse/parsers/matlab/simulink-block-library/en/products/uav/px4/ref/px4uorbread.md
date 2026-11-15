---
type: simulink-block
title: 'PX4 uORB Read'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4uorbread'
documentation_source_path: 'px4/ref/px4uorbread.html'
language: en
---

# PX4 uORB Read

## Ports

### Output

### **Msg** — uORB message nonvirtual bus

uORB message, returned as a nonvirtual bus. The type of uORB message is specified
using the parameter, `Topic to subscribe to`.

Connect a Bus Selector block to the `Msg` output to extract the
signals.

**Data Types:** `bus`

### **Status** — Status of the received uORB data `0` | `1`

The Status output indicates if the uORB message was received during a previous
time step or not. A value of `0` indicates that the uORB data at the
`Msg` output is the latest, and a value of `1`
indicates that the uORB data was received during the previous time step.

This output can be used to trigger subsystems for processing the new messages
received in the uORB network.

**Data Types:** `Boolean`

## Parameters

#### Main tab

### **Topic to subscribe to** — Name of the uORB topic to which the block needs to subscribe sensor\_accel (default) | One of the uORB topic

Select the name of the uORB topic that the block needs to subscribe to read the uORB
data. Click **Select** to browse the topic names available in the
`Firmware/msg` folder of the `px4` directory that
you downloaded.

### **Select instance** — Instance of the uORB topic to which the block needs to subscribe instance of the uORB topic

Select the instance of the uORB topic that the block needs to subscribe to read the
uORB data.

#### Dependencies

This parameter appears only if you select a topic that supports multiple
instances, in the **Topic to subscribe to** parameter.

For example, the `actuator_controls` topic supports multiple
instances and you can select one instance from the drop-down.

### **Sample time** — Interval at which the block reads values `0.001` (default) | any non-negative value that is a multiple of 0.001 | -1

Enter the time interval at which the block reads values from the uORB
network.

When you set this parameter to `-1`, Simulink determines the best sample time for the block based on the block context
within the model.

#### Advanced Tab

### **Wait until data received** — Wait until requested data is available off (default) | on

- When you select this option, the read operation runs in Blocking Mode. The read
  operation is blocked while waiting for the requested data to be available. When
  waiting for the data, the **Status** port displays same values from
  the previous time step. When the data become available, the
  **Data** port outputs data bytes, and the
  **Status** port changes to `0`.

  A task overrun occurs if the target hardware is still waiting for the data to be
  available when the next read operation is scheduled to begin.

  To fix overruns, Increase the time step by using the **Sample
  time** parameter.
- When you clear this option, the read operation runs in Non-Blocking Mode. In
  this mode, the block does not wait for the requested data to be available.

### **Timeout in seconds** — Time to wait until the data is received `0.1` (default) | (0, 2^32/1000]

Specify the amount of time that the block waits for the data during each time step,
if the **Wait until data received** parameter is selected. If timeout
occurs, the read operation is aborted.

#### Dependencies

This parameter appears only when you select the **Wait until data
received** parameter.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 uORB Read and Write Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Read uORB data for the specified uORB topic

The PX4 uORB Read block creates a Simulink® nonvirtual bus that corresponds to the specified uORB topic.

On each simulation step, the block checks if a new message is available on the specific
topic. If a new message is available, the block retrieves the message and converts it to a
Simulink bus signal. The Msg port outputs this new message. If a new message is not
available, Msg outputs the last received uORB message. If a message has not been received
since the start of the simulation, Msg outputs a blank message.

During Normal mode simulation, the block outputs zeroes.

During Connected I/O simulation, this block reads data from the peripherals of the
hardware.
