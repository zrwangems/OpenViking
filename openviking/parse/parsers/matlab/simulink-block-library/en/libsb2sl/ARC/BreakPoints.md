---
type: simulink-block
title: 'n-D Lookup Table'
family: 'libsb2sl'
product_id: 'libsb2sl'
product_name: 'libsb2sl'
documentation_release: R2025b
official_category: 'ARC'
documentation_page: 'ndlookuptable'
documentation_source_path: '../simulink/slref/ndlookuptable.html'
language: en
---

# n-D Lookup Table

## Ports

### Input

### **u1** — First-dimension (row) inputs scalar | vector | matrix

Real-valued inputs to the **u1** port, mapped to an output value
by looking up or interpolating the table of values that you define.

**Example:** `0:10`

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

### **uN** — n-th dimension input values scalar | vector | matrix

Real-valued inputs to the **uN** port, mapped to an output value
by looking up or interpolating the table of values that you define.

**Example:** `0:10`

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

### **T** — Define the table of output values matrix of values with dimensions that match the **Number of table dimensions** and the breakpoint lengths for each dimension of the table

Specify the table of output values with a signal that is tunable at
runtime.

During simulation, the matrix size must match the dimensions defined by the
**Number of table dimensions** parameter. However, during block
diagram editing, you can enter an empty matrix (specified as `[]`) or
an undefined workspace variable. This technique lets you postpone specifying a
correctly dimensioned matrix for the table data and continue editing the block
diagram.

#### Dependencies

To enable this port, set:

- **Data specification** to `Table and
  breakpoints`.
- **Table data** to `Input
  port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **bp1** — Explicit breakpoint values 1-by-n or n-by-1 vector of monotonically increasing values

Specify the breakpoint data explicitly, based on the value of the **Breakpoints
specification** parameter, with a signal that is tunable at
runtime.

- If you set **Breakpoints specification** to
  `Explicit values`, enter the breakpoint vector that
  corresponds to each dimension of table data in each
  **Breakpoints** row. For each dimension, specify breakpoints as
  a 1-by-n or n-by-1 vector whose values are strictly monotonically
  increasing.

You can create up to three breakpoint data input ports. For breakpoints 4 to 30,
you can specify breakpoint data only through the corresponding
**Breakpoints** parameter.

**Note**

To specify breakpoints in the even spacing specification format, set
**Breakpoints specification** to `Even
spacing` and use the **Breakpoints First** point and
**Spacing** parameters.

#### Dependencies

To enable this port, set:

- **Data specification** to `Table and
  breakpoints`.
- **Breakpoints specification** to `Explicit
  values`.
- **Breakpoints 1** to `Input
  port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

### **bp2** — Explicit breakpoint values 1-by-n or n-by-1 vector of monotonically increasing values

Specify the breakpoint data explicitly, based on the value of the
**Breakpoints specification** parameter, with a signal that is
tunable at runtime.

- If you set **Breakpoints specification** to
  `Explicit values`, enter the breakpoint vector that
  corresponds to each dimension of table data in each
  **Breakpoints** row. For each dimension, specify breakpoints as
  a 1-by-n or n-by-1 vector whose values are strictly monotonically
  increasing.

You can create up to three breakpoint data input ports. For breakpoints 4 to 30,
you can specify breakpoint data only through the corresponding
**Breakpoints** parameter.

**Note**

To specify evenly spaced breakpoint data, use the
**Breakpoints** parameter. You cannot specify evenly spaced
breakpoint data through the input port.

#### Dependencies

To enable this port, set:

- **Data specification** to `Table and
  breakpoints`.
- **Breakpoints specification** to `Explicit
  values`.
- **Breakpoints 2** to `Input
  port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`

### **bp3** — Explicit breakpoint values 1-by-n or n-by-1 vector of monotonically increasing values

Specify the breakpoint data explicitly, based on the value of the
**Breakpoints specification** parameter, with a signal that is
tunable at runtime.

- If you set **Breakpoints specification** to
  `Explicit values`, enter the breakpoint vector that
  corresponds to each dimension of table data in each
  **Breakpoints** row. For each dimension, specify breakpoints as
  a 1-by-n or n-by-1 vector whose values are strictly monotonically
  increasing.

You can create up to three breakpoint data input ports. For breakpoints 4 to 30,
you can specify breakpoint data only through the corresponding
**Breakpoints** parameter.

**Note**

To specify evenly spaced breakpoint data, use the
**Breakpoints** parameter. You cannot specify evenly spaced
breakpoint data through the input port.

#### Dependencies

To enable this port, set:

- **Data specification** to `Table and
  breakpoints`.
- **Breakpoints specification** to `Explicit
  values`.
- **Breakpoints 3** to `Input
  port`.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `enumerated` | `fixed point`
### Output

### **Port\_1** — Output computed by looking up or estimating table values scalar | vector | matrix

Output generated by looking up or estimating table values based on the input
values:

| When block inputs... | The n-D Lookup Table block... |
| --- | --- |
| Match the values of indices in breakpoint vectors | Outputs the table value at the intersection of the row, column, and higher dimension breakpoints |
| Do not match the values of indices in breakpoint vectors, but are within range | Interpolates appropriate table values, using the **Interpolation method** you select |
| Do not match the values of indices in breakpoint vectors, and are out of range | Extrapolates the output value, using the **Extrapolation method** you select |

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### Table and Breakpoints

### **Number of table dimensions** — Number of lookup table dimensions `3` (default) | `1` | `2` | `4` | `...` | `30`

Enter the number of dimensions of the lookup table. This parameter
determines:

