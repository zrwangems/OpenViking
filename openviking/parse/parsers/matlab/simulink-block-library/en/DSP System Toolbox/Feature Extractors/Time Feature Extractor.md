---
type: simulink-block
title: 'Time feature extractor'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Feature Extractors'
documentation_page: 'timefeatureextractor'
documentation_source_path: 'ref/timefeatureextractor.html'
language: en
---

# Time feature extractor

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal vector | matrix
  direction: input
  data_types: single | double
- name: Port_1
  summary: Extracted features vector | 3-D array
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Input signal vector | matrix

Specify the input signal as a vector or as a matrix. Specify real- or
complex-valued multichannel inputs of the size
*m*-by-*n*, where *m* ≥ 1 is the
signal length, and *n* ≥ 1 is the number of channels.

The block supports complex-valued signals at this port except when you enable the
`SINAD`, `SNR`, and `THD`
features.

**Data Types:** `single` | `double`
### Output

### **Port\_1** — Extracted features vector | 3-D array

Extracted features, returned as a vector or 3-D array.

- For a single-channel input signal specified as a vector with
  *m* elements, the block returns the extracted features as a
  1-by-*r* vector, where *r* is the number of
  features extracted from the signal
- For an *n*-channel input signal specified as a matrix of
  size *m*-by-*n*, the block returns the
  extracted features as a 1-by-*r*-by-*n* array,
  where *r* is the number of features extracted from the
  signal.

Each column of the output signal corresponds to a different feature
extracted from the input signal. For more information, see the `Feature to
output mapping` parameter.

The sample time at this port equals *Ts* × *HS*,
where *Ts* is the sample time (or the sample period) at the input
port, and *HS* is the **hop size** between
adjacent windows. Hop size equals *WL* − *OL*, where
*WL* is the **window length** and
*OL* is the **overlap length**. For more
information on block sample times, see Sample- and Frame-Based Concepts.

