---
type: simulink-block
title: 'Optical Shaft Encoder'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / Sensors'
documentation_page: 'opticalshaftencoder'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/opticalshaftencoder.html'
language: en
---

# Optical Shaft Encoder

## Ports

Not documented in R2025b.

## Parameters

**Top Port**
:   Select the digital port number to which the top connector is connected. You can
    select a port number from 1 to 12 except port 10. To know the top port, click the
    **What is Top and Bottom Port?** button on the block parameters
    dialog window.

**Bottom Port**
:   Select the digital port number to which the bottom connector is connected. You can
    select a port number from 1 to 12 except port 10. To know the bottom port, click the
    **What is Top and Bottom Port?** button on the block parameters
    dialog window.

**Reset mode**
:   Select the reset mode for resetting the measured value of the encoder. In the
    example table shown below for reset modes, the block is assumed to have the tick count
    at time instant T = 0 is 0 and sample time 1 sec.

    The different reset modes this block supports are as follows:

    - `No reset` – The measurement value is not reset and
      the block outputs the total ticks of rotation.

      For example, in the table below at T = 1, the encoder moves a tick count of 20
      in anti-clockwise direction and therefore the output is 20. Between T = 1 and T =
      2, the encoder moves a tick count of 10.

      Therefore, the tick count is 30 at T = 2 ( 20 from T = 1 and 10 from T = 2).
      In this reset mode, the output at any time instant is a cumulative sum of the
      previous count and the current count.
    - `Reset at each sample time`  – For each sample
      period, the block outputs the measurement value and then resets it to 0.

      For example, in the table below, at T = 1, the encoder moves a tick count of
      20 in anti-clockwise direction and therefore the output is 20. Between T = 1 and T
      = 2, the encoder moves a tick count of 10 and therefore the output is 10. In this
      reset mode, the output is the tick count at a particular time instant.
    - `Reset by external signal`  – The measurement value
      is reset to 0 based on the block input value. When you send a value other than 0
      to the block input, the measurement value is reset to 0. For each sample period,
      the block outputs the measurement value since the last reset.

      For example in the table below, when the external signal is 0, the output is
      based on ‘No reset’ mode and when the external signal is non-zero, the output is
      based on ‘Reset at each sample time’ mode.

**Add input port for simulation**
:   Select this check box, if you want the normal mode simulation with a source block
    providing the input value.

**Sample time**
:   Specify how often this block reads the rotation, in seconds. If you select
    **Add input port for simulation** check box or select
    `Reset by external signal` option in **Reset
    mode** parameter, the **Sample time** parameter is hidden
    and the value is inherited (Sample time = -1).

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Measure the rotation of a motor in ticks

Measure the rotation of a motor shaft passing through the sensor, in ticks. For
anti-clockwise rotation, the tick count increments and for clockwise rotation, the tick
count decrements. The block output is 360 ticks for one rotation.

During simulations, without the hardware, this block emits zeros if no Source block is
connected to the simulation input port. See Block Produces Zeros or Does Nothing in Simulation. Connect a Source block from
the Utilities library in VEX Microcontroller library to achieve simulation behavior. During
code generation, any simulation block that is connected to the input port of the Optical
Shaft Encoder block is ignored and has no effect on the generated code.
