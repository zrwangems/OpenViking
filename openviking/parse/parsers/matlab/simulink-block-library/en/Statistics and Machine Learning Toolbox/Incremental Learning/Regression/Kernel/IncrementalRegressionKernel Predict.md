---
type: simulink-block
title: 'IncrementalRegressionKernel Predict'
family: 'stats'
product_id: 'stats'
product_name: 'Statistics and Machine Learning Toolbox'
documentation_release: R2025b
official_category: 'Incremental Learning / Regression / Kernel'
documentation_page: 'incrementalregressionkernelpredict'
documentation_source_path: 'incrementalregressionkernelpredict.html'
language: en
---

# IncrementalRegressionKernel Predict

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
- name: yfit
  summary: Chunk of predicted responses floating-point vector
  direction: output
  data_types: single | double
- name: CanPredict
  summary: Model status 0 (false) | 1 (true)
  direction: output
```

### Input

### **mdl** — Incremental learning model bus signal

Incremental learning model (`incrementalRegressionKernel`) fit to streaming data, specified as a bus
signal (see Composite Signals (Simulink)).

### **x** — Chunk of predictor data numeric matrix

Chunk of predictor data, specified as a numeric matrix.

**Note**

The block supports only numerical input predictor data. If your input data
includes categorical data, you must prepare an encoded version of the categorical
data. Use `dummyvar` to convert each categorical
variable to a numeric matrix of dummy variables. Then, concatenate all dummy
variable matrices and any other numeric predictors. For more details, see Dummy Variables.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **yfit** — Chunk of predicted responses floating-point vector

Chunk of predicted responses, returned as a floating-point vector

**Note**

If you specify an estimation period when you create **mdl**,
then the predicted responses are zero during the estimation period.

**Data Types:** `single` | `double`

### **CanPredict** — Model status `0` (`false`) | `1` (`true`)

Model status for prediction, returned as logical `0`
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
  summary: Initial incremental kernel regression model kernelMdl (default) | incrementalRegressionKernel model object
  group: Main
  block_parameter: InitialLearner
  type: character vector or string
  values: incrementalRegressionKernel object name
  default: '"kernelMdl"'
- name: Add output port for status of trained machine learning model
  summary: Add second output port for model status off (default) | on
  group: Main
  block_parameter: ShowOutputCanPredict
  type: character vector
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
  values: '"[]" | scalar'
  default: '"[]"'
- name: Output data type Maximum
  summary: Maximum value of yfit output for range checking [] (default) | scalar
  group: Data Types
  block_parameter: OutMax
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
  summary: 'Inner product data type double (default) | Inherit: Inherit via internal rule | single | half | int8 | uint8 |
    int16 | uint16 | int32 | uint32 | int64 | uint64 | boolean | fixdt(1,16,0) | fixdt(1,16,2^0,0) | <data type expression>'
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

### **Select initial machine learning model** — Initial incremental kernel regression model `kernelMdl` (default) | `incrementalRegressionKernel` model object

Specify the name of a workspace variable that contains the configured `incrementalRegressionKernel` model object.

When you create the initial model object, the following restrictions apply:

- The predictor data cannot include
  categorical predictors (`logical`,
  `categorical`, `char`,
  `string`, or `cell`). If you supply
  training data in a table, the predictors must be numeric
  (`double` or `single`). To include
  categorical predictors in a model, preprocess them by using `dummyvar` before fitting the
  model.
- The `NumPredictors` property of the initial model must be a positive
  integer scalar, and must be equal to the number of predictors in
  **x**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialLearner` |
| **Type:** character vector or string |
| **Values:** `incrementalRegressionKernel` object name |
| **Default:** `"kernelMdl"` |

### **Add output port for status of trained machine learning model** — Add second output port for model status `off` (default) | `on`

Select the check box to include the output port **CanPredict** in
the IncrementalRegressionKernel Predict block. This check box does not
appear if the workspace already contains an incremental kernel regression model named
`kernelMdl`, capable of prediction, when you create the
IncrementalRegressionKernel Predict block. Alternatively, you can
specify to include the output port **CanPredict** by selecting the
IncrementalRegressionKernel Predict block in the Simulink workspace and entering
`set_param(gcb,ShowOutputCanPredict="on")` at the MATLAB® command line.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ShowOutputCanPredict` |
| **Type:** character vector |
| **Values:** `"off" | "on"` |
| **Default:** `"off"` |

### **Sample time (–1 for inherited)** — Option to specify sample time `–1` (default) | scalar

Specify the discrete interval between sample time hits or specify another type of sample
time, such as continuous (`0`) or inherited (`–1`). For more
options, see Types of Sample Time (Simulink).

By default, the IncrementalRegressionKernel Predict block inherits sample time based on the context
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

Specify the lower value of the **yfit** output range that
Simulink checks.

Simulink uses the minimum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Output data type Minimum** parameter does not saturate
or clip the actual **yfit** output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMin` |
| **Type**: character vector |
| **Values**: `"[]"` | scalar |
| **Default**: `"[]"` |

### **Output data type Maximum** — Maximum value of yfit output for range checking `[]` (default) | scalar

Specify the upper value of the **yfit** output range that
Simulink checks.

Simulink uses the maximum value to perform:

- Parameter range checking for some blocks (see Specify Minimum and Maximum Values for Block Parameters (Simulink)).
- Simulation range checking (see Specify Signal Ranges (Simulink) and Enable Simulation Range Checking (Simulink)).
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as SIL or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

**Note**

The **Output data type Maximum** parameter does not saturate
or clip the actual **yfit** output. To do so, use the Saturation (Simulink) block instead.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMax` |
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

### **Inner product data type** — Inner product data type `double` (default) | `Inherit: Inherit via internal rule` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

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
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as software-in-the-loop (SIL) mode or external mode. For more information,
  see Optimize using the specified minimum and maximum values (Embedded Coder).

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
- Optimization of the code that you generate from the model. This optimization
  can remove algorithmic code and affect the results of some simulation modes,
  such as SIL or external mode. For more information, see Optimize using the specified minimum and maximum values (Embedded Coder).

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

Statistics and Machine Learning Toolbox / Incremental Learning / Regression / Kernel

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

**Introduced in R2024b**

## Description

Predict responses using incremental kernel regression model

The IncrementalRegressionKernel Predict block predicts responses for
streaming data using a trained kernel regression model returned as the output of an IncrementalRegressionKernel
Fit block.

Import an initial kernel regression model object into the
IncrementalRegressionKernel Predict block by specifying the name of a
workspace variable that contains the object. The input port **mdl** receives
a bus signal that represents an incremental learning model fit to streaming data. The input
port **x** receives a chunk of predictor data (observations), and the output
port **yfit** returns predicted responses for the chunk. The optional output
port **CanPredict** returns the prediction status of the trained
model.
