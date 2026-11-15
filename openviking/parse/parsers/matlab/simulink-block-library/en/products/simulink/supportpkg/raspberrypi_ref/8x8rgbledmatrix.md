---
type: simulink-block
title: '8x8 RGB LED Matrix'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Sense HAT'
documentation_page: '8x8rgbledmatrix'
documentation_source_path: 'supportpkg/raspberrypi_ref/8x8rgbledmatrix.html'
language: en
---

# 8x8 RGB LED Matrix

## Ports

### Input

### **Location** — Location of the pixel to display in the specified color [Nx2] matrix

In Write Pixel mode, provide the location value for row and
column for each pixel in the range 1 to 8.

**Data Types:** `uint8`

### **RGB** — RGB color to display in the specified location [Nx3] matrix

In Write Pixel mode, provide a [Nx3] matrix of values for R,
G, and B in the range 0 to 255.

**Data Types:** `uint8`

### **Image** — Input image to display on the LED matrix [8x8x3] matrix

In `Display Image` mode, provide an
[8x8x3] image signal when you set the **Input Image source** to `One
multidimensional signal`.

**Data Types:** `uint8`

### **R,G,B** — Input image to display on the LED matrix [8x8] matrix

In `Display Image` mode, provide three
[8x8] image color signals when you set the **Input Image source** to `Separate
color signals`.

**Data Types:** `uint8`

### **Orient** — Input port for image orientation 0 | 90 | 180 | 270

In `Display Image` mode, provide the
image orientation in degrees when you set the **Orientation
source** as `Input port`.

**Data Types:** `uint8`

## Parameters

### **View Pixel Information** — Button to view the pixel information on RGB LED matrix button

Click this button to know the pixel location numbers on the
RGB LED matrix.

### **Mode** — Mode of operation for the LED matrix `Write Pixel` (default) | `Display Image`

The mode in which the block works either to write a pixel in
a specific color at a specific location or display an input image.

### **Input Image source** — Source of the input image `One multidimensional signal` (default) | `Separate color signals`

Select the source of input image. You can provide an [8x8x3]
one multidimensional signal or three [8x8] separate color signals.

#### Dependencies

This parameter is enabled only when you select `Display
Image` option in **Mode** parameter.

### **Orientation Source** — The source of the image orientation on the LED matrix `Block dialog` (default) | `Input port`

Select the source of image orientation. If you select `Block
dialog` option, you should select a value in **Orientation** parameter.
The image displayed on the LED matrix is set to the orientation that
you specify in this parameter. If you select `Input port` option,
the block takes the image orientation value from the Orient input
port.

#### Dependencies

This parameter is enabled only when you select
`Display Image` option in
**Mode** parameter.

### **Orientation** — Image orientation 0 (default) | 90 | 180 | 270

Select the image orientation value from the list of values.

#### Dependencies

This parameter is enabled only when you select `Display
Image` value in **Mode** parameter and `Block
dialog` value in **Orientation Source** parameter.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Sense HAT

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017a**

## Description

Control pixel(s) color of 8x8 RGB LED Matrix

Control the pixel(s) color of the 8x8 RGB LED matrix. You can
use the block either in ‘Write Pixel’ mode or the ‘Display
Image’ mode.

*Write Pixel Mode*

To set a pixel to a specified RGB value at a location, set the
block to ‘Write Pixel’ mode. Provide the RGB value and
the location in terms of row and the column for each pixel.

An example of how the ‘Write Pixel’ mode works
for this block is shown in the table below.

| Location [row,column] | RGB [red,green,blue] | Output |
| --- | --- | --- |
| [1,1] —> single pixel location | [255,0,0] —> single pixel color | Pixel at [1,1] is set to Red |
| [1,1;1,2;1,3] —> 3 pixels (multiple pixel locations) | [255,0,0] —> single color for all the pixels | Pixels at [1,1], [1,2] and [1,3] are set to Red |
| [1,1;1,2;1,3] —> 3 pixels (multiple pixel locations) | [255,0,0; 255,255,255; 0,0,255] —> 3 colors (multiple colors) | Pixel at 1,1 to Red   Pixel at 1,2 to White  Pixel at 1,3 to Blue |

**Note**

While setting multiple colors, if the number of colors is not
equal to the number of pixels, then the first color that you provide
is set to all the pixels.

*Display Image Mode*

To display an image on the LED matrix, set the block to ‘Display
Image’ mode.

By setting the **Input Image source** parameter
to `One multidimensional signal`, you can
provide the image to be displayed as a [8x8x3] signal to the ‘Image’
input port.

**Input image as a single [8x8x3] multidimensional signal**

By setting the **Input Image source** parameter
to `Separate color signals`, you can provide
the image to be displayed as three [8x8] separate color signals to
the ‘R’, ‘G’, and ‘B’ input ports.

**Input image as 3 separate [8x8] signals**

You can rotate the image displayed on the LED matrix by specifying
the Orientation. The image can be oriented at 0, 90, 180, or 270 degrees.
You can orientate the image. For any other value you give to the image
orientation, the block defaults the image orientation to 0 degree.

By setting the **Orientation source** parameter
to `Block dialog`, you can select orientation
on the block mask in the **Orientation** parameter.

Setting the **Orientation source** parameter
to `Input port` grows an additional input
port ‘Orient’. You can provide the desired orientation
to this port. If the value of this signal is other than 0,90,180,
or 270, the orientation value defaults to 0.

**Image orientation on LED Matrix**
