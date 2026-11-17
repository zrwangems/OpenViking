---
type: simulink-block
title: 'Draw Shapes'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Text & Graphics'
documentation_page: 'drawshapes'
documentation_source_path: 'ref/drawshapes.html'
language: en
---

# Draw Shapes

## Ports
```yaml
ports:
- name: Image
  summary: Input image or video stream *M*-by-*N* matrix of intensity values | *M*-by-*N*-by-*3* array of color values
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: R
  summary: Red color channel of the image or video frame *M*-by-*N* matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: G
  summary: Green color channel of the image or video frame *M*-by-*N* matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: B
  summary: Blue color channel of the image or video frame *M*-by-*N* matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Pts
  summary: Shape coordinates *M*-by-3 matrix | *M*-by-4 matrix | *M*-by-2*L* matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: ROI
  summary: Region of interest 4-element vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Clr
  summary: Color of shape 3-element vector | *M*-by-*3* matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: Output image *M*-by-*N* matrix of intensity values | *M*-by-*N*-by-*3* array of color values
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### Input

### **Image** — Input image or video stream *M*-by-*N* matrix of intensity values | *M*-by-*N*-by-*3* array of color values

Input image, specified as either an *M*-by-*N*
matrix of intensity values or an
*M*-by-*N*-by-*3* matrix of color
values with *3* color planes.

When the input is a video stream, the block processes it frame by frame.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **R** — Red color channel of the image or video frame *M*-by-*N* matrix

Red color channel of the image or video frame, specified as an
*M*-by-*N* matrix. The **R**,
**G**, and **B** ports must have the same
dimensions and data type.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **G** — Green color channel of the image or video frame *M*-by-*N* matrix

Green color channel of the input image or video frame, specified as an
*M*-by-*N* matrix. The **R**,
**G**, and **B** ports must have the same
dimensions and data type.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **B** — Blue color channel of the image or video frame *M*-by-*N* matrix

Blue color channel of the input image or video frame, specified as an
*M*-by-*N* matrix. The **R**,
**G**, and **B** ports must have the same
dimensions and data type.

#### Dependencies

To enable this port, set the **Image signal** parameter to
`Separate color signals`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Pts** — Shape coordinates *M*-by-3 matrix | *M*-by-4 matrix | *M*-by-2*L* matrix

Coordinates of the input shapes to be drawn on the input. The format of the points
depends on the type of shape you specify with the **Shape** parameter.

- `Rectangles` — *M*-by-4 matrix of
  the form [*x*
  *y*
  *width*
  *height*]. *M* is the number of
  rectangles.

  | Shape | Input to the Pts Port | Drawn Shape |
  | --- | --- | --- |
  | Single Rectangle | Four-element row vector in the format   `[x y width height]`, where:  - `x` and `y` are the   coordinates of the upper-left corner of the rectangle. - `width` and `height`   parameters are the width and height of the rectangle, in   pixels. The values of `width` and   `height` must be greater than 0. |  |
  | *M* Rectangles | *M*-by-4 matrix in the format  [x1y1width1height1x2y2width2height2⋮⋮⋮⋮xMyMwidthMheightM]  ,where each row of the matrix corresponds to a different rectangle and is of the same form as the vector for a single rectangle. |  |
- `Lines` —
  *M*-by-2*L* matrix of the form
  [*x1*,
  *y1*,
  *x2*,
  *y2*,…,*xL*,
  *yL*]. *M* is the
  number of polylines.

  | Shape | Input to the Pts Port | Drawn Shape |
  | --- | --- | --- |
  | Single Line | Four-element row vector in the format `[x1 y1 x2 y2]`, where:  - `x1` and   `y1` are the   coordinates of the beginning of the line. - `x2` and   `y2` are the   coordinates of the end of the line. |  |
  | *M* Lines | *M*-by-4 matrix in the format  [x11y11x12y12x21y21x22y22⋮⋮⋮⋮xM1yM1xM2yM2]  ,where each row of the matrix corresponds to a different line and is of the same form as the vector for a single line. |  |
  | Single Polyline with (*L*-1) Segments | Vector of size 2*L*, where *L* is the number of vertices, in the format, `[x1, y1, x2, y2, ..., xL, yL]`, where  - x1 and y1   are the coordinates of the beginning of the first line   segment. - x2 and y2   are the coordinates of the end of the first line segment and   the beginning of the second line segment. - xL and yL   are the coordinates of the end of the   (*L*-1)th line   segment.  The polyline always contains (*L*-1) number of segments because the first and last vertex points do not connect.  The block produces an error message when the number of columns is less than two or not a multiple of two. |  |
  | *M* Polylines with (*L*-1) Segments | *M*-by-*2**L* matrix in the format  [x11y11x12y12⋯x1Ly1Lx21y21x22y22⋯x2Ly2L⋮⋮⋮⋮⋱⋮⋮xM1yM1xM2yM2⋯xMLyML]  , where each row of the matrix corresponds to a different polyline and is of the same form as the vector for a single polyline. When one of the polylines contains less than (*L*–1) number of segments, fill the matrix by repeating the coordinates of the last vertex.  The block produces an error message if the number of columns is less than two or not a multiple of two. |  |
- `Polygons` —
  *M*-by-2*L* matrix of the form
  [*x1*,
  *y1*,
  *x2*,
  *y2*,…,*xL*,
  *yL*]. *M* is the
  number of polygons. The points are specified in consecutive order to form a
  polygon.

  | Shape | Input to the Pts Port | Drawn Shape |
  | --- | --- | --- |
  | Single Polygon with *L* line segments | Row vector of size 2*L*, where *L* is the number of vertices, in the format `[x1 y1 x2 y2 ... xL yL]`, where:  - x1 and y1   are the coordinates of the beginning of the first line   segment. - x2 and y2   are the coordinates of the end of the first line segment and   the beginning of the second line segment. - xL and yL   are the coordinates of the end of the   (*L*-1)th line   segment and the beginning of the   *L*th line   segment.  The block connects `[x1 y1]` to `[xL yL]` to complete the polygon. The block produces an error if the number of columns is less than two or not a multiple of two. |  |
  | *M* Polygons with the largest number of line segments in any line being *L* | *M*-by-2*L* matrix in the format  [x11y11x12y12⋯x1Ly1Lx21y21x22y22⋯x2Ly2L⋮⋮⋮⋮⋱⋮⋮xM1yM1xM2yM2⋯xMLyML]  , where each row of the matrix corresponds to a different polygon and is of the same form as the vector for a single polygon.  When one of the polygons contains less than *L* number of segments, fill the matrix by repeating the coordinates of the last vertex.  The block produces an error message if the number of columns is less than two or not a multiple of two. |  |
- `Circles` — *M*-by-3 matrix of the
  form [*x*
  *y*
  *radius*]. *M* is the number of circles.

  | Shape | Input to the Pts Port | Drawn Shape |
  | --- | --- | --- |
  | Single Circle | Three-element row vector in the format   `[x y radius]`, where:  - `x` and `y` are coordinates   for the center of the circle. - `radius` is the radius of the circle,   which must be greater than 0. |  |
  | *M* Circles | **M*-by-3* matrix in the format  [xctr1yctr1radius1xctr2yctr2radius2⋮⋮⋮xctrMyctrMradiusM]  , where each row of the matrix corresponds to a different circle and is of the same form as the vector for a single circle. |  |

#### Dependencies

- Double-precision floating point is only supported if the input to the
  **Image** or **R**, **G**,
  and **B** ports is floating point.
- Single-precision floating point is only supported if the input to the
  **Image** or **R**, **G**,
  and **B** ports is floating point.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **ROI** — Region of interest 4-element vector

Region of interest, specified as a four-element vector of the form
[*x*
*y*
*width*
*height*]. The region defines a rectangular area to draw shapes. The
first two elements represent the one-based coordinates of the upper-left corner of the
area. The remaining two elements represent the width and height of the area.

#### Dependencies

To enable this port, set the **Draw shapes in** parameter to
`Specify region of interest via port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Clr** — Color of shape 3-element vector | *M*-by-*3* matrix

