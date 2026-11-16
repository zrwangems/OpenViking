---
type: simulink-block
title: 'Send'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Messages & Events'
documentation_page: 'send'
documentation_source_path: 'slref/send.html'
language: en
---

# Send

## Ports

### Input

### **Port\_Enable** — External enable signal scalar

Input port to enable the block to send a message. For any input value
that is greater than `0` send is enabled. For any value
less than or equal to `0`, the send is disabled.

#### Dependencies

To enable this port, select the box labeled **Show enable
port**.

**Data Types:** `double`

### **Port\_1** — Input signal scalar | vector | matrix

This block accepts inputs of any type that Simulink® supports, including enumerated types and converts the
input signal to a message. For more information, see Data Types Supported by Simulink.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### Output

### **Port\_1** — Output message scalar | vector | matrix

The block outputs a message with constant priority
`20`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

## Parameters

### **Show enable port** — Display the enable port `off` (default) | `on`

Select this check box to display enable port. For any input value that is
greater than `0` send is enabled. For any value less than
or equal to `0`, the send is disabled.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowEnablePort` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

## Libraries

Simulink / Messages & Events SimEvents

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

**Note**

Send blocks do not support row-major code generation.

## Version History

**Introduced in R2016a**

## Description

Create and send message

The Send block reads the value of an input signal, and sends a message
that carries this value. In message-based communication, a message is a discrete-item of
interest that carry data of any type that Simulink supports. Send and
Message Send blocks are identical blocks.
