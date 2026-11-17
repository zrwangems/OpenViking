---
type: simulink-block
title: 'Per Observation Loss'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Incremental Learning / Drift Detection'
documentation_page: 'perobservationloss'
documentation_source_path: 'perobservationloss.html'
language: en
---

# Per Observation Loss

## Ports
```yaml
ports:
- name: mdl
  summary: Incremental learning model bus signal
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: x
  summary: Chunk of predictor data numeric matrix
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: y
  summary: Chunk of responses (labels) numeric vector | logical vector | enumerated vector
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: IsWarm
  summary: Flag indicating whether model tracks performance metrics logical
  direction: output
- name: loss
  summary: Per observation error numeric matrix
  direction: output
```

### Input

### **mdl** — Incremental learning model bus signal

Incremental learning model fit to streaming data, specified as a bus signal (see
`Composite Signals` (Simulink)).

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **x** — Chunk of predictor data numeric matrix

Chunk of predictor data, specified as a numeric matrix. The orientation of the
variables and observations is specified by **Predictor data observation
dimension**. The default orientation is `rows`, which
indicates that observations in the predictor data are oriented along the rows of
**x**.

The length of the observation responses **y** and the number of
observations in **x** must be equal;
**y**`(j)` is the
response of observation *j* (row or column) in
**x**.

The block supports only numeric input predictor data. If your input data includes
categorical data, you must prepare an encoded version of the categorical data. Use
`dummyvar` to convert each categorical
variable to a numeric matrix of dummy variables. Then, concatenate all dummy variable
matrices and any other numeric predictors. For more details, see Dummy Variables.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **y** — Chunk of responses (labels) numeric vector | logical vector | enumerated vector

Chunk of responses (labels) for measuring the model performance, specified as a
numeric, logical, or enumerated vector.

The length of the observation responses **y** and the number of
observations in **x** must be equal;
**y**`(j)` is the response of
observation *j* (row or column) in **x**.

For classification problems:

- Each label must correspond to one row of the array.
- If **y** contains a label that is not in
  `mdl.ClassNames`, the block issues an error.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`
### Output

### **IsWarm** — Flag indicating whether model tracks performance metrics logical

Flag indicating whether the incremental model tracks performance metrics, returned
as logical `0` (`false`) or `1`
(`true`).

| Value | Description |
| --- | --- |
| `1 (true)` | The incremental model `mdl` is warm. Consequently, the block tracks performance metrics in the bus signal output. |
| `0 (false)` | The block does not track performance metrics. |

### **loss** — Per observation error numeric matrix

Per observation regression or classification error of the model predictions using
the predictors in **x** and true observed values in
**y**, returned as a numeric matrix. The matrix is of size
*nchunk*-by-*nobs* where *nchunk*
is the total number of chunks and *nobs* is the number of
observations in a chunk of **x**. The loss is `-1`
if **IsWarm** is `false`.

Specify the loss function to compute the error using **Loss
function**.
## Parameters
```yaml
parameters:
- name: Select initial machine learning model
  summary: Initial incremental learning model initMdl (default)
  group: ''
  block_parameter: InitialLearner
  type: character vector or string
  values: workspace model object name
  default: '"initMdl"'
- name: Loss function
  summary: Loss function to compute the per observation loss classiferror (default) | binodeviance | exponential | hinge |
    logit | quadratic | squarederror | epsiloninsensitive
  group: ''
  block_parameter: LossFun
  type: character vector or string
  values: '"classiferror" | "binodeviance" | "exponential" | "hinge" | "logit" | "quadratic" | "squarederror" | "epsiloninsensitive"'
  default: '"classiferror" for classification models and "squarederror" for regression models'
- name: Predictor data observation dimension
  summary: Observation dimension of predictor data rows (default) | columns
  group: ''
  block_parameter: ObservationsIn
  type: character vector
  values: '"rows" | "columns"'
  default: '"rows"'
- name: Sample time (–1 for inherited)
  summary: Option to specify sample time –1 (default) | scalar
  group: ''
  block_parameter: SystemSampleTime
  type: string scalar or character vector
  values: scalar
  default: '"–1"'
- name: Integer rounding mode
  summary: Rounding mode for fixed-point operations Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest |
    Zero
  group: Data Types
  block_parameter: RndMeth
  type: character vector
  values: '"Ceiling" | "Convergent" | "Floor" | "Nearest" | "Round" | "Simplest" | "Zero"'
  default: '"Floor"'