- The number of independent variables for the table and the
  number of block inputs
- The number of breakpoint vectors to specify

| Value | Setting |
| --- | --- |
| 1, 2, 3, or 4 | Select the value from the drop-down list. |
| A higher number of table dimensions | Enter a positive integer directly in the field.  The maximum number of table dimensions that this block supports is 30. |

For example, a table with a size of *M* x
*N* x ... means that the size of dimension 1 is
*M*, the size of dimension 2 is
*N*, and so forth. *M* must match
the first breakpoint length, *N* must match the second
breakpoint length, and so forth.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfTableDimensions` |
| **Type:** character vector |
| **Values:** `'1' | '2' | '3' | '4' | ... | 30` |
| **Default:** `'3'` |

### **Data specification** — Method of table and breakpoint specification `Table and breakpoints` (default) | `Lookup table object`

From the list, select:

- `Table and breakpoints` —
  Specify the table data and breakpoints. Selecting this option
  enables the following parameters:

  - **Table data**
  - **Breakpoints
    specification**
  - **Breakpoints 1**
  - **Breakpoints 2**
  - **Breakpoints 3**
  - **Edit table and
    breakpoints**

  To specify the table and breakpoints using input ports, see
  the **Source** parameter.
- `Lookup table object` — Use an
  existing lookup table (`Simulink.LookupTable`) object. Selecting this
  option enables the **Name** field and
  **Edit table and breakpoints**
  button.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DataSpecification` |
| **Type:** character vector |
| **Values:** `'Table and breakpoints' | 'Lookup table object'` |
| **Default:** `'Table and breakpoints'` |

To set this parameter from `'Table and breakpoints'` to
`'Lookup table object'`, use the same
`set_param` call to set the
`LookupTableObject` parameter. For
example:

```
set_param('myModel/myLookupBlock',...
   'DataSpecification','Lookup table object',...
   'LookupTableObject','myLUTObject')
```

### **Name** — Name of the lookup table object `[]` (default) | `Simulink.LookupTable` object

Enter the name of the lookup table (`Simulink.LookupTable`) object. If a `Simulink.LookupTable` object does not exist,
click the action button  and select
**Create**. The corresponding parameters of the
new lookup table object are automatically populated with the block
information.

#### Dependencies

To enable this parameter, set **Data
specification** to `Lookup table
object`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LookupTableObject` |
| **Type:** character vector |
| **Values:** name of a `Simulink.LookupTable` object |
| **Default:** `''` |

### **Breakpoints specification** — Method of breakpoint specification `Explicit values` (default) | `Even spacing`

Specify whether to enter data as explicit breakpoints or as parameters
that generate evenly spaced breakpoints.

- To explicitly specify breakpoint data, set this parameter to
  `Explicit values` and enter
  breakpoint data in the text box next to the
  **Breakpoints** parameters.
- To specify parameters that generate evenly spaced breakpoints,
  set this parameter to `Even spacing`
  and enter values for the **First point** and
  **Spacing** parameters for each dimension
  of breakpoint data. The block calculates the number of points to
  generate from the table data.

#### Dependencies

- To enable this parameter, set **Data
  specification** to `Table and
  breakpoints`.
- When this parameter is set to `Even
  spacing`, you can only specify breakpoint
  data through the dialog.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsSpecification` |
| **Type:** character vector |
| **Values:** `'Explicit values' | 'Even spacing'` |
| **Default:** `'Explicit values'` |

### **Support tunable size** — Option to enable tunable table size `off` (default) | `on`

Select this check box to enable tunable table sizing of the active
region while the simulation is running or the generated code is
executing. This option enables the software to work properly
even if you change the size of the active region and values of
the lookup table and breakpoint data while the generated code is
executing. The table size must be 2 or greater and less than the
maximum tunable size.

#### Dependencies

If you set **Interpolation method** to `Cubic spline` or `Akima spline`, **Support tunable size** is not available.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SupportTunableSize` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Source** — Source of table and breakpoint data `Dialog` (default) | `Input port`

Specify the source of the table and breakpoint data as:

- `Dialog` — Specify the table or
  breakpoint data in **Value** parameter.
- `Input port` — Specify the table or
  breakpoint data through the associated input port.

  You can create up to three breakpoint data input ports. For
  breakpoints 4 to 30, you can specify breakpoint data only
  through the corresponding **Breakpoints**
  parameter.

**Note**

Using the input port to specify table or breakpoint data might
negatively affect block performance for simulation due to runtime
checks. To model dynamics that require breakpoints to change during
simulation, select `Dialog` and change the
breakpoint data using the Parameter Writer block.

#### Dependencies

- To enable this parameter, set **Data
  specification** to `Table and
  breakpoints`.
- To enable the associated **Value**, set
  this parameter to `Dialog`.
- To enable the associated input port, set this parameter to
  `Input port`.
- Setting this parameter to `Input
  port` disables the
  **Value** field and hides the
  corresponding parameter on the **Data
  Types** tab.
- Setting this parameter to `Input
  port` for any one of the parameters
  disables the **Edit Table and Breakpoints**
  button.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableSource` | `BreakpointsForDimension1Source` | `BreakpointsForDimension2Source` | `BreakpointsForDimension3Source` |
| **Type:** character vector |
| **Values:** `Dialog` | `Input port` |
| **Default:** `'Dialog'` |

### **Tunable size** — Maximum number of elements for each array `-1` (default) | real integer scalar

Specify the maximum size of each array as one of these values:

- `-1` — All of the elements in the array
- Real integer scalar — Maximum number of elements for each array

