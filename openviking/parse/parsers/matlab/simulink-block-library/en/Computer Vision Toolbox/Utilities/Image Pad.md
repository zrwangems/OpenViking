---
type: simulink-block
title: 'Image Pad'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'imagepad'
documentation_source_path: 'ref/imagepad.html'
language: en
---

# Image Pad

## Ports

### Input

### **I** — Input image matrix | array

Input image, specified as an *M*-by-*N* matrix
or an *M*-by-*N*-by-*P* array,
where *P* is the number of color planes in the input image.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **PVal** — Pad value scalar

Pad value, specified as a scalar. The block uses this value for each element of
the rows or columns added to the input image.

#### Dependencies

To enable this port, set the **Method** parameter to
`Constant` and the **Pad value source**
parameter to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Port\_1** — Output image matrix | array

Output image, returned as a padded matrix or an array. The dimensions of the
output image are specified by the **Specify** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## Parameters

### **Method** — Padding method `Constant` (default) | `Replicate` | `Symmetric` | `Circular`

Pad the image using one of these methods:

- `Constant` — Pad the image with a constant value. See
  Pad with Constant Value.
- `Replicate` — Pad the image by repeating the border
  values of the input image. See Pad by Repeating Border Values.
- `Symmetric` — Pad the image using a mirror image of
  the input data. See Pad with Mirror Image.
- `Circular` — Pad the image using a circular
  repetition of the elements in the input image. See Pad Using Circular Repetition of Elements.

### **Pad value source** — Source of constant pad value `Specify via dialog` (default) | `Input port`

Specify the padding source as `Specify via dialog` or
`Input port`.

- `Specify via dialog` — Specify a pad value using the
  **Pad Value** parameter.
- `Input port` — Specify a pad value using the
  **PVal** input port.

#### Dependencies

To enable this parameter, set the **Method** parameter to
`Constant`.

### **Pad value** — Pad value `0` (default) | scalar

Specify a scalar value with which to pad the image.

#### Dependencies

To enable this parameter, set the **Method** parameter to
`Constant` and the **Pad value source**
parameter to `Specify via dialog`.

### **Specify** — Padding size specification format `Pad size` (default) | `Output size`

Select how to specify the size of the image padding from these two options:

- `Pad size` — Specify the number of columns and rows
  with which to pad the image, using the **Number of added
  columns** and **Number of added rows** parameters,
  respectively.
- `Output size` — Specify the size of the padded output
  image using a combination of the **Output row mode**,
  **Number of output rows**, **Output column
  mode**, and **Number of output columns**
  parameters.

### **Add columns to** — Column padding location `Left` (default) | `Right` | `Both left and right` | `No padding`

Select which sides of the input image to pad with additional columns:

- `Left` — Add columns to the left side of the input
  image.
- `Right` — Add columns to the right side of the input
  image.
- `Both left and right` — Add columns to both the left
  and right sides of the input image.
- `No padding` — Do not add columns to the input
  image.

### **Output column mode** — Output column sizing method `User-specified` (default) | `Next power of two`

Specify the number of columns in the output image using one of these options:

- `User-specified` — Specify the number of columns in
  the output image using the **Number of output columns**
  parameter.
- `Next power of two` — Add columns to the input image
  until the total number of columns is a power of two.

#### Dependencies

To enable this parameter, set the **Specify** parameter to
`Output size`.

### **Number of output columns** — Number of columns in output image `10` (default) | positive integer

Specify the number of columns in the output image as a positive integer
*M*. If the value of this parameter is less than the number of
columns in the input image, then the output image contains only the last
*M* columns of the input image.

#### Dependencies

To enable this parameter, set the **Specify** parameter to
`Output size` and the **Output column
mode** parameter to `User-specified`.

### **Number of added columns** — Number of columns added to input image `2` (default) | positive integer | two-element vector of positive integers

Specify how many columns to add to the input signal. The behavior of this parameter
changes depending on whether you are padding only one side or both sides of the
image.

| **Add columns to** | **Number of added columns** | Description |
| --- | --- | --- |
| `Left` | *P* | Add *P* columns to the left side of the input image. |
| `Right` | *Q* | Add *Q* columns to the right side of the input image. |
| `Both left and right` | [*P Q*] | Add *P* columns to the left side and *Q* columns to the right side of the input image. |

#### Dependencies

To enable this parameter, set the **Specify** parameter to
`Pad size` and the **Add columns** to
parameter to `Left`, `Right`, or
`Both left and right`.

### **Add rows to** — Row padding location `Top` (default) | `Bottom` | `Both top and bottom` | `No padding`

Select which sides of the input image to pad with additional rows:

- `Top` — Add rows to the top of the input
  image.
- `Bottom` — Add rows to the bottom of the input
  image.
- `Both top and bottom` — Add rows to both the top and
  bottom of the input image.
- `No padding` — Do not add rows to the input
  image.

### **Output row mode** — Output row sizing method `User-specified` (default) | `Next power of two`

Specify the number of rows in the output image using one of these options:

- `User-specified` — Specify the number of rows in the
  output image using the **Number of output rows**
  parameter.
- `Next power of two` — Add rows to the input image
  until the total number of rows is a power of two.

#### Dependencies

To enable this parameter, set the **Specify** parameter to
`Output size`.

### **Number of output rows** — Number of rows in output image `12` (default) | positive integer

Specify the number of rows in the output image as a positive integer
*N*. If the value of this parameter is less than the number of rows
in the input image, then the output image contains only the last *N*
rows of the input image.

#### Dependencies

To enable this parameter, set the **Specify** parameter to
`Output size` and the **Output row mode**
parameter to `User-specified`.

### **Number of added rows** — Number of rows added to input image `[2 3]` (default) | positive integer | two-element vector of positive integers

Specify how many rows to add to the input signal. The behavior of this parameter
changes depending on whether you are padding only one side or both sides of the
image.

| **Add rows to** | **Number of added rows** | Description |
| --- | --- | --- |
| `Top` | *R* | Add *R* rows to the top of the input image. |
| `Bottom` | *S* | Add *S* rows to the bottom of the input image. |
| `Both top and bottom` | [*R S*] | Add *R* rows to the top and *S* rows to the bottom of the input image. |

#### Dependencies

To enable this parameter, set the **Specify** parameter to
`Pad size` and the **Add rows** to
parameter to `Top`, `Bottom`, or
`Both top and bottom`.

### **Action when truncation occurs** — Action when input signal is truncated `None` (default) | `Warning` | `Error`

You can specify how the block behaves when the input signal is truncated as one of
these options:

- `None` — Does not notify you when the signal is
  truncated.
- `Warning` — Displays a warning message in the
  MATLAB® command window when the input signal is truncated.
- `Error` — Displays an error dialog box and terminates
  the simulation when the input signal is truncated.

#### Dependencies

To enable this parameter, set the **Specify** parameter to
`Output size`.

## Libraries

Computer Vision Toolbox / Utilities

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Pad image by adding rows, columns, or both

The Image Pad block expands the dimensions of an image by padding its rows,
columns, or both.
