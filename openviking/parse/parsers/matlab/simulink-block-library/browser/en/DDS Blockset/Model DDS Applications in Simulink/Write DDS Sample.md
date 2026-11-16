---
type: simulink-block
title: 'Write DDS Sample'
family: 'dds'
product_id: 'dds'
product_name: 'DDS Blockset'
documentation_release: R2025b
official_category: 'Model DDS Applications in Simulink'
documentation_page: 'writeddssample'
documentation_source_path: 'ref/writeddssample.html'
language: en
---

# Write DDS Sample

## Ports

### Input

### **Port\_Enable** — External enable signal scalar

Enables the block to send a sample into the DDS network. For input values greater
than 0 send is enabled. For input values less than or equal to 0 send is
disabled.

#### Dependencies

To display this port, select the check box labeled **Show enable
port**.

**Data Types:** `double`

### **Port\_1** — Input signal scalar | vector | matrix

Signal in Simulink environment. Signals are converted to samples that applications use to
send data into the DDS network. The conversion preserves the value and data type of
the original signal.

**Data Types:** `bus`
### Output

### **Port\_1** — Output DDS sample scalar | vector | matrix

Sends samples into the DDS network.

**Data Types:** `bus`

## Parameters

### **Show enable port** — Display the enable port `off` (default) | `on`

Select this parameter to display enable port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowEnablePort` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'off'` |

### **Connect to live network** — Connect DDS simulation to live network `off` (default) | `on`

*Since R2025a*

Select this parameter to connect to a live DDS network during simulation. When
**Connect to live network** is selected:

- The block image changes.

  Write DDS Sample block with Connect to live network enabled.
- During simulation, the block connects to a live DDS network based on the model
  setup and writes DDS messages from the defined topic.

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

Send data samples to DDS network

The DDS Blockset Library provides Take DDS Sample and Write DDS
Sample blocks to help model DDS applications. The Take DDS Sample
block receives samples from the DDS network and converts them to signals that can be used in
the Simulink® environment. The Write DDS Sample block converts signals from the
Simulink environment to samples to send data into the DDS network. These blocks are
preconfigured to be compatible with the DDS network and provide type checking
functionality.

Code generation for DDS Blockset requires an Embedded Coder® license.
