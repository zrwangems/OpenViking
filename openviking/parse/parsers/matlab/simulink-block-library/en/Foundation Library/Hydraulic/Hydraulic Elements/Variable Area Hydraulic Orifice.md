---
type: simulink-block
title: 'Variable Area Hydraulic Orifice'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'variableareahydraulicorifice'
documentation_source_path: 'ref/variableareahydraulicorifice.html'
language: en
---

# Variable Area Hydraulic Orifice

## Ports
```yaml
ports: []
```

The block has the following ports:

`A`
:   Hydraulic conserving port associated with the orifice inlet.

`B`
:   Hydraulic conserving port associated with the orifice outlet.

`AR`
:   Physical signal port that provides the value of the orifice area.
## Parameters
```yaml
parameters: []
```

**Flow discharge coefficient**
:   Semi-empirical parameter for orifice capacity characterization. Its value
    depends on the geometrical properties of the orifice, and usually is
    provided in textbooks or manufacturer data sheets. The default value is
    `0.7`.

**Minimum area**
:   Leakage area of the completely closed orifice. If the input signal falls
    below this level (for example, turns negative), the area is saturated to
    this value. The parameter value must be greater than zero. The default value
    is `1e-12` m^2.

**Laminar transition specification**
:   Select how the block transitions between the laminar and turbulent
    regimes:

    - `Pressure ratio` — The transition
      from laminar to turbulent regime is smooth and depends on the value
      of the **Laminar flow pressure ratio** parameter.
      This method provides better simulation robustness.
    - `Reynolds number` — The transition
      from laminar to turbulent regime is assumed to take place when the
      Reynolds number reaches the value specified by the
      **Critical Reynolds number** parameter.

**Laminar flow pressure ratio**
:   Pressure ratio at which the flow transitions between laminar and turbulent
    regimes. The default value is `0.999`. This parameter is
    visible only if the **Laminar transition specification**
    parameter is set to `Pressure ratio`.

**Critical Reynolds number**
:   The maximum Reynolds number for laminar flow. The value of the parameter
    depends on the orifice geometrical profile. You can find recommendations on
    the parameter value in hydraulics textbooks. The default value is
    `12`, which corresponds to a round orifice in thin
    material with sharp edges. This parameter is visible only if the
    **Laminar transition specification** parameter is set
    to `Reynolds number`.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009b**

### R2023a: To be removed

The Hydraulic library will be removed in a future release. Use the Isothermal Liquid library
instead. Blocks in the Isothermal Liquid library provide increased accuracy, usability, and
numerical performance.

For more information on updating your models, see Upgrading Hydraulic Models to Use Isothermal Liquid Blocks.

## Description

(To be removed) Hydraulic variable orifice created by cylindrical spool and sleeve

The Variable Area Hydraulic Orifice block models a variable orifice
created by a cylindrical sharp-edged spool and a variable-area slot in a sleeve. The
area of the orifice is expected to be computed outside the block and imported via the AR
physical signal connection. The **Minimum area** parameter specifies
the minimum orifice area value. If the input signal falls below this level (for example,
turns negative), the area is saturated to this value. The flow rate through the orifice
is proportional to the orifice area and the pressure differential across the orifice.

The flow rate is determined according to the following equations:

q=CD⋅A2ρ⋅p(p2+pcr2)1/4

p=pA−pB

where

|  |  |
| --- | --- |
| *q* | Flow rate |
| *p* | Pressure differential |
| *p*A, *p*B | Gauge pressures at the block terminals |
| *C*D | Flow discharge coefficient |
| *A* | Orifice passage area |
| *ρ* | Fluid density |
| *p*cr | Minimum pressure for turbulent flow, when the block transitions from laminar to turbulent regime |

The minimum pressure for turbulent flow,
*p*cr, is calculated according to the laminar
transition specification method:

- By pressure ratio — The transition from laminar to turbulent regime is
  defined by the following equations:

  *p*cr =
  (*p*avg +
  *p*atm)(1 –
  *B*lam)

  *p*avg =
  (*p*A +
  *p*B)/2

  where

  |  |  |
  | --- | --- |
  | *p*avg | Average pressure between the block terminals |
  | *p*atm | Atmospheric pressure, 101325 Pa |
  | *B*lam | Pressure ratio at the transition between laminar and turbulent regimes (**Laminar flow pressure ratio** parameter value) |
- By Reynolds number — The transition from laminar to turbulent regime is
  defined by the following equations:

  pcr=ρ2(Recr⋅νCD⋅DH)2

  DH=4Aπ

  where

  |  |  |
  | --- | --- |
  | *D*H | Orifice hydraulic diameter |
  | *ν* | Fluid kinematic viscosity |
  | *Re*cr | Critical Reynolds number (**Critical Reynolds number** parameter value) |

The block positive direction is from port A to port B. This means that the flow rate
is positive if it flows from A to B and the pressure differential is determined as p=pA−pB.
