---
type: simulink-block
title: 'Step'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'step'
documentation_source_path: 'slref/step.html'
language: zh-CN
chinese_source: worker-translation
---

# Step

## 端口

### 输出

### **Port\_1** — 输出阶跃信号 标量 | 向量

由参数 **Step time**、**Initial value** 和 **Final value** 定义的输出阶跃函数信号。

**数据类型：** `double` | `single`

## 参数

### **Step time** — 阶跃发生的时间 `1`（默认）| 标量

指定输出从 **Initial value** 参数跳变到 **Final value** 参数的时间，以秒为单位。

#### 编程使用

|  |
| --- |
| **模块参数**：`Time` |
| **类型**：字符向量 |
| **值：** `'1'` | 实值或复值标量、向量或矩阵 |
| **默认值**：`'1'` |

### **Initial value** — 阶跃前的输出值 `0`（默认）| 标量

指定在仿真时间达到 **Step time** 参数之前的模块输出。

#### 编程使用

|  |
| --- |
| **模块参数**：`Before` |
| **类型**：字符向量 |
| **值：** `'1'` | 实值或复值标量、向量或矩阵 |
| **默认值**：`'0'` |

### **Final value** — 阶跃后的输出值 `1`（默认）| 标量

指定当仿真时间达到并超过 **Step time** 参数时的模块输出。

#### 编程使用

|  |
| --- |
| **模块参数**：`After` |
| **类型**：字符向量 |
| **值：** `'1'` | 实值或复值标量、向量或矩阵 |
| **默认值**：`'1'` |

### **Sample time** — 采样率 `0`（默认）| 标量

指定阶跃的采样率。有关详细信息，请参阅 Specify Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0'` |

### **Interpret vector parameters as 1-D** — 将向量视为一维 `on`（默认）| `off`

如果 **Constant value** 参数求值为 `N` 元素行向量或列向量，则选中此复选框以输出长度为 `N` 的向量。

- 选中此复选框时，如果 **Constant value** 参数求值为 `N` 元素行向量或列向量，则模块输出长度为 `N` 的向量。例如，模块输出维度为 `1-by-N` 或 `N-by-1` 的矩阵。
- 清除此复选框时，如果 **Constant value** 参数求值为 `N` 元素行向量或列向量，则模块不输出长度为 `N` 的向量。

#### 编程使用

|  |
| --- |
| **模块参数：** `VectorParams1D` |
| **类型：** 字符向量 |
| **值：** `'on' | 'off'` |
| **默认值：** `'on'` |

### **Enable zero-crossing detection** — 启用过零检测 `on`（默认）| `off`

选择以启用过零检测。有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程使用

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 | 字符串 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

### **Output data type** — 输出数据类型 `double`（默认）| `Inherit: Inherit via back propagation` | `single` | `<data type expression>`

输出数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

当您选择 `Inherit: Inherit via back propagation` 时，模块使用驱动模块的数据类型。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 编程使用

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** 字符向量 |
| **值：** `'Inherit: Inherit via internal rule'` | `'double'` | `'single'` | <data type expression> |
| **默认值：** `'double'` |

### **Mode** — 数据类型类别 `Inherit`（默认）| `Built in` | `Expression`

数据类型类别，指定为 `Inherit`、`Built in` 或 `Expression`。有关使用此参数的详细信息，请参阅 Specify Data Types Using Data Type Assistant。

#### 依赖关系

单击 **Show data type assistant** 按钮可启用此参数。

### **Data type override** — 为此信号指定数据类型覆盖模式 `Inherit` | `Off`

选择此信号的数据类型覆盖模式。

- 当您选择 `Inherit` 时，Simulink® 从其上下文中继承数据类型覆盖设置，即从正在使用该信号的模块、`Simulink.Signal` 对象或 Simulink 中的 Stateflow® 图继承。
- 当您选择 `Off` 时，Simulink 忽略其上下文的数据类型覆盖设置。

有关详细信息，请参阅 Simulink 文档中的 Specify Data Types Using Data Type Assistant。

#### 依赖关系

要启用此参数，请单击 **Show data type assistant** 按钮，并将 **Mode** 设置为 `Built in`。

#### 提示

为单个数据类型关闭数据类型覆盖的能力，可在您应用数据类型覆盖时对模型中的数据类型提供更强的控制。例如，您可以使用此选项确保数据类型满足下游模块的要求，而不受数据类型覆盖设置的影响。

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

生成阶跃函数

Step 模块在指定时间在两个可定义电平之间提供阶跃。如果仿真时间小于 **Step time** 参数值，则模块的输出为 **Initial value** 参数值。对于大于或等于 **Step time** 的仿真时间，输出为 **Final value** 参数值。

数值模块参数在标量扩展后必须具有相同的维度。如果 **Interpret vector parameters as 1-D** 选项关闭，则模块输出与参数具有相同维度和维数的信号。如果 **Interpret vector parameters as 1-D** 选项打开且数值参数为行向量或列向量（即单行或单列二维数组），则模块输出向量（一维数组）信号。否则，模块输出与参数具有相同维数和维度的信号。
