---
type: simulink-block
title: 'Correlation'
family: 'simulink-extras'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Additional Sinks'
documentation_page: 'correlation'
documentation_source_path: 'ref/correlation.html'
language: zh-CN
chinese_source: worker-translation
---

# Correlation

## 端口
```yaml
ports:
- name: Port_1
  summary: 第一个数据输入信号 向量 | 矩阵 | *N* 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_2
  summary: 第二个数据输入信号 向量 | 矩阵 | *N* 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 互相关输出 向量 | 矩阵 | *N* 维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 第一个数据输入信号 向量 | 矩阵 | *N* 维数组

该模块接受实值或复值多通道和多维输入。当将 **Computation domain** 设置为 `Time` 时，输入可以是定点信号。当一个或两个输入信号为复数时，输出信号也为复数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是

### **Port\_2** — 第二个数据输入信号 向量 | 矩阵 | *N* 维数组

该模块接受实值或复值多通道和多维输入。当将 **Computation domain** 设置为 `Time` 时，输入可以是定点信号。当一个或两个输入信号为复数时，输出信号也为复数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 互相关输出 向量 | 矩阵 | *N* 维数组

两个输入信号的互相关输出。

当输入为 *N* 维数组时，该对象输出一个 *N* 维数组，其中除第一维之外的所有维度都与输入数组匹配。例如，

- 当输入 *u* 和 *v* 的维度分别为 *Mu*×*N*×*P* 和 *Mv*×*N*×*P* 时，Correlation 模块输出一个 (*Mu* + *Mv* – 1)×*N*×*P* 数组。
- 当输入 *u* 和 *v* 的维度分别为 *Mu*×*N* 和 *Mv*×*N* 时，该模块输出一个 (*Mu* + *Mv* – 1)×*N* 矩阵。

如果一个输入是列向量，另一个输入是 *N* 维数组，则 Correlation 模块计算该向量与 *N* 维数组中每一列的互相关。例如，

- 当输入 *u* 是 *Mu*×1 列向量，*v* 是 *Mv*×*N* 矩阵时，该模块输出一个 (*Mu* + *Mv* – 1)×*N* 矩阵。
- 类似地，当 *u* 和 *v* 是长度分别为 *Mu* 和 *Mv* 的列向量时，该模块执行向量互相关。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Computation domain
  summary: 模块计算互相关的域 Time（默认）| Frequency | Fastest
  group: 主选项卡
- name: Rounding mode
  summary: 舍入操作的方法 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型选项卡
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型选项卡
- name: Product output
  summary: '乘积输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | fixdt([],16,0)'
  group: 数据类型选项卡
- name: Accumulator
  summary: '累加器数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | Inherit: Same as product output | fixdt([],16,0)'
  group: 数据类型选项卡
- name: Output
  summary: '输出数据类型 Inherit: Same as accumulator（默认）| Inherit: Same as input | Inherit: Same as product output | fixdt([],16,0)'
  group: 数据类型选项卡
- name: Output Minimum
  summary: 模块可以输出的最小值 []（默认）| 标量
  group: 数据类型选项卡
- name: Output Maximum
  summary: 模块可以输出的最大值 []（默认）| 标量
  group: 数据类型选项卡
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型选项卡
```

### 主选项卡

### **Computation domain** — 模块计算互相关的域 `Time`（默认）| `Frequency` | `Fastest`

- `Time` — 在时域中计算互相关，可最大限度地减少内存使用。
- `Frequency` — 在频域中计算互相关。有关详细信息，请参阅算法。
- `Fastest` — 在可使计算次数最少的域中计算互相关。

要对定点信号进行互相关，请将此参数设置为 `Time`。

### 数据类型选项卡

**注意**

定点信号仅支持时域。要使用这些参数，请在 **Main** 选项卡上将 **Computation domain** 设置为 `Time`。

### **Rounding mode** — 舍入操作的方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

