---
type: simulink-block
title: 'IncrementalClassificationKernel Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Incremental Learning / Classification / Kernel'
documentation_page: 'incrementalclassificationkernelpredict'
documentation_source_path: 'incrementalclassificationkernelpredict.html'
language: en
---

# IncrementalClassificationKernel Predict

## Ports
```yaml
ports:
- name: mdl
  summary: Incremental learning model bus signal
  direction: input
- name: x
  summary: Chunk of predictor data numeric matrix
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: label
  summary: Chunk of predicted class labels column vector
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: score
  summary: Predicted class scores or posterior probabilities matrix
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: CanPredict
  summary: Model status 0 (false) | 1(true)
  direction: output
```

### Input

### **mdl** — Incremental learning model bus signal

Incremental learning model (`incrementalClassificationKernel`) fit to streaming data, specified as a bus
signal (see Composite Signals (Simulink)).

### **x** — Chunk of predictor data numeric matrix

Chunk of predictor data, specified as a numeric matrix.

**Note**

The block supports only numeric input predictor data. If your input data
includes categorical data, you must prepare an encoded version of the categorical
data. Use `dummyvar` to convert each categorical
variable to a numeric matrix of dummy variables. Then, concatenate all dummy
variable matrices and any other numeric predictors. For more details, see Dummy Variables.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **label** — Chunk of predicted class labels column vector

Chunk of predicted class labels, returned as a column vector. The label
`label(i)` represents the class yielding the highest score for
the observation **x**(`i`). For more details, see
the `label` output argument of the `predict`
object function.

If you specify an estimation period when you create **mdl**, the
predicted class labels are the majority class during the estimation period. This class
which makes up the largest proportion of the training labels in
**x**.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — Predicted class scores or posterior probabilities matrix

Predicted class scores or posterior probabilities, returned as a matrix. If the
model was trained using a logistic learner, the classification scores are posterior
probabilities. The classification score `score(i)` represents the
posterior probability that the observation in **x** belongs to class
`i`. For more details, see Classification Score.

To check the order of the classes, use the `ClassNames`
property of the kernel classification model specified by **Select initial machine
learning model**.

**Note**

If you specify an estimation period when you create **mdl**,
then the predicted class scores are zero during the estimation period.

#### Dependencies

To enable this port, select the check box for **Add output port for predicted
class scores** on the **Main** tab of the Block
Parameters dialog box.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **CanPredict** — Model status `0` (`false`) | `1`(`true`)

Model status for prediction, returned as numeric or logical `0`
(`false`) or `1` (`true`).

**Note**

If you specify an estimation period when you create **mdl**,
then the model status is `0` (`false`) during the
estimation period.

#### Dependencies

