---
type: simulink-block
title: 'IBIS-AMI clock_times'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'ibisamiclock_times'
documentation_source_path: 'ref/ibisamiclock_times.html'
language: en
---

# IBIS-AMI clock_times

## Ports
```yaml
ports:
- name: clockValid
  summary: Update input at clockTime port scalar | vector
  direction: input
  data_types: double | int8
- name: clockTime
  summary: Clock time data array
  direction: input
  data_types: double
```

### Input

### **clockValid** — Update input at clockTime port scalar | vector

Update the input at **clockTime** port, specified as a scalar or
vector. The value at the **clockValid** port results in only one
clock times output per sample.

Each rising edge of the input signal at the **clockValid** port
updates the S function that passes through the **clockTime** port.
Usually this happens once per unit interval (UI).

**Data Types:** `double` | `int8`

### **clockTime** — Clock time data array

Clock time data, specified as an array. Clock time data is passed to the AMI
wrapper code using an S function.

The time value at the **clockTime** port must be half UI before
the actual data sample times.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Enable IBIS-AMI Offset
  summary: Offset clock time values by half UI on (default) | off
  group: ''
```

### **Enable IBIS-AMI Offset** — Offset clock time values by half UI on (default) | off

Offset clock time values by half UI, according to IBIS-AMI specifications.
## Libraries

SerDes Toolbox / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Recover SerDes clock time values from custom DFECDR and CDR

The IBIS-AMI clock\_times block recovers the clock time values of a SerDes
system when you use a custom DFECDR or CDR block instead of the ones provided with the
SerDes Toolbox™. The block recovers the clock time values from the AMI\_GetWave function and
outputs them to the generated IBIS-AMI models.

The output of the IBIS-AMI clock\_times block is two global variables,
`extern double* Rx_clock_times_buf` and `extern int
Rx_clock_times_idx`. The block only creates the variables. You must add them to
your custom code to make them work. Together, the variables implement the
`clock_times` vector as defined in the IBIS 7.0 specifications.
