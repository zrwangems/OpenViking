---
type: simulink-block
title: 'Get Parameter'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS 2 Network Access / ROS 2 Network Connection and Exploration'
documentation_page: 'getparameterros2'
documentation_source_path: 'ref/getparameterros2.html'
language: en
---

# Get Parameter

## Ports

### Output

### **Value** — Parameter value scalar | array

Parameter value from the ROS 2 network, returned as a scalar or array. The type
and size of this output depends on the **Data type**
parameter.

**Data Types:** `double` | `int64` | `Boolean` | `uint8[]`

### **Length** — Length of array parameter scalar

Length of the array parameter, returned as an integer scalar. This length is the
number of elements of the array or the number of characters in the string that you
cast to `uint8`.

**Note**

When getting string parameters from the ROS 2 network, an ASCII value of 13
returns an error due to its incompatible character type.

#### Dependencies

To enable this port, set the **Data type** parameter to
`uint8[]`, `double[]` ,
`int64[]` or `boolean[]`.

## Parameters

### **Name** — Parameter name `mynamespace.param` (default) | string

Parameter name to get from the ROS 2 network, specified as a string. Valid parameter
names have these characteristics:

- The first character is an alpha character ([a-z|A-Z]), tilde (~), or forward
  slash (/).
- Subsequent characters are alphanumeric ([0-9|a-z|A-Z]), underscores(\_), or
  forward slashes (/).

### **Data type** — Data type of parameter `double` (default) | `int64` | `boolean` | `uint8[]` | `double[]` | `int64[]` | `boolean[]`

Data type of parameter, specified as a string. Array data types such as
`uint8[]`, `double[]`, `int64[]`
and `boolean[]` enable the **Maximum length**
parameter. If the data type changes during runtime, the block throws a warning.

**Note**

The `uint8[]` data type is an array of ASCII values corresponding
to the characters in a string. When getting string parameters, you can create a MATLAB Function (Simulink) block to compare the
string to a desired parameter value.

### **Maximum length** — Maximum length of array 16 (default) | numeric scalar

Maximum length of the array, specified as a scalar. If the array has a length
greater than **Maximum length**, the block returns a warning.

#### Dependencies

To enable this parameter, set the **Data type** parameter to
`uint8[]`, `double[]`, `int64[]`
or `boolean[]`.

### **Initial value** — Default parameter value output `0.0` (default) | numeric scalar | vector

Default parameter value output for when an error occurs and no valid value is
received from the parameter. The specified value must be a valid value for the specified
**Data type**.

### **Sample time** — Interval between outputs `-1` (default) | numeric scalar

Interval between outputs, specified as a numeric scalar. The default value of
`-1` indicates that the block inherits the output sample time from
the model. Otherwise, the block outputs a new blank message at each interval of
`Sample time`.

For more information, see Specify Sample Time (Simulink).

## Libraries

ROS Toolbox / ROS 2

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Get ROS 2 parameter value

The Get Parameter block outputs the value of the specified ROS 2 parameter
associated with the node of the Simulink® model. Simulink creates this node when you run the model and deletes it when the model
terminates. If the model does not have a parameter, the block creates one.

At the start of the simulation, the block initializes the ROS 2 parameter with the
specified initial value. For each sample hit, the block checks the ROS 2 parameter and outputs
its value.
