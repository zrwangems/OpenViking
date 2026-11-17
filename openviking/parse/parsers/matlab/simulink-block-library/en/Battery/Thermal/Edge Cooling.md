---
type: simulink-block
title: 'Edge Cooling'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Thermal'
documentation_page: 'edgecooling'
documentation_source_path: 'ref/edgecooling.html'
language: en
---

# Edge Cooling

## Ports
```yaml
ports:
- name: Tp
  summary: Plate temperature, K physical signal
  direction: output
- name: dT
  summary: Fluid temperature change, K physical signal
  direction: output
- name: dP
  summary: Fluid pressure drop, Pa physical signal
  direction: output
- name: fluid_in
  summary: Fluid in cooling plate thermal fluid
  direction: conserving
- name: fluid_out
  summary: Fluid out of cooling plate thermal fluid
  direction: conserving
- name: Surf1
  summary: Surface 1 of cooling plate thermal
  direction: conserving
- name: Surf2
  summary: Surface 2 of cooling plate thermal
  direction: conserving
```

### Output

### **Tp** — Plate temperature, K physical signal

Temperature of the cooling plate, in Kelvin.

### **dT** — Fluid temperature change, K physical signal

Temperature change of the fluid, in Kelvin.

### **dP** — Fluid pressure drop, Pa physical signal

Pressure drop of the fluid, in Pascal.
### Conserving

### **fluid\_in** — Fluid in cooling plate thermal fluid

Thermal fluid conserving port associated with the fluid that comes in
the cooling plate.

### **fluid\_out** — Fluid out of cooling plate thermal fluid

Thermal fluid conserving port associated with the fluid that comes out
of the cooling plate.

### **Surf1** — Surface 1 of cooling plate thermal

Thermal conserving port associated with the surface 1 of the cooling
plate. This port connects the array of thermal nodes between the cooling
plate and battery pack or module.

### **Surf2** — Surface 2 of cooling plate thermal

Thermal conserving port associated with the surface 2 of the cooling
plate. This port connects the array of thermal nodes between the cooling
plate and battery pack or module.
## Parameters
```yaml
parameters:
- name: Battery Connectivity
  summary: Connectivity of battery Single sided (default) | Double sided
  group: Interface
- name: Number of battery thermal nodes (surface 1)
  summary: Number of battery thermal nodes on surface 1 1 (default) | positive scalar
  group: Interface
- name: Dimension of battery thermal nodes (surface 1)
  summary: Dimension of battery thermal nodes on surface 1 ones(1, 2) (default)
  group: Interface
- name: Coordinates of battery thermal nodes (surface 1)
  summary: Coordinates of battery thermal nodes on surface 1 ones(1, 2) (default) | M-by-N matrix
  group: Interface
- name: Number of battery thermal nodes (surface 2)
  summary: Number of battery thermal nodes on surface 2 1 (default) | positive scalar
  group: Interface
- name: Dimension of battery thermal nodes (surface 2)
  summary: Dimension of battery thermal nodes on surface 2 ones(1, 2) (default) | M-by-N matrix
  group: Interface
- name: Coordinates of battery thermal nodes (surface 2)
  summary: Coordinates of battery thermal nodes on surface 2 ones(1, 2) (default) | M-by-N matrix
  group: Interface
- name: Number of partitions in X dimension for the cooling plate
  summary: Number of partitions in X dimension for cooling plate 2 (default) | positive scalar
  group: Interface
- name: Number of partitions in Y dimension for the cooling plate
  summary: Number of partitions in Y dimension for the cooling plate 5 (default) | positive scalar
  group: Interface
- name: Thickness of cooling plate material
  summary: Thickness of material of cooling plate 2e-3 m (default) | positive scalar
  group: Plate Material
- name: Thermal conductivity of cooling plate material
  summary: Thermal conductivity of material of cooling plate 20 W/(K*m) (default) | positive scalar
  group: Plate Material
- name: Density of cooling plate material
  summary: Density of material of cooling plate 2500 kg/m^3 (default) | positive scalar
  group: Plate Material
- name: Specific heat of cooling plate material
  summary: Specific heat of material of cooling plate 447 J/(K*kg (default) | positive scalar
  group: Plate Material
- name: Initial temperature of the cooling plate and the coolant fluid
  summary: Temperature of cooling plate and coolant fluid at time zero 300 K (default) | positive scalar
  group: Plate Material
- name: Reynolds number upper limit for laminar flow
  summary: Reynolds number above which flow begins to transition from laminar to turbulent 2000 (default) | scalar greater
    than 1
  group: Fluid Properties
- name: Reynolds number lower limit for turbulent flow
  summary: Reynolds number below which flow begins to transition from turbulent to laminar 4000 (default) | positive scalar
  group: Fluid Properties
- name: Nusselt number for laminar flow heat transfer
  summary: Ratio of convective to conductive heat transfer 3.66 (default) | positive scalar
  group: Fluid Properties
- name: Aggregate equivalent length of local resistances
  summary: Combined length of all local resistances present in the pipes 1e-3 m (default) | nonnegative scalar
  group: Fluid Properties
- name: Laminar friction constant for Darcy friction factor
  summary: Effect of pipe geometry on the viscous friction losses 64 (default) | positive scalar
  group: Fluid Properties
- name: Select edge to be cooled
  summary: Cooling edge Edge cooling along Y axis at X = Xmin (default) | Edge cooling along X axis at Y = Ymin | Edge cooling
    along Y axis at X = Xmax | Edge cooling along X axis at Y = Ymax
  group: Design
- name: Cooling channel hydraulic diameter
  summary: Hydraulic diameter of cooling channel 5e-3 m (default) | positive scalar
  group: Design
- name: Cooling channel cross-sectional area
  summary: Cross-sectional area of cooling channel 2e-5 m^2 (default) | positive scalar
  group: Design
- name: Coolant channel roughness
  summary: Roughness of the coolant channel 1.5e-05 m (default) | positive scalar
  group: Design
```

