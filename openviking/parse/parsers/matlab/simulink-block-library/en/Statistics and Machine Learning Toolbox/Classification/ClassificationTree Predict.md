---
type: simulink-block
title: 'ClassificationTree Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification'
documentation_page: 'classificationtreepredict'
documentation_source_path: 'classificationtreepredict.html'
language: en
---

# ClassificationTree Predict

## Ports
```yaml
ports:
- name: x
  summary: Predictor data row vector | column vector
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: label
  summary: Predicted class label scalar
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: score
  summary: Predicted class scores or posterior probabilities row vector
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### Input

### **x** — Predictor data row vector | column vector

Predictor data, specified as a row or column vector of one observation.

The variables in **x** must have the same order as the
predictor variables that trained the model specified by **Select
trained machine learning model**.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **label** — Predicted class label scalar

Predicted class label, returned as a scalar. The predicted class is the class that
minimizes the expected classification cost. For more details, see the More About
section of the `predict` function reference page.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — Predicted class scores or posterior probabilities row vector

Predicted class scores or posterior probabilities, returned as a row vector of
size 1-by-*k*, where *k* is the number of classes in
the tree model.

The classification score of a leaf node is the posterior probability of the
classification at the node. The posterior probability of the classification at a node
is the number of training observations that lead to the node with the classification,
divided by the number of training observations that lead to the node.

To check the order of the classes, use the `ClassNames`
property of the tree model specified by **Select trained machine
learning model**.

#### Dependencies

To enable this port, select the check box for **Add output port for predicted
class scores** on the **Main** tab of the Block
Parameters dialog box.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Select trained machine learning model
  summary: Classification tree model treeMdl (default) | ClassificationTree object | CompactClassificationTree object
  group: Main
  block_parameter: TrainedLearner
  type: workspace variable
  values: ClassificationTree object | CompactClassificationTree object
  default: '''treeMdl'''
- name: Add output port for predicted class scores
  summary: Add second output port for predicted class scores off (default) | on
  group: Main
  block_parameter: ShowOutputScore
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
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
  summary: 'Data type of label output Inherit: Inherit via back propagation | Inherit: auto | double | single | half | int8
    | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | Enum: <class
    name> | <data type expression>'
  group: Data Types
  block_parameter: LabelDataTypeStr
  type: character vector or string
  values: '"Inherit: Inherit via back propagation" | "Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16"
    | "uint16" | "int32" | "uint32" | "int64" | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "Enum: <class
    name>" | "<data type expression>"'
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
- name: Raw score data type
  summary: 'Untransformed score data type Inherit: auto (default) | double | single | half | int8 | uint8 | int16 | uint16
    | int32 | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: Data Types
  block_parameter: RawScoreDataTypeStr
  type: character vector
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Raw score data type Minimum
  summary: Minimum untransformed score for range checking [] (default) | scalar
  group: Data Types
  block_parameter: RawScoreOutMin
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
- name: Raw score data type Maximum
  summary: Maximum untransformed score for range checking [] (default) | scalar
  group: Data Types
  block_parameter: RawScoreOutMax
  type: character vector
  values: '"[]" | scalar'
  default: '"[]"'
```

### Main

### **Select trained machine learning model** — Classification tree model `treeMdl` (default) | `ClassificationTree` object | `CompactClassificationTree` object

Specify the name of a workspace variable that contains a `ClassificationTree` object or `CompactClassificationTree` object.

When you train the model by using `fitctree`, the following restrictions apply:

- The predictor data cannot include categorical predictors
  (`logical`, `categorical`, `char`,
  `string`, or `cell`). If you supply training data in a
  table, the predictors must be numeric (`double` or `single`).
  Also, you cannot use the `CategoricalPredictors` name-value argument. To
  include categorical predictors in a model, preprocess them by using `dummyvar` before fitting the model.
- The value of the `ScoreTransform`
  name-value argument cannot be `'invlogit'` or an anonymous
  function.
- You cannot use surrogate splits; that is, the value of the `Surrogate` name-value
  argument must be `'off'` (default).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TrainedLearner` |
| **Type:** workspace variable |
| **Values:** `ClassificationTree` object | `CompactClassificationTree` object |
| **Default:** `'treeMdl'` |

### **Add output port for predicted class scores** — Add second output port for predicted class scores `off` (default) | `on`

Select the check box to include the second output port **score**
in the ClassificationTree Predict block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutputScore` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

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

