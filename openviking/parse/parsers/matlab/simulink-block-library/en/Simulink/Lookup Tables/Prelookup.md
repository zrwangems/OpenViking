---
type: simulink-block
title: 'Prelookup'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: 'prelookup'
documentation_source_path: 'slref/prelookup.html'
language: en
---

# Prelookup

## Ports

### Input

### **Port\_1** — Input signal, `u` scalar | vector | matrix

The Prelookup block accepts real-valued signals of any numeric data
type that Simulink® supports, except Boolean. The Prelookup block supports
fixed-point data types for signals and breakpoint data.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated` | `bus`

### **bp** — Breakpoint data 1-D vector of real-valued signals

The Prelookup block accepts real-valued signals as breakpoint data of
any numeric data type that Simulink supports, except Boolean.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `enumerated`
### Output

### **k** — Index of the interval containing the input, `u` scalar | vector | matrix

The zero-based index, *k*, is a real-valued integer
that specifies the interval containing the input,
`u`.

#### Dependencies

To enable this port, set the **Output selection**
to `Index and fraction` or
`Index only`.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **f** — Fraction representing the normalized position of the input, `u`, within the interval, *k* scalar | vector | matrix

Fraction, *f*, represents the normalized position of
the input, `u`, within the interval
*k*.

#### Dependencies

To enable this port, set the **Output selection**
to `Index and fraction`.

**Data Types:** `single` | `double` | `fixed point`

### **Port\_2** — Bus containing index, *k*, and fraction, *f* bus

Outputting the index, *k*, and fraction
*f*, as a bus object can help simplify the
model.

#### Dependencies

To enable this port, set the **Output selection**
to `Index and fraction as bus`.

**Data Types:** `bus`

## Parameters

### Main

#### Breakpoints data

### **Specification** — Choose how to enter breakpoint data `Explicit values` (default) | `Even spacing` | `Breakpoint object`

If you set this parameter to:

- `Explicit values`, the
  **Source** and **Value**
  parameters are visible on the dialog box.
- `Even spacing`, the **First
  point**, **Spacing**, and
  **Number of points** parameters are visible
  on the dialog box.
- `Breakpoint object`, the
  **Name** parameter is visible on the dialog
  box.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsSpecification` |
| **Type:** character vector |
| **Values:** `'Explicit values' | 'Even spacing' | 'Breakpoint object'` |
| **Default:** `'Explicit values'` |

To set this parameter from `'Explicit values'` or
`'Even spacing'` to `'Breakpoint
object'`, use the same `set_param`
call to set the `BreakpointObject` parameter. For
example:

```
set_param('myModel/myPrelookupBlock',...
   'BreakpointsSpecification','Breakpoint object',...
   'BreakpointObject','myBPObject')
```

### **Source** — Specify source of breakpoint data `Dialog` (default) | `Input port`

If you set **Source** to:

- `Dialog`, specify breakpoint data
  under **Value**.
- `Input port`, verify that an upstream
  signal supplies breakpoint data to the `bp`
  input port. Each breakpoint data set must be a strictly
  monotonically increasing vector that contains two or more
  elements. For this option, your block inherits breakpoint
  attributes from the `bp` input port.

**Note**

Using the input port to specify table or breakpoint data might
negatively affect block performance for simulation due to runtime
checks. To model dynamics that require breakpoints to change during
simulation, select `Dialog` and change the
breakpoint data using the Parameter Writer block.

#### Dependencies

To enable this parameter, set **Specification**
to `Explicit values`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsDataSource` |
| **Type:** character vector |
| **Values:** `'Dialog' | 'Input port'` |
| **Default:** `'Dialog'` |

### **Value** — Breakpoint data values `[10:10:110]` (default) | vector of strictly monotonically increasing values containing two or more elements

Explicitly specify the breakpoint data. Each breakpoint data set must
be a strictly monotonically increasing vector that contains two or more
elements. For this option, you specify additional breakpoint attributes
on the **Data Types** pane.

To open the Lookup Table Editor, click **Edit**
(see Lookup Table Editor).

**Note**

When you set **Specification** to
`Explicit values` and
**Source** to `Input
port`, verify that an upstream signal supplies
breakpoint data to the `bp` input port. Each
breakpoint data set must be a strictly monotonically increasing
vector that contains two or more elements. For this option, your
block inherits breakpoint attributes (including data type) from the
`bp` input port.

#### Dependencies

To enable this parameter, set **Specification**
to `Explicit values` and
**Source** to
`Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsData` |
| **Type:** character vector |
| **Values:** vector of strictly monotonically increasing values containing two or more elements |
| **Default:** `'[10:10:110]'` |

### **First point** — First point in evenly spaced breakpoint data `10` (default) | real-valued scalar

#### Dependencies

To enable this parameter, set **Specification**
to `Even spacing`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsFirstPoint` |
| **Type:** character vector |
| **Values:** real-valued scalar |
| **Default:** `'10'` |

