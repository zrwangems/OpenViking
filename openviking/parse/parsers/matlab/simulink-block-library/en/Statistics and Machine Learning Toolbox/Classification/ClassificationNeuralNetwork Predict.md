---
type: simulink-block
title: 'ClassificationNeuralNetwork Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Classification'
documentation_page: 'classificationneuralnetworkpredict'
documentation_source_path: 'classificationneuralnetworkpredict.html'
language: en
---

# ClassificationNeuralNetwork Predict

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

Predicted class label, returned as a scalar. The predicted class is the class that
minimizes the expected classification cost. For more details, see the More About section of the
`predict`
function reference page.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **score** — Predicted class scores or posterior probabilities row vector

Predicted class scores or posterior probabilities, returned as a row vector of
size 1-by-*k*, where *k* is the number of classes in
the neural network model. The classification score `Score(i)`
represents the posterior probability that the observation in **x**
belongs to class `i`.

To check the order of the classes, use the `ClassNames`
property of the neural network model specified by **Select trained machine
learning model**.

#### Dependencies

To enable this port, select the check box for **Add output port for predicted
class scores** on the **Main** tab of the Block
Parameters dialog box.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Select trained machine learning model** — Neural network classification model `nnetMdl` (default) | `ClassificationNeuralNetwork` object | `CompactClassificationNeuralNetwork` object

Specify the name of a workspace variable that contains a `ClassificationNeuralNetwork` object or `CompactClassificationNeuralNetwork` object.

When you train the model by using `fitcnet`,
the following restrictions apply:

- The predictor data cannot include categorical predictors
  (`logical`, `categorical`, `char`,
  `string`, or `cell`). If you supply training data in a
  table, the predictors must be numeric (`double` or `single`).
  Also, you cannot use the `CategoricalPredictors` name-value argument. To
  include categorical predictors in a model, preprocess them by using `dummyvar` before fitting the model.
- The value of the `ScoreTransform` name-value argument cannot be
  `'invlogit'` or an anonymous function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TrainedLearner` |
| **Type:** workspace variable |
| **Values:** `ClassificationNeuralNetwork` object | `CompactClassificationNeuralNetwork` object |
| **Default:** `'nnetMdl'` |

### **Add output port for predicted class scores** — Add second output port for predicted class scores `off` (default) | `on`

Select the check box to include the second output port **score**
in the ClassificationNeuralNetwork Predict block.

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

### **Output layer data type** — Data type of final fully connected layer `Inherit: Inherit via internal rule` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the output layer. The type can be inherited, specified
directly, or expressed as a data type object such as
`Simulink.NumericType`.

When you select `Inherit: Inherit via internal rule`, the
block uses an internal rule to determine the output data type. The internal rule chooses
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
| **Block Parameter**: `OutputLayerDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Output layer data type Minimum** — Minimum value for final fully connected layer `[]` (default) | scalar

Specify the lower value of the output layer's internal variable range checked by
Simulink.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Output layer data type Minimum** parameter does not
saturate or clip the output layer value signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputLayerOutMin` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Output layer data type Maximum** — Maximum value for final fully connected layer `[]` (default) | scalar

Specify the upper value of the output layer's internal variable range checked by
Simulink.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as SIL
  or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Output layer data type Maximum** parameter does not
saturate or clip the output layer value signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutputLayerOutMax` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Layer 1 data type** — Data type of first fully connected layer `Inherit: Inherit via internal rule` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the first layer. The type can be inherited, specified
directly, or expressed as a data type object such as
`Simulink.NumericType`.

When you select `Inherit: Inherit via internal rule`, the
block uses an internal rule to determine the data type. The internal rule chooses a data
type that optimizes numerical accuracy, performance, and generated code size, while
taking into account the properties of the embedded target hardware. The software cannot
always optimize efficiency and numerical accuracy at the same
time.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Tips

A trained neural network can have more than one fully connected layer, excluding
the output layer.

- You can specify the data type for each individual layer for the first 10
  layers. Specify the data type **Layer n data type** for
  each layer. The data type of the first layer is **Layer 1 data
  type**, the data type of the second layer is **Layer 2
  data type**, and so on.
- You can specify the data type for layers 11 to *k*, where
  *k* is the total number of layers, by using the data
  type **Additional layer(s) data type**. The **Block Parameter** for **Additional layer(s)
  data type** is `Layer11DataTypeStr`.
- The data types **Layer n data type** and
  **Additional layer(s) data type** can be inherited,
  specified directly, or expressed as a data type object such as
  `Simulink.NumericType`. These data types support the
  same values as **Layer 1 data type**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Layer1DataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Layer 1 data type Minimum** — Minimum value for first fully connected layer `[]` (default) | scalar

Specify the lower value of the first layer's internal variable range checked by
Simulink.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Layer 1 data type Minimum** parameter does not saturate
or clip the first layer value signal.

#### Tips

A trained neural network can have more than one fully connected layer, excluding
the output layer.

- You can specify the lower value of each individual layer's internal
  variable range checked by Simulink for the first 10 layers. Specify the lower value
  **Layer n minimum** for each layer. The minimum value
  of the first layer is **Layer 1 minimum**, the minimum
  value of the second layer is **Layer 2 minimum**, and so
  on.
- You can specify the lower value for layers 11 to *k*,
  where *k* is the total number of layers, by using
  **Additional layer(s) minimum**. The **Block Parameter** for **Additional layer(s)
  minimum** is `Layer11OutMin`.
- **Layer n minimum** and **Additional layer(s)
  minimum** support the same values as **Layer 1
  minimum**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Layer1OutMin` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Layer 1 data type Maximum** — Maximum value for first fully connected layer `[]` (default) | scalar

Specify the upper value of the first layer's internal variable range checked by
Simulink.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as SIL
  or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Layer 1 data type Maximum** parameter does not saturate
or clip the first layer value signal.

#### Tips

A trained neural network can have more than one fully connected layer, excluding
the output layer.

- You can specify the upper value of each individual layer's internal
  variable range checked by Simulink for the first 10 layers. Specify the upper value
  **Layer n maximum** for each layer. The maximum value
  of the first layer is **Layer 1 maximum**, the maximum
  value of the second layer is **Layer 2 maximum**, and so
  on.
- You can specify the upper value for layers 11 to *k*,
  where *k* is the total number of layers, by using
  **Additional layer(s) maximum**. The **Block Parameter** for **Additional layer(s)
  maximum** is `Layer11OutMax`.
- **Layer n maximum** and **Additional layer(s)
  maximum** support the same values as **Layer 1
  maximum**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Layer1OutMax` |
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

**Introduced in R2021b**

## Description

Classify observations using neural network classification model

The ClassificationNeuralNetwork Predict block classifies observations using
a neural network classification object (`ClassificationNeuralNetwork` or `CompactClassificationNeuralNetwork`) for multiclass classification.

Import a trained classification object into the block by specifying the name of a
workspace variable that contains the object. The input port **x** receives an
observation (predictor data), and the output port **label** returns a
predicted class label for the observation. You can add the optional output port
**score**, which returns predicted class scores or posterior
probabilities.
