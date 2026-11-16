---
type: simulink-block
title: 'Insert Text'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Graphics'
documentation_page: 'inserttextblock'
documentation_source_path: 'ref/inserttextblock.html'
language: en
---

# Insert Text

## Ports

### Input

### **Image** — Input image matrix | array

Input image or video, specified as an *M*-by-*N*
matrix, *M*-by-*N*-by-*T* array,
*M*-by-*N*-by-*C* array, or
*M*-by-*N*-by-*C*-by-*T*
array. *T* is the number of frames in a video or image sequence, and
*C* is the number of color channels.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`One multidimensional signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **R** — Red color component of input image matrix | array

Red color component of the input image or video, specified as an
*M*-by-*N* matrix or
*M*-by-*N*-by-*T* array, where
*T* is the number of frames in the input video.

**Note**

Inputs to the **R**, **G**, and
**B** ports must have the same dimensions and data type.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **G** — Green color component of input image matrix | array

Green color component of the input image or video, specified as an
*M*-by-*N* matrix or
*M*-by-*N*-by-*T* array, where
*T* is the number of frames in the input video.

**Note**

Inputs to the **R**, **G**, and
**B** ports must have the same dimensions and data type.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **B** — Blue color component of input image matrix | array

Blue color component of the input image or video, specified as an
*M*-by-*N* matrix or
*M*-by-*N*-by-*T* array, where
*T* is the number of frames in the input video.

**Note**

Inputs to the **R**, **G**, and
**B** ports must have the same dimensions and data type.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Select** — Select the display text positive integer

Select the display text, specified as a positive integer.

Select a display text from the cell array using this port, when the input to the
**Text** parameter is a cell array of character vectors. For
example, the value to the **Select** port must be in the range
`[1, S]`, when the **Text**
parameter is a cell array of *S* character vectors.

#### Dependencies

To enable this port, specify the **Text** parameter as a cell
array of character vectors.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Color** — Text color value scalar | vector | matrix

Text color value, specified as a scalar, a vector or a matrix. Use this table to
determine the type of input value to this port.

| **Input Image** | Same Color for All Text | Different Color for Each Character Vector |
| --- | --- | --- |
| Intensity image | scalar value | *S*-element vector. *S* is the number of character vectors in the cell array specified to **Text** parameter. |
| Color image | three-element vector | *S*-by-3 matrix. *S* is the number of character vectors in the cell array specified to **Text** parameter. |

The data type of the input image determines the range of color values. For
example, a color value for a floating-point input image data type is in the range
[`0`, `1`]. For an input image with a
`uint8` data type, the value is in the range [`0`,
`255`].

**Note**

The input to this port must be of the same data type as the input image.

#### Dependencies

To enable this port, set the **Color value source** parameter
to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Location** — Location index vector | matrix

Location index, specified as a two-element vector of the form `[x
y]` or an *S*-by-2 matrix. `[x y]`
specify the coordinates of the input image to display the text. Specify it as an
*S*-by-2 matrix, to display *S* character vectors
at different locations in the image.

#### Dependencies

To enable this port, set the **Location source** parameter to
`Input port`.

**Data Types:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Opacity** — Opacity factor scalar | vector

Opacity factor, specified as a scalar or an *S*-element vector.

- Scalar — Specify same opacity value to all the display text.
- *S*-element vector — Specify different opacity values to
  *S* character vectors specified in the
  **Text** parameter.

Specify opacity values in the range `[0`,
`1]`.

**Note**

The input to the **Image**, **R**,
**G**, **B**, and **Color**
ports must be of the same data type as the input to this port.

#### Dependencies

To enable this port, set the **Opacity source** parameter to
`Input port`.

**Data Types:** `single` | `double`

### **Variables** — Text variable values scalar | vector

Text variable values, specified as a scalar or a vector. The block replaces the
format specifiers such as `%d`, `%f`, or
`%s` in the **Text** parameter, with the
elements specified by the **Variables** port.

Use the **Variables** port to display *S*
character vectors or numerical values simultaneously, at *S*
locations of the input image or video frame. The input to this port depends on the
type of format specifier specified to the **Text** parameter.

| Display Text | Data Type | Format Specifier | Input to the **Variables** Port |
| --- | --- | --- | --- |
| Character vectors | `uint8` | `'%s', '%c'` | `['Text1' 0 'Text2' 0 .... 0 'Text`*S*`']` |
| Integers | `uint8`, `uint16`, `uint32`, `int8`, `int16`, `int32` | `'%d', '%i', '%o', '%x', '%X'` | `[x1 x2 x3.... xS]` |
| Floating point numbers | `single`, `double` | `'%f', '%e', '%E', '%g', '%G'` | `[x1 x2 x3.... xS]` |

For more information on format specifiers, see `sprintf`.

#### Dependencies

To enable this port, enter ANSI C `printf`-style format
specifiers, such as `'%d'`, `'%f'`, or
`'%s'` in the **Text** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Port\_1** — Output image matrix | array

Output image or video, returned as an *M*-by-*N*
matrix, *M*-by-*N*-by-*T* array,
*M*-by-*N*-by-*C* array, or
*M*-by-*N*-by-*C*-by-*T*
array. *T* is the number of frames in a video or image sequence, and
*C* is the number of color channels.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`One multidimensional signal`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **R** — Red color component of output image matrix | array

Red color component of the output image or video, returned as an
*M*-by-*N* matrix or
*M*-by-*N*-by-*T* array, where
*T* is the number of frames in the output video.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **G** — Green color component of output image matrix | array

Green color component of the output image or video, returned as an
*M*-by-*N* matrix or
*M*-by-*N*-by-*T* array, where
*T* is the number of frames in the output video.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **B** — Blue color component of output image matrix | array

Blue color component of the output image or video, returned as an
*M*-by-*N* matrix or
*M*-by-*N*-by-*T* array, where
*T* is the number of frames in the output video.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### Main

### **Text** — Text to insert `'Text'` (default) | character vector | cell array of character vectors

Specify the text to insert into the image, as a character vector or a cell array
of character vectors. You can display either a single text or multiple texts
simultaneously, using the **Text** parameter.

- Single text — You can specify **Text** parameter as either
  a character vector or a cell array of *S* character vectors. If
  you specify a cell array, select one-out-of-*S* character
  vectors from the cell array, by using the **Select** input
  port.
- Multiple texts simultaneously — You can specify ANSI C
  `printf`-style format specifiers in the
  **Text** parameter. You can then specify the texts by using
  the **Variable** input port. Supported format specifiers
  include `%d`, `%i`,
  `%u`, `%o`,
  `%x`, `%X`,
  `%c`, `%s`,
  `%f`, `%e`,
  `%E`, `%g`, and
  `%G`. For more information on format specifiers, see
  `sprintf`.

Use this table to determine the type of input value to the
**Text** parameter.

| Display | Input to**Text** parameter | Status of **Select** port | Status of **Variables** port |
| --- | --- | --- | --- |
| A character vector | Single character vector such as `'Text'` | `Disabled` | `Disabled` |
| One-out-of-*S* character vectors | Cell array of *S* character vectors such as `{'Text1', 'Text2',...., 'TextS'}` | `Enabled` | `Disabled` |
| *S* character vectors | Format specifier such as `'%s'` | `Disabled` | `Enabled` |

### **Color value source** — Source of text color `Specify via dialog` (default) | `Input port`

Select the text color source as either `Specify via
dialog` or `Input port`. You can specify this
parameter as `Specify via dialog` to specify insert text
colors using the **Color value** parameter. You can specify this
parameter as `Input port` to specify text colors by using the
**Color** input port.

### **Color value** — Text color value `[0 0 0]` (default) | scalar | vector | matrix

Text color value specified as a scalar, a vector, or a matrix. Use this table to
determine the type of input value to this port.

| **Input Image** | Same Color for All Text | Different Color for Each Character Vector |
| --- | --- | --- |
| Intensity image | scalar value | *S*-element vector. *S* is the number of character vectors in the cell array specified to the **Text** parameter. |
| Color image | three-element vector | *S*-by-*3* matrix. *S* is the number of character vectors in the cell array specified to the **Text** parameter. |

The data type of the input image determines the range of color values. For
example, a color value for a floating-point input image data type is in the range
[`0`, `1`]. For an input image with a
`uint8` data type, the value is in the range [`0`,
`255`].

#### Dependencies

To enable this parameter, set the **Color value source**
parameter to `Specify via dialog`.

### **Location source** — Source of location indices `Specify via dialog` (default) | `Input port`

Specify the source of location coordinates of the display text as one these options:

- `Specify via dialog` — Use the **Location
  [x y]** parameter to specify location coordinates of the display
  text.
- `Input port` — Use the
  **Location** input port to specify location coordinates of
  the display text.

### **Location [x y]** — Text location index `[1,1]` (default) | vector | matrix

Text location index, specified as a two-element vector `[x y]` or
an *S*-by-2 matrix. `[x y]` specify the coordinates
of the input image to display the text. Specify the value as an
*S*-by-2 matrix, to display *S* character vectors at
different locations in the image.

#### Dependencies

To enable this parameter, set the **Location source** parameter
to `Specify via dialog`.

### **Opacity source** — Source of opacity factor `Specify via dialog` (default) | `Input port`

Specify opacity factor source as one of these options:

- `Specify via dialog` — Use the
  **Opacity** parameter to specify opacity factor.
- `Input port` — Use the **Opacity**
  input port to specify opacity factor.

### **Opacity** — Opacity factor `1` (default) | scalar | vector

Opacity factor, specified as a scalar or an *S*-element
vector.

- Scalar — Specify same opacity value to the display text.
- *S*-element vector — Specify different opacity values to
  *S* character vectors specified to the
  **Text** parameter

Specify opacity value in the range `[0`,
`1]`.

#### Dependencies

To enable this parameter, set the **Opacity source** parameter
to `Specify via dialog`.

### **Image signal** — Input and output signal format `One multidimensional signal` (default) | `Separate color signals`

Specify the format of the input and output images of the block using these
options:

- `One multidimensional signal` — The block enables a
  single input port and single output port.
- `Separate color signals` — The block enables R, G,
  and B input and output signal ports for the respective color channels of the
  image.

### **Input image is transposed (data order is row major)** — Mirror text and text location `off` (default) | `on`

Enable this parameter to mirror the text string and reverse its location in the
image from `[x y]` to `[y x]`.

### Font

### **Font face** — Font of text `LucidaSansRegular` (default) | `Agency FB` | `Agency FB Bold` | `Algerian` | `Ariel` | `Arial Black` | `Arial Bold` | `Arial Bold Italic` | ...

Specify the font of the inserted text. The block populates this list with the
fonts installed on your system. On Windows®, the block searches the system registry for font files. On UNIX, the
block searches the font path of the X Server for font files.

### **Font size (points)** — Font size `12` (default) | positive scalar

Specify the font size of the inserted text.

### **Anti-aliased** — Smooth text edges `on` (default) | `off`

Enable this parameter to smooth the edges of the inserted text. The smoothing
process is computationally expensive.

## Libraries

Computer Vision Toolbox / Text & Graphics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a Supports word lengths less than or equal to 32 bits. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013a**

## Description

Draw text on images or video frames

The Insert Text block draws formatted text on an input image or video
stream. The block produces stylized text bitmaps using the open-source font engine Free Type
2.3.5 library. For more information about the library, see The FreeType Project website.

**Note**

This block supports only ASCII characters.

This block enables you to insert:

- A single instance of text
- Multiple instances of the same text
- Multiple instances of text, with different text at each location
