---
type: simulink-block
title: 'Reservoir (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Elements'
documentation_page: 'reservoir2p'
documentation_source_path: 'ref/reservoir2p.html'
language: en
---

# Reservoir (2P)

## Ports

### Conserving

### **A** — Reservoir inlet two-phase fluid

Two-phase fluid conserving port associated with the reservoir inlet.

## Parameters

### **Reservoir pressure specification** — Specification method for reservoir pressure `Atmospheric pressure` (default) | `Specified pressure` | `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

Specification method for the reservoir pressure:

- `Atmospheric pressure` — Use the atmospheric
  pressure specified by a Two-Phase Fluid Properties
  (2P) block connected to the circuit.
- `Specified pressure` — Specify a value by using
  the **Reservoir pressure** parameter.
- `Saturation pressure at specified condensing
  temperature` — Use the pressure along the liquid saturation
  curve that corresponds to the temperature specified by the **Reservoir
  condensing temperature** parameter.
- `Saturation pressure at specified evaporating
  temperature` — Use the pressure along the vapor saturation
  curve that corresponds to the temperature specified by using the **Reservoir
  evaporating temperature** parameter.

### **Reservoir pressure** — Pressure in reservoir `0.101325 MPa` (default) | positive scalar

Absolute pressure inside the reservoir. This pressure remains constant during
simulation. The default value corresponds to atmospheric pressure at mean sea
level.

#### Dependencies

To enable this parameter, set **Reservoir pressure
specification** to `Specified pressure`.

### **Reservoir condensing temperature** — Specify saturation pressure in terms of condensing temperature `373.15 K` (default) | positive scalar

Pressure of the fluid inside the reservoir is equal to the saturation pressure,
along the liquid saturation curve, that corresponds to this condensing temperature. The
condensing temperature must be less than the critical temperature because the saturation
curves are not defined above the critical point.

#### Dependencies

To enable this parameter, set **Reservoir pressure
specification** to `Saturation pressure at specified condensing
temperature`.

### **Reservoir evaporating temperature** — Specify saturation pressure in terms of evaporating temperature `373.15 K` (default) | positive scalar

Pressure of the fluid inside the reservoir is equal to the saturation pressure,
along the vapor saturation curve, that corresponds to this evaporating temperature. The
evaporating temperature must be less than the critical temperature because the
saturation curves are not defined above the critical point.

#### Dependencies

To enable this parameter, set **Reservoir pressure
specification** to `Saturation pressure at specified
evaporating temperature`.

### **Reservoir energy specification** — Thermodynamic variable to use to define reservoir conditions `Temperature` (default) | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy` | `Degree of subcooling` | `Degree of superheating`

Thermodynamic variable to use for energy specification:

- `Temperature` — Specify the absolute temperature
  inside the reservoir by using the **Reservoir temperature**
  parameter. You can specify a state that is a subcooled liquid or superheated vapor.
  You cannot specify a liquid-vapor mixture because the temperature is constant across
  the liquid-vapor mixture region.
- `Vapor quality` — Specify the mass fraction of
  vapor in the reservoir by using the **Reservoir vapor quality**
  parameter. You can use this option only when the pressure is less than the critical
  pressure because this quantity does not exist above the critical point. You can
  specify a state that is a liquid-vapor mixture. You cannot specify a subcooled
  liquid or a superheated vapor because the vapor quality is 0 and 1, respectively,
  across the whole region. Additionally, the block limits the pressure to below the
  critical pressure.
- `Vapor void fraction` — Specify the volume
  fraction of vapor in the reservoir by using the **Reservoir void
  fraction** parameter. You can use this option only when the pressure is
  less than the critical pressure because this quantity does not exist above the
  critical point. You can specify a state that is a liquid-vapor mixture. You cannot
  specify a subcooled liquid or a superheated vapor because the vapor quality is 0 and
  1, respectively, across the whole region. Additionally, the block limits the
  pressure to below the critical pressure.
- `Specific enthalpy` — Specify the specific
  enthalpy of the fluid in the reservoir by using the **Reservoir specific
  enthalpy** parameter. This option does not limit the fluid state.
- `Specific internal energy` — Specify the
  specific internal energy of the fluid in the reservoir by using the
  **Reservoir specific internal energy** parameter. This option
  does not limit the fluid state.
- `Degree of subcooling` — Specify the degree of
  subcooling of the fluid in the reservoir by using the **Reservoir
  subcooling** parameter. You can use this option only when the pressure is
  less than the critical pressure because the saturation curves are not defined above
  the critical point.
