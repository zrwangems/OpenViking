---
type: simulink-block
title: 'Semiconductor Switch Selector'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'semiconductorswitchselector'
documentation_source_path: 'ref/semiconductorswitchselector.html'
language: en
---

# Semiconductor Switch Selector

## Ports
```yaml
ports:
- name: Control
  summary: Gate terminal physical signal
  direction: input
- name: Control
  summary: Gate terminal electrical
  direction: conserving
- name: A
  summary: Anode terminal electrical
  direction: conserving
- name: K
  summary: Cathode terminal electrical
  direction: conserving
- name: B
  summary: Body terminal electrical
  direction: conserving
- name: H
  summary: Thermal mass thermal
  direction: conserving
```

### Input

### **Control** — Gate terminal physical signal

Physical signal port associated with the gate terminal.

The port name is not visible in the block icon, but you can see this name by
pausing you pointer on the port.

#### Dependencies

To enable this port, set **Gate-control port** to
`PS` and set **Library block** to
one of these options:

- `Ideal Semiconductor Switch`
- `MOSFET (Ideal, Switching)`
- `IGBT (Ideal, Switching)`
- `Thyristor (Piecewise, Linear)`
- `GTO`
### Conserving

### **Control** — Gate terminal electrical

Electrical conserving port associated with the gate terminal.

The port name is not visible in the block icon, but you can see this name by
pausing your pointer on the port.

#### Dependencies

To enable this port, choose one of these options:

- Set **Gate-control port** to
  `Electrical` and set **Library
  block** to one of these options:

  - `Ideal Semiconductor Switch`
  - `MOSFET (Ideal, Switching)`
  - `IGBT (Ideal, Switching)`
  - `Thyristor (Piecewise, Linear)`
  - `GTO`
- Set **Library block** to one of these
  options:

  - `N-Channel MOSFET`
  - `P-Channel MOSFET`
  - `N-Channel IGBT`
  - `Thyristor`

### **A** — Anode terminal electrical

Electrical conserving port associated with the anode terminal of a GTO or
thyristor, the drain terminal of a MOSFET, or the collector terminal of an
IGBT.

The port name is not visible in the block icon, but you can see this name by
pausing your pointer on the port.

### **K** — Cathode terminal electrical

Electrical conserving port associated with the cathode terminal of a GTO or
thyristor, the source terminal of a MOSFET, or the emitter terminal of an IGBT.

The port name is not visible in the block icon, but you can see this name by
pausing your pointer on the port.

### **B** — Body terminal electrical

Electrical conserving port associated with the body terminal of a four-terminal
MOSFET.

The port name is not visible in the block icon, but you can see this name by
pausing your pointer on the port.

#### Dependencies

To enable this port, set **Number of terminals** to
`Four` and **Library block** to
one of these options:

- `N-Channel MOSFET`
- `P-Channel MOSFET`
- `N-Channel IGBT`

### **H** — Thermal mass thermal

Thermal conserving port associated with the thermal mass.

The port name is not visible in the block icon, but you can see this name by
pausing your pointer on the port.

#### Dependencies

To enable this port, choose one of these options:

- Set **Modeling option** to `Show
  thermal port` and **Library block** to
  one of these options:

  - `MOSFET (Ideal, Switching)`
  - `IGBT (Ideal, Switching)`
  - `Thyristor (piecewise, Linear)`
  - `Thyristor`
  - `GTO`
- Set **Library block** to `N-Channel
  MOSFET` or `P-Channel MOSFET` and set
  **Modeling option** to `threshold-based
  with thermal` or `surface-potential-based with
  thermal`.
- Set **Library block** to `N-Channel
  IGBT` and set **Modeling option** to
  `Full I-V and capacitance characteristics | Show thermal
  port` or `Simplified I-V characteristics and
  event-based timing | Show thermal port`.
