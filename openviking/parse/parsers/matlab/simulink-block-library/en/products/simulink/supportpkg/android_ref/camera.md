---
type: simulink-block
title: 'Camera'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Audio and Video'
documentation_page: 'camera'
documentation_source_path: 'supportpkg/android_ref/camera.html'
language: en
---

# Camera

## Ports

Not documented in R2025b.

## Parameters

**Resolution**
:   Select the camera location on the device and the size of image.

    - `Front` uses the camera on the same side as the
      display.
    - `Back` uses the camera on the opposite side from the
      display.

    To get a list of device specific **Resolution**, connect your
    configured device and press the **Refresh** button. To configure your
    device, follow the instructions provided during the Hardware Setup process.

    Image size significantly affects the rate at which the camera produces data. For
    example, capturing video at `1920x1080` produces almost six times more
    data than capturing video at `720x486`.

**Sample time**
:   Specify how often the block reads the sensor.

    Smaller values require the processor to complete the same number of instructions in
    less time, which can cause task overruns.

## Libraries

Simulink Support Package for Android Devices / Audio & Video

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Capture video using front or rear camera

Capture video from the front or rear camera on the Android™ device.

The Camera block has three output ports: `R`,
`G`, and `B`. Each port outputs a 2–dimensional matrix of
`uint8` values. Together, these matrices make up the color image from the
camera. The **Resolution** parameter determines the matrix dimensions.

**Note**

During simulations without hardware, this block outputs zeros. See Block Produces Zeros or Does Nothing in Simulation.
