---
type: simulink-block
title: 'Array of Thermal Nodes Connector'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Simscape Battery'
documentation_release: R2025b
official_category: 'Thermal Management'
documentation_page: 'arrayofthermalnodesconnector'
documentation_source_path: 'ref/arrayofthermalnodesconnector.html'
language: en
---

# Array of Thermal Nodes Connector

## Ports

### Conserving

### **inConnk** — Array of thermal nodes *k* to concatenate thermal array-of-nodes

Array of thermal nodes *k* that you want to
concatenate, where *k* is an integer in the range [1,
**Number of Input Connections**]. The number of
ports of this type is equal to the value to which you set the
**Number of Input Connections** parameter.

### **outConn** — Concatenated array of thermal nodes thermal array-of-nodes

Concatenated array of thermal nodes.

## Parameters

### **Number of Input Connections** — Number of array of thermal nodes to concatenate `one` (default) | `two` | `three` | `four` | ...

Number of array of thermal nodes that you want to concatenate. You can
specify any value between `one` and
`fifty`.

### **Concatenate dimension** — Output dimension along which to concatenate input arrays `2` (default) | positive scalar

*Since R2024b*

Specify the output dimension along which to concatenate the input arrays:

- `1` — Concatenate inputs vertically. The
  vertical array concatenation stacks the input arrays on top of
  each other in the output array.
- `2` — Concatenate inputs horizontally. The
  horizontal array concatenation places the input arrays
  side-by-side in the output array.
- `3` or more — Perform multidimensional
  concatenation on the inputs.

The input arrays must have compatible sizes for concatenation. Vertical
concatenation requires the input arrays to have the same number of columns.
Horizontal concatenation requires input arrays to have the same number of
rows. Multidimensional concatenation requires that all of the dimensions of
the input arrays are the same size except for the dimension they are
concatenated along.

### **Size of complementary dimensions** — Size of dimensions of all input arrays except concatenate dimension `2` (default) | positive scalar

*Since R2024b*

Size of the dimensions of all input arrays, except the concatenate
dimension.

For example, if the block concatenates one array of thermal nodes with a
size of `[3,4,5]` and another array of thermal nodes with a
size of `[3,1,5]` along the second dimension, you must set
this parameter to `[3,5]`, as the second dimension is the
concatenate dimension.

### **Size of concatenate dimension for Node k** — Number of elements in connection node *k* `1` (default)

Number of elements in connection node *k*, where
*k* is an integer in the range [1, **Number of
Input Connections**]. The number of parameters of this type is
equal to the value to which you set the **Number of Input
Connections** parameter.

## Libraries

Simscape / Battery / Thermal

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2025a: To be removed

The Array of Thermal Nodes Connector block will be removed in a future release.
Use the Array
Connection block instead.

### R2024b: Concatenate arrays horizontally or multidimensionally

You can now perform horizontal and multidimensional concatenation of arrays of
thermal nodes.

To concatenate the inputs horizontally, set the **Concatenate
dimension** parameter to `2`. To perform
multidimensional concatenation, set the **Concatenate dimension**
parameter to `3` or more. The concatenation requires the input
arrays to have all their dimensions of the same size except for the dimension they
are concatenated along.

## Description

(To be removed) Concatenate arrays of thermal nodes into single array of thermal nodes port

The Array of Thermal Nodes Connector block concatenates
different arrays of thermal nodes into a single array of thermal nodes. This block acts
as a mux for the Simscape™ thermal domain by concatenating all input array of nodes into a single
array of the specified dimension.

To specify the number of arrays of thermal nodes that you want to concatenate, set the
**Number of Input Connections** parameter. This action enables a
number of ports and parameters equal to the value of the **Number of Input
Connections** parameter. This block supports from one to 50 different
connections from different battery modules with different
`ThermalNodes` properties.

To specify the number of elements in each connection node, set the **Size of
concatenate dimension for Node k** parameter, where *k* is
an integer in the range [1, **Number of Input Connections**].
