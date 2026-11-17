---
type: simulink-block
title: 'Saturation Properties Sensor (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Sensors'
documentation_page: 'saturationpropertiessensor2p'
documentation_source_path: 'ref/saturationpropertiessensor2p.html'
language: en
---

# Saturation Properties Sensor (2P)

## Ports
```yaml
ports:
- name: TL
  summary: Saturated liquid temperature, K physical signal
  direction: output
- name: TV
  summary: Saturated vapor temperature, K physical signal
  direction: output
- name: PL
  summary: Saturated liquid pressure, MPa physical signal
  direction: output
- name: PV
  summary: Saturated vapor pressure, MPa physical signal
  direction: output
- name: UL
  summary: Saturated liquid specific internal energy, kJ/kg physical signal
  direction: output
- name: UV
  summary: Saturated vapor specific internal energy, kJ/kg physical signal
  direction: output
- name: HL
  summary: Saturated liquid specific enthalpy, kJ/kg physical signal
  direction: output
- name: HV
  summary: Saturated vapor specific enthalpy, kJ/kg physical signal
  direction: output
- name: VL
  summary: Saturated liquid specific volume, m^3/kg physical signal
  direction: output
- name: VV
  summary: Saturated vapor specific volume, m^3/kg physical signal
  direction: output
- name: rhoL
  summary: Saturated liquid density, kg/m^3 physical signal
  direction: output
- name: rhoV
  summary: Saturated vapor density, kg/m^3 physical signal
  direction: output
- name: A
  summary: Sensor inlet two-phase fluid
  direction: conserving
```

### Output

### **TL** — Saturated liquid temperature, K physical signal

Physical signal output port that measures the saturated liquid temperature based
on the pressure at port **A**.

#### Dependencies

To enable this port, select the **Saturated temperature
measurement** check box.

### **TV** — Saturated vapor temperature, K physical signal

Physical signal output port that measures the saturated vapor temperature based on
the pressure at port **A**.

#### Dependencies

To enable this port, select the **Saturated temperature
measurement** check box.

### **PL** — Saturated liquid pressure, MPa physical signal

Physical signal output port that measures the saturated liquid pressure based on
the temperature at port **A**.

#### Dependencies

To enable this port, select the **Saturated pressure
measurement** check box.

### **PV** — Saturated vapor pressure, MPa physical signal

Physical signal output port that measures the saturated vapor pressure based on
the temperature at port **A**.

#### Dependencies

To enable this port, select the **Saturated pressure
measurement** check box.

### **UL** — Saturated liquid specific internal energy, kJ/kg physical signal

Physical signal output port that measures the saturated liquid specific internal
energy based on the pressure at port **A**.

#### Dependencies

To enable this port, set the **Energy measurement** parameter
to `Saturated specific internal energy`.

### **UV** — Saturated vapor specific internal energy, kJ/kg physical signal

Physical signal output port that measures the saturated vapor specific internal
energy based on the pressure at port **A**.

#### Dependencies

To enable this port, set the **Energy measurement** parameter
to `Saturated specific internal energy`.

### **HL** — Saturated liquid specific enthalpy, kJ/kg physical signal

Physical signal output port that measures the saturated liquid specific enthalpy
based on the pressure at port **A**.

#### Dependencies

To enable this port, set the **Energy measurement** parameter
to `Saturated specific enthalpy`.

### **HV** — Saturated vapor specific enthalpy, kJ/kg physical signal

Physical signal output port that measures the saturated vapor specific enthalpy
based on the pressure at port **A**.

#### Dependencies

To enable this port, set the **Energy measurement** parameter
to `Saturated specific enthalpy`.

### **VL** — Saturated liquid specific volume, m^3/kg physical signal

Physical signal output port that measures the saturated liquid specific volume
based on the pressure at port **A**.

#### Dependencies

To enable this port, set the **Density measurement** parameter
to `Saturated specific volume`.

### **VV** — Saturated vapor specific volume, m^3/kg physical signal

Physical signal output port that measures the saturated vapor specific volume
based on the pressure at port **A**.

#### Dependencies

To enable this port, set the **Density measurement** parameter
to `Saturated specific volume`.

### **rhoL** — Saturated liquid density, kg/m^3 physical signal

Physical signal output port that measures the saturated liquid density based on
the pressure at port **A**.

#### Dependencies

To enable this port, set the **Density measurement** parameter
to `Saturated density`.

### **rhoV** — Saturated vapor density, kg/m^3 physical signal

Physical signal output port that measures the saturated vapor density based on the
pressure at port **A**.