### **Label data type** — Data type of label output `Inherit: Inherit via back propagation` | `Inherit: auto` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `Enum: <class name>` | `<data type expression>`

Specify the data type for the **label** output. The type can be
inherited, specified as an enumerated data type, or
expressed as a data type object such as `Simulink.NumericType`.

The supported data types depend on the labels used in the model specified by
**Select trained machine
learning model**.

- If the model uses numeric or logical labels, the supported data types are
  `Inherit: Inherit via back propagation` (default),
  `double`, `single`,
  `half`, `int8`,
  `uint8`, `int16`,
  `uint16`, `int32`,
  `uint32`, `int64`,
  `uint64`, `boolean`, fixed point, and
  a data type object.
- If the model uses nonnumeric labels, the supported data types are
  `Inherit: auto` (default), `Enum: <class
  name>`, and a data type object.

When you select an inherited option, the software behaves as follows:

- `Inherit: Inherit via back propagation` (default for
  numeric and logical labels) — Simulink automatically determines the **Label data
  type** of the block during data type propagation (see Data Type Propagation (Simulink)). In this case, the block uses the
  data type of a downstream block or signal object.
- `Inherit: auto` (default for nonnumeric labels) — The
  block uses an autodefined enumerated data type variable. For example,
  suppose the workspace variable name specified by **Select
  trained machine learning model** is
  `myMdl`, and the class labels are
  `class 1` and `class 2`.
  Then, the corresponding **label** values are
  `myMdl_enumLabels.class_1` and
  `myMdl_enumLabels.class_2`. The block converts the
  class labels to valid MATLAB identifiers by using the `matlab.lang.makeValidName`
  function.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LabelDataTypeStr` |
| **Type**: character vector or string |
| **Values**: `"Inherit: Inherit via back propagation"` | `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"Enum: <class name>"` | `"<data type expression>"` |
| **Default**: `"Inherit: Inherit via back propagation"` (for numeric and logical labels) | `"Inherit: auto"` (for nonnumeric labels) |

### **Label data type Minimum** — Minimum value of label output for range checking `[]` (default) | scalar

Specify the lower value of the **label** output range that
Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Label data type Minimum** parameter does not saturate or clip
the actual **label** output signal. To do so, use the Saturation (Simulink) block instead.

#### Dependencies

You can specify this parameter only if the model specified by **Select trained
machine learning model** uses numeric labels.

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
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as SIL
  or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Label data type Maximum** parameter does not saturate or clip
the actual **label** output signal. To do so, use the Saturation (Simulink) block instead.

#### Dependencies

You can specify this parameter only if the model specified by **Select trained
machine learning model** uses numeric labels.

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

### **Raw score data type** — Untransformed score data type `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the internal untransformed scores. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

When you select `Inherit: auto`, the block uses a rule that inherits a data type.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Dependencies

You can specify this parameter only if the model specified by **Select trained
machine learning model** uses a score transformation other than
`"none"` (default, same as `"identity"`).

- If the model uses no score transformations (`"none"`
  or `"identity"`), then you can specify the score data
  type by using **Score data
  type**.
- If the model uses a score transformation other than
  `"none"` or `"identity"`, then you
  can specify the data type of untransformed raw scores by using this
  parameter. To specify the data type of transformed scores, use
  **Score data type**.

You can change the score transformation option by specifying the
`ScoreTransform` name-value argument during training, or by
modifying the `ScoreTransform` property after training.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `RawScoreDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Raw score data type Minimum** — Minimum untransformed score for range checking `[]` (default) | scalar

Specify the lower value of the untransformed score range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Raw score data type Minimum** parameter does not saturate or
clip the actual untransformed score signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `RawScoreOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Raw score data type Maximum** — Maximum untransformed score for range checking `[]` (default) | scalar

Specify the upper value of the untransformed score range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as SIL
  or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

The **Raw score data type Maximum** parameter does not saturate or
clip the actual untransformed score signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `RawScoreOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |
## Libraries

Statistics and Machine Learning Toolbox / Classification

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

**Introduced in R2021a**

## Description

Classify observations using decision tree classifier

The ClassificationTree Predict block classifies observations using a
classification tree object (`ClassificationTree` or `CompactClassificationTree`) for multiclass classification.

Import a trained classification object into the block by specifying the name of a
workspace variable that contains the object. The input port **x** receives an
observation (predictor data), and the output port **label** returns a
predicted class label for the observation. You can add the optional output port
**score**, which returns predicted class scores or posterior
probabilities.
