---
type: simulink-block
title: 'Translational Detent'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Brakes & Detents / Translational'
documentation_page: 'translationaldetent'
documentation_source_path: 'ref/translationaldetent.html'
language: en
---

# Translational Detent

## Ports
```yaml
ports:
- name: C
  summary: Case mechanical translational
  direction: conserving
- name: R
  summary: Rod mechanical translational
  direction: conserving
```

### Conserving

### **C** — Case mechanical translational

Mechanical translational conserving port associated with the
case.

### **R** — Rod mechanical translational

Mechanical translational conserving port associated with the slider or
rod.
## Parameters
```yaml
parameters:
- name: Parameterization
  summary: Detent characterization parameters By peak force and notch width (default) | By table lookup | By geometry
  group: Detent Characteristics
- name: Peak force
  summary: Maximum detent shear force 10 N (default) | positive scalar
  group: Detent Characteristics
- name: Notch width
  summary: Shear force region 30 mm (default) | positive scalar
  group: Detent Characteristics
- name: Relative displacement vector
  summary: Displacement lookup vector [-15 -12.3 -7.6 -1.1 1.1 7.6 12.3 15] mm | vector
  group: Detent Characteristics
- name: Force vector
  summary: Force lookup vector [0, 0, -8.365, -5.87, 5.87, 8.365, 0, 0] N (default) | vector
  group: Detent Characteristics
- name: Interpolation method
  summary: Method of interpolation between breakpoint values for table lookup Smooth (default) | Linear
  group: Detent Characteristics
- name: Ball diameter
  summary: Ball diameter measurement for ball-notch geometry 12 mm (default) | positive scalar
  group: Detent Characteristics
- name: Notch angle
  summary: Notch angle measurement for ball-notch geometry 120 deg (default) | positive scalar
  group: Detent Characteristics
- name: Notch depth
  summary: Notch depth measurement for ball-notch geometry 4.5 mm (default) | nonnegative scalar
  group: Detent Characteristics
- name: Preload force
  summary: Spring preload force measurement for ball-notch geometry 15 N (default) | nonnegative scalar
  group: Detent Characteristics
- name: Spring stiffness
  summary: Spring stiffness measurement for ball-notch geometry 3000 N/m (default) | nonnegative scalar
  group: Detent Characteristics
- name: Shear reversal region
  summary: Shear reversal region length measurement for ball-notch geometry 0.1 mm (default) | nonnegative scalar
  group: Detent Characteristics
- name: Initial relative position
  summary: Starting location 0 mm (default) | scalar
  group: Detent Characteristics
- name: Viscous friction coefficient
  summary: Proportional viscous friction 0.1 N/(m/s) (default) | nonnegative scalar
  group: Friction
- name: Friction to peak force ratio
  summary: Kinetic friction ratio 0.01 (default) | positive scalar
  group: Friction
- name: Kinetic friction coefficient
  summary: Proportional kinetic friction 0.1 (default) | positive scalar
  group: Friction
- name: Friction velocity threshold
  summary: Velocity that relates to peak kinetic friction 0.05 m/s (default) | positive scalar
  group: Friction
```

### Detent Characteristics

### **Parameterization** — Detent characterization parameters `By peak force and notch width` (default) | `By table lookup` | `By geometry`

Detent characteristic specification.

- `By peak force and notch width` —
  Specify detent characteristics by the peak shear force and the
  notch width.
- `By table lookup` — Define the detent
  characteristics by one-dimensional table lookup based on the
  relative displacement between the slider and case.
- `By geometry` — Define the detent
  characteristics by ball-notch geometry and dynamics.

### **Peak force** — Maximum detent shear force `10` `N` (default) | positive scalar

Peak shear force developed inside the detent.

#### Dependencies

To enable this parameter, set
**Parameterization** to `By peak
force and notch width`.

### **Notch width** — Shear force region `30` `mm` (default) | positive scalar

Width of the region where the shear force develops.

#### Dependencies

To enable this parameter, set
**Parameterization** to `By peak
force and notch width`.

### **Relative displacement vector** — Displacement lookup vector `[-15 -12.3 -7.6 -1.1 1.1 7.6 12.3 15]` `mm` | vector

Vector of input relative displacements that corresponds to the values
in the **Force vector** parameter. This vector must be
same the size as the **Force vector** parameter. You
must specify the displacements in increasing order.

#### Dependencies

To enable this parameter, set
**Parameterization** to `By table
lookup`.

### **Force vector** — Force lookup vector `[0, 0, -8.365, -5.87, 5.87, 8.365, 0, 0]` `N` (default) | vector

Vector of input values for the shear force that corresponds to the
**Relative displacement vector** parameter.

#### Dependencies

To enable this parameter, set
**Parameterization** to `By table
lookup`.

### **Interpolation method** — Method of interpolation between breakpoint values for table lookup `Smooth` (default) | `Linear`

Lookup table breakpoint interpolation. The block uses the
`tablelookup` function to model nonlinearity by
using array data to map input values to output values.

- `Linear` — Select this option for the
  lowest computational cost.
- `Smooth` — Select this option to
  produce a continuous curve with continuous first-order
  derivatives.

For more information, see `tablelookup`.

#### Dependencies

To enable this parameter, set
**Parameterization** to `By table
lookup`.

### **Ball diameter** — Ball diameter measurement for ball-notch geometry `12` `mm` (default) | positive scalar

