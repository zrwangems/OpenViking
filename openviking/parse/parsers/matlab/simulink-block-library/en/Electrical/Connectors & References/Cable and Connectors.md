---
type: simulink-block
title: 'Cable and Connectors'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'cableandconnectors'
documentation_source_path: 'ref/cableandconnectors.html'
language: en
---

# Cable and Connectors

## Ports

### Conserving

### **In** — Input connector terminal electrical | electrical array-of-nodes

Electrical conserving port or electrical array-of-nodes conserving port associated
with the input connector terminal.

If you clear the **Model multiple conductors in cable**
parameter, this port is an electrical conserving port.

If you select the **Model multiple conductors in cable**
parameter, this port is an electrical array-of-nodes conserving port. To connect this
port to an electrical network, use an Array
Connection block. For more information, see Cable.

### **Out** — Output connector terminal electrical | electrical array-of-nodes

Electrical conserving port or electrical array-of-nodes conserving port associated
with the output connector terminal.

If you clear the **Model multiple conductors in cable**
parameter, this port is an electrical conserving port.

If you select the **Model multiple conductors in cable**
parameter, this port is an electrical array-of-nodes conserving port. To connect this
port to an electrical network, use an Array
Connection block. For more information, see Cable.

### **H** — Thermal mass thermal

Thermal conserving port associated with the thermal mass.

#### Dependencies

To enable this port, select the **Model thermal effects**
parameter.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Model multiple conductors in cable** — Option to model multiple conductors `Off` (default) | `On`

Option to model multiple conductors in the cable.

### **Number of independent conductors in cable** — Number of independent conductors in cable `3` (default) | finite positive scalar

Number of independent conductors in the cable.

#### Dependencies

To enable this parameter, select the **Model multiple conductors in
cable** parameter.

### **Model input connector** — Option to model input connector `On` (default) | `Off`

Option to model an input connector.

### **Model output connector** — Option to model output connector `On` (default) | `Off`

Option to model an output connector.

### Cable

### **Conductor material** — Conductor material `Copper` (default) | `Annealed copper` | `Aluminum` | `Silver` | `Gold` | `Custom`

Conductor material. This parameter determines the electrical
conductivity and magnetic permeability of the material. To specify
your own values for material properties, set this parameter to
`Custom`.

### **Electrical conductivity of material** — Electrical conductivity of material `5.96e7` `S/m` (default) | nonnegative scalar

Electrical conductivity of the material.

#### Dependencies

To enable this parameter, set **Conductor material** to
`Custom`.

### **Length of conductor** — Length of conductor `1` `m` (default) | positive scalar

Length of each conductor.

### **Gauge of each conductor** — Gauge of conductor in AWG system `Custom` (default) | `AWG1` | `AWG2` | ...

Gauge of each conductor, specified in the American wire gauge (AWG) system. Choose
a value from `AWG1` to
`AWG40`.

To specify the gauge in length units, set this parameter to
`Custom` and specify the value for the **Conductor
diameter** parameter.

### **Conductor diameter** — Gauge of each conductor in length units `0.5` `mm` (default) | positive scalar

Gauge of each conductor, specified in length units.

#### Dependencies

To enable this parameter, set **Gauge of each conductor**
to `Custom`.

### **Model cable inductance** — Option to model cable inductance `Off` (default) | `On`

Option to model the inductance of the cable.

Clear this parameter to prioritize high simulation speeds. Select this parameter
to prioritize accurate results.

### **Model skin effect** — Option to model skin effect `Off` (default) | `On`

Option to model the skin effect.

### **Rated frequency** — Rated frequency `50` `Hz` (default) | nonnegative scalar

Rated frequency of the cable.

#### Dependencies

To enable this parameter, select the **Model skin
effect** parameter.

### **Relative magnetic permeability of material** — Relative magnetic permeability of material `1` (default) | positive scalar

Relative magnetic permeability of the material.

#### Dependencies

