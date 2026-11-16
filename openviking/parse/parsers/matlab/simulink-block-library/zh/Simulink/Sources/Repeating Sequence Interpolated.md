---
type: simulink-block
title: 'Repeating Sequence Interpolated'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'repeatingsequenceinterpolated'
documentation_source_path: 'slref/repeatingsequenceinterpolated.html'
language: zh-CN
chinese_source: official
---

# Repeating Sequence Interpolated

## 端口

### 输出

### **Port\_1** — 周期性输出信号 标量

根据**时间值的向量**和**输出值的向量**参数中的值生成的输出信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 常设

### **输出值的向量** — 输出值的向量 `[3 1 4 2 1].'` (默认) | 向量

输出值的向量，用于指定输出波形。每个元素对应于**时间值的向量**参数中的时间值。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutValues` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`'[3 1 4 2 1].''` |

### **时间值的向量** — 时间值的向量 `[0 0.1 0.5 0.6 1].'` (默认) | 向量

指定包含时间值的列向量。时间值必须严格递增，并且向量的大小必须与输出值向量的大小相同。

#### 编程用法

|  |
| --- |
| **模块参数**：`TimeValues` |
| **类型**：字符向量 |
| **值**：向量 |
| **默认值**：`'[0 0.1 0.5 0.6 1].''` |

### **查找方法** — 输出的查找方法 **插值 - 使用最终值** (默认) | **取最邻近的输入值** | **向下取输入值** | **向上取输入值**

指定查找方法以确定数据点之间的输出。

#### 编程用法

|  |
| --- |
| **模块参数**：`LookUpMeth` |
| **类型**：字符向量 |
| **值**：`'Interpolation-Use End Values'` | `'Use Input Nearest'` | `'Use Input Below'` | `'Use Input Above'` |
| **默认值**：`'Interpolation-Use End Values'` |

### **采样时间** — 采样时间间隔 `0.01` (默认) | 标量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 指定采样时间。

#### 编程用法

|  |
| --- |
| **模块参数**：`tsamp` |
| **类型**：字符向量 |
| **值**：标量 |
| **默认值**：`'0.01'` |

### 信号属性

### **输出最小值** — 范围检查的最小输出值 `[]` (默认) | 标量

软件检查的输出范围的下限值。

软件使用最小值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

#### 提示

**输出最小值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMin` |
| **值:** | `'[]'` (默认) | scalar in quotes |

### **输出最大值** — 范围检查的最大输出值 `[]` (默认) | 标量

软件检查的输出范围的上限值。

软件使用最大值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

#### 提示

**输出最大值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMax` |
| **值:** | `'[]'` (默认) | scalar in quotes |

### **输出数据类型** — 指定输出数据类型 **double** (默认) | **继承: 通过反向传播继承** | **single** | **int8** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>** | ...

为输出选择数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType`。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | **fixdt(1,16,2^0,0)** | `fixdt(1,16,2^0,0)`. `'<data type expression>'` |
| **默认值**：`'double'` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选中此选项将锁定此模块的输出数据类型设置，从而防止通过定点工具和定点顾问进行更改。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

|  |
| --- |
| **模块参数**：`LockScale` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

## 所属库

Simulink / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不能在触发子系统层次结构中使用。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

输出离散时间序列并重复，从而在数据点之间插值

Repeating Sequence Interpolated 模块根据**时间值的向量**和**输出值的向量**参数中的值输出周期性离散序列。在数据点之间，该模块使用您为**查找方法**参数指定的方法来确定输出。
