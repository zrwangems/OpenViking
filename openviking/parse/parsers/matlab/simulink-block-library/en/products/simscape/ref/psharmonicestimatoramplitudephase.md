---
type: simulink-block
title: 'PS Harmonic Estimator (Amplitude, Phase)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Periodic Operators'
documentation_page: 'psharmonicestimatoramplitudephase'
documentation_source_path: 'ref/psharmonicestimatoramplitudephase.html'
language: en
---

# PS Harmonic Estimator (Amplitude, Phase)

## Ports

### Input

### **I** — Periodic signal, untyped physical signal

Input physical signal. The signal must be periodic.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.
### Output

### **A** — Amplitude of the harmonic signal, untyped physical signal

Output physical signal corresponding to the harmonic amplitude.

### **Phi** — Phase of the harmonic signal, rad physical signal

Output physical signal corresponding to the harmonic phase. Although the physical
output port is untyped, the signal unit is determined by the block equations. When
connecting a PS-Simulink Converter block to this port,
set its **Output signal unit** parameter to `1`, or
to another value commensurate with angular units. For more information, see Angular Units.

## Parameters

### **Base frequency** — Periodic signal frequency `60 Hz` (default)

Base frequency of the periodic signal.

### **Harmonic number** — Number of harmonic `1` (default)

The number of harmonic within the periodic signal. The value must be a positive
integer.

### **Minimum amplitude for phase detection** — Minimum signal amplitude for measuring phase `0.001 1` (default)

The minimum amplitude necessary for measuring the harmonic phase. The parameter unit
must be commensurate with the unit of the input signal. If the harmonic amplitude is
less than this value, the output at port **Phi** is 0.

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

Measure harmonic amplitude and phase of periodic signal

The PS Harmonic Estimator (Amplitude, Phase) block measures
amplitude and phase of a single frequency component (harmonic) of a periodic signal.

A signal is periodic if it completes a pattern within a measurable time frame, called a
period, and repeats that pattern over identical subsequent periods. The signal base frequency
is the number of periods per second.

The block accepts a physical signal with one or more harmonics present. It outputs the
phase and amplitude for the selected harmonic. Untyped physical ports facilitate unit
propagation. The output signal for the amplitude has the same physical unit as the input
signal. The output signal for phase has the unit of radians, or 1. For more information, see
Angular Units.

To obtain meaningful results, run the simulation for at least one full time period of the
signal.
