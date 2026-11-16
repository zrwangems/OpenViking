---
type: simulink-block
title: 'Detect Drift'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Incremental Learning / Drift Detection'
documentation_page: 'detectdriftblock'
documentation_source_path: 'detectdriftblock.html'
language: en
---

# Detect Drift

## Ports

### Input

### **x** — Input data n-by-1 numeric vector | logical vector

Input data, specified as an *n*-by-1 numeric
vector, where *n* is the number of observations, or
as a logical vector. During initialization of the model:

- If the `InputType` value in the call to `incrementalConceptDriftDetector` is
  `"continuous"`, then **x** must be a numeric
  vector.
- If the `InputType` value in the call to
  `incrementalConceptDriftDetector` is
  `"binary"`, then **x** can be a logical
  vector.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **reset** — Reset signal numeric or | `0` (`false`) | `1`(`true`)

Reset signal, specified as `0` (`false`) or
`1`(`true` or a numeric scalar. When the
**reset** signal is a positive scalar (greater than 0), the drift
detector resets the internal states of the `incrementalConceptDriftDetector`, including
`PreviousDriftStatus` and `DriftStatus`. After a
drift is detected in the data, the block resets the detector using a user-defined
reset logic subsystem.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **w** — Observation weights n-by-1 numeric vector

Observation weights, specified as a numeric vector. The Detect Drift
block weights the observations in **x** with the corresponding values
in **w**. The size of **w** must be equal to the
number of observations in **x**.

You cannot provide observation weights for the Hoeffding's Bounds Drift Detection
Method using exponentially weighted moving averages (HDDMW). To use observation
weights, specify the `DetectionMethod` as `"ddm"` or
`"hddma"` in the call to `incrementalConceptDriftDetector`.

#### Dependencies

To enable this port, select the check box for **Add input port for
observation weights** on the **Main** tab of the
Block Parameters dialog box.

**Data Types:** `single` | `double`
### Output

### **IsWarm** — Flag indicating whether block tracks drift status `0` (`false`) | `1`(`true`)

Flag indicating whether the Detect Drift block tracks the drift
status, returned as logical `0` (`false`) or
`1` (`true`).

| Value | Description |
| --- | --- |
| `1 (true)` | The `incrementalConceptDriftDetector` object is warm. Consequently, the block tracks the drift status in the signal output. |
| `0 (false)` | The `incrementalConceptDriftDetector` object is not warm. Consequently, the block only updates the internal statistics and does not track the drift status. |

**Data Types:** `Boolean`

### **status** — Current drift status `0` (stable) | `1` (warning) | `2` (drift)

Current drift status, specified as `0` (stable, or no drift),
`1` (drift warning) or `2` (drift
detected).

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Select concept drift detector** — Initial incremental concept drift detector `IncCDDetector` (default) | `incrementalConceptDriftDetector` object

Specify the name of a workspace variable that contains the configured `incrementalConceptDriftDetector` object.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DriftDetector` |
| **Type:** character vector or string |
| **Values:** `incrementalConceptDriftDetector` object name |
| **Default:** `"IncCDDetector"` |

### **Add input port for observation weights** — Add third input port for observation weights `off` (default) | `on`

Select the check box to include the input port **w**
for observation weights in the Detect Drift block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowInputWeights` |
| **Type:** character vector |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

### **Sample time (–1 for inherited)** — Option to specify sample time `–1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of sample
time, such as continuous (`0`) or inherited (`–1`). For more
options, see Types of Sample Time (Simulink).

By default, the Detect Drift block inherits sample time based on the context
of the block within the model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SystemSampleTime` |
| **Type:** string scalar or character vector |
| **Values:** scalar |
| **Default:** `"–1"` |

### Data Types

#### Fixed-Point Operational Parameters

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression into the mask field using a
MATLAB® rounding function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"` |
| **Default:** `"Floor"` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

| Action | Rationale | Impact on Overflows | Example |
| --- | --- | --- | --- |
| Select this check box (`on`). | Your model has possible overflow, and you want explicit saturation protection in the generated code. | Overflows saturate to either the minimum or maximum value that the data type can represent. | The maximum value that the `int8` (signed 8-bit integer) data type can represent is 127. Any block operation result greater than this maximum value causes overflow of the 8-bit integer. With the check box selected, the block output saturates at 127. Similarly, the block output saturates at a minimum output value of –128. |
| Clear this check box (`off`). | You want to optimize the efficiency of your generated code.  You want to avoid overspecifying how a block handles out-of-range signals. For more information, see Troubleshoot Signal Range Errors (Simulink). | Overflows wrap to the appropriate value that the data type can represent. | The maximum value that the `int8` (signed 8-bit integer) data type can represent is 127. Any block operation result greater than this maximum value causes overflow of the 8-bit integer. With the check box cleared, the software interprets the value causing the overflow as `int8`, which can produce an unintended result. For example, a block result of 130 (binary 1000 0010) expressed as `int8` is –126. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SaturateOnIntegerOverflow` |
| **Type:** character vector |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

### **Lock output data type setting against changes by the fixed-point tools** — Prevention of fixed-point tools from overriding data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data type
you specify for the block. For more information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

#### Data Type

### **Drift status data type** — Data type of drift status output `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the drift **status**
output. The type can be inherited, specified directly, or expressed as a data type
object such as `Simulink.NumericType`.

When you select `Inherit: auto`, the block uses a rule that
inherits the data type.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DriftStatusDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Drift status data type Minimum** — Minimum value of drift status output for range checking `[]` (default) | scalar

Specify the lower value of the drift **status** range
that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DriftStatusOutMin` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Drift status data type Maximum** — Maximum value of drift status output for range checking `[]` (default) | scalar

Specify the upper value of the drift **status** range
that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DriftStatusOutMax` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Mean data type** — Data type of mean `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type of the mean (moving average of input observations). The type
can be inherited, specified directly, or expressed as a data type object such as
`Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MeanDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Mean data type Minimum** — Minimum value of mean for range checking `[]` (default) | scalar

Specify the lower value of the mean range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MeanOutMin` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Mean data type Maximum** — Maximum value of mean for range checking `[]` (default) | scalar

Specify the upper value of the mean range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MeanOutMax` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Variance data type** — Data type of variance `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type of the variance (moving variance of input observations). The
type can be inherited, specified directly, or expressed as a data type object such as
`Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `VarianceDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Variance data type Minimum** — Minimum value of variance for range checking `[]` (default) | scalar

Specify the lower value of the variance range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `VarianceOutMin` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Variance data type Maximum** — Maximum value of variance for range checking `[]` (default) | scalar

Specify the upper value of the variance range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `VarianceOutMax` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Weights sum data type** — Data type of weights sum `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type of the weights sum (moving sum of weighted input
observations). The type can be inherited, specified directly, or expressed as a data
type object such as `Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `WeightsSumDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Weights sum data type Minimum** — Minimum value of weights sum for range checking `[]` (default) | scalar

Specify the lower value of the weights sum range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `WeightsSumOutMin` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Weights sum data type Maximum** — Maximum value of weights sum for range checking `[]` (default) | scalar

Specify the upper value of the weights sum range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `WeightsSumOutMax` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

## Libraries

Statistics and Machine Learning Toolbox / Incremental Learning / Drift Detection

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2024b**

## Description

Update drift detector states and drift status with new data

The Detect Drift block updates the internal statistics and drift status of
a drift detector when given new data.

Import an initialized incremental concept drift detector object (`incrementalConceptDriftDetector`) into the block by specifying the name of a
workspace variable that contains the object. The input port **x** receives a
data stream for which the drift is evaluated. The input port **reset**
receives a signal that resets the internal states of the drift detector. The output port
**IsWarm** returns a value indicating if the drift detector is warm, which
means that it tracks the drift status. The output port **status** returns the
current drift status. The optional input port **w** receives observation
weights.
