---
type: simulink-block
title: 'Deep Signal Anomaly Detector'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'AI'
documentation_page: 'deepsignalanomalydetector'
documentation_source_path: 'ref/deepsignalanomalydetector.html'
language: en
---

# Deep Signal Anomaly Detector

## Ports

### Input

### **Input** — Input signal vector | matrix

Specify the input signal through this port as a vector or a matrix.

When the input has multiple channels, the block assumes that the presence of an
anomaly is uniform across all input channels and generates a single-channel output for
anomaly detection.

This port is unnamed until you enable the **Threshold**
port.

**Data Types:** `single` | `double`

### **Threshold** — Detection threshold value nonnegative scalar

Specify the detection threshold value as a nonnegative scalar. The block uses this
value as the threshold for the window loss to detect anomalies.

#### Dependencies

To enable this port, set:

- **Parameters for post-processing** to
  `Specify on dialog`.
- **Threshold source** to `Input
  port`.

**Data Types:** `single` | `double`
### Output

### **Anomaly flag** — Anomaly flag logical scalar

Anomaly flag, returned as a logical scalar:

- `1` –– Anomaly is present in the input data.
- `0` –– No anomaly is present in the input data.

When the input has multiple channels, the block assumes that the presence of an
anomaly is uniform across all input channels, and generates a single-channel output
for the anomaly detection.

The sample time at this port equals *Ts* × *HS*,
where *Ts* is the sample time (or the sample period) at the input
port, and *HS* is the hop size between adjacent windows. Hop size
equals *WL* − *OL*, where *WL* is
the window length and *OL* is the overlap length. For more
information on block samples times, see Sample- and Frame-Based Concepts.

**Data Types:** `Boolean`

### **Window loss** — Aggregate window loss scalar

Aggregate window loss, returned as a scalar. The block computes this value using
the **Window length**, **Overlap length**, and
**Window loss aggregation** parameters.

The block uses the aggregate window loss to detect the anomalies. For more
information, see Algorithms.

The sample time at this port equals *Ts* × *HS*,
where *Ts* is the sample time (or the sample period) at the input
port and *HS* is the hop size between adjacent windows. Hop size
equals *WL* − *OL*, where *WL* is
the window length and *OL* is the overlap length. For more
information on block samples times, see Sample- and Frame-Based Concepts.

**Data Types:** `single`

### **Delay** — Delay estimate scalar

Estimate of the delay between the input and output signals in samples, returned as
a scalar. To align the input data with the anomaly flag and window loss, apply this
delay estimate to the input before further processing. For an example, see Detect Anomalies in Sinusoidal Signal.

The output at this port is always a scalar and the sample time of this port is
always constant.

#### Dependencies

To enable this port, select the **Enable delay port** check box
in the block dialog box.

**Data Types:** `single`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Detector MAT-file path** — Path to detector MAT-file `untitled.mat` (default) | MAT-file name

Specify the path to the MAT-file that you generated using the `saveModel`
function. This MAT-file contains the trained LSTM autoencoder or LSTM forecaster deep
learning network model and parameters used for post-processing such as the window
length, overlap length, detection threshold, and window loss aggregation.

### **Parameters for post-processing** — Source for post-processing parameters `Read from MAT-file` (default) | `Specify on dialog`

Specify the source for the post-processing parameters as one of these:

- `Read from MAT-file` –– The block uses the default
  parameters read from the MAT-file.
- `Specify on dialog` –– Specify the parameters in the
  block dialog box.

The goal of post-processing is to detect the signal anomalies and determine the
window loss that is a measure of how well the block reconstructs the data.

### **Window length** — Window length `1` (default) | positive integer

Specify the window length *WL* the block uses in post-processing as
a positive integer. By default, the block uses a window length of one sample and an
overlap length of zero samples between adjoining windows. This setting detects point
anomalies. Increase the window length to aggregate the window loss over a larger range
of the signal.

