---
type: simulink-block
title: 'Data Display'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / User Interface'
documentation_page: 'datadisplay'
documentation_source_path: 'supportpkg/android_ref/datadisplay.html'
language: en
---

# Data Display

## Ports

### Input

### **Port\_1** — Data to display numeric vector

The block inputs one-dimensional vector data of variable length to display on the
application screen of a widget.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Format** — Data format value `Float` (default) | `Integer` | `Scientific` | `Octal` | `Hex`

Select the format of the data value to be displayed on the application screen.

**Note**

For input signals with a data type of `single` or
`double`, the Data Display block cannot display in the
`Octal` and `Hex` formats. In this case, the
**Format** parameter defaults to
`Float`.

### **Precision** — Data precision value `6` (default) | nonnegative scalar

Specify the number of digits after the decimal point to display for a given data
value.

#### Dependencies

- To enable this parameter, set **Format** to
  `Float`.

## Libraries

Simulink Support Package for Android Devices / User Interface

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Display numerical data on device screen

Use the Data Display block to display numerical data on the application
screen of a widget. The block label specifies the widget label.
