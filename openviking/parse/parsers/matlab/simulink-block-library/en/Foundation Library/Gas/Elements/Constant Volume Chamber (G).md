---
type: simulink-block
title: 'Constant Volume Chamber (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'constantvolumechamberg'
documentation_source_path: 'ref/constantvolumechamberg.html'
language: en
---

# Constant Volume Chamber (G)

## Ports
```yaml
ports:
- name: A
  summary: Chamber inlet gas
  direction: conserving
- name: B
  summary: Chamber inlet gas
  direction: conserving
- name: C
  summary: Chamber inlet gas
  direction: conserving
- name: D
  summary: Chamber inlet gas
  direction: conserving
- name: H
  summary: Temperature inside chamber thermal
  direction: conserving
```

### Conserving

### **A** — Chamber inlet gas

Gas conserving port associated with the chamber inlet.

### **B** — Chamber inlet gas

Gas conserving port associated with the second chamber inlet.

#### Dependencies

This port is visible if you set the **Number of
ports** parameter to `2`,
`3`, or
`4`.

### **C** — Chamber inlet gas

Gas conserving port associated with the third chamber inlet.

#### Dependencies

This port is visible if you set the **Number of
ports** parameter to `3` or
`4`.

### **D** — Chamber inlet gas

Gas conserving port associated with the fourth chamber inlet. If a
chamber has four inlet ports, you can use it as a junction in a cross
connection.

#### Dependencies

This port is visible only if you set the **Number of
ports** parameter to
`4`.

### **H** — Temperature inside chamber thermal

Thermal conserving port associated with the temperature of the
gas inside the chamber.
## Parameters
```yaml
parameters:
- name: Chamber volume
  summary: Volume of gas in the chamber 0.001 m^3 (default)
  group: ''
- name: Number of ports
  summary: Number of inlet ports in the chamber 1 (default) | 2 | 3 | 4
  group: ''
- name: Cross-sectional area at port A
  summary: Area normal to flow path at the chamber inlet 0.01 m^2 (default)
  group: ''
- name: Cross-sectional area at port B
  summary: Area normal to flow path at the chamber inlet 0.01 m^2 (default)
  group: ''
- name: Cross-sectional area at port C
  summary: Area normal to flow path at the chamber inlet 0.01 m^2 (default)
  group: ''
- name: Cross-sectional area at port D
  summary: Area normal to flow path at the chamber inlet 0.01 m^2 (default)
  group: ''
```

### **Chamber volume** — Volume of gas in the chamber 0.001 m^3 (default)

Volume of gas in the chamber. The chamber is rigid and therefore its
volume is constant during simulation. The chamber is assumed to be
completely filled with gas at all times.

### **Number of ports** — Number of inlet ports in the chamber `1` (default) | `2` | `3` | `4`

Number of inlet ports in the chamber. The chamber can have between one and
four ports, labeled from **A** to **D**.
When you modify the parameter value, the corresponding ports are exposed or
hidden in the block icon.

### **Cross-sectional area at port A** — Area normal to flow path at the chamber inlet `0.01 m^2` (default)

Cross-sectional area of the chamber inlet at port **A**,
in the direction normal to gas flow path.

### **Cross-sectional area at port B** — Area normal to flow path at the chamber inlet `0.01 m^2` (default)

Cross-sectional area of the chamber inlet at port **B**,
in the direction normal to gas flow path.

#### Dependencies

Enabled when port **B** is visible, that is, when the
**Number of ports** parameter is set to
`2`, `3`, or
`4`.

### **Cross-sectional area at port C** — Area normal to flow path at the chamber inlet `0.01 m^2` (default)

Cross-sectional area of the chamber inlet at port **C**,
in the direction normal to gas flow path.

#### Dependencies

Enabled when port **C** is visible, that is, when the
**Number of ports** parameter is set to
`3` or `4`.

### **Cross-sectional area at port D** — Area normal to flow path at the chamber inlet `0.01 m^2` (default)

Cross-sectional area of the chamber inlet at port **D**,
in the direction normal to gas flow path.

#### Dependencies

Enabled when port **D** is visible, that is, when the
**Number of ports** parameter is set to
`4`.
## Libraries

