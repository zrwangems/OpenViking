---
type: simulink-block
title: 'Pack (Generated Block)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Battery Pack Modeling'
documentation_page: 'packgeneratedblock'
documentation_source_path: 'ref/packgeneratedblock.html'
language: en
---

# Pack (Generated Block)

## Ports

### Input

### **balancing** — Balancing switch control, unitless scalar

Switch control port for the balancing strategy, specified as a scalar.

#### Dependencies

To enable this port, set the `BalancingStrategy` property of
the `Pack` object to `"Passive"`.
### Output

**Note**

The names of the output ports depend on the block you have specified in the
`CellModelOptions` property of the underlying `Cell`
object that constitutes this pack.

The names of the output ports in this page refer to a `Cell` object
with the Battery
(Table-Based) block as the cell component model block. If you specify a
custom block for the cell component model, the names of the output ports might
differ.

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

### **iCell** — Cell-level current, Ampere scalar | vector

Current at the cell level. The original signal units from the Module block are
Amperes. The size of this signal is equal to the total number of electrical models in
the system.

### **numCyclesCell** — Cell-level number of cycles, unitless scalar | vector

Cell-level number of cycles related to battery aging. The original signal units
from the Module block are unitless. The size of this signal is equal to the total
number of electrical models in the system.

### **socCell** — Cell-level state of charge, unitless scalar | vector

State of charge at the cell level. The original signal units from the Module block
are unitless and the value typically varies between 0 and 1. The size of this signal
is equal to the total number of electrical models in the system.

### **socParallelAssembly** — State of charge at parallel assembly level, unitless scalar | vector

State of charge at the parallel assembly level. The original signal units from the
Module block are unitless and the value typically varies between 0 and 1. The size of
this signal is equal to the total number of parallel assemblies in the module
assembly.

### **temperatureCell** — Cell-level temperature, kelvin scalar | vector

Temperature at the cell level. The original signal units from the Module block are
kelvin. The size of this signal is equal to the total number of electrical models in
the system.

#### Dependencies

To enable this port, enable the thermal port of the cells that comprise the
pack. To model the thermal port of the cells, in the
`CellModelBlock` property of the cells, set the
**thermal\_port** parameter of the
`BlockParameters` property to
`"Model"`.

### **vCell** — Cell-level voltages, volts scalar | vector

Voltages at the cell level. The original signal units from the Module block are
volts. The size of this signal is equal to the total number of electrical models in
the system.

### **vParallelAssembly** — Parallel assembly-level voltages, volts scalar | vector

Voltages at the parallel assembly level. The original signal units from the Module
block are volts. The size of this signal is equal to the total number of parallel
assemblies in the pack. Use this signal as an input to the battery management system
(BMS) blocks of Simscape Battery.

### **CP\_Out** — Outputs of each cooling plate in model vector of physical signals

*Since R2023a*

Vector that contains the plate temperature, the fluid pressure drop, and the fluid
temperature change of each cooling plate in the model. The size of this port depends
on the number of cooling plates in the model.

#### Dependencies

To enable this port, set the `CoolingPlate` property of the
`Pack` object to either `"Top"` or
`"Bottom"`.

### **SOC** — State of charge, unitless scalar | vector

*Since R2024b*

State of charge at cell level, specified as a scalar or vector.

#### Dependencies

To enable this port, use the Battery (Table-Based) block as the component model
block for the `Cell` child object of this block and enable the
**SOC** port.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive terminal of the battery
pack.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative terminal of the battery
pack.

### **AmbH** — Ambient thermal port thermal

Thermal conserving port associated with the ambient thermal path.

#### Dependencies

To enable this port, set the `AmbientThermalPath` property of
the `Pack` object to
`"CellBasedThermalResistance"`.

### **ClntH** — Coolant thermal port thermal

Thermal conserving port associated with the coolant thermal path.

#### Dependencies

To enable this port, in the `Pack` object, set the
`CoolantThermalPath` property to
`"CellBasedThermalResistance"` and the
`CoolingPlate` property to
`"None"`.

### **Fluid\_In** — Fluid in cooling plate thermal fluid

*Since R2023a*

Thermal fluid conserving port associated with the fluid that comes in each cooling
plate of the model. The size of this port depends on the number of cooling plates in
the model.

