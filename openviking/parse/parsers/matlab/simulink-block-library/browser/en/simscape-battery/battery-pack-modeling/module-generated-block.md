---
type: simulink-block
title: 'Module (Generated Block)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Pack Modeling'
documentation_page: 'modulegeneratedblock'
documentation_source_path: 'ref/modulegeneratedblock.html'
language: en
---

# Module (Generated Block)

## Ports

### Input

### **CB** — Cell balancing, unitless physical signal

Cell balancing port, specified as a physical signal.

#### Dependencies

To enable this port, set the `BalancingStrategy` property of
the `Module` object to `"Passive"`.
Alternatively, set the `BalancingStrategy` property to
`"Passive"` inside the parent object of which the
`Module` object is a subcomponent.
### Output

**Note**

The output ports of this block depend on the Simscape cell model block you used to create the battery object associated with this
block. If the Simscape cell model block has output ports, the Battery Builder forwards these output
ports to all the parent generated blocks of which the battery object is a
subcomponent.

For example, if you create a custom Simscape cell model block with a **Voltage** output port and
eventually use it to create this block, then this block has a **Voltage**
output port. For more information about custom cell model blocks, see the
`CellModelBlockPath` property of the `CellModelBlock`
object.

### **SOC** — State of charge, unitless physical signal

*Since R2024b*

State of charge at cell level, specified as a physical signal.

#### Dependencies

To enable this port, use the Battery (Table-Based) block as the component model
block for the `Cell` child object of this block and enable the
**SOC** port.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive terminal of the battery
module.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative terminal of the battery
module.

### **AmbH** — Ambient thermal port thermal

Thermal conserving port associated with the ambient thermal path.

#### Dependencies

To enable this port, set the `AmbientThermalPath` property of
the `Module` object to
`"CellBasedThermalResistance"`. Alternatively, set the
`AmbientThermalPath` property to
`"CellBasedThermalResistance"` inside the parent object
of which the `Module` object is a subcomponent.

### **ClntH** — Coolant thermal port thermal

Thermal conserving port associated with the coolant thermal path.

#### Dependencies

To enable this port, set the `CoolantThermalPath` property of
the `Module` object to
`"CellBasedThermalResistance"`. Alternatively, set the
`CoolantThermalPath` property to
`"CellBasedThermalResistance"` inside the parent object
of which the `Module` object is a subcomponent.

**Note**

If you set the `CoolingPlate` property to either
`"Top"` or `"Bottom"` inside
the `Module` object or inside the top-level parent object of
which the `Module` object is a subcomponent, then this port is
not enabled.

### **XminH** — Thermal port at Xmin boundary thermal | `N`-by-`1` vector | scalar

*Since R2024a*

Thermal conserving port associated with the minimum X-axis surface boundary,
specified as an `N`-by-`1` vector or a
scalar.

#### Dependencies

To enable this port, set the `XminThermalNodes` property of
the `Module` object to `"Scalar"` or
`"Vectorized"`.

### **XmaxH** — Thermal port at Xmax boundary thermal | `N`-by-`1` vector | scalar

*Since R2024a*

Thermal conserving port associated with the maximum X-axis surface boundary,
specified as an `N`-by-`1` vector or a
scalar.

#### Dependencies

To enable this port, set the `XmaxThermalNodes` property of
the `Module` object to `"Scalar"` or
`"Vectorized"`.

### **YminH** — Thermal port at Ymin boundary thermal | `N`-by-`1` vector | scalar

*Since R2024a*

Thermal conserving port associated with the minimum Y-axis surface boundary,
specified as an `N`-by-`1` vector or a
scalar.

#### Dependencies

To enable this port, set the `YminThermalNodes` property of
the `Module` object to `"Scalar"` or
`"Vectorized"`.

### **YminH** — Thermal port at Ymax boundary thermal | `N`-by-`1` vector | scalar

*Since R2024a*

Thermal conserving port associated with the maximum Y-axis surface boundary,
specified as an `N`-by-`1` vector or a
scalar.

#### Dependencies

