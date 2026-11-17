---
type: simulink-block
title: 'Image From File'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'imagefromfile'
documentation_source_path: 'ref/imagefromfile.html'
language: en
---

# Image From File

## Ports
```yaml
ports:
- name: Image
  summary: Output image matrix | 3-D array
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: R
  summary: Red color component of image matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: G
  summary: Green color component of image matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: B
  summary: Blue color component of image matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### Output

### **Image** — Output image matrix | 3-D array

Output image, returned as a matrix or 3-D array. If the image read is a binary or
grayscale image, the output is an *M*-by-*N* matrix.
If the image read is a color image, the output is an
*M*-by-*N*-by-3 array.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`One multidimensional signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **R** — Red color component of image matrix

Red color component of the image, returned as an
*M*-by-*N* matrix. The block returns this output
if the input is a color image. If the **Image signal** parameter is
set to Separate color signals and the input image is grayscale, the block returns only
this port.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **G** — Green color component of image matrix

Green color component of the image, returned as an
*M*-by-*N* matrix. The block returns this output
only if the input is a color image.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **B** — Blue color component of image matrix

Blue color component of the image, returned as an
*M*-by-*N* matrix. The block returns this output
only if the input is a color image.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: File name
  summary: Input image peppers.png (default) | file name
  group: ''
- name: Sample time
  summary: Sample time for block execution inf (default) | Positive scalar | Vector
  group: ''
- name: Image signal
  summary: Signal returned by block One multidimensional signal (default) | Separate color signals
  group: ''
- name: Output port labels
  summary: Output port labels R|G|B (default) | port names
  group: ''
- name: Output data type
  summary: Data type of output image inherit from input image (default) | double | single | int8 | uint8 | int16 | uint16
    | int32 | uint32 | boolean | fixed-point | user-defined | inherit via back propagation
  group: ''
- name: Signed
  summary: Signed fixed-point data type on (default) | off
  group: ''
- name: Word length
  summary: Bits in fixed-point data type 16 (default) | positive scalar
  group: ''
- name: Set fraction length in output to
  summary: Scaling factor of fixed-point data type User-defined (default) | Best precision
  group: ''
- name: Fractional length
  summary: Fractional bits 15 (default) | scalar
  group: ''
- name: User-defined data type
  summary: User-defined fixed-point data type uint(8) (default) | User-defined fixed-point data type
  group: ''
```

### **File name** — Input image `peppers.png` (default) | file name

Specify the name of the file that contains the image to read. If the file is not on
the MATLAB® path, click **Browse** and navigate to the file. For
the list of supported file formats, see the `imread` function reference page in the MATLAB documentation.

**Note**

The **File name** parameter supports URL paths.

### **Sample time** — Sample time for block execution `inf` (default) | `Positive scalar` | `Vector`

Specify the sample time for block execution. Vector length must be 2 which
represents [Period, Offset] values where offset should be less than period and
non-negative. Given the default value of inf, the block outputs a matrix for grayscale
and binary. For an input grayscale or color image, the output is a 3-D or 4-D array,
respectively.

The value of the added dimension is equal to floor((*Tsim*/*Ts*)+1).

*Tsim* is the simulation time and
*Ts* is the sample time, for block
execution. For example, if the input image is a 256-by-256 matrix, the simulation time
is 10 sec, and the sample time is set to 0.5 sec, then the output is a 256-by-256-by-21
array.

### **Image signal** — Signal returned by block `One multidimensional signal` (default) | `Separate color signals`

Specify how the block returns the image read from the file.

- `One multidimensional signal`— The block has
  one output port, which returns the entire image.
- `Separate color signals` — The block has three
  output ports, one for each color channel, which returns the individual color
  channels of the image.

### **Output port labels** — Output port labels `R|G|B` (default) | port names

Specify the labels for the output ports. Each label can be any value. Use vertical
bar character, |, as a delimiter between the names of all the output ports.

#### Dependencies

To enable this parameter, set the **Image signal** parameter to
`Separate color signals`.

**Data type**

### **Output data type** — Data type of output image inherit from input image (default) | double | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | boolean | fixed-point | user-defined | inherit via back propagation

Specify the data type of the output image. If the input image data type,differs from
the selected value of the **Output data type** parameter, the block
scales the pixel values, adds an offset to the pixel values so that they are in the
dynamic range of the new data type, or both. Double- and single-precision floating-point
pixel values must be in the range [0 1].

### **Signed** — Signed fixed-point data type `on` (default) | `off`

Select this parameter if the input image data type is signed fixed-point.

#### Dependencies

To enable this parameter, set the **Output data type** parameter
to `Fixed-point`.

### **Word length** — Bits in fixed-point data type 16 (default) | positive scalar

Specify the word length, in bits, of the fixed-point output data type. The value
should be less than 32.

#### Dependencies

To enable this parameter, set the **Output data type** parameter
to `Fixed-point`.

### **Set fraction length in output to** — Scaling factor of fixed-point data type `User-defined` (default) | `Best precision`

Specify the scaling factor of the fixed-point output as one of these options.

- `Best precision`— The output scales automatically such
  that the output signal has the best possible precision.
- Choose `User-defined`— Specify the output scaling in
  the **Fraction length** parameter.

#### Dependencies

To enable this parameter, set the **Output data type** parameter
to `Fixed-point`.

### **Fractional length** — Fractional bits `15` (default) | scalar

Specify the number of bits to the right of the decimal point.

#### Dependencies

To enable this port ,set the **Output data type** parameter to
`Fixed-point`, and set the **Set fraction length in
output**  parameter to `User-defined`.

### **User-defined data type** — User-defined fixed-point data type `uint(8)` (default) | `User-defined fixed-point data type`

Specify any built-in or fixed-point data type. You can specify fixed-point data
types using the `fixdt` (Simulink) function.

#### Dependencies

To enable this parameter, set the **Output data type** parameter
to `User-defined`.
## Libraries

Computer Vision Toolbox / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Read image from file location

The Image From File block reads an image from a specified file location and
imports it to the Simulink® workspace. The input file can contain a binary image, grayscale image, or color
image.
