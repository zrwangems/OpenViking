---
type: simulink-block
title: 'Gas Properties (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Utilities'
documentation_page: 'gaspropertiesg'
documentation_source_path: 'ref/gaspropertiesg.html'
language: en
---

# Gas Properties (G)

## Ports

### Conserving

### **A** — Connection port gas

Gas conserving port that connects the block to the gas network. You can connect it to any
point on a gas connection line in a block diagram. When you connect the
Gas Properties (G) block to a gas
line, the software automatically identifies the gas blocks connected to
the particular circuit and propagates the gas properties to all the
blocks in the circuit.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Gas / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2023a: Control block behavior when gas properties go out of range during simulation

Previously, if gas properties went beyond the valid range during simulation, the
block would return an error. You can now use the new **Pressure and
temperature outside valid range** parameter to control the block
behavior if gas properties go out of range during simulation.

## Description

Global gas properties for attached circuit

The Gas Properties (G) block defines the gas properties that
act as global parameters for all the blocks connected to a circuit. The default gas is
dry air.

Each topologically distinct gas circuit in a diagram can have a Gas Properties
(G) block connected to it. If no Gas Properties
(G) block is attached to a circuit, the blocks in this circuit use
the gas properties corresponding to the default Gas Properties
(G) block parameter values.

The Gas Properties (G) block lets you select between three gas
property models: perfect gas, semiperfect gas, and real gas. The three gas property
models provide trade-offs between simulation speed and accuracy. They also enable the
incremental workflow: you start with a simple model, which requires minimal information
about the working gas, and then build upon the model when more detailed gas property
data becomes available. The following table lists the information that must be specified
for each of the three gas property models.

| Gas Property Model | Physical Properties | |
| --- | --- | --- |
| Perfect | *R* | Specific gas constant |
| *Z* | Compressibility factor, *Z* = *p*/(*ρ**R**T*) |
| *T*ref | Reference temperature |
| *h*ref | Specific enthalpy at reference temperature |
| *c*p | Specific heat at constant pressure, cp=(∂h∂T)p |
| *μ* | Dynamic viscosity |
| *k* | Thermal conductivity |
| Semiperfect | *R* | Specific gas constant |
| *Z* | Compressibility factor |
| *h* | Specific enthalpy vector |
| *c*p | Specific heat at constant pressure vector |
| *μ* | Dynamic viscosity vector |
| *k* | Thermal conductivity vector |
| *T* | Temperature vector |
| Real | *ρ* | Density table |
| *s* | Specific entropy table |
| *h* | Specific enthalpy table |
| *c*p | Specific heat at constant pressure table |
| *μ* | Dynamic viscosity table |
| *k* | Thermal conductivity table |
| *β* | Isothermal bulk modulus table, β=ρ(∂p∂ρ)T |
| *α* | Isobaric thermal expansion coefficient table, α=−1ρ(∂ρ∂T)p |
| *T* | Temperature vector |
| *p* | Pressure vector |

For semiperfect gas, caloric and transport properties are functions
of temperature. You specify them as one-dimensional arrays corresponding
to the **Temperature vector**. For real gas, all
properties are functions of temperature and pressure. You specify
them as two-dimensional arrays in which the rows correspond to the **Temperature
vector** and the columns correspond to the **Pressure
vector**.

Simulation issues an error when temperature or pressure is out
of range:

- For perfect gas, you specify the minimum and maximum
  permissible values for pressure and temperature in the **Parameters** section.
- For semiperfect gas, the **Valid temperature
  range parameterization** parameter gives you an option to
  define the permissible range of temperatures by using the lowest and
  highest values of the temperature vector. You have to specify the
  minimum and maximum permissible values for pressure.
- For real gas, the **Valid pressure-temperature
  region parameterization** parameter gives you an option to
  define the permissible ranges of pressure and temperature by using
  the lowest and highest values of the pressure and temperature vectors,
  respectively. You can also specify a validity matrix for the pressure-temperature
  value combinations.

### Data Visualization

The block provides the option to plot the specified gas properties as a function
of temperature and pressure. Plotting the properties lets you visualize the data
before simulating the model.

To plot the data, right-click the Gas Properties
(G) block in your model and, from the context menu, select
**Foundation Library** > **Plot Gas
Properties**. Use the drop-down list located at the top of the plot
to select the gas property to visualize. Click the **Reload**
button to regenerate a plot following a block parameter update.

**Gas Properties Plot**

**Note**

To facilitate plot readability, density data is shown in log-log scale, while
other properties are plotted in semi-log scale. That is, for a density plot as a
function of temperature and pressure, both density and pressure are in log
scales, while the temperature values are not in log scale. For other properties,
only the pressure is in log scale.
