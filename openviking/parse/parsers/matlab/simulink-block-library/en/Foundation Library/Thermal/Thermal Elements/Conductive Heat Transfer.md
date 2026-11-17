---
type: simulink-block
title: 'Conductive Heat Transfer'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Elements'
documentation_page: 'conductiveheattransfer'
documentation_source_path: 'ref/conductiveheattransfer.html'
language: en
---

# Conductive Heat Transfer

## Ports
```yaml
ports:
- name: K
  summary: Thermal conductivity control signal, W/(K\*m) physical signal
  direction: input
- name: A
  summary: Layer A thermal
  direction: conserving
- name: B
  summary: Layer B thermal
  direction: conserving
```

### Input

### **K** — Thermal conductivity control signal, W/(K\*m) physical signal

Input physical signal that controls the thermal conductivity. The signal saturates
when the value is outside the minimum limit specified by the **Minimum thermal
conductivity** parameter.

#### Dependencies

To enable this port, set the **Conductivity type** parameter to
`Variable input`.
### Conserving

### **A** — Layer A thermal

Thermal conserving port associated with layer A.

### **B** — Layer B thermal

Thermal conserving port associated with layer B. For cylindrical wall geometry,
layer B is the inside layer.
## Parameters
```yaml
parameters:
- name: Conductivity type
  summary: How to specify thermal conductivity Constant (default) | Variable input | Tabulated data
  group: ''
- name: Wall geometry
  summary: Wall shape for heat conduction Planar (default) | Cylindrical
  group: ''
- name: Area
  summary: Area of heat transfer 1e-4 m^2 (default) | positive scalar
  group: ''
- name: Thickness
  summary: Thickness of material 0.1 m (default) | positive scalar
  group: ''
- name: Inner diameter
  summary: Inner diameter of pipe 0.05 m (default) | positive scalar
  group: ''
- name: Outer diameter
  summary: Outer diameter of pipe 0.1 m (default) | positive scalar
  group: ''
- name: Length
  summary: Pipe length 1 m (default) | positive scalar
  group: ''
- name: Thermal conductivity
  summary: Thermal conductivity of the material 401 W/(K*m) (default) | positive scalar
  group: ''
- name: Minimum thermal conductivity
  summary: Lower bound for thermal conductivity 10 W/(K*m) (default) | positive scalar
  group: ''
- name: Thermal conductivity vector
  summary: Vector of thermal conductivity values for use in table lookup [413, 401, 392, 383, 371, 357, 342] W/(K*m) (default)
    | vector of positive values
  group: ''
- name: Temperature vector
  summary: Vector of temperature values for use in table lookup [200, 273, 400, 600, 800, 1000, 1200] K (default) | strictly
    increasing vector
  group: ''
```

### **Conductivity type** — How to specify thermal conductivity `Constant` (default) | `Variable input` | `Tabulated data`

Whether to specify thermal conductivity as:

- `Constant` — Thermal conductivity remains constant
  during simulation. You specify the thermal conductivity by using the
  **Thermal conductivity** parameter.
- `Variable input` — You specify thermal conductivity
  using the input physical signal at port **K**, which can vary
  during simulation. The **Minimum thermal conductivity** parameter
  specifies the lower bound for the physical signal.
- `Tabulated data` — You specify thermal conductivity by
  using a lookup table based on temperature. In this case, thermal conductivity can
  also vary during simulation.

### **Wall geometry** — Wall shape for heat conduction `Planar` (default) | `Cylindrical`

Wall shape for heat conduction, specified as:

- `Planar` — Heat transfer is through a flat, rectangular
  wall. Specify the wall area and thickness.
- `Cylindrical` — Heat transfer is through a round pipe
  wall. Specify the pipe inner diameter, outer diameter, and length.

### **Area** — Area of heat transfer `1e-4 m^2` (default) | positive scalar

Area of heat transfer normal to the heat flow direction.

#### Dependencies

To enable this parameter, set **Wall geometry** to
`Planar`.

### **Thickness** — Thickness of material `0.1 m` (default) | positive scalar

Thickness of material, that is, the distance between layers.

#### Dependencies

To enable this parameter, set **Wall geometry** to
`Planar`.

### **Inner diameter** — Inner diameter of pipe `0.05 m` (default) | positive scalar

Inner diameter of the pipe, that is, the diameter of the inner layer of
material.

#### Dependencies

To enable this parameter, set **Wall geometry** to
`Cylindrical`.

### **Outer diameter** — Outer diameter of pipe `0.1 m` (default) | positive scalar

