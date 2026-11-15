---
type: simulink-block
title: 'ToApp'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Advanced'
documentation_page: 'toapp'
documentation_source_path: 'supportpkg/android_ref/toapp.html'
language: en
---

# ToApp

## Ports

### Input

### **Port\_1** — Data to send to a method `argn` where *n* is the number of arguments

The block inputs data to send to a method in an Android app. This data is received as input by the method specified in the
**Method name** parameter. The number of input ports to
the block depend on the number of input arguments. For example, if you set **Number of arguments** parameter to
`2`, you can pass `arg1` and
`arg2` as input arguments to a method in the Android app.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Method name** — Name of method in Android app `ToAppMethod` (default) | character vector

Enter the name of method in the Android app.

### **Number of arguments** — Number of arguments for method `1` (default) | `2` | `3` | `4` | `5`

Select the number of arguments for the method in the Android app. The number of argument that you select are added as input ports to
the block.

## Libraries

Simulink Support Package for Android Devices / Advanced

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Send data to method of app

Use the ToApp block to send data to a specified method in the Android® app. The method must exist in the default activity. For example, suppose the
block input is `int32(ones(3,1))` and the method name is
`ToAppFcn`. Then, the expected method in the Android app would
be:

```
public void ToAppFcn(int[] inData)
```

where
`inData` is an integer array of three elements.

**Note**

During simulation with no hardware connected, this block does nothing. For more
information, see Block Produces Zeros or Does Nothing in Simulation.
