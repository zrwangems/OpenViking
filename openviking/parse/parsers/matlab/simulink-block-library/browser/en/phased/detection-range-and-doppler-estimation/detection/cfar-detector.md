---
type: simulink-block
title: 'CFAR Detector'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Signal and Data Processing / Detection, Range, Angle, and Doppler Estimation'
documentation_page: 'cfardetector'
documentation_source_path: '../phased/ref/cfardetector.html'
language: en
---

# CFAR Detector

## Ports

### Input

### **X** — Cell matrix real-valued *M*-by-1 column vector | real-valued *M*-by-*N* matrix

Cell matrix, specified as a real-valued *M*-by-1
column vector or a real-valued
*M*-by-*N* matrix.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `single` | `double`

### **Idx** — Index of cells under test real-valued length-*D* vector

Cells-under-test (CUT), specified as a real-valued length-*D* vector.
Indices specify the input elements or cells under test on which to
perform detection processing. When `X` is a vector,
`Idx` specifies the element. When
`X` is a matrix, `Idx`
specifies the row of the element. The same index applies to all columns
of the matrix. Detection is performed independently along each column of
`Xww` for the indices specified in
`Idx`.

**Data Types:** `double`

### **K** — Threshold factor positive scalar

Threshold factor, used to calculate the detection threshold, specified
as a positive scalar.

#### Dependencies

To enable this port, set the **Threshold factor
method** parameter to `Input
port`.

**Data Types:** `double`
### Output

### **Y** — Detection results *D*-by-1 vector | *D*-by-*N* matrix | *1*-by-*L* | 2-by-*L* matrix

The format of `Y` depends on the **Output
format** property.

- When **Output format** is `'Cut
  result'`, `Y` is a
  *D*-by-1 vector or a
  *D*-by-*N* matrix
  containing logical detection results. *D*
  is the length of `Idx` and
  *N* is the number of columns of
  `X`. The rows of
  `Y` correspond to the rows in
  `Idx`. For each row,
  `Y` contains `1` in
  a column if there is a detection in the corresponding column
  of `X`. Otherwise, `Y`
  contains a `0`.
- When **Output format** is
  `'Detection report'`,
  `Y` is a 1-by-*L*
  vector or a 2-by-*L* matrix containing
  detections indices. *L* is the number of
  detections found in the input data. When
  `X` is a column vector,
  `Y` contains the index for each
  detection in `X`. When
  `X` is a matrix,
  `Y` contains the row and column
  indices of each detection in `X`. Each
  column of `Y` has the form
  `[detrow;detcol]`. When the
  **Source of number of detections**
  property is set to `'Property'`,
  *L* equals the value of the
  **Maximum number of detections**
  parameter. If the number of actual detections is less than
  this value, columns without detections are set to
  `NaN`.

**Data Types:** `double`

### **Th** — Detection threshold scalar

Detection threshold applied to cells under test, returned as a
scalar.

- When **Output format** is `'CUT
  result'`, `Th` port outputs
  the detection threshold whenever an element of
  `Y` is `1` and
  `NaN` whenever an element of
  `Y` is `0`. The
  output of `Th` has the same size as
  `Y`.
- When **Output format** is
  `'Detection index'`, the
  `Th` port outputs a detection
  threshold for each corresponding detection in
  `Y`.When the **Source of
  the number of detections** parameter is set
  to `'Property'`, the number of detections
  is set by the **Maximum number of
  detections** parameter. If the number of actual
  detections is less than this value, the columns without
  detections are set to `NaN`.

#### Dependencies

To enable this port, select the **Output detection
threshold** check box.

**Data Types:** `double`

### **N** — Estimated noise power positive scalar

Estimated noise power for each detected cell under test, returned as a
positive scalar.

- When **Output format** is `'CUT
  result'`, `N` returns a
  noise power estimate when `Y` is
  `1` and `NaN` whenever
  `Y` is zero. The output from port
  `N` has the same size as
  `Y`.
- When **Output format** is
  `'Detection index'`,
  `M` returns a noise power estimate
  for each corresponding detection in `Y`.
  When the **Source of the number of
  detections** property is set to
  `'Property'`, *L*
  equals the value of the **Maximum number of
  detections** parameter. If the number of actual
  detections is less than this value, columns without
  detections are set to `NaN`.

#### Dependencies

To enable this port, select the **Output estimated noise
power** check box.

**Data Types:** `double`

## Parameters

### **CFAR algorithm** — CFAR algorithm `CA` (default) | `GOCA` | `SOCA` | `OS`

Specify the CFAR detection algorithm using one of the values

|  |  |
| --- | --- |
| `CA` | Cell-averaging |
| `GOCA` | Greatest-of cell averaging |
| `OS` | Order statistic |
| `SOCA` | Smallest-of cell averaging |

### **Number of guard cells** — Number of guard cells `2` (default)

Specify the number of guard cells used in training as an even integer.
This parameter specifies the total number of cells on both sides of the cell
under test.

### **Number of training cells** — Number of training cells `2` (default)

Specify the number of training cells used in training as an even integer.
Whenever possible, the training cells are equally divided before and after
the cell under test.

### **Rank of order statistic** — Rank of order statistic `1` (default)

Specify the rank of the order statistic as a positive integer scalar. The
value must be less than or equal to the value of **Number of
training cells**.

