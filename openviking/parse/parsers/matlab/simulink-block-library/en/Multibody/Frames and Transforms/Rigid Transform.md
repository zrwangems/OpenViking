---
type: simulink-block
title: 'Rigid Transform'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Frames and Transforms'
documentation_page: 'rigidtransform'
documentation_source_path: 'ref/rigidtransform.html'
language: en
---

# Rigid Transform

## Ports

### Frame

### **B** — Base frame frame

Frame with respect to which you specify the transforms.

### **F** — Follower frame frame

Frame to which you apply the transforms.

## Parameters

### Rotation

### **Method** — Method to specify relative rotation `None` (default) | `Aligned Axes` | `Standard Axis` | `Arbitrary Axis` | `Rotation Sequence` | `Rotation Matrix` | `Quaternion`

Method to use to specify the relative rotation between the base and
follower frames. Set the parameter to `None` to
constrain the base and follower frames to the same orientation.

### **Pair 1: Follower** — Follower frame axis used to align with specified base frame axis `+X` (default) | `-X` | `+Y` | `-Y` | `+Z` | `-Z`

Follower frame axis used to align with the base frame axis set by the
**Pair 1: Base** parameter, specified as an
orthogonal axis of the follower frame. The follower frame rotates with
respect to the base frame to enable the alignment between the selected
axes of the base and follower frames.

#### Dependencies

To enable this parameter, under **Rotation**, set
**Method** parameter to `Aligned
Axis`.

### **Pair 1: Base** — Base frame axis `+Y` (default) | `+X` | `-X` | `-Y` | `+Z` | `-Z`

Base frame axis to align with the follower frame specified by the
**Pair 1: Follower**, specified as an orthogonal
axis of the base frame.

#### Dependencies

To enable this parameter, under **Rotation**, set
**Method** parameter to `Aligned
Axis`.

### **Pair 2: Follower** — Follower frame axis used to align with specified base frame axis `+Y` | `+X` | `-X` | `-Y` | `+Z` | `-Z`

Base frame axis to align with the follower frame specified by the
**Pair 2: Follower**, specified as an orthogonal
axis of the follower frame. The follower frame rotates with respect to
the base frame to enable the alignment between the selected axes of the
base and follower frames.

#### Dependencies

To enable this parameter, under **Rotation**, set
**Method** parameter to `Aligned
Axis`.

### **Pair2: Base** — Base frame axis `+Z` (default) | `+X` | `-X` | `+Y` | `-Y` | `-Z`

Base frame axis used to let the follower frame axis set in the
**Pair2: Follower** parameter to align with,
specified as an orthogonal axis of the base frame. The axis choices for
**Pair 2** depend on the **Pair
1** axis selections.

#### Dependencies

To enable this parameter, under **Rotation**, set
**Method** parameter to `Aligned
Axis`.

### **Axis** — Standard axis of relative rotation `+Z` (default) | `+X` | `-X` | `+Y` | `-Y` | `-Z`

Axis of the relative rotation, specified as an orthogonal axis of the
base frame.

#### Dependencies

To enable this parameter, under **Rotation**, set
**Method** parameter to `Standard
Axis`.

### **Angle** — Angle of relative rotation 0.0 `deg` (default) | scalar

Angle of the relative rotation, specified as a scalar. The angle
indicates the rotation of the follower frame with respect to the base
frame about the specified axis.

#### Dependencies

To enable this parameter, under **Rotation**, set
**Method** parameter to `Standard
Axis`.

### **Axis** — Axis of relative rotation [0 0 1] (default) | 3-by1 vector

Axis of the relative rotation, specified as a 3-by-1 unit vector. The
vector is dimensionless and indicates the rotational axis resolved in
the base frame.

#### Dependencies

To enable this parameter, under **Rotation**, set
**Method** parameter to `Arbitrary
Axis`.

### **Angle** — Angle of relative rotation 0.0 `deg` (default) | scalar

Angle of the relative rotation, specified as a scalar. The angle
indicates the rotation of the follower frame with respect to the base
frame about the axis specified by the **Axis**
parameter.

#### Dependencies

To enable this parameter, under **Rotation**, set
**Method** parameter to `Arbitrary
Axis`.

### **Rotation About** — Frame whose axes to rotate follower frame about `Follower Axes` (default) | `Base Axes`

