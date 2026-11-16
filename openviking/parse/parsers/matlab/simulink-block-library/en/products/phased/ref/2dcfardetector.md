---
type: simulink-block
title: '2-D CFAR Detector'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection, Range and Doppler Estimation / Detection'
documentation_page: '2dcfardetector'
documentation_source_path: 'ref/2dcfardetector.html'
language: en
---

# 2-D CFAR Detector

## Ports

### Input

### **X** — Input image real *M*-by-*N* matrix | real *M*-by-*N*-by-*P* array

Input image, specified as a real *M*-by-*N* matrix
or real *M*-by-*N*-by-*P* array. *M* and *N* represent
the rows and columns of the matrix. Each page is a different 2-D signal.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

The size of the first dimension of the input matrix can vary to
simulate a changing signal length. A size change can occur, for example, in the case of a pulse
waveform with variable pulse repetition frequency.

**Data Types:** `double`
**Complex Number Support:** Yes

### **idx** — Location of test cells *2*-by-*L* matrix of positive integers

Location of test cells, specified as a *2*-by-*L* matrix
of positive integers, where *L* is the number of
test cells. Each column of `idx` specifies the
row and column index of a CUT cell. The locations of CUT cells are
restricted so that their training regions lie completely within the
input images.

**Data Types:** `double`

### **K** — Detection threshold factor positive scalar

Threshold factor used to calculate the detection threshold,
specified as a positive scalar.

#### Dependencies

To enable this port, set the **Threshold factor method** parameter
to `'Input port'`

**Data Types:** `double`
### Output

### **Y** — Detection results logical matrix (default) | real-valued matrix

Detection results, whose format depends on the `Output
Format` property

- When `OutputFormat` is `'Cut
  result'`, `Y` is a *D*-by-*P* matrix
  containing logical detection results for cells under test. *D* is
  the length of `cutidx` and *P* is
  the number of pages of `X`. The rows of `Y` correspond
  to the rows of `cutidx`. For each row, `Y` contains `1` in
  a column if there is a detection in the corresponding cell in `X`.
  Otherwise, `Y` contains a `0`.
- When `OutputFormat` is `Detection
  index`, `Y` is a *K*-by-*L* matrix
  containing detections indices. *K* is the number
  of dimensions of `X`. *L* is the
  number of detections found in the input data. When `X` is
  a matrix, `Y` contains the row and column indices
  of each detection in `X` in the form `[detrow;detcol]`.
  When `X` is an array, `Y` contains
  the row, column, and page indices of each detection in `X` in
  the form `[detrow;detcol;detpage]`. When the `NumDetectionsSource` property
  is set to `'Property'`, *L* equals
  the value of the `NumDetections` property. If the
  number of actual detections is less than this value, columns without
  detections are set to `NaN`.

**Data Types:** `double`

### **Th** — Computed detection threshold real-valued matrix

Computed detection threshold for each detected cell, returned
as a real-valued matrix. `Th` has the same dimensions
as `Y`.

- When `OutputFormat` is `'CUT
  result'`, `Th` returns the detection threshold
  whenever an element of `Y` is `1` and `NaN` whenever
  an element of `Y` is `0`.
- When `OutputFormat` is `Detection
  index`, `th` returns a detection threshold
  for each corresponding detection in `Y`. When the `NumDetectionsSource` property
  is set to `'Property'`, *L* equals
  the value of the `NumDetections` property. If the
  number of actual detections is less than this value, columns without
  detections are set to `NaN`.

#### Dependencies

To enable this port, select the **Output detection threshold** checkbox.

**Data Types:** `double`

### **N** — Estimated noise power real-valued matrix

Estimated noise power for each detected cell, returned as a
real-valued matrix. `noise` has the same dimensions
as `Y`.

- When `OutputFormat` is `'CUT
  result'`, `noise` returns the noise power
  whenever an element of `Y` is `1` and `NaN` whenever
  an element of `Y` is `0`.
- When `OutputFormat` is `'Detection
  index'`, `noise` returns a noise power
  for each corresponding detection in `Y`. When the `NumDetectionsSource` property
  is set to `'Property'`, *L* equals
  the value of the `NumDetections` property. If the
  number of actual detections is less than this value, columns without
  detections are set to `NaN`.

#### Dependencies

To enable this port, select the **Output estimated noise
power** checkbox.

**Data Types:** `double`

## Parameters

### **CFAR algorithm** — Noise power estimation algorithm `CA` (default) | `GOCA` | `SOCA` | `OS`

Noise power estimation algorithm, specified as `CA`, `GOCA`, `SOCA`,
or `OS`. For `CA`, `GOCA`, `SOCA`,
the noise power is the sample mean derived from the training band.
For `OS`, the noise power is the *k*th
cell value obtained from a numerical ordering of all training cell
values. Set *k* by the **Rank of order statistic** parameter.
See Training cells.

| Averaging Method | Description |
| --- | --- |
| `CA` — Cell-averaging algorithm | Computes the sample mean of all training cells surrounding the CUT cell. |
| `GOCA` — Greatest-of cell-averaging algorithm | Splits the 2-D training window surrounding the CUT cell into left and right halves. Then, the algorithm computes the sample mean for each half and selects the largest mean. |
| `SOCA` — Smallest-of cell-averaging algorithm | Splits the 2-D training window surrounding the CUT cell into left and right halves. Then, the algorithm computes the sample mean for each half and selects the smallest mean. |
| `OS` — Order statistic algorithm | Sorts training cells in ascending order of numeric values. Then the algorithm selects the *k*th value from the list. *k* is the rank specified by the `Rank` parameter. |