To enable this port, set the `YmaxThermalNodes` property of
the `Module` object to `"Scalar"` or
`"Vectorized"`.

### **SP** — Thermal port at serpentine boundary thermal

*Since R2024a*

Thermal conserving port associated with the serpentine cooling plate
boundary.

#### Dependencies

To enable this port, set the `SerpentineCoolingPlate`
property of the `Module` object to
`"SingleSidedAlongStackingAxis"` or
`"DoubleSidedAlongStackingAxis"`.

### **CPT** — Cooling plate top port thermal array-of-nodes

Thermal conserving port used to connect the top side of the module with a cooling
plate. The size of this port depends on the number of models in the system. If you set
the `ModelResolution` property to
`“Lumped”`, this port outputs a scalar. If you set the
`ModelResolution` property to
`“Detailed”`, this port outputs a vector of size equal to
the number of cells in the system. If you set the `ModelResolution`
property to `“Grouped”`, this port outputs a vector of size
depending on the grouping strategy.

#### Dependencies

To enable this port, set the `CoolingPlate` property of the
`Module` object to `"Top"`. Alternatively,
set the `CoolingPlate` property to
`"Top"` inside the parent object of which the
`Module` object is a subcomponent.

### **CPB** — Cooling plate bottom port thermal array-of-nodes

Thermal conserving port used to connect the bottom side of the module with a
cooling plate. The size of this port depends on the number of models in the system. If
you set the `ModelResolution` property to
`“Lumped”`, this port outputs a scalar. If you set the
`ModelResolution` property to
`“Detailed”`, this port outputs a vector of size equal to
the number of cells in the system. If you set the `ModelResolution`
property to `“Grouped”`, this port outputs a vector of size
depending on the grouping strategy.

#### Dependencies

To enable this port, set the `CoolingPlate` property of the
`Module` object to `"Bottom"`.
Alternatively, set the `CoolingPlate` property to
`"Bottom"` inside the parent object of which the
`Module` object is a subcomponent.

### **+BUS** — Positive terminal bus electrical array-of-nodes

*Since R2024a*

Electrical array-of-nodes conserving port associated with the positive terminals
of the parallel assemblies inside this module. Each element of this array corresponds
to a positive terminal of a parallel assembly inside this module.

#### Dependencies

To enable this port, set the `BalancingStrategy` property of
the `Module` object to `"External"`.
Alternatively, set the `BalancingStrategy` property to
`"External"` inside any of the parent battery objects of
which the `Module` object is a subcomponent.

### **-BUS** — Negative terminal bus electrical array-of-nodes

*Since R2024a*

Electrical array-of-nodes conserving port associated with the negative terminals
of the parallel assemblies inside this module. Each element of this array corresponds
to a negative terminal of a parallel assembly inside this module.

#### Dependencies

To enable this port, set the `BalancingStrategy` property of
the `Module` object to `"External"`.
Alternatively, set the `BalancingStrategy` property to
`"External"` inside any of the parent battery objects of
which the `Module` object is a subcomponent.

## Parameters

**Note**

The names of these parameters and variables depend on the block you have specified in
the `CellModelOptions` property of the underlying `Cell`
object that constitutes this module.

The names of the parameters and variables in this page refer to a `Cell`
object with the Battery
(Table-Based) block as the cell component model block. If you specify a
custom block for the cell component model, the names of the parameters and variables might
differ.

The parameters of this block need to be set for the cell-level and depend on how you
define the `Module` object that
you use to generate this custom model. The block parameters are divided into these sections:

- Main
- Dynamics
- Fade
- Calendar Aging
- Thermal
- Cell Balancing

The visibility of each section also depends on the generated `Module`
object.

For a list of the parameters in the **Main**,
**Dynamics**, **Fade**, and **Calendar
Aging** sections, see the documentation page of the Battery
(Table-Based) block.

If, in the `Module` object that
you use to generate this custom model, you set the `CellParameterDeviation`
property to `"PercentDeviation"`, each cell parameter (that is not an
enumeration or a boolean) has an associated **Percent deviation**
parameter:

