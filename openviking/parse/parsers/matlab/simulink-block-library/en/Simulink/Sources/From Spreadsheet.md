---
type: simulink-block
title: 'From Spreadsheet'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'fromspreadsheet'
documentation_source_path: 'slref/fromspreadsheet.html'
language: en
---

# From Spreadsheet

## Ports
```yaml
ports:
- name: Port_1
  summary: Data from spreadsheet scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated
```

### Output

### **Port\_1** — Data from spreadsheet scalar | vector | matrix

Incremental data from the specified spreadsheet.

The **Sample time** parameter specifies the sample
time that the From Spreadsheet block uses to read data
from the spreadsheet. For details, see Parameters. The time
stamps in the file must be monotonically nondecreasing.

For each simulation time hit for which the spreadsheet contains no
matching time stamp, Simulink software interpolates or extrapolates to obtain the needed
data using the selected method. For details, see Simulation Time Hits That Have No Corresponding Spreadsheet Time Stamps.

The From Spreadsheet block accepts data type specifications at a block
level. If you want to specify different data types for each signal,
consider selecting **Output Data Type** > **Inherit: Auto**. This option resolves back signal data types using back
propagation. For example, assume that there are two signals in the
From Spreadsheet block, In1 and In2, which the block
sends to ports that have int8 and Boolean data types. With back
propagation, the block recasts In1 as int8 and In2 as Boolean.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
## Parameters
```yaml
parameters:
- name: File name
  summary: Full path and file name untitled.xlsx (default) | full path | relative path
  group: ''
  block_parameter: FileName
  type: character vector
  values: full path and file name
  default: '''untitled.xlsx'''
- name: Sheet name
  summary: Name of sheet in spreadsheet Sheet1 (default) | sheet name
  group: ''
  block_parameter: SheetName
  type: character vector
  values: Sheet name
  default: '''Sheet1'''
- name: Range
  summary: Cell range entire range of used cells in sheet (default) | comma-separated list of column:row
  group: ''
  block_parameter: Range
  type: character vector
  values: entire range of used cells in sheet | comma-separated list of column:row
  default: ''''''
- name: Output data type
  summary: 'Output data type Inherit: auto (default) | double | single | int8 | uint8 | int16 | uint16 | int32 | uint32 |
    int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | Enum: <class_name> | <data type expression>'
  group: ''
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: auto'' | ''double'' | ''single'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32''
    | ''int64'' | ''uint64'' | ''boolean'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''Enum: <class name>'' | ''<data
    type expression>'''
  default: '''Inherit: auto'''
- name: Treat first column as
  summary: Time or data Time (default) | Data
  group: ''
  block_parameter: TreatFirstColumnAs
  type: character vector
  values: '''Time'' | ''Data'''
  default: '''Time'''
- name: Sample time
  summary: Sampling period and offset 0 (default) | scalar | vector
  group: ''
  block_parameter: SampleTime
  type: character vector
  values: scalar | vector
  default: '''0'''
- name: Data extrapolation before first data point
  summary: Extrapolation method for simulation times before initial time stamp in spreadsheet Linear extrapolation (default)
    | Hold first value | Ground value
  group: ''
  block_parameter: ExtrapolationBeforeFirstDataPoint
  type: character vector
  values: '''Linear extrapolation'' | ''Hold first value'' | ''Ground value'''
  default: '''Linear extrapolation'''
- name: Data interpolation within time range
  summary: Interpolation method for simulation times that fall between two time stamps in spreadsheet Linear interpolation
    (default) | Zero order hold
  group: ''
  block_parameter: InterpolationWithinTimeRange
  type: character vector
  values: '''Linear interpolation'' | ''Zero order hold'''
  default: '''Linear interpolation'''
- name: Data extrapolation after last data point
  summary: Extrapolation method for simulation times after last time stamp in spreadsheet Linear extrapolation (default) |
    Hold last value | Ground value
  group: ''
  block_parameter: ExtrapolationAfterLastDataPoint
  type: character vector
  values: '''Linear extrapolation'' | ''Hold last value'' | ''Ground value'''
  default: '''Linear extrapolation'''
- name: Output after last data point
  summary: Action after last data point Repeating sequence (default) | Hold final value | Ground value
  group: ''
  block_parameter: OutputAfterLastPoint
  type: character vector
  values: '''Repeating sequence'' | ''Hold final value'' | ''Ground value'''
  default: '''Repeating sequence'''
- name: Enable zero-crossing detection
  summary: Option to enable zero-crossing detection off (default) | on
  group: ''
  block_parameter: ZeroCross
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Mode
  summary: Category of data to specify Inherit (default) | Built in | Fixed point | Enumerated | Expression
  group: ''
- name: Data type override
  summary: Specify data type override mode for this signal Inherit | Off
  group: ''
- name: Signedness
  summary: Specify signed or unsigned Signed (default) | Unsigned
  group: ''
- name: Scaling
  summary: Method for scaling fixed-point data Binary point (default) | Best precision | Slope and bias
  group: ''
- name: Word length
  summary: Bit size of the word that holds the quantized integer 16 (default) | integer from 0 to 32
  group: ''
- name: Fraction length
  summary: Specify fraction length for fixed-point data type 0 (default) | scalar integer
  group: ''
- name: Slope
  summary: Specify slope for the fixed-point data type 2^0 (default) | positive, real-valued scalar
  group: ''
- name: Bias
  summary: Specify bias for the fixed-point data type 0 (default) | real-valued scalar
  group: ''
```

