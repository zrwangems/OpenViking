---
type: simulink-block
title: 'BLDC Commutation Logic'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / BLDC Control\u200b'
documentation_page: 'bldccommutationlogic'
documentation_source_path: 'ref/bldccommutationlogic.html'
language: en
---

# BLDC Commutation Logic

## Ports

### Input

### **Hall** — Hall sensor vector

Hall sensor data.

**Data Types:** `single` | `double`

### **Direction** — Motor direction scalar

Direction of motor rotation.

**Data Types:** `single` | `double`
### Output

### **abc** — Motor phase vector

Motor phase indicated by the commutation logic.

**Data Types:** `single` | `double`

## Parameters

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | positive scalar

Time, in s, between consecutive block executions. During
execution, the block produces outputs and, if appropriate, updates its internal state.
For more information, see What Is Sample Time? and Specify Sample Time.

If this block is inside a triggered subsystem, inherit the
sample time by setting this parameter to `-1`. If this block is in a
continuous variable-step model, specify the sample time explicitly using a positive
scalar.

## Libraries

Simscape / Electrical / Control / BLDC Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Switch-commutation logic for brushless DC motors

The BLDC Commutation Logic block implements a commutation logic for brushless
DC motors as part of this control algorithm.

The commutation logic is based on the Hall signals as summarized in this table.

| Hall Sensors | | | Motor Phases | | |
| --- | --- | --- | --- | --- | --- |
| Hall a | Hall b | Hall c | Phase a | Phase b | Phase c |
| 0 | 0 | 0 | 0 | 0 | 0 |
| 1 | 1 | 0 | 0 | 1 | -1 |
| 0 | 1 | 0 | -1 | 1 | 0 |
| 0 | 1 | 1 | -1 | 0 | 1 |
| 0 | 0 | 1 | 0 | -1 | 1 |
| 1 | 0 | 1 | 1 | -1 | 0 |
| 1 | 0 | 0 | 1 | 0 | -1 |
| 1 | 1 | 1 | 0 | 0 | 0 |
