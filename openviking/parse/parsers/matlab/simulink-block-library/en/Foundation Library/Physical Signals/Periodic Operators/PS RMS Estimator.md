---
type: simulink-block
title: 'PS RMS Estimator'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Periodic Operators'
documentation_page: 'psrmsestimator'
documentation_source_path: 'ref/psrmsestimator.html'
language: en
---

# PS RMS Estimator

## Ports
```yaml
ports:
- name: I
  summary: Input physical signal, untyped physical signal
  direction: input
- name: O
  summary: Output physical signal, untyped physical signal
  direction: output
```

### Input

### **I** — Input physical signal, untyped physical signal

Input physical signal. The signal must be periodic.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **O** — Output physical signal, untyped physical signal

Output physical signal.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
## Parameters
```yaml
parameters:
- name: Base frequency
  summary: Periodic signal frequency 60 Hz (default)
  group: ''
```

### **Base frequency** — Periodic signal frequency `60 Hz` (default)

Base frequency of the periodic signal.
## Libraries

Simscape / Foundation Library / Physical Signals / Periodic Operators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

### R2019a: Unit Propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Measure RMS value of periodic signal

The PS RMS Estimator block measures the root mean square
(RMS) value of a periodic signal.

A signal is periodic if it completes a pattern within a measurable time frame, called a
period, and repeats that pattern over identical subsequent periods. The signal base frequency
is the number of periods per second.

The block accepts a physical signal with one or more AC components present. It outputs an
RMS value, where each frequency component is averaged over its time period.

Both the input and the output are physical signals. Untyped physical ports facilitate unit
propagation. The output signal has the same physical unit as the input signal.

To obtain meaningful results, run the simulation for at least one full time period of the
signal.