### **Percent deviation for k** — Percent deviation for specific cell parameter vector of scalars | matrix

*Since R2023b*

Percent deviation of the value of the corresponding cell parameter
*k* for each cell model in the battery. *k* is the
name of the cell parameter associated with this percent deviation.

The number of parameters of this type is equal to the number of cell parameters in
this block. Parameters of type enumeration and boolean do not have an associated
**Percent deviation** parameter.

The value of the corresponding cell parameter with the deviation applied is equal
to:

cellParameter=1+(cellParameterDeviation100)∗exposedCellParameter.

For this parameter, you can specify either:

- A vector, with one element for each cell model in the battery. These elements
  are concatenated vertically. For example, for a `Module` object
  with two parallel assemblies, three cells, and the
  `ModelResolution` property set to
  `"Detailed"`, this vector requires six elements. For a
  `Module` object with the `ModelResolution`
  property set to `"Grouped"`, the size of this vector
  depends on the number of cells modeled in the module. The number of modeled cells
  is equal to the sum of the elements of the `Parallel grouping simulation
  strategy` property. You can find this property in the
  **Description** tab of the **Property
  Inspector** of the Module block.
- A matrix, where each element of the matrix is either a scalar or a matrix of
  the same size of the underlying associated cell parameter. The parameter deviation
  elements are concatenated vertically. For example, if a cell parameter has a size
  of `[2,7]` and a detailed parallel assembly comprises two cells,
  then the size of the **Percent Deviation** for this parameter is
  equal to `[4,7]`.

For more information about cell-to-cell parameter variation, see the Apply Temperature-Dependent Cell Parameter Variations to Battery Module
example.

#### Dependencies

To enable this parameter, set the `CellParameterDeviation`
property of the `Module` object to
`"PercentDeviation"`.

### Thermal

### **Thermal mass** — Thermal mass at cell level `100` `J/K` (default) | positive scalar

Thermal inertia of a single battery cell. This value represents the energy
required to raise the temperature of the thermal port by one degree.

The Module block automatically scales this value up to the system level.

### **Cell level coolant thermal path resistance** — Coolant thermal path resistance at cell level `1.2` `K/W` (default) | positive scalar | row vector of positive scalars

Resistance of the coolant thermal path at cell level. The size of this parameter
is equal to the total number of electrical models in the system.

#### Dependencies

To enable this parameter, set the `CoolantThermalPath`
property of the `Module` object to
`"CellBasedThermalResistance"`. Alternatively, set the
`CoolantThermalPath` property to
`"CellBasedThermalResistance"` inside the parent object
of which the `Module` object is a subcomponent.

### **Cell level ambient thermal path resistance** — Ambient thermal path resistance at cell level `25` `K/W` (default) | positive scalar | row vector of positive scalars

Resistance of the ambient thermal path at cell level. The size of this parameter
is equal to the total number of electrical models in the system.

#### Dependencies

To enable this parameter, set the `CoolantThermalPath`
property of the `Module` object to
`"CellBasedThermalResistance"`. Alternatively, set the
`CoolantThermalPath` property to
`"CellBasedThermalResistance"` inside the parent object
of which the `Module` object is a subcomponent.

### **Inter-cell thermal path resistance** — Thermal path resistance between cells `1` `K/W` (default) | scalar | row vector of scalars

*Since R2023a*

Resistance of the thermal path between the cells inside the module. The size of
this parameter must be equal to the number of inter-cell thermal connections that this
block models.

#### Dependencies

To enable this parameter, set the `InterCellThermalPath`
property of the `Module` object to `"On"`.
Alternatively, set the `InterCellThermalPath` property to
`"On"` inside the parent object of which the
`Module` object is a subcomponent.

### **Inter-parallel assembly thermal path resistance** — Thermal path resistance between parallel assemblies `1` `K/W` (default) | scalar | row vector of scalars

*Since R2023a*

Resistance of the thermal path between the parallel assemblies inside the module.
The size of this parameter must be equal to the number of inter-parallel assembly
thermal connections that this block models.

#### Dependencies

