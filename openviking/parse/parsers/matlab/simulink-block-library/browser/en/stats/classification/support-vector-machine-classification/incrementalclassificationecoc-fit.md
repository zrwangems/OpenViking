---
type: simulink-block
title: 'IncrementalClassificationECOC Fit'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification / Support Vector Machine Classification'
documentation_page: 'incrementalclassificationecocfit'
documentation_source_path: 'incrementalclassificationecocfit.html'
language: en
---

# IncrementalClassificationECOC Fit

## Ports

### Input

### **x** — Chunk of predictor data numeric matrix

Chunk of predictor data to which the model is fit, specified as a numeric matrix.
The orientation of the variables and observations is specified by **Predictor data observation
dimension**. The default orientation is `rows`, which
indicates that the observations in the predictor data are oriented along the rows of
**x**.

The length of the observation responses **y** and the number of
observations in **x** must be equal;
**y**`(j)` is the
response of observation *j* (row or column) in
**x**.

**Note**

The number of predictor variables in **x** must be equal to the
`NumPredictors` property value of the initial model. If the
number of predictor variables in the streaming data changes from
`NumPredictors`, the block issues an error.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **y** — Chunk of class labels numeric vector | logical vector | enumerated vector

Chunk of class labels to which the model is trained, specified as a numeric, logical, or enumerated vector.

- The length of the observation responses **y** and the number of observations in **x** must be equal; **y**(`j`) is the response of observation *j* (row or column) in **x**.
- Each label must correspond to one row of the array.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **w** — Chunk of observation weights vector of positive values

Chunk of observation weights, specified as a vector of positive values. The
IncrementalClassificationECOC Fit block weights the observations in **x** with the
corresponding values in **w**. The size of **w** must be
equal to the number of observations in **x**.

#### Dependencies

To enable this port, select the check box for
**Add input port for observation
weights** on the
**Main** tab of the Block
Parameters dialog box.

**Data Types:** `single` | `double`

### **reset** — Reset signal `0` (`false`) | `1` (`true`) | numeric scalar

*Since R2025a*

Reset signal, specified as `0` (`false`) or
`1` (`true`) or a numeric scalar. When the
**reset** signal is a positive scalar (greater than 0), the block
resets the learned parameters, if any, of the incremental learning model. If any
hyperparameters of **mdl** are estimated during incremental training,
those get reset as well. `mdl.NumPredictors` are always
preserved.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **mdl** — Updated incremental learning model parameters bus signal

Updated incremental learning model parameters fit to streaming data, returned as a
bus signal (see `Composite Signals` (Simulink)).

## Parameters

### Main

### **Select initial machine learning model** — Initial incremental classification ECOC model `ecocMdl` (default) | `incrementalClassificationECOC` model object

Specify the name of a workspace variable that contains the configured
`incrementalClassificationECOC` model object. The initial model
must have following properties specified:

- The `NumPredictors` property which must be a positive integer scalar
  equal to the number of predictors in **x**.
- The `ClassNames` property.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialLearner` |
| **Type:** workspace variable |
| **Values:** `incrementalClassificationECOC` model object |
| **Default:** `"ecocMdl"` |

### **Add input port for observation weights** — Add second input port for observation weights `off` (default) | `on`

Select the check box to include the input port **w** for
observation weights in the IncrementalClassificationECOC Fit block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowInputWeights` |
| **Type:** character vector |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

### **Add input port for resetting trained learner** — Add input port for resetting trained incremental learner `off` (default) | `on`

*Since R2025a*

Select the check box to include the input port **reset**
for the reset signal in the IncrementalClassificationECOC Fit block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowInputReset` |
| **Type:** character vector or string |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

### **Predictor data observation dimension** — Observation dimension of predictor data `rows` (default) | `columns`

Specify the observation dimension of the predictor data. The default value is
`rows`, which indicates that observations in the predictor data are
oriented along the rows of **x**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ObservationsIn` |
| **Type:** character vector |
| **Values:** `"rows" | "columns"` |
| **Default:** `"rows"` |

### **Sample time (–1 for inherited)** — Option to specify sample time `–1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of sample
time, such as continuous (`0`) or inherited (`–1`). For more
options, see Types of Sample Time (Simulink).

By default, the IncrementalClassificationECOC Fit block inherits sample time based on the context
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

