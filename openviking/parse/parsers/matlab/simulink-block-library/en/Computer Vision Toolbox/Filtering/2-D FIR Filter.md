---
type: simulink-block
title: '2-D FIR Filter'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: '2dfirfilter'
documentation_source_path: 'ref/2dfirfilter.html'
language: en
---

# 2-D FIR Filter

## Ports
```yaml
ports:
- name: I
  summary: Input image matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: H
  summary: Filter coefficients matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: HV
  summary: Vertical filter coefficients vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: HH
  summary: Horizontal filter coefficients vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: PVal
  summary: Pad value scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Output
  summary: Filtered output image matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **I** — Input image matrix

Input image, specified as a numeric matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **H** — Filter coefficients matrix

Filter coefficients, specified as a numeric matrix. The input to the
**H** port must have the same data type as the input to the
**I** port.

#### Dependencies

To enable this port, set the **Coefficient source** parameter
to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **HV** — Vertical filter coefficients vector

Vertical filter coefficients, specified as a numeric vector. The input to the
**HV** port must have the same data type as the input to the
**I** port.

#### Dependencies

To enable this port, specify these parameter values.

- **Separable filter coefficients** —
  `on`
- **Coefficient source** — `Input
  port`

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **HH** — Horizontal filter coefficients vector

Horizontal filter coefficients, specified as a numeric vector. The input to the
**HH** port must have the same data type as the input to the
**I** port.

#### Dependencies

To enable this port, specify these parameter values.

- **Separable filter coefficients** —
  `on`
- **Coefficient source** — `Input
  port`

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes

### **PVal** — Pad value scalar

Pad value, specified as a numeric scalar. The input to the
**PVal** port must have the same data type as the input to the
**I** port.

#### Dependencies

To enable this port, specify these parameter values.

- **Output size** — `Full` or
  `Same as input port I`
- **Padding options** —
  `Constant`
- **Pad value source** — `Input
  port`

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Output** — Filtered output image matrix

Filtered output image, returned as a numeric matrix of the same data type as the
input image.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Separable filter coefficients
  summary: Filter coefficients are separable off (default) | on
  group: Main
- name: Coefficient source
  summary: Source of filter coefficients Specify via dialog (default) | Input port
  group: Main
- name: Coefficients
  summary: Filter coefficients [1 0; 0 -1] (default) | numeric matrix
  group: Main
- name: Vertical coefficients (across height)
  summary: Vertical filter coefficients [4 0] (default) | numeric vector
  group: Main
- name: Horizontal coefficients (across height)
  summary: Horizontal filter coefficients [4 0] (default) | numeric vector
  group: Main
- name: Output size
  summary: Size of filtered image Full (default) | Same as input port I | Valid
  group: Main
- name: Padding options
  summary: Padding method Constant (default) | Replicate | Symmetric | Circular
  group: Main
- name: Pad value source
  summary: Source of padding value Specify via dialog (default) | Input port
  group: Main
- name: Pad value
  summary: Padding value 0 (default) | numeric scalar
  group: Main
- name: Filtering based on
  summary: Method of filtering Convolution (default) | Correlation
  group: Main
- name: Lock data type settings against change by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types
```

### Main

### **Separable filter coefficients** — Filter coefficients are separable `off` (default) | `on`

Select this parameter if your filter coefficients are separable. Using separable
filter coefficients reduces the number of calculations the block must perform to
compute the output. You can use `isfilterseparable` to check if your filter is separable and compute the
vertical and horizontal filter coefficients.

### **Coefficient source** — Source of filter coefficients `Specify via dialog` (default) | `Input port`

Specify the source of the filter coefficients as one of these options.

- `Specify via dialog` — Specify the filter
  coefficients using the **Coefficients** parameter or, if you
  select the **Separable filter coefficients** parameter, by using
  the **Vertical coefficients (across height)** and
  **Horizontal coefficients (across width)** parameters.
- `Input port` — Specify the filter coefficients using
  the **H** port, or if you select the **Separable filter
  coefficients** parameter, by using the **HV** and
  **HH** ports.

### **Coefficients** — Filter coefficients `[1 0; 0 -1]` (default) | numeric matrix

Specify the filter coefficients as a numeric matrix.

#### Dependencies

To enable this parameter, specify these parameter values.

- **Separable filter coefficients** —
  `off`
- **Coefficient source** — `Specify via
  dialog`

### **Vertical coefficients (across height)** — Vertical filter coefficients `[4 0]` (default) | numeric vector

Specify the vertical filter coefficients as a numeric vector.

#### Dependencies

To enable this parameter, specify these parameter values.

- **Separable filter coefficients** —
  `on`
- **Coefficient source** — `Specify via
  dialog`

### **Horizontal coefficients (across height)** — Horizontal filter coefficients `[4 0]` (default) | numeric vector

Specify the horizontal filter coefficients as a numeric vector.

#### Dependencies

To enable this parameter, specify these parameter values.

- **Separable filter coefficients** —
  `on`
- **Coefficient source** — `Specify via
  dialog`

### **Output size** — Size of filtered image `Full` (default) | `Same as input port I` | `Valid`

For an input image having dimensions *M*-by-*N*
and a filter having dimensions *P*-by-*Q*, specify
the size of the filtered image as one of these options.

- `Full` — The block uses padding to return a filtered
  image with full dimensions
  *(M+P–1)*-by-*(N+Q–1)*.
- `Same as input port I` — The block uses padding to
  return a filtered image with dimensions
  *M*-by-*N*, the same size as the input
  image.
- `Valid` — The block filters the input image only
  where the coefficient matrix fits entirely within it without padding, and returns
  a filtered image with dimensions
  *(M–P+1)*-by-*(N–Q+1)*.

### **Padding options** — Padding method `Constant` (default) | `Replicate` | `Symmetric` | `Circular`

Specify the padding method as one of these options.

- `Constant` — Pads the input image with a constant
  value.
- `Replicate` — Pads the input image by repeating its
  border values.
- `Symmetric` — Pads the input image by
  mirror-reflecting the image across its border.
- `Circular` — Pads the input image by assuming the
  image is periodic.

#### Dependencies

To enable this parameter, specify the **Output size** parameter
as either `Full` or `Same as input port
I`.

### **Pad value source** — Source of padding value `Specify via dialog` (default) | `Input port`

Specify the source of the padding value as one of these options.

- `Specify via dialog` — Specify the pad value using
  the **Pad value** parameter.
- `Input port` — Specify the pad value using the
  **PVal** port.

#### Dependencies

To enable this parameter, specify these parameter values.

- **Output size** — `Full` or
  `Same as input port I`
- **Padding options** —
  `Constant`

### **Pad value** — Padding value `0` (default) | numeric scalar

Specify the padding value as a numeric scalar.

#### Dependencies

To enable this parameter, specify these parameter values.

- **Output size** — `Full` or
  `Same as input port I`
- **Padding options** —
  `Constant`
- **Pad value source** — `Specify via
  dialog`

### **Filtering based on** — Method of filtering `Convolution` (default) | `Correlation`

Specify the method of filtering as `Convolution` or
`Correlation`.

### Data Types

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).

### **Lock data type settings against change by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data
types you specify in this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).
## Libraries

Computer Vision Toolbox / Filtering

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

2-D FIR filter on input matrix

The 2-D FIR Filter block filters a 2-D grayscale image using a 2-D finite impulse response
(FIR) filter represented as a 2-D coefficient matrix or a pair of separable filter coefficient
vectors.
