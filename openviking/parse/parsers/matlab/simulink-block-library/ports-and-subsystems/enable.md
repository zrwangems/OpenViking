---
type: simulink-block
title: 'Enable'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'enable'
---

# Enable

Add enable port to subsystem or model

## 中文

将使能端口添加到子系统或模型

### 所属库

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

### 描述

Enable 模块允许外部信号控制子系统或模型的执行。要启用此功能，可在 Subsystem 模块中添加该模块，或在 Model 模块所引用模型的根级别添加该模块。

如果在模型的根级别使用使能端口：

- 对于多速率模型，请将求解器设置为单任务。
- 对于具有定步长的模型，模型中有至少一个模块必须以指定的定步长速率运行。

### 端口

#### 输出

#### **Enable signal** — 子系统或模型的外部使能信号 标量

使能信号从外部连接到 Enabled Subsystem 模块的外部，并传递到子系统的内部。当您选择**显示输出端口**参数时，使能信号端口将添加到 Enable 模块。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `expression`

### 参数

#### **启用时的状态** — 选择当禁用的子系统或模型被激活时要采用的模块状态 **保持** (默认) | **重置**

对于处于禁用状态的 Subsystem 模块或 Model 模块，选择在激活这些模块时其所含模块的状态变化情况。

**保持**
:   按其先前值保持模块状态。

**重置**
:   将模块状态重置为其初始条件（如果未定义，则为零）。

##### 编程用法

|  |
| --- |
| **模块参数：**`StatesWhenEnabling` |
| **类型：**字符向量 |
| **值**：`'held'` | `'reset'` |
| **默认值：**`'held'` |

#### **传播可变大小信号的大小** — 选择何时传播可变大小信号 **仅在启用时** (默认) | **执行期间**

选择何时传播可变大小信号。

**仅在启用时**
:   当重新启用包含 Enable 端口模块的 Subsystem 模块或 Model 模块时，传播可变大小的信号。如果您选择此选项，采样时间必须为周期性采样时间。

**执行期间**
:   在每个时间步传播可变大小的信号。

##### 编程用法

|  |
| --- |
| **模块参数：**`PropagateVarSize` |
| **类型：**字符向量 |
| **值**：`'Only when enabling'` | `'During execution'` |
| **默认值：**`'Only when enabling'` |

#### **显示输出端口** — 控制使能信号的输出端口的显示 `off` (默认) | `on`

输出端口将 Enabled Subsystem 模块或激活的 Model 模块的外接使能信号传递到内部。

off
:   在 Enable 端口模块上删除输出端口。

on
:   在 Enable 端口模块上显示输出端口。选择此选项将允许子系统或模型处理使能信号。

##### 编程用法

|  |
| --- |
| **模块参数：**`ShowOutputPort` |
| **类型：**字符向量 |
| **值：**`'off'` | `'on'` |
| **默认值：**`'off'` |

#### **启用过零检测** — 控制过零检测 `on` (默认) | `off`

控制模型的过零检测。

on
:   检测过零点。

off
:   不检测过零点。

##### 编程用法

|  |
| --- |
| **模块参数：**`ZeroCross` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

#### **端口维度** — 指定使能信号的维度 `1` (默认) | `[n]` | `[m n]`

指定从外部连接到 Model 模块并传递到模块内部的使能信号的维度。

`1`
:   标量信号。

`[n]`
:   宽度为 `n` 的向量信号。

`[m n]`
:   具有 `m` 行和 `n` 列的矩阵信号。

##### 编程用法

|  |
| --- |
| **模块参数：**`PortDimensions` |
| **类型：**字符向量 |
| **值**：`'1'` | `'[n]'` | `'[m n]'` |
| **默认值：**`'1'` |

#### **采样时间** — 指定时间间隔 `-1` (默认) | `Ts` | `[Ts, To]`

指定模块方法执行之间的时间间隔。请参阅指定采样时间。

