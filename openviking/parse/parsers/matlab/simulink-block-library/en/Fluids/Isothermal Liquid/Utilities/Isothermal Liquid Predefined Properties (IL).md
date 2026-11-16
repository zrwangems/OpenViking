---
type: simulink-block
title: 'Isothermal Liquid Predefined Properties (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Utilities'
documentation_page: 'isothermalliquidpredefinedpropertiesil'
documentation_source_path: 'ref/isothermalliquidpredefinedpropertiesil.html'
language: en
---

# Isothermal Liquid Predefined Properties (IL)

## Ports

### Conserving

### **A** — Connection port isothermal liquid

Isothermal liquid conserving port that connects the block to the network. Connect this
port to any point on an isothermal liquid connection line in a block
diagram. When you connect the Isothermal Liquid
Predefined Properties (IL) block to a network line,
the liquid properties propagate to all blocks in the circuit.

## Parameters

### Liquid

### **Isothermal liquid** — Fluid choice `Water` (default) | `Seawater (MIT model)` | `Ethylene glycol and water mixture` | `Propylene glycol and water mixture` | `Glycerol and water mixture` | `Aviation fuel Jet-A` | `Diesel fuel` | `SAE 5W-30` | `SAE 30 Oil` | `SAE 50 Oil` | `10W Oil` | `30W Oil` | `50W Oil` | `Skydrol LD-4` | `Skydrol 500B-4` | `Skydrol 5` | `HyJet-IVA` | `Fluid MIL-F-83282` | `Fluid MIL-F-5606` | `Fluid MIL-F-87257` | `ATF (Dexron III)` | `ISO VG 22 (ESSO UNIVIS N 22)` | `ISO VG 32 (ESSO UNIVIS N 32)` | `ISO VG 46 (ESSO UNIVIS N 46)` | `ISO VG 68` | `Brake fluid DOT 3` | `Brake fluid DOT 4` | `Brake fluid DOT 5` | `Gasoline`

Choice of working fluid in the system.

**Note**

For these fluids, the block calculates the fluid properties by interpolating
experimental data:

- `Water`
- `Seawater (MIT model)`
- `Ethylene glycol and water
  mixture`
- `Propylene glycol and water
  mixture`
- `Glycerol and water
  mixture`
- `Aviation fuel Jet-A`
- `Diesel fuel`
- `SAE 5W-30`

For the remaining fluids, the block uses
approximations to calculate the fluid properties. For these
approximated fluids, the block may output unexpected results at
extreme temperatures or if the fluid deviates significantly from
atmospheric pressure.

### **Dissolved salt mass fraction (salinity)** — Salt concentration `3.5e-3` (default) | positive scalar between (0, 0.12]

Concentration of salt in water by mass.

#### Dependencies

To enable this parameter, set **Isothermal
liquid** to `Seawater
(MIT)`.

### **Concentration type** — Concentration by mass or volume `Volume fraction` (default) | `Mass fraction`

Whether the solute is measured in water by mass or volume.

#### Dependencies

To enable this parameter, set **Isothermal
liquid** to:

- `Ethylene glycol and water
  mixture`.
- `Propylene glycol and water
  mixture`.

### **Ethylene glycol volume fraction** — Ethylene glycol concentration by volume `0.1` (default) | positive scalar between (0, 1.0]

Fraction of ethylene glycol in water, by volume.

#### Dependencies

To enable this parameter, set **Isothermal
liquid** to `Ethylene glycol and water
mixture` and **Concentration
type** to `Volume
fraction`.

### **Ethylene glycol mass fraction** — Ethylene glycol concentration by mass `0.1` (default) | positive scalar between (0, 0.6]

Fraction of ethylene glycol in water, by mass.

#### Dependencies

To enable this parameter, set **Isothermal
liquid** to `Ethylene glycol and water
mixture` and **Concentration
type** to `Mass
fraction`.

### **Isothermal bulk modulus at atmospheric pressure (no entrained air)** — Bulk modulus `2.1791 GPa` (default) | positive scalar

Solution bulk modulus at atmospheric pressure.

#### Dependencies

To enable this parameter, set **Isothermal
liquid** to:

- `Ethylene glycol and water
  mixture`.
- `Propylene glycol and water
  mixture`.
- `Glycerol and water
  mixture`.

### **Minimum valid pressure** — Lower pressure limit `0.01` (default) | positive scalar

Lower pressure limit during simulations. The **Atmospheric
pressure** must greater than or equal to the
**Minimum valid pressure**.

#### Dependencies

To enable this parameter, set **Isothermal
liquid** to:

- `Ethylene glycol and water
  mixture`.
- `Propylene glycol and water
  mixture`.
- `Glycerol and water
  mixture`.

### **Propylene glycol volume fraction** — Propylene glycol concentration by volume `0.1` (default) | positive scalar between [0.1, 0.6]

Fraction of propylene glycol in water, by volume.

#### Dependencies