#### Dependencies

This parameter appears when **CFAR algorithm** is set
to `OS`.

### **Threshold factor method** — Methods of obtaining threshold factor `Auto` (default) | `Input port` | `Custom`

Specify whether the threshold factor comes from an automatic calculation,
the **Custom threshold factor** parameter, or an input
argument. Values of this parameter are:

|  |  |
| --- | --- |
| `Auto` | The application calculates the threshold factor automatically based on the desired probability of false alarm specified in the **Probability of false alarm** parameter. The calculation assumes each independent signal in the input is a single pulse coming out of a square law detector with no pulse integration. The calculation also assumes the noise is white Gaussian. |
| `Custom` | The **Custom threshold factor** parameter specifies the threshold factor. |
| `Input port` | Threshold factor is set using the input port `K`. This port appears only when **Threshold factor method** is set to `Input port`. |

### **Probability of false alarm** — Desired probability of false alarm `0.1` (default)

Specify the desired probability of false alarm as a scalar between 0 and 1
(not inclusive).

#### Dependencies

This parameter appears only when you set **Threshold factor
method** to `Auto`.

### **Custom threshold factor** — Custom threshold factor `1` (default)

Specify the custom threshold factor as a positive scalar.

#### Dependencies

This parameter appears only when you set **Threshold factor
method** to `Custom`.

### **Output format** — Format of detection results `CUT result` (default) | `Detection index`

Specify the format of detection results returned in output port
`Y` as `CUT result` or
`Detection index`.

- When set to `CUT result`, the results
  are logical detection values (`1` or
  `0`) for each tested cell.
  `1` indicates that the value of the tested
  cell exceeds a detection threshold.
- When set to `Detection index`, the
  results form a vector or matrix containing the indices of tested
  cells which exceed a detection threshold.

### **Output detection threshold** — Output detection threshold off (default) | on

Select this check box to create an output port `Th`
containing the detection threshold.

### **Output estimated noise power** — Output estimated noise power off (default) | on

Select this check box to create an output port `N`
containing the estimated noise.

### **Source of the number of detections** — Source of the number of detections `Auto` (default) | `Property`

Specify the source of the number of detections as
`Auto` or `Property`.
When you select `Auto`, the number of detection
indices reported is the total number of cells under test that have
detections. If you select `Property`, the number of
reported detections is determined by the value of the **Maximum
number of detections** parameter.

#### Dependencies

To enable this parameter, set the **Output format**
parameter to `Detection index`.

### **Maximum number of detections** — Maximum number of detections to report `1` (default)

Specify the maximum number of detection indices to report as a positive
integer.

#### Dependencies

To enable this parameter, set the **Output format**
parameter to `Detection index` and the
**Source of the number of detections** parameter to
`Property`.

### **Simulate using** — Block simulation method `Interpreted Execution` (default) | `Code Generation`

Block simulation, specified as `Interpreted Execution` or
`Code Generation`. If you want your block to use the
MATLAB® interpreter, choose `Interpreted Execution`. If
you want your block to run as compiled code, choose `Code
Generation`. Compiled code requires time to compile but usually runs
faster.

Interpreted execution is useful when you are developing and tuning a model. The block
runs the underlying System object™ in MATLAB. You can change and execute your model quickly. When you are satisfied
with your results, you can then run the block using `Code
Generation`. Long simulations run faster with generated code than in
interpreted execution. You can run repeated executions without recompiling, but if you
change any block parameters, then the block automatically recompiles before
execution.

This table shows how the **Simulate using** parameter affects the
overall simulation behavior.

When the Simulink® model is in `Accelerator` mode, the block mode specified
using **Simulate using** overrides the simulation mode.

**Acceleration Modes**

|  |  |  |  |
| --- | --- | --- | --- |
| Block Simulation | Simulation Behavior | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | The block executes using the MATLAB interpreter. | The block executes using the MATLAB interpreter. | Creates a standalone executable from the model. |
| `Code Generation` | The block is compiled. | All blocks in the model are compiled. |

For more information, see Choosing a Simulation Mode (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SimulateUsing` |
| **Type:** enum |
| **Values:** `Interpreted Execution`, `Code Generation` |
| **Default:** `Interpreted Execution` |

## Libraries

Phased Array System Toolbox / Detection

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Constant false alarm rate (CFAR) detector

The CFAR Detector block implements a one-dimensional constant
false-alarm rate (CFAR) detector. Detection processing is performed on selected elements
(called cells) of the input data. A detection is declared when an image cell value
exceeds a threshold. To maintain a constant false alarm-rate, the threshold is set to a
multiple of the image noise power. The detector estimates noise power for a
cell-under-test *(CUT)* from surrounding cells using one of three
cell averaging methods, or an order statistics method. The cell-averaging methods are
cell averaging (CA), greatest-of cell averaging (GOCA), or smallest-of cell averaging
(SOCA).

For more information about CFAR detectors, see [1].

For each test cell, the detector:

1. estimates the noise statistic from the cell values in the training band
   surrounding the CUT cell.
2. computes the threshold by multiplying the noise estimate by the threshold
   factor.
3. compares the CUT cell value to the threshold to determine whether a target
   is present or absent. If the value is greater than the threshold, a target
   is present.
