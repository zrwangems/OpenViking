---
type: simulink-block
title: 'Constant Volume Chamber (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Isothermal Liquid Models / Elements'
documentation_page: 'constantvolumechamberil'
documentation_source_path: 'ref/constantvolumechamberil.html'
language: en
---

# Constant Volume Chamber (IL)

## Ports

### Conserving

### **A** — Chamber inlet isothermal liquid

Isothermal liquid conserving port associated with the chamber inlet.

## Parameters

### **Chamber volume** — Volume of fluid inside the chamber `0.001 m^3` (default) | positive scalar

Volume of fluid in the chamber. This volume is constant during simulation.

## Libraries

Simscape / Foundation Library / Isothermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Chamber with one port and fixed volume of isothermal liquid

The Constant Volume Chamber (IL) block models accumulation
of mass in a chamber containing a fixed volume of isothermal liquid. The chamber has one
inlet, labeled **A**.

The chamber can exchange mass with the connected isothermal liquid network. The pressure
inside the chamber evolves based on the compressibility of the fluid volume.

Mass conservation relates the mass flow rate to the pressure of the internal node
representing the fluid volume:

dρmixdpIp˙IV=m˙A,

where:

- m˙A is the mass flow rate at port
  **A**. The flow rate associated with a port is positive when it flows
  into the block.
- *p*I is the pressure inside the chamber. There
  is no flow resistance between port **A** and the chamber interior,
  therefore, pressure at port **A** is assumed to be equal to this
  pressure, *p*A =
  *p*I.
- *V* is the volume of fluid inside the chamber.
- *ρ*mix is fluid mixture density.

The fluid can be a mixture of pure liquid and a small amount of entrained air, as
specified by the Isothermal Liquid Properties (IL) block
connected to the circuit. Equations used to compute
*ρ*mix depend on the selected isothermal liquid
model. For detailed information, see Isothermal Liquid Modeling Options.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.

### Assumptions and Limitations

- The chamber walls are perfectly rigid.
- There is no flow resistance between port **A** and the chamber
  interior.
