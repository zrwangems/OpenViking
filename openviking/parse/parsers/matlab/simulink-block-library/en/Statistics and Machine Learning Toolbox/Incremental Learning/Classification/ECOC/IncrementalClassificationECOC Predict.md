---
type: simulink-block
title: 'IncrementalClassificationECOC Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Incremental Learning / Classification / ECOC'
documentation_page: 'incrementalclassificationecocpredict'
documentation_source_path: 'incrementalclassificationecocpredict.html'
language: en
---

# IncrementalClassificationECOC Predict

## Ports

### Input

### **mdl** — Incremental learning model bus signal

Incremental learning model (`incrementalClassificationECOC`) fit to streaming data, specified as a bus
signal (see `Composite Signals` (Simulink)).

### **x** — Chunk of predictor data numeric matrix

Chunk of predictor data, specified as a numeric matrix. The orientation of the
variables and observations is specified by **Predictor data observation
dimension**. The default orientation is `rows`, which
indicates that observations in the predictor data are oriented along the rows of
**x**.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **label** — Chunk of predicted class labels column vector

Chunk of predicted class labels, returned as a column vector. The label
`label(i)` represents the class yielding the highest score for
the observation **x**(`i`). For more details, see
the `Label`
argument of the `predict`
object function.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — Predicted class scores or posterior probabilities matrix

Predicted class scores (negated average binary losses) or posterior probabilities,
returned as a matrix. To check the order of the classes, use the
`ClassNames` property of the model specified by **Select initial machine
learning model**.

#### Dependencies

- To enable this port, select the check box for **Add output port for
  predicted class scores** on the **Main** tab of
  the Block Parameters dialog box.
- The block supports two decoding schemes that specify how the block
  aggregates the binary losses to compute the classification scores, and how the
  block determines the predicted class for each observation. For details, see
  **Decoding
  scheme** and Binary Loss and Decoding Scheme.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **pbscore** — Positive-class scores of binary learners matrix

Positive-class scores of binary learners, returned as a matrix. To check the class
assignment codes for the binary learners, use the `CodingMatrix`
property of the model specified by **Select trained machine
learning model**. For more details, see Coding Design
of a `ClassificationECOC` object.

#### Dependencies

To enable this port, select the check box for **Add output port for
positive-class scores of binary learners** on the
**Main** tab of the Block Parameters dialog box.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Select initial machine learning model** — Initial incremental classification ECOC model `ecocMdl` (default) | `incrementalClassificationECOC` model object

Specify the name of a workspace variable that contains the configured
`incrementalClassificationECOC` model object. The `NumPredictors` property of the initial model must be a positive integer
scalar, and must be equal to the number of predictors in
**x**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialLearner` |
| **Type:** workspace variable |
| **Values:** `incrementalClassificationECOC` model object |
| **Default:** `"ecocMdl"` |

### **Add output port for predicted class scores** — Add second output port `off` (default) | `on`

Select the check box to include the output port **score** in the
incrementalClassificationECOC Predict block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutputScore` |
| **Type:** character vector |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

### **Add output port for positive-class scores of binary learners** — Add third output port `off` (default) | `on`

Select the check box to include the third output port **pbscore**
in the incrementalClassificationECOC Predict block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutputPBScore` |
| **Type:** character vector |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

### **Binary learner loss function** — Binary learner loss function `hinge` (default) | `binodeviance` | `exponential` | `hamming` | `linear` | `logit` | `quadratic`

Specify the binary learner loss function as
`binodeviance`, `exponential`,
`hamming`, `hinge`,
`linear`, `logit`, or
`quadratic`.

The recommended binary loss function depends on the score ranges returned by the
binary learners. The following table lists some common cases:

| Description | Recommended Function |
| --- | --- |
| All binary learners are linear classification models of logistic regression learners. | `quadratic` |
| All binary learners are SVMs or linear classification models of SVM learners. | `hinge` |
| You specify to predict class posterior probabilities by setting `FitPosterior=true` when you train the ECOC model. | `quadratic` |

For definitions of the loss functions, see Binary Loss and Decoding Scheme.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `BinaryLoss` |
| **Type:** character vector |
| **Values:** `"binodeviance"` | `"exponential"` | `"hamming"` | `"hinge"` | `"linear"` | `"logit"` | `"quadratic"` |
| **Default:** `"hinge"` |

### **Decoding scheme** — Decoding scheme `lossweighted` (default) | `lossbased`

Specify the decoding scheme that aggregates the binary losses as
`lossweighted` or
`lossbased`.

The definition of the **score**
values depends on the **Decoding scheme** value.

- If you specify `lossweighted`, then the
  *k*th element in **score** is the sum of the
  binary losses divided by the number of binary learners for the
  *k*th class.
- If you specify `lossbased`, then the
  *k*th element in **score** is the sum of the
  binary losses divided by the total number of binary learners.

For more details, see Binary Loss and Decoding Scheme.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Decoding` |
| **Type:** character vector |
| **Values:** `"lossweighted"` | `"lossbased"` |
| **Default:** `"lossweighted"` |

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