`-1`
:   从模型继承采样时间。

`Ts`
:   标量，其中 Ts 是时间间隔。

`[Ts, To]`
:   向量，其中 Ts 是时间间隔，To 是初始时间偏移量。

##### 编程用法

|  |
| --- |
| **模块参数：**`SampleTime` |
| **类型：**字符向量 |
| **值**：`'-1'` | `'Ts'` | `'[Ts, To]'` |
| **默认值：**`'-1'` |

#### **最小** — 指定使能信号的最小输出值 `[]` (默认) | 实数标量

指定从外部连接到 Model 模块并传递到模块内部的使能信号的最小值。

Simulink® 使用此值来执行：

- 仿真范围检查。请参阅指定信号范围。
- 定点数据类型的自动定标。
- 所生成代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

`[]`
:   不指定最小值。

实数标量
:   实数双精度标量值。

##### 编程用法

|  |
| --- |
| **模块参数：**`OutMin` |
| **类型：**字符向量 |
| **值：**`'[]'` | 用引号引起来的实数标量 |
| **默认值：**`'[]'` |

#### **最大** — 指定使能信号的最大输出值 `[]` (默认) | 实数标量

指定从外部连接到 Model 模块并传递到模块内部的使能信号的最大值。

Simulink 使用此值来执行：

- 仿真范围检查。请参阅指定信号范围。
- 定点数据类型的自动定标。
- 所生成代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

`[]`
:   不指定最大值。

实数标量
:   实数双精度标量值。

##### 编程用法

|  |
| --- |
| **模块参数：**`OutMax` |
| **类型：**字符向量 |
| **值：**`'[]'` | 用引号引起来的实数标量 |
| **默认值：**`'[]'` |

#### **数据类型** — 指定使能信号的输出数据类型 **double** (默认) | **single** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **boolean** | **fixdt(1,16)** | **fixdt(1,16,0)** | **fixdt(1,16,2^,0)** | **<数据类型表达式>**

指定从外部连接到 Model 模块并传递到模块内部的使能信号的数据类型。

**double**
:   双精度浮点。

**single**
:   单精度浮点。

**int8**
:   有符号 8 位整数。

**uint8**
:   无符号 8 位整数。

**int16**
:   有符号 16 位整数。

**uint16**
:   无符号 16 位整数。

**int32**
:   有符号 32 位整数。

**uint32**
:   无符号 32 位整数。

**int64**
:   有符号 64 位整数。

**uint64**
:   无符号 64 位整数。

**boolean**
:   值为 `true` 或 `false` 的布尔值。

**fixdt(1,16)**
:   未定义二进制小数点位置的有符号 16 位定点数。

**fixdt(1,16,0)**
:   二进制小数点位置设置为零的有符号 16 位定点数。

**fixdt(1,16,2^,0)**
:   斜率设置为 `2^0` 且偏置设置为 `0` 的有符号 16 位定点数。

**<数据类型表达式>**
:   数据类型对象，例如 `Simulink.NumericType`。您不能以数据类型表达式的形式输入 `Simulink.Bus` 对象的名称。

##### 编程用法