To enable this parameter, set the `InterCellThermalPath`
property of the `Module` object to `"On"`.
Alternatively, set the `InterCellThermalPath` property to
`"On"` inside the parent object of which the
`Module` object is a subcomponent.

### **Inter-cell radiation heat transfer area** — Transfer area of radiation heat between cells `1e-3` `m^2` (default) | scalar | row vector of scalars

*Since R2023a*

Area of the radiation heat transfer between the cells inside the module. The size
of this parameter must be equal to the number of inter-cell thermal connections that
this block models.

#### Dependencies

To enable this parameter, set the
`InterCellRadiativeThermalPath` property of the
`Module` object to `"On"`. Alternatively,
set the `InterCellRadiativeThermalPath` property to
`"On"` inside the parent object of which the
`Module` object is a subcomponent.

### **Inter-cell radiation heat transfer coefficient** — Coefficient of radiation heat transfer between cells `1e-6` `W/(K^4*m^2)` (default) | scalar | row vector of scalars

*Since R2023a*

Coefficient of the radiation heat transfer between the cells inside the module.
The size of this parameter must be equal to the number of inter-cell thermal
connections that this block models.

#### Dependencies

To enable this parameter, set the
`InterCellRadiativeThermalPath` property of the
`Module` object to `"On"`. Alternatively,
set the `InterCellRadiativeThermalPath` property to
`"On"` inside the parent object of which the
`Module` object is a subcomponent.

### **Inter-parallel assembly area for radiation heat transfer** — Area of radiation heat transfer between parallel assemblies `1e-3` `m^2` (default) | scalar | row vector of scalars

*Since R2023a*

Area of the radiation heat transfer between the parallel assemblies inside the
module. The size of this parameter must be equal to the number of inter-parallel
assemblies thermal connections that this block models.

#### Dependencies

To enable this parameter, set the
`InterCellRadiativeThermalPath` property of the
`Module` object to `"On"`. Alternatively,
set the `InterCellRadiativeThermalPath` property to
`"On"` inside the parent object of which the
`Module` object is a subcomponent.

### **Inter-parallel assembly coefficient for radiation heat transfer** — Coefficient of radiation heat transfer between parallel assemblies `1e-6` `W/(K^4*m^2)` (default) | scalar | row vector of scalars

*Since R2023a*

Coefficient of the radiation heat transfer between the parallel assemblies inside
the module. The size of this parameter must be equal to the number of inter-parallel
assemblies thermal connections that this block models.

#### Dependencies

To enable this parameter, set the
`InterCellRadiativeThermalPath` property of the
`Module` object to `"On"`. Alternatively,
set the `InterCellRadiativeThermalPath` property to
`"On"` inside the parent object of which the
`Module` object is a subcomponent.

### **Cell-level thermal path resistance at Xmin boundary** — Thermal path resistance of cells at Xmin boundary `25` `K/W` (default) | positive scalar | row vector of positive scalars

*Since R2024a*

Resistance of the thermal path at the cell level at the minimum X-axis boundary.
The size of this parameter is equal to the total number of Xmin thermal connections
that the block models.

#### Dependencies

To enable this port, set the `XminThermalNodes` property of
the `Module` object to `"Scalar"` or
`"Vectorized"`.

### **Cell-level thermal path resistance at Xmax boundary** — Thermal path resistance of cells at Xmax boundary `25` `K/W` (default) | positive scalar | row vector of positive scalars

*Since R2024a*

Resistance of the thermal path at the cell level at the maximum X-axis boundary.
The size of this parameter is equal to the total number of Xmax thermal connections
that the block models.

#### Dependencies

To enable this port, set the `XmaxThermalNodes` property of
the `Module` object to `"Scalar"` or
`"Vectorized"`.

### **Cell-level thermal path resistance at Ymin boundary** — Thermal path resistance of cells at Ymin boundary `25` `K/W` (default) | positive scalar | row vector of positive scalars

*Since R2024a*

Resistance of the thermal path at the cell level at the minimum Y-axis boundary.
The size of this parameter is equal to the total number of Ymin thermal connections
that the block models.

#### Dependencies

