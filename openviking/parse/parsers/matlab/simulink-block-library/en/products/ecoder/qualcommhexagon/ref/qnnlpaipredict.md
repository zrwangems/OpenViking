---
type: simulink-block
title: 'QNN LPAI Predict'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Qualcomm Hexagon Processors / Embedded AI / Qualcomm AI Engine Direct'
documentation_page: 'qnnlpaipredict'
documentation_source_path: 'qualcommhexagon/ref/qnnlpaipredict.html'
language: en
---

# QNN LPAI Predict

## Ports

### Input

### **Port\_1** — Input signal to predict response `n`–D array

The input tensor used for inference with the selected QNN model, represented
as an `n`-D array, in accordance with the `Input layer
size` parameter of the QNN model.

The QNN LPAI Predict block supports a multiple-input multiple-output tensor
with a maximum of 4 dimensions, but the batch size must always be 1. For
example, if the input layer of the original deep learning network is
128-by-128-by-3, the input dimension should be either 128-by-128-by-3 or
1-by-128-by-128-by-3.

If the leading dimensions are 1 (singleton dimensions), these dimensions can
often be removed without affecting compatibility. For example, if the input
layer of an AI model expects an input size of 1-by-1-by-128-by-3, the input can
be provided as 1-by-1-by-128-by-3 or simply 128-by-3. This is because
dimensions of size 1 can be broadcast to match the expected shape.

The QNN LPAI Predict block accepts either floating-point input or
fixed-point input. The input datatype must be as per the QNN network's input
layer datatype. Additionally, the input can be floating-point even for
quantized QNN network.

**Data Types:** `single` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Port\_2** — Output signal after inference `n`–D array

The output tensor used for inference with the selected QNN model,
represented as an `n`-D array, in accordance with the QNN
output layer. The output datatypes match the QNN network's output layers'
datatypes. If you select **Dequantize Ouptut**, the output is
always `single`.

**Data Types:** `single` | `half` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## Parameters

### **Host(x86) QNN-model file** — QNN model on host (x-86) to predict responses `<filename>`.dll

Click **Browse** and select the QNN model (in .dll format)
to perform inference. For details on creating an QNN model to run on device
processors like LPAI, refer to Qualcomm AI Engine Direct SDK documentation.

**Note**

This parameter does not appear if the host operating system is Linux® (it appears only for Windows host). In the case of Linux, the
block uses the same context binary file (which you select using the
**Context binary file** parameter) as the host(x86)
QNN-model file also.

### **Context binary file** — QNN context binary file on LPAI backend `<filename>`.bin

Click **Browse** and select the QNN context binary file
(.bin) on the target to perform inference on the host. For details on creating an
binary file to run on device processors like LPAI, refer to Qualcomm AI Engine
Direct SDK documentation.

### **Dequantize output** — Use output dequantization to predict response off (default) | on

Select the checkbox to dequantize the block's output. Enabling this option
results in output data type always being `single`, irrespective
of the deep learning neural network's output layer data type.

## Libraries

Embedded Coder Support Package for Qualcomm Hexagon Processors / Hexagon / QNN

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025b**

## Description

Predict responses of a QNN context binary for the LPAI backend

The QNN LPAI Predict block predicts responses of a deep learning network
represented as a QNN context binary for the LPAI backend of Qualcomm® AI Direct Engine, based on the given input data.

To add the block to your Simulink model, open the model (for example,
`myQNNModel`), and enter this command at the MATLAB
prompt:

```
add_block("mwqnnlib/QNN LPAI Predict","myQNNModel/QNN LPAI Predict")
```

The block allows you to select a QNN model as a compiled shared object (.so) for running
on x86-based host. For the target, you can select a QNN context binary file (.bin) that is
optimized to run on LPAI backend.

The code generated using this block can be deployed to Qualcomm Android Board that is
available under the **Hardware board** parameter in Configuration
Parameters.

The block also provides the option to dequantize outputs to single-precision, if
required.