|  |
| --- |
| **模块参数：**`OutDataTypeStr` |
| **类型：**字符向量 |
| **值**：`'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'<fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值：**`'double'` |

#### **模式** — 选择数据类型类别 **内置** (默认) | **定点** | **表达式**

选择数据类型类别并显示下拉列表以帮助您定义数据类型。

**内置**
:   显示数据类型和“数据类型覆盖”的下拉列表。

**定点**
:   显示“符号性”、“定标”和“数据类型覆盖”的下拉列表。

**表达式**
:   显示用于输入表达式的框。

##### 依赖关系

要启用此参数，请选择“显示数据类型助手”按钮。

##### 编程用法

没有等效的命令行参数。

#### **数据插值** — 指定缺失的工作区数据的值 `on` (默认) | `off`

指定从工作区加载数据时缺失的工作区数据的值。

on
:   在不存在对应工作区数据的时间步上对输出进行线性插值。

off
:   不在时间步处进行输出插值。取存在数据的最近时间步上的输出作为当前输出。

##### 编程用法

|  |
| --- |
| **模块参数：**`Interpolate` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `是` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

有关详细信息，请参阅 Enabled Subsystem 中的 HDL 代码生成。

**HDL 架构**

此模块具有一个默认 HDL 架构。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## Description

The Enable block allows an external signal to control execution of a
subsystem or a model. To enable this functionality, add the block to a
Subsystem block or at the root level of a model that is referenced by a
Model block.

If you use an enable port at the root-level of a model:

- For multi-rate models, set the solver to single-tasking.
- For models with a fixed-step size, at least one block in the model must run at
  the specified fixed-step size rate.

## Ports

### Output

### **Enable signal** — External enable signal for a subsystem or model scalar

Enable signal attached externally to the outside of an Enabled
Subsystem block and passed to the inside of the subsystem.
An enable signal port is added to an Enable block when
you select the **Show output port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `expression`

## Parameters

### **States when enabling** — Select block states when subsystem or model is disabled `held` (default) | `reset`

When a Subsystem block or Model block is
disabled, select what happens to block states for the blocks within the
subsystem or model.

`held`
:   Hold block states at their previous values.

`reset`
:   Reset block states to their initial conditions (zero if not
    defined).

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `StatesWhenEnabling` |
| **Type:** character vector |
| **Values:** `'held'` | `'reset'` |
| **Default:** `'held'` |

### **Propagate sizes of variable-size signals** — Select when to propagate a variable-size signal `Only when enabling` (default) | `During execution`

Select when to propagate a variable-size signal.

`Only when enabling`
:   Propagate a variable-size signal when reenabling a
    Subsystem block or Model block
    containing an Enable port block. When you select
    this option, sample time must be periodic.

`During execution`
:   Propagate variable-size signals at each time step.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PropagateVarSize` |
| **Type:** character vector |
| **Values:** `'Only when enabling'` | `'During execution'` |
| **Default:** `'Only when enabling'` |

### **Show output port** — Control display of output port for enable signal `off` (default) | `on`

The output port passes the enable signal attached externally to the
outside of an Enabled Subsystem block or enabled
Model block to the inside.

off
:   Remove the output port on the Enable port
    block.

on
:   Display an output port on the Enable port
    block. Selecting this option allows the subsystem or model to
    process the enable signal.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ShowOutputPort` |
| **Type:** character vector |
| **Values:** `'off'` | `'on'` |
| **Default:** `'off'` |

### **Enable zero-crossing detection** — Control zero-crossing detection `on` (default) | `off`

Control zero-crossing detection for a model.

on
:   Detect zero crossings.

off
:   Do not detect zero crossings.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `ZeroCross` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

### **Port dimensions** — Specify dimensions for the enable signal `1` (default) | `[n]` | `[m n]`

Specify dimensions for the enable signal attached externally to a
Model block and passed to the inside of the block.

`1`
:   Scalar signal.

`[n]`
:   Vector signal of width `n`.

`[m n]`
:   Matrix signal having `m` rows and
    `n` columns.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `PortDimensions` |
| **Type:** character vector |
| **Values:** `'1'` | `'[n]'` | `'[m n]'` |
| **Default:** `'1'` |

### **Sample time** — Specify time interval `-1` (default) | `Ts` | `[Ts, To]`

Specify time interval between block method execution. See Specify Sample Time.

`-1`
:   Sample time inherited from the model.

`Ts`
:   Scalar where Ts is the time interval.

`[Ts, To]`
:   Vector where Ts is the time interval and To is the initial
    time offset.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** `'-1'` | `'Ts'` | `'[Ts, To]'` |
| **Default:** `'-1'` |

### **Minimum** — Specify minimum output value for the enable signal `[]` (default) | real scalar

Specify minimum value for the enable signal attached externally to a
Model block and passed to the inside of the block.

Simulink® uses this value to perform:

- Simulation range checking. See Specify Signal Ranges.
- Automatic scaling of fixed-point data types.
- Optimization of generated code. This optimization can remove
  algorithmic code and affect the results of some simulation modes
  such as SIL or external mode. See Optimize using the specified minimum and maximum values (Embedded Coder).

`[]`
:   Unspecified minimum value.

real scalar
:   Real double scalar value.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutMin` |
| **Type:** character vector |
| **Values:** `'[]'` | real scalar in quotes |
| **Default:** `'[]'` |