To enable this port, set the `YminThermalNodes` property of
the `Module` object to `"Scalar"` or
`"Vectorized"`.

### **Cell-level thermal path resistance at Ymax boundary** — Thermal path resistance of cells at Ymax boundary `25` `K/W` (default) | positive scalar | row vector of positive scalars

*Since R2024a*

Resistance of the thermal path at the cell level at the maximum Y-axis boundary.
The size of this parameter is equal to the total number of Ymax thermal connections
that the block models.

#### Dependencies

To enable this port, set the `YmaxThermalNodes` property of
the `Module` object to `"Scalar"` or
`"Vectorized"`.

### **Cell-level thermal path resistance at serpentine boundary** — Thermal path resistance of cells at serpentine boundary `25` `K/W` (default) | positive scalar | row vector of positive scalars

*Since R2024a*

Resistance of the thermal path at the cell level at the serpentine boundary. The
size of this parameter is equal to the total number of serpentine thermal connections
that the block models.

#### Dependencies

To enable this port, set the `SerpentineCoolingPlate`
property of the `Module` object to
`"SingleSidedAlongStackingAxis"` or
`"DoubleSidedAlongStackingAxis"`.

### Parallel Assembly

### **Non-cell electrical resistance** — Parallel assembly non-cell resistance `1 / 1000` `Ohm` (default) | positive scalar

Non-cell electrical resistance of each parallel assembly in the module.

#### Dependencies

To enable this parameter, set the `NonCellResistance`
property of the `Module` object to `"On"`.
Alternatively, set the `NonCellResistance` property to
`"On"` inside the parent object of which the
`Module` object is a subcomponent.

### Module

### **Non-cell electrical resistance** — Module non-cell resistance `1 / 1000` `Ohm` (default) | positive scalar

Non-cell electrical resistance of the module.

#### Dependencies

To enable this parameter, set the `NonCellResistance`
property of the `Module` object to `"On"`.
Alternatively, set the `NonCellResistance` property to
`"On"` inside the parent object of which the
`Module` object is a subcomponent.

### Cell Balancing

### **Cell balancing switch closed resistance** — Closed resistance of cell balancing switch `0.01` `Ohm` (default) | positive scalar

Closed resistance of the cell balancing switch.

### **Cell balancing switch open conductance** — Open conductance of cell balancing switch `1e-8` `1/Ohm` (default) | positive scalar

Open conductance of the cell balancing switch.

### **Cell balancing switch operation threshold** — Threshold for cell balancing switch operation `0.5` (default) | positive scalar

Threshold to activate the cell balancing switch operation.

### **Cell balancing shunt resistance** — Resistance of cell balancing shunt `50` `Ohm` (default) | positive scalar

Resistance of the cell balancing shunt.

### Initial Targets (Variables)

The size of these variables is equal to the total number of electrical models in the
system. For example, in a Module block with 2 parallel assemblies and 2 series cells, the
size of the variables depends on the `ModelResolution` property of the
`Module` object and is equal to `4` for
`Detailed`, `1` for
`Lumped`, or `3` when the
`SeriesGrouping` property is equal to `[1 1]` and the
`ParallelGrouping` property is equal to `[1
2]`.

### **Cell current (positive in)** — Cell-level current, iCell `0` `A` (default) | scalar | vector

Current at the cell level. The size of this variable is equal to the total number
of electrical models in the system.

### **Cell terminal voltage** — Cell-level voltages, vCell `0` `V` (default) | scalar | vector

Voltages at the cell level. The size of this signal is equal to the total number
of electrical models in the system.

### **Cell state of charge** — Cell-level state of charge, socCell `1` (default) | scalar | vector

State of charge at cell level. The value of this variable typically varies between
0 and 1. The size of this signal is equal to the total number of electrical models in
the system.

### **Cell discharge cycles** — Cell-level number of cycles, numCyclesCell `0` (default) | scalar | vector

Cell-level number of cycles related to battery aging. The size of this signal is
equal to the total number of electrical models in the system.

### **Cell temperature** — Cell-level temperature, temperatureCell `298.15` `K` (default) | positive scalar

