---
type: simulink-block
title: 'P-H Diagram (2P)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Utilities'
documentation_page: 'phdiagram2p'
documentation_source_path: 'ref/phdiagram2p.html'
language: en
---

# P-H Diagram (2P)

## Ports
```yaml
ports:
- name: p
  summary: Pressure, MPa vector
  direction: input
- name: h
  summary: Specific enthalpy, kJ/kg vector
  direction: input
```

### Input

### **p** — Pressure, MPa vector

Vector of pressures. The vector must have same number of elements as
the enthalpy signal at port **h**

### **h** — Specific enthalpy, kJ/kg vector

Vector of specific enthalpies. The vector must have same number of
elements as the pressure signal at port **p**.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Fluids / Two-Phase Fluid / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block can be used for simulation visibility in systems that generate code,
but is not included in the generated code.

## Version History

**Introduced in R2021a**

### R2025a: Change units and specify cycle point order

Click the Settings button  to specify the units and cycle point order. You
can specify the pressure, specific enthalpy, and temperature units. Clear the
**Array element order of inputs p and h with closed loop**
check box to use the **Array indices of inputs p and h** parameter
to specify the order in which the block connects the cycle points.

### R2022b: Access playback capabilities

Use the controls at the top of the figure window to control and replay the
animation from the most recent simulation.

## Description

Thermodynamic scope for two-phase fluid networks

The P-H Diagram (2P) block plots a p-h diagram of the
pressure with respect to the specific enthalpy of a thermodynamic, two-phase fluid. A
p-h diagram indicates the fluid state at key points during a thermodynamic cycle.

Each numbered point on the diagram indicates the fluid state after a dynamic process in the
refrigeration cycle:

1. Cool vapor at low pressure
2. Hot vapor at high pressure
3. Hot liquid at high pressure
4. Mixed vapor and liquid at low pressure

To use the P-H Diagram (2P) block:

1. Place a Thermodynamic Properties Sensor
   (2P) and a Pressure, Temperature & Internal
   Energy Sensor (2P) block at each location you want to
   monitor.

   **Note**

   The Pressure & Internal Energy Sensor
   (2P) block measures a differential pressure. Connect
   port **A** to the monitor point and port
   **B** to an Absolute Reference
   (2P) block.
2. Convert the Simscape physical signals to Simulink signals with a
   PS-Simulink Converter block.
3. Use a Mux block to combine the pressure signals. Connect
   the output signal to the P-H Diagram (2P)
   **p** port.
4. Use a Mux block to combine the converted specific enthalpy
   signals and connect the output signal to the **h**
   port.
5. Before running the simulation, double-click the P-H Diagram
   (2P) block, then click the Select fluid properties
   button  to set the network fluid properties.

   If you do not select the fluid properties, the block uses the default
   two-phase network fluid, which is water.

### Settings

Click the Settings button  to specify the pressure, specific enthalpy, and
temperature units and the element order. Clear the **Array element order of
inputs p and h with closed loop** check box to use the **Array
indices of inputs p and h** parameter to specify the order in which the
block connects the cycle points.

### P-H Diagram Playback

You can also replay the animation from the most recent simulation. After running the model,
double-click the block and use the buttons at the top of the window to control the
animation. Use the drop-down menu to the right of the **Time**
field to control the rate of the playback. The replay controls are disabled before
you run a simulation, when the model is loaded, and when the simulation is running.

Use the playback slider or **Time** field to control the
simulation cycle. If you enter a time that is not a model time step, the block
displays the next closest time step.

To save the current iteration of the plot, point to the plot area. From the icons in the
top-right corner of the plot, click the Export icon  and select the Save As button  to save the plot.
