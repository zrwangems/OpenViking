---
type: simulink-block
title: 'Binary File Reader'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Import and Export'
documentation_page: 'binaryfilereader'
documentation_source_path: 'ref/binaryfilereader.html'
language: en
---

# Binary File Reader

## Ports

### Output

### **data** — Binary file data column vector | row vector | matrix

The reader block reads the binary data from the file specified in the
**File name** parameter. The data output from the
block has dimensions **Samples per
frame**-by-**Number of channels**. The
block can read floating-point data and integer data. The input data can
be real or complex. When the data is complex, the block reads the data
as interleaved real and imaginary components. The reader assumes the
default endianness of the host machine.

This port is unnamed until you select the **Output end-of-file
indicator** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
**Complex Number Support:** Yes

### **EOF** — End-of-file indicator boolean scalar

When the block reaches the end of the file, the port outputs a
`1`. Otherwise, the port outputs a
`0`.

This port is unnamed until you select the **Output end-of-file
indicator** parameter.

**Data Types:** `Boolean`

## Parameters

### **File name** — Name of the file `'Untitled.bin'` (default) | character vector

Name of the file from which the block reads the data. If the file is not
on the MATLAB® path, then specify the full path for the file.

### **File header** — Size of the header `struct([])` (default) | structure

The structure specifies the prototype of the file header, that is, the
size of the header and the data type of the field values. The structure can
have an arbitrary number of fields. Each field of the structure must be a
real matrix of a built-in type. For example, if **File
header** is set to
`struct('field1',1:10,'field2',single(1))`, the block
assumes that the header is formed by 10 real double-precision values
followed by 1 single-precision value. If the file contains no header, you
can set this parameter to an empty structure,
`struct([])`.

### **Export header to base workspace** — Retrieve the header button

To retrieve the file header, click **Export header to base
workspace**. The block exports the file header to the base
workspace.

### **Storage data type** — Storage class of data in file `'double'` (default) | `'single'` | `'int8'` | `'int16'` | `'int32'` | `'int64'` | `'uint8'` | `'uint16'` | `'uint32'` | `'uint64'`

Storage class of data in file, specified as a character vector. This
parameter defines the data type of the matrix the block outputs.

### **Samples per frame** — Number of samples per output frame `1024` (default) | positive integer

**Samples per frame** specifies the number of rows of the
output matrix that the block outputs. The output matrix has dimensions
**Samples per frame**-by-**Number of
channels**. Once the end of the file is reached, the block
returns zeros of the specified data type, size, and complexity.

### **Data is complex** — Specify data complexity off (default) | on

When you select this parameter, the reader treats the data as complex
data. The block reads the data as interleaved real and imaginary components.
Configure the block to read the data as a 2-by-2 matrix. The block reads
`[1 5 2 6 3 7 4 8]` as `[1 2; 3 4]+1j*[5 6; 7
8]`. When you do not select this parameter, the block reads the
data as `[1 5; 2 6]`.

### **Number of channels** — Number of channels `1` (default) | positive integer

**Number of channels** specifies the number of columns of
the output matrix that the block outputs. This parameter defines the number
of consecutive interleaved data samples stored in the file for each time
instant. The size of the data is **Samples per
frame**-by-**Number of channels**. Once the
end of the file is reached, if the output matrix is not full, the block
fills the matrix with zeros to make it a full-sized matrix.

### **Output end-of-file indicator** — End-of-file indicator off (default) | on

When you select this parameter, an additional output port named
**EOF** appears on the block. When the block reaches
the end of the file, the port outputs a `1`. Otherwise, the
port outputs a `0`.

### **Sample time (s)** — Sample time 1 (default) | nonnegative scalar

**Sample time (s)** controls the sample time at the
output port of the block. This value represents 1/*Fs*, where *Fs* is the sampling rate of the signal data. The Simulink sample time at the output port is **Samples per
frame** × **Sample time (s)**.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.

## Libraries

DSP System Toolbox / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

## Description

Read data from binary files

The Binary File Reader block reads multichannel signal data from a
binary file. The block reads the header that precedes the data. The **File
header** parameter specifies the structure of the header. You can specify
the type, size, and complexity of the data through the block parameters. You can also
export the header to the base workspace by clicking on the **Export header to
base workspace** button.

The first time you read the file, the reader reads the header, followed by the data.
On subsequent calls, the reader reads the remaining data. Once the end of the file is
reached, the reader returns zeros of the specified data type, size, and complexity. The
reader can read signal data from a binary file that is not created by the Binary File Writer block.