### **Spacing** — Spacing between evenly spaced breakpoints `10` (default) | real-valued, positive scalar

#### Dependencies

To enable this parameter, set **Specification**
to `Even spacing`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsSpacing` |
| **Type:** character vector |
| **Values:** real-valued, positive scalar |
| **Default:** `'10'` |

### **Number of points** — Number of evenly spaced points `11` (default) | real-valued, positive scalar

#### Dependencies

To enable this parameter, set **Specification**
to `Even spacing`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointsNumPoints` |
| **Type:** character vector |
| **Values:** real-valued, positive scalar |
| **Default:** `'11'` |

### **Name** — Name of a `Simulink.Breakpoint` object no default | `Simulink.Breakpoint` object

Specify the name of a `Simulink.Breakpoint` object. A
breakpoint object references Simulink breakpoint objects. If a `Simulink.Breakpoint` object does not exist, click the
action button  and select
**Create**. The corresponding parameters of the
new breakpoint object are automatically populated with the block
information.

#### Dependencies

To enable this parameter, set **Specification**
to `Breakpoint object`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointObject` |
| **Type:** character vector |
| **Values:** `Simulink.Breakpoint` object |
| **Default:** `''` |

#### Algorithm

### **Output selection** — Specify the signals the block outputs `Index and fraction` (default) | `Index and fraction as bus` | `Index only`

If you want the block to output the index and interval fraction, you
can specify whether the block outputs individual signals or a bus signal
that includes both the index and fraction signals.

- `Index only` outputs just the index,
  without the fraction. Typical applications for this option
  include:

  - Feeding a Direct Lookup Table (n-D)
    block, with no interpolation on the interval
  - Feeding selection ports of a subtable selection for an
    Interpolation Using Prelookup
    block
  - Performing nonlinear quantizations
- `Index and fraction` outputs the
  index and fraction as individual signals.
- `Index and fraction as bus` outputs a
  bus signal that includes the index and fraction signals. Using a
  bus for these signals:

  - Simplifies the model by tying these two related
    signals together
  - Creates a test point `DpResult`
    structure for the AUTOSAR 4.0 library
  - For the AUTOSAR 4.0 library, avoids the creation of
    extra copies during code generation when the
    Prelookup and Interpolation
    Using Prelookup blocks are in separate
    models

  **Note**

  Selecting `Index and fraction as
  bus` displays the
  **Output** parameter in the
  **Data Types** pane and sets the
  **Output** parameter to
  `Inherit: auto`. Change this
  default value to specify a user-defined bus object. For
  details about defining the bus object, see the
  **Output** parameter
  description.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputSelection` |
| **Type:** character vector |
| **Values:** `'Index and fraction' | 'Index and fraction as bus' | 'Index only'` |
| **Default:** `'Index and fraction'` |

### **Index search method** — Method for searching breakpoint data `Binary search` (default) | `Linear search` | `Evenly spaced points`

Each search method has speed advantages in different
situations:

- For evenly spaced breakpoint sets (for example, 10, 20, 30,
  and so on), you achieve optimal speed by selecting
  `Evenly spaced points` to calculate
  table indices. This algorithm uses only the first two
  breakpoints of a set to determine the offset and spacing of the
  remaining points.
- For unevenly spaced breakpoint sets, follow these
  guidelines:

  - If input values for `u` do not vary
    significantly between time steps, selecting
    `Linear search` with
    **Begin index search using previous index
    result** produces the best
    performance.
  - If input values for `u` jump more
    than one or two table intervals per time step, selecting
    `Binary search` produces
    the best performance.

A suboptimal choice of index search method can lead to slow
performance of models that rely heavily on lookup tables.

**Note**

The generated code stores only the first breakpoint, the spacing,
and the number of breakpoints when:

- The breakpoint data is not tunable.
- The index search method is `Evenly spaced
  points`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexSearchMethod` |
| **Type:** character vector |
| **Values:** `'Evenly spaced points'` | `'Linear search'` | `'Binary search'` |
| **Default:** `'Binary search'` |

### **Begin index search using previous index result** — Start search using the index found at the previous time step `off` (default) | `on`

For input values of `u` that change slowly with
respect to the interval size, enabling this option can improve
performance. Otherwise, the linear search and binary search methods can
take longer, especially for large breakpoint sets.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BeginIndexSearchUsingPreviousIndexResult` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Extrapolation method** — Method for handling out-of-range input values `Clip` (default) | `Linear`

