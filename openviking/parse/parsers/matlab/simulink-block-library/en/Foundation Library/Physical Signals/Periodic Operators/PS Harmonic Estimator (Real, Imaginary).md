---
type: simulink-block
title: 'PS Harmonic Estimator (Real, Imaginary)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Periodic Operators'
documentation_page: 'psharmonicestimatorrealimaginary'
documentation_source_path: 'ref/psharmonicestimatorrealimaginary.html'
language: en
---

# PS Harmonic Estimator (Real, Imaginary)

## Ports

### Input

### **I** — Periodic signal, untyped physical signal

Input physical signal. The signal must be periodic.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **Re** — Real part of the harmonic signal, untyped physical signal

Output physical signal corresponding to the real part of the selected harmonic.

### **Im** — Imaginary part of the harmonic signal, untyped physical signal

Output physical signal corresponding to the imaginary part of the selected
harmonic.

## Parameters

### **Base frequency** — Periodic signal frequency `60 Hz` (default)

Base frequency of the periodic signal.

### **Harmonic number** — Number of harmonic `1` (default)

The number of harmonic within the periodic signal. The value must be a positive
integer.

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

Measure real and imaginary parts of periodic signal harmonic

The PS Harmonic Estimator (Real, Imaginary) block measures
real and imaginary parts of a single frequency component (harmonic) of a periodic signal.

A signal is periodic if it completes a pattern within a measurable time frame, called a
period, and repeats that pattern over identical subsequent periods. The signal base frequency
is the number of periods per second.

The block accepts a physical signal with one or more harmonics present. It outputs the
real and imaginary parts of the signal for the selected harmonic. Untyped physical ports
facilitate unit propagation. The output signals at both ports have the same physical unit as
the input signal.

To obtain meaningful results, run the simulation for at least one full time period of the
signal.
