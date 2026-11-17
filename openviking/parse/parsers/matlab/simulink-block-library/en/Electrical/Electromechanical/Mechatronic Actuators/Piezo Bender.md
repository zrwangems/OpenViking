---
type: simulink-block
title: 'Piezo Bender'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Mechatronic Actuators'
documentation_page: 'piezobender'
documentation_source_path: 'ref/piezobender.html'
language: en
---

# Piezo Bender

## Ports
```yaml
ports:
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
- name: Ctr
  summary: Translational case mechanical
  direction: conserving
- name: Cro
  summary: Rotational case mechanical
  direction: conserving
- name: Rtr
  summary: Translational rotor mechanical
  direction: conserving
- name: Rro
  summary: Rotational rotor mechanical
  direction: conserving
```

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the piezo bender positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the piezo bender negative
terminal.

### **Ctr** — Translational case mechanical

Mechanical translational conserving port associated with the
case.

### **Cro** — Rotational case mechanical

Mechanical rotational conserving port associated with the case.

### **Rtr** — Translational rotor mechanical

Mechanical translational conserving port associated with the
rotor.

### **Rro** — Rotational rotor mechanical

Mechanical rotational conserving port associated with the
rotor.
## Parameters
```yaml
parameters:
- name: Number of elements
  summary: Number of elements 1 (default) | positive integer greater than or equal to 1
  group: Dimensions
- name: Total beam length
  summary: Total beam length 3.175E-2 m (default) | positive scalar
  group: Dimensions
- name: Beam width
  summary: Beam width 1.27E-2 m (default) | positive scalar
  group: Dimensions
- name: Beam thickness
  summary: Beam thickness 5.08E-4 m (default) | positive scalar
  group: Dimensions
- name: Parameterization
  summary: Steady-state parameterization Specify from a datasheet for clamped-free configuration (default) | Specify from
    material properties
  group: Steady-State
- name: Capacitance
  summary: Piezo bender capacitance 15 nF (default) | positive scalar
  group: Steady-State
- name: Rated drive voltage, Vrated
  summary: Rated drive voltage 180 V (default) | positive scalar
  group: Steady-State
- name: Free deflection at Vrated
  summary: Free deflection at Vrated +0.233 mm (default) | nonzero value
  group: Steady-State
- name: Blocking force at Vrated
  summary: Blocking force at Vrated -0.414 N (default) | scalar
  group: Steady-State
- name: Young modulus, E
  summary: Young modulus 1.36628e11 N/m^2 (default) | positive scalar
  group: Steady-State
- name: Piezoelectric stress coefficient, e31
  summary: Piezoelectric stress coefficient 7.5459 C/m^2 (default) | nonzero scalar
  group: Steady-State
- name: Dielectric constant
  summary: Dielectric constant 1.38965e-08 F/m (default) | positive scalar
  group: Steady-State
- name: Inertial effects
  summary: Inertial effects modeling option On (default) | Off
  group: Dynamics
- name: Parameterization
  summary: Inertia parameterization Specify from a datasheet for clamped-free configuration (default) | Specify from material
    properties
  group: Dynamics
- name: Beam mass
  summary: Beam mass 1.6 g (default) | positive scalar
  group: Dynamics
- name: First natural frequency
  summary: First natural frequency 391 Hz (default) | positive scalar
  group: Dynamics
- name: Rayleigh damping constant proportional to stiffness
  summary: Rayleigh damping constant proportional to stiffness 1e-5 s (default) | nonnegative scalar
  group: Dynamics
- name: Rayleigh damping constant proportional to mass
  summary: Rayleigh damping constant proportional to mass 0 1/s (default) | nonnegative scalar
  group: Dynamics
```

### Dimensions

### **Number of elements** — Number of elements `1` (default) | positive integer greater than or equal to 1

Number of elements in which the piezo bender beam is discretized using the
Euler-Bernoulli finite elements equations.

### **Total beam length** — Total beam length `3.175E-2` `m` (default) | positive scalar

Total length of the beam.

### **Beam width** — Beam width `1.27E-2` `m` (default) | positive scalar

Width of the beam.

### **Beam thickness** — Beam thickness `5.08E-4` `m` (default) | positive scalar

Thickness of the beam.

### Steady-State

### **Parameterization** — Steady-state parameterization `Specify from a datasheet for clamped-free configuration` (default) | `Specify from material properties`

