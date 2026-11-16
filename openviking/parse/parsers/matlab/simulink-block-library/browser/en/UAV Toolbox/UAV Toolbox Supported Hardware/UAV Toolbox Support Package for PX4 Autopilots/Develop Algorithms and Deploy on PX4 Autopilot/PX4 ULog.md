---
type: simulink-block
title: 'PX4 ULog'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4ulog'
documentation_source_path: 'px4/ref/px4ulog.html'
language: en
---

# PX4 ULog

## Ports

### Input

### **double\_a** — First input signal, specified as double scalar

Input signal to be logged by the block, specified as double.

**Data Types:** `double`

### **double\_b** — Second input signal, specified as double scalar

Input signal to be logged by the block, specified as double.

**Data Types:** `double`

### **single\_a** — First input signal, specified as single scalar

Input signal to be logged by the block, specified as single.

**Data Types:** `single`

### **single\_b** — Second input signal, specified as single scalar

Input signal to be logged by the block, specified as single.

**Data Types:** `single`

## Parameters

### **Topic** — Name of the uORB topic to which the Simulink signals are to be logged SL\_CustomPX4uORB (default) | one of the uORB topics

Select the name of the uORB topic that the block needs to log Simulink signals.
Click **Select** to browse topic names available in the
`Firmware/msg` folder of the `px4` directory
that you downloaded.

## Libraries

UAV Toolbox Support Package for PX4 Autopilots / PX4 Utility Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023b**

## Description

Log Simulink signals to an SD card in ULog format

The PX4 ULog block logs the Simulink® signals to an SD Card in the ULog format.

In PX4 Autopilots, the system architecture uses logger module that logs topics in ULog
file formats. PX4 uses  ULog file
format for uORB
logging messages. These messages are commonly known as micro-ORB (Object Request Broker)
and form the basis for subscribe, publish architecture in PX4.

The ULog format is efficient for post-flight analysis. Using ulogreader, flight logger
app or online tools you can analyze, visualize, and convert ULog files to gain insights and
improve the performance of PX4-based autonomous systems.

The number of ports in the block updates as per the uORB topic selected. To create your
own topic, use `createPX4uORBMessage` API. The block is
currently configured with default uORB topic `SL_CustomPX4uORB` that is
build during setup screens.

**Note**

This block does not support PX4 Host target and Connected I/O Simulation.