Outer diameter of the pipe, that is, the diameter of the outer layer of
material.

#### Dependencies

To enable this parameter, set **Wall geometry** to
`Cylindrical`.

### **Length** — Pipe length `1 m` (default) | positive scalar

Length of the pipe.

#### Dependencies

To enable this parameter, set **Wall geometry** to
`Cylindrical`.

### **Thermal conductivity** — Thermal conductivity of the material `401 W/(K*m)` (default) | positive scalar

Thermal conductivity of the material.

#### Dependencies

To enable this parameter, set **Conductivity type** to
`Constant`.

### **Minimum thermal conductivity** — Lower bound for thermal conductivity `10 W/(K*m)` (default) | positive scalar

Lower bound for the thermal conductivity value. The input signal at port
**K** saturates at this value to prevent the thermal conductivity
from further decreasing.

#### Dependencies

To enable this parameter, set **Conductivity type** to
`Variable input`.

### **Thermal conductivity vector** — Vector of thermal conductivity values for use in table lookup `[413, 401, 392, 383, 371, 357, 342] W/(K*m)` (default) | vector of positive values

Vector of thermal conductivity values that correspond to the **Temperature
vector** parameter values. The vector size must be the same as the
**Temperature vector** parameter. The block performs one-dimensional
table lookup of thermal conductivity by using the average temperature of the block,
linear interpolation, and nearest extrapolation. For more information on the
interpolation and extrapolation algorithms, see PS Lookup Table (1D).

#### Dependencies

To enable this parameter, set **Conductivity type** to
`Tabulated data`.

### **Temperature vector** — Vector of temperature values for use in table lookup `[200, 273, 400, 600, 800, 1000, 1200] K` (default) | strictly increasing vector

Vector of temperature values that correspond to the **Thermal conductivity
vector** parameter values. The vector must be strictly increasing. The values
can be nonuniformly spaced. The vector must contain at least two values.

#### Dependencies

To enable this parameter, set **Conductivity type** to
`Tabulated data`.
## Libraries

Simscape / Foundation Library / Thermal / Thermal Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007b**

### R2022b: Model variable thermal conductivity and heat transfer through a round pipe wall

The new **Conductivity type** parameter lets the thermal conductivity
be either constant, which you specify by the **Thermal conductivity**
parameter, or variable. You can specify variable thermal conductivity either as a physical
signal at port **K** or as a lookup table based on temperature.

Additionally, you can set the new **Wall geometry** parameter to either
`Planar` or `Cylindrical`.
`Planar` refers to a flat, rectangular wall.
`Cylindrical` refers to a round pipe wall.

In the default configuration, with **Conductivity type** set to
`Constant` and **Wall geometry** set to
`Planar`, the block functions as in previous releases.

## Description

Heat transfer by conduction

The Conductive Heat Transfer block represents heat transfer
by conduction between two layers of the same material. For a flat surface, the Fourier law
describes the transfer,

Q=k⋅AD(TA−TB),

where:

- *Q* is the heat flow.
- *k* is the thermal conductivity of the material.
- *A* is the area normal to the heat flow direction.
- *D* is the distance between layers, that is, the thickness of
  material.
- *T*A is the temperature of layer A.
- *T*B is the temperature of layer B.

Heat conduction through a round pipe wall is

Qcyl=2πk⋅Lln(doutdin)(TA−TB),

where:

- *L* is the pipe length.
- *d*in is the inner diameter.
- *d*out is the outer diameter.

You can specify the thermal conductivity by using the **Conductivity
type** parameter:

- `Constant` — Thermal conductivity remains constant during
  simulation. You specify the thermal conductivity by using the **Thermal
  conductivity** parameter.
- `Variable input` — You specify the thermal conductivity using
  the input physical signal at port **K**, which can vary during
  simulation. The **Minimum thermal conductivity** parameter specifies the
  lower bound for the physical signal.
- `Tabulated data` — You specify the thermal conductivity by
  using a lookup table based on temperature. In this case, thermal conductivity can also
  vary during simulation.

The `Tabulated data` option uses the average temperature of the
block to find the thermal conductivity. For planar wall geometry, the average temperature
is

Tavg=TA+TB2.

For cylindrical wall geometry, the average temperature is

Tavg=(TA−TB)⋅(doutdout−din−1ln(doutdin))+TB,

which assumes that *T*B is at the inside of the
cylinder.

**A** and **B** are thermal conserving ports associated
with the material layers. Because the block positive direction is from port
**A** to port **B**, the heat flow is positive if it flows
from **A** to **B**.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