- name: Saturate on integer overflow
  summary: Method of overflow action off (default) | on
  group: Data Types
  block_parameter: SaturateOnIntegerOverflow
  type: character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Lock output data type setting against changes by the fixed-point tools
  summary: Prevention of fixed-point tools from overriding data type off (default) | on
  group: Data Types
  block_parameter: LockScale
  type: character vector
  values: '"off" | "on"'
  default: '"off"'
- name: Loss data type
  summary: Data type of loss output double (default) | single | half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64
    | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>
  group: Data Types
  block_parameter: LossDataTypeStr
  type: character vector or string
  values: '"double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64" | "uint64"
    | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"double"'
- name: Loss data type Minimum
  summary: Minimum value of loss output for range checking [] (default) | scalar
  group: Data Types
  block_parameter: LossOutMin
  type: string or numeric scalar
  values: '"[]" | scalar'
  default: '"[]"'
- name: Loss data type Maximum
  summary: Maximum value of loss output for range checking [] (default) | scalar
  group: Data Types
  block_parameter: LossOutMax
  type: string or numeric scalar
  values: '"[]" | scalar'
  default: '"[]"'
- name: Predict response data type
  summary: 'Data type of predict response Inherit: auto (default) | double | single | half | int8 | uint8 | int16 | uint16
    | int32 | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: Data Types
  block_parameter: PredictResponseDataTypeStr
  type: character vector or string
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Predict response data type Minimum
  summary: Minimum value of predict response for range checking [] (default) | scalar
  group: Data Types
  block_parameter: PredictResponseOutMin
  type: string or numeric scalar
  values: '"[]" | scalar'
  default: '"[]"'
- name: Predict response data type Maximum
  summary: Maximum value of predict response for range checking [] (default) | scalar
  group: Data Types
  block_parameter: PredictResponseOutMax
  type: string or numeric scalar
  values: '"[]" | scalar'
  default: '"[]"'
- name: Additional predict data type
  summary: 'Additional predict data type Inherit: Inherit via internal rule (default) | double | single | half | int8 | uint8
    | int16 | uint16 | int32 | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: Data Types
  block_parameter: AdditionalPredictDataTypeStr
  type: character vector
  values: '"Inherit: Inherit via internal rule" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32"
    | "uint32" | "int64" | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: Inherit via internal rule"'
- name: Additional predict data type Minimum
  summary: Minimum value of additional predict for range checking [] (default) | scalar
  group: Data Types
  block_parameter: AdditionalPredictOutMin
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Additional predict data type Maximum
  summary: Maximum value of additional predict for range checking [] (default) | scalar
  group: Data Types
  block_parameter: AdditionalPredictOutMax
  type: string or numeric scalar
  values: '"[]" | scalar'
  default: '"[]"'
- name: Linear sum data type
  summary: 'Data type of linear sum Inherit: Inherit via internal rule (default) | double | single | half | int8 | uint8 |
    int16 | uint16 | int32 | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: Data Types
  block_parameter: LinearSumDataTypeStr
  type: character vector or string
  values: 'Inherit: Inherit via internal rule | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32"
    | "uint32" | "int64" | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: 'Inherit: Inherit via internal rule'
- name: Linear sum data type Minimum
  summary: Minimum value of linear sum for range checking [] (default) | scalar
  group: Data Types
  block_parameter: LinearSumOutMin
  type: string or numeric scalar
  values: '"[]" | scalar'
  default: '"[]"'
- name: Linear sum data type Maximum
  summary: Maximum value of linear sum for range checking [] (default) | scalar
  group: Data Types
  block_parameter: LinearSumOutMax
  type: string or numeric scalar
  values: '"[]" | scalar'
  default: '"[]"'
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Select initial machine learning model** — Initial incremental learning model `initMdl` (default)

Specify the name of a workspace variable that contains the configured model object.
You can use the following objects:

- `incrementalRegressionLinear`
- `incrementalClassificationLinear`
- `incrementalClassificationECOC`
- `incrementalClassificationKernel`
- `incrementalRegressionKernel`
- `incrementalDriftAwareLearner`

If a drift-aware model object is provided, the block will use the incremental
learning model inside it.

The following constraints apply:

- The predictor data cannot include
  categorical predictors (`logical`,
  `categorical`, `char`,
  `string`, or `cell`). If you supply training
  data in a table, the predictors must be numeric (`double` or
  `single`). To include categorical predictors in a model,
  preprocess them by using `dummyvar` before fitting the
  model.
- The `NumPredictors` property of the initial model must be a
  positive integer scalar, and must be equal to the number of predictors in
  **x**.
