---
type: simulink-block
title: 'Convective Heat Transfer'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Elements'
documentation_page: 'convectiveheattransfer'
documentation_source_path: 'ref/convectiveheattransfer.html'
language: en
---

# Convective Heat Transfer

## Ports

### Input

### **K** — Heat transfer coefficient control signal, W/(K\*m^2) physical signal

Input physical signal that controls the heat transfer coefficient. The signal
saturates when the value is outside the minimum limit specified by the
**Minimum heat transfer coefficient** block parameter.

#### Dependencies

To enable this port, set the **Convection type** parameter to
`Variable`.
### Conserving

### **A** — Body A thermal

Thermal conserving port associated with body A.

### **B** — Body B thermal

Thermal conserving port associated with body B.

## Parameters

### **Convection type** — How to specify heat transfer coefficient `Constant` (default) | `Variable`

Whether to specify the heat transfer coefficient of the material as a block
parameter or an input signal:

- `Constant` — The heat transfer coefficient, specified
  by the **Heat transfer coefficient** parameter, remains constant
  during simulation.
- `Variable` — The input physical signal at port
  **K** specifies the heat transfer coefficient, which can vary
  during simulation. The **Minimum heat transfer coefficient**
  parameter specifies the lower bound for the heat transfer coefficient.

### **Area** — Area of heat transfer `1e-4 m^2` (default) | positive scalar

Surface area of the heat transfer.

### **Heat transfer coefficient** — Convection heat transfer coefficient `20 W/(K*m^2)` (default) | positive scalar

Convection heat transfer coefficient.

#### Dependencies

To enable this parameter, set **Convection type** to
`Constant`.

### **Minimum heat transfer coefficient** — Lower bound for heat transfer coefficient `1e-3 W/(K*m^2)` (default) | positive scalar

Lower bound for the convection heat transfer coefficient. The input signal at port
**K** saturates at this value to prevent the heat transfer
coefficient from further decreasing.

#### Dependencies

To enable this parameter, set **Convection type** to
`Variable`.

## Libraries

Simscape / Foundation Library / Thermal / Thermal Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007b**

### R2022b: Model variable heat transfer coefficient

The new **Convection type** parameter lets the heat transfer
coefficient be either constant, which you specify by the **Heat transfer
coefficient** parameter, or variable, which you specify as a physical signal at
port **K**.

In the default configuration, with **Convection type** parameter set to
`Constant`, the block functions as in previous releases.

## Description

Heat transfer by convection

The Convective Heat Transfer block represents heat transfer by convection
between two bodies by means of fluid motion. The Newton law of cooling describes the
transfer,

Q=k⋅A⋅(TA−TB),

where:

- *Q* is the heat flow.
- *k* is the convection heat transfer coefficient.
- *A* is the surface area.
- *T*A and
  *T*B are the temperatures of the two
  bodies.

The heat transfer coefficient, *k*, can be either constant, which you
specify by using the **Heat transfer coefficient** parameter, or variable,
which you specify by using the physical signal at port **K**.

**A** and **B** are thermal conserving ports associated
with the points between which the heat transfer by convection takes place. Because the block
positive direction is from port **A** to port **B**, the
heat flow is positive if it flows from **A** to **B**.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
