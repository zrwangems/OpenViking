---
type: simulink-block
title: 'ClassificationECOC Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification'
documentation_page: 'classificationecocpredict'
documentation_source_path: 'classificationecocpredict.html'
language: en
---

# ClassificationECOC Predict

## Ports

### Input

### **x** — Predictor data row vector | column vector

Predictor data, specified as a row or column vector of one observation.

The variables in **x** must have the same order as the
predictor variables that trained the model specified by **Select
trained machine learning model**.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **label** — Predicted class label scalar

Predicted class label, returned as a scalar. **label** is the
class yielding the highest score. For more details, see the `label`
argument of the `predict` object function.

The block supports two decoding schemes that specify how the block aggregates the
binary losses to compute the classification scores, and how the block determines the
predicted class for each observation. For details, see **Decoding
scheme** and Binary Loss and Decoding Scheme.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — Predicted class scores or posterior probabilities row vector

Predicted class scores (negated average binary losses) or posterior probabilities,
returned as a row vector of size 1-by-*K*, where *K*
is the number of classes in the ECOC model.

To check the order of the classes, use the `ClassNames`
property of the model specified by **Select trained machine
learning model**.

#### Dependencies

- To enable this port, select the check box for **Add output port for predicted
  class scores** on the **Main** tab of the Block
  Parameters dialog box.
- The block supports two decoding schemes that specify how the block
  aggregates the binary losses to compute the classification scores, and how the
  block determines the predicted class for each observation. For details, see
  **Decoding
  scheme** and Binary Loss and Decoding Scheme.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **pbscore** — Positive-class scores of binary learners row vector

Positive-class scores of binary learners, returned as a row vector of size
1-by-*B*, where *B* is the number of binary
learners in the ECOC model.

To check the class assignment codes for the binary learners, use the
`CodingMatrix` property of the model specified by **Select trained machine
learning model**. For more details, see Coding Design
of a `ClassificationECOC` object.

#### Dependencies

To enable this port, select the check box for **Add output port for
positive-class scores of binary learners** on the
**Main** tab of the Block Parameters dialog box.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### Main

### **Select trained machine learning model** — ECOC classification model `ecocMdl` (default) | `ClassificationECOC` object | `CompactClassificationECOC` object

Specify the name of a workspace variable that contains a `ClassificationECOC` or `CompactClassificationECOC` model object.

When you train the model by using `fitcecoc`, the following restrictions apply:

- You must train an ECOC model using either SVM learners or linear learners.

  - For SVM learners, you can specify the `Learners`
    name-value argument as `"svm"`, an SVM template object
    created by using `templateSVM`, or a cell array of
    SVM template objects.
  - For linear learners, you can specify the `Learners`
    name-value argument as `"linear"`, a linear template
    object created by using `templateLinear`, or a cell array
    of linear template objects. The `Lambda` value
    (regularization term strength) of the template object must be a numeric
    scalar.
- The predictor data cannot include categorical predictors
  (`logical`, `categorical`, `char`,
  `string`, or `cell`). If you supply training data in a
  table, the predictors must be numeric (`double` or `single`).
  Also, you cannot use the `CategoricalPredictors` name-value argument. To
  include categorical predictors in a model, preprocess them by using `dummyvar` before fitting the model.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TrainedLearner` |
| **Type:** workspace variable |
| **Values:** `ClassificationECOC` object | `CompactClassificationECOC` object |
| **Default:** `'ecocMdl'` |

### **Add output port for predicted class scores (negated average binary losses)** — Add second output port `off` (default) | `on`

Select the check box to include the second output port **score**
in the ClassificationECOC Predict block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutputScore` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Add output port for positive-class scores of binary learners** — Add third output port `off` (default) | `on`

