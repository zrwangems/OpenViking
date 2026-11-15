---
type: simulink-block
title: 'Optical Shaft Encoder'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'opticalshaftencoder'
documentation_source_path: 'vexv5/ref/opticalshaftencoder.html'
language: en
---

# Optical Shaft Encoder

## Ports

### Input

### **Rst** — Signal that resets the encoder reading integer (0 = no reset; integer ≥ 1 = reset)

Connect to a signal that resets the Optical Shaft Encoder.

#### Dependencies

This input appears only when you set the **Reset mode**
parameter to `Reset by external signal`.

**Data Types:** `double`
### Output

### **Tick** — Number of ticks read from Optical Shaft Encoder tick count

The number of ticks that is read from the Optical Shaft Encoder connected to VEX
V5 Robot Brain. One rotation corresponds to 360 ticks. The value increments for
anti-clockwise rotation and decrements for clockwise rotation of the motor
shaft.

**Data Types:** `double`

## Parameters

### **3-Wire Expander (smart port)** — Select the smart port that is used by 3-Wire Expander `None` (default) | `1` to `21`

If you are using a 3-Wire Expander, specify the smart port on VEX® EDR V5 Robot Brain to which the expander is connected.

### **Top port** — 3-wire port to which the top port of Optical Shaft Encoder is connected A (default) | `C` | `E` | `G`

Select the 3-wire port of VEX V5 Robot Brain to which the top port of Optical Shaft
Encoder is connected. To know the top port, click the **What is Top and Bottom
Port?** button.

After you select the **Top port** in the block, the consecutive
3-wire port is assumed to be connected to the bottom port of the encoder. For example,
if you select `A` as the **Top port**, it is
assumed that `B` is connected to the bottom port of the
encoder.

### **Reset mode** — Select the reset mode for reading values `Reset at each sample time` (default) | `No reset` | `Reset by external signal`

Select the reset mode for reading values from the Optical Shaft Encoder.

When you select `Reset by external signal`, an additional
input – `Rst` – is added to the block, which can be connected to a
reset signal.

The different reset modes this block supports are as follows:

- `No reset` – The measurement value is not reset and the
  block outputs the total ticks of rotation.

  For example, in the table below at T = 1, the encoder moves a tick count of 20
  in anti-clockwise direction and therefore the output is 20. Between T = 1 and T = 2,
  the encoder moves a tick count of 10.

  Therefore, the tick count is 30 at T = 2 ( 20 from T = 1 and 10 from T = 2). In
  this reset mode, the output at any time instant is a cumulative sum of the previous
  count and the current count.
- `Reset at each sample time`  – For each sample period,
  the block outputs the measurement value and then resets it to 0.

  For example, in the table below, at T = 1, the encoder moves a tick count of 20
  in anti-clockwise direction and therefore the output is 20. Between T = 1 and T = 2,
  the encoder moves a tick count of 10 and therefore the output is 10. In this reset
  mode, the output is the tick count at a particular time instant.
- `Reset by external signal`  – The measurement value is
  reset to 0 based on the block input value. When you send a value other than 0 to the
  block input, the measurement value is reset to 0. For each sample period, the block
  outputs the measurement value since the last reset.

  For example in the table below, when the external signal is 0, the output is
  based on ‘No reset’ mode and when the external signal is non-zero, the output is
  based on ‘Reset at each sample time’ mode.

### **Sample time** — Interval at which the block reads values `0.2` (default) | positive scalar | -1

Enter the time interval at which the block reads values from the Optical Shaft
Encoder.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model. If you select `Reset by external signal`
option in **Reset mode** parameter, the **Sample
time** parameter is hidden and the value is inherited (Sample time =
-1).

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Represent connected Optical Shaft Encoder and read relative position of motor shaft in ticks

The Optical Shaft Encoder block represents an Optical Shaft Encoder that is
connected to the 3-wire ports of VEX EDR V5 Robot Brain, and reads the relative position of
the motor shaft in ticks. The value increments for anti-clockwise rotation and decrements for
clockwise rotation of the motor shaft.

The tick count also depends on the Reset mode that you selected.
