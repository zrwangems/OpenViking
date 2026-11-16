---
type: simulink-block
title: 'File Solid'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements'
documentation_page: 'filesolid'
documentation_source_path: 'ref/filesolid.html'
language: en
---

# File Solid

## Ports

### Frame

### **R** — Local reference frame frame

Local reference frame of the imported solid. This frame is fixed with
respect to the solid. Connect this frame to another block to specify the
location and orientation of the solid.
### Geometry

### **CH** — Convex hull representation geometry

Convex hull that represents the geometry of the solid. Connect this port to a Spatial Contact Force block to model contacts on the convex hull.

#### Dependencies

To enable this port, under **Geometry**, expand **Export**
and select **Convex Hull**.

## Parameters

### Geometry

### **File Name** — CAD file name or path to CAD file character vector

CAD file name or path to CAD file, specified as a character vector. If the file name
or path does not include a file extension, the block assumes the file type is STEP. The
block supports various formats of CAD files. For a list of supported CAD file formats,
see Supported Software and File Formats.

Depending on the location of the CAD file, use one of these methods to specify
**File Name**.

| **Location** | Methods |
| --- | --- |
| File is in the current working folder or on the MATLAB® path | Enter the file name in the text box.  **Example:** `myShape.STEP` |
| File is in a folder that is neither the current folder nor on the MATLAB path | - Enter the relative path of the CAD file, which is the path   relative to the current folder.  **Example:**   `Geometries/myShape.STEP, or   ../Geometries/myShape.STEP` - Click the Browsing for CAD file    button and browse to the CAD file. - Enter the full path of the CAD file.  **Example:**   `C:/Users/Model/Geometries/myShape.STEP` |

**Tip**

- When using the block across multiple platforms or sharing the model with
  others, consider using either the file name or relative path.
- A forward slash (/) is a valid separator on any platform. A backward slash
  (\) is valid only on Microsoft Windows platforms.

### **Unit Type** — Source for solid geometry units `From File` (default) | `Custom`

Source of the solid geometry units. Select `From
File` to use the units specified in the imported file.
Select `Custom` to specify your own
units.

### **Unit** — Length units in which geometry coordinates are specified in the imported file `m` (default) | `cm` | `mm` | `km` | `in` | `ft`

Length units in which to interpret the geometry defined in a geometry
file. Changing the units changes the scale of the imported
geometry.

### **Convex Hull** — Generate a convex hull representation of the true geometry `off` (default) | `on`

Select **Convex Hull** to generate a convex
hull representation of the true geometry. Select this parameter enables
the port **CH**.

### Inertia

### **Type** — Inertia parameterization to use `Calculate from Geometry` (default) | `Point Mass` | `Custom`

Inertia parameterization to use. Select `Point
Mass` to model a concentrated mass with negligible
rotational inertia. Select `Custom` to model a
distributed mass with the specified moments and products of inertia. The
default setting, `Calculate from Geometry`,
enables the block to automatically calculate the rotational inertia
properties from the solid geometry and either density or mass.

### **Based on** — Parameter to use in inertia calculation `Density from File` (default) | `Custom Density` | `Custom Mass`

Parameter to use in inertia calculation. The block calculates the
inertia tensor from the solid geometry and the parameter
selected.

- `Density from File`: The block
  calculates the inertia of the body based on the density
  obtained from the CAD file. Note that only some CAD formats
  contain density data.
- `Custom Density`: The block
  calculates the inertia of the body based on the density
  specified in the dialog box.
- `Custom Mass`: The block
  calculates the inertia of the body based on the mass
  specified in the dialog box.

### **Density** — Mass per unit volume of material `1000 kg/m^3` (default)

Mass per unit volume of material. The mass density can take on a
positive or negative value. Specify a negative mass density to model the
effects of a void or cavity in a solid body.

#### Dependencies

To enable this parameter, set:

1. **Type** to `Calculate from
   Geometry`
2. **Based on** to `Custom
   Density`

### **Mass** — Total mass of the solid element `1 kg` (default) | scalar with units of mass

Total mass to attribute to the solid element. This parameter can be positive or
negative. Use a negative value to capture the effect of a void or cavity in a compound
body (one comprising multiple solids and inertias), being careful to ensure that the
mass of the body is on the whole positive.

### **Center of Mass** — Center-of-mass coordinates `[0 0 0] m` (default) | three-element vector with units of length