Whether to parameterize the steady state parameters from a datasheet
or from material properties.

### **Capacitance** — Piezo bender capacitance `15` `nF` (default) | positive scalar

Capacitance of the piezo bender.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
from a datasheet for clamped-free
configuration`.

### **Rated drive voltage, Vrated** — Rated drive voltage `180` `V` (default) | positive scalar

Rated drive voltage.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
from a datasheet for clamped-free
configuration`.

### **Free deflection at Vrated** — Free deflection at Vrated `+0.233` `mm` (default) | nonzero value

Tip deflection when no force is applied. The sign of this parameter must be different
from the sign of the **Blocking force at Vrated**
parameter.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
from a datasheet for clamped-free
configuration`.

### **Blocking force at Vrated** — Blocking force at Vrated `-0.414` `N` (default) | scalar

Force that nullifies the tip deflection. The sign of this parameter must be different
from the sign of the **Free deflection at Vrated**
parameter.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
from a datasheet for clamped-free
configuration`.

### **Young modulus, E** — Young modulus `1.36628e11` `N/m^2` (default) | positive scalar

Young modulus, or the modulus of elasticity in tension.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
from material properties`.

### **Piezoelectric stress coefficient, e31** — Piezoelectric stress coefficient `7.5459` `C/m^2` (default) | nonzero scalar

(3,1) piezoelectric stress-charge coupling coefficient.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
from material properties`.

### **Dielectric constant** — Dielectric constant `1.38965e-08` `F/m` (default) | positive scalar