Options include:

- `Clip`

  | Block Input | Block Outputs |
  | --- | --- |
  | Less than the first breakpoint | - Index of the first breakpoint (for example,   `0`) - Interval fraction of   `0` |
  | Greater than the last breakpoint | - Index of the next-to-last breakpoint - Interval fraction of   `1` |

  Suppose the range is `[1 2 3]` and you select
  this option. If `u` is `0.5`,
  the index is `0` and the interval fraction is
  `0`. If `u` is
  `3.5`, the index is `1`
  and the interval fraction is `1`.
- `Linear`

  | Block Input | Block Outputs |
  | --- | --- |
  | Less than the first breakpoint | - Index of the first breakpoint (for example,   `0`) - Interval fraction that represents the linear   distance from `u` to the first   breakpoint |
  | Greater than the last breakpoint | - Index of the next-to-last breakpoint - Interval fraction that represents the linear   distance from the next-to-last breakpoint to   `u` |

  Suppose the range is `[1 2 3]` and you select
  this option. If `u` is `0.5`,
  the index is `0` and the interval fraction is
  `-0.5`. If `u` is
  `3.5`, the index is `1`
  and the interval fraction is `1.5`.

**Note**

The Prelookup block supports linear extrapolation
only when all of the following conditions are true:

- The input `u`, breakpoint data, and
  fraction output use floating-point data types.
- The index uses a built-in integer data type.

To use Prelookup and Interpolation Using Prelookup blocks to replicate n-D Lookup Table block behavior, the **Extrapolation method** for both Prelookup and Interpolation Using Prelookup blocks must be the same as if you use only the n-D Lookup Table block. For example, to get the same behavior as the n-D Lookup Table block with **Extrapolation method** set to `Linear`, set **Extrapolation method** to `Linear` for both Prelookup and Interpolation Using Prelookup blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ExtrapMethod` |
| **Type:** character vector |
| **Values:** `'Clip' | 'Linear'` |
| **Default:** `'Clip'` |

### **Use last breakpoint for input at or above upper limit** — Method of handling inputs at or above upper limit `off` (default) | `on`

Specify how to index input values of `u` that are
greater than or equal to the last breakpoint. The index value is zero
based. When input equals the last breakpoint, block outputs differ as
follows.

| Check Box | Block Outputs |
| --- | --- |
| Selected (`on`) | - Index of the last element in the breakpoint   data set - Interval fraction of   `0` |
| Cleared (`off`) | - Index of the next-to-last breakpoint - Interval fraction of   `1` |

**Tip**

When you select **Use last breakpoint for input at or
above upper limit** for a Prelookup
block, you must also select **Valid index input may reach
last index** for the Interpolation Using
Prelookup block to which it connects. This action allows
the blocks to use the same indexing convention when accessing the
last elements of their breakpoint and table data sets.

#### Dependencies

This parameter is visible only when **Extrapolation
method** is `Clip`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `UseLastBreakpoint` |
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

Options include:

- `None` — Produce no
  response.
- `Warning` — Display a warning
  and continue the simulation.
- `Error` — Terminate the
  simulation and display an error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DiagnosticForOutOfRangeInput` |
| **Type:** character vector |
| **Values:** `'None' | 'Warning' | 'Error'` |
| **Default:** `'None'` |

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

### **Breakpoint** — Breakpoint data type `Inherit: Same as input` (default) | `Inherit: Inherit from 'Breakpoint data'` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