[*x*
*y*
*z*] coordinates of the center of mass relative to the
block reference frame.

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Moments of Inertia** — Diagonal elements of inertia tensor `[1 1 1] kg*m^2` (default) | three-element vector with units of mass\*length^2

Three-element vector with the
[*Ixx*
*Iyy*
*Izz*] moments of inertia
specified relative to a frame with origin at the center of mass and axes
parallel to the block reference frame. The moments of inertia are the
diagonal elements of the inertia tensor

(IxxIyyIzz),

where:

- Ixx=∫m(y2+z2) dm
- Iyy=∫m(x2+z2) dm
- Izz=∫m(x2+y2) dm

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Products of Inertia** — Off-diagonal elements of inertia tensor `[0 0 0] kg*m^2` (default) | three-element vector with units of mass\*length^2

Three-element vector with the
[*Iyz*
*Izx*
*Ixy*] products of inertia
specified relative to a frame with origin at the center of mass and axes
parallel to the block reference frame. The products of inertia are the
off-diagonal elements of the inertia tensor

(IxyIzxIxyIyzIzxIyz),

where:

- Iyz=−∫myz dm
- Izx=−∫mzx dm
- Ixy=−∫mxy dm

#### Dependencies

To enable this parameter, set **Type** to
`Custom`.

### **Derived Values** — Display of calculated values of inertia properties button

Display of the calculated values of the solid inertia properties—mass,
center of mass, moments of inertia, and products of inertia. Click the
**Update** button to calculate and display the
properties of the solid. Click this button following any changes to the
block parameters to ensure that the displayed values are still
current.

The center of mass is resolved in the local reference frame of the
solid. The moments and products of inertia are each resolved in the
inertia frame of resolution—a frame whose axes are parallel to those of
the reference frame but whose origin coincides with the solid center of
mass.

#### Dependencies

To enable this parameter, set **Type** to
`Calculate from Geometry`.

### Graphic

### **Type** — Graphic to use for visualization `From Geometry` (default) | `Marker` | `None`

Type of the visual representation of the solid, specified as `From Geometry`, `Marker`, or `None`. Set the parameter to `From Geometry` to show the visual representation of the solid. Set the parameter to `Marker` to represent the solid as a marker. Set the parameter to `None` to hide the solid in the model visualization.

### **Visual Properties** — Parameterizations for color and opacity `Simple` (default) | `Advanced`

Parameterizations for specifying visual properties. Select
`Simple` to specify **Diffuse
Color** and **Opacity**. Select
`Advanced` to specify more visual
properties, such as **Specular Color**, **Ambient
Color**, **Emissive Color**, and
**Shininess**.

#### Dependencies

To enable this parameter, set **Type** to `From
Geometry` or
`Marker`.

### **Shape** — Shape of marker to represent to the solid `Sphere` (default) | `Cube` | `Frame`

Shape of the marker by means of which to visualize the solid. The motion of the marker reflects the motion of the solid itself.

#### Dependencies

To enable this parameter, set **Type** to `Marker`.

### **Size** — Width of the marker in pixels 10 `pixels` (default) | scalar

Width of the marker in pixels. This width does not scale with zoom level. Note that the apparent size of the marker depends partly on screen resolution, with higher resolutions packing more pixels per unit length, and therefore producing smaller icons.

#### Dependencies

To enable this parameter, set **Type** to `Marker`.

### **Color** — Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the graphic under direct white light, specified as an [R G B] or [R G B A]
vector on a 0–1 scale. An optional fourth element (A) specifies the color opacity on a
scale of 0–1. Omitting the opacity element is equivalent to specifying a value of
1.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry` or
   `Marker`
2. **Visual Properties** to
   `Simple`

### **Opacity** — Graphic opacity 1.0 (default) | scalar in the range of 0 to 1

Graphic opacity, specified as a scalar in the range of 0 to 1. A scalar of 0
corresponds to completely transparent, and a scalar of 1 corresponds to completely
opaque.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry` or
   `Marker`
2. **Visual Properties** to
   `Simple`

### **Diffuse Color** — Color of light due to diffuse reflection [0.5 0.5 0.5] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to diffuse reflection, specified as an [R,G,B] or [R,G,B,A]
vector with values in the range of 0 to 1. The vector can be a row or column vector. The
optional fourth element specifies the color opacity. Omitting the opacity element is
equivalent to specifying a value of 1.

