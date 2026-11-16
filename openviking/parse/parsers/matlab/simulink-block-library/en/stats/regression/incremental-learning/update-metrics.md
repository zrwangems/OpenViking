---
type: simulink-block
title: 'Update Metrics'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Regression / Linear Regression / Multiple Linear Regression'
documentation_page: 'updatemetrics'
documentation_source_path: 'updatemetrics.html'
language: en
---

# Update Metrics

## Ports

### Input

### **mdl** — Incremental learning model bus signal

Incremental learning model fit to streaming data, specified as a bus signal (see
`Composite
Signals` (Simulink)).

### **x** — Chunk of predictor data numeric matrix

Chunk of predictor data, specified as a numeric matrix. The orientation of the variables
and observations is specified by **Predictor
data observation dimension**. The default orientation is
`rows`, which indicates that observations in the
predictor data are oriented along the rows of
**x**.

The length of the observation responses **y** and the
number of observations in **x** must be equal;
**y**`(j)`
is the response of observation *j* (row or column) in
**x**.

**Note**

The block supports only numeric input predictor data. If your
input data includes categorical data, you must prepare an encoded
version of the categorical data. Use `dummyvar` to convert
each categorical variable to a numeric matrix of dummy variables.
Then, concatenate all dummy variable matrices and any other numeric
predictors. For more details, see Dummy Variables.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **y** — Chunk of responses (labels) numeric vector | logical vector | enumerated vector

Chunk of responses (labels) for measuring the model performance, specified as a numeric,
logical, or enumerated vector.

The length of the observation responses **y** and the number of
observations in **x** must be equal;
**y**`(j)` is
the response of observation *j* (row or column) in
**x**.

For classification problems:

- Each label must correspond to one row of the array.
- If **y** contains a label that is in
  `mdl.ClassNames`, the block issues an
  error.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **w** — Chunk of observation weights vector of positive values

Chunk of observation weights, specified as a vector of positive values. The
Update Metrics block weights the observations in **x** with the
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

### **IsWarm** — Flag indicating whether model tracks performance metrics logical

Flag indicating whether the incremental model tracks performance metrics, returned as
logical `0` (`false`) or
`1` (`true`).

| Value | Description |
| --- | --- |
| `1 (true)` | The incremental model `mdl` is warm. Consequently, the block tracks performance metrics in the bus signal output. |
| `0 (false)` | The block does not track performance metrics. |

### **metrics** — Model performance metrics matrix

Model performance metrics updated during incremental learning, returned as a matrix with
two columns and *m* rows, where *m* is
the number of observations in **x**. Specify the
performance metrics using **Model
performance metrics to track**. The block ignores the
metrics specified by the `Metrics` property of
**mdl**.

The columns of **metrics** are:

- **`Cumulative`** — Model
  performance from the time the model becomes warm (`IsWarm` is `1`).
- **`Window`**
  — Model performance evaluated over all observations within
  the window specified by the
  `MetricsWindowSize` property of
  **mdl**. The software updates
  `Window` after it processes
  `MetricsWindowSize`
  observations.

**Data Types:** `matrix`

## Parameters

### Main

### **Select initial machine learning model** — Initial incremental learning model `Mdl` (default) | `incrementalRegressionLinear` model object | `incrementalClassificationLinear` model object | `incrementalClassificationECOC` model object

Specify the name of a workspace variable that contains the configured `incrementalRegressionLinear`, `incrementalClassificationLinear`, or `incrementalClassificationECOC` model object.

- The predictor data
  cannot include categorical predictors
  (`logical`,
  `categorical`, `char`,
  `string`, or `cell`).
  If you supply training data in a table, the predictors must
  be numeric (`double` or
  `single`). To include categorical
  predictors in a model, preprocess them by using `dummyvar`
  before fitting the model.
- The `NumPredictors` property of the initial
  model must be a positive integer scalar, and must be equal to
  the number of predictors in **x**.