#### Dependencies

To enable this port, set the **Density measurement** parameter
to `Saturated density`.
### Conserving

### **A** — Sensor inlet two-phase fluid

Two-phase fluid conserving port associated with the sensor inlet. Connect this
port to the node in the two-phase fluid network for which you want to measure liquid
and vapor saturation properties.
## Parameters
```yaml
parameters:
- name: Saturated temperature measurement
  summary: Measure saturated liquid and vapor temperature based on pressure On (default) | Off
  group: ''
- name: Saturated pressure measurement
  summary: Measure saturated liquid and vapor pressure based on temperature Off (default) | On
  group: ''
- name: Saturated pressure beyond min and max pressure
  summary: Reporting preference for out-of-bounds saturated pressure Error (default) | Warning | None
  group: ''
- name: Energy measurement
  summary: Measure saturated specific internal energy or saturated specific enthalpy based on pressure Off (default) | Saturated
    specific internal energy | Saturated specific enthalpy
  group: ''
- name: Density measurement
  summary: Measure saturated specific volume or saturated density based on pressure Off (default) | Saturated specific volume
    | Saturated density
  group: ''
```

### **Saturated temperature measurement** — Measure saturated liquid and vapor temperature based on pressure `On` (default) | `Off`

Selecting this check box exposes output ports **TL** and
**TV**, which measure the saturated liquid and vapor temperature,
respectively, based on the pressure at port **A**.

### **Saturated pressure measurement** — Measure saturated liquid and vapor pressure based on temperature `Off` (default) | `On`

Selecting this check box enables the **Saturated pressure beyond min and max
pressure** parameter and exposes output ports **PL** and
**PV**, which measure the saturated liquid and vapor pressure,
respectively, based on the temperature at port **A**.

### **Saturated pressure beyond min and max pressure** — Reporting preference for out-of-bounds saturated pressure `Error` (default) | `Warning` | `None`

When either of the saturated pressures is below the minimum pressure or above the
maximum pressure specified in the fluid properties, then the saturated pressure value is
based on extrapolated values of the temperature tables, rather than the interpolation
within the table. Choose your reporting preference for when the saturated pressure is
out of bounds:

- `Error` — Simulation stops with an error.
- `Warn` — The block issues a warning.
- `None` — The block does not issue an
  assertion.

#### Dependencies

To enable this parameter, set **Saturated pressure measurement**
to `On`.

### **Energy measurement** — Measure saturated specific internal energy or saturated specific enthalpy based on pressure `Off` (default) | `Saturated specific internal energy` | `Saturated specific enthalpy`

Setting this parameter to:

- `Saturated specific internal energy` — Exposes
  output ports **UL** and **UV**, which measure the
  saturated specific internal energy of liquid and vapor, respectively, based on the
  pressure at port **A**.
- `Saturated specific enthalpy` — Exposes output
  ports **HL** and **HV**, which measure the
  saturated specific enthalpy of liquid and vapor, respectively, based on the pressure
  at port **A**.

### **Density measurement** — Measure saturated specific volume or saturated density based on pressure `Off` (default) | `Saturated specific volume` | `Saturated density`

Setting this parameter to:

- `Saturated specific volume` — Exposes output
  ports **VL** and **VV**, which measure the
  saturated specific volume of liquid and vapor, respectively, based on the pressure
  at port **A**.
- `Saturated density` — Exposes output ports
  **rhoL** and **rhoV**, which measure the
  saturated density of liquid and vapor, respectively, based on the pressure at port
  **A**.
## Libraries

Simscape / Foundation Library / Two-Phase Fluid / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

### R2023a: Usability enhancement for sensors

The Saturation Properties Sensor (2P) block now has the
**Saturated temperature measurement** check box, which controls the
visibility of ports **TL** and **TV** on the block icon.
The **Saturated pressure measurement** parameter, which controls the
visibility of ports **PL** and **PV**, is now a check box.

This change has no compatibility impact.

## Description

Measure liquid and vapor saturation properties in two-phase fluids

The Saturation Properties Sensor (2P) block represents an
ideal sensor that lets you measure these liquid and vapor saturation properties in a two-phase
fluid network:

- Saturated temperature, specific volume, internal energy, or enthalpy, based on the
  pressure measurement
- Saturated pressure based on the temperature measurement

The block measures these properties at the node connected to port **A**.
There is no mass or energy flow through the sensor.

By default, only the output ports that measure the saturated liquid and vapor
temperatures, **TL** and **TV**, are visible on the block
icon. Use the block parameters to control visibility of output ports for the other
measurements.
