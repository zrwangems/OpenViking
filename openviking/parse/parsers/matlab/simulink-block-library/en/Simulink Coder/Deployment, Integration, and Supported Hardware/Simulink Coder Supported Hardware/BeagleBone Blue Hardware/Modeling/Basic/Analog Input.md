---
type: simulink-block
title: 'Analog Input'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Basic'
documentation_page: 'analoginput'
documentation_source_path: 'beagleboneblue/ref/analoginput.html'
language: en
---

# Analog Input

## Ports

### Output

### **Port\_1** — Voltage of analog input pin scalar

Measure the voltage of an analog pin relative to the analog input reference
voltage on the BeagleBone® Blue hardware. If the measured voltage equals the ground voltage, the
block outputs `0` in raw mode, and `0` in volt mode.
If the measured voltage equals the analog reference voltage, the block outputs
`4096` in raw mode, and `1.8` in volt mode.

**Data Types:** `double`

## Parameters

### **Pin** — Pin number of the analog input pin AIN0 (default) | AIN1 | AIN2 | AIN3 | LIPO Battery | DC Jack

Specify the pin number.

To open the pin mapping table,
click **View pin map**.

Make sure to assign different pin
numbers to the different blocks of your model.

### **Mode** — Mode to read output voltage Raw (default) | Volt

- Raw - The block outputs the voltage as a 12-bit digital value.
- Volt - The block outputs the voltage in volts

### **Sample time** — Frequency at which the block reads the input pin value 0.1 (default)

Specify how often this block measures the voltage of the analog input pin, in
seconds.

When you specify this parameter as`-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Basic

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Measure voltage of specified analog input pin

This block measures the voltage of a specified analog input pin. The block outputs the
measurement as a double value.
