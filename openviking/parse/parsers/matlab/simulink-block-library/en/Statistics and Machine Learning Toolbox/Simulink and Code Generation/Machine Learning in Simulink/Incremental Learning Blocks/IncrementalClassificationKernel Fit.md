---
type: simulink-block
title: 'IncrementalClassificationKernel Fit'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification / Support Vector Machine Classification'
documentation_page: 'incrementalclassificationkernelfit'
documentation_source_path: 'incrementalclassificationkernelfit.html'
language: en
---

# IncrementalClassificationKernel Fit

## Ports

### Input

### **x** — Chunk of predictor data numeric matrix

Chunk of predictor data to which the model is fit, specified as a numeric matrix. The
orientation of the variables and observations is assumed to be `rows`, which
indicates that the observations in the predictor data are oriented along the rows of
**x**.

The length of the observation responses **y** and the number of observations
in **x** must be equal;
**y**`(j)`
is the response of observation *j* (row or
column) in **x**. The following restrictions
apply:

- The number of predictor variables in
  **x** must be equal to the
  `NumPredictors` property value of
  the initial model. If the number of predictor
  variables in the streaming data changes from
  `NumPredictors`, the block issues
  an error.
- The IncrementalClassificationKernel Fit block supports only
  numeric input predictor data. If your input data
  includes categorical data, you must prepare an
  encoded version of the categorical data. Use
  `dummyvar` to convert each categorical
  variable to a numeric matrix of dummy variables.
  Then, concatenate all dummy variable matrices and
  any other numeric predictors. For more details,
  see Dummy Variables.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **y** — Chunk of class labels numeric vector | logical vector | enumerated vector

Chunk of class labels to which the model is trained, specified as a numeric, logical, or enumerated vector. The following restrictions apply:

- The IncrementalClassificationKernel Fit block supports only binary classification.
- The length of the observation responses **y** and the number of observations in **x** must be equal; **y** (`j`) is the response of observation *j* (row or column) in **x**.
- Each label must correspond to one row of the observation matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **w** — Chunk of observation weights vector of positive values

Chunk of observation weights, specified as a vector of positive values. The
IncrementalClassificationKernel Fit block weights the observations in **x** with the
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

Updated parameters of the incremental learning model fit to streaming data
(including `Beta` and `Bias`), returned as a bus
signal (see Composite Signals (Simulink)).

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Select initial machine learning model** — Initial incremental kernel classification model `kernelMdl` (default) | `incrementalClassificationKernel` model object

Specify the name of a workspace variable that contains the configured `incrementalClassificationKernel` model object.

The following restrictions apply:

- The predictor data cannot include
  categorical predictors (`logical`,
  `categorical`, `char`,
  `string`, or `cell`). If you supply
  training data in a table, the predictors must be numeric
  (`double` or `single`). To include
  categorical predictors in a model, preprocess them by using `dummyvar` before fitting the
  model.
- The `ScoreTransform` property of the initial model cannot be
  `"invlogit"` or an anonymous function.
- The `NumPredictors` property of the initial model must be a positive
  integer scalar, and must be equal to the number of predictors in
  **x**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialLearner` |
| **Type:** character vector or string |
| **Values:** `incrementalClassificationKernel` object name |
| **Default:** `"kernelMdl"` |

### **Add input port for observation weights** — Add second input port for observation weights `off` (default) | `on`

Select the check box to include the input port **w** for
observation weights in the IncrementalClassificationKernel Fit block.

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
for the reset signal in the IncrementalClassificationKernel Fit block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowInputReset` |
| **Type:** character vector or string |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

### **Sample time (–1 for inherited)** — Option to specify sample time `–1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of sample
time, such as continuous (`0`) or inherited (`–1`). For more
options, see Types of Sample Time (Simulink).

By default, the IncrementalClassificationKernel Fit block inherits sample time based on the context
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

### **Beta data type** — Data type of linear coefficient estimates `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the linear coefficient estimates (beta) in the
**mdl** output bus signal. The type can be inherited, specified directly,
or expressed as a data type object such as `Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BetaDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Beta data type Minimum** — Minimum value of beta for range checking `[]` (default) | scalar

Specify the lower value of the beta range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as software-in-the-loop (SIL) mode or external mode.
  For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Beta data type Minimum** parameter does not saturate or
clip the actual beta estimate. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BetaOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Beta data type Maximum** — Maximum value of beta for range checking `[]` (default) | scalar

Specify the upper value of the beta range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Beta data type Maximum** parameter does not saturate or
clip the actual beta estimate. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BetaOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Bias data type** — Data type of intercept estimates `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the intercept estimates (bias) in the **mdl**
output bus signal. The type can be inherited, specified directly, or expressed as a data type
object such as `Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BiasDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Bias data type Minimum** — Minimum value of bias for range checking `[]` (default) | scalar

Specify the lower value of the bias range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as software-in-the-loop (SIL) mode or external mode.
  For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Bias data type Minimum** parameter does not saturate or
clip the actual bias estimate. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BiasOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Bias data type Maximum** — Maximum value of bias for range checking `[]` (default) | scalar

Specify the upper value of the bias range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Bias data type Maximum** parameter does not saturate or
clip the actual bias estimate. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BiasOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Kernel data type** — Kernel computation data type `Inherit: Inherit via internal rule` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type of the parameters for Gaussian kernel approximation computation.
The type can be specified directly or expressed as a data type object such as
`Simulink.NumericType`.

When you select `Inherit: Inherit via internal rule`, the
block uses an internal rule to determine the kernel data type. The internal rule chooses
a data type that optimizes numerical accuracy, performance, and generated code size,
while taking into account the properties of the embedded target hardware. The software
cannot always optimize efficiency and numerical accuracy at the same
time.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `KernelDataTypeStr` |
| **Type**: character vector |
| **Values**: `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'uint64'` | `'int64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Kernel data type Minimum** — Minimum kernel computation value for range checking `[]` (default) | scalar