To enable this parameter, set **Conductor material** to
`Custom`.

### Connectors

### **Contact resistance between pins and sockets** — Contact resistance between pins and sockets `1` `Ohm` (default) | positive scalar

Contact resistance between the pins and sockets.

#### Dependencies

To enable this parameter, select the **Model input
connector** or **Model output connector**
parameter.

### **Conductance between pins** — Conductance between pins `1e-12` `S` (default) | positive scalar

Conductance between the pins.

#### Dependencies

To enable this parameter:

- Select the **Model input connector** or
  **Model output connector** parameter.
- Select the **Model multiple conductors in cable**
  parameter.

### Thermal

### **Model thermal effects** — Option to model thermal effects `Off` (default) | `On`

Option to model thermal effects. Select this parameter to enable the **H** port.

### **Resistance temperature coefficient** — Resistance temperature coefficient `1e-6` `1/K` (default) | nonnegative scalar

Resistance temperature coefficient.

#### Dependencies

To enable this parameter, select the **Model thermal
effects** parameter.

### **Measurement temperature** — Measurement temperature `298.15` `K` (default) | scalar

Measurement temperature. This value is the temperature at which you quote the
value for the **Resistance temperature coefficient**
parameter.

#### Dependencies

To enable this parameter, select the **Model thermal
effects** parameter.

### **Thermal mass of each conductor** — Thermal mass of each conductor `0.1` `J/K` (default) | positive scalar

Thermal mass of each conductor.

#### Dependencies

To enable this parameter, select the **Model thermal
effects** parameter.

### **Thermal mass of each connector pin** — Thermal mass of each connector pin `0.1` `J/K` (default) | positive scalar

Thermal mass of each connector pin.

#### Dependencies

To enable this parameter, select the **Model thermal
effects** parameter.

### Faults

### **Inter-pin short circuit in input connector fault** — Option to add inter-pin short circuit in input connector fault `Add fault`

Option to add an inter-pin short-circuit fault to the input connector.

To add a fault, click the **Add fault**
hyperlink.

#### Dependencies

To enable this parameter, select the **Model multiple conductors in
cable** and **Model input connector**
parameters.

### **Short-circuit conductance of faulted input connector** — Short-circuit conductance of faulted input connector `1e9` `S` (default) | nonnegative scalar

Short-circuit conductance of the faulted input connector.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in input connector fault**
  parameter.

### **Faultable pin pairs** — Faultable pin pairs `Make all pin pairs faultable` (default) | `Specify faultable pin pairs`

Option to make all pin pairs faultable or to specify the faultable pin
pairs.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in input connector fault**
  parameter.

### **Matrix of faultable pin pairs** — Faultable pin pairs `[1,2;1,3]` (default) | matrix

Faultable pin pairs, specified as an `N`-by-`2`
matrix where `N` is the number of faultable pin pairs and each row
defines a pair of pins by their indices. For example, to enable a short-circuit fault
between pin 1 and pin 2, add the row `1,2;` to the matrix. When a
short-circuit fault triggers, the inter-pin conductance changes for only the pin pairs
you specify.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in input connector fault**
  parameter.
- Set **Faultable pin pairs** to `Specify
  faultable pin pairs`.

### **Trigger type** — Trigger type `Always on` (default) | `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

Trigger type, specified as one of these options:

- `Always On` — The fault injects at the start of the
  simulation.
- `Timed` — The fault injects when the simulation time
  reaches the value you specify for the **Trigger fault at time**
  parameter.
- `Behavioral` — The fault injects as a result of fault
  parameter values during simulation. Setting **Trigger type** to
  `Behavioral` enables block parameters that define
  the failure conditions.
