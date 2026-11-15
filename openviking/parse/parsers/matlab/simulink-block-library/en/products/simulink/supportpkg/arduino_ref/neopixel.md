---
type: simulink-block
title: 'NeoPixel'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'neopixel'
documentation_source_path: 'supportpkg/arduino_ref/neopixel.html'
language: en
---

# NeoPixel

## Ports

### Input

### **LEDPosition** — NeoPixel LED position to blink matrix

Use this port to specify the LEDs on the NeoPixel strip to blink. Input the LED
positions as an *N*-by-1 matrix, where *N*
ranges from `0` to (Number of pixels - `1`). Ensure
that the value you input to this port must lie between `0` to No. of pixel. The block
ignores any input values out of this range.

**Data Types:** `uint16`

### **RGBColor** — RGB components of NeoPixel LED strip matrix

Use this port to specify the RGB components of the NeoPixel LED strip. Specify the
components an *N*-by-3 matrix. The values of R, G, and B for each
pixel must lie in the range `0` to `255`.

#### Dependencies

To enable this port, set **Color format of pixel** to either
`GRB`, `RGB`,
`RBG`, or `BRG`.

**Data Types:** `uint8`

### **RGBWColor** — RGBW components of NeoPixel LED strip matrix

Use this port to specify the RGBW components of the NeoPixel LED strip. Specify
the components as an*N*-by-4 matrix. The values of R, G, B, and W
for each pixel must lie in the range `0` to
`255`.

#### Dependencies

To enable this port, set **Color format of pixel** to either
`RGBW`, `RBGW`,
`WRGB`, `WGRB`,
`WRBG`, `WBGR`,
`GRBW`, `GBRW`,
`BRGW`, or `BGRW`.

**Data Types:** `uint8`

### **Brightness** — Adjust brightness of each LED pixel positive integer in the range [0, 255]

Use this port to adjust the brightness of each NeoPixel LED. An input value of 255
indicates maximum LED brightness, while an input value of 0 indicates minimum LED
brightness

**Data Types:** `uint8`

### **Reset** — Option to reset pixel values of NeoPixel LED strip `0` | `1`

Use this port to reset or accept the pixel values of the NeoPixel LED strip.

- `0` — The block accepts the RGB and RGBW components of the
  NeoPixel LED strip.
- `1` — The block resets all the pixels of the NeoPixel LED
  strip.

**Data Types:** `Boolean`

## Parameters

### **Digital pin (Din)** — Digital pin on Arduino board `6` (default) | Arduino board pin number

Specify the digital pin number of the Arduino board to which the NeoPixel strip is connected. Click **View pin
map** to open the Arduino pin mapping table. For more information on how to assign pins or to view
the pins for the NeoPixel block, see Pin Mapping for Arduino Timer-Independent Blocks.

### **No. of pixel** — Number of LED pixels `24` (default) | positive integer in the range [0, 1023]

Specify the number of sequential LED pixels in a NeoPixel strip.

### **Color format of pixel** — NeoPixel color format `GRB` (default) | `RGB` | `RBG` | `BRG` | `RGBW` | `RBGW` | `WRGB` | `WGRB` | `WRBG` | `WBGR` | `GRBW` | `GBRW` | `BRGW` | `BGRW`

Set the NeoPixel color order format.

### **Frequency of pixel** — NeoPixel bitstream frequency `800KHz` (default) | `400KHz`

Select the frequency at which the NeoPixel LED strip receives data from the
Arduino board.

**Note**

For a NeoPixel strip that uses 800 kHz of bitstream frequency, after the
Arduino board sends the last pixel data to the strip, the streaming must stop
for at least 50 μsec for the new color to latch on to the LED strip.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Control color and brightness of RGB and RGBW Adafruit NeoPixel LED strip

Use the NeoPixel block to control the color and brightness of RGB or RGBW
Adafruit® NeoPixel LED strip. Using the block, you can set the color of individual pixels
for a three-color format (red–green–blue) or a four-color format (red–green–blue–white)
NeoPixel strip. The block supports configuring a maximum of 1024 pixels on the NeoPixel LED
strip.

### Limitations

- The NeoPixel block does not support the Arduino® Nano 33 BLE Sense board currently.
- You can use up to `10`
  NeoPixel blocks in a Simulink® model and deploy the model to a Arduino board.
- If you use the NeoPixel block with the Input
  Capture, Servo Write,
  Standard Servo Read, SAMD Hardware
  Interrupt, AVR Hardware
  Interrupt, External
  Interrupt, or Encoder
  blocks in a Simulink model, the NeoPixel block might not behave as
  expected.
