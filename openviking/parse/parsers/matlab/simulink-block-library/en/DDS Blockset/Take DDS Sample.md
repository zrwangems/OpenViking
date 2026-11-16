---
type: simulink-block
title: 'Take DDS Sample'
family: 'dds'
product_id: 'dds'
product_name: 'DDS Blockset'
documentation_release: R2025b
official_category: ''
documentation_page: 'takeddssample'
documentation_source_path: 'ref/takeddssample.html'
language: en
---

# Take DDS Sample

## Ports

### Input

### **Port\_1** — Input DDS sample scalar | vector | matrix

Receives samples from the DDS network. Samples are converted to signals that can
be used within the Simulink environment. The conversion preserves the value and data type of the
original DDS sample.

**Data Types:** `bus`
### Output

### **Port\_S** — Show whether a DDS sample was received scalar

Shows whether a sample was received successfully from the DDS network. If a sample
was received successfully the block outputs 1, otherwise it outputs 0.

#### Dependencies

To enable this port, select the check box labeled **Show receive
status**.

**Data Types:** `double`

### **Port\_1** — Output signal scalar | vector | matrix

Converted signal that can be used in the Simulink environment.

**Data Types:** `bus`

## Parameters

### **Show receive status** — Show whether a DDS sample was received `off` (default) | `on`

Select this parameter to show whether a sample was received from the DDS network. If
a sample was received successfully the block outputs 1, otherwise it outputs 0.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowQueueStatus` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'off'` |

### **Connect to live network** — Connect DDS simulation to live network `off` (default) | `on`

*Since R2025a*

Select this parameter to connect to a live DDS network during simulation. When
**Connect to live network** is selected:

- The block image changes.

  Take DDS Sample block with Connect to live network enabled.
- During simulation, the block connects to a live DDS network based on the model
  setup, reads DDS messages from the defined topic, and provides the subscriber
  sample data for processing in the Simulink model algorithm.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ConnectToLive` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'off'` |

## Libraries

DDS Blockset

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Code generation of DDS blocks requires an Embedded Coder license.

## Version History

**Introduced in R2021a**

### R2025a: Added support for connecting to DDS network during simulation

You can configure your DDS application model to subscribe to and publish topics directly
to a live DDS network during simulation. Select the block parameter **Connect to live network** to enable communication between the simulation and the
DDS network.

## Description

Receive data samples from DDS network

The DDS Blockset provides Take DDS Sample and Write DDS Sample
blocks to help model DDS applications. The Take DDS Sample block receives
samples from the DDS network and converts them to signals that can be used in the Simulink® environment. The Write DDS Sample block takes signals from the
Simulink environment and converts them to samples to send data into the DDS network.
These blocks are preconfigured to be compatible with the DDS network and provide type checking
functionality.

Code generation for DDS Blockset requires an Embedded Coder® license.