By default, the IncrementalClassificationECOC Predict block inherits sample time based on the context
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
  numeric and logical labels) — Simulink® automatically determines the **Label data type**
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
| **Default**: `"Inherit: Inherit via back propagation"` |

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
or clip the actual **label** output signal. To do so, use the
Saturation (Simulink) block instead.

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
or clip the actual **label** output signal. To do so, use the
Saturation (Simulink) block instead.

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

### **Positive-class score data type** — Positive-class score data type `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the **pbscore** output. This data type also determines the data type for the classification scores of binary learners. The type can be inherited, specified directly, or expressed as a data type object such as `Simulink.NumericType`.

When you select `Inherit: auto`, the block uses a rule that inherits a data type.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PBScoreDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Positive-class score data type Minimum** — Minimum value of `pbscore` output for range checking `[]` (default) | scalar

Specify the lower value of the **pbscore** output range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Positive-class score data type Minimum** parameter does not saturate or clip the actual **pbscore** signal. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PBScoreOutMin` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Positive-class score data type Maximum** — Maximum value of `pbscore` output for range checking `[]` (default) | scalar

Specify the upper value of the **pbscore** output range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as SIL
  or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Positive-class score data type Maximum** parameter does not saturate or clip the actual **pbscore** signal. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `PBScoreOutMax` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Binary learner score data type** — Binary learner score data type `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the binary learner scores that are internal to the
`IncrementalClassificationECOC Predict` block. The type can be inherited, specified directly,
or expressed as a data type object such as
`Simulink.NumericType`.

When you select `Inherit: auto`, the block uses a rule
that inherits a data
type.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryScoreDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Binary learner score data type Minimum** — Minimum value of binary learner score for range checking `[]` (default) | scalar

Specify the lower value of the binary learner score output range that Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryScoreOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Binary learner score data type Maximum** — Maximum value of binary learner score for range checking `[]` (default) | scalar

Specify the upper value of the binary learner score output range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as SIL
  or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryScoreOutMax` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Binary learner kernel data type** — Binary learner kernel computation data type `double` (default) | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type of a parameter for kernel computation of binary learners.
The type can be specified directly or expressed as a data type object such as
`Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Dependencies

You can specify this parameter only if the model specified by **Select trained machine
learning model** uses SVM learners. If the model uses linear
learners, then specify **Inner product data
type** instead.

The IncrementalClassificationECOC Predict block supports only linear kernels. The
**Binary learner kernel data type** parameter specifies the data
type for the output of the linear kernel function G(x,s)=xs', where *x* is the predictor data for an
observation and *s* is a support vector. You specify the kernel
function type by using the `KernelFunction`
name-value argument of the `templateSVM` function. You must pass
the output of `templateSVM` as the value for the `Learners` name-value
argument of the `fitcecoc`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryKernelDataTypeStr` |
| **Type**: character vector |
| **Values**: `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"uint64"` | `"int64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"double"` |

### **Binary learner kernel data type Minimum** — Minimum kernel computation value for range checking `[]` (default) | scalar

Specify the lower value of the kernel computation internal variable range that
Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Binary learner kernel data type Minimum** parameter
does not saturate or clip the actual kernel computation value signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryKernelOutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Binary learner kernel data type Maximum** — Maximum kernel computation value for range checking `[]` (default) | scalar

Specify the upper value of the kernel computation internal variable range that
Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as SIL
  or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Binary learner kernel data type Maximum** parameter
does not saturate or clip the actual kernel computation value signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinaryKernelOutMax` |
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

## Description

Classify observations using incremental ECOC classification model

The IncrementalClassificationECOC Predict block classifies observations
using a trained error-correcting output codes (ECOC) classification model returned as the
output of an IncrementalClassificationECOC
Fit block.

Import an initial ECOC classification model object into the block by specifying the name
of a workspace variable that contains the object. The input port **mdl**
receives a bus signal that represents an incremental learning model fit to streaming data. The
input port **x** receives a chunk of predictor data (observations), and the
output port **label** returns predicted class labels for the chunk. You can
add optional output ports **score** and **pbscore**, where
**score** returns predicted class scores (negated average binary losses),
and **pbscore** returns positive-class scores for binary learners.