The diffuse color reflects the main color of the rendered solid and provides shading
that gives the rendered object a three-dimensional appearance.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry` or
   `Marker`
2. **Visual Properties** to
   `Advanced`

### **Specular Color** — Color of light due to specular reflection [0.5 0.5 0.5 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the light due to specular reflection, specified as an [R,G,B] or [R,G,B,A]
vector with values in the range of 0 to 1. The vector can be a row or column vector. The
optional fourth element specifies the color opacity. Omitting the opacity element is
equivalent to specifying a value of 1. This parameter changes the color of the specular
highlight, which is the bright spot on the rendered solid due to the reflection of the
light from the light source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry` or
   `Marker`
2. **Visual Properties** to
   `Advanced`

### **Ambient Color** — Color of ambient light [0.15 0.15 0.15 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

Color of the ambient light, specified as an [R,G,B] or [R,G,B,A] vector with values in
the range of 0 to 1. The vector can be a row or column vector. The optional fourth
element specifies the color opacity. Omitting the opacity element is equivalent to
specifying a value of 1.

Ambient light refers to a general level of illumination that does not come directly
from a light source. The Ambient light consists of light that has been reflected and
re-reflected so many times that it is no longer coming from any particular direction.
You can adjust this parameter to change the shadow color of the rendered solid.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry` or
   `Marker`
2. **Visual Properties** to
   `Advanced`

### **Emissive Color** — Self-illumination color [0.0 0.0 0.0 1.0] (default) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1

Color due to self illumination, specified as an [R,G,B] or [R,G,B,A] vector in the
range of 0 to 1. The vector can be a row or column vector. The optional fourth element
specifies the color opacity. Omitting the opacity element is equivalent to specifying a
value of 1.

The emission color is color that does not come from any external
source, and therefore seems to be emitted by the solid itself. When
a solid has an emissive color, the solid can be seen even if there
is no external light source.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry` or
   `Marker`
2. **Visual Properties** to
   `Advanced`

### **Shininess** — Highlight sharpness 75 (default) | scalar with value constrained to 0–128

Sharpness of specular light reflections, specified as a scalar number on a 0–128
scale. Increase the shininess value for smaller but sharper highlights. Decrease the
value for larger but smoother highlights.

#### Dependencies

To enable this parameter, set:

1. **Type** to `From Geometry` or
   `Marker`
2. **Visual Properties** to
   `Advanced`

### Frames

### **Show Port R** — Show reference frame port for connection to other blocks on (default) | off

Select to expose the **R** port.

### **New Frame** — Create custom frame for connection to other blocks button

Click the Create button Create to open a pane for creating a new
body-attached frame. In this pane, you can specify the name, origin, and
orientation for the frame.

- To name the custom frame, click the text field of the
  **Frame Name** parameter. The name
  identifies the corresponding port on the solid block and in
  the **Model Tree** pane of the
  Multibody Explorer.
- To select the **Frame Origin** of the
  custom frame, use one of the following methods:

  - **At Reference Frame
    Origin**: Make the new frame origin
    coincident with the origin of the reference frame
    of the solid.
  - **At Center of Mass**: Make
    the new frame origin coincident with the center of
    mass of the solid.
  - **Based on Geometric
    Feature**: Make the new frame origin
    coincident with the center of the selected
    feature. Valid features include surfaces, lines,
    and points. Select a feature from the
    visualization pane, then click **Use
    Selected Feature** to confirm the
    location of the origin. The name of the origin
    location appears in the field below this
    option.
- To define the orientation of the custom frame, under the
  **Frame Axes** section, select the
  **Primary Axis** and
  **Secondary Axis** of the custom frame
  and then specify their directions.

  Use the following methods to select a vector for
  specifying the directions of the primary and secondary axes.
  The primary axis is parallel to the selected vector and
  constrains the remaining two axes to its normal plane. The
  secondary axis is parallel to the projection of the selected
  vector onto the normal plane.

  - **Along Reference Frame
    Axis**: Selects an axis of the reference
    frame of the solid.
  - **Along Principal Inertia
    Axis**: Selects an axis of the principal
    inertia axis of the solid.
  - **Based on Geometric
    Feature**: Selects the vector associated
    with the chosen geometry feature of the solid.
    Valid features include surfaces and lines. The
    corresponding vector is indicated by a white arrow
    in the visualization pane. You can select a
    feature from the visualization pane and then click
    **Use Selected Feature** to
    confirm the selection. The name of the selected
    feature appears in the field below this
    option.

### **FrameN** — Edit or delete existing custom frame frame name

Frames that you have created. `N` is a unique
identifying number for each custom frame.

- Click the text field to edit the name of an existing
  custom frame.

