---
type: simulink-block
title: 'General QAM Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PAM/QAM'
documentation_page: 'generalqammodulatorbaseband'
documentation_source_path: 'ref/generalqammodulatorbaseband.html'
language: en
---

# General QAM Modulator Baseband

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

**Signal constellation**
:   A real or complex vector that lists the constellation points.

**View Constellation**
:   Click **View
    Constellation** on the block mask to visualize a signal constellation for the
    specified block parameters. Before viewing a constellation, apply the parameter settings. For
    more information, see View Constellation of Modulator Block.

**Output data type**
:   Output data type, specified as `double`,
    `single`,
    `fixdt(1,16)`,
    `fixdt(1,16,0)`, `Inherit via back
    propagation`, or `<data type
    expression>`.

    Setting this parameter to

    - `fixdt(1,16)`,
      `fixdt(1,16,0)`, or
      `<data type expression>` enables
      parameters in which you can further specify details.
    - `Inherit via back propagation` sets
      the output data type and scaling to match the following
      block.

    For information about specifying data types, see Data Type Assistant.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Modulate using quadrature amplitude modulation

The General QAM Modulator Baseband block modulates using quadrature amplitude
modulation. The output is a baseband representation of the modulated signal.

The **Signal constellation** parameter defines the constellation by
listing its points in a length-*M* vector of complex numbers. The input
signal values must be integers in the range [0, (*M*-1)]. The block
maps an input integer m to the (m+1)st value in the **Signal
constellation** vector.

This block accepts a scalar or column vector input signal. For information about the
data types each block port supports, see the Supported Data Types table on this page.