- `Additional triggers` — The fault injects as a result
  of additional triggers not available in the block dialog box. Select this option
  and click the **Open fault properties** hyperlink to set the
  **Trigger type** to one of these values in the Property
  Inspector:

  - `Conditional` — The fault injects as a result
    of a condition that reflects a behavior associated with a signal.
    Conditionals evaluate the Boolean expression in the
    **Condition** parameter at each time step. To model
    irreversible faults, select the **Trigger stays on once
    activated** parameter in the Property Inspector. The block
    enters the faulted state when the trigger condition becomes true for the
    first time and remains in the faulted state for the rest of the
    simulation. To model reversible faults, clear the **Trigger
    stays on once activated** parameter. The block enters the
    faulted state when the trigger condition is true and enters the
    unfaulted state when the trigger condition is false. To learn more, see
    Create and Manage Conditionals.
  - `Manual` — The fault injects or clears when
    you toggle the status in the **Fault Dashboard** pane.
    To learn more, see Manually Trigger Faults in Models.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in input connector fault**
  parameter.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in input connector fault**
  parameter.
- Set **Trigger type** to
  `Timed`.

### **Maximum permissible temperature** — Upper temperature threshold for fault transition `inf` `degC` (default) | scalar

Upper temperature threshold for a behavioral fault transition. The block enters the faulted state if the temperature continuously exceeds this value for a period longer than the value of the **Time to fail when exceeding temperature** parameter.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Select the **Model thermal effects** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in input connector fault**
  parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Time to fail when exceeding temperature** — Time to fail when exceeding temperature `1` `s` (default) | positive scalar

Amount of time that the temperature must continuously exceed the maximum permissible temperature before a behavioral fault triggers.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Select the **Model thermal effects** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in input connector fault**
  parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Maximum permissible voltage** — Voltage threshold for fault transition `inf` `V` (default) | positive scalar

Voltage threshold for a fault transition. The block enters the
faulted state if the voltage continuously exceeds this value for a period longer than the value
of the **Time to fail when exceeding voltage** parameter.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in input connector fault**
  parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Time to fail when exceeding voltage** — Time to fail when exceeding voltage `1` `s` (default) | positive scalar

Amount of time that the voltage must continuously exceed the maximum permissible voltage before a short-circuit fault triggers.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in input connector
  fault**.
- Set **Trigger type** to
  `Behavioral`.

### **Trigger configuration** — Option to enable additional trigger types `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in input connector fault**
  parameter.
- Set **Trigger type** to `Additional
  triggers`.

### **Inter-pin short circuit in output connector fault** — Option to add inter-pin short circuit in output connector fault `Add fault`

Option to add an inter-pin short-circuit fault to the output connector.

To add a fault, click the **Add fault**
hyperlink.

#### Dependencies

To enable this parameter, select the **Model multiple conductors in
cable** and **Model output connector**
parameters.

### **Short-circuit conductance of faulted output connector** — Short-circuit conductance of faulted output connector `1e9` `S` (default) | nonnegative scalar

Short-circuit conductance of the faulted output connector.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model output connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in output connector fault**
  parameter.

### **Faultable pin pairs** — Faultable pin pairs `Make all pin pairs faultable` (default) | `Specify faultable pin pairs`

Option to make all pin pairs faultable or to specify the faultable pin
pairs.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model output connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in output connector fault**
  parameter.

### **Matrix of faultable pin pairs** — Faultable pin pairs `[1,2;1,3]` (default) | matrix

Faultable pin pairs, specified as an `N`-by-`2`
matrix where `N` is the number of faultable pin pairs and each row
defines a pair of pins by their indices. For example, to enable a short-circuit fault
between pin 1 and pin 2, add the row `1,2;` to the matrix. When a
short-circuit fault triggers, the inter-pin conductance changes for only the pin pairs
you specify.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model output connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in output connector fault**
  parameter.
- Set **Faultable pin pairs** to `Specify
  faultable pin pairs`

### **Trigger type** — Trigger type `Always on` (default) | `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

Trigger type, specified as one of these options:

- `Always On` — The fault injects at the start of the
  simulation.
