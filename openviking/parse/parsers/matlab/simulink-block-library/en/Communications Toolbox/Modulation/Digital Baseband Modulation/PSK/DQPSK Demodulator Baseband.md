---
type: simulink-block
title: 'DQPSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PSK'
documentation_page: 'dqpskdemodulatorbaseband'
documentation_source_path: 'ref/dqpskdemodulatorbaseband.html'
language: en
---

# DQPSK Demodulator Baseband

## Ports

Not documented in R2025b.

## Parameters

Not documented in R2025b.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Demodulate DQPSK-modulated data

The DQPSK Demodulator Baseband block demodulates a signal that was modulated using the
differential quadrature phase shift keying method. The input is a baseband representation of
the modulated signal.

The input must be a discrete-time complex signal. The output depends on the phase
difference between the current symbol and the previous symbol. The first integer (or binary
pair, if you set the **Output type** parameter to
`Bit`) at the block output is the initial condition of zero because
there is no previous symbol.

This block accepts either a scalar or column vector input signal. For information about
the data types each block port supports, see Supported Data Types.

### Outputs and Constellation Types

When you set **Output type** parameter to
`Integer`, the block maps a phase difference of

θ + πm/2

to *m*, where θ represents the **Phase rotation**
parameter and *m* is 0, 1, 2, or 3.

When you set the **Output type** parameter to
`Bit`, then the output contains pairs of binary values. The
reference page for the DQPSK Modulator Baseband block shows which phase
differences map to each binary pair, for the cases when the **Constellation
ordering** parameter is either `Binary` or
`Gray`.
