---
type: simulink-block
title: 'Frame Rate Display'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Video Loading, Saving, and Display'
documentation_page: 'frameratedisplay'
documentation_source_path: 'ref/frameratedisplay.html'
language: en
---

# Frame Rate Display

## Ports

### Input

### **Port\_1** — Input data matrix | array

Input data, specified as an *M*-by-*N* matrix,
*M*-by-*N*-by-*T* array, or
*M*-by-*N*-by-*C*-by-*T*
array. *T* is the number of frames in a video or image sequence, and
*C* is the number of color channels.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## Parameters

### **Update rate** — Frequency of updates `10` (default) | positive scalar

Specify this parameter to control how often the block updates the display. The block
displays the average update rate across the specified number of video frames. For
example, if this parameter is set to `10`, the Frame Rate
Display block calculates the elapsed time to pass `10` video
frames to the block, divides the elapsed time by `10`, and displays the
average video frame rate.

**Note**

If the input port of Frame Rate Display block is not connected to a
signal, the block displays the base (fastest) rate of the Simulink® model.

## Libraries

Computer Vision Toolbox / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Calculate and display video frame rate

The Frame Rate Display block calculates and displays the average update
rate of an input signal. For an input video signal, this block displays the video frame rate
of the simulation. The calculated rate is in relation to the wall clock time. For example, if
the model is updating the input signal 30 times for every second, this block displays
`30` on the block mask.

This block supports images and video frames as input. Inputs can contain intensity or
color values.
