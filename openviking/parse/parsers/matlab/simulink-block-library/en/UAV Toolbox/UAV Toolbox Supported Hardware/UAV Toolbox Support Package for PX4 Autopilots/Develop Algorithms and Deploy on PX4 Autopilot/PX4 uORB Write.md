---
type: simulink-block
title: 'PX4 uORB Write'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4uorbwrite'
documentation_source_path: 'px4/ref/px4uorbwrite.html'
language: en
---

# PX4 uORB Write

## Ports

### Input

### **Msg** — uORB message, specified as a nonvirtual bus nonvirtual bus

To specify the type of uORB message, use the parameter, `Topic to Publish
to`.

**Data Types:** `bus`

## Parameters

#### Main Tab

### **Topic to publish to** — Name of the uORB topic to which the message needs to be published vehicle\_gps\_position (default) | one of the uORB topics

Select the name of the uORB topic that the block needs to publish to. Click
**Select** to browse topic names available in the
`Firmware/msg` folder of the `px4` directory that
you downloaded.

### **Select instance** — Instance of the uORB topic to which the message needs to be published instance of the uORB topic

Select the instance of the uORB topic that the block needs needs to publish to.

#### Dependencies

This parameter appears only if you select a topic that supports multiple
instances, in the **Topic to publish to** parameter.

For example, the `actuator_controls` topic supports multiple
instances and you can select one instance from the drop-down.

#### Advanced Tab

### **Length of publish queue** — Maximum number of buffered elements `1` (default) | integer

Enter the maximum number of buffered elements in the publish queue. If the value is
`1`, no queuing is used to publish the data.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 uORB Read and Write Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Write uORB data for the specified uORB topic

The PX4 uORB Write block accepts a Simulink® nonvirtual bus that corresponds to the specified uORB topic and publishes the
message to the uORB network.

On each sample hit, the block converts the `Msg` input from a Simulink bus signal to a uORB message and publishes it. The block does not distinguish
whether the input is a new message; but, merely publishes it on every sample hit.

During Connected I/O simulation, this block writes data to the peripherals of the
hardware.