### Interface

### **Battery Connectivity** — Connectivity of battery `Single sided` (default) | `Double sided`

Option to choose the connectivity of the battery.

### **Number of battery thermal nodes (surface 1)** — Number of battery thermal nodes on surface 1 `1` (default) | positive scalar

Number of battery thermal nodes on surface 1 of the cooling
plate.

When manually connecting this cooling plate to a battery, you can
obtain this information by querying the
`ThermalNodes` property of the battery object
associated with the battery block you are connecting this block to. The
`ThermalNodes` property includes information such
as the number of nodes, the 2-D location of nodes, and the dimensions of
nodes.

### **Dimension of battery thermal nodes (surface 1)** — Dimension of battery thermal nodes on surface 1 `ones(1, 2)` (default)

Dimension of the battery thermal nodes on surface 1 of the cooling
plate.

When manually connecting this cooling plate to a battery, you can
obtain this information by querying the
`ThermalNodes` property of the battery object
associated with the battery block you are connecting this block to. The
`ThermalNodes` property includes information such
as the number of nodes, the 2-D location of nodes, and the dimensions of
nodes.

### **Coordinates of battery thermal nodes (surface 1)** — Coordinates of battery thermal nodes on surface 1 `ones(1, 2)` (default) | M-by-N matrix

Coordinates of the battery thermal nodes on surface 1 of the cooling
plate.

When manually connecting this cooling plate to a battery, you can
obtain this information by querying the
`ThermalNodes` property of the battery object
associated with the battery block you are connecting this block to. The
`ThermalNodes` property includes information such
as the number of nodes, the 2-D location of nodes, and the dimensions of
nodes.

### **Number of battery thermal nodes (surface 2)** — Number of battery thermal nodes on surface 2 `1` (default) | positive scalar

Number of battery thermal nodes on surface 2 of the cooling
plate.

When manually connecting this cooling plate to a battery, you can
obtain this information by querying the
`ThermalNodes` property of the battery object
associated with the battery block you are connecting this block to. The
`ThermalNodes` property includes information such
as the number of nodes, the 2-D location of nodes, and the dimensions of
nodes.

#### Dependencies

To enable this parameter, set **Battery
Connectivity** to `Double
sided`.

### **Dimension of battery thermal nodes (surface 2)** — Dimension of battery thermal nodes on surface 2 `ones(1, 2)` (default) | M-by-N matrix

Dimension of the battery thermal nodes on surface 2 of the cooling
plate.

