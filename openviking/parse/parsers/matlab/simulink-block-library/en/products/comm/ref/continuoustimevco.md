---
type: simulink-block
title: 'Continuous-Time VCO'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Synchronization and Receiver Design'
documentation_page: 'continuoustimevco'
documentation_source_path: 'ref/continuoustimevco.html'
language: en
---

# Continuous-Time VCO

## Ports

Not documented in R2025b.

## Parameters

**Output amplitude**
:   The amplitude of the output.

**Quiescent frequency**
:   The frequency of the oscillator output when the input signal is
    zero.

**Input sensitivity**
:   This value scales the input voltage and, consequently, the shift from the
    **Quiescent frequency** value. The units of
    **Input sensitivity** are Hertz per volt.

**Initial phase**
:   The initial phase of the oscillator in radians.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2024a: Removed

Continuous-Time VCO has been removed. To design voltage-controlled
oscillators (VCOs) and phase-locked loops (PLLs), use the Phase-Locked Loops (Mixed-Signal Blockset)
blocks.

## Description

(Removed) Implement voltage-controlled oscillator (VCO)

The Continuous-Time VCO block generates a signal with a frequency shift from
the **Quiescent frequency** parameter that is proportional to the input
signal. The input signal is interpreted as a voltage. If the input signal is
*u*(*t*), then the output signal is

y(t)=Accos(2πfct+2πkc∫0tu(τ)dτ+φ)

where *A*c is the **Output
amplitude** parameter, *f*c is
the **Quiescent frequency** parameter,
*k*c is the **Input
sensitivity** parameter, and φ is the **Initial phase**
parameter.

This block uses a continuous-time integrator to interpret the equation above.

The input and output are both sample-based scalar signals.
