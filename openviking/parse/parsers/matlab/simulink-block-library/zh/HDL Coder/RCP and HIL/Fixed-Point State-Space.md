---
type: simulink-block
title: 'Fixed-Point State-Space'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'RCP and HIL'
documentation_page: 'fixedpointstatespace'
documentation_source_path: '../simulink/slref/fixedpointstatespace.html'
language: zh-CN
chinese_source: worker-translation
---

# Fixed-Point State-Space

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入向量，其宽度等于 **B** 和 **D** 矩阵的列数。有关详细信息，请参阅描述。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

输出信号，其宽度等于 **C** 和 **D** 矩阵的行数。有关详细信息，请参阅描述。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: 状态矩阵 A
  summary: 状态矩阵 [2.6020 -2.2793 0.6708; 1 0 0; 0 1 0]（默认）| 标量 | 向量 | 矩阵
  group: 主要
  block_parameter: A
  type: 字符向量
  values: 标量 | 向量 | 矩阵
- name: 输入矩阵 B
  summary: 输入列向量 [ 1; 0; 0]（默认）| 标量 | 向量 | 矩阵
  group: 主要
  block_parameter: B
  type: 字符向量
  values: 标量 | 向量 | 矩阵
- name: 输出矩阵 C
  summary: 输出列向量 [0.0184 0.0024 0.0055]（默认）| 标量 | 向量 | 矩阵
  group: 主要
  block_parameter: C
  type: 字符向量
  values: 标量 | 向量 | 矩阵
- name: 直接馈通矩阵 D
  summary: 直接馈通矩阵 [0.0033]（默认）| 标量 | 向量 | 矩阵
  group: 主要
  block_parameter: D
  type: 字符向量
  values: 标量 | 向量 | 矩阵
- name: 状态初始条件
  summary: 初始状态向量 0.0（默认）| 标量 | 向量 | 矩阵
  group: 主要
  block_parameter: InitialCondition
  type: 字符向量
  values: 标量 | 向量 | 矩阵
- name: 内部计算数据类型
  summary: 内部计算的数据类型 fixdt('double')（默认）| 数据类型字符串
  group: 信号属性
  block_parameter: InternalDataType
  type: 字符向量
  values: 数据类型字符串
- name: 状态方程 AX+BU 的定标
  summary: 状态方程的定标 2^0（默认）| 标量
  group: 信号属性
  block_parameter: StateEqScaling
  type: 字符向量
  values: 标量
- name: 输出方程 CX+DU 的定标
  summary: 输出方程的定标 2^0（默认）| 标量
  group: 信号属性
  block_parameter: OutputEqScaling
  type: 字符向量
  values: 标量
- name: 锁定输出数据类型设置以防止被定点工具更改
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 信号属性
  block_parameter: LockScale
  type: 字符向量
  values: '''off'' | ''on'''