### **File name** — Full path and file name `untitled.xlsx` (default) | full path | relative path

Enter full path and file name of a spreadsheet file, including the file extension,
specified as a full path or relative path. Note:

This block supports non-English full paths and file names only on
Microsoft platforms.

**Tip**

- You can specify a full-path, relative path, or just the file
  name.

  - With both full path and relative path file names, the
    block supports simulation and code-generation.
  - If the file is not found, the block looks for the file
    in the current folder.
  - With just the file name, the block simulates. However,
    for code-generation, the block caches the full path. If
    the block cannot find the file, it searches in the
    current folder.
- If you do not include a file extension, the block assumes
  `.xlsx` as the extension.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `FileName` |
| **Type**: character vector |
| **Value**: full path and file name |
| **Default**: `'untitled.xlsx'` |

### **Sheet name** — Name of sheet in spreadsheet `Sheet1` (default) | sheet name

Enter the name of the sheet in the spreadsheet. You can type the sheet name in this edit
box or select the sheet name after you open the sheet.

If your spreadsheet is the CSV format, the block populates this parameter with the name
of the CSV file without the extension. Do not change this value.

To open the sheet, click . In the sheet, you can select the range
of data by dragging over the desired range of values.

Alternatively, you can select the range of data by specifying the range of
values in the **Range** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SheetName` |
| **Type**: character vector |
| **Value**: Sheet name |
| **Default**: `'Sheet1'` |

### **Range** — Cell range entire range of used cells in sheet (default) | comma-separated list of `column:row`

To specify the range, use the format
`column:row`,
with multiple specifications separated by commas. For example,
`A1:B3,D1:D3,A7:B9,D7:D9`. If unspecified, or empty,
the block automatically detects the used range, which is all the data in the
sheet.

If the selections overlap, the block resolves the selection information as
appropriate. For example, if you specify multiple ranges that overlap, such
as `A1:B4,B1:E7`, the block resolves the selection to A1 to
E7, inclusive.

**Selection/History** contains the list of selected
ranges during this session. The block does not store the ranges after you
close **Range Selection**.

An alternate to using the **Range** parameter is to open the sheet, by
clicking . In the sheet, you can select the range
of data by dragging over the desired range of values. The range selection
reflects in the **Range** parameter text box.

To apply a new range from the block dialog, click
**Apply**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Range` |
| **Type**: character vector |
| **Value**: entire range of used cells in sheet | comma-separated list of `column:row` |
| **Default**: `''` |