Specify the breakpoint data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as input`
- The name of a built-in data type, for example,
  `single`
- The name of a data type class, for example, an enumerated data
  type class
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

**Tip**

- Specify a breakpoint data type different from the data
  type of input `u` for these cases:

  - Lower memory requirement for storing breakpoint
    data that uses a smaller type than the input signal
    `u`
  - Sharing of prescaled breakpoint data between two
    Prelookup blocks with different
    data types for input `u`
  - Sharing of custom storage breakpoint data in the
    generated code for blocks with different data types
    for input `u`
- Specify the same slope and bias for a breakpoint data type
  and its corresponding input data type if either of them has
  a fixed-point data type.
- Enumerated data:

  - Breakpoints support unordered enumerated data. As
    a result, linear searches are also unordered, which
    offers flexibility but can impact performance. The
    search begins from the first element in the
    breakpoint.
  - If the **Begin index search using previous
    index result** parameter is selected, you
    must use ordered monotonically increasing data. This
    ordering improves performance.
  - For enumerated data, **Extrapolation
    method** must be
    `Clip`.
  - Because the fraction is `1` or
    `0`, select **Output selection** > **Index only**.

    If you are using the index only output selection
    setting with the Interpolation Using
    Prelookup block, consider using the
    **Number of sub-table selection
    dimensions** parameter.

These are limitations for using enumerated data with this
block:

- The block does not support out-of-range input for enumerated
  data. When specifying enumerated data, include the entire
  enumeration set in the breakpoint data set. For example, use the
  `enumeration`
  function.
- When breakpoints data source is set to `Inport
  port`, the enumeration data type must have
  `0` as the default value. For example, for
  this enumeration class, the default value of
  `GEAR1` must be `0`.

  ```
  classdef(Enumeration) Gears < Simulink.IntEnumType
      enumeration
          GEAR1(1),
          GEAR2(2),
          GEAR3(4),
          GEAR4(8),
          SPORTS(16),
          REVERSE(32),
          NEUTRAL(0)
      end
  end
  ```

#### Dependencies

To enable this parameter, set the breakpoints data
**Source** to
`Dialog`.

**Note**

When you set **Source** to `Input
port`, the block inherits all breakpoint
attributes (data type, minimum, and maximum) from the
`bp` input port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Same as input' | 'Inherit: Inherit from 'Breakpoint data'' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64'| 'fixdt(1,16)' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'|'<data type expression>'` |
| **Default:** `'Inherit: Same as input'` |

### **Index** — Index data type `uint32` (default) | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `<data type expression>`

Specify a data type that can index all elements in the breakpoint data
set. You can:

- Select a built-in integer data type from the list.
- Specify an integer data type using a fixed-point
  representation.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `IndexDataTypeStr` |
| **Type:** character vector |
| **Values:** `'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16)' | '<data type expression>'` |
| **Default:** `'uint32'` |

### **Fraction** — Fraction data type `Inherit: Inherit via internal rule` (default) | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

Specify the data type of the interval fraction. You can:

- Select a built-in data type from the list.
- Specify data type inheritance through an internal rule.
- Specify a fixed-point data type using the [Slope Bias] or
  binary-point-only scaling representation.

  - If you use the [Slope Bias] representation, the
    scaling must be trivial — that is, the slope is
    `1` and the bias is
    `0`.
  - If you use the binary-point-only representation, the
    fixed power-of-two exponent must be less than or equal
    to zero.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

This parameter displays only when you set **Output
selection** on the **Main**
tab to `Index and fraction`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FractionDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via internal rule' | 'double' | 'single' | 'fixdt(1,16,0)' | '<data type expression>'` |
| **Default:** `'Inherit: Inherit via internal rule'` |

### **Output** — Output data type `Inherit: auto` (default) | `bus: <object name>`

To output a virtual bus, use the `Inherit: auto`
setting. The resulting virtual bus contains two elements, the index and
the fraction signals.

To output and specify a nonvirtual bus, use the `Bus:
<object name>` template. Replace
`<object name>` with the name of a
bus object that contains the index and fraction signals.

- The bus object must contain two elements. The first element
  corresponds to the index signal and the second to the fraction
  signal.
- The index and fraction bus element signals cannot be bus
  signals.
- The data type and the complexity of the bus elements must meet
  the same constraints that apply to the index and fraction
  signals if you set **Output selection** to
  `Index and fraction`.

To create the bus object with the index and fraction bus elements, use
MATLAB® code similar to this, customizing the bus object name and
the names and data types of the bus elements.

```
% Bus object: kfBus
elems(1) = Simulink.BusElement;
elems(1).Name = 'Index';
elems(1).DataType = 'int8';

elems(2) = Simulink.BusElement;
elems(2).Name = 'Fraction';
elems(2).DataType = 'double';

kfBus = Simulink.Bus;
kfBus.Elements = elems;
clear elems;
```

Alternatively, you can use the Type Editor to create or modify the bus
object to use with the Prelookup block.

If you feed the bus output signal from this block to an
Interpolation Using Prelookup block, select
**Require index and fraction as bus** in that
block.

**Note**

Use the Fixed-Point Tool data type override option to override bus
objects with new bus objects that replace fixed-point data types
with floating-point data types.

Overridden bus objects used with the Prelookup
block can cause an error because the block does not accept
floating-point data types for the first element in the bus.

If you encounter this issue, use the **Fix**
button to redefine the original bus object and protect it from being
overridden. For example, suppose you define the first element of the
bus object to be an `int32`.

