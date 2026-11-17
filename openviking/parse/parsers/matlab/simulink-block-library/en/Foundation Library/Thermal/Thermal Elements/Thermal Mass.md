---
type: simulink-block
title: 'Thermal Mass'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Elements'
documentation_page: 'thermalmass'
documentation_source_path: 'ref/thermalmass.html'
language: en
---

# Thermal Mass

## Ports
```yaml
ports:
- name: Mdot
  summary: Mass control signal, kg/s physical signal
  direction: input
- name: Tin
  summary: Temperature of incoming mass, K physical signal
  direction: input
- name: M
  summary: Port that connects mass to circuit thermal
  direction: conserving
- name: N
  summary: Second graphical port thermal
  direction: conserving
```

### Input

### **Mdot** — Mass control signal, kg/s physical signal

Input physical signal that specifies the change in thermal mass. Use the
high-priority **Mass** variable to specify the initial thermal mass
value.

#### Dependencies

To enable this port, set the **Mass type** parameter to
`Variable`.

### **Tin** — Temperature of incoming mass, K physical signal

Input physical signal that specifies the temperature of incoming mass. The signal
value at port **Tin** has no effect when the signal at port
**Mdot** is less than or equal to 0.

#### Dependencies

To enable this port, set the **Mass type** parameter to
`Variable`.
### Conserving

### **M** — Port that connects mass to circuit thermal

Thermal conserving port that connects the mass to the physical network.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

### **N** — Second graphical port thermal

Second thermal conserving port that lets you connect the mass in series with other
elements in the block diagram. This port has the same temperature as port
**M**, therefore the difference between the one-port and two-port
block representations is purely graphical.

The port name is not visible in the block icon, but you can see this name in the
underlying source file by clicking the **Source code** link in the
**Description** tab of the block dialog box.

#### Dependencies

To enable this port, set the **Number of graphical ports**
parameter to `2`.
## Parameters
```yaml
parameters:
- name: Mass type
  summary: Specify whether thermal mass can change during simulation Constant (default) | Variable
  group: ''
- name: Mass
  summary: Constant mass 1 kg (default) | positive scalar
  group: ''
- name: Specific heat
  summary: Specific heat of the material 447 J/(K*kg) (default) | positive scalar
  group: ''
- name: Minimum mass
  summary: Minimum acceptable mass 1e-6 kg (default) | positive scalar
  group: ''
- name: Number of graphical ports
  summary: Number of visible ports 1 (default) | 2
  group: ''
```

### **Mass type** — Specify whether thermal mass can change during simulation `Constant` (default) | `Variable`

Select whether the thermal mass can change during simulation:

- `Constant` — The thermal mass is constant during
  simulation.
- `Variable` — The thermal mass can vary during
  simulation. Use this option to model systems where the mass changes but the
  geometric effects remain negligible, such as a washing machine being filled, heated,
  and then emptied with a varying amount of liquid per cycle.

### **Mass** — Constant mass `1 kg` (default) | positive scalar

Mass value. The mass is constant during simulation.

#### Dependencies

To enable this parameter, set the **Mass type** parameter to
`Constant`.

### **Specific heat** — Specific heat of the material `447 J/(K*kg)` (default) | positive scalar

Specific heat of the material.

### **Minimum mass** — Minimum acceptable mass `1e-6 kg` (default) | positive scalar

The minimum thermal mass value. The block issues an error if the thermal mass falls
below this value during simulation.

#### Dependencies

To enable this parameter, set the **Mass type** parameter to
`Variable`.

### **Number of graphical ports** — Number of visible ports `1` (default) | `2`

How to connect the block to the rest of the circuit:

- `1` — The block has one conserving port that
  connects it to the thermal circuit. When the block has one port, attach it to a
  connection line between two other blocks.
- `2` — Selecting this option exposes the second
  port, which lets you connect the block in series with other blocks in the circuit.
  Because the two ports have the same temperature, the block functions the same as if
  it had one port.
## Libraries

Simscape / Foundation Library / Thermal / Thermal Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007b**

### R2023a: Use variable thermal mass

The block includes the **Mass type** parameter, which lets you specify
whether the thermal mass stay constant or varies during simulation. In previous releases,
the thermal mass could only be constant.

## Description

Mass in thermal systems

The Thermal Mass block represents a thermal mass that reflects the ability
of a material, or a combination of materials, to store internal energy. The mass of the
material and its specific heat characterize this property. The thermal mass is described
by

Q=c⋅mdTdt,

where:

- *Q* is the heat flow.
- *c* is the specific heat of the mass material.
- *m* is the mass.
- *T* is the temperature.
- *t* is time.

The **Mass type** parameter lets you specify whether the thermal mass
stays constant or varies during simulation:

- `Constant` — The thermal mass is constant during simulation.
- `Variable` — The thermal mass can vary during simulation. If
  you select this option, the **Mass** parameter in the block dialog is
  replaced by the **Minimum mass** parameter and a high-priority
  **Mass** variable, and the block has two physical signal input ports:
  **Mdot**, which specifies the change in the thermal mass, and
  **Tin**, which specifies the temperature of incoming mass. The signal
  value at port **Tin** has no effect when the thermal mass is constant or
  decreasing.

Use the `Variable` option to model systems where the mass changes
but the geometric effects remain negligible, such as a washing machine being filled, heated,
and then emptied with a varying amount of liquid per cycle.

By default, the block has one thermal conserving port. Because the block positive
direction is from the port towards the block, the heat flow is positive if it flows into the
block.

In some applications, it is customary to display mass in series with other elements in the
block diagram layout. To support this use case, the **Number of graphical
ports** parameter lets you display a second port on the opposite side of the block
icon. The two-port variant is purely graphical: the two ports have the same temperature, so
the block functions the same whether it has one or two ports. The block icon changes depending
on the value of the **Mass type** and **Number of graphical
ports** parameters.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.

If you set the **Mass type** parameter to
`Variable`, use the high-priority **Mass**
variable to specify the initial thermal mass value.
