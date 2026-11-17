---
type: simulink-block
title: 'Variable Hydraulic Chamber'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Elements'
documentation_page: 'variablehydraulicchamber'
documentation_source_path: 'ref/variablehydraulicchamber.html'
language: en
---

# Variable Hydraulic Chamber

## Ports
```yaml
ports: []
```

The block has the following ports:

`A`
:   Hydraulic conserving port associated with the chamber inlet.

`V`
:   Physical signal port that provides the chamber volume variation.
## Parameters
```yaml
parameters: []
```

**Chamber dead volume**
:   Minimal volume of fluid in the chamber. The default value is
    `1e-4` m^3.

**Specific heat ratio**
:   Gas-specific heat ratio. The default value is
    `1.4`.

 Restricted Parameters

When your model is in Restricted editing mode, you cannot modify the following
parameter:

- **Chamber orientation**

All other block parameters are available for modification.
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

(To be removed) Hydraulic capacity of variable volume with compressible fluid

The Variable Hydraulic Chamber block models fluid compressibility in
variable volume chambers. The fluid is considered to be a mixture of liquid and a small
amount of entrained, nondissolved gas. Use this block together with the
Translational Hydro-Mechanical Converter block.

**Note**

The Variable Hydraulic Chamber block takes into account only the
flow rate caused by fluid compressibility. The fluid volume consumed to create
piston velocity is accounted for in the Translational Hydro-Mechanical
Converter block.

The chamber is simulated according to the following equations (see [1, 2]):

q=V0+VE·dpdt

E=El1+α(papa+p)1/n1+αpa1/nn·(pa+p)n+1nEl

where

|  |  |
| --- | --- |
| *q* | Flow rate due to fluid compressibility |
| *V*0 | Initial volume of fluid in the chamber |
| *V* | Chamber volume change, provided through port V |
| *E* | Fluid bulk modulus |
| *E*l | Pure liquid bulk modulus |
| *p* | Gauge pressure of fluid in the chamber |
| *p*α | Atmospheric pressure |
| *α* | Relative gas content at atmospheric pressure, *α* = *V*G/*V*L |
| *V*G | Gas volume at atmospheric pressure |
| *V*L | Volume of liquid |
| *n* | Gas-specific heat ratio |

The main objective of representing fluid as a mixture of liquid and gas is to
introduce an approximate model of cavitation, which takes place in a chamber if pressure
drops below fluid vapor saturation level. As it is seen in the graph below, the bulk
modulus of a mixture decreases as the gauge pressure approaches zero, thus considerably
slowing down further pressure change. At gauge pressures far above zero, a small amount
of undissolved gas has practically no effect on the system behavior.

For information on how to reproduce this graph, see Constant Volume Hydraulic Chamber.

Cavitation is an inherently thermodynamic process, requiring consideration of
multiple-phase fluids, heat transfers, etc., and as such cannot be accurately simulated
with Simscape™ software. But the simplified version implemented in the block is good
enough to signal if pressure falls below dangerous level, and to prevent computation
failure that normally occurs at negative pressures.

If pressure falls below absolute vacuum (–101325 Pa), the simulation stops and an
error message is displayed.

Port A is a hydraulic conserving port associated with the chamber inlet. Port V is a
physical signal port that provides the chamber volume variation.

The block positive direction is from port A to the reference point. This means that
the flow rate is positive if it flows into the chamber.

### Variables

Use the **Variables** tab to set the priority and initial
target values for the block variables prior to simulation. For more information,
see Set Priority and Initial Target for Block Variables.
