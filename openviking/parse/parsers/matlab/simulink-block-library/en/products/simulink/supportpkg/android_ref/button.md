---
type: simulink-block
title: 'Button'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / User Interface'
documentation_page: 'button'
documentation_source_path: 'supportpkg/android_ref/button.html'
language: en
---

# Button

## Ports

### Output

### **Port\_1** — Button state output Boolean scalar

The block outputs the button state, returned as a Boolean scalar. If the button
state is `Pressed`, the block outputs `1`.
If the button state is `Not Pressed`, the block outputs
`0`.

**Data Types:** `Boolean`

## Parameters

### **Button state** — Initial state of button `Not pressed` (default) | `Pressed`

Select the initial state of the button when the Android app starts.

### **Sample time** — Time interval of sampling `0.1` (default) | nonnegative scalar

Specify a discrete time interval, in seconds, at which the block reads the button
state and outputs the data.

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

Display button widget on device screen

The Button block displays a button widget on the Android® app. The button has two states: *pressed* and
*not-pressed*. Tapping the button switches the state of the
button. The **Button state** parameter determines the button
state when the Android app starts.

**Note**

During simulation with no hardware connected, this block does nothing. For more
information, see Block Produces Zeros or Does Nothing in Simulation.
