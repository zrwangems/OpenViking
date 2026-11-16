---
type: simulink-block
title: 'Ultrasonic Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Sensors'
documentation_page: 'ultrasonicsensor'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/ultrasonicsensor.html'
language: en
---

# Ultrasonic Sensor

## Ports

Not documented in R2025b.

## Parameters

**INPUT (Ping port)**
:   Select the digital port to which the connector ‘INPUT’ of the ultrasonic sensor is
    connected. To know the INPUT port, click the **What is INPUT and
    OUTPUT?** button on the block parameters dialog window.

**OUTPUT (Echo port)**
:   Select the digital port to which the connector ‘OUTPUT’ of the ultrasonic sensor
    is connected. To know the OUTPUT port, click the **What is INPUT and
    OUTPUT?** button on the block parameters dialog window. You can select any
    port number for OUTPUT except port number 10.

**Add input port for simulation**
:   Select this check box, if you want the normal mode simulation with a source block
    providing the input value.

**Sample time**
:   Specify how often this block reads the distance, in seconds. If you select
    **Add input port for simulation** check box, the **Sample
    time** parameter is hidden and the value is inherited (Sample time =
    -1).

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Measure the distance to an object: 0.02 to 2.0 meters (m)

Measure the distance of the object in the path of the robot by using high-frequency
sound waves. The block enables the object detection when it is in the range from 0.02
through 2.0 meters of the sensor. The block outputs a value 0 for an object that is farther
than 2 meters.

During simulations, without the hardware, this block emits zeros if no Source block is
connected to the simulation input port. See Block Produces Zeros or Does Nothing in Simulation. To achieve simulation
behavior, connect a Source block from the Utilities library in VEX Microcontroller library.
During code generation, any simulation block that is connected to the input port of the
Ultrasonic Sensor block is ignored and has no effect on the generated code.