**Tunable size** must be less than or equal to the size of the
array.

#### Dependencies

To enable this parameter:

- Set **Data specification** to `Table and breakpoints`.
- Select the **Support tunable size** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `N1` to `N31` |
| **Type:** character vector |
| **Values:** `-1` | real integer scalar |
| **Default:** `-1` |

### **Table data** — Define the table of output values `reshape(repmat([4 5 6;16 19 20;10 18 23],1,2),[3,3,2])` (default) | matrix of values with dimensions that match the **Number of table dimensions**

Enter the table of output values in the associated
**Value** field.

During simulation, the matrix size must match the dimensions defined
by the **Number of table dimensions** parameter.
However, during block diagram editing, you can enter an empty matrix
(specified as `[]`) or an undefined workspace variable.
This technique lets you postpone specifying a correctly dimensioned
matrix for the table data and continue editing the block diagram.

#### Dependencies

To enable this parameter, set:

- **Data specification** to
  `Table and breakpoints`.
- **Table data: Source** to
  `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Table` |
| **Type:** character vector |
| **Values:** matrix of table values |
| **Default:** `'reshape(repmat([4 5 6;16 19 20;10 18 23],1,2),[3,3,2])'` |

### **Breakpoints** — Explicit breakpoint values or first point and spacing of breakpoints `[10,22,31]` (default) | 1-by-n or n-by-1 vector of monotonically increasing values

Specify the breakpoint data explicitly or as evenly-spaced
breakpoints, based on the value of the **Breakpoints
specification** parameter.

- If you set **Breakpoints specification** to
  `Explicit values`, enter the
  breakpoint vector that corresponds to each dimension of table
  data in each **Breakpoints** row in the
  associated **Value** field. For each dimension,
  specify breakpoints as a 1-by-n or n-by-1 vector whose values
  are strictly monotonically increasing.
- If you set **Breakpoints specification** to
  `Even spacing`, enter the
  parameters **First point** and
  **Spacing** in each
  **Breakpoints** row to generate
  evenly-spaced breakpoints in the respective dimension. Your
  table data determines the number of evenly spaced points.

#### Dependencies

- To enable this parameter, set:

  - **Data specification** to
    `Table and
    breakpoints`.
  - **Table data: Source** to
    `Dialog`.
- When the **Breakpoints specification**
  parameter is set to `Even spacing`,
  you can only specify breakpoint data through the
  dialog.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsForDimension1` | `BreakpointsForDimension2` | ... | `BreakpointsForDimension30` |
| **Type:** character vector |
| **Values:** 1-by-n or n-by-1 vector of monotonically increasing values |
| **Default:** `'[10, 22, 31]'` | `'[10, 22, 31]'` | … | `'[1:3]'` |

### **First point** — First point in evenly spaced breakpoint data `1` (default) | scalar

Specify the first point in your evenly spaced breakpoint data as a
real-valued, finite scalar. This parameter is available when
**Breakpoints specification** is set to
`Even spacing`.

#### Dependencies

To enable this parameter, set **Data
specification** to `Table and
breakpoints`, and **Breakpoints
specification** to `Even
spacing`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsForDimension1FirstPoint | BreakpointsForDimension2FirstPoint | ... | BreakpointsForDimension30FirstPoint` |
| **Type:** character vector |
| **Values:** real-valued, finite, scalar |
| **Default:** `'1'` |

### **Spacing** — Spacing between evenly spaced breakpoints `1` (default) | scalar

Specify the spacing between points in your evenly-spaced breakpoint
data.

#### Dependencies

To enable this parameter, set **Data
specification** to `Table and
breakpoints`, and **Breakpoints
specification** to `Even
spacing`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsForDimension1Spacing | BreakpointsForDimension2Spacing | ... | BreakpointsForDimension30Spacing` |
| **Type:** character vector |
| **Values:** positive, real-valued, finite, scalar |
| **Default:** `'1'` |

### **Edit table and breakpoints** — Open Lookup Table Editor dialog box button

Click this button to open the Lookup Table Editor. For more information, see Lookup Table Editor.

Clicking this button for a lookup table object lets you edit the
object and save the new values for the object.

### Algorithm

#### Lookup method

### **Interpolation method** — Method of interpolation between breakpoint values `Linear point-slope` (default) | `Flat` | `Nearest` | `Linear Lagrange` | `Cubic spline` | `Akima spline`

When an input falls between breakpoint values, the block interpolates the output value using neighboring breakpoints. For more information on interpolation methods, see Interpolation Methods.

#### Dependencies

- If you select `Cubic spline`, the block
  supports only scalar signals. The other interpolation methods
  support nonscalar signals.
- If you select `Akima spline`, the
  extrapolation method can only be `Akima
  spline`.

  When set to the modified Akima interpolation method, this block
  does not support:

  - Row-major array layout and algorithms optimized for
    row-major array layout
  - Scaled double and fixed-point data types
  - `Simulink.LookupTable` objects
  - Code generation when the configuration parameter **Code Generation** > **Interface** > **Support non-finite numbers** check box is selected

  When set to the modified Akima interpolation method, this block is
  known to run more slowly when these conditions are true:

  - Code generation-based simulation targets, such as those
    for accelerator mode, rapid accelerator mode, protected
    models, and so forth.
  - Code generated for large breakpoint and data table sizes.
    For example with a table size of 629x1601.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InterpMethod` |
| **Type:** character vector |
| **Values:** `'Linear point-slope' | 'Flat' | 'Nearest' | 'Linear Lagrange' | 'Cubic spline' | 'Akima spline'` |
| **Default:** `'Linear point-slope'` |