#### Dependencies

To enable this port, set the `CoolingPlate` property of the
`Pack` object to either `"Top"` or
`"Bottom"`.

### **Fluid\_Out** — Fluid out of cooling plate thermal fluid

*Since R2023a*

Thermal fluid conserving port associated with the fluid that comes out of each
cooling plate in the model. The size of this port depends on the number of cooling
plates in the model.

#### Dependencies

To enable this port, set the `CoolingPlate` property of the
`Pack` object to either `"Top"` or
`"Bottom"`.

### **+BUS** — Positive terminal bus electrical array-of-nodes

*Since R2024a*

Electrical array-of-nodes conserving port associated with the positive terminals
of the parallel assemblies inside this pack. Each element of this array corresponds to
a positive terminal of a parallel assembly inside this pack.

#### Dependencies

To enable this port, set the `BalancingStrategy` property of
the `Pack` object to `"External"`.

### **-BUS** — Negative terminal bus electrical array-of-nodes

*Since R2024a*

Electrical array-of-nodes conserving port associated with the negative terminals
of the parallel assemblies inside this pack. Each element of this array corresponds to
a negative terminal of a parallel assembly inside this pack.

#### Dependencies

To enable this port, set the `BalancingStrategy` property of
the `Pack` object to `"External"`.

## Parameters

Not documented in R2025b.

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
in the `Pack` object that
you use to generate this custom model.

## Description

Generated Simscape model of battery pack

The Pack block is a custom generated subsystem model of a battery pack. You can create
this Simscape™ subsystem by using the `buildBattery`
function with a `Pack` object as an
input argument. The Pack subsystem block is inside the Simulink® library that you specify in the `LibraryName` argument of the
`buildBattery` function.

**Note**

To allow for structural changes and further customization, when you add the Pack (Generated Block) masked library block from the parent library to a Simulink model, the linked block does not contain the link or path to the parent library block. If you modify any of the battery structural properties, such as `NumSeriesAssemblies` or `NumParallelCells`, you must rebuild the original parent library and copy the block in your model again.

For more information about parent and linked blocks, see Linked Blocks.

The Pack subsystem model comprises six major sections.

- The Battery Module Assemblies section displays all the ModuleAssembly subsystems
  defined in the `Pack` object. This section contains all the series and
  parallel electrical circuit connections between the module assemblies, as well as the
  additional connections to the main electrical terminals and the
  ModuleAssembly-to-thermal boundary conditions. If you require additional
  non-ModuleAssembly resistances, then the function adds and connects two additional
  electrical resistors here.
- The Output signals section groups the output of each ModuleAssembly subsystem into a
  single multiplexed output signal for the Pack subsystem.
- The Thermal Boundary Conditions section contains the thermal boundary conditions for
  each ModuleAssembly subsystem. The `buildBattery` function adds a
  connector port from the thermal domain and routes it to every ModuleAssembly subsystem
  according to the specified thermal boundary conditions. This section is optional and
  only appears if you define an ambient or coolant thermal path in the
  `Pack` object.
- The Balancing Signals section contains the routing of the cell balancing control
  signal from the battery management system to every ModuleAssembly subsystem. Selector
  blocks route the correct elements of the control signal to their corresponding
  ParallelAssembly blocks.
- The Coolant Thermal Liquid section contains the thermal liquid network manifold for
  the coolant that circulates inside the battery cooling plates. This section is optional
  and only appears if you define a cooling plate in the `Pack`
  object.
- The Cell Outputs section groups each output of the cell model block into a
  corresponding multiplexed output signal for the Pack subsystem.

### Battery Module Assemblies

This figure shows the Battery Module Assemblies section for a Pack subsystem made of
four battery module assemblies.

### Output Signals

This figure shows the Output Signals section for a Pack subsystem made of four battery
module assemblies.

### Thermal Boundary Conditions

This figure shows the Thermal Boundary Conditions section for a Pack subsystem made of
four battery module assemblies.

### Balancing Signals

This figure shows the Balancing Signals section for a Pack subsystem made of four
battery module assemblies.

### Coolant Thermal Liquid

This figure shows the Coolant Thermal Liquid section for a Pack subsystem made of four
battery module assemblies.