### **Output data type** — Output data type `Inherit: auto` (default) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class_name>` | `<data type expression>`

The data type for the From Spreadsheet block output. The
From Spreadsheet block accepts spreadsheets that contain
many data types. However, the block reads the spreadsheet data type as
doubles. It then outputs the data type according to the value of
**Output data type**.

If you want to specify different data types for each signal, consider
selecting **Output Data Type** > **Inherit: auto**. This option resolves back signal data types using back
propagation. For example, assume that there are two signals in the
From Spreadsheet block, In1 and In2, which the block
sends to ports that have int8 and Boolean data types. With back propagation,
the block recasts In1 as int8 and In2 as boolean.

To allow the block to cast the output data type to match that of the receiving block, use
`Inherit: auto`.

For more information, see Control Data Types of Signals.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: auto' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'Enum: <class name>' | '<data type expression>'` |
| **Default**: `'Inherit: auto'` |

### **Treat first column as** — Time or data `Time` (default) | `Data`

Select how the block should treat the first column of the
spreadsheet:

- `Time` — Treat first column as
  time.
- `Data` — Treat first column as
  data.

#### Dependencies

When you select `Data`, the block
disables:

- **Data extrapolation before first data
  point**
- **Data interpolation within time
  range**
- **Data extrapolation after last data
  point**

And enables:

- **Output after last data point**

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TreatFirstColumnAs` |
| **Type**: character vector |
| **Value**: `'Time' | 'Data'` |
| **Default**: `'Time'` |

### **Sample time** — Sampling period and offset `0` (default) | scalar | vector

The sample period and offset.

The From Spreadsheet block reads data from a spreadsheet using a sample
time that either:

- You specify for the From Spreadsheet block
- The From Spreadsheet block inherits from the blocks into which the
  From Spreadsheet block feeds data

The default is `0`, which specifies a continuous sample
time. The spreadsheet is read at the base (fastest) rate of the model. For
details, see Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'0'` |

### **Data extrapolation before first data point** — Extrapolation method for simulation times before initial time stamp in spreadsheet `Linear extrapolation` (default) | `Hold first value` | `Ground value`

Extrapolation method that Simulink uses for a simulation time hit that is before the first time
stamp in the spreadsheet. Choose one of these extrapolation methods.

| Method | Description |
| --- | --- |
| `Linear extrapolation` | (Default)  If the spreadsheet contains only one sample, the From Spreadsheet block outputs the corresponding data value.  If the spreadsheet contains more than one sample, the From Spreadsheet block linearly extrapolates using the first two samples:  - For `double` data, linearly   extrapolates the value using the first two   samples - For `Boolean` data, outputs   the first data value - For a built-in data type other than   `double` or   `Boolean`:  - Upcasts the data to     `double`   - Performs linear extrapolation (as described     above for `double` data)   - Downcasts the extrapolated data value to the     original data type  You cannot use the `Linear extrapolation` option with enumerated (`enum`) data. |
| `Hold first value` | Uses the first data value in the file |
| `Ground value` | Uses a value that depends on the data type of spreadsheet sample data values:  - Fixed-point data types — Uses the   ground value - Numeric types other than fixed–point —   Uses `0` - `Boolean` — Uses   `false` - Enumerated data types — Uses default   value |

#### Dependencies

To enable this parameter, set **Treat first column
as** to `Time`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `ExtrapolationBeforeFirstDataPoint` |
| **Type:** character vector |
| **Values:** `'Linear extrapolation' | 'Hold first value' | 'Ground value'` |
| **Default:** `'Linear extrapolation'` |

### **Data interpolation within time range** — Interpolation method for simulation times that fall between two time stamps in spreadsheet `Linear interpolation` (default) | `Zero order hold`

