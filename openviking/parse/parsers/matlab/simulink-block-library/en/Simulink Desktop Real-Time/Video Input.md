---
type: simulink-block
title: 'Video Input'
family: 'sldrt'
product_id: 'sldrt'
product_name: 'Simulink Desktop Real-Time'
documentation_release: R2025b
official_category: ''
documentation_page: 'videoinput'
documentation_source_path: 'ref/videoinput.html'
language: en
---

# Video Input

## Ports
```yaml
ports:
- name: ROI Input Data
  summary: Region-of-interest origin coordinates ROI input data
  direction: input
- name: Data
  summary: Video data output RGB data | Luminance data
  direction: output
- name: Frame Ready
  summary: Indicates video frame ready boolean
  direction: output
  data_types: Boolean
- name: Frame Error
  summary: Indicates data acquisition frame error boolean
  direction: output
  data_types: Boolean
- name: Timestamp
  summary: Provides video frame timestamp double
  direction: output
  data_types: double
- name: Missed Ticks
  summary: Missed tick count (optional) double
  direction: output
  data_types: double
```

### Input

### **ROI Input Data** — Region-of-interest origin coordinates ROI input data

If you configure the **ROI origin source** as
`External`, the **ROI Input Data** port is
available on the block. The data input is a vector of ROI origin coordinates. Its
elements correspond to X (horizontal) and Y (vertical) coordinates of the top-left
corner of the ROI area. If the **ROI origin source** is
`Internal`, the ROI origin coordinates are set by the **ROI
origin** parameter.
### Output

### **Data** — Video data output `RGB` data | `Luminance` data

The Data output provides the video data output. The dimensions and format of the
port depend on the configuration of ROI parameters and output format.

If the output format is set to `RGB`, the video data output is an
height x width x 3 matrix of uint8 values. The height and width are height and width
of the ROI area. A value of the output matrix on coordinates [y,x,c] corresponds to a
value of the image on the coordinates [y,x] of the color channel c.

If the output format is set to `Luminance`, the video data output
is an height x width matrix of UINT8 values. The height and width are height and width
of the ROI area. A value of the output matrix on coordinates [y,x] correspond to the
luminance of the pixel on coordinates [y,x].

### **Frame Ready** — Indicates video frame ready boolean

The **Frame Ready** output is a Boolean output, which value is
True (1), if, and only if, the new frame from the camera is ready. If you enable the
**Show "Frame Ready" port** parameter, the **Frame
Ready** port is available on the block.

**Data Types:** `Boolean`

### **Frame Error** — Indicates data acquisition frame error boolean

The **Frame Error** output is a Boolean output. The value is True
(1) if an error has occurred during frame acquisition, and the value is False (0) if
no error occurred. Error conditions include:

- When the acquired frame might be corrupted
- When the ROI area exceeds the frame boundary

If you enable the **Show "Frame Error" port** parameter, the
**Frame Error** port is available on the block.

**Data Types:** `Boolean`

### **Timestamp** — Provides video frame timestamp double

The **Timestamp** output in seconds is a Double output, which
value corresponds to the presentation timestamp of the frame on the video data output.
The frame timestamp is relative to the simulation start. If you enable the
**Show frame timestamp port** parameter, the
**Timestamp** port is available on the block.

**Data Types:** `double`

### **Missed Ticks** — Missed tick count (optional) double

In **Connected IO** mode, returns the number of timer ticks that your model
lags behind the real-time kernel. When the model lags by more than **Maximum missed
ticks**, the software reports an error and simulation stops.

#### Dependency

When you select **Show “Missed Ticks”
port**, this port is visible.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Sample time
  summary: Sample time of block 0.1 (default) | double
  group: ''
  block_parameter: SampleTime
- name: Maximum missed ticks
  summary: Number of timer ticks by which your model can trail the kernel 10 (default) | integer
  group: ''
  block_parameter: MaxMissedTicks
- name: Show “Missed Ticks” port
  summary: Send number of missed ticks to port Missed Ticks 'off' (default) | 'on'
  group: ''
  block_parameter: ShowMissedTicks
- name: Yield CPU when waiting
  summary: Yield CPU while kernel waits for hardware 'off' (default) | 'on'
  group: ''
  block_parameter: YieldWhenWaiting
- name: ROI origin source
  summary: Select region-of-interest origin source Internal (default) | External
  group: ''
  block_parameter: ROIOriginSource
- name: ROI origin
  summary: Select region-of-interest origin [X Y] values [1 1] (default) | 2-element vector
  group: ''
  block_parameter: RoiOrigin
- name: ROI Dimensions
  summary: Select region-of-interest dimensions [W H] values full frame width and height dimensions (default) | [640 480]
    (default if no device configured) | 2-element vector
  group: ''
  block_parameter: RoiDimensions
- name: Frame format
  summary: Select video data format RGB (default) | Luminance
  group: ''
  block_parameter: Channels
- name: Show "Frame Ready" port
  summary: Enable "Frame Ready" output port off (default) | on
  group: ''
  block_parameter: ShowReady
