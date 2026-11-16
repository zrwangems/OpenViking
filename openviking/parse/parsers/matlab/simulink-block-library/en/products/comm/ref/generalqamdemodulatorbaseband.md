---
type: simulink-block
title: 'General QAM Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Amplitude Modulation'
documentation_page: 'generalqamdemodulatorbaseband'
documentation_source_path: 'ref/generalqamdemodulatorbaseband.html'
language: en
---

# General QAM Demodulator Baseband

## Ports

Not documented in R2025b.

## Parameters

**Signal constellation**
:   A real or complex vector that lists the
    constellation points.

**Output type**
:   Determines whether the block produces
    integers or binary representations of
    integers.

    If you set this parameter to
    `Integer`, the block
    produces integers.

    If you set this parameter to
    `Bit`, the block produces
    a group of K bits, called a *binary
    word*, for each symbol, when
    **Decision type** is set to
    `Hard decision`. If
    **Decision type** is set to
    `Log-likelihood ratio` or
    `Approximate log-likelihood
    ratio`, the block outputs bitwise LLR and
    approximate LLR, respectively.

**Decision type**
:   Specifies the use of hard decision, LLR, or approximate LLR
    during demodulation. For more information, see Hard- vs. Soft-Decision Demodulation.

    To enable this parameter, set **Output type**
    to `Bit`.

**Variance source**
:   When you set this parameter to `Dialog`, you
    can then specify the noise variance in the
    **Variance** parameter. When you set this
    option to `Port`, a port appears on the block
    through which the noise variance can be input.

    To enable this parameter, set **Decision type**
    to `Approximate log-likelihood ratio` or
    `Log-likelihood ratio`.

**Variance**
:   This parameter appears when the **Variance
    source** is set to `Dialog` and
    specifies the noise variance in the input signal. This parameter
    is tunable in normal mode, Accelerator mode, and Rapid
    Accelerator mode. This parameter is nontunable for fixed-point
    inputs.

    If you use the Simulink®
    Coder™ rapid simulation (RSIM) target to build an RSIM
    executable, then you can tune the parameter without recompiling
    the model. This is useful for Monte Carlo simulations in which
    you run the simulation multiple times (perhaps on multiple
    computers) with different amounts of noise.

    The
    exact LLR algorithm computes exponentials using finite precision arithmetic. For computations
    involving very large positive or negative magnitudes, the exact LLR algorithm yields:

    - `Inf` or `-Inf` if the noise variance is a very
      large value
    - `NaN` if the noise variance and signal power are both very small
      values

    The approximate LLR algorithm does not compute exponentials. You can avoid
    `Inf`, `-Inf`, and `NaN` results by using
    the approximate LLR algorithm.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

- When using code generation, the
  **Variance** parameter is
  nontunable for fixed-point inputs.

## Version History

**Introduced before R2006a**

## Description

Demodulate QAM-modulated data

The General QAM Demodulator Baseband block
demodulates a signal that was modulated using
quadrature amplitude modulation. The input is a
baseband representation of the modulated
signal.

The input must be a discrete-time complex
signal. The **Signal constellation** parameter defines the
constellation by listing its points in a length-*M* vector of
complex numbers. The block maps the *m*th point in the
**Signal constellation** vector to the integer
*m*-1.

This block accepts a scalar or column vector
input signal. For information about the data types
each block port supports, see the Supported Data Types table on this page.