Dielectric constant that represents the relative permittivity of the
material. This parameter must be bigger than the vacuum
permittivity.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Specify
from material properties`.

### Dynamics

### **Inertial effects** — Inertial effects modeling option `On` (default) | `Off`

Whether to model inertial effects.

### **Parameterization** — Inertia parameterization `Specify from a datasheet for clamped-free configuration` (default) | `Specify from material properties`

Whether to parameterize the inertia parameters from a datasheet or
from material properties.

#### Dependencies

To enable this parameter, set **Inertial
effects** to `On`.

### **Beam mass** — Beam mass `1.6` `g` (default) | positive scalar

Mass of the beam.

#### Dependencies

To enable this parameter, set **Inertial effects** to
`On` and
**Parameterization** to `Specify
from material properties`.

### **First natural frequency** — First natural frequency `391` `Hz` (default) | positive scalar

First natural frequency.

#### Dependencies

To enable this parameter, set **Inertial
effects** to `On` and
**Parameterization** to `Specify
from a datasheet for clamped-free
configuration`.

### **Rayleigh damping constant proportional to stiffness** — Rayleigh damping constant proportional to stiffness `1e-5` `s` (default) | nonnegative scalar

Damping coefficient proportional to stiffness, for Rayleigh
damping.

### **Rayleigh damping constant proportional to mass** — Rayleigh damping constant proportional to mass `0` `1/s` (default) | nonnegative scalar

Damping coefficient proportional to mass, for Rayleigh damping.

#### Dependencies

To enable this parameter, set **Inertial
effects** to `On`.
## Libraries

Simscape / Electrical / Electromechanical / Mechatronic Actuators

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Piezoelectric bimorph beam of rectangular cross-section

The Piezo Bender block models a piezoeletric bimorph
beam of rectangular cross-section.

A piezo bender is a piezoelectric device that bends when you apply an electrical
potential between its plates. Conversely, when a piezo bender bends, it generates an
electrical potential.

A piezo bender comprises different rectangular layers of piezoelectic material with a
polarization perpendicular to the stack. This polarization is alternated in each layer.

### Equations

This figure shows the cartesian reference frame

where:

- *L* is the beam length.
- *w* is the beam width.
- *d* is the beam thickness.

These are the constitutive equations for a piezoelectric material in the
stress-charge formulation,

|  |  |
| --- | --- |
| T=[c]S−[e]TE | **(1)** |

|  |  |
| --- | --- |
| D=[e]S−[ϵS]E | **(2)** |

where:

- *T* is the stress field.
- *[c]* is the compliance tensor.
- *S* is the strain field.
- *[e]* is the piezo stress coefficient tensor.
- *E* is the electric field.
- *D* is the electric displacement field.
- *[ϵS]* is the permittivity
  tensor at constant or zero strain.

To model the flexibility, the block uses the Euler-Bernoulli finite-element beam equations.
The translation and rotation of each beam cross-section in function of the
*x*-axis determine the beam kinematics.

This block considers only the forces applied in the *y* direction and the
piezoelectric material is polarized to bend only in the *x-y*
plane. For this reason, to describe the kinematics, you only need to specify the
vertical displacement in the *y* direction of the center of gravity
of each cross-section, *y(x)*, and the rotation around the
*z*-axis of each cross-section,
*φz(x)*.

From the previous assumptions, the strain field in an Euler-Bernoulli beam subject
to bending is equal to:

|  |  |
| --- | --- |
| Sxx(x,y)=−ydφzdx(x). | **(3)** |

Because the electric field is constant between the positive and negative plates, Ey=vd, the block substitutes equation 3 into equation
1:

Txx(x,y)=−Eydφzdx(x)−e31vd.

In this equation, *E =
c11* is the Young modulus of the material and
*e31* is the (3,1) piezoelectric
stress-charge coupling coefficient, σxx=−e31Ey.

This equation defines the bending moment from the stress field:

Mz(x)=−∬yTxx(x,y) dS=∬Ey2dφzdx(x)+e31vdy dS.

Because the polarization of the material for y=[−d2,0] is the opposite than the polarization for y=[0,d2], the (3,1) piezoelectric stress-charge coupling coefficient
changes sign and the bending moment is defined by

Mz(x)=E12w d3dφzdx(x)+w d e31v=EIdφzdx(x)+w d e31v,

where I=112wd3 is the second moment of area of the rectangular
cross-section.

In this equation, the first term is the classical equation of a beam subject to bending,
and the second term is the electromechanical coupling due to the presence of a
voltage across the piezoelectric material. This voltage produces a uniform
electrical bending moment loaded along the beam.

The block then substitutes equation 3 into equation 2:

Dy(x,y)=−e31ydφzdx(x)+ϵvd.

The electric charge inside a volume is equal to the Gauss integral of the electric displacement:

dq(x)=∯Dy dS=e31dw dxdφzdx=e31dw dφz.

Then, this equation defines the charge accumulated between the two sections of the
beam due to the piezoelectric effect:

q=e31dw(φz(x2)−φz(x1)).

Finally, from the mechanical perspective, you can model a piezo bender as an
Euler-Bernoulli beam loaded with a uniform torque that is proportional to the voltage:

Mz(x)=EIdφzdx(x)+w d e31v

From the electrical perspective, you can model a piezo bender as a capacitor with
a charge source proportional to the bending angle:

q=e31d w(φzR−φzC)+ϵwldv.

### Finite Element Formulation

To discretize and solve the Euler-Bernoulli equations with the piezoelectric
coupling, the Piezo Bender block uses a Finite
Element method.

The block discretizes the piezo bender beam into a number of slices in the length direction
with the same width, *w*, and thickness, *d*. The
length of each element is equal to the total length of the beam divided by the
number of elements, l=LNelements.

This stiffness matrix of a finite element of an Euler-Bernoulli beam defines the
relationship between the vertical displacement and rotational angle of each end of
the beam element, and the corresponding forces and moments due to the beam elasticity:

[FCTCFRTR]=[12EIl36EIl2−12EIl36EIl26EIl24EIl−6EIl22EIl−12EIl3−6EIl212EIl3−6EIl26EIl22EIl−6EIl24EIl][yCφCyRφR].

Then, to obtain the equations for a piezo bender beam element, add the coupling
terms and the mass matrix for the inertia:

ρlwd420[15622l54−13l22l4l213l−3l25413l156−22l−13l−3l2−22l4l2][d2yCdt2d2φCdt2d2yRdt2d2φRdt20]+[12EIl36EIl2−12EIl36EIl206EIl24EIl−6EIl22EIle31wd−12EIl3−6EIl212EIl3−6EIl206EIl22EIl−6EIl24EIl−e31wd0−e31wd0e31wdϵwld][yCφCyRφRv]=[FCTCFRTRq].

Finally, this is the equation for a piezo bender beam element with damping:

ρlwd420[15622l54−13l22l4l213l−3l25413l156−22l−13l−3l2−22l4l2][d2yCdt2d2φCdt2d2yRdt2d2φRdt20]+[[B]⋯0⋮⋱⋮0⋯0][dyCdtdφCdtdyRdtdφRdt0]+[12EIl36EIl2−12EIl36EIl206EIl24EIl−6EIl22EIle31wd−12EIl3−6EIl212EIl3−6EIl206EIl22EIl−6EIl24EIl−e31wd0−e31wd0e31wdϵwld][yCφCyRφRv]=[FCTCFRTRq]

where:

- *l* is the element length.
- *w* is the element width.
- *d* is the element thickness.
- I=112wt3 is the second moment of area.
- *E* is the Young modulus.
- *m = ρlwd* is the element mass, where
  *ρ* is the mass density.
- *e31* is the (3,1)
  piezoelectric stress-charge coupling coefficient, σxx=−e31Ey.
- *ε* is the electrical permittivity.
- B=bkK+bmM is the damping matrix.
- *bm* is the Rayleigh damping
  coefficient proportional to mass.
- *bk* is the Rayleigh damping
  coefficient proportional to stiffness.
- K=[12EIl36EIl2−12EIl36EIl26EIl24EIl−6EIl22EIl−12EIl3−6EIl212EIl3−6EIl26EIl22EIl−6EIl24EIl] is the stiffness finite element matrix.
- M=ρlwd420[15622l54−13l22l4l213l−3l25413l156−22l−13l−3l2−22l4l2] is the mass matrix.
- *yC* is the deflection along
  the *y*-axis of the left-end of the element.
- *yR* is the deflection along
  the *y*-axis of the right-end of the element.
- *φC* is the rotation around
  the *z*-axis of the left-end of the element.
- *φR* is the rotation around
  the *z*-axis of the right-end of the element.
- *FC* is the force along the
  *y*-axis of the left-end of the element.
- *FR* is the force along the
  *y*-axis of the right-end of the element.
- *TC* is the torque in the
  *z*-axis of the left-end of the element.
- *TR* is the torque in the
  *z*-axis of the right-end of the element.
- *v* is the voltage across the top and bottom
  electrodes.
- *q* is the accumulated charge between the electrodes
  and the piezoelectric material.

### Datasheet Parameterization

A datasheet of a piezo bender usually provides this data:

- Dimensions (*l*, *w*,
  *d*)
- Mass, *m*
- Rated voltage, *vrated*
- Free deflection at rated voltage,
  *yfree*
- Blocking force at rated voltage,
  *Fblock*
- Capacitance, *Cpiezo*
- First resonant frequency,
  *f1*

It is possible to calculate the fundamental material parameters of a piezo bender
by using the datasheet parameters.

First, the block solves the voltage-force deflection relationships from the
steady-state equations with no torque applied and clamped-free configuration:

[12EIl3−6EIl20−6EIl24EIl−e31w d0e31w dε wld][yRφRv]=[FR0q].

These equations define the relationship between the tip deflection, voltage and
tip force:

yR=l2(4FR l+6 d w e31 v)12EI=l2 (4FR l+6 d w e31 v)E w d3=FR4l3Ewd3+v6 e31l2E d2yfree=6l2 d w e31 vrated12EI=6 e31l2 vratedE d2Fblock=−3 d w e31 vrated2l

The block computes the capacitance by assuming zero applied force:

Cpiezo=εl wd+e312l d2w2EI=εl wd+e31212l wEd=(ε+12e312E)l wd.

Finally, this equation shows the relationship between density and mass:

m=ρ lwd.

Once you have defined all the relationships between the fundamental and datasheet
parameters, you can calculate the fundamental parameters with these equations:

e31=−2 l Fblock3 d w vratedE=−4 Fblockl3yfreed3wε=dl w(Cpiezo+4Fblockyfreevrated2)

Then substitute these equations in the constitutive equations:

vvrated=FRFblock+yRyfreeq=Cpiezov+yfreevratedFR

**Dynamics Datasheet Parameterization**

You can calculate the first resonance frequency of a clamped-free beam of
uniform cross section by using this equation:

2πf0=1.8552EIm l3.

The block then parameterizes the dynamics directly by specifying the desired
natural frequency.

### Boundary Conditions

Beams have different boundary conditions at their left and right ends:

- Free — Both the displacement and rotation are equal to any value.
- Simply supported — The displacement is equal to
  `0`.
- Clamped — Both the displacement and rotation are equal to
  `0`.

This table shows the possible boundary configurations for a piezo bender
beam.

| **Configuration** | Model |
| --- | --- |
| Clamped-free |  |
| Supported-supported |  |
| Clamped-clamped |  |
