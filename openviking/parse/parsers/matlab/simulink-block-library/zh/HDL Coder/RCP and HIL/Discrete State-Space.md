---
type: simulink-block
title: 'Discrete State-Space'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'RCP and HIL'
documentation_page: 'discretestatespace'
documentation_source_path: '../simulink/slref/discretestatespace.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete State-Space

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量

输入向量，其宽度等于 **B** 和 **D** 矩阵的列数。有关详细信息，请参阅描述。

**提示**

对于整数和定点输入信号，请使用 Fixed-Point State-Space 模块。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 输出向量 标量 | 向量

输出向量，其宽度等于 **C** 和 **D** 矩阵的行数。有关详细信息，请参阅描述。

**数据类型：** `single` | `double`

## 参数

### 主要

### **A** — 矩阵系数 A `1`（默认）| 标量 | 向量 | 矩阵

指定矩阵系数 `A`，为实值 *n*×*n* 矩阵，其中 *n* 为状态数。有关矩阵系数的详细信息，请参阅描述。

#### 编程用法

|  |
| --- |
| **模块参数：** `A` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'1'` |

### **B** — 矩阵系数 B `1`（默认）| 标量 | 向量 | 矩阵

指定矩阵系数 `B`，为实值 *n*×*m* 矩阵，其中 *n* 为状态数，*m* 为输入数。有关矩阵系数的详细信息，请参阅描述。

#### 编程用法

|  |
| --- |
| **模块参数：** `B` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'1'` |

### **C** — 矩阵系数 C `1`（默认）| 标量 | 向量 | 矩阵

指定矩阵系数 **C**，为实值 *r*×*n* 矩阵，其中 *r* 为输出数，*n* 为状态数。有关矩阵系数的详细信息，请参阅描述。

#### 编程用法

|  |
| --- |
| **模块参数：** `C` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'1'` |

### **D** — 矩阵系数 D `1`（默认）| 标量 | 向量 | 矩阵

指定矩阵系数 **D**，为实值 *r*×*m* 矩阵，其中 *r* 为输出数，*m* 为输入数。有关矩阵系数的详细信息，请参阅描述。

#### 编程用法

|  |
| --- |
| **模块参数：** `D` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认值：** `'1'` |

### **Initial conditions** — 初始状态向量 0（默认）| 标量 | 向量

将初始状态向量指定为标量或向量。初始状态向量不能包含 `inf` 或 `NaN` 值。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialCondition` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认值：** `'0'` |

### **Sample time (–1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。请参阅指定采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认值：** `'-1'` |

### 状态属性

### **State name** — 模块状态的唯一名称 `''`（默认）| 字母数字字符串

使用此参数为模块状态分配唯一名称。默认值为 `' '`。当此字段为空时，不分配名称。使用此参数时，请记住以下注意事项：

- 有效标识符以字母或下划线字符开头，后跟字母数字或下划线字符。
- 状态名称仅适用于所选模块。

当您点击 **Apply** 时，此参数会启用 **State name must resolve to Simulink signal object**。

有关详细信息，请参阅 C Data Code Interface Configuration for Model Interface Elements (Simulink Coder)。

#### 编程用法

|  |
| --- |
| **模块参数：** `StateName` |
| **类型：** 字符向量 |
| **值：** 唯一名称 |
| **默认值：** `''` |

### **State name must resolve to Simulink signal object** — 要求状态名称解析为信号对象 `off`（默认）| `on`

选中此复选框以要求状态名称解析为 Simulink® 信号对象。

#### 依赖关系

要启用此参数，请为 **State name** 指定一个值。仅当您将模型配置参数 **Signal resolution** 设置为 `None` 以外的值时，此参数才会出现。

#### 编程用法

|  |
| --- |
| **模块参数：** `StateMustResolveToSignalObject` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

## 所属库

Simulink / Discrete Simulink / Quick Insert / Discrete HDL Coder / RCP and HIL

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

默认情况下，以下 HDL 模块属性可用。

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | 指定是否将设计中的模块映射为浮点运算符的 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 `inherit`。另请参阅 LatencyStrategy (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现离散状态空间系统

### 非空矩阵的模块行为

Discrete State-Space 模块实现由以下方程描述的系统

x(n+1)=Ax(n)+Bu(n)y(n)=Cx(n)+Du(n),

其中 *u* 为输入，*x* 为状态，*y* 为输出。矩阵系数必须具有以下特征，如下图所示：

- **A** 必须为 *n*×*n* 矩阵，其中 *n* 为状态数。
- **B** 必须为 *n*×*m* 矩阵，其中 *m* 为输入数。
- **C** 必须为 *r*×*n* 矩阵，其中 *r* 为输出数。
- **D** 必须为 *r*×*m* 矩阵。

该模块接受一个输入并生成一个输出。输入向量的宽度是 **B** 和 **D** 矩阵的列数。输出向量的宽度是 **C** 和 **D** 矩阵的行数。要定义初始状态向量，请使用 **Initial conditions** 参数。

要为 **A**、**B**、**C**、**D** 或 **Initial conditions** 指定零向量或零矩阵，请使用 `zeros` 函数。

### 空矩阵的模块行为

当矩阵 **A**、**B** 和 **C** 为空（例如 `[]`）时，模块的功能变为 `y(n) = Du(n)`。如果 **Initial conditions** 向量也为空，则模块使用零初始状态向量。