The interpolation method that Simulink uses for a simulation time hit between two time stamps in the
spreadsheet. Choose one of the following interpolation methods.

| Method | Description |
| --- | --- |
| `Linear interpolation` | (Default)  The From Spreadsheet block interpolates using the two corresponding spreadsheet samples:  - For `double` data, linearly   interpolates the value using the two corresponding   samples - For Boolean data, if the simulation time is   between two spreadsheet data points with different   values, the From Spreadsheet block   positions the value transition halfway between the   spreadsheet data points. For example, if the   spreadsheet data transitions from true to false,   the From Spreadsheet data provides   an output value of true for simulation times in   the first half of the interval between the   spreadsheet data points. It provides an output   value of false for simulation times in the latter   half of the interval. - For a built-in data type other than   `double` or   `Boolean`:  - Upcasts the data to     `double`   - Performs linear interpolation (as described     above for `double` data)   - Downcasts the interpolated value to the     original data type  You cannot use the `Linear interpolation` option with enumerated (`enum`) data. |
| `Zero order hold` | Uses the data from the first of the two samples |

#### Dependencies

To enable this parameter, set **Treat first column
as** to `Time`.

#### Programmatic Use

|  |
| --- |
| **Parameter:** `InterpolationWithinTimeRange` |
| **Type:** character vector |
| **Values:** `'Linear interpolation' | 'Zero order hold'` |
| **Default:** `'Linear interpolation'` |

### **Data extrapolation after last data point** — Extrapolation method for simulation times after last time stamp in spreadsheet `Linear extrapolation` (default) | `Hold last value` | `Ground value`

The extrapolation method that Simulink uses for a simulation time hit that is after the last time
stamp in the spreadsheet. Choose one of the following extrapolation
methods.

| Method | Description |
| --- | --- |
| `Linear extrapolation` | (Default)  If the spreadsheet contains only one sample, the From Spreadsheet block outputs the corresponding data value.  If the spreadsheet contains more than one sample, the From Spreadsheet block linearly extrapolates using data values of the last two samples:  - For `double` data,   extrapolates the value using the last two   samples - For `Boolean` data, outputs   the last data value - For a built-in data type other than   `double` or   `Boolean`:  - Upcasts the data to     `double`.   - Performs linear extrapolation (as described     above for `double` data).   - Downcasts the extrapolated value to the     original data type.  You cannot use the `Linear extrapolation` option with enumerated (`enum`) data. |
| `Hold last value` | Uses the last data value in the file |
| `Ground value` | Uses a value that depends on the data type of spreadsheet sample data values:  - Fixed-point data types — Uses the   ground value - Numeric types other than fixed–point —   uses `0` - `Boolean` — Uses   `false` - Enumerated data types — Uses default   value |

#### Dependencies

To enable this parameter, set **Treat first column
as** to `Time`.

#### Programmatic Use

|  |
| --- |
| **Parameter:**  `ExtrapolationAfterLastDataPoint` |
| **Type:**  character vector |
| **Values:** `'Linear extrapolation' | 'Hold last value' | 'Ground value'` |
| **Default:** `'Linear extrapolation'` |

### **Output after last data point** — Action after last data point `Repeating sequence` (default) | `Hold final value` | `Ground value`

Select action after last data point:

- `Repeating sequence` — Repeat the
  sequence by reading the data from the first row of the range
  specified in **Range**
- `Hold final value` — Output the last
  defined value for the remainder of the simulation.
- `Ground value` — Output a ground value
  depending on the data type value specified in **Output data
  type**.

#### Dependencies

To enable this parameter, set **Treat first column
as** to `Data`.

#### Programmatic Use

|  |
| --- |
| **Parameter:**  `OutputAfterLastPoint` |
| **Type:**  character vector |
| **Values:** `'Repeating sequence' | 'Hold final value' | 'Ground value'` |
| **Default:** `'Repeating sequence'` |

