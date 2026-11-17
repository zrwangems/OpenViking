---
type: simulink-block
title: 'Forward Substitution'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Linear System Solvers'
documentation_page: 'forwardsubstitution'
documentation_source_path: 'ref/forwardsubstitution.html'
language: zh-CN
chinese_source: worker-translation
---

# Forward Substitution

## 端口
```yaml
ports:
- name: L
  summary: 输入下三角矩阵，*M*×*M* 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: B
  summary: '*B* 矩阵，*M*×*N* 矩阵 | *M*×1 向量'
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: X
  summary: 方程组的解，*M*×*N* 矩阵 | *M*×1 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
```

### 输入

### **L** — 输入下三角矩阵，*M*×*M* 矩阵

通过此端口指定输入下三角
*M*×*M* 矩阵
*L*。输入 *L*
和 *B* 必须具有相同的行数。

当输入 *L* 为定点数时，仅支持有符号数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是

### **B** — *B* 矩阵，*M*×*N* 矩阵 | *M*×1 向量

将方程
*L**X* = *B*
中的 *B* 矩阵指定为 *M*×*N* 矩阵或
*M*×1 向量。

当指定 *M*×1 向量时，模块将端口
**B** 处输入的长度为 *M* 的向量视为 *M*×1 矩阵。
输入 *L* 和 *B* 必须具有相同的行数。

当输入 *B* 为定点数时，仅支持有符号数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是
### 输出

### **X** — 方程组的解，*M*×*N* 矩阵 | *M*×1 矩阵

模块以 *M*×*N* 矩阵
或 *M*×1 矩阵的形式返回输出。*X*
矩阵的大小与 *B* 矩阵的大小相同。

当输入为定点数时，输出矩阵
*X* 仅为有符号定点数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: 输入 L 为单位下三角矩阵
  summary: 输入矩阵的对角线元素的值为 1 off（默认） | on
  group: 主选项卡
- name: 复数输入 L 的对角线为实数
  summary: 复数输入的对角元素为实数 off（默认）| on
  group: 主选项卡
- name: 舍入模式
  summary: 舍入运算的方法 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型选项卡
- name: 整数溢出时饱和
  summary: 溢出处理方式 off（默认）| on
  group: 数据类型选项卡
- name: Product output
  summary: '乘积输出数据类型 Inherit: Inherit via internal rule（默认） | Inherit: Same as first input | fixdt(1,16,0)'
  group: 数据类型选项卡
- name: Accumulator
  summary: '累加器数据类型 Inherit: Inherit via internal rule（默认） | Inherit: Same as product output | Inherit: Same as first input
    | fixdt(1,16,0)'
  group: 数据类型选项卡
- name: Output
  summary: '输出数据类型 Inherit: Same as first input（默认值）| fixdt(1,16,0)'
  group: 数据类型选项卡
- name: Output Minimum
  summary: 模块可输出的最小值 []（默认值）| 标量
  group: 数据类型选项卡
- name: Output Maximum
  summary: 模块可输出的最大值 []（默认值）| 标量
  group: 数据类型选项卡
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认值）| on
  group: 数据类型选项卡
```

### 主选项卡

### **输入 L 为单位下三角矩阵** — 输入矩阵的对角线元素的值为 1 `off`（默认） | `on`

仅当 *L* 的对角线上所有元素的值均为 `1` 时，才选中此复选框。
选中后，模块会通过跳过不必要的除法运算来优化其行为。

如果 *L* 的对角线上有任何元素的值不为 `1`，请不要选中此复选框。
清除 **输入 L 为单位下三角矩阵** 复选框时，模块始终执行除法运算。

### **复数输入 L 的对角线为实数** — 复数输入的对角元素为实数 `off`（默认）| `on`

选中此参数可在复数输入 *L* 的对角元素为实数时优化仿真速度。

**注意**

当 *L* 为复数定点信号时，必须选择 **输入 L 为单位下三角矩阵** 或 **复数输入 L 的对角线为实数**。在这些情况下，模块会忽略 *L* 对角线中的任何虚部。

#### 依赖关系

仅当未选择 **输入 L 为单位上三角矩阵** 时，此参数才可见。

### 数据类型选项卡

**注意**

浮点继承优先于此窗格中定义的数据类型设置。当输入为浮点时，模块会忽略这些设置，并且所有内部数据类型均为浮点。

### **舍入模式** — 舍入运算的方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下各项之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

### **整数溢出时饱和** — 溢出处理方式 off（默认）| on

选择此参数时，模块会将其定点运算的结果进行饱和处理。清除此参数时，模块会将其定点运算的结果进行绕回处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as first input` | `fixdt(1,16,0)`

