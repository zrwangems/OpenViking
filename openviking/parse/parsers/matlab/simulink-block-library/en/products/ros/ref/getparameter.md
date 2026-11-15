---
type: simulink-block
title: 'Get Parameter'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS Network Access / ROS Network Access in Simulink'
documentation_page: 'getparameter'
documentation_source_path: 'ref/getparameter.html'
language: en
---

# Get Parameter

## Ports

### Output

### **Value** — Parameter value scalar | logical | uint8 array

Parameter value from the ROS network. The value depends on the **Data type** parameter.

### **ErrorCode** — Status of ROS parameter 0 | 1 | 2 | 3

Status of ROS parameter, specified as one of the following:

- **0 —** ROS parameter retrieved successfully. The retrieved value is output in the **Value** port.
- **1 —** No ROS parameter with specified name found. If there is no known value, **Value** is set to the last received value or to **Initial value**.
- **2 —** ROS parameter retrieved, but its type is different than the specified **Data type**. If there is no known value, Value is set to the last received value or to **Initial value**.
- **3 —** For string parameters, the incoming string has been truncated based on the specified length.

### **Length** — Length of string parameter integer

Length of the string parameter, returned as an integer. This length is the number of elements of the `uint8` array or the number of characters in the string that you cast to `uint8`.

**Note**

When getting string parameters from the ROS network, an ASCII value of 13 returns an error due to its incompatible character type.

#### Dependencies

To enable this port, set the **Data type** to `uint8[] (string)`.

## Parameters

### **Source** — Source for specifying the parameter name `Select from ROS network` | `Specify your own`

Source for specifying the parameter name as one of the following:

- `Select from ROS network`
  — Use **Select** to select a parameter name. The **Data type** parameter is set automatically. You must be connected to a ROS network.
- `Specify your own`
  — Enter a parameter name in **Name** and specify its data type in **Data type**. You must match a parameter name exactly.

### **Name** — Parameter name string

Parameter name to get from the ROS network, specified as a string. When **Source** is set to `Select from ROS network`, use **Select** to select an existing parameter. You must be connected to a ROS network to get a list of parameters. Otherwise, specify the parameter and data type.

Parameter name strings must follow the rules of ROS graph names. Valid names have these characteristics:

- The first character is an alpha character ([a-z|A-Z]), tilde (~), or forward slash (/).
- Subsequent characters are alphanumeric ([0-9|a-z|A-Z]), underscores(\_), or forward slashes (/).

### **Data type** — Data type of your parameter double | int32 | boolean | uint8[] (string)

Data type of your parameter, specified as a string. The `uint8[] (string)` enables the **Maximum length** parameter.

**Note**

The `uint8[] (string)` data type is an array of ASCII values corresponding to the characters in a string. When getting string parameters, you can create a MATLAB Function (Simulink) block to compare the string to a desired parameter value. For more information, see ROS Parameters in Simulink.

**Data Types:** `double` | `int32` | `Boolean` | `uint8`

### **Maximum length** — Maximum length of the `uint8` array scalar

Maximum length of the `uint8` array, specified as a scalar. If the parameter string has a length greater than **Maximum length**, the **ErrorCode** output is set to 3.

#### Dependencies

To enable this port, set the **Data type** to `uint8[] (string)`.

### **Initial value** — Default parameter value output double | int32 | boolean | uint8

Default parameter value output from when an error occurs and no valid value has been received from the parameter server. The data type must match the specified **Data type**.

### **Sample time** — Interval between outputs `inf` (default) | scalar

Interval between outputs, specified as a scalar. This default value indicates that the block output never changes. Using this value speeds simulation and code generation by eliminating the need to recompute the block output. Otherwise, the block outputs a new blank message at each interval of `Sample time`.

For more information, see Specify Sample Time (Simulink).

### **Show ErrorCode output port** — Display error code output on | off

To enable error code output, select this parameter. When you clear this parameter, the **ErrorCode** output port is removed from the block. The status options are:

- **0 —** ROS parameter retrieved successfully. The retrieved value is output in the **Value** port.
- **1 —** No ROS parameter with specified name found. If there is no known value, **Value** is set to the last received value or to **Initial value**.
- **2 —** ROS parameter retrieved, but its type is different than the specified **Data type**. If there is no known value, Value is set to the last received value or to **Initial value**.
- **3 —** For string parameters, the incoming string has been truncated based on the specified length.

## Libraries

ROS Toolbox / ROS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Get values from ROS parameter server

The Get Parameter block outputs the value of the specified ROS parameter. The block uses the ROS node of the Simulink® model to connect to the ROS network. This node is created when you run the model and is deleted when the model terminates. If the model does not have a node, the block creates one.

On each sample hit, the block checks the ROS parameter server for the specified ROS parameter and outputs its value.
