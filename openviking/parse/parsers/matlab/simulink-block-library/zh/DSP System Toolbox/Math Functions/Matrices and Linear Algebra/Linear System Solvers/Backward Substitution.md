---
type: simulink-block
title: 'Backward Substitution'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'backwardsubstitution'
documentation_source_path: 'ref/backwardsubstitution.html'
language: zh-CN
chinese_source: worker-translation
---

# Backward Substitution

## 端口
```yaml
ports:
- name: U
  summary: 输入上三角矩阵 *M*×*M* 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: B
  summary: '*B* 矩阵 *M*×*N* 矩阵 | *M*×1 向量'
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: X
  summary: 方程组的解 *M*×*N* 矩阵 | *M*×1 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
```

### 输入

### **U** — 输入上三角矩阵 *M*×*M* 矩阵

通过此端口指定输入上三角 *M*×*M* 矩阵 *U*。输入 *U* 和 *B* 必须具有相同的行数。

如果输入为定点，则它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是

### **B** — *B* 矩阵 *M*×*N* 矩阵 | *M*×1 向量

将 *U**X* = *B* 方程中的 *B* 矩阵指定为 *M*×*N* 矩阵或 *M*×1 向量。

当您指定 *M*×1 向量时，模块将端口 **B** 处长度为 *M* 的向量输入视为 *M*×1 矩阵。输入 *U* 和 *B* 必须具有相同的行数。

如果输入为定点，则它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是
### 输出

### **X** — 方程组的解 *M*×*N* 矩阵 | *M*×1 矩阵

模块将输出返回为 *M*×*N* 矩阵或 *M*×1 向量。*X* 矩阵的大小与 *B* 矩阵的大小相同。

当输入为定点时，输出矩阵 *X* 仅为有符号定点。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Input U is unit-upper triangular
  summary: 输入矩阵的对角元素值为 1 off（默认）| on
  group: 主选项卡
- name: Diagonal of complex input U is real
  summary: 复数输入的对角元素为实数 off（默认）| on
  group: 主选项卡
- name: Rounding mode
  summary: 舍入运算的方法 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型选项卡
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型选项卡
- name: Product output
  summary: '乘积输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as first input | fixdt(1,16,0)'
  group: 数据类型选项卡
- name: Accumulator
  summary: '累加器数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as product output | Inherit: Same as first input
    | fixdt(1,16,0)'
  group: 数据类型选项卡
- name: Output
  summary: '输出数据类型 Inherit: Same as first input（默认）| fixdt(1,16,0)'
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

### **Input U is unit-upper triangular** — 输入矩阵的对角元素值为 1 `off`（默认）| `on`

仅当 *U* 对角线上的所有元素值均为 `1` 时，才选中此复选框。选中后，模块将通过跳过不必要的除法运算来优化其行为。

如果 *U* 对角线上的任何元素值不为 `1`，请勿选中此复选框。当您清除 **Input U is unit-upper triangular** 复选框时，模块始终执行除法运算。

### **Diagonal of complex input U is real** — 复数输入的对角元素为实数 `off`（默认）| `on`

当复数输入 *U* 的对角元素为实数时，选中此选项以优化仿真速度。

**注意**

当 U 为复数定点信号时，您必须选择 **Input U is unit-upper triangular** 或 **Diagonal of complex input U is real**。当选中其中任一选项时，模块将忽略 *U* 对角线的任何虚部。

#### 依赖关系

此参数仅在未选中 **Input U is unit-upper triangular** 时可见。

### 数据类型选项卡

**注意**

浮点继承优先于此窗格上定义的数据类型设置。当输入为浮点时，模块将忽略这些设置，并且所有内部数据类型均为浮点。

### **Rounding mode** — 舍入运算的方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 溢出操作的方法 off（默认）| on

当您选中此参数时，模块将饱和其定点运算的结果。当您清除此参数时，模块将环绕其定点运算的结果。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `fixdt(1,16,0)`

**Product output** 指定 Backward Substitution 模块中乘积运算输出的数据类型。有关乘积输出数据类型的更多信息，请参阅定点数据类型和乘法数据类型。

- `Inherit: Inherit via internal rule` — 模块基于内部规则继承乘积输出数据类型。有关此规则的更多信息，请参阅通过内部规则继承。
- `Inherit: Same as first input` — 模块将乘积输出数据类型指定为与第一个输入数据类型相同。
- `fixdt(1,16,0)` — 模块指定一个有符号、二进制点、定标、定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Product output** 数据类型。要使用该助手，请单击 **Show data type assistant** 按钮 。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as product output` | `Inherit: Same as first input` | `fixdt(1,16,0)`

**Accumulator** 指定 Backward Substitution 模块中累加运算输出的数据类型。有关如何在此模块中使用累加器数据类型的说明，请参阅定点数据类型。

- `Inherit: Inherit via internal rule` — 模块基于内部规则继承累加器数据类型。有关此规则的更多信息，请参阅通过内部规则继承。
- `Inherit: Same as product output` — 模块将累加器数据类型指定为与乘积输出数据类型相同。
- `Inherit: Same as first input` — 模块将累加器数据类型指定为与第一个输入数据类型相同。
- `fixdt(1,16,0)` — 模块指定一个有符号、二进制点定标、定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Accumulator** 数据类型。要使用该助手，请单击 **Show data type assistant** 按钮 。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Output** — 输出数据类型 `Inherit: Same as first input`（默认）| `fixdt(1,16,0)`

**Output** 指定 Backward Substitution 模块输出的数据类型。有关输出数据类型的更多信息，请参阅定点数据类型。

- `Inherit: Same as first input` — 模块将输出数据类型指定为与第一个输入数据类型相同。
- `fixdt(1,16,0)` — 模块指定一个有符号、二进制点定标、定点数据类型，字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Output** 数据类型。要使用该助手，请单击 **Show data type assistant** 按钮。

有关数据类型助手的更多信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Output Minimum** — 模块可以输出的最小值 `[]`（默认）| 标量

指定模块可以输出的最小值。Simulink® 软件使用此最小值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **Output Maximum** — 模块可以输出的最大值 `[]`（默认）| 标量

指定模块可以输出的最大值。Simulink 软件使用此最大值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。
## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Linear System Solvers

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

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

当 U 为上三角矩阵时，求解 U X = B 中的 X

Backward Substitution 模块通过简单的变量回代求解线性系统 *U**X* = *B*，其中：

- *U* 是输入到 **U** 端口的上三角 *M*×*M* 矩阵。
- *B* 是输入到 **B** 端口的 *M*×*N* 矩阵。
- *X* 是 *M*×*N* 输出矩阵，是方程组的解。

模块不检查输入的秩。模块仅使用输入 *U* 的*上三角*中的元素，并忽略下三角元素。当您选中 **Input U is unit-upper triangular** 复选框时，模块假定 *U* 对角线上的元素为 1。当矩阵 *U* 是另一个运算（例如 LDL 分解，其使用对角元素表示 *D* 矩阵）的结果时，这很有用。
