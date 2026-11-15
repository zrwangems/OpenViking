---
type: simulink-block
title: 'V4L2 Video Capture'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Video'
documentation_page: 'v4l2videocapture'
documentation_source_path: 'beagleboneblue/ref/v4l2videocapture.html'
language: en
---

# V4L2 Video Capture

## Ports

### Output

### **R** — Red component of pixel matrix

This port outputs the red component of each pixel.

#### Dependencies

This port appears only when you select the `RGB` from
**Pixel format**.

**Data Types:** `uint8`

### **G** — Green component of pixel matrix

This port outputs the green component of each pixel.

#### Dependencies

This port appears only when you select the `RGB` from
**Pixel format**.

**Data Types:** `uint8`

### **B** — Blue component of pixel matrix

This port outputs the blue component of each pixel.

#### Dependencies

This port appears only when you select the `RGB` from
**Pixel format**.

**Data Types:** `uint8`

### **Y** — Luma component of pixel matrix

This port outputs the luma component of each pixel.

#### Dependencies

This port appears only when you select the `YCbCr
4:2:2` from **Pixel format**.

**Data Types:** `uint8`

### **Cb** — Blue difference component of pixel matrix

This port outputs the blue difference component of each pixel.

#### Dependencies

This port appears only when you select the `YCbCr
4:2:2` from **Pixel format**.

**Data Types:** `uint8`

### **Cr** — Red difference component of pixel matrix

This port outputs the red difference component of each pixel.

#### Dependencies

This port appears only when you select the `YCbCr
4:2:2` from **Pixel format**.

**Data Types:** `uint8`

## Parameters

### **Device name** — Name of connected video device `'/dev/video0'` (default)

Enter the path and name of the video device.

The Linux kernel creates a video device file when you connect a supported USB video
camera to the target hardware. By default, the Linux kernel supports all USB video class (UVC) devices.

To see the list of video device files, open a command line session with the target
hardware and enter: `ls -al /dev/video*`.

### **Image size** — Display resolution 320x240 (default) | 160x120 | Custom

Specify the display resolution of the image to be captured, in pixels.

### **Image size ([width, height])** — Size of the image to be captured `[640,480]` (default)

Specify the width in pixels and height in lines of the image to be captured.

#### Dependencies

This parameter appears only when you select `Custom` from
**Image Size**.

### **Pixel format** — Format of output video stream RGB (default)

Select the video format of the video device, `RGB` or
`YCbCr 4:2:2`.

`RGB` represents the red, green, and blue components of a pixel
using an 8-bit value. RGB color space is device-dependent.

`YCbCr 4:2:2` uses three channels to represent color image data for
each pixel:

- `Y` is the luma component (essentially a grayscale
  signal).
- `Cb` is the blue-difference chroma component.
- `Cr` is the red-difference chroma component.

The Cb and Cr components are sampled at half the sample rate of Y.

### **Sample time** — Frequency at which a new image is captured `1/10` (default)

Select the sample time of the video device.

Smaller values require the processor to complete the same number of instructions in
less time, which can cause task overruns.

## Libraries

Simulink Coder Support Package for BeagleBone Blue Hardware / Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Capture video from USB camera using V4L2

Capture live video from a USB video camera, using the V4L2 (Video for Linux Two API)
driver framework. The output is in row major format. During simulation, the model outputs a
moving colorbar image.

The Ubuntu®
Linux® image used on the target hardware supports video capture from USB cameras listed
as Universal Video Class (UVC). In addition to being a UVC class camera, the camera itself
must support data acquisition in YUYV mode.

The following cameras have been tested:

- Logitech QuickCam Pro 9000
- Logitech QuickCam Pro 3000
- Logitech Webcam C600
- Logitech HD Webcam C310