**Product output** 指定 Backward Substitution 模块中乘积运算输出的数据类型。有关乘积输出数据类型的详细信息，请参阅定点数据类型和乘法数据类型。

- `Inherit: Inherit via internal rule`
  — 模块根据内部规则继承乘积输出数据类型。有关此规则的详细信息，请参阅通过内部规则继承。
- `Inherit: Same as first input`
  — 模块将乘积输出数据类型指定为与第一个输入的数据类型相同。
- `fixdt(1,16,0)` — 模块指定一种有符号的二进制点定标定点数据类型，其字长为 16 bits，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Product output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as product output` | `Inherit: Same as first input` | `fixdt(1,16,0)`

**Accumulator** 指定 Backward Substitution 模块中累加运算输出的数据类型。有关如何在此模块中使用累加器数据类型的图示，请参阅“定点数据类型”一节。

- `Inherit: Inherit via internal rule`
  — 模块根据内部规则继承累加器数据类型。有关此规则的详细信息，请参阅“通过内部规则继承”。
- `Inherit: Same as product output`
  — 模块将累加器数据类型指定为与乘积输出数据类型相同。
- `Inherit: Same as first input`
  — 模块将累加器数据类型指定为与第一个输入数据类型相同。
- `fixdt(1,16,0)` — 模块指定一种有符号、二进制点定标的定点数据类型，其字长为 16 位，小数长度为 0。

或者，您可以使用 **Data Type Assistant** 设置 **Accumulator** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮。

有关数据类型助手的详细信息，请参阅“使用数据类型助手指定数据类型 (Simulink)”。

### **Output** — 输出数据类型 `Inherit: Same as first input`（默认值）| `fixdt(1,16,0)`

**Output** 指定 Backward Substitution 模块输出的数据类型。有关输出数据类型的详细信息，请参阅“定点数据类型”一节。

- `Inherit: Same as first input`
  — 模块将输出数据类型指定为与第一个输入的数据类型相同。
- `fixdt(1,16,0)` — 模块指定一种有符号、按二进制小数点定标的定点数据类型，其字长为 16 位，小数长度为 0。

此外，您还可以使用 **Data Type Assistant**（数据类型助手）设置 **Output** 数据类型。要使用该助手，请点击 **Show data type assistant**（显示数据类型助手）按钮。

有关数据类型助手的详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Output Minimum** — 模块可输出的最小值 `[]`（默认值）| 标量

指定模块可输出的最小值。Simulink® 软件使用此最小值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **Output Maximum** — 模块可输出的最大值 `[]`（默认值）| 标量

指定模块可输出的最大值。Simulink 软件使用此最大值执行：

- 仿真范围检查。请参阅指定信号范围 (Simulink)。
- 定点数据类型的自动定标。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认值）| `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。
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

生成的代码在某些条件下依赖于 `memcpy` 或
`memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

当 L 为下三角矩阵时，求解 L X = B 中的 X

Forward Substitution 模块通过简单的变量前向替换求解线性系统
*L**X* = *B*，其中：

- *L* 是输入到 **L** 端口的下三角
  *M*×*M* 矩阵。
- *B* 是输入到 **B** 端口的
  *M*×*N* 矩阵。
- *X* 是 *M*×*N*
  输出矩阵，也是该方程组的解。

模块不检查输入的秩。模块仅使用输入 *L* 的
*下三角* 中的元素，并忽略
上三角元素。当您选择 **Input L is unit-lower triangular** 时，
模块假定 *L* 的对角线元素均为 1。当矩阵 *L* 是另一种运算（例如
LDL 分解）的结果，且该运算使用对角线元素来表示 *D*
矩阵时，此功能非常有用。
