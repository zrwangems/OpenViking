---
type: simulink-block
title: 'Parallel Channels'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'Thermal'
documentation_page: 'parallelchannels'
documentation_source_path: 'ref/parallelchannels.html'
language: en
---

# Parallel Channels

## Ports

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

### **Dimension of battery thermal nodes (surface 1)** — Dimension of battery thermal nodes on surface 1 `ones(1, 2)` (default) | M-by-N matrix

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

### **Number of coolant channels** — Number of coolant channels `4` (default) | positive scalar

Number of the coolant channels inside the cooling plate.

### **Select channel orientation direction** — Option for direction of channel orientation `Channel along X axis` (default) | `Channel along Y axis`

Option to choose the axis direction of the channel orientation. You
can place the channels along the X axis or the Y axis. This figure shows
the coolant channels and the distributor pipes for a cooling plate with
3 channels in both the X direction and the Y direction.

### **Cooling channel hydraulic diameter** — Hydraulic diameter of cooling channel `0.005` `m` (default) | positive scalar

Diameter of an equivalent cylindrical pipe with the same
cross-sectional area.

### **Distributor pipe diameter** — Diameter of distributor pipe `0.005` `m` (default) | positive scalar

Diameter of the distributor pipe.

### **Coolant channel and distributor roughness** — Roughness of coolant channel and distributor `1.5e-05` `m` (default) | positive scalar

Roughness of the coolant channel and of the distributor.

## Libraries

Simscape / Battery / Thermal

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Cooling plate with multiple parallel channels

The Parallel Channels block models a battery cooling plate with multiple channels and a pair of
distributor channels for inlet and outlet flow. Use the `buildBattery` function to create a Simscape model of a battery and
connect it to either end of the cooling plate. To learn how to connect a cooling plate
block to a battery, see Connect Battery Block to Cooling Plate Block Automatically.

Typically, a cooling plate comprises two stamped flat plates joined together. The stamped
portion of the plate forms a channel in which the fluid can flow. The Parallel Channels block
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
calculates this thermal mass from the value of the parameters in the **Plate Material** section. In this example, the value of the
**Number of coolant channels** parameter is equal to 2 and the
**Select channel orientation direction** parameter is set to
`Channels along Y axis`. The software then places two
Pipe (TL) blocks along the
*Y*-axis and connects them to the cooling plate. During the
simulation, the cooling plate has one temperature value at each time step.
Consequently, each cell of the battery pack connected to this cooling plate measures
the same plate temperature value.

To increase the model fidelity, change the value of the **Number of
partitions in X direction** to 2. The software now divides the cooling
plate along the X dimension in two regions. Each region comprises a separate thermal
mass. With this configuration, each Pipe (TL) block
connects to a different region of the plate. During the simulation, the cooling
plate has two different temperature values, one for each region of the plate.

To increase the model fidelity even further, change the value of the
**Number of partitions in Y direction** to 3. The software
discretizes the cooling plate along the Y dimension in three regions. The total
number of regions in the cooling plate is now six. Since the Y direction is also the
direction of the coolant flow, the software discretizes the cooling pipes as well.
Instead of one Pipe (TL) block per cooling channel,
this configuration comprises three pipe blocks for each cooling channel. Each region
of the plate then connects to a different Pipe (TL)
block. During the simulation, this cooling plate has six different temperature
values at each time step. Consequently, the cells of the battery pack connected to
this plate measure a temperature value that depends on the position of the cells.

For more information about cooling plates and their connection to battery blocks,
see Connect Cooling Plate to Battery Blocks.
