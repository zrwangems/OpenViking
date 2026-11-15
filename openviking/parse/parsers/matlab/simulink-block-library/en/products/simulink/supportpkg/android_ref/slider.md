---
type: simulink-block
title: 'Slider'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / User Interface'
documentation_page: 'slider'
documentation_source_path: 'supportpkg/android_ref/slider.html'
language: en
---

# Slider

## Ports

### Output

### **Port\_1** — Slider value numeric scalar

The block outputs the slider value corresponding to its position.

**Data Types:** `single`

## Parameters

### **Minimum** — Minimum value of slider `-5` (default) | numeric scalar

Specify the minimum value that the slider widget can output.

### **Initial value** — Initial value of slider `0` (default) | numeric scalar

Specify the initial value that the slider widget can output.

### **Maximum** — Maximum value of slider `5` (default) | numeric scalar

Specify the maximum value that the slider widget can output.

### **Resolution** — Resolution of slider `0.1` (default) | numeric scalar

Specify the smallest discrete change that the slider widget can output.

### **Sample time** — Time interval of sampling `0.1` (default) | nonnegative scalar

Specify a discrete time interval, in seconds, at which the block reads the slider
position and output the data.

**Note**

Smaller values for **Sample time** require the processor to
complete the same number of instructions in less time, which can cause task
overruns.

## Libraries

Simulink Support Package for Android Devices / User Interface

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2015a**

## Description

Display slider widget

Use the Slider block to display a slider widget on the device
screen.

The Slider block outputs a single-precision value. The output value depends
on the position of the slider along the length of the bar. When you slide the slider to the
left position, the block outputs the value of the **Minimum** parameter. When
you slide the slider to the rightmost position, the block outputs the value of the
**Maximum** parameter.

**Note**

During simulation with no hardware connected, this block outputs the initial
state.