Color of the shape, specified as either a *3*-element vector or
an *M*-by-*3* matrix. *M* is the
number of shapes and three denotes the number of color planes. You can specify
different color for each of the *M* shapes, or specify one color for
all shapes.

#### Dependencies

To enable this port, set the **Border color source** or
**Fill color source** parameter to `Input
port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output image *M*-by-*N* matrix of intensity values | *M*-by-*N*-by-*3* array of color values

Output image, returned as an *M*-by-*N* matrix
or *M*-by-*N*-by-*3* array. The
output image is of the same dimension as the input image.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## Parameters
```yaml
parameters:
- name: Shape
  summary: Shape to draw Rectangles (default) | Lines | Polygons | Circles
  group: ''
- name: Fill shapes
  summary: Fill shapes with color off (default) | on
  group: ''
- name: Line width
  summary: Line width for the shapes 1 (default) | positive scalar
  group: ''
- name: Fill color source
  summary: Input source to specify fill color Specify via dialog (default) | Input port
  group: ''
- name: Fill color
  summary: Color to fill the shapes Black (default) | White | User-specified value
  group: ''
- name: Border color source
  summary: Input source to specify border color Specify via dialog (default) | Input port
  group: ''
- name: Border color
  summary: Outline color of the shape Black (default) | White | User-specified value
  group: ''
