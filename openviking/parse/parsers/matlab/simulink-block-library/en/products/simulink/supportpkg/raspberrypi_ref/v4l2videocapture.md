---
type: simulink-block
title: 'V4L2 Video Capture'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'v4l2videocapture'
documentation_source_path: 'supportpkg/raspberrypi_ref/v4l2videocapture.html'
language: en
---

# V4L2 Video Capture

## Ports

### Output

### **R** — Red component of pixel matrix

The block outputs the red component of each pixel.

#### Dependencies

To enable this port, set **Pixel format** to
`RGB`.

**Data Types:** `uint8`

### **G** — Green component of pixel matrix

The block outputs the green component of each pixel.

#### Dependencies

To enable this port, set **Pixel format** to
`RGB`.

**Data Types:** `uint8`

### **B** — Blue component of pixel matrix

The block outputs the blue component of each pixel.

#### Dependencies

To enable this port, set **Pixel format** to
`RGB`.

**Data Types:** `uint8`

### **Y** — Luma component of pixel matrix

The block outputs the luma component of each pixel.

#### Dependencies

To enable this port, set **Pixel format** to `YCbCr
4:2:2`.

**Data Types:** `uint8`

### **Cb** — Blue difference component of pixel matrix

The block outputs the blue difference component of each pixel.

#### Dependencies

To enable this port, set **Pixel format** to `YCbCr
4:2:2`.

**Data Types:** `uint8`

### **Cr** — Red difference component of pixel matrix

The block outputs the red difference component of each pixel.

#### Dependencies

To enable this port, set **Pixel format** to `YCbCr
4:2:2`.

**Data Types:** `uint8`

## Parameters

### Basic

### **Device name** — Name of video device `/dev/video0` (default) | character array

Enter the path and name of the video device. The Linux kernel creates a video device file when you connect a supported USB
video camera to the target hardware. By default, the Linux kernel supports all UVC devices.

To find the name of your video device, connect the hardware to your Raspberry Pi board and follow any one of these approaches:

- Open the Raspberry
  Pi Resource Monitor App. The **Device ID**
  is populated in the **Peripherals** section of the
  app.
- Open a command line session with the Raspberry Pi hardware. Execute this command: `ls -al
  /dev/video*`.

### **Image size** — Display resolution of image `320x240` (default) | `160x120` | `640x480` | `800x600` | `custom`

Select the display resolution of the image in pixels.

### **Image size ([width, height])** — Size of image [ 320, 240 ] (default) | positive integer

Enter the width in pixels and the height in lines of the image.

#### Dependencies

To enable this parameter, set **Image size** to
`custom`.

### **Pixel format** — Format of output video stream `RGB` (default) | `YCbCr 4:2:2`

Set the format of the video device to either `RGB` or
`YCbCr 4:2:2`.

`RGB` represents the red, green, and blue components of a
pixel using an 8-bit value. RGB color space is device-dependent.

`YCbCr 4:2:2` uses three channels to represent color
image data for each pixel:

- `Y` is the luma component (essentially a grayscale
  signal).
- `Cb` is the blue-difference chroma component.
- `Cr` is the red-difference chroma component.

The `Cb` and `Cr` components are sampled at half
the sample rate of `Y`.

### **Sample time** — Frequency at which device captures new image `0.1` (default) | scalar

Enter the sample time of the video device. Smaller values require the processor to
complete the same number of instructions in less time, which can cause task
overruns.

### **Flip image along horizontal axis** — Flip image horizontally `off` (default) | `on`

Select the parameter to flip the image along its horizontal reference axis.

### **Flip image along vertical axis** — Flip image vertically `off` (default) | `on`

Select the parameter to flip the image along its vertical reference axis.

### Advanced

**Image properties**

### **Brightness** — Adjust image brightness `0.5` (default) | positive scalar in the range [0, 1]

Adjust the amount of light in the image.

### **Saturation** — Adjust image saturation `0.5` (default) | positive scalar in the range [0, 1]

Adjust the amount of color in the image.

### **Contrast** — Adjust image contrast `0.5` (default) | scalar in the range [0, 1]

Adjust the difference between the darkest and brightest areas in the image.

### **Sharpness** — Adjust image sharpness `0.5` (default) | scalar in the range [0, 1]

Adjust the sharpness to accentuate edges in an image.

**Device properties**

Not all cameras support the device properties.

### **Pan** — Adjust camera pan `0` (default) | scalar in the range [-1, 1]

Adjust the viewing angle of the camera in the horizontal plane.

### **Tilt** — Adjust camera tilt `0` (default) | scalar in the range [-1, 1]

Adjust the viewing angle of the camera in the vertical plane.

### **Zoom** — Adjust camera zoom `0.5` (default) | positive scalar in the range [0, 1]

Zoom-in or zoom-out of the camera.

### **Enable Manual Focus** — Manually focus camera `off` (default) | `on`

Select the parameter to manually adjust the camera focus.

### **Manual focus** — Adjust camera focus `0.5` (default) | positive scalar in the range [0, 1]

Adjust the focus of the camera to enhance the image clarity.

#### Dependencies

To enable this parameter, select **Enable Manual
Focus**.

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2013a**

## Description

Capture video from USB camera using V4L2 framework

The V4L2 Video Capture block enables you to capture live video from a USB
video camera using the Video for Linux Two API (V4L2) driver framework. During simulation, the
block outputs a moving colorbar image.

The debian Linux® image on Raspberry Pi® hardware supports video capture from USB cameras compliant with the USB video
class (UVC) specification. In addition to being a UVC compliant camera, the camera itself
should also support data acquisition in the YUYV mode.

The following cameras have been tested with the
V4L2 Video Capture block but is not limited to:

- Logitech QuickCam Pro 9000
- Logitech QuickCam Pro 3000
- Logitech Webcam C600
- Logitech HD Webcam C310

The V4L2 Video Capture block supports the Raspberry Pi camera board for these Raspbian Linux operating systems running on your Raspberry Pi board: Buster and Bullseye. For more information on how to use the Raspberry Pi camera board for the Bookworm Raspbian Linux operating system, see Use Raspberry Pi Camera Board for Bookworm Raspbian Linux Operating System.
