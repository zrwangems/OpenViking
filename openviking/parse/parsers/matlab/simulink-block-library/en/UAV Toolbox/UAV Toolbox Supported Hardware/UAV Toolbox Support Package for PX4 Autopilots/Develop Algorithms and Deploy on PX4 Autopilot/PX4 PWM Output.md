---
type: simulink-block
title: 'PX4 PWM Output'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4pwmoutput'
documentation_source_path: 'px4/ref/px4pwmoutput.html'
language: en
---

# PX4 PWM Output

## Ports

### Input

### **Arm** — Arm the PX4 flight controller `0` (default) | `1`

Enable signal for arming the PX4 flight controller.

**Data Types:** `Boolean`

### **Set failsafe** — Enforce failsafe for PX4 flight controller `0` (default) | `1`

Enforce failsafe values even though the failsafe conditions might or might not
have occurred. You can specify the failsafe values in the Configuration Parameters
dialog box in Simulink.

**Note**

If you are using PX4 firmware 1.12.3, the value at `Set failsafe` input
port is not valid if you use AUX channels for PWM.

**Data Types:** `Boolean`

### **Ch *`x`*** — Inputs that accept PWM ON values `0` (default) | `1`

Connect the Ch `x` inputs to signals that represent PWM ON values
(in microseconds)

#### Dependencies

The required `Ch` inputs are selected using the **PWM
Channels** parameter.

**Data Types:** `uint16`

## Parameters

#### Main tab

### **Select PWM Device** — Channel category to identify the channels that you are going to select Main (default) | Aux

Select the category (Main or AUX) to identify and select the corresponding channels.
After you select this category, you can select the channels in the parameter list, for
Main and AUX, separately.

### **PWM Channels** — Channels to which you want to send the PWM ON time values Channel numbers

Select the channels to which you want to send the values for PWM ON time (the
channels to which you connect servo motors or ESC). The `Ch` inputs to
the block appear based on the selection in this parameter list.

**Note**

Ensure that you select all the channels that belong to the same channel group. If
you need to connect to PWM channels that are in different groups, select all channels
in all the desired groups. Only one PX4 PWM Output block per channel category (Main or
AUX) is allowed in the entire Simulink model.

**Tip**

To identify the channel groups in the Pixhawk Series flight controller board, use
QGroundControl application on your host computer:

1. Open QGroundControl.
2. Connect the Pixhawk Series flight controller board to the USB port of the
   host computer.
3. In QGroundControl, go to **Mavlink Console**, and do
   the following:

   - To identify the Main channels and their groups, enter the command
     `pwm info`.
   - To identify the Aux channels and their groups, enter the command
     `pwm info -d /dev/pwm_output1`

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

### R2024b: To be removed in a future release

The PX4 PWM Output function will be removed in a future release. Use the
PX4 Actuator Write block instead.

For information to convert the PX4 PWM Output in your Simulink model to a
PX4 Actuator Write block, see Convert PX4 PWM Output Block to PX4 Actuator Write Block.

## Description

Configure PWM outputs for servo motors and ESC control

The PX4 PWM Output block helps you to configure the PWM output from the
PX4® flight controller board. The block accepts time value (in microseconds) that
represents the ON period of PWM signal for a particular channel, and passes the same to the
corresponding PWM channels on the board.

The PX4 PWM Output block also accepts signals for arming the flight
controller.

During Connected IO simulation, this block writes data to the peripherals of the
hardware.

**Configure Actuators**

For Firmware version 1.14, the PWM & AUX pins need to be configured in QGroundControl
before the PWM Output block can be used in Simulink. To do this, QGroundControl version 4.2.8
is needed which can be downloaded from this
location.

**Note**

Configuring the actuators is not required for Hardware-in-the-loop or PX4 Host Target
simulations.

To configure the actuators, perform these steps.

1. Perform the Hardware setup process for your Autopilot.
2. Launch QGroundControl 4.2.8 (QGC) and allow it connect to your Autopilot.
3. Once QGC is connected, go to **Vehicle Setup** ->
   **Actuators** tab.

   Hardware board
4. Assign the following sequence of Motors against each Main Channel.

   Hardware board

   It is recommended to change the Minimum PWM value of each channel to 1000 and Maximum
   PWM value to 2000.
5. Assign the following sequence of Motors against each AUX Channel.

   Hardware board
