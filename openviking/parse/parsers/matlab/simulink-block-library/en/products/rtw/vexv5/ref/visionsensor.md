---
type: simulink-block
title: 'Vision Sensor'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'visionsensor'
documentation_source_path: 'vexv5/ref/visionsensor.html'
language: en
---

# Vision Sensor

## Ports

### Output

### **Object count** — Number of objects detected by V5 Vision Sensor [1,10]

The number of objects (color blobs) that are detected by V5 Vision Sensor, based
on the selected ID of `Color signature`. One Vision Sensor block can
be used to detect up to 10 objects based on the selected ID.

#### Dependencies

This output depends on the value selected for the **Maximum no. of
objects** parameter.

**Data Types:** `double`

### **X** — X coordinate of the detected color blob based on the field of view pixels | vector

The x coordinate of the color blob (object) based on the field of view, measured
in pixels, as detected by V5 Vision Sensor. If multiple objects (say,
`n`) are detected, this output is a 1-by-`n` array
of values.

**Data Types:** `double`

### **Y** — Y coordinate of the detected color blob based on the field of view pixels | vector

The y coordinate of the color blob (object) based on the field of view, as
detected by V5 Vision Sensor. If multiple objects (say, `n`) are
detected, this output is a 1-by-`n` array of values.

**Data Types:** `double`

### **Width** — Width of the field of view of the detected color blob pixels | vector

The width of the field of view of the color blob, as detected by V5 Vision Sensor.
If multiple objects (say, `n`) are detected, this output is a
1-by-`n` array of values.

**Data Types:** `double`

### **Height** — Height of the field of view of the detected color blob pixels | vector

The height of the field of view of the color blob, as detected by V5 Vision
Sensor. If multiple objects (say, `n`) are detected, this output is a
1-by-`n` array of values.

**Data Types:** `double`

## Parameters

### **Smart Port** — Select the Smart Port to which V5 Vision Sensor is connected 1 (default) | `1` to `21`

Select the Smart Port on the VEX EDR V5 Robot Brain to which the V5 Vision Sensor is connected. There are
21 Smart Ports on the VEX EDR V5 Robot Brain that you can connect to V5 Vision Sensor.

Smart Port must be unique for each block in the model. If multiple Vision Sensor
blocks with the same port are used, the last executed Vision Sensor block may only be
active.

### **Color Signature** — ID of the color signature to detect the object `SIG_1` (default)

Select the ID of the color signature (which you configured using the VEX Vision
Utility) to detect the object. The ID corresponds to the sequence of the color signature
as it appears in the Vision Utility, irrespective of the name that you gave for a
particular signature.

### **Max no. of objects** — Maximum number of objects that the V5 Vision Sensor should try to detect `1` (default)

Select the maximum number of objects that the V5 Vision Sensor should try to detect
based on the selected ID of `Color signature`.

### **Enable display on VEX V5 Brain** — Enable display of detected objects on LCD screen of VEX V5 Robot Brain `1` (default)

Select this option to enable the display of objects (as detected by the V5 Vision
Sensor) on the LCD screen of VEX V5 Robot Brain. The size of the color blobs displayed
in the LCD screen corresponds to the distance of the objects from the V5 Vision Sensor.

### **Sample time** — Interval at which the block reads values `0.2` (default) | positive scalar | -1

Enter the time interval at which the block reads values from the V5 Vision
Sensor.

When you set this parameter to `-1`, Simulink® determines the best sample time for the block based on the block context
within the model.

### Launch V5 Vision Utility

To configure a color signature that you specify in the Vision Sensor block, you need to
use the VEX Vision Utility. Click **Launch V5 Vision Utility** in the
block mask to launch Vision Utility.

For details about saving a color signature on V5 Vision Sensor using the VEX Vision
Utility, see Train V5 Vision Sensor for Color Signature.

### Visualize Detected Objects

To visualize the detected objects on VEX V5 robot brain, select **Enable display
on VEX V5 Brain** on the Vision Sensor block.

A sample screen showing the object detected by Vision Sensor is shown below.

## Libraries

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Represent connected V5 Vision Sensor and read coordinates of color blobs (objects)

The Vision Sensor block represents a V5 Vision Sensor connected to a
specified port on a VEX® EDR V5 Robot Brain, and reads the coordinates of color blobs (objects) detected
by the V5 Vision Sensor. The color blob to detect depends on the ID of the color signature
that you select in this block.

To configure the color signatures, see Launch V5 Vision Utility.