### **Extrapolation method** — Method of handling input values that fall outside the range of a breakpoint vector `Linear` (default) | `Clip` | `Cubic spline` | `Akima spline`

Select `Clip`, `Linear`, or
`Cubic spline`. See Extrapolation Methods for more
information.

If the extrapolation method is `Linear`, the
extrapolation value is calculated based on the selected linear interpolation
method. For example, if the interpolation method is linear Lagrange, the
extrapolation method inherits the linear Lagrange equation to compute the
extrapolated value.

#### Dependencies

- To select `Cubic spline` for
  **Extrapolation method**, you must also select
  `Cubic spline` for
  **Interpolation method**.
- To select `Akima spline` for
  **Extrapolation method**, you must also select
  `Akima spline` for
  **Interpolation method**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ExtrapMethod` |
| **Type:** character vector |
| **Values:** `'Linear' | 'Clip' | 'Cubic spline' | 'Akima spline'` |
| **Default:** `'Linear'` |

### **Index search method** — Method of calculating table indices `Binary search` (default) | `Linear search` | `Evenly spaced points`

Select `Evenly spaced points`, `Linear
search`, or `Binary search`. Each
search method has speed advantages in different circumstances:

- For evenly spaced breakpoint vectors (for example, 10, 20, 30, and so
  on), you achieve optimal speed by selecting `Evenly spaced
  points` to calculate table indices.

  This algorithm uses only the first two breakpoints of a set to
  determine the offset and spacing of the remaining points.

  **Note**

  Set **Index search method** to
  `Evenly spaced points` when using the
  `Simulink.LookupTable` object to specify table
  data and the **Breakpoints Specification**
  parameter of the referenced `Simulink.LookupTable`
  object is set to `Even spacing`.
- For unevenly spaced breakpoint vectors, follow these
  guidelines:

  - If input signals do not vary much between time steps,
    selecting `Linear search` with
    **Begin index search using previous index
    result** produces the best performance.
  - If input signals jump more than one or two table intervals per
    time step, selecting `Binary search`
    produces the best performance.

A suboptimal choice of index search method can lead to slow performance of models that rely heavily on lookup tables.

**Note**

The generated code stores only the first breakpoint, the spacing, and the number of breakpoints when:

- The breakpoint data is not tunable.
- The index search method is `Evenly spaced
  points`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexSearchMethod` |
| **Type:** character vector |
| **Values:** `'Binary search' | 'Evenly spaced points' | 'Linear search'` |
| **Default:** `'Binary search'` |

### **Apply more accurate and efficient rounding when possible** — More accurate fixed-point table lookup using efficient round to nearest `off` (default) | `on`

Select this check box to enable an efficient round to nearest implementation
when possible. Enabling this option sets the rounding mode to
`Nearest` and adjusts the fraction lengths and intermediate
data types to offer a balance between accuracy and efficiency. If an efficient
implementation is not possible, the rounding mode, fraction lengths and
intermediate data types remain unchanged.

#### Dependencies

To enable this parameter:

- Set **Number of table dimensions** to
  `2`.
- Set **Interpolation method** to
  `Linear point-slope`.
- Set **Extrapolation method** to
  `Clip`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ApplyAccurateEfficientRounding` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Begin index search using previous index result** — Start using the index from the previous time step `off` (default) | `on`

Select this check box when you want the block to start its search using the index found at the
previous time step. For inputs that change slowly with respect to the interval
size, enabling this option can improve performance. Otherwise, the linear search
and binary search methods can take longer, especially for large breakpoint
vectors.

#### Dependencies

To enable this parameter, set **Index search method** to `Linear search` or `Binary search`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BeginIndexSearchUsingPreviousIndexResult` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Assume input is within range** — Option to check for out-of-range input values `off` (default) | `on`

*Since R2025a*

Specify whether or not to include code that checks for out-of-range input values.
Selecting this parameter means that you guarantee that the block has no out-of-range
inputs, enabling the block to further optimize the code and simulation. The valid input
range depends on the breakpoint data and the **Extrapolation method**
setting.

When you select **Assume input is within range**:

- During simulation, the block assumes that there are no out-of-range inputs and
  enforces this assumption by returning an error for out-of-range inputs.
- For code generation, the block does not generate out-of-range input handling
  code because it assumes there is no out-of-range input. This means that if the
  block tries to generate code for a model that returns an error because of
  out-of-range inputs, when the generated code is given the same input, the
  behavior is undefined, which can lead to severe consequence.

  **Warning**

  If the model tries to generate code and instead generates an error
  because the block detects out-of-range input, the behavior is undefined
  if the same out-of-range input is passed to deployed code. This
  undefined behavior might cause severe issues. For safety critical
  applications, do not select **Assume input is within
  range**.

If you want to select the **Assume input is within range** parameter
for efficiency, ensure that your model inputs are in range. For example:

| Parameter | Result | When to Use |
| --- | --- | --- |
| `on` | Simulation and generated code does not include conditional statements to check for out-of-range breakpoint inputs.  When the input is out-of-range, it may cause undefined behavior for simulation and generated code. | For simulation and code efficiency |
| `off` | Simulation and generated code includes conditional statements to check for out-of-range inputs. | For safety-critical applications |

If you are confident your input is within range, you can select the **Assume
input is within range** parameter for efficiency. By default, this
parameter is cleared. For safety-critical applications, do not select this parameter. If
you want to select the **Assume input is within range** parameter,
first check that your model inputs are in range. For example:

1. Clear the **Assume input is within range** parameter.
2. Set the **Diagnostic for out-of-range input** parameter to
   `Error`.
