---
type: simulink-block
title: 'FromApp'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Advanced'
documentation_page: 'fromapp'
documentation_source_path: 'supportpkg/android_ref/fromapp.html'
language: en
---

# FromApp

## Ports

### Output

### **Data** — Data returned by method numeric array

The block outputs the data returned by the method specified in the **Method name** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Size** — Size of data returned by method numeric scalar

The block outputs the size of the data returned by the method specified in the
**Method name** parameter.

**Data Types:** `double`

## Parameters

### **Method name** — Name of method `'FromAppMethod'` (default) | character array

Enter the name of method in the Android app.

### **Return type** — Data type element returned by method `uint8` (default) | `int8` | `uint16` | `int16` | `uint32` | `int32` | `single` | `double`

Select the data type of the elements returned by the method specified in the
**Method name** parameter.

### **Data size (N)** — Number of data elements returned by method `32` (default) |

Enter the number of data elements the method returns to the block each time it
runs.

### **Sample time** — Time interval of sampling `0.1` (default) | nonnegative scalar

Specify how often the block reads the method in the Android app.

**Note**

Smaller values for **Sample time** require the processor to
complete the same number of instructions in less time, which can cause task
overruns.

## Libraries

Simulink Support Package for Android Devices / Advanced

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Receive data from method of app

Use the FromApp block to receive data from a method in an Android® app. After code generation is completed, you can modify the generated code to
configure the **Method name**, **Data
type**, and **Data size (N)** parameters to match
those of the method.

For example, consider a method, `public int[] FromAppFcn()`, that sends
three data elements each time it runs, and the data type of those elements is
`int32`. In this case, set these parameter values.

- **Method name** to `FromAppFcn`
- **Data size** to `3`
- **Data type** to `int32`

The method in the Android app must send a data type that this block can accept.

**Note**

During simulation with no hardware connected, this block does nothing. For more
information, see Block Produces Zeros or Does Nothing in Simulation.
