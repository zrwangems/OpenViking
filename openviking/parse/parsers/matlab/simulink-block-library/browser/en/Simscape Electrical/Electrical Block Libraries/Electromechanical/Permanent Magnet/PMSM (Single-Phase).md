---
type: simulink-block
title: 'PMSM (Single-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Electromechanical / Permanent Magnet'
documentation_page: 'pmsmsinglephase'
documentation_source_path: 'ref/pmsmsinglephase.html'
language: en
---

# PMSM (Single-Phase)

## Ports

### Conserving

### **R** — Machine rotor mechanical rotational

Mechanical rotational conserving port associated with the machine
rotor.

### **C** — Machine case mechanical rotational

Mechanical rotational conserving port associated with the machine
case.

### **+** — Negative electrical

Electrical conserving port associated with the supply positive
terminal.

### **-** — Positive electrical

Electrical conserving port associated with the supply negative
terminal.

### **HS** — Stator thermal port thermal

Thermal conserving port associated with the stator.

#### Dependencies

To enable this port, set **Modeling option** to `Show
thermal port`.

### **HR** — Rotor thermal port thermal

Thermal conserving port associated with the rotor.

#### Dependencies

To enable this port, set **Modeling option** to
`Show thermal port`.

## Parameters

### **Modeling option** — Whether to enable thermal ports `No thermal port` (default) | `Show thermal port`

Whether to enable the thermal ports of the block and model the effects of generated heat and motor temperature.

### Main

### **Number of pole pairs** — Rotor pole pairs `2` (default) | positive integer

Number of permanent magnet pole pairs on the rotor.

### **Permanent magnet flux linkage parameterization** — Parameterization method `Specify flux linkage` (default) | `Specify back EMF constant`

Method for parameterizing the stator.

#### Dependencies

Selecting `Specify flux linkage` exposes
the **Permanent magnet flux linkage**
parameter.

Selecting `Specify back EMF constant` exposes the
**Back EMF constant** parameter.

### **Permanent magnet flux linkage** — Flux linkage `0.2` `Wb` (default) | positive scalar

Peak permanent magnet flux linkage.

#### Dependencies

Selecting `Specify flux linkage` for the
**Permanent magnet flux linkage
parameterization** parameter exposes the
**Permanent magnet flux linkage**
parameter.

### **Back EMF constant** — Back-electromotive force constant `0.4` `V/(rad/s)` (default) | positive scalar

Back-electromotive force constant.

#### Dependencies

Selecting `Specify back EMF constant` for the
**Permanent magnet flux linkage
parameterization** parameter exposes the **Back
EMF constant** parameter.

### **Inductance of stator coil** — Inductance `1.15` `H` (default) | positive scalar

The direct-axis inductance.

### **Resistance of stator coil** — Resistance `150` `Ohm` (default) | positive scalar

Resistance of each of the stator windings.

### **Rotor position at standstill due to asymmetric airgap** — Rotor angular position at standstill `45` `deg` (default) | positive scalar in the interval [0, 360] deg

Rotor angular position at standstill due to asymmetric air gap.

### Mechanical

### **Rotor inertia** — Rotor moment of inertia `1e-6` `kg*m^2` (default) | positive scalar

Inertia of the rotor attached to mechanical translational port
**R**.

### **Rotor damping** — Rotor damping `0` `N*m/(rad/s)` (default) | positive scalar

Damping of the rotor.

### Thermal

To enable these parameters, set **Modeling option** to
`Show thermal port`.

### **Measurement temperature** — Rated temperature `298.15` `K` (default) | real scalar

Temperature for which motor parameters are quoted.

### **Resistance temperature coefficient** — Temperature coefficient `3.93e-3` `1/K` (default) | positive scalar

Coefficient α in the equation relating resistance to temperature for
all three windings, as described in Thermal Model for Actuator Blocks. The default value,
`3.93e-3` 1/K, is for copper.

### **Permanent magnet flux temperature coefficient** — Permanent magnet flux temperature coefficient `-0.001` `1/K` (default)

Fractional rate of change of permanent magnet flux density with
temperature. Use this parameter to linearly reduce the torque and the
induced back EMF as temperature rises.

### **Thermal mass for each stator winding** — Winding thermal mass `100` `J/K` (default) | positive scalar

Thermal mass value for each stator winding. The thermal mass is the
energy required to raise the temperature by one degree.

### **Rotor thermal mass** — Rotor thermal mass `200` `J/K` (default) | positive scalar

Thermal mass of the rotor. The thermal mass is the energy required to
raise the temperature of the rotor by one degree.

## Libraries

Simscape / Electrical / Electromechanical / Permanent Magnet

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Single-phase permanent magnet synchronous motor

The PMSM (Single-Phase) represents a single-phase
permanent magnet synchronous motor (PMSM), a type of DC motor that is useful for
automation applications.

The figure shows the topology of the single-phase PMSM drive.

The figure shows the motor construction with a single pole-pair on the rotor.
Single-phase PMSMs are not self-starting unless the air gap is asymmetrical.

The figure shows the equivalent circuit for the PMSM
(Single-Phase) block.

### Equations

The motor voltage equations are

vs=Ri+Ldidt+e

and

vs=Vmsin(ωst+ε),

where:

- *vs* is the supply
  voltage.
- *i* is the instantaneous motor current.
- *R* is the resistance of the windings.
- *L* is the self-inductance of the windings.
- *e* is the back-electromotive force (BEMF).
- *ɷs* is the angular frequency
  of the supply voltage.
- *ε* is the angle of the supply voltage.

The back electro-motive force (BEMF) is

e=keωesin(θe),

where:

- *ɷe* is the rotor electrical
  angular velocity.
- *θe* is the rotor electrical
  angle.
- *ke* is the BEMF
  constant.

Due to the large low-permeability gaps between the stator and rotor, the saturation can be
neglected. Therefore, the electric torque equations are

Te=p i ψmsin(θe)

and

ψm=kep,

where:

- *Te* is the electric
  torque.
- *ψm* is the permanent magnet
  flux linkage.
- *p* is the number of pole pairs.

The mechanical equation is

Jmdωrdt=Te−TL−Bmωr,

where:

- *Jm* is the rotor
  inertia.
- *TL* is the torque
  load.
- *Bm* is the friction
  coefficient.
- *ɷr* is the rotor mechanical
  angular velocity.

### Model Thermal Effects

You can expose thermal ports to simulate the effects of generated heat and motor temperature. To expose the thermal ports and the **Thermal** parameters, set the **Modeling option** parameter to either:

- `No thermal port` — The block does not contain thermal ports.
- `Show thermal port` — The block contains thermal conserving ports for the stator and the rotor.

For more information about using thermal ports in actuator blocks, see Simulating Thermal Effects in Rotational and Translational Actuators.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