- name: Color value(s)
  summary: Color value to draw the border or fill the shape scalar | 3-element vector
  group: ''
- name: Opacity factor (between 0 and 1)
  summary: Opacity of the color value in the range [0,1] | *R*-element vector
  group: ''
- name: Use antialiasing
  summary: Smoothing algorithm off | on
  group: ''
- name: Draw shapes in
  summary: Region to draw the shape Entire image (default) | Specify region of interest via port
  group: ''
- name: Image signal
  summary: Number of input ports for the image signal One multidimensional signal (default) | Separate color signals
  group: ''
```

**Main Tab**

### **Shape** — Shape to draw `Rectangles` (default) | `Lines` | `Polygons` | `Circles`

One or more shapes to draw on the image, specified as one of the following:

- `Rectangles` — Draw one or more rectangles on
  the input image or the video frame using the specified shape coordinates.
- `Lines` — Draw one or more lines on the input
  image or the video frame using the specified shape coordinates.
- `Polygons` — Draw one or more polygons on the
  input image or the video frame using the specified shape coordinates.
- `Circles` — Draw one or more circles on the
  input image or the video frame using the specified shape coordinates.

### **Fill shapes** — Fill shapes with color off (default) | on

Select **Fill shapes** to enable the color parameters to fill
shapes.

**Note**

If you are generating the code and selecting the **Fill shapes**
check box, the word length of the block input(s) cannot exceed 16 bits.

### **Line width** — Line width for the shapes 1 (default) | positive scalar

Specify the line width for the shapes to be drawn, as a positive scalar.

### **Fill color source** — Input source to specify fill color `Specify via dialog` (default) | `Input port`

Specify the input source for the fill color value. Select **Fill color
source** as one of the following:

- `Specify via dialog` — To specify the color value by
  using **Fill color** parameter.
- `Input port` — To specify the color value by using
  **Clr** port.

#### Dependencies

To enable this parameter, select **Fill shapes**.

### **Fill color** — Color to fill the shapes `Black` (default) | `White` | `User-specified value`

Specify the shape fill color as either `Black`,
`White` or `User-specified value`.
The `User-specified value` can be scalar or a 3-element vector.
Use a scalar to specify an intensity value and 3-element vector to specify RGB color
value.

| Color Value(s) for Filling One Shape or Multiple Shapes with the Same Color | Color Value(s) for Filling Multiple Shapes with Unique Colors |
| --- | --- |
| Scalar intensity value | *R*-element vector, where *R* is the number of shapes. |
| *3*-element RGB vector | *R*-by-*3* matrix, where *3* is the number of color planes and *R* is the number of shapes. |

For each value in the **Color Value(s)** parameter,
enter a number between the minimum and maximum values that can be represented by the
data type of the input image. If you enter a value outside this range, the block
produces an error message.

#### Dependencies

To enable this parameter, select the **Fill shapes**
parameter.

### **Border color source** — Input source to specify border color `Specify via dialog` (default) | `Input port`

Specify the input source for the border color value. Select **Border color
source** as one of the following:

- `Specify via dialog` — To specify the color value by
  using **Border color** parameter.
- `Input port` — To specify the color value by using
  **Clr** port.

### **Border color** — Outline color of the shape `Black` (default) | `White` | `User-specified value`

Specify the border color of shape as either `Black`,
`White` or `User-specified value`.
The `User-specified value` can be scalar or a 3-element vector.
Use a scalar to specify an intensity value and 3-element vector to specify RGB color
value.

| Color Value(s) for Drawing One Shape or Multiple Shapes with the Same Color | Color Value(s) for Drawing Multiple Shapes with Unique Colors |
| --- | --- |
| Scalar intensity value | *R*-element vector, where *R* is the number of shapes. |
| *3*-element RGB vector | *R*-by-*3* matrix, where three is the number of color planes and *R* is the number of shapes. |

For each value in the **Color Value(s)** parameter,
enter a number between the minimum and maximum values that can be represented by the
data type of the input image. If you enter a value outside this range, the block
produces an error message.

### **Color value(s)** — Color value to draw the border or fill the shape scalar | 3-element vector

Specify color value to draw the border or fill the shape as a scalar or 3-element
vector. Use a scalar to specify intensity value and a 3-element vector for RGB color
value.

**Tunable:** Yes

#### Dependencies

To enable this parameter set the **Border color** or
**Fill color** parameter to `User-specified
value`.

### **Opacity factor (between 0 and 1)** — Opacity of the color value in the range [0,1] | *R*-element vector

Specify the opacity of the color as a positive value in the range [0, 1].
`0` is transparent and `1` is opaque.

| Opacity Factor value for Filling One Shape or Multiple Shapes with the Same Color | Opacity Factor value for Filling Multiple Shapes with Unique Colors |
| --- | --- |
| Scalar intensity value | *R*-element vector where *R* is the number of shapes |

#### Dependencies

To enable this parameter, select the **Fill shapes**
parameter.

### **Use antialiasing** — Smoothing algorithm off | on

Performs smoothing on the line, polygon, or circle.

#### Dependencies

- To enable this parameter, set the **Shape** parameter to
  either `Lines`, `Polygons`, or
  `Circles`.

### **Draw shapes in** — Region to draw the shape `Entire image` (default) | `Specify region of interest via port`

Specify the extent of the region to draw the specified shape. Select the value as
one of the following:

- `Entire image` — To draw the shape on the entire
  image.
- `Specify region of interest via port` — To draw the
  shape within an ROI specified by the input **ROI** port.

### **Image signal** — Number of input ports for the image signal `One multidimensional signal` (default) | `Separate color signals`

Specify the number of input ports to use for specifying the input image. Select the
value as one of the following:

- `One multidimensional signal` — To specify intensity
  or color image using a single port. The block enables the
  **Image** port for a
  *M*-by-*N*-by-*3* color
  image, or a *M*-by-*N* intensity image.
- `Separate color signals` — To specify red, green,
  and, blue color planes of the input color image. The block enables the
  **R**,**G**, and, **B** input
  ports. Each port accepts the *M*-by-*N* plane of
  an RGB color image.

**Data Types Tab**

For details on the fixed-point block parameters, see Specify Fixed-Point Attributes for Blocks (DSP System Toolbox).
## Libraries

Computer Vision Toolbox / Text & Graphics

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Draw rectangles, lines, polygons, or circles on images

The Draw Shapes block draws rectangles, lines, polygons, or circles on
images by overwriting the pixel values. As a result, the shapes are drawn on the output image.
The block uses Bresenham's line drawing algorithm to draw lines, polygons, and rectangles and
Bresenham's circle drawing algorithm to draw circles. The output signal is of the same size
and data type as the input signal fed to the **Image**,
**R**, **G**, and **B** ports.

You can set the shape fill or border color via the input port or by manually entering the
values using the parameters. Use the color parameters to specify the appearance of the
rectangles, lines, polygons, or circles.
