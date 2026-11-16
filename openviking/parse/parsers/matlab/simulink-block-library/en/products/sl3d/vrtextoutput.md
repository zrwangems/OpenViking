---
type: simulink-block
title: 'VR Text Output'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrtextoutput'
documentation_source_path: 'vrtextoutput.html'
language: en
---

# VR Text Output

## Ports

Not documented in R2025b.

## Parameters

**Associated VRML file** — Virtual world 3D file specifying the
virtual world to which text is output.

**Associated Text node** — Text node within the virtual world to
which text is output.

**Format string** — Format used for output text. This block uses
`sprintf()` to format the output strings. Like
`sprintf()`, it works in a vectorized fashion, where the format
string is recycled through the components of the input vector. This block does not
support the `%c` and `%s` conversion formats, as
signals in the Simulink product cannot have both characters and strings.

**Sample time** — Enter the sample time or `-1` for
inherited sample time.

**Ensure that a viewer window is open during simulation** — Select
this check box to ensure that the Simulink
3D Animation Viewer is open during simulation.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced in R2006b**

### R2023b: To be removed

The `VR Text Output` will be removed in a future
release. Instead, use `sim3d` classes and Simulation 3D blocks to
interface MATLAB® and Simulink with the Unreal Engine® 3D simulation environment. To get started, see Create 3D Simulations in Unreal Engine Environment.

## Description

(To be removed) Allows display of Simulink signal values as text in virtual reality scene

The VR Text Output can display Simulink values of signal as text in a virtual reality scene.

Text rendering is a demanding task for virtual world viewers, so there is generally be
a decrease in rendering speed when outputting text. This effect increases with the
complexity of the text output. You can improve the performance if you limit the output
from the Simulink model to only the values of signals that change (e.g., modeling captions)
or use more static-text nodes.

To open the Block Parameters dialog box, double-click the block.