- `Timed` — The fault injects when the simulation time
  reaches the value you specify for the **Trigger fault at time**
  parameter.
- `Behavioral` — The fault injects as a result of fault
  parameter values during simulation. Setting **Trigger type** to
  `Behavioral` enables block parameters that define
  the failure conditions.
- `Additional triggers` — The fault injects as a result
  of additional triggers not available in the block dialog box. Select this option
  and click the **Open fault properties** hyperlink to set the
  **Trigger type** to one of these values in the Property
  Inspector:

  - `Conditional` — The fault injects as a result
    of a condition that reflects a behavior associated with a signal.
    Conditionals evaluate the Boolean expression in the
    **Condition** parameter at each time step. To model
    irreversible faults, select the **Trigger stays on once
    activated** parameter in the Property Inspector. The block
    enters the faulted state when the trigger condition becomes true for the
    first time and remains in the faulted state for the rest of the
    simulation. To model reversible faults, clear the **Trigger
    stays on once activated** parameter. The block enters the
    faulted state when the trigger condition is true and enters the
    unfaulted state when the trigger condition is false. To learn more, see
    Create and Manage Conditionals.
  - `Manual` — The fault injects or clears when
    you toggle the status in the **Fault Dashboard** pane.
    To learn more, see Manually Trigger Faults in Models.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in output connector fault**
  parameter.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in output connector fault**
  parameter.
- Set **Trigger type** to
  `Timed`.

### **Maximum permissible temperature** — Upper temperature threshold for fault transition `inf` `degC` (default) | scalar

Upper temperature threshold for a behavioral fault transition. The block enters the faulted state if the temperature continuously exceeds this value for a period longer than the value of the **Time to fail when exceeding temperature** parameter.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Select the **Model thermal effects** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in output connector fault**
  parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Time to fail when exceeding temperature** — Time to fail when exceeding temperature `1` `s` (default) | positive scalar

Amount of time that the temperature must continuously exceed the maximum permissible temperature before a behavioral fault triggers.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Select the **Model thermal effects** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in output connector fault**
  parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Maximum permissible voltage** — Voltage threshold for fault transition `inf` `V` (default) | positive scalar

Voltage threshold for a fault transition. The block enters the
faulted state if the voltage continuously exceeds this value for a period longer than the value
of the **Time to fail when exceeding voltage** parameter.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in output connector fault**
  parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Time to fail when exceeding voltage** — Time to fail when exceeding voltage `1` `s` (default) | positive scalar