- Click the Edit button Edit to edit other aspects of
  the custom frame, such as origin and axes.
- Click the Delete button Delete to delete the custom
  frame.

#### Dependencies

To enable this parameter, create a frame by clicking **New
Frame**.

## Libraries

Simscape / Multibody / Body Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

### R2023b: Import assemblies

You can now import assemblies to the File Solid
block from various CAD formats. The File Solid block
represents the imported assembly as a single rigid body using the default pose in
the CAD file. The block ignores all the constraints and assumes that the whole
geometry has one density. The block can obtain the density from the CAD file if the
densities of all the parts are the same. If the assembly file does not have a
density or has multiple densities, you must explicitly specify the inertia
properties for the assembly.

## Description

Solid with properties derived from CAD file

The File Solid block models a solid with geometry,
inertia, color, and reference frame derived from a CAD file. You can manually specify
the inertia and color for the imported solid. The File
Solid block can model a solid by using various CAD formats.

### Supported Software and File Formats

| CAD | Release Supported |
| --- | --- |
| ACIS | Up to 2020 |
| Autodesk® Inventor | Up to 2022 |
| CATIA V4 | Up to 4.2.5 |
| CATIA V5 | Up to V5-6 R2021 |
| CATIA V6 | Up to V5-6 R2019(R29) |
| Creo-Pro/E | Pro/Engineer 19.0 to Creo 8.0 |
| IGES | 5.1, 5.2, and 5.3 |
| JT | Up to v10.5 |
| NX | V11.0 to NX 18.0, NX to NX12, NX 1847 Series to NX 1980 Series |
| OBJ | All Versions |
| Parasolid | Up to v33 |
| PRC | All Versions |
| Rhino3D | 4 to 7 |
| Solid Edge | V19 - 20, ST - ST10, 2021 |
| SolidWorks® | 97 to 2021 |
| STEP | AP 203 E1/E2, AP 214, and AP 242 |
| STL | All Versions |
| U3D | ECMA-363 |

**Note**

The block cannot read CAD drawings because they do not contain the necessary
data for a solid.

### Import Parts

The File Solid block represents the imported part
as a rigid body. The block can read the inertia and color data from the CAD file.
Alternatively, you can explicitly specify these properties for the imported parts.
For more information, see Inertia and Graphic.

The File Solid block uses the inertia frame, whose
origin is coincident with the center of mass and axes are parallel to the axes of
the reference frame, to compute the inertia of the imported solid. The frame in
which the moments and products of inertia are computed varies among CAD software.
For more information about how to specify the inertia, see Specifying Custom Inertias.

**Calculate Inertia**

If the block computes the inertia according to the geometry of the imported
body, you can see the computed values in the block dialog box. Expand the
**Derived Values** node under **Inertia**
and click **Update**. If the geometry, density, or mass
changes, click the **Update** button to compute the inertia
again. All the computed values are in SI units.

**Frames**

The imported bodies connect through frames. By default, the imported body has
a reference frame represented by port **R**. The CAD file
specifies the location of the reference frame.

If you need to have the connection on a different part of the body or if you
need to have multiple connections on the body, you can create additional frames
on the body. Each frame adds a new frame port to the block. For more information
about creating custom frames, see Frames.

### Import Assemblies

The File Solid block represents the imported
assembly as a single rigid body using the default pose specified in the CAD file.
The block ignores all the constraints in the CAD file and assumes that the whole
assembly has one density.

The File Solid block can read density data from the
CAD file if you, under **Inertia**, specify
**Type** as `Calculate From Geometry`
and **Based On** as `Density`. To ensure
that the block successfully reads the density, the CAD file must have a density for
the whole assembly and the densities of all the parts must either have the same
value or be unspecified. Otherwise, the simulation returns an error.

You can manually specify the density, mass, or inertia properties of the imported
assembly. The process is the same as the process for a single part. For more
information, see Specifying Custom Inertias.

You can import an assembly that has parts represented by different modeling
methods, such as faceted, polygonal, and BRep models. However, you can create frames
only on parts represented by BRep models because they have the necessary boundary
primitives, such as points, edges, and faces.

### Export Geometry

The File Solid block can generate a convex hull geometry
representation of an imported CAD file in the Simscape Multibody environment. You
can use the exported geometry for spatial contacts.

As shown in the figure, the convex hull geometry is an approximation of the true
geometry. The block calculates the physical properties, such as mass and inertia,
based on its true geometry.

Illustration of the true geometry and the corresponding convex hull of a body