- name: Show "Frame Error" port
  summary: Enable "Frame Error" output port off (default) | on
  group: ''
  block_parameter: ShowError
- name: Show frame timestamp port
  summary: Enable timestamp output port off (default) | on
  group: ''
  block_parameter: ShowTimestamp
```

### **Sample time** — Sample time of block `0.1` (default) | double

Enter a value, in seconds, that represents how frequently you
want the block to execute and interact with the I/O hardware. The
block synchronizes your model with the real-time clock at this sample
rate.

If you are using a fixed-step solver, enter the value that you entered as the **Fixed
step size** configuration parameter or an integer multiple of that
value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |

### **Maximum missed ticks** — Number of timer ticks by which your model can trail the kernel `10` (default) | integer

In **Connected IO** mode, enter the number of timer ticks that your model can
lag behind the real-time kernel. When the model lags behind by this number or fewer timer
ticks, the software assumes that the lag is temporary. It allows the model to catch up, even
if the model misses some ticks. When the model lags by more than this number, the software
reports an error and simulation stops.

In **Run in Kernel** mode, the software ignores this value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `MaxMissedTicks` |

### **Show “Missed Ticks” port** — Send number of missed ticks to port `Missed Ticks` `'off'` (default) | `'on'`

In **Connected IO** mode, select this check box to send the number of missed
ticks to output port `Missed Ticks`.

In **Run in Kernel** mode, the `Missed Ticks` port is
zero.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowMissedTicks` |

### **Yield CPU when waiting** — Yield CPU while kernel waits for hardware `'off'` (default) | `'on'`

In **Connected IO** mode, select this check box to grant other programs more
CPU time while the kernel waits for a response from the hardware.

In **Run in Kernel** mode, the software ignores this value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `YieldWhenWaiting` |

### **ROI origin source** — Select region-of-interest origin source `Internal` (default) | `External`

Select whether the ROI area origin, the pixel coordinates of its top-left corner,
values are controlled by an external source..

- When `Internal` is selected, the origin is controlled by the
  block parameters.
- When `External` is selected, the origin is controlled by the
  block input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ROIOriginSource` |

### **ROI origin** — Select region-of-interest origin [X Y] values `[1 1]` (default) | 2-element vector

The **ROI origin** specifies coordinates of the top-left corner of
ROI area; X for horizontal and Y for vertical. If **ROI origin source**
is configured as `Internal`, the **ROI origin**
2-element vector values to specify the top-left-corner origin point can be selected in
the block parameters dialog box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RoiOrigin` |

### **ROI Dimensions** — Select region-of-interest dimensions [W H] values full frame width and height dimensions (default) | `[640 480]` (default if no device configured) | 2-element vector

The **ROI Dimensions** specify the dimensions of the width-height
of the ROI area for the configured device; W for width and H for height.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RoiDimensions` |

### **Frame format** — Select video data format `RGB` (default) | `Luminance`

The Frame format determines whether the video data are served in RGB format or are
served in luminance format. Changing the output format changes the dimensions of the
output video data signal; `HxWx3` for RGB and `HxW`
for Luminance.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:**`Channels` |

### **Show "Frame Ready" port** — Enable "Frame Ready" output port `off` (default) | `on`

When set to `on`, the block includes a Frame Ready output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowReady` |

### **Show "Frame Error" port** — Enable "Frame Error" output port `off` (default) | `on`

When set to `on`, the block includes a Frame Error output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowError` |

### **Show frame timestamp port** — Enable timestamp output port `off` (default) | `on`

When set to `on`, the block includes a Timestamp output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowTimestamp` |
## Libraries

Simulink Desktop Real-Time

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

### R2024b: Update to blocks with port names

In R2024b, when you enable optional ports, such as **Show "Missed Ticks"
port**, these Simulink®
Desktop Real-Time™ block ports appear with labels.

## Description

Get video data from system video devices

The Video Input block lets you get video data from system video devices.
The camera device support includes support for video input from standard USB video class
devices (webcams). The block also can output video frames status as ready or corrupted, and
include the frame presentation timestamp. You can select the output format and
region-of-interest (ROI).

The block gets the camera resolution from the configuration of the data acquisition board,
for example a system camera that you install by using the block option to **Install new board** > **Standard Devices** > **Camera**.

The device configuration interface for the camera consists of camera ID, frame dimensions
(width and height), and optional luminance channel toggle.

- The camera ID is an integer number greater than or equal to one, specifying order of
  the accessed camera in the system. For example, the first, primary camera listed by the
  system has ID of 1. The camera ID default value is 1.
- The frame width and height determine the required resolution of the video input.
  Maximum allowed resolution is FHD (1920x1080). The default dimensions are VGA (640x480).
- The luminance channel toggle is a checkbox determining if the camera device should
  calculate luminance channel of the video, in addition to the RGB channels. Its default
  value is TRUE (checked).

You can test or accept the configuration by using **Test** and
**OK** buttons. In case the camera configuration is invalid, the test or
setting process fails and shows an error message. The camera configuration can fail for
multiple reasons, for example absence of a camera with specified ID in the system, the
specified resolution not being supported by the camera, or hardware failure.
