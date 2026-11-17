---
type: simulink-block
title: 'Second-Order Section Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'secondordersectionfilter'
documentation_source_path: 'ref/secondordersectionfilter.html'
language: en
---

# Second-Order Section Filter

## Ports
```yaml
ports:
- name: In
  summary: Input signal vector | matrix
  direction: input
  data_types: single | double
- name: Num
  summary: Numerator coefficients *P*-by-3 matrix
  direction: input
  data_types: single | double
- name: Den
  summary: Denominator coefficients *P*-by-3 matrix | *P*-by-2 matrix
  direction: input
  data_types: single | double
- name: g
  summary: Scale values for each second-order section scalar | vector
  direction: input
  data_types: single | double
- name: Out
  summary: Filtered output vector | matrix
  direction: output
  data_types: single | double
```

### Input

### **In** — Input signal vector | matrix

Specify the input signal as a vector or a matrix. The input can be a variable-size
signal, that is, the frame size of the signal can change during simulation but the
number of channels cannot.

This port is unnamed until you set the **Coefficient source**
parameter to `Input ports`.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Num** — Numerator coefficients *P*-by-3 matrix

Specify the numerator coefficients of the SOS filter as a
*P*-by-3 matrix, where *P* is the number of filter
sections. For more details on this input port, see
**Numerator**.

During simulation, you cannot change the size of the coefficients matrix but you
can change the coefficient values.

The size and complexity of the **Num** and
**Den** inputs must be the same.

#### Dependencies

To enable this port, set the **Coefficient source** parameter
to `Input ports`.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Den** — Denominator coefficients *P*-by-3 matrix | *P*-by-2 matrix

Specify the denominator coefficients of the SOS filter as a
*P*-by-3 matrix or a *P*-by-2 matrix, where
*P* is the number of filter sections. For more details on this
input port, see **Denominator**.

When you specify a *P*-by-3 matrix, the block always assumes the
leading denominator coefficient to be 1. If you specify any other value in the first
column, the block ignores this value and treats it as 1. If you specify a
*P*-by-2 matrix, the block prepends each row of the matrix with a
value of 1.

During simulation, you cannot change the size of the coefficients matrix but you
can change the coefficient values.

The size and complexity of the **Num** and
**Den** inputs must be the same.

#### Dependencies

To enable this port, set the **Coefficient source** parameter
to `Input ports`.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **g** — Scale values for each second-order section scalar | vector

Specify the scale values that the block applies before and after each section of
the SOS filter as a scalar or a vector with *P* + 1 elements, where
*P* is the number of filter sections.

If you input a scalar, the block applies this gain value before the first filter
section and sets the gain values before all the other sections to
`1`. If you specify a vector of *P* + 1 values, the
block applies each value to a separate section of the filter.

**Tunable:** Yes

#### Dependencies

To enable this port, set **Coefficient source** to
`Input ports` and select the **Specify scale
values** parameter.

**Data Types:** `single` | `double`
### Output

### **Out** — Filtered output vector | matrix

Filtered output, returned as a vector or a matrix. The output has the same size
and data type as the input. The output signal is complex if the input signal,
numerator coefficients, or the denominator coefficients is complex.

This port is unnamed until you set the **Coefficient source**
parameter to `Input ports`.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Filter structure
  summary: Filter structure Direct form II transposed (default) | Direct form I | Direct form I transposed | Direct form II
  group: ''
- name: Coefficient source
  summary: Filter coefficient source Dialog parameters (default) | Input ports
  group: ''
- name: Numerator
  summary: Numerator coefficients of filter [0.0975 0.195 0.0975] (default) | *P*-by-3 matrix
  group: ''
- name: Denominator
  summary: Denominator coefficients of filter [1 -0.9428 0.3333] (default) | *P*-by-3 matrix | *P*-by-2 matrix
  group: ''
- name: Specify scale values
  summary: Specify if filter has scale values for each section off (default) | on
  group: ''
- name: Scale Values
  summary: Scale values for each second-order section [1 1] (default) | scalar | vector
  group: ''
- name: Input processing
  summary: Method to process input Columns as channels (frame based) (default) | Elements as channels (sample based)
  group: ''
- name: View Filter Response
  summary: View filter response button
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Filter structure** — Filter structure `Direct form II transposed` (default) | `Direct form I` | `Direct form I transposed` | `Direct form II`

Specify the filter structure as one of these:

- `Direct form I`
- `Direct form I transposed`
- `Direct form II`
- `Direct form II transposed`

### **Coefficient source** — Filter coefficient source `Dialog parameters` (default) | `Input ports`

Specify the filter coefficient source as one of these:

- `Dialog parameters` –– Set the filter coefficients
  and scale values through the **Numerator**,
  **Denominator**, and **Scale Values**
  parameters in the block dialog box.
- `Input ports` –– Set the filter coefficients and the
  scale values through the **Num**, **Den**, and
  **g** input ports.