To enable this port, select the check box for **Add output port for status of trained machine learning model** on the
**Main** tab of the Block Parameters dialog box.
## Parameters
```yaml
parameters:
- name: Select initial machine learning model
  summary: Initial incremental kernel classification model kernelMdl (default) | incrementalClassificationKernel model object
  group: Main
  block_parameter: InitialLearner
  type: character vector or string
  values: incrementalClassificationKernel object name
  default: '"kernelMdl"'
- name: Add output port for predicted class scores
  summary: Add second output port for predicted class scores off (default) | on
  group: Main
  block_parameter: ShowOutputScore
  type: character vector or string
  values: '"off" | "on"'
  default: '"off"'
- name: Add output port for status of trained machine learning model
  summary: Add third output port for model status off (default) | on
  group: Main
  block_parameter: ShowOutputCanPredict
  type: character vector or string
  values: '"off" | "on"'
  default: '"off"'
- name: Sample time (–1 for inherited)
  summary: Option to specify sample time –1 (default) | scalar
  group: Main
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
- name: Label data type
  summary: 'Data type of label output Inherit: Inherit via back propagation | double | single | half | int8 | uint8 | int16
    | uint16 | int32 | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | Enum: <class name> | <data
    type expression>'
  group: Data Types
  block_parameter: LabelDataTypeStr
  type: character vector
  values: '"Inherit: Inherit via back propagation" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16"
    | "int32" | "uint32" | "int64" | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "Enum: <class name>" |
    "<data type expression>"'
  default: '"Inherit: Inherit via back propagation" (for numeric and logical labels) | "Inherit: auto" (for nonnumeric labels)'
- name: Label data type Minimum
  summary: Minimum value of label output for range checking [] (default) | scalar
  group: Data Types
  block_parameter: LabelOutMin
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Label data type Maximum
  summary: Maximum value of label output for range checking [] (default) | scalar
  group: Data Types
  block_parameter: LabelOutMax
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Score data type
  summary: 'Data type of score output Inherit: auto (default) | double | single | half | int8 | uint8 | int16 | uint16 | int32
    | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: Data Types
  block_parameter: ScoreDataTypeStr
  type: character vector or string
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Score data type Minimum
  summary: Minimum value of score output for range checking [] (default) | scalar
  group: Data Types
  block_parameter: ScoreOutMin
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Score data type Maximum
  summary: Maximum value of score output for range checking [] (default) | scalar
  group: Data Types
  block_parameter: ScoreOutMax
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Kernel data type
  summary: 'Kernel computation data type Inherit: Inherit via internal rule (default) | double | single | half | int8 | uint8
    | int16 | uint16 | int32 | int64 | uint64 | uint32 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: Data Types
  block_parameter: KernelDataTypeStr
  type: character vector
  values: '''double'' | ''single'' | ''half'' | ''int8'' | ''uint8'' | ''int16'' | ''uint16'' | ''int32'' | ''uint32'' | ''uint64''
    | ''int64'' | ''boolean'' | ''fixdt(1,16,0)'' | ''fixdt(1,16,2^0,0)'' | ''<data type expression>'''
  default: '''Inherit: Inherit via internal rule'''
- name: Kernel data type Minimum
  summary: Minimum kernel computation value for range checking [] (default) | scalar
  group: Data Types
  block_parameter: KernelOutMin
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
- name: Kernel data type Maximum
  summary: Maximum kernel computation value for range checking [] (default) | scalar
  group: Data Types
  block_parameter: KernelOutMax
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
- name: Inner product data type
  summary: 'Inner product term of the predicted response Inherit: Inherit via internal rule (default) | double | single |
    half | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) |
    <data type expression>'
  group: Data Types
  block_parameter: InnerProductDataTypeStr
  type: character vector
  values: '"Inherit: Inherit via internal rule" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32"
    | "uint32" | "int64" | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: Inherit via internal rule"'
- name: Inner product data type Minimum
  summary: Minimum of inner product term for range checking [] (default) | scalar
  group: Data Types
  block_parameter: InnerProductOutMin
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Inner product data type Maximum
  summary: Maximum of inner product term for range checking [] (default) | scalar
  group: Data Types
  block_parameter: InnerProductOutMax
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Select initial machine learning model** — Initial incremental kernel classification model `kernelMdl` (default) | `incrementalClassificationKernel` model object

Specify the name of a workspace variable that contains the configured `incrementalClassificationKernel` model object.

When you create the initial model object, the following restrictions apply:

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

### **Add output port for predicted class scores** — Add second output port for predicted class scores `off` (default) | `on`

Select the check box to include the output port **score** in the
IncrementalClassificationKernel Predict block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutputScore` |
| **Type:** character vector or string |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

### **Add output port for status of trained machine learning model** — Add third output port for model status `off` (default) | `on`

Select the check box to include the output port **CanPredict** in
the IncrementalClassificationKernel Predict block. This check box does
not appear if the workspace already contains an incremental kernel classification
model named `kernelMdl`, capable of prediction, when you create the
IncrementalClassificationKernel Predict block. Alternatively, you can
specify to include the output port **CanPredict** by selecting
the IncrementalClassificationKernel Predict block in the Simulink workspace and entering
`set_param(gcb,ShowOutputCanPredict="on")` at the MATLAB® command line.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutputCanPredict` |
| **Type:** character vector or string |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

### **Sample time (–1 for inherited)** — Option to specify sample time `–1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of sample
time, such as continuous (`0`) or inherited (`–1`). For more
options, see Types of Sample Time (Simulink).

By default, the IncrementalClassificationKernel Predict block inherits sample time based on the context
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
MATLAB rounding function.

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

### **Label data type** — Data type of label output `Inherit: Inherit via back propagation` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

Specify the data type for the **label** output. The type can be
inherited, specified as an enumerated data type, or
expressed as a data type object such as `Simulink.NumericType`.

The supported data types depend on the labels used in the model specified by
**Select initial machine
learning model**.

- If the model uses numeric or logical labels, the supported data types are
  `Inherit: Inherit via back propagation` (default),
  `double`, `single`, `half`,
  `int8`, `uint8`, `int16`,
  `uint16`, `int32`,
  `uint32`, `int64`, `uint64`,
  `boolean`, fixed point, and a data type object.
