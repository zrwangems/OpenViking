---
type: simulink-block
title: 'Annular Leakage (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Orifices'
documentation_page: 'annularleakageil'
documentation_source_path: 'ref/annularleakageil.html'
language: en
---

# Annular Leakage (IL)

## Ports
```yaml
ports:
- name: A
  summary: Liquid port isothermal liquid
  direction: conserving
- name: B
  summary: Liquid port isothermal liquid
  direction: conserving
- name: L
  summary: Variable overlap length physical signal
  direction: input
- name: E
  summary: Variable eccentricity physical signal
  direction: input
```

### Conserving

### **A** — Liquid port isothermal liquid

Entry or exit port of the liquid to or from the orifice.

### **B** — Liquid port isothermal liquid

Entry or exit port of the liquid to or from the orifice.
### Input

### **L** — Variable overlap length physical signal

Optional physical signal port that provides the variable overlap
length between the sleeve and annular insert.

#### Dependencies

To expose this port, set **Overlap length
specification** to
`Variable`.

### **E** — Variable eccentricity physical signal

Optional physical signal port that provides variable eccentricity of
the annular insert to the sleeve.

#### Dependencies

To expose this port, set **Eccentricity
specification** to
`Variable`.
## Parameters
```yaml
parameters:
- name: Overlap length specification
  summary: Type of insert-sleeve overlap Constant (default) | Variable
  group: ''
- name: Overlap length
  summary: Overlap between tube and insert 1e-3 m (default) | positive scalar
  group: ''
- name: Minimum overlap length
  summary: Minimum overlap between tube and insert 1e-6 m (default) | positive scalar
  group: ''
- name: Eccentricity specification
  summary: Eccentricity variability Constant (default) | Variable
  group: ''
- name: Eccentricity
  summary: Center of insert offset with respect to sleeve center 0 m (default) | positive scalar
  group: ''
- name: Inner radius
  summary: Radius of insert 9.8e-3 m (default) | positive scalar
  group: ''
- name: Outer radius
  summary: Radius of tube 1e-2 m (default) | positive scalar
  group: ''
```

### **Overlap length specification** — Type of insert-sleeve overlap `Constant` (default) | `Variable`

Whether the length-wise sleeve-insert overlap is constant or
variable.

### **Overlap length** — Overlap between tube and insert `1e-3 m` (default) | positive scalar

Length-wise overlap between the insert and tube.

#### Dependencies

To enable this parameter, set **Overlap length
specification** to
`Constant`.

### **Minimum overlap length** — Minimum overlap between tube and insert `1e-6 m` (default) | positive scalar

Lower limit to the length-wise overlap between the insert and tube. Any
length shorter than this value will be set to the specified minimum.

#### Dependencies

To enable this parameter, set **Overlap length
specification** to
`Variable`.

### **Eccentricity specification** — Eccentricity variability `Constant` (default) | `Variable`

Whether the orifice eccentricity changes or remains at a set value.

### **Eccentricity** — Center of insert offset with respect to sleeve center `0 m` (default) | positive scalar

The distance between the center of the orifice and the center of the insert.

#### Dependencies

To enable this parameter, set **Eccentricity
specification** to
`Constant`.

### **Inner radius** — Radius of insert `9.8e-3 m` (default) | positive scalar

Insert radius *r*.

### **Outer radius** — Radius of tube `1e-2 m` (default) | positive scalar

Tube radius *R*, measured from the tube center to the inner wall.
## Libraries

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Orifices

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Models annular leakage between a circular tube and a round insert in an isothermal flow

The Annular Leakage (IL) block models annular leakage between a circular tube and a
round insert in an isothermal liquid network. The insert can be located off-center from
the tube and can have varying lengthwise overlap with the tube.

Ports **A** and **B** correspond with the orifice
inlet and outlet. The input ports **L** and **E** are
optional physical signal ports that model variable overlap length (L) and variable
eccentricity (E).

### The Mass Flow Rate Equation

The leakage mass flow rate is calculated from the pressure-flow rate equation

m˙=π(R−r)3(R+r)12v(pA−pB)l[1+3εsat2R(R+r)+38ε4(R−r)(R+r)],

where:

- *R* is the annulus outer radius.
- *r* is the annulus inner radius.
- *p*A is the pressure at port
  **A**.
- *p*B is the pressure at port
  **B**.
- *ν* is the fluid kinematic viscosity.
- *l* is the overlap length.
- ε is the eccentricity ratio, ε=eR−r, where *e* is the eccentricity, which
  can be defined as a physical signal or constant value.
- *ε*sat is the saturated
  eccentricity ratio, which is ε for constant orifices, or the physical
  signal connected to port **L** for variable orifices.
  The eccentricity ratio is always between 0 and 1.

When modeling a variable overlap length, the user-defined minimum overlap length
is used if the physical signal falls below the value of the **Minimum
overlap length** parameter.

### Assumptions and Limitations

The pressure-flow equation is valid only for fully-developed, laminar flows. The flow
Reynolds number can be determined using Re=m˙Dhμπ(R2−r2) or by checking the simulation log in the Results Explorer or the
Simulation Data Inspector. For more information, see Data Logging.