- name: 整数舍入模式
  summary: 定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 信号属性
  block_parameter: RndMeth
  type: 字符向量
  values: '''Ceiling'' | ''Convergent'' | ''Floor'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: 发生溢出时饱和至最大值或最小值
  summary: 溢出操作的方法 off（默认）| on
  group: 信号属性
  block_parameter: DoSatur
  type: 字符向量
  values: '''off'' | ''on'''
```

### 主要

### **状态矩阵 A** — 状态矩阵 `[2.6020 -2.2793 0.6708; 1 0 0; 0 1 0]`（默认）| 标量 | 向量 | 矩阵

将状态矩阵指定为 *n*×*n* 的实数或复数值矩阵，其中 *n* 是状态数。有关矩阵系数的详细信息，请参阅描述。

#### 程序化使用

|  |
| --- |
| **模块参数：** `A` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认：** `'[2.6020 -2.2793 0.6708; 1 0 0; 0 1 0]'` |

### **输入矩阵 B** — 输入列向量 `[ 1; 0; 0]`（默认）| 标量 | 向量 | 矩阵

将输入列向量指定为 *n*×*m* 的实数或复数值矩阵，其中 *n* 是状态数，*m* 是输入数。有关矩阵系数的详细信息，请参阅描述。

#### 程序化使用

|  |
| --- |
| **模块参数：** `B` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认：** `'[ 1; 0; 0]'` |

### **输出矩阵 C** — 输出列向量 `[0.0184 0.0024 0.0055]`（默认）| 标量 | 向量 | 矩阵

将输出列向量指定为 *r*×*n* 的实数或复数值矩阵，其中 *r* 是输出数，*n* 是状态数。有关矩阵系数的详细信息，请参阅描述。

#### 程序化使用

|  |
| --- |
| **模块参数：** `C` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认：** `'[0.0184 0.0024 0.0055]'` |

### **直接馈通矩阵 D** — 直接馈通矩阵 `[0.0033]`（默认）| 标量 | 向量 | 矩阵

将直接馈通矩阵指定为 *r*×*m* 的实数或复数值矩阵，其中 *r* 是输出数，*m* 是输入数。有关矩阵系数的详细信息，请参阅描述。

#### 程序化使用

|  |
| --- |
| **模块参数：** `D` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认：** `'[0.0033]'` |

### **状态初始条件** — 初始状态向量 `0.0`（默认）| 标量 | 向量 | 矩阵

指定状态的初始条件。

#### 限制

初始状态不能为 `inf` 或 `NaN`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialCondition` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 | 矩阵 |
| **默认：** `'0.0'` |

或者，使用 `X0`。

### 信号属性

### **内部计算数据类型** — 内部计算的数据类型 `fixdt('double')`（默认）| 数据类型字符串

指定模块用于内部计算的数据类型。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InternalDataType` |
| **类型：** 字符向量 |
| **值：** 数据类型字符串 |
| **默认：** `'fixdt('double')'` |

### **状态方程 AX+BU 的定标** — 状态方程的定标 `2^0`（默认）| 标量

指定状态方程 **AX+BU** 的定标。

#### 程序化使用

|  |
| --- |
| **模块参数：** `StateEqScaling` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'2^0'` |

### **输出方程 CX+DU 的定标** — 输出方程的定标 `2^0`（默认）| 标量

指定输出方程 **CX+DU** 的定标。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputEqScaling` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'2^0'` |

### **锁定输出数据类型设置以防止被定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此选项可锁定此模块的输出数据类型设置，防止被 Fixed-Point Tool 和 Fixed-Point Advisor 更改。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 程序化使用

|  |
| --- |
| **模块参数**： `LockScale` |
| **类型**： 字符向量 |
| **值**： `'off'` | `'on'` |
| **默认**： `'off'` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认：** `'Floor'` |

### **发生溢出时饱和至最大值或最小值** — 溢出操作的方法 `off`（默认）| `on`

选中此复选框时，溢出饱和至数据类型可表示的最大值或最小值。否则，溢出将回绕。

选中此复选框时，饱和适用于模块上的每次内部运算，而不仅仅是输出或结果。通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DoSatur` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认：** `'off'` |
## 所属库

Simulink / Additional Math & Discrete / Additional Discrete

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 不建议将此模块用于布尔信号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

默认情况下，以下 HDL 模块属性可用。

| 常规 | |
| --- | --- |
| **SharingFactor** | 使用 SharingFactor 指定要映射到单个共享资源的等效功能资源数。默认值为 0。请参阅 Resource Sharing (HDL Coder)。 |

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

实现离散时间状态空间

Fixed-Point State-Space 模块实现由以下方程描述的系统

y(n)=Cx(n)+Du(n)

x(n+1)=Ax(n)+Bu(n)

其中 *u* 是输入，*x* 是状态，*y* 是输出。两个方程具有相同的数据类型。

- **A** 必须是 *n*×*n* 矩阵，其中 *n* 是状态数。
- **B** 必须是 *n*×*m* 矩阵，其中 *m* 是输入数。
- **C** 必须是 *r*×*n* 矩阵，其中 *r* 是输出数。
- **D** 必须是 *r*×*m* 矩阵。

此外：

- 状态 x 必须是 *n*×1 向量。
- 输入 u 必须是 *m*×1 向量。
- 输出 y 必须是 *r*×1 向量。

该模块接受一个输入并生成一个输出。输入向量的宽度是 **B** 和 **D** 矩阵的列数。输出向量的宽度是 **C** 和 **D** 矩阵的行数。要定义初始状态向量，请使用 **Initial conditions** 参数。
