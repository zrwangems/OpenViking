---
type: simulink-block
title: 'Matrix 1-Norm'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'matrix1norm'
documentation_source_path: 'ref/matrix1norm.html'
language: zh-CN
chinese_source: worker-translation
---

# Matrix 1-Norm

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Port_1
  summary: 输出信号 标量
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
```

### 输入

### **Port\_1** — 输入信号 向量 | 矩阵

输入信号，指定为向量或矩阵。

该模块将长度为 *M* 的无向向量输入视为 *M*×1 矩阵。

Matrix 1-Norm 模块支持实数和复数浮点输入以及实数定点输入。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 输出信号 标量

输入的矩阵 1-范数或最大列和，以标量形式返回。输出 *y* 始终为标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
## 参数
```yaml
parameters:
- name: 舍入模式
  summary: 舍入操作的方法 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
- name: 整数溢出时饱和
  summary: 溢出处理方法 off（默认）| on
  group: 数据类型
- name: 累加器
  summary: '累加器数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as input | fixdt([],16,0)'
  group: 数据类型
- name: 输出
  summary: '输出数据类型 Inherit: Same as accumulator（默认）| Inherit: Same as input | fixdt([],16,0)'
  group: 数据类型
- name: 输出最小值
  summary: 模块可以输出的最小值 []（默认）| 标量
  group: 数据类型
- name: 输出最大值
  summary: 模块可以输出的最大值 []（默认）| 标量
  group: 数据类型
- name: 锁定数据类型设置以防止定点工具更改
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型
```

### 主

**主选项卡**上没有参数。

### 数据类型

### **舍入模式** — 舍入操作的方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

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

当满足以下所有条件时，**舍入模式**和**整数溢出时饱和**参数对数值结果没有影响：

- **累加器**数据类型为 `Inherit: Inherit via internal rule`。
- **输出**数据类型为 `Inherit: Same as accumulator`。

使用这些数据类型设置时，该模块以全精度模式运行。

### **整数溢出时饱和** — 溢出处理方法 off（默认）| on

选中此参数以对定点运算的结果进行饱和处理。清除此参数以对定点运算的结果进行环绕处理。有关*饱和*和*环绕*的详细信息，请参阅定点运算的溢出处理。

**注意**

当满足以下所有条件时，**舍入模式**和**整数溢出时饱和**参数对数值结果没有影响：

- **乘积输出**数据类型为 `Inherit: Inherit via internal rule`。
- **累加器**数据类型为 `Inherit: Inherit via internal rule`。

使用这些数据类型设置时，该模块以全精度模式运行。

### **累加器** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as input` | `fixdt([],16,0)`

**累加器**指定 Matrix 1-Norm 模块中累加运算输出的数据类型。

- `Inherit: Inherit via internal rule` — 该模块基于内部规则继承累加器数据类型。有关此规则的更多信息，请参阅通过内部规则继承。
- `Inherit: Same as input` — 该模块将累加器数据类型指定为与输入数据类型相同。
- `fixdt([],16,0)` — 该模块指定一个自动有符号、二进制点、定标定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用**数据类型助手**设置**累加器**数据类型。要使用该助手，请单击**显示数据类型助手**按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

有关如何在此模块中使用累加器数据类型的说明，请参阅定点数据类型。

### **输出** — 输出数据类型 `Inherit: Same as accumulator`（默认）| `Inherit: Same as input` | `fixdt([],16,0)`

**输出**指定 Matrix 1-Norm 模块输出的数据类型。

- `Inherit: Same as input` — 该模块将输出数据类型指定为与输入数据类型相同。
- `Inherit: Same as accumulator` — 该模块将输出数据类型指定为与累加器数据类型相同。
- `fixdt([],16,0)` — 该模块指定一个自动有符号、二进制点、定标定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用**数据类型助手**设置**输出**数据类型。要使用该助手，请单击**显示数据类型助手**按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

有关输出数据类型的更多信息，请参阅定点数据类型。

### **输出最小值** — 模块可以输出的最小值 `[]`（默认）| 标量

指定模块可以输出的最小值。Simulink 使用此最小值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **输出最大值** — 模块可以输出的最大值 `[]`（默认）| 标量

指定模块可以输出的最大值。Simulink 使用此最大值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数以防止定点工具覆盖您在模块对话框中指定的数据类型。

**注意**

浮点继承优先于此选项卡上定义的数据类型设置。当输入为浮点时，该模块忽略这些设置，所有内部数据类型均为浮点。
## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

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

**在 R2006a 之前引入**

## 描述

计算矩阵的 1-范数

Matrix 1-Norm 模块计算 *M*×*N* 输入矩阵 *A* 的 1-范数或最大列和。

y=‖A‖1=max1≤j≤N∑i=1M|aij|

等效的 MATLAB® 代码为：

```
y = max(sum(abs(A)))
```