- The `ScoreTransform` property of the
  initial model (classification only) cannot be
  `"invlogit"` or an anonymous
  function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialLearner` |
| **Type:** workspace variable |
| **Values:** `incrementalRegressionLinear` model object, `incrementalClassificationLinear` model object, `incrementalClassificationECOC` model object |
| **Default:** `"Mdl"` |

### **Model performance metrics to track** — Performance metrics function `classiferror` (default) | `binodeviance` | `exponential` | `hinge` | `logit` | `quadratic` | `mse` | `epsiloninsensitive`

Loss function for cumulative and window performance metrics to track
during incremental learning. For more details on loss functions, see
`loss`.

The following table lists the built-in loss function names:

- For Regression Models:

  | Name | Description |
  | --- | --- |
  | `"mse"` | Weighted mean squared error |
  | `"epsiloninsensitive"` | Epsilon-insensitive error |

  Default is `"epsiloninsensitive"` for
  regression models.
- For Classification Models:

  | Name | Description |
  | --- | --- |
  | `"binodeviance"` | Binomial deviance |
  | `"classiferror"` | Misclassification error rate |
  | `"exponential"` | Exponential |
  | `"hinge"` | Hinge |
  | `"logit"` | Logistic |
  | `"quadratic"` | Quadratic |

  **Note**

  You can only specify `"classiferror"` for
  `incrementalClassificationECOC`
  models.

The Update Metrics block ignores the metrics specified by the
`Metric` property of
**mdl**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Metric` |
| **Type:** character vector |
| **Values:** `"classiferror" | "binodeviance" | "exponential" | "hinge" | "logit" | "quadratic" | "mse" | "epsiloninsensitive"` |
| **Default:** `"classiferror"` (for classification models) | `"epsiloninsensitive"` (for regression models) |

### **Add input port for observation weights** — Add second input port for observation weights `off` (default) | `on`

Select the check box to include the input port **w** for
observation weights in the Update Metrics block.

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
for the reset signal in the Update Metrics block.

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

By default, the Update Metrics block inherits sample time based on the context
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

### **Metrics data type** — Data type of metrics output `double` (default) | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the metrics output. The type can be inherited, specified
directly, or expressed as a data type object such as
`Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button
 to display the **Data Type
Assistant**, which helps you set the data type attributes.
For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MetricsDataTypeStr` |
| **Type**: character vector |
| **Values**: `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"double"` |

### **Metrics data type Minimum** — Minimum value of metrics for range checking `[]` (default) | scalar

Specify the lower value of the metrics output range that Simulink® checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model.
  This optimization can remove algorithmic code and affect the
  results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more
  information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Metrics data type Minimum** parameter
does not saturate or clip the actual metrics output. To do so,
use the Saturation (Simulink) block
instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MetricsOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Metrics data type Maximum** — Maximum value of metrics for range checking `[]` (default) | scalar

Specify the upper value of the metrics output range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model.
  This optimization can remove algorithmic code and affect the
  results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more
  information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Metrics data type Maximum** parameter
does not saturate or clip the actual metrics output. To do so,
use the Saturation (Simulink) block
instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `MetricsOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Predict response data type** — Data type of predict response `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the response output from the predict block (IncrementalRegressionLinear Predict, IncrementalClassificationLinear Predict, IncrementalClassificationECOC Predict etc.) that is internal to the Update Metrics block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

When you select `Inherit: auto`, the block uses a rule that inherits a data type.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant** button  to display the **Data Type Assistant**, which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PredictResponseDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Predict response data type Minimum** — Minimum value of predict response for range checking `[]` (default) | scalar

