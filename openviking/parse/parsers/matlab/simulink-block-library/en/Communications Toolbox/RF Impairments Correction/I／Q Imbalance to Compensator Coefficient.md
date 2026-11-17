---
type: simulink-block
title: 'I/Q Imbalance to Compensator Coefficient'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments Correction'
documentation_page: 'iqimbalancetocompensatorcoefficient'
documentation_source_path: 'ref/iqimbalancetocompensatorcoefficient.html'
language: en
---

# I/Q Imbalance to Compensator Coefficient

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

**Introduced in R2014b**

## Description

Converts amplitude and phase imbalance into I/Q compensator coefficient

The I/Q Imbalance to Compensator Coefficient block returns a complex
coefficient to compensate for amplitude and phase imbalance.

This block has an amplitude imbalance input port and a phase imbalance input port,
where the amplitude imbalance is a real number expressed in dB and the phase imbalance
is a real number expressed in degrees. The imbalance inputs are vectors. The complex
coefficients are returned from a single output port.