Specify the lower value of the kernel computation internal variable range that
Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Kernel data type Minimum** parameter does not saturate
or clip the actual kernel computation value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `KernelOutMin` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Kernel data type Maximum** — Maximum kernel computation value for range checking `[]` (default) | scalar

Specify the upper value of the kernel computation internal variable range that
Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as SIL
  or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Kernel data type Maximum** parameter does not saturate
or clip the actual kernel computation value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `KernelOutMax` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

#### Additional Data Types

### **Internal states data type** — Data type of internal states `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the internal states in the **mdl** output
bus signal. The type can be inherited, specified directly, or expressed as a data type
object such as `Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `StatesDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Internal states data type Minimum** — Minimum value of internal states for range checking `[]` (default) | scalar

Specify the lower value of the internal states range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as software-in-the-loop (SIL) mode or external mode.
  For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Internal states data type Minimum** parameter does not saturate
or clip the actual internal states. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `StatesOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Internal states data type Maximum** — Maximum value of internal states for range checking `[]` (default) | scalar

Specify the upper value of the internal states range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

The **Internal states data type Maximum** parameter does not saturate
or clip the actual internal states. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `StatesOutMax` |
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

### **Mu data type** — Data type of predictor means `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the predictor means (mu) in the **mdl** output
bus signal. The type can be inherited, specified directly, or expressed as a data type object
such as `Simulink.NumericType`.

If you do not specify `Standardize`=`"true"` when you
create the initial model, then the IncrementalClassificationKernel Fit block sets mu to
`0`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MuDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Mu data type Minimum** — Minimum value of mu for range checking `[]` (default) | scalar

Specify the lower value of the mu range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as software-in-the-loop (SIL) mode or external mode.
  For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Mu data type Minimum** parameter does not saturate or
clip the actual mu value. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MuOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Mu data type Maximum** — Maximum value of mu for range checking `[]` (default) | scalar

Specify the upper value of the mu range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Mu data type Maximum** parameter does not saturate or
clip the actual mu value. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MuOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Sigma data type** — Data type of predictor standard deviations `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the predictor standard deviations (sigma) in the
**mdl** output bus signal. The type can be inherited, specified directly,
or expressed as a data type object such as `Simulink.NumericType`.

If you do not specify `Standardize`=`true` when you
create the initial model, then the IncrementalClassificationKernel Fit block sets sigma to
`0`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SigmaDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Sigma data type Minimum** — Minimum value of sigma for range checking `[]` (default) | scalar

Specify the lower value of the sigma range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as software-in-the-loop (SIL) mode or external mode.
  For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Sigma data type Minimum** parameter does not saturate
or clip the actual sigma value. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SigmaOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Sigma data type Maximum** — Maximum value of sigma for range checking `[]` (default) | scalar

Specify the upper value of the sigma range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and
  Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes, such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Sigma data type Maximum** parameter does not saturate
or clip the actual sigma value. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SigmaOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

## Libraries

Statistics and Machine Learning Toolbox / Incremental Learning / Classification / Kernel

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

### R2025a: New reset inport

The IncrementalClassificationKernel Fit has a new **reset** inport that allows the
resetting of the learned parameters, if any, of the incremental learning model. If any
hyperparameters of the model are estimated during incremental training, those get reset as
well. Use the **reset** signal when performing drift-aware learning to
reset the model parameters when drift is detected.

## Description

Fit incremental kernel classification model

The IncrementalClassificationKernel Fit block fits a configured incremental
model for kernel classification (`incrementalClassificationKernel`) to streaming data.

Import an initial kernel classification model object into the block by specifying the name
of a workspace variable that contains the object. The input port **x**
receives a chunk of predictor data (observations), and the input port **y**
receives a chunk of responses (labels) to which the model is fit. The output port
**mdl** returns an updated
`incrementalClassificationKernel` model. The optional input port
**w** receives a chunk of observation weights and the optional input port **reset** resets
the learned parameters.
