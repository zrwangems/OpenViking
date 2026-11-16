---
type: simulink-block
title: 'VGA'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Design and Simulate SerDes Systems / Signal Modification'
documentation_page: 'vga'
documentation_source_path: 'ref/vga.html'
language: en
---

# VGA

## Ports

### Input

### **WaveIn** — Input signal scalar | vector

Input signal to be scaled, specified as a scalar or vector.

**Data Types:** `double`
### Output

### **WaveOut** — Estimated channel output scalar | vector

Estimated channel output, returned as a scalar or vector corresponding to the
input signal.

**Data Types:** `double`

## Parameters

### **Mode** — VGA operating mode `On` (default) | `Off`

VGA operating mode:

- `Off` — VGA is bypassed and the input waveform
  remains unchanged.
- `On` — VGA scales the input waveform according
  to the specified `Gain`.

#### Programmatic Use

- Use `get_param(gcb,'Mode')` to view the current VGA
  **Mode**.
- Use `set_param(gcb,'Mode',value)` to set VGA to a specific
  **Mode**.

### **Gain** — Multiplicative gain used to scale the input waveform `1` (default) | scalar

Multiplicative gain used to scale the input waveform, specified as a unitless
scalar.

#### Programmatic Use

- Use `get_param(gcb,'Gain')` to view the current value of
  **Gain**.
- Use `set_param(gcb,'Gain',value)` to set VGA
  **Gain** to a specific value.

**Data Types:** `double`

#### IBIS-AMI parameters

### **Mode** — Include Mode parameter in IBIS-AMI model on (default) | off

Select to include **Mode** as a parameter in the IBIS-AMI file. If
you deselect **Mode**, it is removed from the AMI files, effectively
hard-coding **Mode** to its current value.

### **Gain** — Include Gain parameter in IBIS-AMI model on (default) | off

Select to include **Gain** as a parameter in the IBIS-AMI file. If
you deselect **Gain**, it is removed from the AMI files, effectively
hard-coding **Gain** to its current value.

## Libraries

SerDes Toolbox / Datapath Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Models a variable gain amplifier

The VGA block scales the amplitude of the input waveform based on a gain
specified by the user.