Simscape / Foundation Library / Gas / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

## Description

Chamber with fixed volume of gas and variable number of ports

The Constant Volume Chamber (G) block models mass and energy
storage in a gas network. The chamber contains a constant volume of gas. It can have
between one and four inlets. The enclosure can exchange mass and energy with the
connected gas network and exchange heat with the environment, allowing its internal
pressure and temperature to evolve over time. The pressure and temperature evolve based
on the compressibility and thermal capacity of the gas volume.

### Mass Balance

Mass conservation relates the mass flow rates to the dynamics
of the pressure and temperature of the internal node representing
the gas volume:

∂M∂p⋅dpIdt+∂M∂T⋅dTIdt=m˙A+m˙B+m˙C+m˙D,

where:

- ∂M∂p is
  the partial derivative of the mass of the gas volume with respect
  to pressure at constant temperature and volume.
- ∂M∂T is
  the partial derivative of the mass of the gas volume with respect
  to temperature at constant pressure and volume.
- *p*I is the pressure of the gas
  volume. The pressure at ports **A**, **B**, **C**, and
  **D** is assumed to be equal to this
  pressure, *p*A =
  *p*B =
  *p*C =
  *p*D =
  *p*I.
- *T*I is the temperature of the gas
  volume. The temperature at port **H** is assumed to be
  equal to this temperature, *T*H =
  *T*I.
- *t* is time.
- m˙A is the mass flow rate at port
  **A**. The flow rate associated with a port is positive
  when it flows into the block.
- m˙B is the mass flow rate at port
  **B**. The flow rate associated with a port is positive
  when it flows into the block.
- m˙C is the mass flow rate at port
  **C**. The flow rate associated with a port is positive
  when it flows into the block.
- m˙D is the mass flow rate at port
  **D**. The flow rate associated with a port is positive
  when it flows into the block.

### Energy Balance

Energy conservation relates the energy and heat flow rates to
the dynamics of the pressure and temperature of the internal node
representing the gas volume:

∂U∂p⋅dpIdt+∂U∂T⋅dTIdt=ΦA+ΦB+ΦC+ΦD+QH,

where:

- ∂U∂p is
  the partial derivative of the internal energy of the gas volume with
  respect to pressure at constant temperature and volume.
- ∂U∂T is
  the partial derivative of the internal energy of the gas volume with
  respect to temperature at constant pressure and volume.
- ФA is the energy flow rate at port
  **A**.
- ФB is the energy flow rate at port
  **B**.
- ФC is the energy flow rate at port
  **C**.
- ФD is the energy flow rate at port
  **D**.
- *Q*H is the heat flow rate at port
  **H**.

### Partial Derivatives for Perfect and Semiperfect Gas Models

The partial derivatives of the mass *M* and the internal energy
*U* of the gas volume, with respect to pressure and temperature at
constant volume, depend on the gas property model. For perfect and semiperfect gas models,
the equations are:

∂M∂p=VρIpI∂M∂T=−VρITI∂U∂p=V(hIZRTI−1)∂U∂T=VρI(cpI−hITI)

where:

- *ρ*I is
  the density of the gas volume.
- *V* is the volume of gas.
- *h*I is the
  specific enthalpy of the gas volume.
- *Z* is the compressibility factor.
- *R* is the specific gas constant.
- *c*pI is the
  specific heat at constant pressure of the gas volume.

### Partial Derivatives for Real Gas Model

For real gas model, the partial derivatives of the mass *M* and the internal
energy *U* of the gas volume, with respect to pressure and temperature at
constant volume, are:

∂M∂p=VρIβI∂M∂T=−VρIαI∂U∂p=V(ρIhIβI−TIαI)∂U∂T=VρI(cpI−hIαI)

where:

- *β* is the isothermal bulk
  modulus of the gas volume.
- *α* is the isobaric thermal
  expansion coefficient of the gas volume.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables and Initial Conditions for Blocks with Finite Gas Volume.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.

### Assumptions and Limitations

- The chamber walls are perfectly rigid.
- There is no flow resistance between ports **A**,
  **B**, **C**, and
  **D** and the chamber interior.
- There is no thermal resistance between port **H** and
  the chamber interior.