### **Binary learner beta data type** — Data type of linear coefficient estimates output `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the linear coefficient estimates (beta) output. The type
can be inherited, specified as an enumerated data
type, or expressed as a data type object such as
`Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryBetaDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Binary learner beta data type Minimum** — Minimum value of beta for range checking `[]` (default) | scalar

Specify the lower value of the beta output range that Simulink® checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Binary learner beta data type Minimum** parameter does
not saturate or clip the actual beta output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryBetaOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Binary learner beta data type Maximum** — Maximum value of beta for range checking `[]` (default) | scalar

Specify the upper value of the beta output range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as SIL or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Binary learner beta data type Maximum** parameter does
not saturate or clip the actual beta output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryBetaOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Binary learner bias data type** — Data type of intercept estimates output `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the intercept estimates (bias) output. The type can be
inherited, specified as an enumerated data type, or
expressed as a data type object such as `Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryBiasDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Binary learner bias data type Minimum** — Minimum value of bias for range checking `[]` (default) | scalar

Specify the lower value of the bias output range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Binary learner bias data type Minimum** parameter does
not saturate or clip the actual bias output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryBiasOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Binary learner bias data type Maximum** — Maximum value of bias for range checking `[]` (default) | scalar

Specify the upper value of the bias output range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as SIL or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Binary learner bias data type Maximum** parameter does
not saturate or clip the actual bias output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryBiasOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Binary learner internal states data type** — Data type of binary learner internal states output `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the binary learner internal states output. The type can
be inherited, specified as an enumerated data type,
or expressed as a data type object such as `Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryStatesDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Binary learner internal states data type Minimum** — Minimum value of binary learner internal states for range checking `[]` (default) | scalar

Specify the lower value of the binary learner internal states range that
Simulink checks.

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
| **Block Parameter**: `BinaryStatesOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Binary learner internal states data type Maximum** — Maximum value of binary learner internal states for range checking `[]` (default) | scalar

Specify the upper value of the binary learner internal states range that
Simulink checks.

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
| **Block Parameter**: `BinaryStatesOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Prior data type** — Data type of prior term `double` (default) | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the internal prior term. The type can be inherited,
specified directly, or expressed as a data type object such as
`Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PriorDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` |`"<data type expression>"` |
| **Default**: `"double"` |

### **Prior data type Minimum** — Minimum value of prior term for range checking `[]` (default) | scalar

Specify the lower value of the prior term range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as software-in-the-loop (SIL) mode or external mode.
  For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Prior data type Minimum** parameter does not saturate or clip
the actual prior term value. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PriorOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Prior data type Maximum** — Maximum value of prior term for range checking `[]` (default) | scalar

Specify the upper value of the prior term range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

The **Prior data type Maximum** parameter does not saturate or clip
the actual prior term value. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PriorOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Binary learner mu data type** — Data type of binary learner mu output `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the binary learner mu (predictor means) output. The type
can be inherited, specified as an enumerated data
type, or expressed as a data type object such as
`Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Binary MuDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Binary learner mu data type Minimum** — Minimum value of binary learner mu for range checking `[]` (default) | scalar

Specify the lower value of the binary learner mu range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Binary learner mu data type Minimum** parameter does
not saturate or clip the actual mu output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryMuOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Binary learner mu data type Maximum** — Maximum value of binary learner mu for range checking `[]` (default) | scalar

Specify the upper value of the binary learner mu range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Binary learner mu data type Maximum** parameter does
not saturate or clip the actual mu output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryMuOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Binary learner sigma data type** — Data type of binary learner sigma output `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the binary learner sigma (predictor standard deviations)
output. The type can be inherited, specified as an enumerated data
type, or expressed as a data type object such as
`Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Binary SigmaDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"`|`"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Binary learner sigma data type Minimum** — Minimum value of binary learner sigma for range checking `[]` (default) | scalar

Specify the lower value of the binary learner sigma range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Binary learner sigma data type Minimum** parameter does
not saturate or clip the actual sigma output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinarySigmaOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Binary learner sigma data type Maximum** — Maximum value of binary learner sigma for range checking `[]` (default) | scalar

Specify the upper value of the binary learner sigma range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Binary learner sigma data type Maximum** parameter does
not saturate or clip the actual sigma output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinarySigmaOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

## Libraries

Statistics and Machine Learning Toolbox / Incremental Learning / Classification / ECOC

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

**Introduced in R2024a**

### R2025a: New reset inport

The IncrementalClassificationECOC Fit has a new **reset** inport that allows the
resetting of the learned parameters, if any, of the incremental learning model. If any
hyperparameters of the model are estimated during incremental training, those get reset as
well. Use the **reset** signal when performing drift-aware learning to
reset the model parameters when drift is detected.

## Description

Fit incremental ECOC classification model

The IncrementalClassificationECOC Fit block fits a configured incremental
error-correcting output codes (ECOC) classification model (`incrementalClassificationECOC`) for multiclass classification to streaming
data.

Import an initial ECOC classification object into the block by specifying the name of a
workspace variable that contains the object. The input port **x** receives a
chunk of predictor data (observations), and the input port **y** receives a
chunk of responses (labels) to which the model is fit. The output port returns an updated
`incrementalClassificationECOC` model **mdl**. The
optional input port **w** receives a chunk of observation weights and the optional input port **reset** resets
the learned parameters.