#### Dependencies

To enable this parameter, set **Parameters for post-processing**
to `Specify on dialog`.

### **Overlap length** — Overlap length between adjoining windows `0` (default) | nonnegative integer

Specify the overlap length *OL* between adjoining windows as a
nonnegative integer. The block obtains one detection per input sample when
*OL* is *WL* − 1, that is, a hop size of 1 sample.
Hop size is the difference between the window length and overlap length,
*WL* − *OL*. If you want to downsample the output by
a factor of the hop size *HS*, set *OL* to
*WL* − *HS*.

#### Dependencies

To enable this parameter, set **Parameters for post-processing**
to `Specify on dialog`.

### **Threshold source** — Source of detection threshold value `Dialog` (default) | `Input port`

Specify the source of detection threshold as one of these:

- `Dialog` –– Specify the threshold value in the block
  dialog box using the **Threshold** parameter.
- `Input port` –– Specify the threshold value through
  the **Threshold** input port.

#### Dependencies

To enable this parameter, set **Parameters for post-processing**
to `Specify on dialog`.

### **Threshold** — Detection threshold value `0.01` (default) | nonnegative scalar

Specify the detection threshold value as a nonnegative scalar. The block computes
the loss for each window based on the statistic method you specify in the
**Window loss aggregation** parameter. To set the anomaly flag, the
block compares the aggregate window loss to the threshold value you specify in this
parameter. If the window loss is greater than the threshold value, the block sets the
anomaly flag to 1 and sets it to 0 otherwise. A lower threshold value results in the
block classifying more samples as anomalies. Adjust the threshold value based on the
window loss observed in anomalous and non-anomalous regions.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set:

- **Parameters for post-processing** to `Specify
  on dialog`.
- **Threshold source** to
  `Dialog`.

### **Window loss aggregation** — Statistic method to aggregate window loss `Mean` (default) | `Max` | `Min` | `Median`

Specify the statistic method the block uses to aggregate the sample loss in each
window segment as one of these:

- `Mean`
- `Max`
- `Min`
- `Median`

#### Dependencies

To enable this parameter, set **Parameters for post-processing**
to `Specify on dialog`.

### **Parameter values from MAT-file** — Display post-processing parameter values from MAT-file Read-only: text box

This parameter is read-only.

Display the post-processing parameter values the block reads from the MAT-File. The
display parameters are:

- **Window length**
- **Overlap length**
- **Threshold**
- **Window loss aggregation**

Use these values as a baseline if you want to adjust the post-processing parameters
by setting **Parameters for post-processing** to `Specify
on dialog`.

#### Dependencies

To enable this parameter, set **Parameters for post-processing**
to `Read from MAT-file`.

### **Enable delay port** — Output estimated delay `off` (default) | `on`

Select this check box to enable the **Delay** output port. The
block outputs the estimated delay in samples between the input and the reconstructed
signals through this port.

## Libraries

DSP System Toolbox / AI

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports library-free code generation.

## Version History

**Introduced in R2024a**

### R2024b: Support for LSTM forecaster model

The Deep Signal Anomaly Detector block now supports the LSTM forecaster
model. To generate this model, when creating the signal anomaly detector using the `deepSignalAnomalyDetector` function, set `ModelType` to
`"lstmforecaster"`.

## Description

Detect signal anomalies using deep learning network in Simulink

The Deep Signal Anomaly Detector block detects real-time signal anomalies
in Simulink® using a trained long short-term memory (LSTM) autoencoder or a trained long short-term memory (LSTM) forecaster *(since R2024b)* deep learning
network model.

You must first create and train a detector object in MATLAB® using the `deepSignalAnomalyDetector` function, and then configure the block to use this
model in Simulink. To configure the block, specify the path to the detector model in the block
dialog box. For more information on these steps, see User Workflow.

**Note**

This block additionally requires a Deep Learning Toolbox™ license.