Amount of time that the voltage must continuously exceed the maximum permissible voltage before a short-circuit fault triggers.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model input connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in output connector fault**
  parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Trigger configuration** — Option to enable additional trigger types `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Select the **Model output connector** parameter.
- Click the **Add fault** hyperlink for the
  **Inter-pin short circuit in output connector fault**
  parameter.
- Set **Trigger type** to `Additional
  triggers`.

### **Open-circuit fault** — Option to add open-circuit fault `Add fault`

Option to add an open-circuit fault to the conductors in the cable.

To add a fault, click the **Add fault**
hyperlink.

### **Open-circuit conductance** — Open circuit conductance `1e-5` `S` (default) | positive scalar

Open-circuit conductance of a faulted conductor in the cable.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for
the **Open-circuit fault** parameter.

### **Faultable conductors** — Faultable conductors `Make all conductors faultable` (default) | `Specify faultable conductors`

Option to make all conductors faultable or to specify the faultable
conductors.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Click the **Add fault** hyperlink for the
  **Open-circuit fault** parameter.

### **Indices of faultable conductors** — Indices of faultable conductors `[1,2]` (default) | vector

Indices of faultable conductors. When an open-circuit fault triggers, the
conductance changes for only the conductors with the indices that you specify.

#### Dependencies

To enable this parameter:

- Select the **Model multiple conductors in cable**
  parameter.
- Click the **Add fault** hyperlink for the
  **Open-circuit fault** parameter.
- Set **Faultable conductors** to `Specify
  faultable conductors`.

### **Trigger type** — Trigger type `Always on` (default) | `Timed` | `Behavioral` | `Additional triggers` | `Conditional` | `Manual`

Trigger type, specified as one of these options:

- `Always On` — The fault injects at the start of the
  simulation.
- `Timed` — The fault injects when the simulation time
  reaches the value you specify for the **Trigger fault at time**
  parameter.
- `Behavioral` — The fault injects as a result of fault
  parameter values during simulation. Setting **Trigger type** to
  `Behavioral` enables block parameters that define
  the failure conditions.
- `Additional triggers` — The fault injects as a result
  of additional triggers not available in the block dialog box. Select this option
  and click the **Open fault properties** hyperlink to set the
  **Trigger type** to one of these values in the Property
  Inspector:

  - `Conditional` — The fault injects as a result
    of a condition that reflects a behavior associated with a signal.
    Conditionals evaluate the Boolean expression in the
    **Condition** parameter at each time step. To model
    irreversible faults, select the **Trigger stays on once
    activated** parameter in the Property Inspector. The block
    enters the faulted state when the trigger condition becomes true for the
    first time and remains in the faulted state for the rest of the
    simulation. To model reversible faults, clear the **Trigger
    stays on once activated** parameter. The block enters the
    faulted state when the trigger condition is true and enters the
    unfaulted state when the trigger condition is false. To learn more, see
    Create and Manage Conditionals.
  - `Manual` — The fault injects or clears when
    you toggle the status in the **Fault Dashboard** pane.
    To learn more, see Manually Trigger Faults in Models.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for
the **Open-circuit fault** parameter.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for
the **Open-circuit fault** parameter and set **Trigger type** to `Timed`.

### **Maximum permissible current** — Current threshold for fault transition `inf` `A` (default) | positive scalar

Current threshold for a fault transition. The block enters the faulted state if the current
continuously exceeds this value for a period longer than the value of the **Time to
fail when exceeding current** parameter.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for
the **Open-circuit fault** parameter and set **Trigger type** to `Behavioral`.

### **Maximum permissible temperature** — Upper temperature threshold for fault transition `inf` `degC` (default) | scalar

Upper temperature threshold for a behavioral fault transition. The block enters the faulted state if the temperature continuously exceeds this value for a period longer than the value of the **Time to fail when exceeding temperature** parameter.

#### Dependencies

To enable this parameter:

- Select the **Model thermal effects** parameter.
- Click the **Add fault** hyperlink for the
  **Open-circuit fault** parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Time to fail when exceeding current** — Time to fail when exceeding current `1` `s` (default) | positive scalar

Amount of time that the current must continuously exceed the maximum permissible current
before a fault triggers.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for
the **Open-circuit fault** parameter and set **Trigger type** to `Behavioral`.

### **Time to fail when exceeding temperature** — Time to fail when exceeding temperature `1` `s` (default) | positive scalar

Amount of time that the temperature must continuously exceed the maximum permissible temperature before a behavioral fault triggers.

#### Dependencies

To enable this parameter:

- Select the **Model thermal effects** parameter.
- Click the **Add fault** hyperlink for the
  **Open-circuit fault** parameter.
- Set **Trigger type** to
  `Behavioral`.

### **Trigger configuration** — Option to enable additional trigger types `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for
the **Open-circuit fault** parameter and set **Trigger type** to `Additional triggers`.

## Libraries

Simscape / Electrical / Connectors & References

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

### R2025a: Model Reversible Conditional Faults

You can now model reversible conditional faults in the Cable and Connectors block by clearing the
**Trigger stays on once activated** parameter. The block enters the
faulted state when the trigger condition is true and enters the unfaulted state when the
trigger condition is false.

Before R2025a, the block enters the faulted state when the trigger condition becomes true
for the first time and remains in the faulted state for the rest of the simulation.

