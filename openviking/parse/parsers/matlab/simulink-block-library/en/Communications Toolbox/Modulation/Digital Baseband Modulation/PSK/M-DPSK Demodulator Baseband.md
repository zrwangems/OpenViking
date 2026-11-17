---
type: simulink-block
title: 'M-DPSK Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PSK'
documentation_page: 'mdpskdemodulatorbaseband'
documentation_source_path: 'ref/mdpskdemodulatorbaseband.html'
language: en
---

# M-DPSK Demodulator Baseband

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

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

Demodulate DPSK-modulated data

The M-DPSK Demodulator Baseband block demodulates a signal that was modulated using
the M-ary differential phase shift keying method. The input is a baseband representation
of the modulated signal. The input and output for this block are discrete-time signals.
This block accepts a scalar-valued or column vector input signal. For information about
the data types each block port supports, see the Supported Data Types table on this page.

The **M-ary number** parameter, M, is the number of possible output
symbols that can immediately follow a given output symbol. The block compares the
current symbol to the previous symbol. The block's first output is the initial condition
of zero (or a group of zeros, if the **Output type** parameter is set
to `Bit`) because there is no previous symbol.

### Integer-Valued Signals and Binary-Valued Signals

If you set the **Output type** parameter to
`Integer`, then the block demodulates a phase
difference of

θ + 2πk/M

to *k*, where θ represents the **Phase
rotation** parameter and *k* represents an integer
between `0` and *M*-1.

When you set the **Output type** parameter to
`Bit`, the block outputs binary-valued signals that represent
integers. The block represents each integer using a group of *K* =
log2(*M*) bits, where *K*
represents the number of bits per symbol. The output vector length must be an integer
multiple of *K*.

In binary output mode, the symbols can be either binary-demapped or Gray-demapped.
The **Constellation ordering** parameter indicates how the block
maps an integer to a corresponding group of *K* output bits. See
the reference pages for the M-DPSK Modulator Baseband and M-PSK Modulator Baseband blocks for details.
