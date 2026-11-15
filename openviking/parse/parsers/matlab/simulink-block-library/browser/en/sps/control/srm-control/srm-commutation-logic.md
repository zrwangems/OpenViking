---
type: simulink-block
title: 'SRM Commutation Logic'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / SRM Control\u200b'
documentation_page: 'srmcommutationlogic'
documentation_source_path: 'ref/srmcommutationlogic.html'
language: en
---

# SRM Commutation Logic

## Ports

### Input

### **theta** — Phase angle scalar

Phase angle, *θph*, in the
interval [0, *β* ].

**Data Types:** `single` | `double`

### **thetaON** — Switch-on angle scalar

Lower threshold for turning on the switch.

**Data Types:** `single` | `double`

### **thetaOFF** — Switch-off angle scalar

Upper threshold for turning off the switch.

**Data Types:** `single` | `double`
### Output

### **abcOnOff** — Commutation signal vector

Commutation signal for each phase: `1` for the switch-on condition and
`0` for switch-off condition

**Data Types:** `single` | `double`

## Parameters

### **Torque capability angle (rad)** — Torque angle `pi/2` (default)

The torque production capability of one rotor pole, in radians.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

## Libraries

Simscape / Electrical / Control / SRM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Commutation logic for switched reluctance machines

The SRM Commutation Logic block provides a logic signal for the
Switched Reluctance
Machine (SRM) block. The signal indicates when to switch the supply
for each phase on and off.

The commutation signal for each phase is:

- `1` if *θon* ≤
  *θph* ≤
  *θoff*.
- `0` if *θph* <
  *θon*.
- `0` if *θph* >
  *θoff*.

where:

- *θph* is the phase angle in the
  interval [0,*β* ].
- *β* is the torque capability angle.
- *θon* is the switch-on
  angle.
- *θoff* is the switch-off
  angle.