### **Enable zero-crossing detection** — Option to enable zero-crossing detection `off` (default) | `on`

Select to enable zero-crossing detection.

The Zero-Crossing Detection
parameter applies only if the **Sample time** parameter is
set to `0` (continuous).

This block supports zero-crossing detection only in simulations
that use a variable-step solver. When you use a fixed-step solver for simulation, the software
does not detect or locate zero crossings for this block.

Simulink uses a technique known as zero-crossing detection to locate
accurately a discontinuity, without resorting to excessively small time
steps. In this context, zero-crossing is used to represent
discontinuities.

For the From Spreadsheet block, zero-crossing detection can
only occur at time stamps in the file. Simulink examines only the time stamps, not the data values.

If the input array contains duplicate time stamps (more than one entry
with the same time stamp), Simulink detects a zero crossing at that time stamp. For example,
suppose that the input array has this data.

```
time:     0 1 2 2 3
signal:   2 3 4 5 6
```

At time 2, there is a zero crossing from the input signal
discontinuity.

For data with nonduplicate time stamps, zero-crossing detection depends on
the settings of the following parameters:

- **Data extrapolation before first data
  point**
- **Data interpolation within time range**
- **Data extrapolation after last data
  point**

The block applies the following rules when determining when:

- Zero-crossing occurs for the first time stamp
- For time stamps between the first and last time stamp
- For the last time stamp

| Time Stamp | When Zero-Crossing Detection Occurs |
| --- | --- |
| First | **Data extrapolation before first data point** is set to `Ground value`. |
| Between first and last | **Data interpolation within time range** is set to `Zero-order hold`. |
| Last | One or both of these settings occur:  - **Data extrapolation after last data   point** is set to `Ground   value`. - **Data interpolation within time   range** is set to `Zero-order   hold`. |

The figure illustrates zero-crossing detection for data accessed by a
From Spreadsheet block that has these settings:

- **Data extrapolation before first data point**
  — `Linear extrapolation`
- **Data interpolation within time range** (for
  internal points) — `Zero order
  hold`
- **Data extrapolation after last data point**
  — `Linear extrapolation`

Graph showing no zero crossing at the first point, zero crossing at each internal point, and zero crossing at the last point

The figure illustrates zero-crossing detection for data accessed by a
From Spreadsheet block. The block has these settings for
the time stamps (points):

- **Data extrapolation before first data point**
  — `Hold first value`
- **Data interpolation within time range** —
  `Zero order hold`
- **Data extrapolation after last data point**
  — `Hold last value`

Graph showing no zero crossing at the first point, zero crossing at each internal point, and zero crossing at the last point

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Mode** — Category of data to specify `Inherit` (default) | `Built in` | `Fixed point` | `Enumerated` | `Expression`

Select the category of data to specify. For more information, see Control Data Types of Signals.

- `Inherit`

  Inheritance rule for data types. Selecting
  `Inherit` enables a second menu/text
  box to the right.
- `Built in`

  Built-in data types. Selecting `Built in` enables a second
  menu/text box to the right. Select one of these choices:

  - `double` —
    Default
  - `single`
  - `int8`
  - `uint8`
  - `int16`
  - `uint16`
  - `int32`
  - `uint32`
  - `int64`
  - `uint64`
  - `boolean`
- `Fixed point` — Fixed-point data
  types.
- `Enumerated` — Enumerated data
  types. Selecting `Enumerated` enables a
  second menu/text box to the right, where you can enter the class
  name.
- `Expression` — Expression that
  evaluates to a data type. Selecting
  `Expression` enables a second menu/text
  box to the right, where you enter the expression.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- When you select `Inherit`, Simulink inherits the data
  type override setting from its context, that is, from the block,
  `Simulink.Signal` object or Stateflow® chart in Simulink that is using the signal.
- When you select `Off`, Simulink ignores the data type
  override setting of its context and uses the fixed-point data type specified for
  the signal.

