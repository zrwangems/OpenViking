---
type: simulink-block
title: 'LCD Screen'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / ARM Cortex-based VEX Microcontroller / Modeling / LCD'
documentation_page: 'lcdscreen'
documentation_source_path: 'armcortexbasedvexmicrocontroller/ref/lcdscreen.html'
language: en
---

# LCD Screen

## Ports

### Input

### **Bklgt** — Signal to turn the LCD backlight on or off scalar

When you send 0 to this port, the LCD backlight turns off. Otherwise
it turns on.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Val** — Input value scalar

Value to display on the LCD screen.

A maximum of 16 characters are displayed for a combination of label
and its value. Any output on the LCD screen more than 16 characters is
truncated.

#### Dependencies

This port becomes available only when you clear the
**Display only text** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **UART port** — UART port number `1` (default) | `2`

Select the UART port number on the microcontroller to which the LCD
Display Module is connected.

### **Display only text** — Specify if you want to display only the label off (default) | on

- `off`— Display a combination of the label
  and its value on the LCD screen.
- `on`— Display only the label on the LCD
  screen.

  When you select this parameter, the `Val` port is
  not available and the **Precision** parameter is
  hidden.

### **Label** — Label to display Value (default)

Specify a label to display on the LCD screen. The block displays the label
to the left of the input value. For example, if you are displaying the state
of an LCD button, specify `Button:`.

A maximum of 16 characters are displayed for a label. Any output on the
LCD screen more than 16 characters is truncated.

### **Display on line** — LCD line on which to display a label or a combination of label and its value `1` (default) | `2`

Select the line on which to display the label or a combination of the
label and its value.

### **Precision** — Number of digits after decimal point `2` (default) | `0` | `1` | `3` | `4` | `5` | `6`

Select the number of digits after the decimal point to display for an
input value.

#### Dependencies

This parameter appears only when you clear the **Display only
text** parameter.

## Libraries

Simulink Coder Support Package for ARM Cortex-based VEX Microcontroller/LCD

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Display text and numerical value on specified line of LCD screen

The LCD Screen block displays a static label and a value from the block
input on the LCD screen. You can also choose to display only the label and not to
display the value.

A maximum of 16 characters are displayed for a label or a combination of label and its
value. Any output on the LCD screen more than 16 characters is truncated.

For example, if you select only a label to be displayed, the label can have maximum
length of 16 characters. If you select a combination of label and its value, the maximum
length of the characters displayed for both is 16.

Using this block, select a line on which you want to display the label and value, and
then turn the LCD backlight on or off.