When manually connecting this cooling plate to a battery, you can
obtain this information by querying the
`ThermalNodes` property of the battery object
associated with the battery block you are connecting this block to. The
`ThermalNodes` property includes information such
as the number of nodes, the 2-D location of nodes, and the dimensions of
nodes.

#### Dependencies

To enable this parameter, set **Battery
Connectivity** to `Double
sided`.

### **Coordinates of battery thermal nodes (surface 2)** — Coordinates of battery thermal nodes on surface 2 `ones(1, 2)` (default) | M-by-N matrix

Coordinates of the battery thermal nodes on surface 2 of the cooling
plate.

When manually connecting this cooling plate to a battery, you can
obtain this information by querying the
`ThermalNodes` property of the battery object
associated with the battery block you are connecting this block to. The
`ThermalNodes` property includes information such
as the number of nodes, the 2-D location of nodes, and the dimensions of
nodes.

#### Dependencies

To enable this parameter, set **Battery
Connectivity** to `Double
sided`.

### **Number of partitions in X dimension for the cooling plate** — Number of partitions in X dimension for cooling plate `2` (default) | positive scalar

Number of partitions in the X dimension for the cooling plate. This
parameter affects the level of fidelity of the cooling plate.

### **Number of partitions in Y dimension for the cooling plate** — Number of partitions in Y dimension for the cooling plate `5` (default) | positive scalar

Number of partitions in the Y dimension for cooling plate. This
parameter affects the level of fidelity of the cooling plate.

### Plate Material

### **Thickness of cooling plate material** — Thickness of material of cooling plate `2e-3` `m` (default) | positive scalar

Thickness of the material of the cooling plate.

### **Thermal conductivity of cooling plate material** — Thermal conductivity of material of cooling plate `20` `W/(K*m)` (default) | positive scalar

Thermal conductivity of the material of the cooling plate.

### **Density of cooling plate material** — Density of material of cooling plate `2500` `kg/m^3` (default) | positive scalar

Density of the material of the cooling plate.

### **Specific heat of cooling plate material** — Specific heat of material of cooling plate `447` `J/(K*kg` (default) | positive scalar

Specific heat of the material of the cooling plate.

### **Initial temperature of the cooling plate and the coolant fluid** — Temperature of cooling plate and coolant fluid at time zero `300` `K` (default) | positive scalar

Temperature of the cooling plate and of the coolant fluid at the start
of simulation.

### Fluid Properties

### **Reynolds number upper limit for laminar flow** — Reynolds number above which flow begins to transition from laminar to turbulent `2000` (default) | scalar greater than `1`

Reynolds number above which flow begins to transition from laminar to
turbulent. This number equals the maximum Reynolds number corresponding
to fully developed laminar flow.

### **Reynolds number lower limit for turbulent flow** — Reynolds number below which flow begins to transition from turbulent to laminar `4000` (default) | positive scalar

Reynolds number below which flow begins to transition from turbulent
to laminar. This number equals to the minimum Reynolds number
corresponding to fully developed turbulent flow.

The value of this parameter must be greater than the value of the
**Reynolds number upper limit for laminar flow**
parameter.

### **Nusselt number for laminar flow heat transfer** — Ratio of convective to conductive heat transfer `3.66` (default) | positive scalar

Ratio of convective to conductive heat transfer in the laminar flow
regime. Its value depends on the pipe cross-sectional geometry and pipe
wall thermal boundary conditions, such as constant temperature or
constant heat flux. Typical value is 3.66, for a circular cross section
with constant wall temperature.

### **Aggregate equivalent length of local resistances** — Combined length of all local resistances present in the pipes `1e-3` `m` (default) | nonnegative scalar

Combined length of all local resistances present in the pipe. Local
resistances include bends, fittings, armatures, and pipe inlets and
outlets. The effect of the local resistances is to increase the
effective length of the pipe segment. This length is added to the
geometrical pipe length only for friction calculations. The liquid
volume inside the pipe depends only on the pipe geometrical
length.

### **Laminar friction constant for Darcy friction factor** — Effect of pipe geometry on the viscous friction losses `64` (default) | positive scalar