For more information, see Specify Data Types Using Data Type Assistant in the
Simulink documentation.

#### Dependencies

To enable this parameter, set **Mode** to `Built
in` or `Fixed point`.

#### Tips

The ability to turn off data type override for an individual data type provides
greater control over the data types in your model when you apply data type override.
For example, you can use this option to ensure that data types meet the requirements
of downstream blocks regardless of the data type override setting.

### **Signedness** — Specify signed or unsigned `Signed` (default) | `Unsigned`

Specify whether the fixed-point data is signed or unsigned. Signed data can represent
positive and negative values, but unsigned data represents positive values only.

- `Signed`, specifies the fixed-point data as
  signed.
- `Unsigned`, specifies the fixed-point data as
  unsigned.

For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set the **Mode** to `Fixed
point`.

### **Scaling** — Method for scaling fixed-point data `Binary point` (default) | `Best precision` | `Slope and bias`

Specify the method for scaling your fixed-point data to avoid overflow
conditions and minimize quantization errors. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

Setting **Scaling** to `Binary
point` enables:

- **Fraction length**
- **Calculate Best-Precision
  Scaling**

Setting **Scaling** to `Slope and
bias` enables:

- **Slope**
- **Bias**
- **Calculate Best-Precision
  Scaling**

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Fraction length** — Specify fraction length for fixed-point data type `0` (default) | scalar integer

Specify fraction length for fixed-point data type as a positive or
negative integer. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Binary point`.

### **Slope** — Specify slope for the fixed-point data type `2^0` (default) | positive, real-valued scalar

Specify slope for the fixed-point data type. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

### **Bias** — Specify bias for the fixed-point data type `0` (default) | real-valued scalar

Specify bias for the fixed-point data type as any real number. For more
information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.
## Libraries

Simulink / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed pointa` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |
|  |  |
| --- | --- |
| a Supports up to 32-bit fixed-point data types. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- Not recommended for production code.
- Code generation for RSim target provides identical support as Simulink;
  all other code generation targets support only double, one-dimensional, real
  signals in array with time format.
- Simulating in accelerator, rapid accelerator, model reference accelerator
  mode, or model reference rapid accelerator mode behaves the same way, and
  has the same requirements, as simulating in normal mode.
- The From Spreadsheet block does not support generating code
  that involves building ERT or GRT targets, or using SIL or PIL simulation
  modes.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Supports up to 32-bit fixed-point data types.

## Version History

**Introduced in R2015b**

### R2024a: From Spreadsheet Block Updates

The From Spreadsheet now supports relative and full paths for
**File name** for simulation and code
generation. In releases prior to R2024a, if you specified a relative path for
**File name**, the From Spreadsheet block
changed the relative path to the full path during code generation.

### R2022b: From Spreadsheet Searches for Spreadsheet File Within Current Folder

The From Spreadsheet block now searches for the spreadsheet file
within the current folder if it cannot find the spreadsheet file in the full path
provided. This change enables Simulink
Compiler™ standalone executables containing From Spreadsheet
blocks to find spreadsheet files. In previous releases, the From
Spreadsheet block did not look for spreadsheet files in current
folders.

### R2022b: Read Issue with COM

`'LibXL'` is a new value for the `'ReaderLibrary'`
parameter of the `set_param` function.

## Description

Read data from spreadsheet

The From Spreadsheet block reads data from Microsoft®
Excel® (all platforms) or CSV (Microsoft Windows® platform with Microsoft Office installed only) spreadsheets and outputs the data as a signal. The
From Spreadsheet block does not support Microsoft
Excel spreadsheet charts.

The From Spreadsheet icon displays the spreadsheet
file name and sheet name specified in the block **File name** and **Sheet name** parameters.

### Storage Formats

The data that the From Spreadsheet block reads from a spreadsheet
must be appropriately formatted.

