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

Not documented in R2025b.

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
