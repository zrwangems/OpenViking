---
type: simulink-block
title: 'PX4 Analog Input'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4analoginput'
documentation_source_path: 'px4/ref/px4analoginput.html'
language: en
---

# PX4 Analog Input

## Ports

### Output

### **Port\_1** — Voltage values represented as a 1-by-12 array analog

The voltage values captured at the different ADC channels on the flight controller
board.

Connect this output to a Selector block with its `Input port
size` parameter value set to `12`. You can use the
Selector block to specify the index values of the required channel numbers from which
you want to read the voltage values.

**Data Types:** `vector`

## Parameters

### **Sample time** — Interval at which the block reads analog voltage values `0.001` (default) | any non-negative value that is a multiple of 0.001 | -1

Enter the time interval at which the block reads voltage values from the ADC
channels on the flight controller board.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Measure analog voltage applied to an ADC channel

The PX4 Analog Input block measure the analog voltage at the ADC channels
on the PX4® flight controller hardware, and outputs the voltages as a 1-by-12 array. Each
value in the array corresponds to the analog voltage at a particular channel number.

For more information about mapping the channel numbers and the voltage array, see Index Numbers for Analog Channels on Pixhawk Series Controller Boards.

During Normal mode simulation, the block outputs zeroes.

During Connected I/O simulation, this block reads data from the peripherals of the
hardware.