For Microsoft
Excel spreadsheets:

- The From Spreadsheet block interprets the first row as a
  signal name. If you do not specify a signal name, the From
  Spreadsheet block assigns a default one with the format
  `Signal #`, where
  *`#`* increments with each additional unnamed
  signal.
- The From Spreadsheet block interprets the first column as
  time. In this column, the time values must monotonically increase.
- The From Spreadsheet block interprets the remaining columns
  as signals.

This example shows an acceptably formatted Microsoft
Excel spreadsheet. The first column is Time and the first row contains
signal names. Each worksheet contains a signal group.

For CSV text files (Microsoft platform with Microsoft Office installed only):

- The From Spreadsheet block interprets the first column as
  time. In this column, the time values must increase.
- The From Spreadsheet block interprets the remaining columns
  as signals.
- Each column must have the same number of entries.
- The From Spreadsheet block interprets each file as one
  signal group.

This example shows an acceptably formatted CSV file. The contents represent one
signal group.

```
0,0,0,5,0
1,0,1,5,0
2,0,1,5,0
3,0,1,5,0
4,5,1,5,0
5,5,1,5,0
6,5,1,5,0
7,0,1,5,0
8,0,1,5,1
9,0,1,5,1
10,0,1,5,0
```

The From Spreadsheet block does not accept signal values of
nonfinite data, such as `Nan`, `Inf`, or
`-Inf`.

### Block Behavior During Simulation

The From Spreadsheet block incrementally reads data from the spreadsheet during simulation.

The **Sample time** parameter specifies the
sample time that the From Spreadsheet block uses to
read data from the spreadsheet. For details, see Parameters. The time stamps in the file must be monotonically nondecreasing.

For each simulation time hit for which the spreadsheet contains
no matching time stamp, Simulink® software interpolates or extrapolates
to obtain the needed data using the selected method. For details,
see Simulation Time Hits That Have No Corresponding Spreadsheet Time Stamps.

### Simulation Time Hits That Have No Corresponding Spreadsheet Time Stamps

If the simulation time hit does not have a corresponding spreadsheet
time stamp, the From Spreadsheet block output depends on:

- Whether the simulation time hit occurs before the first time stamp, within the range of time stamps, or after the last time stamp
- The interpolation or extrapolation methods that you select
- The data type of the spreadsheet data

For details about interpolation and extrapolation options, see the descriptions of these
parameters:

- Data extrapolation before first data point
- Data interpolation within time range
- Data extrapolation after last data point

Sometimes the spreadsheet includes two or more data values that
have the same time stamp. In such cases, the From Spreadsheet block action depends on when the simulation time hit occurs, relative to the duplicate time stamps in the spreadsheet.

For example, suppose that the spreadsheet contains this data.
Three data values have a time stamp value of `2`.

```
time stamps:    0 1 2 2 2 3 4
data values:    2 3 6 4 9 1 5
```

The table describes the From Spreadsheet block output.

| Simulation Time, Relative to Duplicate Time Stamp Values in Spreadsheet | From Spreadsheet Block Action |
| --- | --- |
| Before the duplicate time stamps | Performs the same actions as when the time stamps are distinct, using the first of the duplicate time stamp values as the basis for interpolation. (In this example, the time stamp value is `6`.) |
| At or after the duplicate time stamps | Performs the same actions as when the times stamps are distinct, using the last of the duplicate time stamp values as the basis for interpolation. (In this example, that time stamp value is `9`.) |

### Read Issue with COM

By default, the From Spreadsheet block reads spreadsheets using the
Component Object Model (COM) interface on Windows platforms and the LibXL library on other platforms. If the From
Spreadsheet block has a problem reading the spreadsheet on Windows, use the `set_param` function to set
`'ReaderLibrary'` to `'LibXL'`. For
example:

```
set_param(blockPath,‘ReaderLibrary’,‘LibXL’);
```

where *blockPath* is the model block path.