### **Maximum** — Specify maximum output value for the enable signal `[]` (default) | real scalar

Specify maximum value for the enable signal attached externally to a
Model block and passed to the inside of the block.

Simulink uses this value to perform:

- Simulation range checking. See Specify Signal Ranges.
- Automatic scaling of fixed-point data types.
- Optimization of generated code. This optimization can remove
  algorithmic code and affect the results of some simulation modes
  such as SIL or external mode. See Optimize using the specified minimum and maximum values (Embedded Coder).

`[]`
:   Unspecified maximum value.

real scalar
:   Real double scalar value.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutMax` |
| **Type:** character vector |
| **Values:** `'[]'` | real scalar in quotes |
| **Default:** `'[]'` |

### **Data type** — Specify output data type for the enable signal `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `fixdt(1,16,2^,0)` | `<data type expression>`

Specify data type for the enable signal attached externally to a
Model block and passed to the inside of the block.

`double`
:   Double-precision floating point.

`single`
:   Single-precision floating point.

`int8`
:   Signed 8-bit integer.

`uint8`
:   Unsigned 8-bit integer.

`int16`
:   Signed 16-bit integer.

`uint16`
:   Unsigned 16-bit integer.

`int32`
:   Signed 32-bit integer.

`uint32`
:   Unsigned 32-bit integer.

`int64`
:   Signed 64-bit integer.

`uint64`
:   Unsigned 64-bit integer.

`boolean`
:   Boolean with a value of `true` or
    `false`.

`fixdt(1,16)`
:   Signed 16-bit fixed point number with binary point
    undefined.

`fixdt(1,16,0)`
:   Signed 16-bit fixed point number with binary point set to
    zero.

`fixdt(1,16,2^,0)`
:   Signed 16-bit fixed point number with slope set to
    `2^0` and bias set to
    `0`.

`<data type expression>`
:   Data type object, for example
    `Simulink.NumericType`. You cannot enter
    the name of a `Simulink.Bus`
    object as a data type expression.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'double'` | `'single'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'boolean'` | `'<fixdt(1,16)'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default:** `'double'` |

### **Mode** — Select data type category `Built in` (default) | `Fixed point` | `Expression`

Select data type category and display drop-down lists to help you define
the data type.

`Built in`
:   Display drop-down lists for data type and Data type
    override.

`Fixed point`
:   Display drop-down lists for Signedness, Scaling, and Data type
    override.

`Expression`
:   Display box for entering an expression.

#### Dependency

To enable this parameter, select the Show data type assistant
button.

#### Programmatic Use

No equivalent command-line parameter.

### **Interpolate data** — Specify value of missing workspace data `on` (default) | `off`

Specify value of missing workspace data when loading data from the
workspace.

on
:   Linearly Interpolate output at time steps for which no
    corresponding workspace data exists.

off
:   Do not interpolate output at time steps. The current output
    equals the output at the most recent time step for which data
    exists.

#### Programmatic Use

|  |
| --- |
| **Block parameter:** `Interpolate` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

For more information, see HDL Code Generation in Enabled Subsystem.

**HDL Architecture**

This block has one default HDL architecture.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
