---
type: simulink-block
title: 'RegressionLinear Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Regression'
documentation_page: 'regressionlinearpredict'
documentation_source_path: 'regressionlinearpredict.html'
language: en
---

# RegressionLinear Predict

## Ports
```yaml
ports:
- name: x
  summary: Predictor data row vector | column vector
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: yfit
  summary: Predicted response scalar
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

### **yfit** — Predicted response scalar

Predicted
response, returned as a scalar. For more details, see the `YHat` argument of the `predict` object function.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## Parameters
```yaml
parameters:
- name: Select trained machine learning model
  summary: Linear regression model linearMdl (default) | RegressionLinear object
  group: Main
  block_parameter: TrainedLearner
  type: workspace variable
  values: RegressionLinear object
  default: '''linearMdl'''
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
- name: Output data type
  summary: 'Data type of yfit output Inherit: auto (default) | double | single | half | int8 | uint8 | int16 | uint16 | int32
    | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: Data Types
  block_parameter: OutDataTypeStr
  type: character vector
  values: '"Inherit: auto" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32" | "uint32" | "int64"
    | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"Inherit: auto"'
- name: Output data type Minimum
  summary: Minimum value of yfit output for range checking [] (default) | scalar
  group: Data Types
  block_parameter: OutMin
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
- name: Output data type Maximum
  summary: Maximum value of yfit output for range checking [] (default) | scalar
  group: Data Types
  block_parameter: OutMax
  type: character vector
  values: '''[]'' | scalar'
  default: '''[]'''
- name: Inner product data type
  summary: 'Inner product data type double (default) | Inherit: Inherit via internal rule | single | half | int8 | uint8 |
    int16 | uint16 | int32 | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
  group: Data Types
  block_parameter: InnerProductDataTypeStr
  type: character vector
  values: '"Inherit: Inherit via internal rule" | "double" | "single" | "half" | "int8" | "uint8" | "int16" | "uint16" | "int32"
    | "uint32" | "int64" | "uint64" | "boolean" | "fixdt(1,16,0)" | "fixdt(1,16,2^0,0)" | "<data type expression>"'
  default: '"double"'
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

### Main

### **Select trained machine learning model** — Linear regression model `linearMdl` (default) | `RegressionLinear` object

Specify the name of a workspace variable that contains a `RegressionLinear` object.

When you train the model by using `fitrlinear`, the following restrictions apply:

- The predictor data cannot include categorical predictors
  (`logical`, `categorical`, `char`,
  `string`, or `cell`). If you supply training data in a
  table, the predictors must be numeric (`double` or `single`).
  Also, you cannot use the `CategoricalPredictors` name-value argument. To
  include categorical predictors in a model, preprocess them by using `dummyvar` before fitting the model.
- The `Lambda` property
  (regularization term strength) of the trained model must be a numeric scalar. If
  `Lambda` is a numeric vector, you must select the model
  corresponding to one regularization strength by using `selectModels`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TrainedLearner` |
| **Type:** workspace variable |
| **Values:** `RegressionLinear` object |
| **Default:** `'linearMdl'` |

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

### **Output data type** — Data type of yfit output `Inherit: auto` (default) | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the **yfit** output. The type can be inherited,
specified directly, or expressed as a data type object such as
`Simulink.NumericType`.

When you select `Inherit: auto`, the block uses a rule that inherits a data type.

For more information about data types, see Control Data Types of Signals (Simulink).

Click the **Show data type assistant**
button  to display the **Data Type Assistant**,
which helps you set the data type attributes. For more information, see Specify Data Types Using Data Type Assistant (Simulink).

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `"Inherit: auto"` | `"double"` | `"single"` | `"half"` | `"int8"` | `"uint8"` | `"int16"` | `"uint16"` | `"int32"` | `"uint32"` | `"int64"` | `"uint64"` | `"boolean"` | `"fixdt(1,16,0)"` | `"fixdt(1,16,2^0,0)"` | `"<data type expression>"` |
| **Default**: `"Inherit: auto"` |

### **Output data type Minimum** — Minimum value of yfit output for range checking `[]` (default) | scalar

Specify the lower value of the **yfit** output range that Simulink® checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as
  software-in-the-loop (SIL) mode or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Output data type Minimum** parameter does not saturate
or clip the actual **yfit** signal. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMin` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Output data type Maximum** — Maximum value of yfit output for range checking `[]` (default) | scalar

Specify the upper value of the **yfit** output range that Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization can
  remove algorithmic code and affect the results of some simulation modes, such as SIL
  or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Output data type Maximum** parameter does not saturate
or clip the actual **yfit** signal. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMax` |
| **Type**: character vector |
| **Values**: `'[]'` | scalar |
| **Default**: `'[]'` |

### **Inner product data type** — Inner product data type `double` (default) | `Inherit: Inherit via internal rule` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type for the inner product term of the predicted
response. The type can be inherited, specified directly, or expressed as a
data type object such as `Simulink.NumericType`.

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
| **Default**: `"double"` |

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

Statistics and Machine Learning Toolbox / Regression

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
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

Predict responses using linear regression model

The RegressionLinear Predict block predicts responses using a linear
regression object (`RegressionLinear`).

Import a trained regression object into the block by specifying the name of a workspace
variable that contains the object. The input port **x** receives an
observation (predictor data), and the output port **yfit** returns predicted
responses for the observation.
