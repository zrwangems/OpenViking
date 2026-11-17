---
type: simulink-block
title: 'Array Connection'
family: 'utilities'
product_id: 'utilities'
product_name: 'Utilities'
documentation_release: R2025b
official_category: ''
documentation_page: 'arrayconnection'
documentation_source_path: '../simscape/ref/arrayconnection.html'
language: en
---

# Array Connection

## Ports
```yaml
ports:
- name: elementNodek
  summary: Element connection node *k* to concatenate connection port
  direction: conserving
- name: arrayNode
  summary: Concatenated array of nodes AON port
  direction: conserving
```

### Conserving

### **elementNodek** — Element connection node *k* to concatenate connection port

Connection port of type defined by the **Domain** parameter. This
port represents an element that you want to concatenate, where *k* is
an integer in the range [1, *N*]. The number of ports of this type,
*N*, is equal to the value to which you set the **Number of
elements** parameter (or, for scalar connections, the **Number of
scalar elements** parameter). These ports are all located on the same side
of the block icon and labeled **1**, **2**, and so
on, through *N*.

### **arrayNode** — Concatenated array of nodes AON port

Concatenated AON port of type defined by the **Domain**
parameter, located on the opposite side of the block icon from the element ports. This
port does not have a label.
## Parameters
```yaml
parameters:
- name: Domain
  summary: Specify domain for block connections Electrical Domain (default) | list of Foundation domains and registered custom
    domains | <specify domain path>
  group: ''
- name: Concatenate dimension
  summary: Array dimension along which to concatenate element nodes 2 (default) | positive scalar
  group: ''
- name: Mode
  summary: Specify whether element nodes are scalars or arrays Scalar Elements (default) | Sized Elements
  group: ''
- name: Number of scalar elements
  summary: Number of scalar element nodes to concatenate 2 (default) | positive integer
  group: ''
- name: Number of elements
  summary: Number of nonscalar element nodes to concatenate 2 (default) | positive scalar
  group: ''
- name: Element size k
  summary: Array size in connection node *k* [1,1] (default) | array
  group: ''
```

### **Domain** — Specify domain for block connections `Electrical Domain` (default) | list of Foundation domains and registered custom domains | `<specify domain path>`

Specify the domain for the block connections. You can select from the list of
domains or use the `<specify domain path>` option and type a
custom domain name. The custom domain must be either in the current folder, in a folder
that is on the MATLAB® path, or in a namespace. If the custom domain is in a namespace, include
the full path from the top-level namespace folder. The namespace top-level folder must
reside either in the current folder or in a folder that is on the MATLAB path.

### **Concatenate dimension** — Array dimension along which to concatenate element nodes `2` (default) | positive scalar

Specify the dimension along which to concatenate the element scalars or arrays:

- `1` — Concatenate elements vertically. The vertical array
  concatenation stacks the elements on top of each other in the concatenated array.
- `2` — Concatenate elements horizontally. The horizontal array
  concatenation places the elements side-by-side in the concatenated array.
- `3` or more — Perform multidimensional concatenation on the
  element arrays.

The element arrays must have compatible sizes for concatenation. Vertical
concatenation requires the element arrays to have the same number of columns. Horizontal
concatenation requires element arrays to have the same number of rows. Multidimensional
concatenation requires that all of the dimensions of the element arrays are the same
size except for the dimension they are concatenated along.

### **Mode** — Specify whether element nodes are scalars or arrays `Scalar Elements` (default) | `Sized Elements`

Specify the mode of concatenation:

- `Scalar Elements` — When all the element nodes being
  concatenated are scalars, you can use this simplified mode. In this mode, you
  specify only the number of elements and select whether to concatenate them
  vertically or horizontally. By default, **Concatenate dimension**
  is `2`, which means that the block concatenates the elements
  horizontally. To concatenate them vertically, set the **Concatenate
  dimension** parameter to `1`.
- `Sized Elements` — In this mode, the element nodes
  being concatenated can be either arrays or scalars. You specify the number of
  elements and the size of each element, and the block performs array concatenation
  according to the **Concatenate dimension** parameter value.

### **Number of scalar elements** — Number of scalar element nodes to concatenate `2` (default) | positive integer

Specify the number of scalar element nodes to concatenate. This number defines the
number of element ports on the block icon.

#### Dependencies

To enable this parameter, set the **Mode** parameter to
`Scalar Elements`.

### **Number of elements** — Number of nonscalar element nodes to concatenate `2` (default) | positive scalar

Specify the number of nonscalar element nodes to concatenate. This number defines
the number of element ports on the block icon and the number of **Element size
k** parameters in the block dialog box.

#### Dependencies

To enable this parameter, set the **Mode** parameter to
`Sized Elements`.

### **Element size k** — Array size in connection node *k* `[1,1]` (default) | array

Element size in connection node *k*, where *k* is
an integer in the range [1, **Number of elements**]. The number of
parameters of this type is equal to the value to which you set the **Number of
elements** parameter.

#### Dependencies

To enable this set of parameters, set the **Mode** parameter to
`Sized Elements`.
## Libraries

Simscape / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Concatenate arrays of conserving connections into single array-of-nodes port

The Array Connection block concatenates arrays of
conserving connections into a single array-of-nodes (AON) port. This block acts as a mux for
the Simscape™ conserving connections by concatenating all elements on one side of the block
into a single AON port on the other side.

Physical connection lines are nondirectional, therefore, the block can serve as both a mux
and a demux for conserving connections. For example, you can declutter a model diagram by
bundling multiple connections of the same type and having two Array
Connection blocks, facing each other, with their AON ports connected. You
can also use the Array Connection blocks to connect individual
elements, or subsets of elements, of AON ports of different sizes.