```
myBus.Elements(1).DataType
```

```
int32
```

Clicking the **Fix** button redefines the first
bus element:

```
myBus.Elements(1).DataType = 'fixdt(''int32'',''DataTypeOverride'',''Off'')'
```

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

This parameter displays only when you set **Output
selection** on the **Main**
tab to `Index and fraction as bus`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputBusDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: auto' | 'Bus: <object name>' | '<data type expression>'` |
| **Default:** `'Inherit: auto'` |

### **Breakpoint Minimum** — Minimum value breakpoint data can have `[]` (default) | scalar

Specify the minimum value that the breakpoint data can have. The
default value is `[]` (unspecified).

#### Dependencies

To enable this parameter, set the breakpoints data
**Source** to `Dialog`
on the **Main** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointMin` |
| **Type:** character vector |
| **Value:** scalar |
| **Default:** `'[]'` |

### **Breakpoint Maximum** — Maximum value breakpoint data can have `[]` (default) | scalar

Specify the maximum value that the breakpoint data can have. The
default value is `[]` (unspecified).

#### Dependencies

To enable this parameter, set the breakpoints data
**Source** to `Dialog`
on the **Main** tab.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BreakpointMax` |
| **Type:** character vector |
| **Value:** scalar |
| **Default:** `'[]'` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output** data type you specify on the block. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB rounding function into the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

## Libraries

Simulink / Lookup Tables HDL Coder / Lookup Tables

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `enumerated` | `fixed point` | `integer` | `single` |
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

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

**Required Block Settings**

- **Breakpoint data**: For
  **Source**, select
  `Dialog`.
- **Specification**: You can select either
  `Explicit values` or `Even
  spacing`.
- **Index search method**: Select
  `Evenly spaced points`,
  `Binary search` or `Linear
  search`.
- **Extrapolation method**: Select
  `Clip`.
- **Diagnostic for out-of-range input**: Select
  `Error`.
- **Use last breakpoint for input at or above upper
  limit**: Select this parameter.
- **Breakpoint**: For **Data
  Type**, select `Inherit: Same as
  input`.
- **Integer rounding mode**: Select
  `Zero`,
  `Floor`, or
  `Simplest`.

**Table Data Typing and Sizing**

- It is good practice to structure your table such that the spacing
  between breakpoints is a power of two. If the breakpoint spacing does
  not meet this condition, HDL Coder issues a warning. When the breakpoint spacing is a power
  of two, you can replace division operations in the prelookup step with
  right-shift operations.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

Simulink PLC Coder has limited support for lookup table blocks. The coder does not
support:

- Number of dimensions greater than 2
- Cubic spline interpolation method
- Begin index search using a previous index mode
- Cubic spline extrapolation method

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2006b**

### R2025a: Prelookup block **Remove protection against out-of-range input in generated code** parameter replaced

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

## Description

Compute index and fraction for Interpolation Using Prelookup block

The Prelookup block calculates the index and interval fraction that specify how its
input value `u` relates to the breakpoint data set. The Prelookup block
works best with the Interpolation Using Prelookup block. Feed
the resulting index and fraction values into an Interpolation Using Prelookup block to
interpolate an *n*-dimensional table. These two blocks have
distributed algorithms. When combined together, they perform the same operation as the
integrated algorithm in the n-D Lookup Table block. However, the
Prelookup and Interpolation Using Prelookup blocks offer
greater flexibility and more efficient simulation and code generation than the
n-D Lookup Table block. For more information, see Efficiency of Performance.

### Supported Block Operations

To use the Prelookup block, you must specify a set of breakpoint values. You
choose whether to specify the breakpoint values directly on the dialog box or by
feeding the values to a `bp` input port by setting the
**Source** parameter to `Dialog` or
`Input port`. Typically, this breakpoint data set
corresponds to one dimension of the table data in an Interpolation Using Prelookup
block. The Prelookup block generates a pair of outputs for each input value
`u` by calculating:

- The index of the breakpoint set element that is less than or equal to
  `u` and forms an interval containing
  `u`
- The interval fraction in the range 0 ≤ f < 1, representing the
  normalized position of `u` on the breakpoint interval
  between the index and the next index value for in-range input

For example, if the breakpoint data set is `[0 5 10 20 50 100]`
and the input value `u` is 55, the index is 4 and the fractional
value is 0.1. Labels for the index and interval fraction appear as
**k** and **f** on the Prelookup block icon.
The index value is zero based.

The interval fraction can be negative or greater than `1` for
out-of-range input. See the **Extrapolation method** block
parameter for more information.
