---
type: simulink-block
title: 'PassThrough'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'passthrough'
documentation_source_path: 'ref/passthrough.html'
language: en
---

# PassThrough

## Ports
```yaml
ports:
- name: WaveIn
  summary: Input baseband signal scalar | vector
  direction: input
  data_types: double
- name: WaveOut
  summary: Unchanged output voltage scalar | vector
  direction: output
  data_types: double
```

### Input

### **WaveIn** — Input baseband signal scalar | vector

Input baseband signal, can be a sample-by-sample signal specified as a scalar, or
an impulse response vector signal.

**Data Types:** `double`
### Output

### **WaveOut** — Unchanged output voltage scalar | vector

Unchanged output voltage. The PassThrough block does not modify the
input voltage in any way and returns the same output as the input.

**Data Types:** `double`
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

SerDes Toolbox / Datapath Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Propagates baseband signal without modification

The PassThrough block passes the input signal without any modification.
This block is used as a place holder within a SerDes system and as a template for
user-authored blocks for use in SerDes Toolbox™.