**Data Types:** `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Window length
  summary: Number of samples per frame 64 (default) | positive integer
  group: ''
- name: Specify
  summary: Buffering method Overlap length (default) | Hop size
  group: ''
- name: Overlap length
  summary: Number of overlapping samples between consecutive frames 0 (default) | positive integer
  group: ''
- name: Hop size
  summary: Number of samples between the start of frames 64 (default) | positive integer
  group: ''
- name: Mean
  summary: Option to extract mean on (default) | off
  group: ''
- name: RMS
  summary: Option to extract root mean square off (default) | on
  group: ''
- name: Standard deviation
  summary: Option to extract standard deviation off (default) | on
  group: ''
- name: Shape factor
  summary: Option to extract shape factor off (default) | on
  group: ''
- name: SNR
  summary: Option to extract signal-to-noise ratio off (default) | on
  group: ''
- name: THD
  summary: Option to extract total harmonic distortion off (default) | on
  group: ''
- name: SINAD
  summary: Option to extract signal to noise and distortion ratio off (default) | on
  group: ''
- name: Peak value
  summary: Option to extract peak value off (default) | on
  group: ''
- name: Crest factor
  summary: Option to extract crest factor off (default) | on
  group: ''
- name: Clearance factor
  summary: Option to extract clearance factor off (default) | on
  group: ''
- name: Impulse factor
  summary: Option to extract impulse factor off (default) | on
  group: ''
- name: Feature to output mapping
  summary: Display column indices of features in output section
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

#### Signal buffering

### **Window length** — Number of samples per frame `64` (default) | positive integer

Specify the number of samples per frame as a positive integer. The block divides the
signal into frames of the specified length and extracts features for each frame.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Specify** — Buffering method `Overlap length` (default) | `Hop size`

Specify the buffering method as one of these:

- `Overlap length` — Number of overlapping samples
  between consecutive frames
- `Hop size` — Number of samples between the start of
  frames

### **Overlap length** — Number of overlapping samples between consecutive frames `0` (default) | positive integer

Specify the number of overlapping samples between consecutive frames as a
nonnegative integer less than the window length.

#### Dependencies

To enable this parameter, set **Specify** to `Overlap
length`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Hop size** — Number of samples between the start of frames `64` (default) | positive integer

Specify the number of samples between the start of frames as a positive
integer.

#### Dependencies

To enable this parameter, set **Specify** to `Hop
size`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

#### Features to extract

### **Mean** — Option to extract mean `on` (default) | `off`

Select this parameter to extract the mean value of the input signal.

If you select this parameter, the feature-extractor block enables this feature for
extraction, extracts this feature, and concatenates it with all the other features that
you enable in the block.

For more information about the mean feature, see `mean`.

### **RMS** — Option to extract root mean square `off` (default) | `on`

Select this parameter to extract the root mean square (RMS) of the input
signal.

If you select this parameter, the feature-extractor block enables this feature for
extraction, extracts this feature, and concatenates it with all the other features that
you enable in the block.

For more information about the root mean square feature, see `rms`.

### **Standard deviation** — Option to extract standard deviation `off` (default) | `on`

Select this parameter to extract the standard deviation of the input signal.

If you select this parameter, the feature-extractor block enables this feature for
extraction, extracts this feature, and concatenates it with all the other features that
you enable in the block.

For more information about the standard deviation feature, see `std`.

### **Shape factor** — Option to extract shape factor `off` (default) | `on`

Select this parameter to extract the shape factor of the input signal. The shape
factor is equal to the RMS value divided by the mean absolute value of the
signal.

If you select this parameter, the feature-extractor block enables this feature for
extraction, extracts this feature, and concatenates it with all the other features that
you enable in the block.

### **SNR** — Option to extract signal-to-noise ratio `off` (default) | `on`

Select this parameter to extract the signal-to-noise ratio (SNR) of the input
signal.

If you select this parameter, the feature-extractor block enables this feature for
extraction, extracts this feature, and concatenates it with all the other features that
you enable in the block.

**Note**

You must specify a real-valued input signal to extract this feature.

For more information about the signal-to-noise ratio feature, see `snr`.

### **THD** — Option to extract total harmonic distortion `off` (default) | `on`

Select this parameter to extract the total harmonic distortion (THD) of the input
signal.

If you select this parameter, the feature-extractor block enables this feature for
extraction, extracts this feature, and concatenates it with all the other features that
you enable in the block.

**Note**

You must specify a real-valued input signal to extract this feature.

For more information about the total harmonic distortion feature, see `thd`.

### **SINAD** — Option to extract signal to noise and distortion ratio `off` (default) | `on`

Select this parameter to extract the signal to noise and distortion ratio (SINAD) in
decibels of the input signal.

If you select this parameter, the feature-extractor block enables this feature for
extraction, extracts this feature, and concatenates it with all the other features that
you enable in the block.

**Note**

You must specify a real-valued input signal to extract this feature.

For more information about the signal to noise and distortion ratio feature, see
`sinad`.

### **Peak value** — Option to extract peak value `off` (default) | `on`

Select this parameter to extract the peak value of the input signal.

The peak value corresponds to the largest absolute value of the signal.

If you select this parameter, the feature-extractor block enables this feature for
extraction, extracts this feature, and concatenates it with all the other features that
you enable in the block.

### **Crest factor** — Option to extract crest factor `off` (default) | `on`

Select this parameter to extract the crest factor of the input signal.

If you select this parameter, the feature-extractor block enables this feature for
extraction, extracts this feature, and concatenates it with all the other features that
you enable in the block.

The crest factor is equal to the peak value divided by the RMS value of the signal.
For more information about the crest factor feature, see `peak2rms`.

### **Clearance factor** — Option to extract clearance factor `off` (default) | `on`

Select this parameter to extract the clearance factor of the input signal.

If you select this parameter, the feature-extractor block enables this feature for
extraction, extracts this feature, and concatenates it with all the other features that
you enable in the block.

The clearance factor is equal to the peak value divided by the squared mean of the
square roots of the absolute amplitude of the signal.

### **Impulse factor** — Option to extract impulse factor `off` (default) | `on`

Select this parameter to extract the impulse factor of the input signal.

If you select this parameter, the feature-extractor block enables this feature for
extraction, extracts this feature, and concatenates it with all the other features that
you enable in the block.

The impulse factor is equal to the peak value divided by the mean of the absolute
amplitude.

### **Feature to output mapping** — Display column indices of features in output section

Expand this section to display the column index of each feature in the output. Each
feature extracted from the input signal appears in a separate column of the output. For
each feature listed in the **Feature** section of the table, the
corresponding entry in the **Column index in output** section displays
the column index where the feature appears in the output signal.
## Libraries

DSP System Toolbox / Feature Extractors

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

## Version History

**Introduced in R2025a**

## Description

Extract time-domain features from signals

The Time Feature Extractor block extracts time-domain features
from a signal. You can extract these time-domain features: mean, root mean square (RMS),
standard deviation, shape factor, signal-to-noise ratio (SNR), total harmonic distortion
(THD), signal to noise and distortion ratio (SINAD), peak value, crest factor, clearance
factor, and impulse factor.