If you create a model before R2025a and enable a conditional fault in the Cable and Connectors
block, the block now selects the **Trigger stays on once activated**
parameter by default for backward compatibility.

## Description

Cable and connectors with optional fault modeling

The Cable and Connectors block models a cable and
connectors using resistors and inductors.

For most applications, you can directly connect two or more blocks with physical
connection lines. These connection lines are idealized and have no resistance or inductance.
If you need a simple physics-based model for an electrical cable or connectors, you can use a
combination of Resistor blocks and Inductor blocks. Use the Cable and
Connectors block instead if you want to:

- Model multiple conductors in a single cable.
- Analyze cables with open-circuit faults.
- Analyze input or output connectors with short-circuit faults.
- Parameterize the conductors by defining the material and geometry instead of the
  resistance and inductance.
- Specify the gauge of the conductors using the American wire gauge (AWG) system.

### Cable

The Cable and Connectors block models each conductor in
the cable as a resistor. You can also choose to include an inductor in series with the
resistor by selecting the **Model cable inductance** parameter. Clear this
parameter to prioritize high simulation speeds. Select this parameter to prioritize accurate
results.

To model a single conductor, clear the **Model multiple conductors in
cable** parameter. To model multiple conductors, select the **Model
multiple conductors in cable** parameter and specify the number of conductors
using the **Number of independent conductors in cable** parameter.

The Cable and Connectors block has two ports that
represent the input and output ends of the cable. If you model a single conductor, these
**In** and **Out** ports are electrical conserving ports. If you model
multiple conductors, the **In** and **Out** ports are electrical
array-of-nodes conserving ports. To connect the electrical array-of-nodes ports to the rest
of your network, use an Array
Connection block to act as a multiplexor for the Simscape™ electrical domain by concatenating all input array of nodes into a single 1-D
array. First, connect the **In** and **Out** ports to the
**RConn** ports of separate Array Connection
blocks. The **RConn** port name is not visible in the block icon, but you can see
this name if you pause your pointer over the port. Then, set the **Domain**
parameter of the Array Connection block to
`Electrical Domain`. Finally, set the **Number of scalar
elements** parameter of the Array Connection
blocks to the same value as the **Number of independent conductors in
cable** parameter of the Cable and Connectors
block. This figure shows how to connect a Cable and
Connectors block with three independent conductors in the cable to an
electrical network.

Cable and Connectors block connected in series with two Array Connection blocks

**Equations**

The block assumes that the conductors in the cable are round wires and calculates the
resistance of each conductor, *R*, using these equations [1],

R=ρLπ(r2−(r−δ)2)