- `Degree of superheating` — Specify the degree of
  superheating of the fluid in the reservoir by using the **Reservoir
  superheating** parameter. You can use this option only when the pressure
  is less than the critical pressure because the saturation curves are not defined
  above the critical point.

### **Reservoir temperature** — Temperature in reservoir `293.15 K` (default) | positive scalar

Absolute temperature inside the reservoir. This temperature remains constant during
simulation. The specified temperature maps to a specific enthalpy in either the
subcooled liquid region or the superheated vapor region. For most fluids, the
temperature in the liquid-vapor mixture region of a P-H diagram is constant, therefore a
temperature value does not correspond one-to-one to a specific enthalpy value within the
liquid-vapor mixture region.

#### Dependencies

To enable this parameter, set **Reservoir energy specification**
to `Temperature`.

### **Reservoir vapor quality** — Mass fraction of vapor in reservoir `0.5` (default) | scalar in range [0 1]

Mass fraction of vapor in the reservoir. This value remains constant during
simulation.

#### Dependencies

To enable this parameter, set **Reservoir energy specification**
to `Vapor quality`.

### **Reservoir vapor void fraction** — Volume fraction of vapor in reservoir `0.5` (default) | scalar in range [0 1]

Volume fraction of vapor in the reservoir. This value remains constant during
simulation.

#### Dependencies

To enable this parameter, set **Reservoir energy specification**
to `Vapor void fraction`.

### **Reservoir specific enthalpy** — Specific enthalpy of fluid in reservoir `1500 kJ/kg` (default) | positive scalar

Specific enthalpy of the fluid in the reservoir. This value remains constant during
simulation.

#### Dependencies

To enable this parameter, set **Reservoir energy specification**
to `Specific enthalpy`.

### **Reservoir specific internal energy** — Specific internal energy of fluid in reservoir `1500 kJ/kg` (default) | positive scalar

Specific internal energy of the fluid in the reservoir. This value remains constant
during simulation.

#### Dependencies

To enable this parameter, set **Reservoir energy specification**
to `Specific internal energy`.

### **Reservoir subcooling** — Degree of subcooling in reservoir `5 deltaK` (default) | positive scalar

Degree of subcooling of the fluid in the reservoir, that is, the difference between
the liquid saturation temperature and the fluid temperature. This value remains constant
during simulation.

#### Dependencies

To enable this parameter, set **Reservoir energy specification**
to `Degree of subcooling`.

### **Reservoir superheating** — Degree of superheating in reservoir `5 deltaK` (default) | positive scalar

Degree of superheating of the fluid in the reservoir, that is, the difference
between the fluid temperature and the vapor saturation temperature. This value remains
constant during simulation.

#### Dependencies

To enable this parameter, set **Reservoir energy specification**
to `Degree of superheating`.

### **Cross-sectional area at port A** — Area normal to flow path at reservoir inlet `0.01 m^2` (default) | positive scalar

Flow area of the reservoir inlet, represented by port **A**.

## Libraries

Simscape / Foundation Library / Two-Phase Fluid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

## Description

Two-phase fluid reservoir at constant temperature and pressure

The Reservoir (2P) block sets pressure and temperature
boundary conditions in a two-phase fluid network. The reservoir is assumed infinite in size,
causing its pressure and specific internal energy to remain constant.

Port **A** represents the reservoir inlet. The flow resistance between
port **A** and the reservoir interior is assumed negligible. The pressure at
port **A** is therefore equal to the pressure inside the reservoir.

The specific enthalpy and specific internal energy at the reservoir inlet depend on the
direction of flow. Fluid leaves the reservoir at the reservoir pressure and specific internal
energy. Fluid enters the reservoir at the reservoir pressure, but the specific internal energy
is determined by the two-phase fluid network upstream.

The block provides independent selection of pressure specification and energy
specification, by using the **Reservoir pressure specification** and
**Reservoir energy specification** parameters. Depending on the selected
options, the block exposes additional parameters to specify values for the selected
quantities.

This block also serves as a reference connection for the Pressure &
Internal Energy Sensor (2P) block. In this case, the measured pressure and
specific internal energy are relative to the reservoir pressure and specific internal energy.

### Assumptions and Limitations

- The pressure and specific internal energy of the fluid are assumed constant in the
  reservoir.
- The flow resistance between port **A** and the reservoir interior
  is negligible. Pressure is the same at port **A** and in the reservoir
  interior.
