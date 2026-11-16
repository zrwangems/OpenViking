---
type: simulink-block
title: 'Discrete-Time VCO'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Synchronization and Receiver Design'
documentation_page: 'discretetimevco'
documentation_source_path: 'ref/discretetimevco.html'
language: en
---

# Discrete-Time VCO

## Ports

Not documented in R2025b.

## Parameters

**Output amplitude**
:   The amplitude of the output.

**Quiescent frequency (Hz)**
:   The frequency of the oscillator output when the input signal is
    zero.

**Input sensitivity**
:   This value scales the input voltage and, consequently, the shift from the
    **Quiescent frequency** value. The units of
    **Input sensitivity** are Hertz per volt.

**Initial phase (rad)**
:   The initial phase of the oscillator in radians.

**Sample time**
:   The calculation sample time.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2024a: To be removed

Discrete-Time VCO will be removed. To design voltage-controlled
oscillators (VCOs) and phase-locked loops (PLLs), use the Phase-Locked Loops (Mixed-Signal Blockset)
blocks.

## Description

(To be removed) Implement voltage-controlled oscillator (VCO) in discrete time

The Discrete-Time VCO block generates a signal whose frequency shift from the
**Quiescent frequency** parameter is proportional to the input
signal. The input signal is interpreted as a voltage. If the input signal is
*u*(*t*), then the output signal is

y(t)=Accos(2πfct+2πkc∫0tu(τ)dτ+φ)

where *A*c is the **Output
amplitude**, *f*c is the
**Quiescent frequency**,
*k*c is the **Input
sensitivity**, and φ is the **Initial phase**

This block uses a discrete-time integrator to interpret the equation above.

This block accepts a scalar-valued input signal with a data type of
`single` or `double`. The output signal inherits
its data type from the input signal. For code generation, the block supports double
precision only.
