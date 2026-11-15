---
type: simulink-block
title: 'V4L2 Video Capture'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'v4l2videocapture'
documentation_source_path: 'beaglebone/ref/v4l2videocapture.html'
language: en
---

# V4L2 Video Capture

## Ports

### Output

### **R** — Red component of pixel matrix

The block outputs the red component of each pixel.

#### Dependencies

- To enable this port, set **Pixel format** to
  `RGB`.

**Data Types:** `uint8`

### **G** — Green component of pixel matrix

The block outputs the green component of each pixel.

#### Dependencies

- To enable this port, set **Pixel format** to
  `RGB`.

**Data Types:** `uint8`

### **B** — Blue component of pixel matrix

The block outputs the blue component of each pixel.

#### Dependencies

- To enable this port, set **Pixel format** to
  `RGB`.

**Data Types:** `uint8`

### **Y** — Luma component of pixel matrix

The block outputs the luma component of each pixel.

#### Dependencies

- To enable this port, set **Pixel format** to
  `YCbCr 4:2:2`.

**Data Types:** `uint8`

### **Cb** — Blue difference component of pixel matrix

The block outputs the blue difference component of each pixel.

#### Dependencies

- To enable this port, set **Pixel format** to
  `YCbCr 4:2:2`.

**Data Types:** `uint8`

### **Cr** — Red difference component of pixel matrix

The block outputs the red difference component of each pixel.

#### Dependencies

- To enable this port, set **Pixel format** to
  `YCbCr 4:2:2`.

**Data Types:** `uint8`

## Parameters

### **Device name** — Name of video device `'/dev/video0'` (default) | character array

Enter the path and name of the video device. The Linux kernel creates a video device file when you connect a supported USB video
camera to the target hardware. By default, the Linux kernel supports all UVC devices.

To see the list of video device files, open a command-line session with the board
and enter: `ls -al /dev/video*`.

### **Image size** — Display resolution of image `320x240` (default) | `160x120` | `640x480` | `800x600` | `custom`

Select the display resolution of the image in pixels.

### **Image size ([width, height])** — Size of image 640x480 (default) | positive integer

Enter the width in pixels and the height in lines of the image.

#### Dependencies

To enable this parameter, set **Image size** to
`custom`.

### **Pixel format** — Format of output video stream `RGB` (default) | `YCbCr 4:2:2`

Set the format of the video device to either `RGB` or
`YCbCr 4:2:2`.

`RGB` represents the red, green, and blue components of a
pixel using an 8-bit value. RGB color space is device-dependent.

`YCbCr 4:2:2` uses three channels to represent color image
data for each pixel:

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

## Libraries

Embedded Coder Support Package for BeagleBone Black Hardware

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

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

Sometimes, when you connect a USB webcam to the BeagleBone® Black hardware that was running, the BeagleBone Black hardware does not recognize the USB webcam. To verify that the BeagleBone Black hardware recognizes the USB webcam, in the Command Window,
enter:

```
bbone = beaglebone_black;
system(bbone,'ls -al /dev/videox')
```

If the board recognizes the USB camera, this command returns the name of the video device
associated with the USB camera. Otherwise, restart the BeagleBone Black hardware. After restarting, if the BeagleBone Black hardware does not recognize the USB webcam, is possible that the webcam is
not a supported device. Try using a different USB webcam.
