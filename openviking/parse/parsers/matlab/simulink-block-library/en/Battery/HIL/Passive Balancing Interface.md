---
type: simulink-block
title: 'Passive Balancing Interface'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'HIL'
documentation_page: 'passivebalancinginterface'
documentation_source_path: 'ref/passivebalancinginterface.html'
language: en
---

# Passive Balancing Interface

## Ports
```yaml
ports:
- name: Ibat
  summary: Current flowing through each balancing circuit, A physical signal | scalar or vector
  direction: input
- name: Vbat
  summary: Voltage across each balancing circuit, V physical signal | scalar or vector
  direction: output
- name: +
  summary: Positive terminal electrical array of nodes
  direction: conserving
- name: '-'
  summary: Negative terminal electrical array of nodes
  direction: conserving
```

### Input

### **Ibat** — Current flowing through each balancing circuit, A physical signal | scalar or vector

Current, in amperes, flowing through the balancing circuit connected to each
parallel assembly of the battery, specified as a scalar if the **Number of
balancing circuits** is `1`, or a vector otherwise. The
size of this vector must be equal to the value of the **Number of balancing
circuits** parameter.
### Output

### **Vbat** — Voltage across each balancing circuit, V physical signal | scalar or vector

Voltage, in volts, across the balancing circuit connected to each parallel
assembly of the battery, returned as a scalar if the **Number of balancing
circuits** is `1`, or a vector otherwise. The size of this
vector is equal to the value of the **Number of balancing circuits**
parameter.
### Conserving

### **+** — Positive terminal electrical array of nodes

Electrical array-of-nodes conserving port associated with the positive terminal of
the interface. The size of this port is equal to the value of the **Number of
balancing circuits** parameter.

If you create a block using the `ParallelAssembly`, `Module`,
`ModuleAssembly`, or `Pack`
objects, set the `BalancingStrategy` property to
`"External"` and connect this port to the **+BUS**
port of the battery generated block.

### **-** — Negative terminal electrical array of nodes

Electrical array-of-nodes conserving port associated with the negative terminal of
the interface. The size of this port is equal to the value of the **Number of
balancing circuits** parameter.

If you create a block using the `ParallelAssembly`, `Module`,
`ModuleAssembly`, or `Pack`
objects, set the `BalancingStrategy` property to
`"External"` and connect this port to the **-BUS**
port of the battery generated block.
## Parameters
```yaml
parameters:
- name: Number of balancing circuits
  summary: Number of balancing circuits 1 (default) | positive scalar
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Number of balancing circuits** — Number of balancing circuits 1 (default) | positive scalar

Number of balancing circuits that the interface connects to. The value of this
parameter affects the size of all ports of this block and must be equal to the number of
parallel assemblies in the battery or to the total number of series connections.
## Libraries

Simscape / Battery / HIL

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Interface for cell balancing between battery and cell supervisory circuit

The Passive Balancing Interface block provides an
abstracted vectorized interface for cell balancing between a battery and a cell supervisory
circuit. Use this block with desktop simulations and hardware-in-the-loop battery emulation
hardware.

A cell supervisory circuit is an electronic circuit that connects to battery cells or
parallel assemblies. You can use this circuit to normalize voltages or states-of-charge (SOC)
inside a module or pack. In the real world, you implement this equipment between your battery
and the battery management system (BMS) control.

This figure represents the real-world equipment, voltages, and currents.

Figure representing the real-world equipment, voltages, and currents

To avoid damaging your battery and to test your cell balancing algorithms under standard
operational conditions and fault conditions, you can use hardware-in-the-loop battery
emulation hardware. You can use an abstracted interface to connect, set, and configure the
passive balancing BMS to your emulated battery.

In this figure:

- The blue color represents the real-world equipment, voltages, and currents.
- The green color represents the interface between the real-world and simulated
  equipment, voltages, and currents.
- The orange color represents the simulated equipment, voltages, and currents.

Figure representing the real-world and simulated equipment, voltages, and currents, as well as the interface between real world and simulation

The Passive Balancing Interface block provides the abstract
representation of power electronic equipment without the need to model it in detail. For
example, if you have a battery pack with different levels of temperature or voltage in its
constituent parts, you can use this block to check if the BMS is correctly balancing your pack
after operational scenarios.