To enable this parameter, set **Isothermal
liquid** to `Propylene glycol and water
mixture` and **Concentration
type** to `Volume
fraction`.

### **Propylene glycol mass fraction** — Propylene glycol concentration by mass `0.1` (default) | positive scalar between (0, 0.6]

Fraction of propylene glycol in water, by mass.

#### Dependencies

To enable this parameter, set **Isothermal
liquid** to `Propylene glycol and water
mixture` and **Concentration
type** to `Mass
fraction`.

### **Glycerol mass fraction** — Glycerol concentration by mass `0.1` (default) | positive scalar between (0, 0.6]

Fraction of glycerol in water, by mass.

#### Dependencies

To enable this parameter, set **Isothermal
liquid** to `Glycerol and water
mixture`.

### **System temperature** — Network temperature `300 K` (default) | positive scalar

Isothermal liquid network temperature.

### **Viscosity derating factor** — Viscosity correction factor `1` (default) | positive scalar

Correction factor for fluids diverging from the clean fluid standard
viscosity.

### **Atmospheric pressure** — User-defined environmental pressure `0.101325 MPa` (default) | positive scalar

Environmental pressure of the system.

### **Pressure below minimum valid value** — Whether to notify when pressure is below the minimum valid value `Error` (default) | `Warning` | `None`

Select what happens if the fluid pressure goes below the minimum valid
value during simulation:

- `None` ― The block does not return an
  error if the properties go below the minimum valid value.
- `Warning` ― The block issues a
  warning, but continues the simulation.
- `Error` ― The block returns an error
  and stops the simulation.

### Entrained Air

### **Volumetric fraction of air that is entrained at atmospheric pressure** — System air entrainment at atmospheric pressure `0.005` (default) | positive scalar

Air entrainment in fluid network at atmospheric pressure.

### **Air polytropic index** — Polytropic process exponent `1.0` (default) | positive scalar between [0, 1]

Exponent of the equation that governs the polytropic process relating
fluid pressure and volume.

### **Air density at atmospheric condition** — Air density `1.225 kg/m^3` (default) | positive scalar

Air density at the pressure defined in the **Atmospheric
pressure** parameter.

### **Model air dissolution** — Whether to model air entrainment `off` (default) | `on`

Whether to account for air dissolution into the fluid network. Air
dissolution into the liquid is modeled between the values of the
**Atmospheric pressure** parameter and the
**Pressure at which all entrained air is
dissolved** parameter by Henry's Law.

### **Pressure at which all entrained air is dissolved** — Upper pressure limit for air entrainment `3 MPa` (default) | positive scalar

Upper pressure limit for air entrainment into the fluid.

#### Dependencies

To enable this parameter, select **Model air dissolution**.

## Libraries

Simscape / Fluids / Isothermal Liquid / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

### R2024a: New predefined fluids

The block now includes these predefined isothermal fluids:

- `SAE 30 Oil`
- `SAE 50 Oil`
- `10W Oil`
- `30W Oil`
- `50W Oil`
- `Skydrol LD-4`
- `Skydrol 500B-4`
- `Skydrol 5`
- `HyJet-IVA`
- `Fluid MIL-F-83282`
- `Fluid MIL-F-5606`
- `Fluid MIL-F-87257`
- `ATF (Dexron III)`
- `ISO VG 22 (ESSO UNIVIS N 22)`
- `ISO VG 32 (ESSO UNIVIS N 32)`
- `ISO VG 46 (ESSO UNIVIS N 46)`
- `ISO VG 68`
- `Brake fluid DOT 3`
- `Brake fluid DOT 4`
- `Brake fluid DOT 5`
- `Gasoline`

### R2024a: Pressure outside valid range parameter renamed

The **Pressure outside valid range** parameter is renamed to
**Pressure below minimum valid value** for clarity. The
behavior of the parameter is not changed.

### R2023a: Numerical adjustments for SAE 5W-30

When the **Isothermal liquid** parameter is `SAE
5W-30`, the block includes numerical adjustments to the density,
bulk modulus, thermal expansion coefficient, and specific internal energy to make
the data more closely match experimental data.

### R2023a: Control block behavior when fluid properties go out of range during simulation

Previously, if fluid properties went beyond the valid range during simulation, the
block would return an error. You can now use the new **Pressure outside
valid range** parameter to control the block behavior if fluid
properties go out of range during simulation

## Description

Set working fluid properties for an isothermal liquid network

The Isothermal Liquid Predefined Properties (IL) block sets the working fluid liquid
properties of your isothermal liquid network to the properties of a predefined
fluid.

You can also model dissolved air in the system as a function of pressure. To specify your
own working fluid properties, use the Foundation Library Isothermal Liquid Properties (IL) block. If you do
not specify a fluid, the system defaults apply. See Specify Fluid Properties for more
details.

### Fluid Properties Range

You can set the block to model the properties of several predefined different
liquids by using the **Isothermal liquid** parameter.

**Water**