### **Numerator** — Numerator coefficients of filter [`0.0975 0.195 0.0975`] (default) | *P*-by-3 matrix

Specify the numerator coefficients **b** of the SOS filter as a
*P*-by-3 matrix, where *P* is the number of filter
sections.

b=[b01b11b21b02b12b22⋮⋮⋮b0Pb1Pb2P]

This equation represents the SOS filter in the transfer function form.

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2a0k+a1kz−1+a2kz−2,

where

- **a** is the denominator coefficients matrix. For more
  details on how to specify this matrix, see
  **Denominator**.
- *k* is the row index.

You cannot change the size of this parameter during simulation, but you can change
its value.

#### Dependencies

To enable this parameter, set **Coefficient source** to
`Dialog parameters`.

**Tunable:** Yes

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Denominator** — Denominator coefficients of filter [`1 -0.9428 0.3333`] (default) | *P*-by-3 matrix | *P*-by-2 matrix

Specify the denominator coefficients **a** of the SOS filter as a
*P*-by-3 matrix or a *P*-by-2 matrix, where
*P* is the number of filter sections.

a=[a01a11a21a02a12a22⋮⋮⋮a0Pa1Pa2P]

The block algorithm assumes that the value of the leading coefficients is always 1.
If the denominator is of size *P*-by-2, the block algorithm prepends a
column of 1s to the denominator to change its size to *P*-by-3. If the
denominator is of size *P*-by-3 and the elements in the first column do
not equal 1, the algorithm ignores the values in the first column and sets them to
1.

This equation represents the SOS filter in the transfer function form.

H(z)=∏k=1PHk(z)=∏k=1Pb0k+b1kz−1+b2kz−2a0k+a1kz−1+a2kz−2,

where

- **b** is the numerator coefficients matrix. For more details
  on how to specify this matrix, see **Numerator**.
- *k* is the row index.

You cannot change the size of this parameter during simulation, but you can change
its value.

#### Dependencies

To enable this parameter, set **Coefficient source** to
`Dialog parameters`.

**Tunable:** Yes

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **Specify scale values** — Specify if filter has scale values for each section `off` (default) | `on`

Specify if the filter has scale values for each section. When you select this
parameter, you can specify the scale values using the **Scale Values**
parameter in the block dialog box or through the **g** input
port.

### **Scale Values** — Scale values for each second-order section [`1 1`] (default) | scalar | vector

Specify the scale values that the block applies before and after each section of the
SOS filter as a scalar or a vector with *P* + 1 elements, where
*P* is the number of filter sections.

If you set this property to a scalar, the block applies this gain value before the
first filter section and sets the gain values before all the other sections to
`1`. If you set this property to a vector of *P* + 1
values, the block applies each value to a separate section of the filter.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Coefficient source** to
`Dialog parameters` and select the **Specify scale
values** parameter.

**Data Types:** `single` | `double`

### **Input processing** — Method to process input `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify the input processing method as one of these:

- `Columns as channels (frame based)` –– The block treats
  each column of the input as a separate channel.

  For more information, see What Is Frame-Based Processing?
- `Elements as channels (sample based)` –– The block
  treats each element of the input as a separate channel.

  For more information, see What Is Sample-Based Processing?

### **View Filter Response** — View filter response button

Open the Filter Visualization tool and display the magnitude response of the SOS
filter. The response is based on the parameters you select in the block dialog box. To
update the magnitude response, modify the parameters in the dialog box and click
**Apply**.
## Libraries

DSP System Toolbox / Filtering / Filter Implementations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

**Symbolic Dimension Support**

This block supports setting symbolic dimensions for simulation and for code
generation. You can specify the dimension information in the block as symbols (variables).
These symbols propagate throughout the model during simulation and then go into the
generated code. That way, you do not need to change the dimensions in the block each time
you update this information.

- The ports that support symbolic dimensions are these:

  - `Num` — The dimensions must be `[P
    3]`, where `P` is the number of sections.
  - `Den` — The dimensions must be `[P
    M]`, where `M` can be `2` or
    `3`.
  - `g` — The dimension must be `P+1`,
    where `P` is the number of sections.
- The block supports symbolic dimensions only in the normal simulation
  mode.

You must have Simulink
Coder™ and Embedded Coder® to use this functionality.

For more information, see Implement Symbolic Dimensions for Array Sizes in Generated Code (Embedded Coder).

## Version History

**Introduced in R2023b**

### R2025a: Use symbolic dimensions for simulation and code generation

The Second-Order Section Filter block supports setting symbolic dimensions for simulation
and code generation.

## Description

Implement cascade of second-order section filters

The Second-Order Section Filter block implements a cascade of second-order
section (SOS) filters in Simulink®. You can specify the numerator and denominator coefficients of the filter in the
block parameters dialog box or through input ports.
