---
type: simulink-block
title: 'Discrete Derivative'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'discretederivative'
documentation_source_path: 'slref/discretederivative.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Derivative

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 缩放后的离散时间导数 标量 | 向量 | 矩阵

可选的缩放离散时间导数，指定为标量、向量或矩阵。有关该模块如何计算离散时间导数的详细信息，请参阅描述。您可以通过 **Output data type** 参数指定输出信号的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主要

### **Gain value** — 缩放因子 `1.0` （默认） | 标量

应用于所计算导数的缩放因子，指定为实数标量值。

#### 编程使用

|  |
| --- |
| **模块参数**：`gainval` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'1.0'` |

### **Initial condition for previous weighted input K\*u/Ts** — 初始条件 `0.0` （默认） | 标量

前一个缩放输入的初始条件，指定为标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`ICPrevScaledInput` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'0.0'` |

### **Input processing** — 指定基于采样或基于帧的处理 `Elements as channels (sample based)` （默认） | `Columns as channels (frame based)`

指定模块执行基于采样还是基于帧的处理：

- `Columns as channels (frame based)` — 将输入的每一列视为独立通道（基于帧的处理）。

  **注意**

  基于帧的处理需要 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。
- `Elements as channels (sample based)` — 将输入的每个元素视为独立通道（基于采样的处理）。

使用 **Input processing** 指定模块执行基于采样还是基于帧的处理。有关这两种处理模式的详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 编程使用

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：character vector |
| **值**：`'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**：`'Elements as channels (sample based)'` |

### 信号属性

### **Output minimum** — 用于范围检查的最小输出值 `[]` （默认） | 标量

软件检查的输出范围的下限值。

软件使用最小值执行以下操作：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动缩放。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **值**：| `'[]'` （默认） | 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]` （默认） | 标量

软件检查的输出范围的上限值。

软件使用最大值执行以下操作：

- 某些模块的参数范围检查（请参阅 Specify Minimum and Maximum Values for Block Parameters）。
- 仿真范围检查（请参阅 Specify Signal Ranges 和 Enable Simulation Range Checking）。
- 定点数据类型的自动缩放。
- 从模型生成的代码的优化。此优化可能会移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **值**：| `'[]'` （默认） | 带引号的标量 |

### **Output data type** — 输出数据类型 `Inherit: Inherit via internal rule` （默认） | `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)`

指定输出数据类型。您可以将其设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via back propagation`
- 内置数据类型的名称，例如 `single`
- 数据类型对象的名称，例如 `Simulink.NumericType` 对象
- 计算结果为数据类型的表达式，例如 `fixdt(1,16,0)`

**Data Type Assistant** 可帮助您设置数据属性。要使用 **Data Type Assistant**，请单击 Show data type assistant 按钮。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule' | 'Inherit: Inherit via back propagation' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type 的选项 `off` （默认） | `on`

选中此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **值**：| `'off'` （默认） | `'on'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor` （默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入方式，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **值**：| `'Floor'` （默认） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate to max or min when overflows occur** — 溢出操作的方法 `off` （默认） | `on`

选中此复选框时，溢出饱和到数据类型可以表示的最大值或最小值。否则，溢出将回绕。

选中此复选框时，饱和应用于模块上的每个内部操作，而不仅仅是输出或结果。通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

|  |
| --- |
| **模块参数**：`DoSatur` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

## 所属库

Simulink / Discrete

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 在触发子系统层次结构内使用时依赖于绝对时间。
- 在某些条件下，生成的代码依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算离散时间导数

Discrete Derivative 模块按如下方式计算可选的缩放离散时间导数

y(tn)=K(u(tn)−u(tn−1)Ts)

其中

- u(tn) 和 y(tn) 分别是当前时间步的模块输入和输出。
- u(tn−1) 是前一个时间步的模块输入。
- K 是可选的缩放因子，使用 **Gain value** 参数指定。
- Ts 是仿真的离散步长，必须是固定的。

**注意**

请勿在具有非周期性触发的子系统（例如非周期性函数调用子系统）中使用此模块。此配置会产生不准确的结果。