Dimensionless factor that encodes the effect of pipe cross-sectional
geometry on the viscous friction losses in the laminar flow regime.
Typical values are 64 for a circular cross section, 57 for a square
cross section, 62 for a rectangular cross section with an aspect ratio
of 2, and 96 for a thin annular cross section.

### Design

### **Select edge to be cooled** — Cooling edge `Edge cooling along Y axis at X = Xmin` (default) | `Edge cooling along X axis at Y = Ymin` | `Edge cooling along Y axis at X = Xmax` | `Edge cooling along X axis at Y = Ymax`

Option to choose which edge of the cooling plate you want to cool.

### **Cooling channel hydraulic diameter** — Hydraulic diameter of cooling channel `5e-3` `m` (default) | positive scalar

Hydraulic diameter of the cooling channel.

### **Cooling channel cross-sectional area** — Cross-sectional area of cooling channel `2e-5` `m^2` (default) | positive scalar

Internal area of the cooling channel normal to the direction of the
flow.

### **Coolant channel roughness** — Roughness of the coolant channel `1.5e-05` `m` (default) | positive scalar

Roughness of the coolant channel.
## Libraries

Simscape / Battery / Thermal

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Cooling plate with edge cooling

The Edge Cooling block models a battery cooling plate with edge cooling. Use the `buildBattery` function to create a Simscape model of a battery and
connect it to the either end of the cooling plate. You can cool any of the four edges of
the cooling plate. To learn how to connect a cooling plate block to a battery, see Connect Battery Block to Cooling Plate Block Automatically.

Typically, a cooling plate comprises two stamped flat plates joined together. The stamped
portion of the plate forms a channel in which the fluid can flow. The Edge Cooling block
models the flat material of the plate by using one or more Thermal Mass blocks and the fluid-flow through the cooling channels by
using Pipe (TL) blocks. The number of Pipe
(TL) blocks and their connection to the plate depend on the
discretization. For more information on the implementation of the Pipe
(TL) block and its equations, see the Pipe (TL) documentation page.

The thermal masses of the cooling plate exchange heat with each other through heat conduction
by using this equation:

Q=K A dTdx,

where *T* is the temperature, *K* is
the plate thermal conductivity, and *A* and *x* depend on
the plate thickness and on the number of partitions and directions, *x* or
*y*.

The fluid carries the heat away, or heats the battery pack, through these thermal masses. A
thermal mass that is not connected to a pipe can only add or remove heat from a battery
based on the heat conduction parameters that you specify.

### Cooling Plate Discretization

The **Number of partitions in X direction** and **Number
of partitions in Y direction** parameters control the discretization of
the cooling plate.

If you set the **Number of partitions in X direction** and
**Number of partitions in Y direction** parameters to 1, the
cooling plate is a lumped mass with a single thermal mass value. The software
calculates this thermal mass from the value of the parameters in the **Plate Material** section. In this example, the
**Select edge to be cooled** parameter is set to
`Edge cooling along Y axis at X = Xmax`. The software
then places one Pipe (TL) block along the
*Y*-axis at the maximum *X*-axis value and
connects them to the cooling plate. During the simulation, the cooling plate has one
temperature value at each time step. Consequently, each cell of the battery pack
connected to this cooling plate measures the same plate temperature value.

To increase the model fidelity, change the value of the **Number of
partitions in X direction** to 2. The software now divides the cooling
plate along the X dimension in two regions. Each region comprises a separate thermal
mass. With this configuration, the Pipe (TL) block
connects to both regions of the plate. During the simulation, the cooling plate has
two different temperature values, one for each region of the plate.

To increase the model fidelity even further, change the value of the
**Number of partitions in Y direction** to 3. The software
discretizes the cooling plate along the Y dimension in three regions. The total
number of regions in the cooling plate is now six. Since the Y direction is also the
direction of the coolant flow, the software discretizes the cooling pipe as well.
Instead of one Pipe (TL) block for each couple of
partitions in the X direction, this configuration comprises one Pipe
(TL) block for each couple of partitions in the X direction.
During the simulation, this cooling plate has six different temperature values at
each time step. Consequently, the cells of the battery pack connected to this plate
measure a temperature value that depends on the position of the cells.

For more information about cooling plates and their connection to battery blocks,
see Connect Cooling Plate to Battery Blocks.
