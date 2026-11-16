---
type: simulink-block
title: 'Road Track Friction'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'roadtrackfriction'
documentation_source_path: 'ref/roadtrackfriction.html'
language: en
---

# Road Track Friction

## Ports

### Input

### **XWhl** — Wheel displacement along X-axis 4-by-1 array

Wheel displacement along the earth-fixed X-axis, specified as a 4-by-1
array.

### **YWhl** — Wheel displacement along Y-axis 4-by-1 array

Wheel displacement along the earth-fixed Y-axis, specified as a 4-by-1
array.

### **Cg** — Vehicle CG 3-by-1 array

Vehicle cg, along earth-fixed axis, specified as a 3-by-1 array.
### Output

### **FricCoeffLambda** — Friction coefficient applied to wheels 4-by-1 array

Wheel friction coefficient, specified as a 4-by-1 array.

## Parameters

### **Type of surface** — Friction `Split friction coefficient scaling factor` (default) | `Constant friction coefficient scaling factor`

- `Constant friction coefficient scaling factor` —
  Constant surface friction during the maneuver
- `Split friction coefficient scaling factor` — Two
  friction coefficients

  Select this option to specify the friction scaling coefficients for a split-mu
  braking test. Use the enabled parameters to set the ground friction and rectangular
  surface friction coefficient scaling factors.

### **Scaling factor for the friction coefficient of ground, lambda\_g** — Scaling factor `.6` (default) | `scalar`

Scaling factor for the ground friction coefficient.

### **Scaling factor for the friction coefficient of rectangular surface, lambda\_r** — Scaling factor `.8` (default) | `scalar`

Scaling factor for the friction coefficient of the rectangular surface.

#### Dependencies

To enable this parameter, set **Type of surface/track** to
`Split friction coefficient scaling factor`.

### **X coordinate of lower left corner of rectangular surface, r\_x0** — X coordinate `175` (default) | `scalar`

X coordinate of lower left corner of rectangular surface, in earth-fixed coordinate
system, in m.

#### Dependencies

To enable this parameter, set **Type of surface/track** to
`Split friction coefficient scaling factor`.

### **Y coordinate of lower left corner of rectangular surface, r\_y0** — X coordinate `-100` (default) | `scalar`

Y coordinate of lower left corner of rectangular surface, in earth-fixed coordinate
system.

#### Dependencies

To enable this parameter, set **Type of surface/track** to
`Split friction coefficient scaling factor`.

### **Rectangular surface width in X direction, r\_xw** — Rectangular surface `1000` (default) | `scalar`

Rectangular surface width in X direction, in m.

#### Dependencies

To enable this parameter, set **Type of surface/track** to
`Split friction coefficient scaling factor`.

### **Rectangular surface width in Y direction, r\_yw** — Rectangular surface `500` (default) | `scalar`

Rectangular surface width in Y direction, in m.

#### Dependencies

To enable this parameter, set **Type of surface/track** to
`Split friction coefficient scaling factor`.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Configure road for braking test

The Road Track Friction block implements the road, including friction, for
the Braking Test. Use the **Type
of surface** parameter to specify the friction coefficient scaling factor:

- `Constant friction coefficient scaling factor` — Constant
  surface friction during the maneuver
- `Split friction coefficient scaling factor` — Two friction
  coefficients

  Select this option to specify the friction scaling coefficients for a split-mu
  braking test. Use the enabled parameters to set the ground friction and rectangular
  surface friction coefficient scaling factors.
