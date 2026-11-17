---
type: simulink-block
title: 'Variable Thermal Resistance'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Elements'
documentation_page: 'variablethermalresistance'
documentation_source_path: 'ref/variablethermalresistance.html'
language: en
---

# Variable Thermal Resistance

## Ports
```yaml
ports:
- name: R
  summary: Thermal resistance control signal, K/W physical signal
  direction: input
- name: A
  summary: Layer A thermal
  direction: conserving
- name: B
  summary: Layer B thermal
  direction: conserving
```

### Input

### **R** — Thermal resistance control signal, K/W physical signal

Input physical signal that specifies the thermal resistance
value.
### Conserving

### **A** — Layer A thermal

Thermal conserving port associated with layer A.

### **B** — Layer B thermal

Thermal conserving port associated with layer B.
## Parameters
```yaml
parameters:
- name: Minimum thermal resistance
  summary: Minimum thermal resistance value allowed 0 K/W (default)
  group: ''
```

### **Minimum thermal resistance** — Minimum thermal resistance value allowed 0 K/W (default)

If the input physical signal falls below this value, the resistance
remains at this value.
## Libraries

Simscape / Foundation Library / Thermal / Thermal Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Variable resistance in thermal systems

The Variable Thermal Resistance block lets you model a variable heat
transfer process in generalized terms, independent of whether it is by conduction,
convection, radiation, or a combination thereof. Thermal resistance is an abstract
quantity that relates the thermal conductivity, the heat transfer coefficient, and the
radiation coefficient. Thermal resistance of this block can vary with time, according to
the input physical signal at port R.

The heat transfer equation for the Thermal Resistance block is:

R⋅Q=ΔT

where:

- *R* is the thermal resistance.
- *Q* is the heat flow rate.
- *ΔT* is the temperature difference between layers.

Thermal resistance is related to the other heat transfer quantities as follows:

R=Dk⋅A=1h⋅A=1r⋅A(TA2+TB2)(TA+TB)

where:

- *D* is material thickness, that is, distance between layers.
- *A* is area normal to the heat flow direction.
- *k* is thermal conductivity of the material.
- *h* is convection heat transfer coefficient.
- *r* is radiation coefficient.
- *T*A and
  *T*B are temperatures at ports A and
  B, respectively.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
