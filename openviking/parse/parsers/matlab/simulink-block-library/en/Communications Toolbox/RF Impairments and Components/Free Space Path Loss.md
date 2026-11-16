---
type: simulink-block
title: 'Free Space Path Loss'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments and Components'
documentation_page: 'freespacepathloss'
documentation_source_path: 'ref/freespacepathloss.html'
language: en
---

# Free Space Path Loss

## Ports

### Input

### **In1** — Complex signal scalar | column vector

Complex signal, specified as a scalar or column vector.

**Data Types:** `double` | `single`
**Complex Number Support:** Yes
### Output

### **Out1** — Output signal scalar | vector

Output signal, returned as a scalar or column vector. This output is
the same dimension and data type as the input signal.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Mode** — Loss calculation mode `Decibels` (default) | `Distance and Frequency`

Loss calculation mode, specified as one of these options.

- `Decibels` — The loss is specified
  using the **Loss (dB)** parameter.
- `Distance and Frequency` — The loss
  is computed using the **Distance (km)** and
  **Carrier frequency (MHz)**
  parameters.

### **Loss (dB)** — Power loss `10` (default) | scalar

Power loss in decibels, specified as a scalar. The decibel amount shown on
the block icon is rounded for display purposes only.

#### Dependencies

To enable this parameter, set the **Mode** parameter
to `Decibels`.

### **Distance (km)** — Distance between transmitter and receiver `0.100` (default) | scalar

Distance between the transmitter and receiver in kilometers, specified as
a scalar.

#### Dependencies

To enable this parameter, set the **Mode** parameter
to `Distance and Frequency`.

### **Carrier frequency (MHz)** — Carrier frequency `1920` (default) | scalar

Carrier frequency in megahertz, specified as a scalar.

#### Dependencies

To enable this parameter, set the **Mode** parameter
to `Distance and Frequency`.

## Libraries

Communications Toolbox / RF Impairments and Components

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Apply free space path loss to complex signal

The Free Space Path Loss block applies a free space path loss to a complex signal. The block
simulates the loss of signal power due to the distance between the transmitter and
receiver. The **Mode** parameter indicates whether you specify the loss
in decibels or as a computation that is based on distance and the RF signal
frequency.