## Parameters
```yaml
parameters:
- name: Switching device
  summary: Type of semiconductor switching device MOSFET (default) | IGBT | Thyristor | GTO
  group: ''
- name: Library block
  summary: Underlying library block Ideal Semiconductor Switch (default) | MOSFET (Ideal, Switching) | N-Channel MOSFET |
    P-Channel MOSFET | ...
  group: ''
- name: Gate-control port
  summary: Option to specify physical or electrical control port PS (default) | Electrical
  group: ''
- name: Modeling option
  summary: Modeling option No thermal port (default) | Show thermal port | Threshold-based | Surface-potential based | ...
  group: ''
- name: Number of terminals
  summary: Number of terminals Three (default) | Four
  group: ''
- name: Edit parameters
  summary: Option to edit library block parameters button
  group: ''
- name: Remove Semiconductor Switch Selector block mask
  summary: Option to remove Semiconductor Switch Selector block mask button
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Switching device** — Type of semiconductor switching device `MOSFET` (default) | `IGBT` | `Thyristor` | `GTO`

Type of semiconductor switching device.

### **Library block** — Underlying library block `Ideal Semiconductor Switch` (default) | `MOSFET (Ideal, Switching)` | `N-Channel MOSFET` | `P-Channel MOSFET` | ...

Underlying block from the **Simscape** > **Electrical** > **Semiconductors & Converters** > **Semiconductors** library. The available options depend on the value of the
**Switching Device** parameter.

### **Gate-control port** — Option to specify physical or electrical control port `PS` (default) | `Electrical`

Option to specify a physical signal or electrical conserving port for the switch
gate. For a simpler control method, set this parameter to `PS`.
For a more versatile and high-fidelity control method, set this parameter to
`Electrical`. All semiconductor blocks support electrical
gates but only some support physical signals. If you use an electrical port and connect
the Semiconductor Switch Selector block to a Gate
Driver block, you can easily change the fidelity level by changing the
**Library block** parameter without changing the gate driver.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **Switching device** to
  `MOSFET` and set **Library
  block** to `Ideal Semiconductor Switch`
  or `MOSFET (Ideal, Switching)`.
- Set **Switching device** to
  `IGBT` and set **Library
  block** to `Ideal Semiconductor Switch`
  or `IGBT (Ideal, Switching)`.
- Set **Switching device** to
  `Thyristor` and set **Library
  block** to `Thyristor (Piecewise,
  Linear)`.
- Set **Switching device** to
  `GTO`.

### **Modeling option** — Modeling option `No thermal port` (default) | `Show thermal port` | `Threshold-based` | `Surface-potential based` | ...

Modeling option that determines whether you expose the thermal port,
**H**, and defines the mathematical model that the underlying library
block uses. The available options depend on the value of the **Library
block** parameter. For more information about **Modeling
option** parameter values, see the reference page for the underlying library
block.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **Switching device** to
  `MOSFET` and set **Library
  block** to `MOSFET (Ideal, Switching)`,
  `N-Channel MOSFET`, or `P-Channel
  MOSFET`.
- Set **Switching device** to
  `IGBT` and set **Library
  block** to `IGBT (Ideal, Switching)` or
  `N-Channel IGBT`.
- Set **Switching device** to
  `Thyristor` or `GTO`.

### **Number of terminals** — Number of terminals `Three` (default) | `Four`

Number of terminals of an N-Channel MOSFET,
P-Channel MOSFET, or N-Channel
IGBT block.

#### Dependencies

To enable this parameter, choose one of these options:

- Set **Switching device** to
  `MOSFET` and set **Library
  block** to `N-Channel MOSFET` or
  `P-Channel MOSFET`.
- Set **Switching device** to
  `IGBT` and set **Library
  block** to `N-Channel IGBT`.

### **Edit parameters** — Option to edit library block parameters button

Option to edit the library block parameters. Click this button to open the dialog
box of the underlying library block.

### **Remove Semiconductor Switch Selector block mask** — Option to remove Semiconductor Switch Selector block mask button

Option to remove the Semiconductor Switch Selector block mask. Click this button to keep only the
underlying library block. If you double-click the block mask, the dialog box for the
underlying library block now opens and the port names on the block icon match the
underling library block. This action also enables parameters in the underlying block
that were only enabled in the Semiconductor Switch Selector block dialog box. This action is
irreversible.
## Libraries

Simscape / Electrical / Semiconductors & Converters

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Controlled semiconductor switch at multiple fidelity levels

The Semiconductor Switch Selector block models a controlled switch that represents a
metal-oxide-semiconductor field-effect transistor (MOSFET), insulated-gate bipolar transistor
(IGBT), thyristor, or gate turn-off thyristor (GTO).

Simscape™
Electrical™ includes blocks that can model the same type of semiconductor device but at
different levels of fidelity. For example, the MOSFET
(Ideal, Switching) and N-Channel
MOSFET blocks both model a MOSFET. To develop your model with the right
level of complexity, you need a different fidelity level depending on the stage you are at in
the design process. The Semiconductor Switch Selector block combines these different library blocks under a
single top-level block mask. Use the Semiconductor Switch Selector block to change the fidelity level without
replacing a block or reentering parameter values that you have already specified.

To select and parameterize the underlying library block:

1. Specify the type of semiconductor device using the **Switching
   device** parameter.
2. Specify the underlying library block using the **Library block**
   parameter.
3. Choose which ports you want to enable in the underlying library block using the
   **Modeling option**, **Gate-control port**, and
   **Number of terminals** parameters. The **Modeling
   option** parameter determines whether you expose the thermal port,
   **H**, and defines the mathematical model that the underlying library
   block uses. The visibility of these parameters depends on the **Switching
   device** and **Library block** parameters.
4. Click the **Edit parameters** button to open the block dialog box
   for the underlying library block and specify the block parameters.

To switch to a different underlying library block, repeat steps 2 and 4. Parameter values
that are common to both blocks carry over to your new selection. The Semiconductor Switch Selector block also
stores parameter values that are specific to the underlying library block, so you can easily
return to a previous choice.

If you no longer want to switch between fidelities, click the **Remove
Semiconductor Switch Selector block mask** button. This button removes the
Semiconductor Switch Selector block and replaces it with the underlying block. This action is
irreversible.

This table shows the underlying library blocks that the Semiconductor Switch Selector block supports for
each value of the **Switching device** parameter. Typically, you use simpler
blocks for system-level design and more complex blocks for detailed component design. For more
information about choosing the right level of fidelity for your application, see Choose Blocks to Model Semiconductor Devices. For more information about
the underlying library block, see the relevant block reference page from this table.

| Switching Device | Library Block | |
| --- | --- | --- |
| Low or Medium Fidelity | High Fidelity |
| MOSFET | - Ideal Semiconductor   Switch - MOSFET (Ideal,   Switching) | - N-Channel MOSFET - P-Channel MOSFET |
| IGBT | - Ideal Semiconductor   Switch - IGBT (Ideal, Switching) | - N-Channel IGBT |
| Thyristor | - Thyristor (Piecewise   Linear) | - Thyristor |
| GTO | - GTO | Not supported |

If you change the **Library block** parameter, the Semiconductor Switch Selector block icon
updates to the underlying library block icon.

The **Gate-control port**, **Modeling option**, and
**Number of terminals** parameters are common to the Semiconductor Switch Selector block and
the underlying library block. However, you must set the values of these parameters in the
Semiconductor Switch Selector block mask. If you click the **Edit parameters** button, the
underlying library block does not enable these parameters. You can only enable these
parameters in the underlying library block by removing the Semiconductor Switch Selector block mask.

If you change the **Library block** parameter, the values of all
parameters that are common to both blocks, including initial targets and nominal values, carry
over to the new block. Values of equivalent parameters that have different names in different
blocks also carry over. This table shows the equivalent parameters for MOSFETs.

| Equivalent Parameter | Library Block | | | |
| --- | --- | --- | --- | --- |
| Ideal Semiconductor Switch | MOSFET (Ideal, Switching) | N-Channel IGBT | P-Channel MOSFET |
| Threshold voltage | **Threshold voltage, Vth** | | **Gate-source threshold voltage, Vth** | |
| On-state resistance | **On-state resistance** | **Drain-source on resistance, R\_DS(on)** | | |

This table shows the equivalent parameters for IGBTs.

| Equivalent Parameter | Library Block | | |
| --- | --- | --- | --- |
| Ideal Semiconductor Switch | IGBT (Ideal, Switching) | N-Channel IGBT Block |
| Threshold voltage | **Threshold voltage, Vth** | | **Gate-emitter threshold voltage, Vge(th)** |

If you change the **Switching device** parameter, the parameter values do
not carry over. So you can also use the Semiconductor Switch Selector block to compare an optimized MOSFET to an
optimized IGBT, thyristor, or GTO.