- The `ScoreTransform` property of the initial model
  (classification only) cannot be `"invlogit"` or an anonymous
  function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialLearner` |
| **Type:** character vector or string |
| **Values:** workspace model object name |
| **Default:** `"initMdl"` |

### **Loss function** — Loss function to compute the per observation loss `classiferror` (default) | `binodeviance` | `exponential` | `hinge` | `logit` | `quadratic` | `squarederror` | `epsiloninsensitive`

Specify the loss function to compute the per observation loss during incremental
learning. For more details on loss functions, see `loss`.

The following table lists the built-in loss function names:

- For Regression Models:

  | Name | Description |
  | --- | --- |
  | `"squarederror"` | Squared error |
  | `"epsiloninsensitive"` | Epsilon-insensitive error |

  Default is `"squarederror"` for regression models.
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
  `incrementalClassificationECOC` models.

The Per Observation Loss block ignores the metrics specified by the
`Metric` property of **mdl**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LossFun` |
| **Type:** character vector or string |
| **Values:** `"classiferror" | "binodeviance" | "exponential" | "hinge" | "logit" | "quadratic" | "squarederror" | "epsiloninsensitive"` |
| **Default:** `"classiferror"` for classification models and `"squarederror"` for regression models |

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

By default, the Per Observation Loss block inherits sample time based on the context
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

### **Loss data type** — Data type of loss output `double` (default) | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the loss output. The type can be specified directly or
expressed as a data type object such as `Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LossDataTypeStr` |
| **Type**: character vector or string |
| **Values**: | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"double"` |

### **Loss data type Minimum** — Minimum value of loss output for range checking `[]` (default) | scalar

Specify the lower value of the loss output range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Loss data type Minimum** parameter does not saturate or
clip the actual loss output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LossOutMin` |
| **Type**: string or numeric scalar |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Loss data type Maximum** — Maximum value of loss output for range checking `[]` (default) | scalar

Specify the upper value of the loss output range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Loss data type Maximum** parameter does not saturate or
clip the actual loss output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LossOutMax` |
| **Type**: string or numeric scalar |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Predict response data type** — Data type of predict response `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the response output from the predict block (IncrementalRegressionLinear Predict, IncrementalClassificationLinear Predict, IncrementalClassificationECOC Predict etc.) that is internal to the Per Observation Loss block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

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

#### Additional Data Types

### **Additional predict data type** — Additional predict data type `Inherit: Inherit via internal rule` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the additional response output from the predict block (IncrementalRegressionLinear Predict, IncrementalClassificationLinear Predict, or IncrementalClassificationECOC Predict) that is internal to the Per Observation Loss block. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

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

### **Additional predict data type Minimum** — Minimum value of additional predict for range checking `[]` (default) | scalar

Specify the lower value of the additional predict output range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can remove algorithmic code and affect the results of some simulation modes, such as software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Additional predict data type Minimum** parameter does not
saturate or clip the actual additional predict. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `AdditionalPredictOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

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

### **Linear sum data type** — Data type of linear sum `Inherit: Inherit via internal rule` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the internal linear sum. The type can be inherited,
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
| **Block Parameter**: `LinearSumDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `Inherit: Inherit via internal rule` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `Inherit: Inherit via internal rule` |

### **Linear sum data type Minimum** — Minimum value of linear sum for range checking `[]` (default) | scalar

Specify the lower value of the linear sum range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Linear sum data type Minimum** parameter does not saturate
or clip the actual linear sum. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LinearSumOutMin` |
| **Type**: string or numeric scalar |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Linear sum data type Maximum** — Maximum value of linear sum for range checking `[]` (default) | scalar

Specify the upper value of the linear sum range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Linear sum data type Maximum** parameter does not saturate
or clip the actual linear sum. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LinearSumOutMax` |
| **Type**: string or numeric scalar |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |
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

**Introduced in R2025a**

## Description

Per observation regression or classification error of incremental model

The Per Observation Loss block outputs the per observation regression or
classification error of a configured incremental model, given predictor data
**x** and ground-truth responses (labels) **y**.

Import a trained incremental learning or incremental drift-aware model object into the
block by specifying the name of a workspace variable that contains the object. The input port
**mdl** receives a bus signal that represents an incremental learning model
fit to streaming data. The input port **x** receives a chunk of predictor
data (observations), and the input port **y** receives a chunk of responses
or labels for measuring the model loss. The output port **IsWarm** returns a
value indicating if the model is warm, which means that it is computing the loss. The output
port **loss** returns the computed loss.