Temperature at the cell level. The size of this signal is equal to the total
number of electrical models in the system.

### **Parallel Assembly Voltage** — Parallel assembly-level voltages, vParallelAssembly `repmat(0,4,1)` `V` (default) | scalar | vector

Voltages at the parallel assembly level. The size of this signal is equal to the
total number of parallel assemblies in the module.

### **Parallel Assembly state of charge** — State of charge at parallel assembly level, socParallelAssembly `repmat(1,4,1)` (default) | scalar | vector

State of charge at the parallel assembly level. The size of this signal is equal
to the total number of parallel assemblies in the module.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022b**

### R2024b: Expose the cell-level output ports in parent battery blocks

This block now exposes the same output ports of the cell model block that you specify in
the `CellModelBlockPath` property of the `CellModelBlock`
object associated with this block.

### R2024a: Expose electrical array-of-nodes ports for external cell balancing strategy

You can now expose two electrical array-of-nodes ports, **+BUS** and
**-BUS**, to specify and model an external cell balancing strategy for desktop
simulations and hardware-in-the-loop battery emulation hardware. Use this option in
conjunction with the Passive Balancing
Interface block.

To specify and model an external cell balancing strategy, set the
`BalancingStrategy` property to `"External"`
in the `Module` object
that you use to generate this custom model.

### R2024a: Expose thermal ports for cells at specific surface boundaries

For a more detailed thermal modeling of the battery cells in the battery pack
environment, you can now expose the ports associated with the thermal nodes of the cells
located at the surface boundaries of the module. To expose these thermal ports, specify the
`XminThermalNodes`, `XmaxThermalNodes`,
`YminThermalNodes`, and `YmaxThermalNodes`
properties in the `Module` object
that you use to generate this custom model.

For modules with hexagonal cylindrical cells, you can also enable the heat transfer
between the cells of the module and a serpentine cooling plate. To expose the thermal ports
associated with the serpentine cooling plate inside the module, specify the
`SerpentineCoolingPlate` property.

### R2023b: Specify parameter values for each cell model in the system

You can now specify the parameter values for each cell model inside your battery system.
To support specific cell parameterization, you must set the
`CellParameterDeviation` property to
`"PercentDeviation"` in the `Module` object
that you use to generate this custom model. This action enables a **Percent
deviation** parameter for the cell parameters in the generated Module
block that specifies the percent deviation of the value of corresponding cell parameter for
each cell model in the battery.

## Description

Generated Simscape model of battery module

The Module block represents a custom generated system model of a battery module. You can
create this Simscape™ block by using the `buildBattery`
function with a `Module` object as
an input argument. The Module generated block is inside the Simulink library that you specify
in the `LibraryName` argument of the `buildBattery`
function.

**Note**

To allow for structural changes and further customization, when you add the Module (Generated Block) masked library block from the parent library to a Simulink® model, the linked block does not contain the link or path to the parent library block. If you modify any of the battery structural properties, such as `NumSeriesAssemblies` or `NumParallelCells`, you must rebuild the original parent library and copy the block in your model again.

For more information about parent and linked blocks, see Linked Blocks.

### Variables

To set the priority and initial target values for the block variables prior to
simulation, use the **Initial Targets** section in the block dialog box or
Property Inspector. For more information, see Set Priority and Initial Target for Block Variables.

For a detailed list of the variables in the ParallelAssembly block, see the Initial Targets (Variables)
section.

**Note**

The values of variables for cell-level components refer to the value of a single physical cell and not that of a cell model. *(since R2023a)*

For example, consider a parallel assembly with 10 cells in parallel and a lumped model resolution. The ParallelAssembly generated block exposes the variable *v* of the cell component as *vCell*. For a cell with a voltage of 4.2 V, *vCell* is equal to `4.2 V`. Before R2023a, the generated blocks exposed the cell variables with the suffix *CellModel* and represented the variables of the entire model they represented. For example, using the previous ParallelAssembly generated block, the block exposed a *vCellModel* variable with a value equal to *4.2\*10 = 42V*.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
