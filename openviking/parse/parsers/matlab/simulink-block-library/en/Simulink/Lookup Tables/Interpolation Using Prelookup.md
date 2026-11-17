---
type: simulink-block
title: 'Interpolation Using Prelookup'
family: 'libsb2sl'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'NTP'
documentation_page: 'interpolationusingprelookup'
documentation_source_path: 'slref/interpolationusingprelookup.html'
language: en
---

# Interpolation Using Prelookup

## Ports
```yaml
ports:
- name: k1
  summary: Index, k, for the first dimension of the table scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: f1
  summary: Fraction, f, for the first dimension of the table scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: kn
  summary: Index, k, for the n-th dimension of the table scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: fn
  summary: Fraction, f, for the n-th dimension of the table scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: kf1
  summary: Input containing index k and fraction f bus object
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | bus
- name: kfn
  summary: Input containing index k and fraction f bus object
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | bus
- name: sm
  summary: Select and interpolate a subset of the table data scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
- name: T
  summary: Table data scalar | vector | matrix | n-d array
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: Approximation of N-dimensional function scalar | vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **k1** — Index, `k`, for the first dimension of the table scalar | vector | matrix

Zero-based index, `k`, specifying the interval containing the input
`u` for the first dimension of the table.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **f1** — Fraction, `f`, for the first dimension of the table scalar | vector | matrix

Fraction, `f`, representing the normalized position of the input within
the interval, `k`, for the first dimension of the
table.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **kn** — Index, `k`, for the `n`-th dimension of the table scalar | vector | matrix

Zero-based index, `k`, specifying the interval
containing the input `u` for the
`n`-th dimension of the table.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **fn** — Fraction, `f`, for the `n`-th dimension of the table scalar | vector | matrix

Fraction, `f`, representing the normalized position
of the input within the interval, `k`, for the
`n`-th dimension of the table.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **kf1** — Input containing index `k` and fraction `f` bus object

Inputs to the **kf1** port contain index
`k` and fraction `f` specified as
a bus object.

#### Dependencies

To enable this port, select the **Require index and
fraction as a bus** check box.

The number of available `kf` input ports depends
on the value of the **Number of dimensions** and
**Number of sub-table selection dimensions**
parameters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **kfn** — Input containing index `k` and fraction `f` bus object

Inputs to the **kfn** port contain index
`k` and fraction `f` for the n-th
dimension of the input, specified as a bus object.

#### Dependencies

To enable this port, select the **Require index and
fraction as a bus** check box.

The number of available **kf** input ports
depends on the value of the **Number of
dimensions** and **Number of sub-table
selection dimensions** parameters.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **sm** — Select and interpolate a subset of the table data scalar | vector | matrix

For column-major algorithm, the block uses inputs to the s*m*,
s*m*+1, ... s*n* port to perform
selection and interpolation within the subtables.
*`m`* maps to the
*m*th dimension of the
table. *n* equals the **Number of
dimensions**.

For row-major algorithm, the block uses inputs to the s1, s2,...
,s*m* port to perform selection and interpolation
within the subtables. *`m`* maps to the
*m*th dimension of the
table. *m* equals the **Number of sub-table
selection dimensions**.

#### Dependencies

To enable this port, the **Number of sub-table selection
dimensions** must be a positive integer less than or
equal to the **Number of dimensions**.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **T** — Table data scalar | vector | matrix | n-d array

Table data values provided as input to port **T**.
Typically, these table values correspond to the breakpoint data sets
specified in Prelookup blocks. The Interpolation Using Prelookup block
generates output by looking up or estimating table values based on index
(`k`) and interval fraction (`f`)
values fed from Prelookup blocks.

#### Dependencies

To enable this port, set **Source** to
`Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Approximation of N-dimensional function scalar | vector | matrix

Approximation of N-dimensional function, computed by interpolating (or
extrapolating) table data using values from the input index,
`k`, and fraction, `f`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Number of dimensions
  summary: Number of table data dimensions 2 (default) | integer between 1 and 30
  group: Main
  block_parameter: NumberOfTableDimensions
  type: character vector
  values: '''1'' | ''2'' | ''3'' |''4'' | ... | ''30'''
  default: '''2'''