Select the check box to include the third output port **pbscore**
in the ClassificationECOC Predict block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutputPBScore` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

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
| **Values:** `'binodeviance'` | `'exponential'` | `'hamming'` | `'hinge'` | `'linear'` | `'logit'` | `'quadratic'` |
| **Default:** `'hinge'` |

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
| **Values:** `'lossweighted'` | `'lossbased'` |
| **Default:** `'lossweighted'` |

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
  numeric and logical labels) — Simulink® automatically determines the **Label data
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

### **Kernel data type** — Binary learner kernel computation data type `double` (default) | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `int64` | `uint64` | `uint32` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type of a parameter for kernel computation of binary learners.
The type can be specified directly or expressed as a data type object such as
`Simulink.NumericType`.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Dependencies

You can specify this parameter only if the model specified by **Select trained machine
learning model** uses SVM learners. If the model uses linear learners,
then specify **Inner product data
type** instead.

The **Kernel data type** parameter specifies the data type of a
different parameter depending on the type of kernel function of the specified SVM
learners. You specify the kernel function type by using the `KernelFunction`
name-value argument of the `templateSVM` function. You must pass
the output of `templateSVM` as the value for the `Learners` name-value
argument of the `fitcecoc` function.

| `KernelFunction` Value | Data Type |
| --- | --- |
| `'gaussian'` or `'rbf'` | The parameter specifies the data type of the squared distance D2=‖x−s‖2 for the Gaussian kernel G(x,s)=exp(−D2), where *x* is the predictor data for an observation and *s* is a support vector. |
| `'linear'` | The parameter specifies the data type for the output of the linear kernel function G(x,s)=xs', where *x* is the predictor data for an observation and *s* is a support vector. |
| `'polynomial'` | The parameter specifies the data type for the output of the polynomial kernel function G(x,s)=(1+xs')p, where *x* is the predictor data for an observation, *s* is a support vector, and *p* is a polynomial kernel function order. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `KernelDataTypeStr` |
| **Type**: character vector |
| **Values**: `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'uint64'` | `'int64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'double'` |

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
or clip the actual kernel computation value signal.

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
or clip the actual kernel computation value signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `KernelOutMax` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Inner product data type** — Inner product data type for binary learners `Inherit: Inherit via internal rule` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the inner product term of the classification score of
binary learners. The type can be inherited, specified directly, or expressed as a data
type object such as `Simulink.NumericType`.

When you select `Inherit: Inherit via internal rule`, the
block uses an internal rule to determine the output data type. The internal rule
chooses a data type that optimizes numerical accuracy, performance, and generated code
size, while considering the properties of the embedded target hardware. The software
cannot always optimize efficiency and numerical accuracy at the same
time.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Dependencies

You can specify this parameter only if the model specified by **Select trained machine
learning model** uses linear learners. If the model uses SVM learners,
then specify **Kernel data
type** instead.

For linear classification learners, the classification score for classifying the
observation *x* into the positive class is defined by

*f*(*x*) =
*x**β*+*b*.

*β* is the estimated column vector of coefficients, and
*b* is the estimated scalar bias. Each linear classification
learner in the ECOC model object contains the coefficients and bias in the
`Beta` and `Bias` properties,
respectively.

If the model consists of logistic regression learners, then the software applies
the `'logit'` score transformation to the classification scores of
binary learners. The classification score for classifying *x* into
the negative class is –*f*(*x*). The software
classifies observations into the class that yields a positive score for each binary
learner.

Use **Inner product data type** to determine the data type of
*x**β*, and use **Positive-class score
data type** to determine the data type of the classification scores of
binary learners.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InnerProductDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

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
saturate or clip the actual inner product value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InnerProductOutMin` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

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
saturate or clip the actual inner product value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InnerProductOutMax` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

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

**Introduced in R2023a**

## Description

Classify observations using error-correcting output codes (ECOC) classification model

The ClassificationECOC Predict block classifies observations using an
error-correcting output codes (ECOC) classification model (`ClassificationECOC` or `CompactClassificationECOC`) for multiclass
classification.

Import a trained classification object into the block by specifying the name of a
workspace variable that contains the object. The input port **x** receives an
observation (predictor data), and the output port **label** returns predicted
class labels for the observation. You can add optional output ports **score**
and **pbscore**, where **score** returns predicted class
scores (negated average binary losses), and **pbscore** returns
positive-class scores for binary learners.