Frame whose axes to rotate the follower frame about, specified as
`Follower Axes` or `Base
Axes`. If you set the parameter to
`Follower Axes`, the follower frame rotates
about its own axes, and the follower frame changes the orientation with
each successive rotation. If you set the parameter to `Base
Axes`, the follower frame rotates about the fixed base
frame axes. See Rotational Measurements for more information.

#### Dependencies

To enable this parameter, under **Rotation**, set
**Method** parameter to `Rotation
Sequence`.

### **Sequence** — Sequence of rotation axis `X-Y-X` (default) | `X-Y-Z` | `X-Z-X` | `X-Z-Y` | `Y-X-Y` | `Y-X-Z` | `Y-Z-X` | `Y-Z-Y` | `Z-X-Y` | `Z-X-Z` | `Z-Y-X` | `Z-Y-Z`

Sequence of the rotation axis for three successive elementary
rotations. See Rotation Sequence Measurements for
more information.

#### Dependencies

To enable this parameter, under **Rotation**, set
**Method** parameter to `Rotation
Sequence`.

### **Angles** — Angles for elementary rotations [0 0 0] `deg` (default) | 3-by-1 vector

Angles for elementary rotations, specified as a 3-by-1 vector. See
Rotation Sequence Measurements for
more information.

#### Dependencies

To enable this parameter, under **Rotation**, set
**Method** parameter to `Rotation
Sequence`.

### **Matrix** — Rotation matrix [1 0 0; 0 1 0; 0 0 1] (default) | 3-by-3 matrix

Relative rotation, specified as a 3-by-3 matrix. The matrix must be
orthogonal and have determinant 1. See Rotational Measurements for more information.

#### Dependencies

To enable this parameter, under **Rotation**, set
**Method** parameter to `Rotation
Matrix`.

### **Quaternion** — Relative rotation using quaternion [1 0 0 0] (default) | unit quaternion vector

Relative rotation, specified as a vector in quaternion
parameterization. See Rotational Measurements for more information about the
quaternion.

#### Dependencies

To enable this parameter, under **Rotation**, set
**Method** parameter to
`Quaternion`.

### Translation

### **Method** — Method for specifying the translation `None` (default) | `Cartesian` | `Standard Axis` | `Cylindrical`

Method to use to specify the relative translation between the base and
follower frames. The table summarizes the available
options.

| Method | Description |
| --- | --- |
| `None` | Make base and follower frames coincident. This method requires no parameters. |
| `Cartesian` | Specify a 3-D translation in terms of Cartesian coordinates |
| `Standard Axis` | Specify a 1-D translation along the *x*, *y*, or *z* axis |
| `Cylindrical` | Specify a 3-D translation in terms of cylindrical coordinates |

`Cartesian Axis`
:   Specify the **Offset** of the
    follower frame with respect to the base frame. This is
    the 3-D translation vector that brings the base frame
    into coincidence with the follower frame. Select or
    enter a physical unit.

`Standard Axis`
:   Specify the offset of the follower frame with respect
    to the base frame along the base frame
    *x*, *y*, or
    *z* axis. Select or enter a
    physical unit.

    | Parameter | Description |
    | --- | --- |
    | **Axis** | Axis the follower frame translates along |
    | **Offset** | Translation of the follower frame with respect to the base frame along the specified axis |

`Cylindrical`
:   Specify in cylindrical coordinates the translation
    that brings the base frame into coincidence with the
    follower frame. Select or enter a physical unit.

    | Parameter | Description |
    | --- | --- |
    | **Radius** | Distance between the origin of the follower frame and the *z* axis of the base frame. This is the cylindrical radius coordinate. |
    | **Theta** | Rotation angle of the line connecting base and follower frame origins with respect to the base frame *x* axis. This is the cylindrical azimuth coordinate. |
    | **Z Offset** | Distance between base and follower frame origins along the base frame *z* axis. This is the cylindrical length coordinate. |

## Libraries

Simscape / Multibody / Frames and Transforms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012a**

## Description

Fixed spatial relationship between frames

The Rigid Transform block specifies and maintains a
fixed spatial relationship between two frames during simulation. The spatial
relationship can include a translation and a rotation.

The block has various methods to specify the position and orientation of the follower
frame with respect to the base frame. For more information, see Rotation and Translation.
