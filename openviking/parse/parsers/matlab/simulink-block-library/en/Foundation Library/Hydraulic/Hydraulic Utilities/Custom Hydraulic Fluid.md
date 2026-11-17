---
type: simulink-block
title: 'Custom Hydraulic Fluid'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Hydraulic / Hydraulic Utilities'
documentation_page: 'customhydraulicfluid'
documentation_source_path: 'ref/customhydraulicfluid.html'
language: en
---

# Custom Hydraulic Fluid

## Ports
```yaml
ports: []
```

The block has one hydraulic conserving port.
## Parameters
```yaml
parameters: []
```

**Fluid density**
:   Density of the working fluid. The default value is 850 kg/m^3.

**Kinematic viscosity**
:   Kinematic viscosity of the working fluid. The default value is 1.8e-5
    m^2/s.

**Bulk modulus at atm. pressure and no gas**
:   Bulk modulus of the working fluid, at atmospheric pressure and with no
    entrapped air. The default value is 8e8 Pa.

**Relative amount of trapped air**
:   Amount of entrained, nondissolved gas in the fluid. The amount is
    specified as the ratio of gas volume at normal conditions to the fluid
    volume in the chamber. Therefore, the parameter value must be less than 1.
    In practice, the relative amount of trapped air is always greater than 0. If
    set to 0, ideal fluid is assumed. The default value is 0.005.

**Absolute pressure below absolute zero in blocks with fluid compressibility**
:   During simulation, the software checks that the absolute pressure does not
    fall below absolute zero. This check is performed only for those blocks in
    the hydraulic circuit where fluid compressibility is important. The value of
    this parameter determines how the block handles the out-of-range assertion
    during simulation:

    - `Error` — If the pressure falls
      below absolute zero, the simulation stops and you get an error
      message. This is the default.
    - `Warning` — If the pressure falls
      below absolute zero, you get a warning but the simulation continues.
      Use this option when modeling systems where cavitation can occur in
      extreme cases.
## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2023a: To be removed

The Hydraulic library will be removed in a future release. Use the Isothermal Liquid library
instead. Blocks in the Isothermal Liquid library provide increased accuracy, usability, and
numerical performance.

For more information on updating your models, see Upgrading Hydraulic Models to Use Isothermal Liquid Blocks.

## Description

(To be removed) Working fluid properties, set by specifying parameter values

The Custom Hydraulic Fluid block lets you specify the type of hydraulic
fluid used in a loop of hydraulic blocks. It provides the hydraulic fluid properties,
such as kinematic viscosity, density, and bulk modulus, for all the hydraulic blocks in
the loop. These fluid properties are assumed to be constant during simulation time.

The Custom Hydraulic Fluid block lets you specify the fluid properties,
such as kinematic viscosity, density, bulk modulus, and relative amount of entrapped
air, as block parameters.

The Custom Hydraulic Fluid block has one port. You can connect it to a
hydraulic diagram by branching a connection line off the main line and connecting it to
the port. When you connect the Custom Hydraulic Fluid block to a
hydraulic line, the software automatically identifies the hydraulic blocks connected to
the particular loop and propagates the hydraulic fluid properties to all the hydraulic
blocks in the loop.

Each topologically distinct hydraulic loop in a diagram requires the properties of the
working fluid to be specified. You can specify these properties by using either a
Custom Hydraulic Fluid block or a Hydraulic Fluid
block, which is available with Simscape™
Fluids™ libraries. If no Hydraulic Fluid block or Custom
Hydraulic Fluid block is attached to a loop, the hydraulic blocks in this
loop use the default fluid, which is equivalent to fluid defined by a Custom
Hydraulic Fluid block with the default parameter values.
