---
type: simulink-block
title: 'Controlled Reservoir (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Two-Phase Fluid Models / Elements'
documentation_page: 'controlledreservoir2p'
documentation_source_path: 'ref/controlledreservoir2p.html'
language: en
---

# Controlled Reservoir (2P)

## Ports

### Input

### **P** — Pressure control signal, MPa physical signal

Physical signal port that provides the reservoir pressure control signal.

#### Dependencies

To enable this port, set **Reservoir pressure specification**
to `Specified pressure`.

### **Tc** — Reservoir condensing temperature control signal, K physical signal

Physical signal port that provides the reservoir condensing temperature control
signal.

#### Dependencies

To enable this port, set **Reservoir pressure specification**
to `Saturation pressure at specified condensing
temperature`.

### **Te** — Reservoir evaporating temperature control signal, K physical signal

Physical signal port that provides the reservoir evaporating temperature control
signal.

#### Dependencies

To enable this port, set **Reservoir pressure specification**
to `Saturation pressure at specified evaporating
temperature`.

### **T** — Temperature control signal, K physical signal

Physical signal port that provides either the subcooled liquid temperature or the
superheated vapor temperature control signal, based on the **Reservoir energy
specification** parameter setting.

#### Dependencies

To enable this port, set **Reservoir energy specification** to
either `Subcooled liquid temperature` or
`Superheated vapor temperature`.

### **X** — Mass fraction of vapor control signal, unitless physical signal

Physical signal port that specifies the mass fraction of vapor in the reservoir.

#### Dependencies

To enable this port, set **Reservoir energy specification** to
`Vapor quality`.

### **a** — Volume fraction of vapor control signal, unitless physical signal

Physical signal port that specifies the volume fraction of vapor in the reservoir.

#### Dependencies

To enable this port, set **Reservoir energy specification** to
`Vapor void fraction`.

### **H** — Specific enthalpy of the fluid control signal, kJ/kg physical signal

Physical signal port that specifies the specific enthalpy of the fluid in the
reservoir.

#### Dependencies

To enable this port, set **Reservoir energy specification** to
`Specific enthalpy`.

### **U** — Specific internal energy of the fluid control signal, kJ/kg physical signal

Physical signal port that specifies the specific internal energy of the fluid in
the reservoir.

#### Dependencies

To enable this port, set **Reservoir energy specification** to
`Specific internal energy`.

### **SC** — Degree of subcooling of the fluid control signal, deltaK physical signal

Physical signal port that specifies the degree of subcooling of the fluid in the
reservoir, that is, the difference between the liquid saturation temperature and the
fluid temperature.

This input signal specifies a temperature difference, in units of
`deltaK`, rather than an absolute temperature. Therefore, if you
connect a Simulink-PS Converter block directly to this
port, do not select the **Apply affine conversion** check
box.

#### Dependencies

To enable this port, set **Reservoir energy specification** to
`Degree of subcooling`.

### **SH** — Degree of superheating of the fluid control signal, deltaK physical signal

Physical signal port that specifies the degree of superheating of the fluid in the
reservoir, that is, the difference between the fluid temperature and the vapor
saturation temperature.

This input signal specifies a temperature difference, in units of
`deltaK`, rather than an absolute temperature. Therefore, if you
connect a Simulink-PS Converter block directly to this
port, do not select the **Apply affine conversion** check
box.

#### Dependencies

To enable this port, set **Reservoir energy specification** to
`Degree of superheating`.
### Conserving

### **A** — Reservoir inlet two-phase fluid

Two-phase fluid conserving port associated with the reservoir inlet.

## Parameters

### **Reservoir pressure specification** — Specification method for reservoir pressure `Specified pressure` (default) | `Saturation pressure at specified condensing temperature` | `Saturation pressure at specified evaporating temperature`

Specification method for the reservoir pressure:

- `Specified pressure` — Specify a value by using
  the control signal at port **P**.
- `Saturation pressure at specified condensing
  temperature` — Use the pressure along the liquid saturation
  curve that corresponds to the temperature specified by the control signal at port
  **Tc**. When you select this option, the block limits the
  pressure to be less than or equal to critical pressure.
- `Saturation pressure at specified evaporating
  temperature` — Use the pressure along the vapor saturation
  curve that corresponds to the temperature specified by the control signal at port
  **Te**. When you select this option, the block limits the
  pressure to be less than or equal to critical pressure.

