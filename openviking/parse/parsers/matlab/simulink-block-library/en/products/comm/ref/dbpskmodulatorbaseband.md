---
type: simulink-block
title: 'DBPSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Phase Modulation'
documentation_page: 'dbpskmodulatorbaseband'
documentation_source_path: 'ref/dbpskmodulatorbaseband.html'
language: en
---

# DBPSK Modulator Baseband

## Ports

### Input

### **In** — Input signal scalar | column vector

Input signal, specified as a scalar or vector with element values of
`0` or `1`. For more information,
see Supported Data Types.

This port is unnamed on the block.

**Data Types:** `double` | `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out** — DBPSK-modulated baseband signal scalar | column vector

DBPSK-modulated baseband signal, returned as a complex-valued scalar
or column vector.

This port is unnamed on the block.

**Data Types:** `double` | `single`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Phase rotation (rad)** — Additional phase shift `0` (default) | scalar

Additional phase shift in radians between previous and current
modulated symbols, specified as a scalar. This value corresponds to the
phase difference between previous and current modulated symbols when the
input is zero.

**Example:** `pi/4`

### **Output data type** — Output data type `double` (default) | `single`

Output data type, specified as `double` or
`single`.

## Libraries

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Modulate using differential binary phase shift keying method

The DBPSK Modulator Baseband block modulates signals using the differential binary
phase shift keying (DBPSK) method. The output is a baseband representation of the
modulated signal. For more information, see Algorithms.
