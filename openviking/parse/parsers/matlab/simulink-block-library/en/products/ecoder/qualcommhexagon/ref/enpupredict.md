---
type: simulink-block
title: 'eNPU Predict'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Qualcomm Hexagon Processors / Embedded AI / Micro NPU'
documentation_page: 'enpupredict'
documentation_source_path: 'qualcommhexagon/ref/enpupredict.html'
language: en
---

# eNPU Predict

## Ports

### Input

### **Port\_1** — Input data to predict response `N`–dimensional array

The input data, specified as an *N*-dimensional array.
The array must be of the same size specified in the `Input layer
size` parameter of the eAI model.

The eNPU Predict block supports multiple-input multiple-output tensor with a
maximum of four dimensions, but the batch size must always be 1. For example,
if the input layer of the original deep learning network is 128-by-128-by-3,
the input signal dimension must be either 128-by-128-by-3 or
1-by-128-by-128-by-3.

If the leading dimensions are 1 (singleton dimensions), you can remove these
dimensions without affecting compatibility. For example, if the input layer of
an AI model expects an input of size 1-by-1-by-128-by-3, you can specify an
input of size 1-by-1-by-128-by-3 or 128-by-3. You can remove these dimensions
because dimensions of size 1 can be broadcast to match the expected
shape.

The eNPU Predict block accepts either a floating-point (which requires
quantization using other block parameters) or a fixed-point input
signal.

Data type of input signal must match with the eAI model (eAI network file)
if its input layer is of type `int8`, `int16`
or `int32`. If the input signal data type is
`single`, specify the **Input value range [Min
Value, Max Value]** parameter.

**Data Types:** `single` | `int8` | `int16` | `int32`
### Output

### **Port\_2** — Output signal after predicting response `n`–D array

The output tensor specified as an *N*-dimensional array.
The array must be of the same size specified in the `Output layer
size` parameter of the eAI model.

The eNPU Predict block supports a multiple-input multiple-output tensor with
a maximum of four dimensions, but the batch size must always be 1.

Data type of output signal must match with the eAI model (eAI network file)
if its input layer is of type `int8`, `int16`
or `int32`. If the output signal data type is
`single`, select the **Dequantize
output** parameter and specify the **Output value range
[MinValue,MaxValue]** parameter.

**Data Types:** `single` | `int8` | `int16` | `int32`

## Parameters

### **eAI network file** — eAI model to predict responses `<filename>`.eai

Click **Browse** and select the compiled eAI model (eAI
network file) to predict responses. For more information on creating an eAI model
using the eAI Builder tool, refer to the Qualcomm LPAI SDK documentation.

### **Input value range [MinValue,MaxValue]** — Range of input values for min-max quantization of floating-point input `M`-by-2 array

Minimum and maximum range of input values for quantization of floating-point
input, specified as an *M*-by-2 array containing
`M` number of [`min`,`max`]
values, where `M` is the count of input layers.

For example, to quantize both inputs of a tensor layout with two inputs,
specify the value: `[[0, 255];[0,255]]`.

The block supports both symmetric quantization (absolute of minimum and maximum
values are same) and asymmetric quantization (absolute of minimum and maximum
values are different).

**Note**

Specifying a value range for quantization is not required if you are using
the latest LPAI Add-on version 2.5.0.0. Therefore, this parameter is required
only for older versions of LPAI Add-On.

### **Dequantize output** — Option to use output dequantization to predict response off (default) | on

Select this parameter to dequantize the block's output.

### **Output value range [MinValue,MaxValue]** — Range of output values for min-max quantization of floating-point output `M`-by-2 array

Minimum and maximum range of output values for quantization of floating-point
output, specified as an *M*-by-2 array containing
`M` number of [`min`,`max`]
values, where `M` is the count of output layers.

The block supports both symmetric quantization (absolute value of minimum and
maximum values are same) and asymmetric quantization (absolute value of minimum
and maximum values are different).

**Note**

Specifying a value range for quantization is not required if you are using
the latest LPAI Add-on version 2.5.0.0. Therefore, this parameter is required
only for older versions of LPAI Add-On.

#### Dependencies

This parameter appears only if you select **Dequantize
output** checkbox.

### **Use default performance configuration** — Option to use default performance configuration values for eAI client `on` (default) | `off`

Select this parameter to use the default performance configuration values for
the eAI client while obtaining response. The default values as per the LPAI SDK
Addon documentation are:

- Frames per second: 1
- Faster Than Real Time (FTRT) ratio: 10
- Priority level: 3

### **Frames per second** — Number of frames per second `1` (default) | numeric scalar

Number of frames to process per second while predicting response using the eAI
model. For more information, refer to the Qualcomm LPAI SDK documentation.

#### Dependencies

To enable this parameter, clear the **Use default performance
configuration** parameter.

### **Faster Than Real Time (FTRT) ratio** — FTRT ratio `10` (default) | numeric scalar

Ratio to use for faster than real-time performance while predicting response
using the eAI model. For more information, refer to the Qualcomm LPAI SDK
documentation.

#### Dependencies

To enable this parameter, clear the **Use default performance
configuration** parameter.

### **Priority level** — Client priority level for eNPU scheduling `3` (default) | `2` | `1` | `0`

Client priority level for eNPU scheduling while predicting response using the
eAI model. You can specify one of these values with the corresponding priorities:

- 3 – Very low
- 2 – Low
- 1 – Medium
- 0 – High

For more information, refer to the Qualcomm LPAI SDK documentation.

#### Dependencies

To enable this parameter, clear the **Use default performance
configuration** parameter.

### **Real-time processing** — Option to predict response with real-time processing `on` (default) | `off`

Select this parameter to perform real-time processing of input data while
predicting the response.

#### Dependencies

To enable this parameter, clear the **Use default performance
configuration** parameter.

## Libraries

Embedded Coder Support Package for Qualcomm Hexagon Processors / Hexagon / eNPU Library

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2025a**

## Description

Predict responses of eNPU using compiled eAI model

The eNPU Predict block predicts responses by using a compiled embedded
Artificial Intelligence (eAI ) model designed for Qualcomm® eNPU, based on the given input data. The block helps you to simulate and
evaluate the neural network represented in the eAI network file.

Use this block to select a deep learning network represented as an eAI model (eAI
network file) that is generated using the LPAI SDK Addon for Qualcomm Hexagon® SDK. For host simulations, the eNPU Predict block uses the LPAI SDK's host
runtime library in the background to process the input data.

If the input data is of data type `single`, use the input value range
option available in the block to quantize the input as per the selected eAI model.

The output data is quantized by default. To obtain single-precision output, select the
dequantize option in the block and provide the output value range as per the selected eAI
model.

Before predicting the response using the eAI model, you can also use the additional
performance options available in the block to customize some of the performance
configuration parameters of the eAI client. For more information on these parameters, refer
to the Qualcomm LPAI SDK documentation.

**Note**

The eNPU Predict block does not support the `Rapid
Accelerator` simulation mode. When you add the eNPU Predict block to
your model, use the `Normal` or
`Accelerator` modes.

**Note**

To use this block, ensure that you install the LPAI Add-on that is available as part
of Hardware Setup process. For more details, see