**注意**

当满足以下所有条件时，**Rounding mode** 和 **Saturate on integer overflow** 参数对数值结果没有影响：

- **Product output** 数据类型为 `Inherit: Inherit via internal rule`。
- **Accumulator** 数据类型为 `Inherit: Inherit via internal rule`。
- **Output** 数据类型为 `Inherit: Same as accumulator`。

使用这些数据类型设置时，该模块以全精度模式运行。

### **Saturate on integer overflow** — 溢出操作的方法 off（默认）| on

选中此参数时，该模块对其定点运算的结果进行饱和处理。清除此参数时，该模块对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

**注意**

当满足以下所有条件时，**Rounding mode** 和 **Saturate on integer overflow** 参数对数值结果没有影响：

- **Product output** 数据类型为 `Inherit: Inherit via internal rule`。
- **Accumulator** 数据类型为 `Inherit: Inherit via internal rule`。

使用这些数据类型设置时，该模块以全精度模式运行。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt([],16,0)`

**Product output** 指定 Correlation 模块中乘积运算输出的数据类型。有关乘积输出数据类型的更多信息，请参阅乘法数据类型和定点数据类型。

- `Inherit: Inherit via internal rule` — 该模块根据内部规则继承乘积输出数据类型。有关此规则的更多信息，请参阅通过内部规则继承。
- `Inherit: Same as input` — 该模块将乘积输出数据类型指定为与输入数据类型相同。
- `fixdt([],16,0)` — 该模块指定一个自动有符号、二进制点、定标的定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Product output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Accumulator** 指定 Correlation 模块中累加运算输出的数据类型。有关如何在此模块中使用累加器数据类型的说明，请参阅定点数据类型。

- `Inherit: Inherit via internal rule` — 该模块根据内部规则继承累加器数据类型。有关此规则的更多信息，请参阅通过内部规则继承。
- `Inherit: Same as input` — 该模块将累加器数据类型指定为与输入数据类型相同。
- `Inherit: Same as product output` — 该模块将累加器数据类型指定为与乘积输出数据类型相同。
- `fixdt([],16,0)` — 该模块指定一个自动有符号、二进制点、定标的定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Accumulator** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Output** — 输出数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `Inherit: Same as product output` | `fixdt([],16,0)`

**Output** 指定 Correlation 模块输出的数据类型。有关输出数据类型的更多信息，请参阅定点数据类型。

- `Inherit: Same as input` — 该模块将输出数据类型指定为与输入数据类型相同。
- `Inherit: Same as product output` — 该模块将输出数据类型指定为与乘积输出数据类型相同。
- `Inherit: Same as accumulator` — 该模块将输出数据类型指定为与累加器数据类型相同。
- `fixdt([],16,0)` — 该模块指定一个自动有符号、二进制点、定标的定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Output Minimum** — 模块可以输出的最小值 `[]`（默认）| 标量

指定该模块可以输出的最小值。Simulink® 软件使用此最小值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **Output Maximum** — 模块可以输出的最大值 `[]`（默认）| 标量

指定该模块可以输出的最大值。Simulink 软件使用此最大值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 off（默认）| on

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。
## 所属库

DSP System Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

两个输入的互相关

Correlation 模块沿第一维计算两个 *N* 维输入数组的互相关。计算可以在时域或频域中完成。您可以通过 **Computation domain** 参数指定域。在时域中，该模块将第一个输入信号 *u* 与第二个输入信号 *v* 的时间反转复共轭进行卷积。在频域中，为计算互相关，该模块：

1. 对两个输入信号 *U* 和 *V* 进行傅里叶变换。
2. 将 *U* 和 *V*\* 相乘，其中 \* 表示复共轭。
3. 计算乘积的逆傅里叶变换。

如果将 **Computation domain** 设置为 `Fastest`，该模块将选择可使计算次数最少的域。有关这些计算方法的信息，请参阅算法。