### **Rank of order statistic** — Rank of order statistic `1` (default) | positive integer

Specify the rank of the order statistic used in the 2-D CFAR
algorithm as a positive integer. The value of this parameter must
lie between 1 and *Ntrain*,
where *Ntrain* is the number
of training cells. A value of 1 selects the smallest value in the
training region.

#### Dependencies

To enable this parameter, set the **CFAR Algorithm** parameter
to `OS`.

### **Size in cells of the guard region band** — Widths of guard band `[1,1]` (default) | nonnegative integer scalar | 2-element vector of positive integers

The number of row and column guard cells on each side of the
cell under test as nonnegative integers. The first element specifies
the guard band size along the row dimension. The second element
specifies the guard band size along the row dimension. Specifying **Size
in cells of the guard region band** as a scalar is equivalent
to specifying a vector with the same value for both dimensions. For
example, a value of `[1 1]`, indicates that there
is a one-guard-cell-wide region surrounding each CUT cell.

### **Size in cells of the training region band** — Widths of training band `[1,1]` (default) | nonnegative integer scalar | 2-element vector of positive integers

Size in cells of the training region band, specified as a nonnegative
integer or 1-by-2 matrix of nonnegative integers. The first element
specifies the training band size along the row dimension, and the
second along the column dimension. Specifying **Size in cells
of the training region band** as a scalar is equivalent to
specifying a vector with the same value for both dimensions. For example,
a value of `[1 1]` indicates that there is a one-training-cell-wide
region surrounding the guard region for each cell under test.

### **Threshold factor method** — Method to determine threshold factor `Auto` (default) | `Input port` | `Custom`

Method to determine threshold factor, specified as `Auto`, `Input
port`, or `Custom`.

- When you choose `Auto`, the threshold
  factor is determined from the estimated noise statistic and the probability
  of false alarm.
- When you choose `Input Port`, set
  the threshold factor using the `K` input port.
- When you choose `Custom`, set the
  threshold factor using the **Custom threshold factor** parameter.

### **Custom threshold factor** — Custom threshold factor `1` (default) | positive scalar

Custom threshold factor, specified as a positive scalar.

#### Dependencies

To enable this parameter, set the **Threshold factor
method** parameter to `Custom`.

### **Probability of false alarm** — Probability of false alarm `0.1` (default) | real scalar between 0 and 1

Probability of false alarm, specified as a real scalar between
0 and 1. You can calculate the threshold factor from the required
probability of false alarm.

#### Dependencies

To enable this parameter, set the **Threshold factor
method** property to `Auto`.

### **OutputFormat** — Format of detection results `CUT result` (default) | `Detection index`

Format of detection results, specified as `CUT result` or `Detection
index`.

- When set to `'CUT result'`, the detection
  results are logical detection values (`1` or `0`)
  for each tested cell.
- When set to `'Detection index'`,
  the results form a vector or matrix containing the indices of tested
  cells that exceed a detection threshold.

### **Output threshold detection** — Enable detection threshold output off (default) | on

Select this check box to enable the output of detection thresholds via the
`Th` output port.

### **Output estimated noise power** — Enable detection threshold output off (default) | on

Select this check box to enable the output of estimated noise power via
the `N` output port.

### **Source of the number of detections** — Source of the number of detections to report `Auto` (default) | `Property`

Source of the number of detections, specified as
`Auto` or `Property`.
When you select `Auto`, the number of detection
indices reported is the total number of cells under test that have
detections. If you select `Property`, the number of
reported detections is determined by the value of the **Maximum
number of detections** parameter.

#### Dependencies

To enable this parameter, set the **Output format**
parameter to `Detection index`.

**Data Types:** `char`

### **Maximum number of detections** — Maximum number of detection indices to report `1` (default) | positive integer

Maximum number of detection indices to report, specified as a positive
integer.

#### Dependencies

To enable this parameter, set the **Output format**
parameter to `Detection index` and the
**Source of the number of detections** parameter to
`Property`.

**Data Types:** `double`

## Libraries

Phased Array System Toolbox / Detection

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

## Description

Two-dimensional constant false alarm rate (CFAR) detector

The 2-D CFAR Detector block implements a constant
false-alarm rate detector for two dimensional image data. A detection
is declared when an image cell value exceeds a threshold. To maintain
a constant false alarm-rate, the threshold is set to a multiple of
the image noise power. The detector estimates noise power from neighboring
cells surrounding the cell-under-test *(CUT)* using
one of three cell averaging methods, or an order statistics method.
The cell-averaging methods are cell-averaging (CA), greatest-of cell
averaging (GOCA), or smallest-of cell averaging (SOCA).

For each test cell, the detector:

1. estimates the noise statistic from the cell values
   in the training band surrounding the CUT cell.
2. computes the threshold by multiplying the noise estimate
   by the threshold factor.
3. compares the CUT cell value to the threshold to determine
   whether a target is present or absent. If the value is greater than
   the threshold, a target is present.