3. Simulate the model in normal mode.
4. If there are out-of-range errors, the block returns runtime errors. Fix them
   to be in range and run the simulation again.
5. When the simulation no longer generates out-of-range input errors, select the
   **Assume input is within range** parameter.

   **Note**

   When you select the **Assume input is within range**
   parameter and the input is out of range, the block returns a runtime error
   at simulation. The behavior is undefined for generated code.

Depending on your application, you can run the following Model Advisor checks to
verify the usage of this parameter:

- **By Product** > **Embedded Coder** > **Identify lookup table blocks that generate expensive
  out-of-range checking code**
- **By Product** > **Simulink Check** > **Modeling Standards** > **DO-178C/DO-331 Checks** > **Check usage of lookup table blocks**

For more information about the Model Advisor, see Run Model Advisor Checks.

Additionally, to determine if it is safe to select this parameter, if you have a
Simulink
Design Verifier™ license, consider using the Detect Block Input Range Violations (Simulink Design Verifier) check.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RemoveProtectionInput` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Diagnostic for out-of-range input** — Block action when input is out of range `None` (default) | `Warning` | `Error`

Specify whether to produce a warning or error when the input is out of range. Options include:

- `None` — Produce no response.
- `Warning` — Display a warning and continue the simulation.
- `Error` — Terminate the simulation and display an error.

#### Dependencies

To enable this parameter, clear the **Assume input is within
range** or **Assume index is within range**
parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DiagnosticForOutOfRangeInput` |
| **Type:** character vector |
| **Values:** `'None' | 'Warning' | 'Error'` |
| **Default:** `'None'` |

### **Apply full precision fixed-point algorithm when possible** — More accurate fixed-point table lookup `off` (default) | `on`

Use this check box to enable full-precision fixed-point algorithm lookup for
linear interpolation lookup when possible. This algorithm generally achieves
better precision for hardware-efficient fixed-point rounding modes.

#### Dependencies

To enable this parameter, set:

- **Number of table dimensions** to
  `1`.
- **Interpolation method** to `Linear
  point-slope`.
- **Extrapolation method** to
  `Clip`.
- Select the **Use last table value for inputs at or above
  last breakpoint** parameter.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ApplyFullPrecisionForLinearInterpolation` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Use last table value for inputs at or above last breakpoint** — Method for computing output for inputs at or above last breakpoint `off` (default) | `on`

Using this check box, specify the indexing convention that the block uses to address the last
element of a breakpoint vector and its corresponding table value. This check box
is relevant if the input is equal to or larger than the last element of the
breakpoint data. Due to rounding, selecting and clearing this check box may
result in differing results for the last breakpoint between simulation and code
generation.

| Check Box | Index Used by Block | Interval Fraction |
| --- | --- | --- |
| Selected | Last element of breakpoint data on the **Table and Breakpoints** tab | 0 |
| Cleared | Next-to-last element of breakpoint data on the **Table and Breakpoints** tab | 1 |

Given an input *u* within range of a breakpoint vector *bp*,
the interval fraction *f*, in the range
0≦*f*<1, is computed as shown below.

Suppose the breakpoint vector is `[1 4 5]` and
input *u* is `5.5`. If you select this check
box, the index is that of the last element (`5`) and the
interval fraction is 0. If you clear this check box, the index is that of the
next-to-last element (`4`) and the interval fraction is
1.

#### Dependencies

To enable this parameter, set:

- **Interpolation method** to `Linear`.
- **Extrapolation method** to `Clip`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseLastTableValue` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

#### Input settings

### **Use one input port for all input data** — Use only one input port `off` (default) | `on`

Select this check box to use only one input port that expects a signal that is
`n` elements wide for an n-dimensional table. This option
is useful for removing line clutter on a block diagram with many lookup
tables.

**Note**

When you select this check box, one input port with the label
`u` appears on the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseOneInputPortForAllInputData` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### Data Types

### **Table data** — Data type of table data `Inherit: Same as output` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the table data type. You can set it to:

- A rule that inherits a data type, for example, `Inherit:
  Same as output`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

**Tip**

Specify a table data type different from the output data type for these
cases:

- Lower memory requirement for storing table data that uses a
  smaller type than the output signal
- Sharing of prescaled table data between two n-D Lookup
  Table blocks with different output data types
- Sharing of custom storage table data in the generated code for
  blocks with different output data types

#### Dependencies

To enable this parameter, set **Table data** from the
**Table and Breakpoints** tab to
`Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit from 'Table data'' | 'Inherit: Same as output' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **Default:** `'Inherit: Same as output'` |

### **Table data Minimum** — Minimum value of the table data `[]` | `scalar`