### **Reservoir energy specification** — Thermodynamic variable to use to define reservoir conditions `Subcooled liquid temperature` (default) | `Superheated vapor temperature` | `Vapor quality` | `Vapor void fraction` | `Specific enthalpy` | `Specific internal energy` | `Degree of subcooling` | `Degree of superheating`

Thermodynamic variable to use for energy specification:

- `Subcooled liquid temperature` — Specify the
  subcooled liquid temperature inside the reservoir by using the control signal at
  port **T**. When you select this option, the block limits the
  pressure to be less than or equal to the critical pressure. The block also limits
  the input at port **T** to the range between the minimum
  temperature and the liquid saturation temperature to avoid the discontinuity in the
  corresponding specific internal energy or specific enthalpy when the input
  temperature varies across the saturation temperature.
- `Superheated vapor temperature` — Specify the
  superheated vapor temperature inside the reservoir by using the control signal at
  port **T**. When you select this option, the block limits the
  pressure to be less than or equal to the critical pressure. The block also limits
  the input at port **T** to the range between the vapor saturation
  temperature and the maximum temperature to avoid the discontinuity in the
  corresponding specific internal energy or specific enthalpy when the input
  temperature varies across the saturation temperature.
- `Vapor quality` — Specify the mass fraction of
  vapor in the reservoir by using the control signal at port **X**.
  When you select this option, the block limits the pressure to be less than or equal
  to critical pressure. You can specify a state that is a liquid-vapor mixture. You
  cannot specify a subcooled liquid or a superheated vapor because the vapor quality
  is 0 and 1, respectively, across the whole region. Additionally, the block limits
  the pressure to below the critical pressure.
- `Vapor void fraction` — Specify the volume
  fraction of vapor in the reservoir by using the control signal at port
  **a**. When you select this option, the block limits the pressure
  to be less than or equal to critical pressure. You can specify a state that is a
  liquid-vapor mixture. You cannot specify a subcooled liquid or a superheated vapor
  because the vapor quality is 0 and 1, respectively, across the whole region.
  Additionally, the block limits the pressure to below the critical pressure.
- `Specific enthalpy` — Specify the specific
  enthalpy of the fluid in the reservoir by using the control signal at port
  **H**. This option does not limit the fluid state.
- `Specific internal energy` — Specify the
  specific internal energy of the fluid in the reservoir by using the control signal
  at port **U**. This option does not limit the fluid state.
- `Degree of subcooling` — Specify the degree of
  subcooling of the fluid in the reservoir by using the control signal at port
  **SC**. The degree of subcooling is the difference between the
  liquid saturation temperature and the fluid temperature. When you select this
  option, the block limits the pressure to be less than or equal to critical pressure.
- `Degree of superheating` — Specify the degree of
  superheating of the fluid in the reservoir by using the control signal at port
  **SH**. The degree of superheating is the difference between the
  fluid temperature and the vapor saturation temperature. When you select this option,
  the block limits the pressure to be less than or equal to critical pressure.

### **Cross-sectional area at port A** — Area normal to flow path at reservoir inlet `0.01 m^2` (default) | positive scalar

Flow area of the reservoir inlet, represented by port **A**.

### **Reservoir pressure above critical** — Define action for when reservoir pressure exceeds critical pressure `Warn and limit to critical pressure` (default) | `Limit to critical pressure` | `Error`

Define action for when reservoir pressure exceeds critical pressure:

- `Warn and limit to critical pressure` — The
  block issues a warning and limits the pressure to critical pressure.
- `Limit to critical pressure` — The block limits
  the pressure to critical pressure, but the simulation continues without a
  warning.
- `Error` — Simulation stops with an error.

#### Dependencies

This parameter is automatically exposed when you select a combination of pressure
specification and energy specification options that requires the pressure inside the
reservoir to be less than the critical pressure.

## Libraries

Simscape / Foundation Library / Two-Phase Fluid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

## Description

Two-phase fluid reservoir at variable pressure and temperature

The Reservoir (2P) block sets boundary conditions in a
two-phase fluid network. The reservoir is assumed infinite in size.

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
options, the block exposes the relevant input ports to provide the control signals for the
selected quantities.

For certain option combinations, the pressure inside the reservoir must be less than the
critical pressure because the saturation curves are not defined above the critical point. If
you select such a combination, the **Reservoir pressure above critical**
parameter lets you decide what happens when the fluid pressure exceeds the critical pressure.

This block also serves as a reference connection for the Pressure &
Internal Energy Sensor (2P) block. In this case, the measured pressure and
specific internal energy are relative to the reservoir pressure and specific internal energy.