Specify the lower value of the internal predict response output range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can remove algorithmic code and affect the results of some simulation modes, such as software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Predict response data type Minimum** parameter does not
saturate or clip the actual predict response output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PredictResponseOutMin` |
| **Type**: string or numeric scalar |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Predict response data type Maximum** — Maximum value of predict response for range checking `[]` (default) | scalar

Specify the upper value of the internal predict response output range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can remove algorithmic code and affect the results of some simulation modes, such as software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Predict response data type Maximum** parameter does not
saturate or clip the actual predict response output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PredictResponseOutMax` |
| **Type**: string or numeric scalar |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Loss data type** — Data type of loss output `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the loss value output used internally by the Update Metrics block to evaluate the cumulative loss and the loss over the window specified by the `MetricsWindowSize` property of **mdl**. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

When you select `Inherit: auto`, the block uses a rule that inherits a data type.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant** button  to display the **Data Type Assistant**, which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LossDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Loss data type Minimum** — Minimum value of loss for range checking `[]` (default) | scalar

Specify the lower value of the internal loss output range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can remove algorithmic code and affect the results of some simulation modes, such as software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LossOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Loss data type Maximum** — Maximum value of loss for range checking `[]` (default) | scalar

Specify the upper value of the internal loss output range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can remove algorithmic code and affect the results of some simulation modes, such as software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LossOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Additional predict data type** — Additional predict data type `Inherit: Inherit via internal rule` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the additional response output from the predict block (IncrementalRegressionLinear Predict, IncrementalClassificationLinear Predict, or IncrementalClassificationECOC Predict) that is internal to the Update Metrics block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

When you select `Inherit: Inherit via internal rule`, the block uses an internal rule to determine the additional predict data type. The internal rule chooses a data type that optimizes numerical accuracy, performance, and generated code size, while taking into account the properties of the embedded target hardware. The software cannot always optimize efficiency and numerical accuracy at the same time.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AdditionalPredictDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: Inherit via internal rule"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: Inherit via internal rule"` |

### **Additional predict data type Maximum** — Maximum value of additional predict for range checking `[]` (default) | scalar

Specify the upper value of the additional predict output range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can remove algorithmic code and affect the results of some simulation modes, such as software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Additional predict data type Maximum** parameter does not
saturate or clip the actual additional predict. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AdditionalPredictOutMax` |
| **Type**: string or numeric scalar |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Additional loss data type** — Additional loss data type `Inherit: Inherit via internal rule` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for additional operations on the loss value used internally by the
Update Metrics block to evaluate the cumulative loss and
the loss over the window specified by the
`MetricsWindowSize` property of
**mdl**. The type can be inherited, specified
directly, or expressed as a data type object such as
`Simulink.NumericType`.

When you select `Inherit: Inherit via internal
rule`, the block uses an internal rule to determine the
additional loss data type. The internal rule chooses a data type that
optimizes numerical accuracy, performance, and generated code size,
while taking into account the properties of the embedded target
hardware. The software cannot always optimize efficiency and numerical
accuracy at the same
time.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AdditionalLossDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: Inherit via internal rule"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: Inherit via internal rule"` |

### **Additional loss data type Minimum** — Minimum value of additional loss for range checking `[]` (default) | scalar

Specify the lower value of the additional loss output range that
Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model.
  This optimization can remove algorithmic code and affect the
  results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more
  information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AdditionalLossOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Additional loss data type Maximum** — Maximum value of additional loss for range checking `[]` (default) | scalar

Specify the upper value of the additional loss output range that
Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model.
  This optimization can remove algorithmic code and affect the
  results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more
  information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AdditionalLossOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

## Libraries

Statistics and Machine Learning Toolbox / Incremental Learning

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

**Introduced in R2023b**

### R2025a: New reset inport

The Update Metrics has a new **reset** inport that allows the
resetting of the learned parameters, if any, of the incremental learning model. If any
hyperparameters of the model are estimated during incremental training, those get reset as
well. Use the **reset** signal when performing drift-aware learning to
reset the model parameters when drift is detected.

## Description

Update performance metrics in incremental learning model given new data

The Update Metrics block outputs the performance metrics of a configured
incremental model for binary classification (`incrementalClassificationLinear`), multiclass classification (`incrementalClassificationECOC`), or linear regression (`incrementalRegressionLinear`), given new data.

Import a trained incremental learning model object into the block by specifying the name of
a workspace variable that contains the object. The input port **mdl**
receives a bus signal that represents an incremental learning model fit to streaming
data. The input port **x** receives a chunk of predictor data
(observations), and the input port **y** receives a chunk of responses
or labels for measuring the model performance. The output port
**IsWarm** returns a value indicating if the model is warm, which
means that it tracks performance metrics. The output port **metrics**
returns the computed performance metrics. The optional input port **w**
receives a chunk of observation weights and the
optional input port **reset** resets the learned parameters
.