Specify the minimum value for table data. The default value is `[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Table data Maximum** — Maximum value of the table data `[]` | `scalar`

Specify the maximum value for table data. The default value is `[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Breakpoints** — Breakpoint data type `Inherit: Same as corresponding input` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

Specify the data type for a set of breakpoint data. You can set it to:

- A rule that inherits a data type, for example, `Inherit:
  Same as corresponding input`
- The name of a built-in data type, for example,
  `single`
- The name of a data type class, for example, an enumerated data type
  class
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

**Tip**

- Breakpoints support unordered enumerated data. As a result, linear
  searches are also unordered, which offers flexibility but can impact
  performance. The search begins from the first element in the
  breakpoint.
- If the **Begin index search using previous index
  result** check box is selected, you must use ordered
  monotonically increasing data. This ordering improves
  performance.
- For enumerated data, **Extrapolation method**
  must be `Clip`.
- The block does not support out-of-range input for enumerated data.
  When specifying enumerated data, include the entire enumeration set
  in the breakpoint vector. For example, use the `enumeration`
  function.

This is a limitation for using enumerated data with this block:

- The block does not support out-of-range input for enumerated data.
  When specifying enumerated data, include the entire enumeration set in
  the breakpoint vector. For example, use the `enumeration`
  function.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

**Tip**

Specify a breakpoint data type different from the corresponding input data
type for these cases:

- Lower memory requirement for storing breakpoint data that uses a
  smaller type than the input signal
- Sharing of prescaled breakpoint data between two n-D Lookup
  Table blocks with different input data types
- Sharing of custom storage breakpoint data in the generated code
  for blocks with different input data types

Specify the same slope and bias for a breakpoint data type and its
corresponding input data type if either of them has a fixed-point data type.

#### Dependencies

To enable this parameter, set the corresponding
**Breakpoints** parameter from the **Table and
Breakpoints** tab to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsForDimension1DataTypeStr | BreakpointsForDimension2DataTypeStr| ... | BreakpointsForDimension30DataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as corresponding input' | 'Inherit: Inherit from 'Breakpoint data'' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **Default:** `'Inherit: Same as corresponding input'` |

### **Breakpoints Minimum** — Minimum value breakpoint data can have `[]` | `scalar`

Specify the minimum value that a set of breakpoint data can have. The default value is `[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsForDimension1Min | BreakpointsForDimension2Min | ... | BreakpointsForDimension30Min` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Breakpoints Maximum** — Maximum value breakpoint data can have `[]` | `scalar`

Specify the maximum value that a set of breakpoint data can have. The default value is `[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsForDimension1Max | BreakpointsForDimension2Max | ... | BreakpointsForDimension30Max` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Fraction** — Fraction data type `Inherit: Inherit via internal rule` (default) | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

Specify the fraction data type. You can set it to:

- A rule that inherits a data type, for example, `Inherit:
  Inherit via internal rule`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FractionDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'double' | 'single' | 'fixdt(1,16,0)'|'<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Intermediate results** — Intermediate results data type `Inherit: Same as output` (default) | `Inherit: Inherit via internal rule` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the intermediate results data type. You can set it to:

- A rule that inherits a data type, for example, `Inherit:
  Same as output`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

**Tip**

Use this parameter to specify higher (or lower) precision for internal
computations than for table data or output data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IntermediateResultsDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as output' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **Default:** `'Inherit: Same as output'` |

### **Output** — Output data type `Inherit: Same as input` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the output data type. You can set it to:

- A rule that inherits a data type, for example, `Inherit:
  Inherit via back propagation`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via back propagation' | 'Inherit: Inherit from table data' | 'Inherit: Same as first input' | 'double' | 'single' | 'half' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression'` |
| **Default:** `'Inherit: Same as first input'` |

### **Output Minimum** — Minimum value for range checking `[]` | `scalar`

Specify the minimum value for range checking. The default value is
`[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters).
- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Output Maximum** — Maximum value for range checking `[]` | `scalar`

Specify the maximum value for range checking. The default value is
`[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters).
- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Internal rule priority** — Internal rule for intermediate calculations `Speed` (default) | `Precision`

Specify the internal rule for intermediate calculations. Select `Speed` for faster calculations. If you do, a loss of accuracy might occur, usually up to 2 bits.

#### Dependencies

This parameter takes effect only when the **Intermediate
results** or **Fraction** parameter is set to
`Inherit: Inherit via internal rule`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InternalRulePriority` |
| **Type:** character vector |
| **Values:** `'Speed' | 'Precision'` |
| **Default:** `'Speed'` |

### **Require all inputs to have the same data type** — Require all inputs to have the same data type `on` (default) | `off`

Select to require all inputs to have the same data type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputSameDT` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'on'` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Simplest` (default) | `Ceiling` | `Convergent` | `Floor` | `Nearest` | `Round` | `Zero`

Specify the rounding mode for fixed-point lookup table calculations that occur during simulation or execution of code generated from the model. For more information, see Rounding Modes (Fixed-Point Designer).

This option does not affect rounding of values of block parameters. Simulink rounds such values to the nearest representable integer value. To control the rounding of a block parameter, enter an expression using a MATLAB® rounding function into the edit field on the block dialog box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Simplest'` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

| Action | Reasons for Taking This Action | What Happens for Overflows | Example |
| --- | --- | --- | --- |
| Select this check box (`on`). | Your model has possible overflow and you want explicit saturation protection in the generated code. | Overflows saturate to either the minimum or maximum value that the data type can represent. | An overflow associated with a signed 8-bit integer can saturate to -128 or 127. |
| Do not select this check box (`off`). | You want to optimize efficiency of your generated code.  You want to avoid overspecifying how a block handles out-of-range signals. For more information, see Troubleshoot Signal Range Errors. | Overflows wrap to the appropriate value that is representable by the data type. | The number 130 does not fit in a signed 8-bit integer and wraps to -126. |

**Tip**

If you save your model as version R2009a or earlier, this check box setting has no effect and no saturation code appears. This behavior preserves backward compatibility.

When you select this check box, saturation applies to every internal operation on the block, not just the output or result. In general, the code generation process can detect when overflow is not possible. In this case, the code generator does not produce saturation code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SaturateOnIntegerOverflow` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Libraries

Simulink / Lookup Tables HDL Coder / Lookup Tables

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **MapToRAM** | Map lookup tables (LUTs) to RAM. The default is `on`. See also MapToRAM (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **HandleDenormals** | Specify whether you want HDL Coder to insert additional logic to handle denormal numbers in your design. Denormal numbers are numbers that have magnitudes less than the smallest floating-point number that can be represented without leading zeros in the mantissa. The default is `inherit`. See also HandleDenormals (HDL Coder). |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |
| **MantissaMultiplyStrategy** | Specify how to implement the mantissa multiplication operation during code generation. By using different settings, you can control the DSP usage on the target FPGA device. The default is `inherit`. See also MantissaMultiplyStrategy (HDL Coder). |
| **PrecomputeCoefficients** | To enable this property, set **Interpolation method** to `Linear point-slope`.  When you enable this property, the slope and bias coefficients are statically precomputed depending on the table data and breakpoints. This setting reduces the number of division operations that are performed during runtime to compute the coefficients. It also reduces the overall number of floating-point addition and multiplication operations that are performed.  Enabling this property reduces the latency and saves area number of lookup table resources that are required. However, this property reorders the floating-point operations, which might result in small numeric differences. You can observe these numerical differences in the generated validation model. |
| **AreaOptimization** | For 4-D and 5-D LUT, HDL code generation supports fully parallel and serial implementations. To enable this property, use linear interpolation method for 4-D and 5-D LUT. When you set this property to either `Parallel` or `Serial`, HDL Coder manipulates the resources for your design. To reduce the area of your design, use serial implementation for minimizing the resources. To observe the results of fully parallel and serial implementation, compare the resource utilization report of native floating-point operators for your design. You can also compare the synthesis results of the design for fully parallel and serial implementation. |

**Latency Consideration for Lookup Table**

When you use the floating-point data types for LUT in native floating point
(NFP) mode, code generator computes the latency of LUT with respect to the
latency values of Add, Divide and Multiplication operators. The latency of LUT
also depends on HDL Block Properties, such as
**PrecomputeCoefficients** and
**MapToRAM**. It is computed as follows:

- When **PrecomputeCoefficients** is
  `Off`, latency of LUT is calculated as,

  `LUT Latency = D + N(2A +
  M)`

  where,

  `D` is NFP latency of Divide operator

  `A` is NFP latency of Add operator

  `M` is NFP latency of Multiplication operator

  `N` is Number of table dimensions
- When **PrecomputeCoefficients** is
  `On`, latency of LUT is calculated
  as,

  `LUT Latency = (2^N - 1)A +
  N(M)`
- When you turned `On` the
  **MapToRAM** property for the LUT and specify the
  synthesis tool and target device for your model, one additional latency
  has been added.

The latency values of the floating-point operators, such as Add, Divide and
Multiply, is listed in table. For more information, see Latency Values of Floating-Point Operators (HDL Coder).

| Floating-Point Operators | Data Type | Minimum Latency | Maximum Latency |
| --- | --- | --- | --- |
| Add | Double | 6 | 11 |
| Single | 6 | 11 |
| Half | 4 | 8 |
| Divide | Double | 31 | 61 |
| Single | 17 | 32 |
| Half | 10 | 19 |
| Multiply | Double | 6 | 9 |
| Single | 6 | 8 |
| Half | 4 | 6 |

For example, consider a 1-D lookup table with single-precision data type and
**PrecomputeCoefficients** as `off`. The
latency of 1-D LUT is

`LUT Latency = 32 + 1(2x11 + 8) = 62`.

If you turn on the **MapToRAM** option, then LUT latency comes out to be
63.

**Complex Data Support**

This block supports code generation for complex signals.

**Required Block Settings**

| Block Setting | HDL Coder Support |
| --- | --- |
| **Number of table dimensions** | Select the table dimension between 1 to 30. |
| **Breakpoints specification** | Select either `Explicit values` or `Even spacing`. |
| **Extrapolation method** | Select `Clip` or `Linear`. The code generator does not support extrapolation beyond even bounds. |
| **Interpolation method** | Select `Flat` or `Linear point-slope`. |
| **Diagnostic for out-of-range input** | Select `Error`. If you specify other options, HDL Coder generates a warning. |
| **Use last table value for inputs at or above last breakpoint** | Select this check box. |
| **Require all inputs to have the same data type** | Select this check box. |
| **Fraction** | Select `Inherit: Inherit via internal rule`. |
| **Integer rounding mode** | Select `Zero`, `Floor`, or `Simplest`. |
| **Use one input port for all input data** | Clear this check box. |

**Fixed-Point Data Type Support**

You can generate a code for block with fixed-point data types. You can use
fixed-point data types for all the dimensions in the n-D Lookup Table block. To
generate code with fixed-point data types for the block, use these block
parameter settings:

| Block Setting | HDL Coder Support |
| --- | --- |
| **Number of table dimensions** | Select the table dimension between 1 to 30. |
| **Breakpoints specification** | Select either `Explicit values` or `Even spacing`. |
| **Extrapolation method** | Select `Clip` |
| **Interpolation method** | Select `Flat` or `Linear point-slope`. |
| **Index search methods** | Select `Evenly spaced points`, `Binary search` or `Linear search`. |

**MAX 10 Device Settings**

If you use Intel® MAX 10 device, to map the lookup table to RAM, add this Tcl
command when creating the project in the Quartus tool:

`set_global_assignment -name INTERNAL_FLASH_UPDATE_MODE "SINGLE IMAGE
WITH ERAM"`

**Table Data Typing and Sizing**

- It is good practice to structure your table such that the spacing
  between breakpoints is a power of two. If the breakpoint spacing does
  not meet this condition, HDL Coder issues a warning. When the breakpoint spacing is a power
  of two, you can replace division operations in the prelookup step with
  right-shift operations.

**Restrictions**

- When you set the **Interpolation method** to
  `Flat`, the block supports
  `half` data types for data inputs, breakpoints, and
  outputs. Linear interpolation is not supported for half data
  types.
- HDL code generation does not support LUTs with more than 131072 table
  elements.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

Simulink
PLC Coder™ has limited support for lookup table blocks. The coder does not support:

- Number of dimensions greater than 2
- Cubic spline interpolation method
- Begin index search using a previous index mode
- Cubic spline extrapolation method

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2011a**

### R2025a: n-D Lookup Table block **Remove protection against out-of-range input in generated code** parameter replaced

The **Remove protection against out-of-range input in generated code**
parameter has been replaced by **Assume input is within range**. The
programmatic name, `RemoveProtectionInput`, remains the same.

If the model simulation generates errors because the out-of-range input is fed to a block with
**Assume input is within range** selected, the code generated by the
model has undefined behavior when the same out-of-range input occurs during execution of the
generated code. This undefined behavior might cause severe issues. For safety critical
applications, do not select **Remove protection against out-of-range input in
generated code**.

In releases prior to R2025a, the **Remove protection against out-of-range input in
generated code** only removed the code checks for out-of-range values for
generated code. The block failed to detect these issues. As a workaround. if you have a
model from a release prior to R2025a and cannot migrate to a later release, set the
**Diagnostic for out-of-range input** parameter to
`Error`. The next time you run the model, an error is generated
when the input is out-of-range.

### R2024b: **Support tunable table size in code generation** Parameter Replaced with **Support tunable size**

In lookup table blocks, the **Support tunable table size in code
generation** parameter has been replaced with **Support
tunable table size**. Due to this change:

- If you set the **Table and Breakpoints** > **Support tunable size** parameter programmatically with
  `SupportTunableTableSize`, the next time you open the
  lookup table block, the block displays a warning. Existing models continue
  to work.
- The **Support tunable size** parameter on the
  **Table and Breakpoints** tab replaces the
  **Support tunable table size in code generation** and
  **Maximum indices for each dimension** parameters on
  the **Algorithm** tab. Prior to R2024b, selecting the
  **Support tunable table size in code generation**
  parameter enabled the **Maximum indices for each
  dimension** parameter, which set the maximum index value for
  each table dimension. Starting in R2024b, selecting the **Support
  tunable size** parameter enables **Tunable
  Size** fields for the **Breakpoints**
  parameters. These **Tunable Size** fields replace the
  functionality of the **Maximum indices for each
  dimension** parameter. The block displays a warning on the
  block dialog box. Existing models continue to work. For more information,
  see Tunable size.

## Description

Approximate n-dimensional function

### Supported Block Operations

The 1-D, 2-D, and n-D Lookup Table blocks evaluate a sampled representation of a function in N
variables

y=F(x1,x2,x3,...,xN)

where the function *F* can be empirical. The block maps inputs to an output
value by looking up or interpolating a table of values you define with block parameters. The
block supports flat (constant), linear (linear point-slope), Lagrange (linear Lagrange),
nearest, cubic-spline, and Akima spline interpolation methods. You can apply these methods to
a table of any dimension from 1 through 30.

In the following block, the first input identifies the first dimension (row) breakpoints, the second input identifies the second dimension (column) breakpoints, and so on.

See Identify Port Location on Rotated or Flipped Block for a description of the port order for various block orientations.

When the **Math and Data Types** > **Use algorithms optimized for row-major array layout** configuration parameter is set, the 2-D and n-D Lookup Table block behavior
changes from column-major to row-major. For these blocks, the column-major and row-major
algorithms may differ in the order of the output calculations, possibly resulting in slightly
different numerical values. This capability requires a Simulink®
Coder™ or Embedded Coder® license. For more information on row-major support, see Code Generation of Matrices and Arrays (Simulink Coder).

### Specification of Breakpoint and Table Data

These block parameters define the breakpoint and table data.

| Block Parameter | Purpose |
| --- | --- |
| **Number of table dimensions** | Specifies the number of dimensions of your lookup table. |
| **Breakpoints** | Specifies a breakpoint vector that corresponds to each dimension of your lookup table. |
| **Table data** | Defines the associated set of output values. |

**Tip**

Evenly spaced breakpoints can make the generated code division-free. For more information, see `fixpt_evenspace_cleanup` and Identify questionable fixed-point operations (Embedded Coder).

### How the Block Generates Output

The n-D, 1-D and 2-D Lookup Table blocks generate output by looking up or estimating table
values based on the input values.

| Block Inputs | n-D Lookup Table Block Behavior |
| --- | --- |
| Match the values of indices in breakpoint vectors | Outputs the table value at the intersection of the row, column, and higher dimension breakpoints |
| Do not match the values of indices in breakpoint vectors, but are within range | Interpolates appropriate table values, using the **Interpolation method** you select |
| Do not match the values of indices in breakpoint vectors, and are out of range | Extrapolates the output value, using the **Extrapolation method** you select |

### Other Blocks That Perform Equivalent Operations

You can use the Interpolation Using Prelookup block with the Prelookup block to perform the equivalent operation of one n-D Lookup Table block. This combination of blocks offers greater flexibility that can result in more efficient simulation performance for linear interpolations.

When the lookup operation is an array access that does not require interpolation, use the Direct Lookup Table (n-D) block. For example, if you have an integer value `k` and you want the `k`th element of a table, `y = table(k)`, interpolation is unnecessary.