The block provides the water properties between the triple point, when the fluid
temperature and pressure reach `273.160 K` and `611.657
Pa`, and the critical point, when the fluid temperature reaches
`647.096 K`. *Pmin*
is set by the triple point or the saturation pressure, whichever is
greater.

**Ethylene-, Propylene-, and Glycerol-Water Mixtures**

The block provides the properties for ethylene-glycol, propylene-glycol, and glycerol are
provided for temperatures above the solution freezing point. When you visualize
properties, the displayed minimum temperature may be lower than the fluid
freezing point. The block does not display updated temperatures for different
mixture concentrations.

When you specify the mixture, you can define the concentration of ethylene glycol,
propylene glycol, or glycerol to water by mass fraction or volume fraction by
using the **Concentration type** parameter.

The block provides the properties for:

- Concentration by mass between 0 and 0.6 and by volume between 0
  and 1 for ethylene glycol.
- Concentration by mass between 0 and 0.6 and by volume between 0.1
  and 0.6 for propylene glycol.
- Concentration by mass between 0 and 0.6 for glycerol. You cannot
  model glycerol concentration by volume.

The block stores the properties as a function of temperature and concentration. The block
maintains all properties, except for density and the thermal expansion
coefficient *α*, as constants for a range of pressures.

**Seawater**

The block provides seawater properties for temperatures between `273.15
K` and `393.15 K` and for pressures above the
system saturation pressure. The salinity concentration can range from
`0` to `0.12` by mass.

The block stores the properties as tabulated data with respect to pressure and
temperature. The block derives the data from the Thermophysical properties of
seawater software on the MIT website.

**Aviation Fuel Jet-A**

The block provides properties for a general, representative fuel mixture based on
Jet-A-4658 and Jet-A-3638 surrogates at temperatures between `222.22
K` and `645.61 K` and pressures above the
saturation point.

The block stores the properties as tabulated data with respect to pressure and
temperature.

**Diesel Fuel**

The block provides diesel properties for temperatures between `238.20 K`
and `690.97 K` and for pressures above the saturation
point.

**SAE 5W-30**

The block provides SAE 5W-30 properties for temperatures between `235.15
K` and `473.15 K` and for pressures above
`0.01 MPa`. The block bases the properties at the system
temperature and atmospheric pressure measurements for temperatures between
`29.85 °C` and `74.85 °C` (`303
K` to  `348 K`) and pressures between `7
MPa` and `87 MPa`. The block uses curve fits to
define properties in extrapolated regions.

**Lubricating Oils and Hydraulic Fluids**

The block uses numerical approximations to calculate fluid properties for these
liquids:

- `SAE 30 Oil`
- `SAE 50 Oil`
- `10W Oil`
- `30W Oil`
- `50W Oil`
- `Skydrol LD-4`
- `Skydrol 500B-4`
- `Skydrol 5`
- `HyJet-IVA`
- `Fluid MIL-F-83282`
- `Fluid MIL-F-5606`
- `Fluid MIL-F-87257`
- `ATF (Dexron III)`
- `ISO VG 22 (ESSO UNIVIS N 22)`
- `ISO VG 32 (ESSO UNIVIS N 32)`
- `ISO VG 46 (ESSO UNIVIS N 46)`
- `ISO VG 68`
- `Brake fluid DOT 3`
- `Brake fluid DOT 4`
- `Brake fluid DOT 5`

The block uses the Walther equation to approximate changes in velocity,
*v*, with respect to temperature, *T*

log10(log10(v+a))=b−dlog10(T),

where *a*, *b*, and
*d* are constants that are specific to each fluid.

The block assumes that the density, *ρ*, changes linearly
with respect to temperature,

ρ=ρref+α(Tref−T),

where:

- *α* are constants that are specific to each
  fluid.
- *ρref* is the fluid
  density at the reference temperature,
  *Tref*.

The bulk modulus, *β*, is

β=ρc2,

where *c* is the speed of sound. The block
uses *c*
`= 1460 m/s` as the speed of sound in hydraulic oils.

**Gasoline**

The block uses the same approximations as the lubricating oils and hydraulic fluids to
calculate the gasoline density and bulk modulus. In gasoline, the speed of sound
is `1250 m/s`.

The Vogel-Fulcher-Tammann equation calculates the fluid viscosity for
gasoline,

v=v0eBT−T0,

where *v0*,
*B*, and *T0* are
constants.

### Dissolved Air

You can optionally model air dissolved into the liquid system. If you select
**Model air dissolution**, the block models dissolution between
the values of the **Atmospheric pressure** parameter and the
**Pressure at which all entrained air is dissolved** parameter
by using Henry's law. For more information, see Fluid Models with Entrained Air.

### Visualizing Fluid Properties

To visualize the fluid density and bulk modulus in your network, right-click the Isothermal
Liquid Predefined Properties (IL) block and select **Fluids** > **Plot Fluid Properties**.

Use the **Reload Data** button to regenerate the plot when the fluid
selection or fluid parameters change.
