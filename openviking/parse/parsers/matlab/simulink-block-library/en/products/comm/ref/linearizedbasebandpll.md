---
type: simulink-block
title: 'Linearized Baseband PLL'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Synchronization and Receiver Design'
documentation_page: 'linearizedbasebandpll'
documentation_source_path: 'ref/linearizedbasebandpll.html'
language: en
---

# Linearized Baseband PLL

## Ports

Not documented in R2025b.

## Parameters

**Lowpass filter numerator**
:   The numerator of the lowpass filter transfer function, represented as a
    vector that lists the coefficients in order of descending powers of
    *s*.

**Lowpass filter denominator**
:   The denominator of the lowpass filter transfer function, represented as a
    vector that lists the coefficients in order of descending powers of
    *s*.

**VCO input sensitivity (Hz/V)**
:   This value scales the input to the VCO and, consequently, the shift from
    the VCO's quiescent frequency.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

### R2024a: Removed

Linearized Baseband PLL has been removed. To design voltage-controlled
oscillators (VCOs) and phase-locked loops (PLLs), use the Phase-Locked Loops (Mixed-Signal Blockset)
blocks.

## Description

(Removed) Implement linearized version of baseband phase-locked loop

The Linearized Baseband PLL block is a feedback control system that automatically
adjusts the phase of a locally generated signal to match the phase of an input signal.
This block uses a baseband model method and simplifies computations by using
*x* to approximate sin(*x*). The baseband PLL
model depends on the amplitude of the incoming signal but does not depend on a carrier
frequency.

This PLL has these three components:

- An integrator used as a phase detector.
- A filter. You specify the filter's transfer function using the
  **Lowpass filter numerator** and **Lowpass filter
  denominator** parameters. Each is a vector that gives the
  respective polynomial's coefficients in order of descending powers of
  *s*.

  To design a filter, you can use functions such as `butter`, `cheby1`, and `cheby2`. The default filter is a
  Chebyshev type II filter whose transfer function arises from the command
  below.

  `[num, den] = cheby2(3,40,100,'s')`
- A voltage-controlled oscillator (VCO). You specify the sensitivity of the VCO
  signal to its input using the **VCO input sensitivity**
  parameter. This parameter, measured in Hertz per volt, is a scale factor that
  determines how much the VCO shifts from its quiescent frequency.

This block accepts a sample-based scalar input signal. The input signal represents the
received signal. The three output ports produce:

- The output of the filter
- The output of the phase detector
- The output of the VCO
