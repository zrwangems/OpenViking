---
type: simulink-block
title: 'Event Send'
family: 'autosar'
product_id: 'autosar'
product_name: 'AUTOSAR Blockset'
documentation_release: R2025b
official_category: 'Adaptive Software Component Modeling / Component Development'
documentation_page: 'eventsend'
documentation_source_path: 'ref/eventsend.html'
language: en
---

# Event Send

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

The input port for the Event Send block to receive inputs of any
type that AUTOSAR Blockset supports.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus`
### Output

### **Port\_1** — Output event scalar | vector | matrix

The output port for the Event Send block to output an event.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus`

## Parameters

Not documented in R2025b.

## Libraries

AUTOSAR Blockset / Adaptive Platform / Signal Routing

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019a**

## Description

Convert input signal to event

At the top level of an AUTOSAR adaptive model, use the Event
Receive and Event Send blocks to set up event-based
communication.

- After each root inport, add an Event Receive block which converts an
  input event to a signal, while preserving the signal values and data type.
- Before each root outport, add an Event Send block which converts an
  input signal to an event, while preserving the signal values and data type.

Event Send blocks do not support row-major code generation.