- If the model uses nonnumeric labels, the supported data types are
  `Enum: <class name>` and a data type object.

When you select an inherited option, the software behaves as follows:

- `Inherit: Inherit via back propagation` (default for
  numeric and logical labels) — Simulink automatically determines the **Label data type**
  of the block during data type propagation (see Data Type Propagation (Simulink)). In this case, the block uses the data
  type of a downstream block or signal object.
- `Inherit: auto` (default for nonnumeric labels) — The block
  uses an autodefined enumerated data type variable. For example, suppose the
  workspace variable name specified by **Select initial
  machine learning model** is `myMdl`, and the
  class labels are `class 1` and
  `class 2`. Then, the corresponding
  **label** values are
  `myMdl_enumLabels.class_1` and
  `myMdl_enumLabels.class_2`. The block converts the class
  labels to valid MATLAB identifiers by using the `matlab.lang.makeValidName`
  function.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type
assistant** button  to display the **Data Type
Assistant**, which helps you set the data type attributes. For more
information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LabelDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: Inherit via back propagation"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **Default**: `"Inherit: Inherit via back propagation"` (for numeric and logical labels) | `"Inherit: auto"` (for nonnumeric labels) |

### **Label data type Minimum** — Minimum value of label output for range checking `[]` (default) | scalar

Specify the lower value of the **label** output range that
Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Label data type Minimum** parameter does not saturate
or clip the actual **label** output. To do so, use the Saturation (Simulink) block instead.

#### Dependencies

You can specify this parameter only if the model specified by **Select initial machine
learning model** uses numeric labels.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LabelOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Label data type Maximum** — Maximum value of label output for range checking `[]` (default) | scalar

Specify the upper value of the **label** output range that
Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as SIL or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Label data type Maximum** parameter does not saturate
or clip the actual **label** output. To do so, use the Saturation (Simulink) block instead.

#### Dependencies

You can specify this parameter only if the model specified by **Select initial machine
learning model** uses numeric labels.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LabelOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Score data type** — Data type of score output `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the **score** output. The type can be
inherited, specified directly, or expressed as a data type object such as
`Simulink.NumericType`.

When you select `Inherit: auto`, the block uses a rule that
inherits a data
type.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ScoreDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Score data type Minimum** — Minimum value of score output for range checking `[]` (default) | scalar

Specify the lower value of the **score** output range that
Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Score data type Minimum** parameter does not saturate or clip
the actual **score** output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ScoreOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Score data type Maximum** — Maximum value of score output for range checking `[]` (default) | scalar

Specify the upper value of the **score** output range that
Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as SIL
  or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Score data type Maximum** parameter does not saturate or clip
the actual **score** output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ScoreOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

#### Additional Data Types

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

### **Inner product data type** — Inner product term of the predicted response `Inherit: Inherit via internal rule` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the inner product term of the predicted response. The
type can be inherited, specified directly, or expressed as a data type object such as
`Simulink.NumericType`.

When you select `Inherit: Inherit via internal rule`, the
block uses an internal rule to determine the inner product data type. The internal
rule chooses a data type that optimizes numerical accuracy, performance, and generated
code size, while taking into account the properties of the embedded target hardware.
The software cannot always optimize efficiency and numerical accuracy at the same
time.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InnerProductDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: Inherit via internal rule"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: Inherit via internal rule"` |

### **Inner product data type Minimum** — Minimum of inner product term for range checking `[]` (default) | scalar

Specify the lower value of the inner product term range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Inner product data type Minimum** parameter does not
saturate or clip the actual inner product term value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InnerProductOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Inner product data type Maximum** — Maximum of inner product term for range checking `[]` (default) | scalar

Specify the upper value of the inner product term range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as SIL
  or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Inner product data type Maximum** parameter does not
saturate or clip the actual inner product term value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InnerProductOutMax` |
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

## Description

Classify observations using incremental kernel classification model

The IncrementalClassificationKernel Predict block classifies observations
using a trained kernel classification model returned as the output of an IncrementalClassificationKernel Fit block.

Import an initial kernel classification model object into the
IncrementalClassificationKernel Predict block by specifying the name of a
workspace variable that contains the object. The input port **mdl** receives
a bus signal that represents an incremental learning model fit to streaming data. The input
port **x** receives a chunk of predictor data (observations), and the output
port **label** returns predicted class labels for the chunk. The optional
output port **score** returns the predicted class scores or posterior
probabilities and the optional output port **CanPredict** returns
the prediction status of the trained model.
