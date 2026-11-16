---
type: simulink-block
title: 'Analog Output'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'analogoutput'
documentation_source_path: 'nucleo/ref/analogoutput.html'
language: en
---

# Analog Output

## Ports

### Input

### **Port\_1** — Voltage of analog output pin scalar

If the generated voltage equals the ground voltage, the block emits
`0`. If the generated voltage equals the analog
reference voltage, the block emits `1`.

## Parameters

### **Pin** — Pin name of the analog output

Specify the digital pin.

To open the pin mapping table, click **View pin
map**.

Make sure to assign different pin name to the different blocks of your
model.

Apart from the pins names mentioned in the pin mapping table, there are
other alternate pin names `(Px_y_ALTz)` that can be used to
access other hardware peripherals connected to the same pin. To know more,
refer to .

The alternate pin names are only applicable for Simulink®
Coder™ Support Package for STMicroelectronics® Nucleo Boards and Discovery boards.

## Libraries

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Generate voltage on the specified analog output pin in volt (V)

The Analog Output block generate voltage on the specified analog out
pin in volt (V) on the hardware. The block accepts normalized decimal values in the
range `0` – `1`.
