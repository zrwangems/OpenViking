---
type: simulink-block
title: 'Simulation 3D Video Writer'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Simulation 3D / Utilities'
documentation_page: 'simulation3dvideowriter'
documentation_source_path: 'simulation3dvideowriter.html'
language: en
---

# Simulation 3D Video Writer

## Ports

Not documented in R2025b.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Filename** — Name of video file `output.avi` (default) | character vector | string

Specify the name of the video file with file format
as a character vector or string scalar. The video file is saved in the same working
folder where the model is saved. You can also specify the file path along with the
filename to save the video file at a specific location. The block supports these file
extensions.

| File Extension | Description |
| --- | --- |
| `.avi` | AVI file |
| `.mj2` | Motion JPEG 2000 file |
| `.mp4` or `.m4v` | MPEG-4 file (systems with Windows® 7 or later, or macOS 10.7 and later) |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `Filename` |
| **Values:** | `'output.avi'` (default) | character vector | string |
| **Data Types:** | `string` |

**Example:** `set_param(gcb,"Filename","video1.avi")`

### **File action** — How to manage video file `Preserve` (default) | `Overwrite` | character vector | string

Specify how to manage the video file.

| Option | Description |
| --- | --- |
| `Preserve` | Protect existing video files from being overwritten. |
| `Overwrite` | Permit overwriting of the video file. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `FileAction` |
| **Values:** | `'Preserve'` (default) | `'Overwrite'` | character vector | string |
| **Data Types:** | `string` |

**Example:** `set_param(gcb,"FileAction","Overwrite")`

### **Recording interval (s)** — Recording time interval `[0 inf]` (default) | real positive 1-by-2 vector

Specify the recording time interval as a real
positive 1-by-2 vector, in seconds. By default, the recording time interval is the start
time to the end time of the 3D simulation.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` (Simulink) function.

To get the block parameter value
programmatically, use the `get_param` (Simulink) function.

|  |  |
| --- | --- |
| **Parameter:** | `Interval` |
| **Values:** | `[0 inf]` (default) | real positive 1-by-2 vector |
| **Data Types:** | `double` |

**Example:** `set_param(gcb,"Interval","[0 inf]")`

## Libraries

Simulink 3D Animation / Simulation 3D / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Capture 3D simulation as video file

The Simulation 3D Video Writer captures a 3D simulation as a video file with one frame per
step.
