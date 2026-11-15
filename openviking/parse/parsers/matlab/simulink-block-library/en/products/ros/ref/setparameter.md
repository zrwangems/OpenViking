---
type: simulink-block
title: 'Set Parameter'
family: 'ros'
product_id: 'ros'
product_name: 'ROS Toolbox'
documentation_release: R2025b
official_category: 'Network Access / ROS Network Access / ROS Network Connection and Exploration'
documentation_page: 'setparameter'
documentation_source_path: 'ref/setparameter.html'
language: en
---

# Set Parameter

## Ports

### Input

### **Value** — Parameter value scalar | logical | uint8 array

Parameter value from the ROS network. The value depends on the **Data type** parameter.

### **Length** — Length of string parameter integer

Length of the string parameter, specified as an integer. This length is the number of elements of the `uint8` array or the number of characters in the string that you cast to `uint8`.

**Note**

When casting your string parameters to `uint8`, ASCII values 0–31 (control characters) return an error due to their incompatible character type.

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

Data type of your parameter, specified as a string.

**Note**

The `uint8[] (string)` data type is an array of ASCII values corresponding to the characters in a string. When getting string parameters, you can create a MATLAB Function (Simulink) block to compare the string to a desired parameter value. For more information, see ROS Parameters in Simulink.

**Data Types:** `double` | `int32` | `Boolean` | `uint8`

## Libraries

ROS Toolbox / ROS

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Set values on ROS parameter server

The Set Parameter block sets the **Value** input to the specified name on the ROS parameter server. The block uses the ROS node of the Simulink® model to connect to the ROS network. This node is created when you run the model and is deleted when the model terminates. If the model does not have a node, the block creates one.
