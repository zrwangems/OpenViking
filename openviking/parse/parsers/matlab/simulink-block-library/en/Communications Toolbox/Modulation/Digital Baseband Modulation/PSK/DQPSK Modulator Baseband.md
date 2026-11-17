---
type: simulink-block
title: 'DQPSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PSK'
documentation_page: 'dqpskmodulatorbaseband'
documentation_source_path: 'ref/dqpskmodulatorbaseband.html'
language: en
---

# DQPSK Modulator Baseband

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

Modulate using differential quadrature phase shift keying method

The DQPSK Modulator Baseband block modulates using the differential quadrature phase shift
keying method. The output is a baseband representation of the modulated signal.

The input must be a discrete-time signal. For information about the data types each block
port supports, see Supported Data Types.

### Integer-Valued Signals and Binary-Valued Signals

When you set the **Input type** parameter to
`Integer`, the valid input values are 0, 1, 2, and 3. In this
case, the block accepts a scalar or column vector input signal. If the first input is
*m*, then the modulated symbol is

exp(jθ + jπm/2)

where θ represents the **Phase rotation** parameter. If a successive
input is *m*, then the modulated symbol is the previous modulated symbol
multiplied by exp(jθ + jπm/2).

When you set the **Input type** parameter to
`Bit`, the input contains pairs of binary values. In this case,
the block accepts a column vector whose length is an even integer. The following figure
shows the complex numbers by which the block multiples the previous symbol to compute the
current symbol, depending on whether you set the **Constellation ordering**
parameter to `Binary` or `Gray`. The
following figure assumes that you set the **Phase rotation** parameter to Π4; in other cases, the two schematics would be rotated accordingly.

The following figure shows the signal constellation for the DQPSK modulation method when
you set the **Phase rotation** parameter to Π4. The arrows indicate the four possible transitions from each symbol to the
next symbol. The `Binary` and `Gray`
options determine which transition is associated with each pair of input values.

More generally, if the **Phase rotation** parameter has the form Πkfor some integer *k*, then the signal constellation has
2*k* points.
