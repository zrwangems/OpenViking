---
type: simulink-block
title: 'VR Placeholder'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrplaceholder'
documentation_source_path: 'vrplaceholder.html'
language: en
---

# VR Placeholder

## Ports

### Output

### **Output 1** — Output signal real scalar | real vector

Output signal returned as unspecified, that drives the virtual reality
visualization.

**Data Types:** `double`

## Parameters

### **Output width** — Length of vector `1` (default)

Length of the vector containing placeholder signal values.

## Libraries

Simulink 3D Animation

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

### R2023b: To be removed

The `VR Placeholder` will be removed in a future
release. Instead, use `sim3d` classes and Simulation 3D blocks to
interface MATLAB® and Simulink® with the Unreal Engine® 3D simulation environment. To get started, see Create 3D Simulations in Unreal Engine Environment.

## Description

(To be removed) Send unspecified value to Simulink 3D Animation block

The VR Placeholder block sends out a special value that is interpreted as
“unspecified” by the VR Sink block. When this value appears on the VR Sink input,
whether as a single value or as an element of a vector, the appropriate value in the
virtual world stays unchanged. Use this block to change only one value from a larger
vector. For example, use this block to change just one coordinate from a 3-D
position.

The value output by the VR Placeholder block should not be modified before being used
in other VR blocks.

To open the Block Parameters dialog box, double-click the block.
