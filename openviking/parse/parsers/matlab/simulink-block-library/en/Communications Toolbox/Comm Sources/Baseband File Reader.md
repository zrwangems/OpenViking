---
type: simulink-block
title: 'Baseband File Reader'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources'
documentation_page: 'basebandfilereader'
documentation_source_path: 'ref/basebandfilereader.html'
language: en
---

# Baseband File Reader

## Ports

### Output

### **Data** — Baseband signal scalar | vector | matrix

Baseband signal, returned as a scalar, vector, or matrix. The signal
is read from the file specified by the **Baseband file
name** parameter. The sample time is either inherited from
the file or can be set by the **Sample Time (s)**
parameter.

**Data Types:** `double`
**Complex Number Support:** Yes

### **EOF** — End-of-file indicator logical scalar

End-of-file indicator, returned as a logical scalar. The output is
`true` when the **Repeatedly read the
file** parameter is `false` and the entire
file has been read. To enable this port, select the **Output
end-of-file indicator** parameter.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Baseband file name** — Name of baseband file to read `example.bb` (default) | character vector

Name of the baseband file to read, specified as a string scalar or
character vector.

- Click **Browse** to locate the baseband file
  you want to read.
- Click **File Info** to display this
  information:

  - File name, including absolute path
  - Sample rate
  - Center frequency
  - Number of samples
  - Number of channels
  - Data type
  - Any metadata fields

    - - If the file has no descriptive data, this
        property is an empty structure.
      - If the baseband file writer defined the
        object with a function call, the bb-file stores
        that function call. The baseband file reader
        executes the function call to display the object.

        - If you are licensed to use the software
          associated with that feature, the metadata output
          contains the object contents.
        - If you are not licensed to use the software
          associated with that feature, the metadata output
          contains the string rather than the object
          contents.

### **Inherit sample time from file** — Select source of sample time `on` (default) | `off`

Select this check box to inherit the sample time from the file specified
by **Baseband file name**.

### **Sample time (s)** — Block sample time `1` (default) | positive scalar

Specify the block sample time in seconds as a positive scalar. To enable
this parameter, clear the **Inherit sample time from file**
check box.

### **Samples per frame** — Number of samples per output frame `100` (default) | positive integer scalar

Number of samples per output frame, specified as a positive integer or
`inf`. When this parameter is `inf`,
the output frame contains all of the samples in the baseband file.

### **Repeatedly read the file** — Continuously loop data from file `off` (default) | `on`

Select this check box to repeatedly read the contents of the baseband
file. When the end of the file is reached:

- The block outputs zeros, if the **Repeatedly read the
  file** parameter is not selected
  (`off`).
- The block outputs samples from the beginning of the file, if the
  **Repeatedly read the file** parameter is
  selected (`on`).

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as `Code generation` or
`Interpreted execution`.

- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.
- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option shortens startup time, but the speed
  of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.

For more information, see Interpreted Execution vs. Code Generation (Simulink).

## Libraries

Communications Toolbox / Comm Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2024a: Support reading objects from metadata

The Baseband File Reader block now supports reading objects and
structures-of-structures from the saved metadata.

## Description

Read baseband signals from file

The Baseband File Reader block reads a signal from a baseband file. A baseband
file is a specific type of binary file written by the Baseband File Writer block. Baseband signals are typically downconverted
from a nonzero center frequency to 0 Hz. The block automatically reads the sample rate,
center frequency, number of channels, and any descriptive data.