- name: Require index and fraction as bus
  summary: Index and fraction inputs can be combined in a bus off (default) | on
  group: Main
  block_parameter: RequireIndexFractionAsBus
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Specification
  summary: Choose how to enter table data Explicit values (default) | Lookup table object
  group: Main
  block_parameter: TableSpecification
  type: character vector
  values: '''Explicit values'' | ''Lookup table object'''
  default: '''Explicit values'''
- name: Source
  summary: Source of table data Dialog (default) | Input port
  group: Main
  values: '''Dialog'' | ''Input port'''
  block_parameter: TableSource
  type: character vector
  default: '''Dialog'''
- name: Value
  summary: Specify table data values sqrt([1:11]' * [1:11]) (default) | multidimensional array of table data
  group: Main
  block_parameter: Table
  type: character vector
  values: scalar | vector | matrix | N-D array
  default: '''sqrt([1:11]'' * [1:11])'''
- name: Name
  summary: Name of a Simulink.LookupTable object Simulink.LookupTable object
  group: Main
  block_parameter: LookupTableObject
  type: character vector
  values: Simulink.LookupTable object
  default: ''''''
- name: Interpolation method
  summary: Select Linear point-slope, Flat, Nearest, or Linear Lagrange Linear point-slope (default) | Nearest | Flat | Linear
    Lagrange
  group: Main
  block_parameter: InterpMethod
  type: character vector
  values: '''Flat'' | ''Linear point-slope'' | ''Nearest'' | ''Linear Lagrange'''
  default: '''Linear point-slope'''
- name: Extrapolation method
  summary: Method of handling input that falls outside the range of the breakpoint data set Linear (default) | Clip
  group: Main
  block_parameter: ExtrapMethod
  type: character vector
  values: '''Clip'' | ''Linear'''
  default: '''Linear'''
- name: Valid index input may reach last index
  summary: Allow inputs to access the last elements of table data off (default) | on
  group: Main
  block_parameter: ValidIndexMayReachLast
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Assume index is within range
  summary: Option to check for out-of-range index values off (default) | on
  group: Main
  block_parameter: RemoveProtectionIndex
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Diagnostic for out-of-range input
  summary: Block action when input is out of range None (default) | Warning | Error
  group: Main
  block_parameter: DiagnosticForOutOfRangeInput
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''None'''
- name: Number of sub-table selection dimensions
  summary: Number of dimensions of the output computation subtable 0 (default) | positive integer, less than or equal to the
    number of table dimensions
  group: Main
  block_parameter: NumSelectionDims
  type: character vector
  values: '''0'' | ''1'' | ''2'' | ''3'' | ''4'' | ... | Number of table dimensions'
  default: '''0'''
- name: Sample time (-1 for inherited)
  summary: Interval between samples -1 (default) | scalar | vector
  group: Main
  block_parameter: SampleTime
  values: '"-1" (default) | scalar or vector in quotes'
- name: Table data
  summary: 'Data type of table values Inherit: Same as output (default) | Inherit: Inherit from ''Table data'' | double |
    single | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | fixdt(1,16) | fixdt(1,16,0) | fixdt(1,16,2^0,0)
    | <data type expression>'
  group: Data Types
  block_parameter: TableDataTypeStr
  type: character vector
  values: '''Inherit: Inherit from table data'' | ''Inherit: Same as output'' | ''double'' | ''single'' | ''int8'' | ''uint8''
    | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)''
    | ''<data type expression>'''
  default: '''Inherit: Same as output'''
- name: Table minimum
  summary: Minimum value of table data [] (default) | scalar
  group: Data Types
  block_parameter: TableMin
  type: character vector
  values: scalar
  default: '''[]'''
- name: Table maximum
  summary: Maximum value of table data [] (default) | scalar
  group: Data Types
  block_parameter: TableMax
  type: character vector
  values: scalar
  default: '''[]'''
- name: Intermediate results
  summary: 'Data type of intermediate results Inherit: Inherit via internal rule (default) | Inherit: Same as output | double
    | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | fixdt(1,16) | fixdt(1,16,0) | fixdt(1,16,2^0,0)
    | <data type expression>'
  group: Data Types
  block_parameter: IntermediateResultsDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via internal rule'' | ''Inherit: Same as output'' | ''double'' | ''single'' | ''int8'' | ''uint8''
    | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''fixdt(1,16)'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)''
    | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Output
  summary: 'Output data type Inherit: Inherit from ''Table data'' (default) | Inherit: Inherit via back propagation | double
    | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | fixdt(1,16) | fixdt(1,16,0) | fixdt(1,16,2^0,0)
    | <data type expression>'
  group: Data Types
  block_parameter: OutDataTypeStr
  type: character vector
  values: '''Inherit: Inherit via back propagation'' | ''Inherit: Inherit from table data'' | ''double'' | ''single'' | ''int8''
    | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''int64'' | ''uint64'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)''
    | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''Inherit: Inherit from table data'''
- name: Output minimum
  summary: Minimum value the block can output [] (default) | scalar
  group: Data Types
  block_parameter: OutMin
  type: character vector
  values: scalar
  default: '''[]'''
- name: Output maximum
  summary: Maximum value the block can output [] (default) | scalar
  group: Data Types
  block_parameter: OutMax
  type: character vector
  values: scalar
  default: '''[]'''
- name: Internal rule priority
  summary: Internal rule for intermediate calculations Speed (default) | Precision
  group: Data Types
  block_parameter: InternalRulePriority
  type: character vector
  values: '''Speed'' | ''Precision'''
  default: '''Speed'''
- name: Lock data type settings against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types
  block_parameter: LockScale
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Integer rounding mode
  summary: Rounding mode for fixed-point operations Floor (default) | Convergent | Ceiling | Nearest | Round | Simplest |
    Zero
  group: Data Types
  block_parameter: RndMeth
  type: character vector
  values: '''Ceiling'' | ''Convergent'' | ''Floor'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
  default: '''Floor'''
- name: Saturate on integer overflow
  summary: Method of overflow action off (default) | on
  group: Data Types
  block_parameter: SaturateOnIntegerOverflow
  values: '''off'' (default) | ''on'''
```

### Main

#### Table data

### **Number of dimensions** — Number of table data dimensions `2` (default) | integer between 1 and 30

Specify the number of dimensions that the table data must have. The
**Number of dimensions** defines the number of
independent variables for the table.

| To specify... | Do this... |
| --- | --- |
| 1, 2, 3, or 4 | Select the value from the drop-down list. |
| A higher number of table dimensions | Enter a positive integer directly in the field.  The maximum number of table dimensions that this block supports is 30. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumberOfTableDimensions` |
| **Type:** character vector |
| **Values:** `'1' | '2' | '3' |'4' | ... | '30'` |
| **Default:** `'2'` |

### **Require index and fraction as bus** — Index and fraction inputs can be combined in a bus `off` (default) | `on`

Select this check box to combine index and fraction inputs in a bus.

To enable the Prelookup block to supply input to the
Interpolation Using Prelookup block, set:

- **Output selection** to `Index
  and fraction as bus`
- **Output** to `Bus: <object
  name>`, where `<object
  name>` must be a valid bus object name
  accessible to the model

Regardless of this check box setting, the selection port always
operates in nonbus mode.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RequireIndexFractionAsBus` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Specification** — Choose how to enter table data `Explicit values` (default) | `Lookup table object`

Specify whether to enter table data directly or use a lookup table
object. If you set this parameter to:

- `Explicit values`, the
  **Source** and **Value**
  parameters are visible on the dialog box.
- `Lookup table object`, the
  **Name** parameter is visible on the dialog
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableSpecification` |
| **Type:** character vector |
| **Values:** `'Explicit values' | 'Lookup table object'` |
| **Default:** `'Explicit values'` |

To set this parameter from `'Explicit values'` to `'Lookup
table object'`, use the same
`set_param` call to set the
`LookupTableObject` parameter. For
example:

```
set_param('myModel/myInterpBlock',...
   'TableSpecification','Lookup table object',...
   'LookupTableObject','myLUTObject')
```

### **Source** — Source of table data `Dialog` (default) | `Input port`

Specify whether to enter table data in the dialog box or to inherit
the data from an input port. If you set **Source** to:

- `Dialog`, enter table data in the text box under
  **Value**
- `Input port`, verify that an upstream signal supplies table
  data to the table input port

#### Dependencies

To enable this parameter, set **Specification** to
`Explicit values`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableSource` |
| **Type:** character vector |
| **Values:** `'Dialog' | 'Input port'` |
| **Default:** `'Dialog'` |

### **Value** — Specify table data values `sqrt([1:11]' * [1:11])` (default) | multidimensional array of table data

Specify table data as an `N`-D array, where `N` is the
value of the **Number of dimensions** parameter. You
can edit the block diagram without specifying a correctly dimensioned
matrix by entering an empty matrix (`[]`) or an
undefined workspace variable in the **Value** edit
field. For information about how to construct multidimensional arrays in
MATLAB®, see Multidimensional Arrays.

If you set **Source** to `Input port`, verify
that an upstream signal supplies table data to the
**T** input port. The size of table data must match
the **Number of table dimensions**. For this option,
the block inherits table attributes from the **T**
input port.

To edit lookup tables using the Lookup Table Editor, click **Edit**
(see Lookup Table Editor).

#### Dependencies

To enable this parameter and explicitly specify table values on
the dialog box, you must set **Specification** to
`Explicit values` and
**Source** to
`Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Table` |
| **Type:** character vector |
| **Values:** scalar | vector | matrix | N-D array |
| **Default:** `'sqrt([1:11]' * [1:11])'` |

### **Name** — Name of a `Simulink.LookupTable` object `Simulink.LookupTable object`

Specify the name of a `Simulink.LookupTable` object. A
lookup table object references Simulink® breakpoint objects. If a `Simulink.LookupTable` object does not exist, click the
action button  and select
**Create**. The corresponding parameters of the
new lookup table object are automatically populated with the block
information.

#### Dependencies

To enable this parameter, set **Specification**
to `Lookup table object`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LookupTableObject` |
| **Type:** character vector |
| **Value:** `Simulink.LookupTable object` |
| **Default:** `''` |

#### Algorithm

### **Interpolation method** — Select `Linear point-slope`, `Flat`, `Nearest`, or `Linear Lagrange` `Linear point-slope` (default) | `Nearest` | `Flat` | `Linear Lagrange`

Specify the method the block uses to interpolate table data. You can
select `Linear point-slope`, `Flat`,
`Nearest`, or `Linear Lagrange`.
See Interpolation Methods for
more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InterpMethod` |
| **Type:** character vector |
| **Values:** `'Flat' | 'Linear point-slope' | 'Nearest' | 'Linear Lagrange'` |
| **Default:** `'Linear point-slope'` |

### **Extrapolation method** — Method of handling input that falls outside the range of the breakpoint data set `Linear` (default) | `Clip`

Specify the method the block uses to extrapolate values for all inputs
that fall outside the range of the breakpoint data set. You can select
`Clip` or
`Linear`. See Extrapolation Methods for
more information.

If the extrapolation method is `Linear`, the
extrapolation value is calculated based on the selected linear
interpolation method. For example, if the interpolation method is Linear
Lagrange, the extrapolation method inherits the Linear Lagrange equation
to compute the extrapolated value.

To use Prelookup and Interpolation Using Prelookup blocks to replicate n-D Lookup Table block behavior, the **Extrapolation method** for both Prelookup and Interpolation Using Prelookup blocks must be the same as if you use only the n-D Lookup Table block. For example, to get the same behavior as the n-D Lookup Table block with **Extrapolation method** set to `Linear`, set **Extrapolation method** to `Linear` for both Prelookup and Interpolation Using Prelookup blocks.

#### Dependencies

To enable the **Extrapolation method** parameter,
set the **Interpolation method** to
`Linear`.

The Interpolation Using Prelookup block does not support
`Linear` extrapolation when the input
or output signals specify integer or fixed-point data types.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ExtrapMethod` |
| **Type:** character vector |
| **Values:** `'Clip' | 'Linear'` |
| **Default:** `'Linear'` |

### **Valid index input may reach last index** — Allow inputs to access the last elements of table data `off` (default) | `on`

Specify how block inputs for index (`k`) and interval fraction
(`f`) access the last elements of
*n*-dimensional table data. Index values are zero
based.

This check box is relevant if the input index is equal to or larger
than the table's last index for that dimension. Due to rounding,
selecting and clearing this check box may result in differing results
for the last index between simulation and code generation.

| Check Box | Block Behavior |
| --- | --- |
| `on` | Returns the value of the last element in a dimension of its table when:  - `k` indexes the last table   element in the corresponding dimension - `f` is   `0` |
| `off` | Returns the value of the last element in a dimension of its table when:  - `k` indexes the   next-to-last table element in the corresponding   dimension - `f` is   `1` |

#### Dependencies

This check box is visible only when:

- **Interpolation method** is
  `Linear point-slope` or
  `Linear Lagrange`
- **Extrapolation method** is
  `Clip`

**Tip**

When you select **Valid index input may reach last
index** for an Interpolation Using Prelookup block,
you must also select **Use last breakpoint for input at
or above upper limit** for all Prelookup blocks
that feed it. This action allows the blocks to use the same
indexing convention when accessing the last elements of their
breakpoint and table data sets.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ValidIndexMayReachLast` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Assume index is within range** — Option to check for out-of-range index values `off` (default) | `on`

*Since R2025a*

Specify whether or not to include code that checks for out-of-range index values.
Selecting this parameter means you guarantee that the block has no out-of-range indices,
enabling the block to further optimize the code and simulation. The valid index range
depends on the breakpoint data and the **Extrapolation method**
setting.

When you select **Assume index is within range**:

- During simulation, the block assumes that there are no out-of-range indices
  and enforces this assumption by returning an error for out-of-range
  indices.
- For code generation, the block does not generate out-of-range index handling
  code because it assumes there is no out-of-range index. This means that if the
  block tries to generate code for a model that returns an error because of
  out-of-range indices, when the generated code is given the same index, the
  behavior is undefined, which can lead to severe consequence.

  **Warning**

  If the model tries to generate code and instead generates an error
  because the block detects out-of-range indices, the behavior is
  undefined if the same out-of-range index is passed to deployed code.
  This undefined behavior might cause severe issues. For safety critical
  applications, do not select **Assume index is within
  range**.

If you want to select the **Assume index is within range** parameter
for efficiency, ensure that your model indices are in range. For example:

| Parameter | Result | When to Use |
| --- | --- | --- |
| `on` | Simulation and generated code does not include conditional statements to check for out-of-range breakpoint indices.  When the index is out-of-range, it may cause undefined behavior for simulation and generated code. | For simulation and code efficiency |
| `off` | Simulation and generated code includes conditional statements to check for out-of-range indices. | For safety-critical applications |

If you are confident your indices is within range, you can select the **Assume
index is within range** parameter for efficiency. By default, this
parameter is cleared. For safety-critical applications, do not select this parameter. If
you want to select the **Assume index is within range** parameter,
first check that your model indices are in range. For example:

1. Clear the **Assume index is within range** parameter.
2. Set the **Diagnostic for out-of-range index** parameter to
   `Error`.
3. Simulate the model in normal mode.
4. If there are out-of-range errors, the block returns runtime errors. Fix them
   to be in range and run the simulation again.
5. When the simulation no longer generates out-of-range index errors, select the
   **Assume index is within range** parameter.

   **Note**

   When you select the **Assume index is within range**
   parameter and the index is out of range, the block returns a runtime error
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
| **Block Parameter:** `RemoveProtectionIndex` |
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

### **Number of sub-table selection dimensions** — Number of dimensions of the output computation subtable `0` (default) | positive integer, less than or equal to the number of table dimensions

Specify the number of dimensions of the subtable that the block uses
to compute the output. Follow these rules:

- To enable subtable selection, enter a positive integer.

  This integer must be less than or equal to the
  **Number of table dimensions**.
- To disable subtable selection, enter `0` to
  interpolate the entire table.

For nonzero values, the subtable selection behavior is optimized for
row-major layout when you select the **Math and Data Types** > **Use algorithms optimized for row-major array
layout** configuration parameter.

For more information, see How The Block Interpolates a Subset of Table Data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumSelectionDims` |
| **Type:** character vector |
| **Values:** `'0' | '1' | '2' | '3' | '4' | ... | Number of table dimensions` |
| **Default:** `'0'` |

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

### Data Types

### **Table data** — Data type of table values `Inherit: Same as output` (default) | `Inherit: Inherit from 'Table data'` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the table data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as output`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the table data
type.

**Tip**

Specify a table data type different from the output data type for
these cases:

- Lower memory requirement for storing table data that uses
  a smaller type than the output signal
- Sharing of prescaled table data between two
  Interpolation Using Prelookup blocks with
  different output data types
- Sharing of custom storage table data in Simulink
  Coder™ generated code for blocks with different
  output data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit from table data' | 'Inherit: Same as output' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Same as output'` |

### **Table minimum** — Minimum value of table data `[]` (default) | scalar

Specify the minimum value for table data as a finite, real, double, scalar. The default
value is `[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Table maximum** — Maximum value of table data `[]` (default) | scalar

Specify the maximum value for table data as a finite, real, double, scalar. The default
value is `[]` (unspecified).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TableMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Intermediate results** — Data type of intermediate results `Inherit: Inherit via internal rule` (default) | `Inherit: Same as output` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the intermediate results data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as output`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

**Tip**

Use this parameter to specify higher precision for internal
computations than for table data or output data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IntermediateResultsDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'Inherit: Same as output' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Output** — Output data type `Inherit: Inherit from 'Table data'` (default) | `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the output data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via back
  propagation`
- The name of a built-in data type, for example,
  `single`
- The name of a data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the output data
type.

See Control Data Types of Signals for more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via back propagation' | 'Inherit: Inherit from table data' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | 'fixdt(1,16,2^0,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit from table data'` |

### **Output minimum** — Minimum value the block can output `[]` (default) | scalar

Specify the minimum value that the block should output as a finite, real-valued scalar.
The default value is `[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters).
- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more
  information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMin` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Output maximum** — Maximum value the block can output `[]` (default) | scalar

Specify the maximum value that the block should output as a finite,
real-valued scalar. The default value is `[]`
(unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters).
- Simulation range checking (see Specify Signal Ranges).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model.
  This optimization can remove algorithmic code and affect the
  results of some simulation modes such as SIL or external mode.
  For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutMax` |
| **Type:** character vector |
| **Values:** scalar |
| **Default:** `'[]'` |

### **Internal rule priority** — Internal rule for intermediate calculations `Speed` (default) | `Precision`

Specify the internal rule for intermediate calculations. Select
`Speed` for faster calculations. If you do,
a loss of accuracy might occur, usually up to 2 bits.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InternalRulePriority` |
| **Type:** character vector |
| **Values:** `'Speed' | 'Precision'` |
| **Default:** `'Speed'` |

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types you specify on this block. For more information, see Lock the Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Convergent` | `Ceiling` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more
information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To
control the rounding of a block parameter, enter an expression using a
MATLAB rounding function in the mask field.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer `int8`
can represent is 127. Any block operation result greater than this maximum value causes
overflow of the 8-bit integer.

- With this parameter selected, the block output saturates at 127.
  Similarly, the block output saturates at a minimum output value of
  -128.
- With this parameter cleared, the software interprets the overflow-causing
  value as `int8`, which can produce an unintended result.
  For example, a block result of 130 (binary 1000 0010) expressed as
  `int8` is -126.

#### Tips

- Consider selecting this parameter when your model has a possible overflow
  and you want explicit saturation protection in the generated code.
- Consider clearing this parameter when you want to optimize efficiency of
  your generated code. Clearing this parameter also helps you to avoid
  overspecifying how a block handles out-of-range signals. For more
  information, see Troubleshoot Signal Range Errors.
- When you select this parameter, saturation applies to every internal
  operation on the block, not just the output or result.
- In general, the code generation process can detect when overflow is not
  possible. In this case, the code generator does not produce saturation
  code.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `'off'` (default) | `'on'` |
## Libraries

Simulink / Lookup Tables

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

Simulink
PLC Coder™ has limited support for lookup table blocks. The coder does not
support:

- Number of dimensions greater than 2
- Cubic spline interpolation method
- Begin index search using a previous index mode
- Cubic spline extrapolation method

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2006b**

### R2025a: Interpolation Using Prelookup block **Remove protection against out-of-range index in generated code** parameter replaced

The **Remove protection against out-of-range index in generated code**
parameter has been replaced by **Assume index is within range**.
The programmatic name, `RemoveProtectionInput`, remains the
same.

If the model simulation generates errors because the out-of-range index is fed to
a block with **Assume index is within range** selected, the code
generated by the model has undefined behavior when the same out-of-range index
occurs during execution of the generated code. This situation might cause severe
issues. This undefined behavior might cause severe issues. For safety critical
applications, do not select **Remove protection against out-of-range index
in generated code**.

In releases prior to R2025a, the **Remove protection against out-of-range
index in generated code** only removed the code checks for
out-of-range values for generated code. The block failed to detect these issues. As
a workaround. if you have a model from a release prior to R2025a and cannot migrate
to a later release, set the **Diagnostic for out-of-range input**
parameter to `Error`. The next time you run the model, an
error is generated when the index is out-of-range.

## Description

Use precalculated index and fraction values to accelerate approximation of N-dimensional function

The Interpolation Using Prelookup block is most efficient when used with the Prelookup block. The Prelookup block calculates the index and interval
fraction that specify how its input value `u` relates to the breakpoint
data set. Feed the resulting index and fraction values into an Interpolation Using
Prelookup block to interpolate an *n*-dimensional table. These two
blocks have distributed algorithms. When combined together, they perform the same
operation as the integrated algorithm in the n-D Lookup Table block. However, the
Prelookup and Interpolation Using Prelookup blocks offer greater flexibility that can
provide more efficient simulation and code generation. For more information, see Efficiency of Performance.

### Supported Block Operations

To use the Interpolation Using Prelookup block, you specify a set of table data values
directly on the dialog box or feed values into the **T** input
port. Typically, these table values correspond to the breakpoint data sets specified
in Prelookup blocks. The Interpolation Using Prelookup block generates output by
looking up or estimating table values based on index and interval fraction values
fed from Prelookup blocks. Labels for the index and interval fraction appear as
`k` and `f` on the Interpolation Using
Prelookup block icon.

| When inputs for index and interval fraction... | The Interpolation Using Prelookup block... |
| --- | --- |
| Map to values in breakpoint data sets | Outputs the table value at the intersection of the row, column, and higher dimension breakpoints |
| Do not map to values in breakpoint data sets, but are within range | Interpolates appropriate table values using the **Interpolation method** you select |
| Do not map to values in breakpoint data sets, and are out of range | Extrapolates the output value using the **Extrapolation method** you select |

### How The Block Interpolates a Subset of Table Data

You can use the **Number of sub-table selection dimensions** parameter to
specify that interpolation occur only on a subset of the table data. To activate
this interpolation mode, set this parameter to a positive integer. This value
defines the number of dimensions to select, starting from the highest dimension of
table data for the default column-major algorithm. Therefore, the value must be less
than or equal to the **Number of table dimensions**.

For row-major algorithms, the interpolation starts from the first or lowest
dimension of the table data.

For nonzero values, the subtable selection behavior is optimized for row-major
layout when you select the **Math and Data Types** > **Use algorithms optimized for row-major array layout** configuration parameter.

Suppose that you have 3-D table data in your Interpolation Using Prelookup
block. This behavior applies for the column-major algorithm.

| Number of Selection Dimensions | Action by the Block | Block Appearance |
| --- | --- | --- |
| 0 | Interpolates the entire table and does not activate subtable selection | Does not change |
| 1 | Interpolates the first two dimensions and selects the third dimension | Displays an input port with the label `s3` that you use to select and interpolate 2-D tables |
| 2 | Interpolates the first dimension and selects the second and third dimensions | Displays two input ports with the labels `s2` and `s3` that you use to select and interpolate 1-D tables |

Subtable selection uses zero-based indexing. For an example of interpolating a subset of
table data, see Using the Prelookup and Interpolation Blocks.

For 2-D or n-D interpolation without subtable selection, the column-major and
row-major algorithms may differ in the order of output calculations, causing slight
different numerical results.