Cross sectional diameter of the ball..

#### Dependencies

To enable this parameter, set
**Parameterization** to `By
geometry`.

### **Notch angle** — Notch angle measurement for ball-notch geometry `120` `deg` (default) | positive scalar

Full angle of the notch.

#### Dependencies

To enable this parameter, set
**Parameterization** to `By
geometry`.

### **Notch depth** — Notch depth measurement for ball-notch geometry `4.5` `mm` (default) | nonnegative scalar

Depth of the notch in the slider.

#### Dependencies

To enable this parameter, set
**Parameterization** to `By
geometry`.

### **Preload force** — Spring preload force measurement for ball-notch geometry `15` `N` (default) | nonnegative scalar

Force to preload the detent spring.

#### Dependencies

To enable this parameter, set
**Parameterization** to `By
geometry`.

### **Spring stiffness** — Spring stiffness measurement for ball-notch geometry `3000` `N/m` (default) | nonnegative scalar

Stiffness of the detent spring.

#### Dependencies

To enable this parameter, set
**Parameterization** to `By
geometry`.

### **Shear reversal region** — Shear reversal region length measurement for ball-notch geometry `0.1` `mm` (default) | nonnegative scalar

Width of the region between notch faces.

#### Dependencies

To enable this parameter, set
**Parameterization** to `By
geometry`.

### **Initial relative position** — Starting location `0` `mm` (default) | scalar

Relative displacement of the slider and case when simulation
starts.

### Friction

### **Viscous friction coefficient** — Proportional viscous friction `0.1` `N/(m/s)` (default) | nonnegative scalar

Viscous friction coefficient for the ball-notch contact.

### **Friction to peak force ratio** — Kinetic friction ratio `0.01` (default) | positive scalar

Ratio by which to compute kinetic friction. The kinetic friction is
this ratio multiplied by the peak shear force.

#### Dependencies

To enable this parameter, set
**Parameterization** to `By peak
force and notch width` or `By table
lookup`.

### **Kinetic friction coefficient** — Proportional kinetic friction `0.1` (default) | positive scalar

Kinetic friction coefficient for the ball-notch contact.

#### Dependencies

To enable this parameter, set
**Parameterization** to `By
geometry`.

### **Friction velocity threshold** — Velocity that relates to peak kinetic friction `0.05` `m/s` (default) | positive scalar

Relative velocity required for peak kinetic friction in the
detent.
## Libraries

Simscape / Driveline / Brakes & Detents / Translational

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011b**

## Description

Double-sided, spring-loaded translational detent

The Translational Detent block represents a double-sided,
spring-loaded translational detent with a ball and conical notch. The detent slider
slides horizontally over the detent case. This interaction creates horizontal shear
force. Inside of the slider is the conical notch, and the detent-case contains a
vertical spring. The detent ball lies between the spring and the conical notch. The
model also includes viscous damping and kinetic friction between the slider and
case.

The figure demonstrates the geometry of the ball notch detent.

Translational detent dimensioning diagram

Here,

- *b* is the notch depth.
- *r* is the ball radius.
- *α* is the notch half angle.

Depending on how you parameterize the block, the shear force model is defined by geometric
and spring parameters, by the peak force and notch width, or by a table lookup that
specifies relative displacement versus force.

### Translational Detent Parameterization

When you set **Parameterization** to `By peak force and notch
width`, the block ensures that the force-relative displacement
curve provides a continuous force and force derivative over the detent region. The
peak forces are halfway between the detent center and detent edge, as the figure
shows.

Detent force profile plot

When you set **Parameterization** to `By
geometry`, the block uses four regions to define the shear force.
The figure displays these regions.

Translational detent region diagram. The regions are 1, 2, 3, 4, 3, 2, 1, where region 4 crosses the y-axis at the origin from negative to positive. There is more information in the table below.

Because the ball is spherical and the notch is symmetric, the horizontal force
versus displacement function is symmetric about the origin.

The table describes the ball position, contact angle, and shear force
contributions for each region.

| Region | Ball Position and Contact Angle | Shear Force |
| --- | --- | --- |
| 1 | The ball is outside of the conical notch. The contact angle is vertical. | Viscous damping and kinetic friction only. No spring contribution. |
| 2 | The ball is entering notch and is in contact with the notch corner. The contact angle rotates from vertical. | Spring, viscous damping, and kinetic friction contributions. Peaks at transition from region 2 to region 3. |
| 3 | The ball slides along the face of the notch. The contact angle is constant. | Force decreases as spring extends until reaching the spring preload force. |
| 4 | The ball moves from one face to the other. The contact angle switches direction. | Force switches direction. The shear reversal region width controls how smooth this switch is. |

When you set **Parameterization** to `By table
lookup`, you can create an arbitrary function that relates shear
force to relative displacement. If you create such a function, consider these best
practices.

**Energy Conservation**

To ensure that the detent conserves energy, the integral of the force-relative
displacement curve must be zero.

**Simulation Performance**

Avoid discontinuities in the force-relative displacement function. The most
important requirement is to have a shear reversal region of nonzero width,
analogous to region 4 in the geometric parameterization.

### Assumptions and Limitations

- The block does not account for inertia. Add mass externally to the
  **R** and **C** ports.
- When you set **Parameterization** to `By
  peak force and notch width` or `By table
  lookup`, the kinetic friction is independent of the
  detent normal force.