δ={1πμσf       if r≥1πμσfr                  if r≤1πμσf

where:

- *ρ* is the electrical resistivity of each conductor.
- *L* is the value of the **Length of conductor**
  parameter.
- *r* is the radius of the conductor.
- *δ* is the skin depth.
- *μ* is the magnetic permeability of the conductor.
- *σ* is the specific conductivity of the conductor.
- *f* is the rated frequency.

For DC current, there is no skin effect. The current spreads evenly over the
cross-section of the conductor, so *δ* = *r*. For
high-frequency AC current, at full skin effect, current flows only on the surface of the
conductor, so *δ* = 0.

If you clear the **Model skin effect** parameter,
*f* = 0. If you select the **Model skin effect**
parameter, *f* is equal to the value of the **Rated
frequency** parameter.

If you select the **Model cable inductance** parameter, the block
calculates the inductance of each conductor *LDC*
using these equations [2],

LDC=μ02πL(ln(2Lr)−Y)

Y=11+rπ4μσf

where:

- *μ*0 is the permeability of free
  space.
- *Y* is the current distribution constant.

The current distribution constant has a value between 0 and 1. For DC,
*Y* = 1. For high-frequency AC, *Y* approaches
0.

### Connectors

The block models the connectors with resistors. The number of pins in the conductor is
equal to the number of independent conductors in the cable. This figure shows the equivalent
circuit for a three-pin input connector. The resistors labeled `Ri` model
the contact resistance between each pin and the corresponding socket. The resistors labeled
`Gij` model the inter-pin conductance for each pin pair
`(i,j)`.

Connector represented by resistors between each pin and socket and between each pair of pins

Specify the resistance of resistors `Ri` using the **Contact
resistance between pin and sockets** parameter. Specify the conductance of
resistors `Gij` using the **Conductance between pins**
parameter.

You do not always need to model connectors at both ends of the cable. For example:

- If you model a cable soldered directly to a printed circuit board (PCB), then do
  not model the connector at that end of the cable, for greater accuracy.
- If you model a cable with almost ideal connectors, or if you model an open-circuit
  fault in the cable, the inter-pin conductance and the contact resistance between the
  pins and sockets in the connectors have a negligible impact on the simulation
  results.

You can choose whether to model each connector by using the **Model input
connector** and **Model output connector** parameters. To
increase the simulation speed, do not model the connectors if you do not need to.

### Faults

To model a fault in the Cable and Connectors block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Cable and Connectors block models electrical faults
as an instantaneous change in the conductance of the cable or connectors. You can model an
open-circuit fault in the cable or a short-circuit fault in the connectors.

When the cable fails in open circuit, the conductance of the conductors changes to the
value of the **Open-circuit conductance** parameter. If you model multiple
conductors in the same cable, you can choose to trigger faults for all conductors or specify
which conductors you want to fail.

- To trigger an open-circuit fault for all conductors, set **Faultable
  conductors** to `Make all conductors faultable`.
- To trigger an open-circuit fault for specific conductors, set **Faultable
  conductors** to `Specify faultable conductors` and
  specify which conductors you want to fail using the **Indices of faultable
  conductors** parameter.

When an input or output connector short circuits, the inter-pin conductance of pin pairs
changes to the value of the **Short-circuit conductance of faulted input
connector** or **Short-circuit conductance of faulted output
connector** parameter, respectively.

- To trigger a short-circuit fault for all pin pairs, set **Faultable pin
  pairs** to `Make all pin pairs faultable`.
- To trigger a short-circuit fault for specific pin pairs, set **Faultable
  conductors** to `Specify faultable conductors` and
  specify which conductors you want to fail using the **Matrix of faultable pin
  pairs** parameter. Each row of this matrix defines a pair of pins by their
  indices. For example, to enable a short-circuit fault between pin 1 and pin 2, add the
  row `1,2;` to the matrix.

**Fault Triggers**

You can specify how and when faults occur by using the **Trigger
type** parameter.

If you set the **Trigger type** to
`Behavioral`, the Cable and Connectors block triggers fault events when
the temperature continuously exceeds the value of the **Maximum permissible
temperature** for a duration longer than the value of the **Time to
fail when exceeding temperature** parameter. The block also triggers:

- Open-circuit faults in the cable when the current continuously exceeds the value
  of the **Maximum permissible current** parameter for a duration
  longer than the value of the **Time to fail when exceeding
  current** parameter.
- Short-circuit faults in the connectors when the voltage continuously exceeds the
  value of the **Maximum permissible voltage** parameter for a
  duration longer than the value of the **Time to fail when exceeding
  voltage** parameter.

If you set the **Trigger
type** to `Conditional`, you can choose whether faults
in the Cable and Connectors block are reversible *(since R2025a)*. To model irreversible faults, click
**Open fault properties** to open the Property Inspector and select the
**Trigger stays on once activated** parameter. The block enters the faulted
state when the trigger condition becomes true for the first time and remains in the faulted
state for the rest of the simulation. To model reversible faults, clear the **Trigger
stays on once activated** parameter. The block enters the faulted state when the
trigger condition is true and enters the unfaulted state when the trigger condition is
false.

For more information about adding faults to blocks and
specifying fault triggers, see Introduction to Simscape Faults.
