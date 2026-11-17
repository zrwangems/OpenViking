---
type: simulink-block
title: 'Array-Vector Multiply'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Math Functions / Matrices and Linear Algebra / Matrix Operations'
documentation_page: 'arrayvectormultiply'
documentation_source_path: 'ref/arrayvectormultiply.html'
language: zh-CN
chinese_source: worker-translation
---

# Array-Vector Multiply

## 端口
```yaml
ports:
- name: A
  summary: 数组输入 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: V
  summary: 向量输入 向量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Port_1
  summary: 相乘后的输出 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
```

### 输入

### **A** — 数组输入 向量 | 矩阵

将数组输入指定为向量或矩阵。

如果输入为定点，则它必须是有符号整数或具有 2 的幂斜率且零偏置的有符号定点值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

### **V** — 向量输入 向量

将向量输入指定为向量。

#### 依赖关系

此端口仅在将 **Vector (V) source** 参数设置为 `Input port` 时出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是
### 输出

### **Port\_1** — 相乘后的输出 向量 | 矩阵

Array-Vector Multiply 模块的输出，以向量或矩阵形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Multiply along dimension
  summary: 沿其乘以输入数组的维度 2（默认）| 正整数
  group: 主选项卡
- name: Vector (V) source
  summary: 向量来源 Input port（默认）| Dialog parameter
  group: 主选项卡
- name: Vector (V)
  summary: 向量参数 [0.5 0.25]（默认）| 向量
  group: 主选项卡
- name: Rounding mode
  summary: 舍入运算的方法 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型选项卡
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: 数据类型选项卡
- name: Vector (V)
  summary: '向量元素的字长和小数长度 Inherit: Same word length as input（默认）| fixdt(1,16,0) | <data type expression>'
  group: 数据类型选项卡
- name: Vector (V) Minimum
  summary: 向量元素的最小值 []（未指定）（默认）| 标量
  group: 数据类型选项卡
- name: Vector (V) Maximum
  summary: 向量元素的最大值 []（未指定）（默认）| 标量
  group: 数据类型选项卡
- name: Product output
  summary: '乘积输出数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as first input | fixdt([],16,0) | <data type expression>'
  group: 数据类型选项卡
- name: Accumulator
  summary: '累加器数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as first input | Inherit: Same as product output
    | fixdt([],16,0) | <data type expression>'
  group: 数据类型选项卡
- name: Output
  summary: '输出数据类型 Inherit: Same as product output（默认）| Inherit: Same as first input | Inherit: Same as first input | fixdt([],16,0)
    | <data type expression>'
  group: 数据类型选项卡
- name: Output Minimum
  summary: 模块输出的最小值 []（未指定）（默认）| 标量
  group: 数据类型选项卡
- name: Output Maximum
  summary: 模块输出的最大值 []（未指定）（默认）| 标量
  group: 数据类型选项卡
- name: Lock data type settings against changes by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: 数据类型选项卡
```

### 主选项卡

### **Multiply along dimension** — 沿其乘以输入数组的维度 `2`（默认）| 正整数

将输入数组 *A* 沿其与向量 *V* 的元素相乘的维度指定为正整数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Vector (V) source** — 向量来源 `Input port`（默认）| `Dialog parameter`

将向量 *V* 的来源设置为以下选项之一。

- `Input port` — 向量来自输入端口。
- `Dialog parameter` — 向量来自对话框参数 **Vector (V)**。

### **Vector (V)** — 向量参数 `[0.5 0.25]`（默认）| 向量

指定向量 *V*。

#### 依赖关系

此参数仅在将 **Vector (V) source** 参数设置为 `Dialog parameter` 时出现。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

### 数据类型选项卡

**注意**

浮点继承优先于 **Data Types** 选项卡上定义的数据类型设置。当输入为浮点时，模块会忽略这些设置，所有内部数据类型均为浮点。

### **Rounding mode** — 舍入运算的方法 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式设置为以下选项之一。

- `Ceiling`
- `Convergent`
- `Floor`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关详细信息，请参阅 rounding mode。

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

选中此参数时，模块会对其定点运算的结果进行饱和处理。清除此参数时，模块会对其定点运算的结果进行回绕处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅 overflow mode for fixed-point operations。

### **Vector (V)** — 向量元素的字长和小数长度 `Inherit: Same word length as input`（默认）| `fixdt(1,16,0)` | `<data type expression>`

使用此参数指定向量 *V* 元素的字长和小数长度。将此参数选择为以下选项之一。

- `Inherit: Same word length as input` — 继承数据类型，使其与输入数组 *A* 的数据类型相同。
- `fixdt(1,16,0)` — 指定一个有符号、二进制小数点、定标、定点数据类型，其字长为 16 位，小数长度为 0。
- `<data type expression>` — 允许您指定一个求值结果为有效数据类型的表达式。

或者，您可以使用 **Data Type Assistant** 设置 **Vector (V)** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮 。

有关数据类型助手的详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

**注意**

当向量通过模块的输入端口传入时，其元素的数据类型和定标将从驱动模块继承。

#### 依赖关系

此参数仅在将 **Main** 选项卡上的 **Vector (V) source** 参数设置为 `Dialog parameter` 时出现。

### **Vector (V) Minimum** — 向量元素的最小值 `[]`（未指定）（默认）| 标量

指定向量 *V* 元素的最小值。默认值为 `[]`（未指定）。Simulink® 使用此值执行：

- 参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 定点数据类型的自动定标。

#### 依赖关系

此参数仅在将 **Main** 选项卡上的 **Vector (V) source** 参数设置为 `Dialog parameter` 时出现。

### **Vector (V) Maximum** — 向量元素的最大值 `[]`（未指定）（默认）| 标量

指定向量 *V* 元素的最大值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 定点数据类型的自动定标。

#### 依赖关系

此参数仅在将 **Main** 选项卡上的 **Vector (V) source** 参数设置为 `Dialog parameter` 时出现。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `fixdt([],16,0)` | `<data type expression>`

指定 Array-Vector Multiply 模块中乘积运算输出的数据类型。有关说明此模块中乘积输出数据类型用法的图示，请参阅 Fixed-Point Data Types and Multiplication Data Types。将此参数设置为以下选项之一。

- `Inherit: Inherit via internal rule` — 基于内部规则继承数据类型。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as first input` — 继承数据类型，使其与输入数组 *A* 的数据类型相同。
- `fixdt([],16,0)` — 允许您指定数据类型的定点属性。
- `<data type expression>` — 允许您指定一个求值结果为有效数据类型的表达式。

或者，您可以使用 **Data Type Assistant** 设置 **Product output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮 。

有关数据类型助手的详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `Inherit: Same as product output` | `fixdt([],16,0)` | `<data type expression>`

指定 Array-Vector Multiply 模块中累加运算输出的数据类型。有关说明此模块中累加器数据类型用法的图示，请参阅 Fixed-Point Data Types。将此参数设置为以下选项之一。

- `Inherit: Inherit via internal rule` — 基于内部规则继承数据类型。有关此规则的详细信息，请参阅 Inherit via Internal Rule。
- `Inherit: Same as first input` — 继承数据类型，使其与输入数组 *A* 的数据类型相同。
- `Inherit: Same as product output` — 继承数据类型，使其与乘积输出数据类型相同。
- `fixdt([],16,0)` — 允许您指定数据类型的定点属性。
- `<data type expression>` — 允许您指定一个求值结果为有效数据类型的表达式。

或者，您可以使用 **Data Type Assistant** 设置 **Accumulator** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮 。

有关数据类型助手的详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出数据类型 `Inherit: Same as product output`（默认）| `Inherit: Same as first input` | `Inherit: Same as first input` | `fixdt([],16,0)` | `<data type expression>`

指定输出数据类型。有关说明此模块中输出数据类型用法的图示，请参阅 Fixed-Point Data Types。将此参数设置为以下选项之一。

- `Inherit: Same as first input` — 继承数据类型，使其与输入数组 *A* 的数据类型相同。
- `Inherit: Same as product output` — 继承数据类型，使其与乘积输出数据类型相同。
- `fixdt([],16,0)` — 允许您指定数据类型的定点属性。
- `<data type expression>` — 允许您指定一个求值结果为有效数据类型的表达式。

有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

或者，您可以使用 **Data Type Assistant** 设置 **Output** 数据类型。要使用该助手，请点击 **Show data type assistant** 按钮 。

有关数据类型助手的详细信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output Minimum** — 模块输出的最小值 `[]`（未指定）（默认）| 标量

指定模块输出的最小值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动定标。

### **Output Maximum** — 模块输出的最大值 `[]`（未指定）（默认）| 标量

指定模块应输出的最大值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink)。
- 定点数据类型的自动定标。

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。
## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2007b 中引入**

## 描述

沿指定维度将数组乘以向量

Array-Vector Multiply 模块将 *N* 维输入数组 *A* 的指定维度中的值乘以输入向量 *V* 中的值。

输入 *V* 的长度必须与 *A* 的指定维度的长度相同。Array-Vector Multiply 模块将 *V* 的每个元素乘以 *A* 沿该维度的对应元素。

考虑一个 3 维 *M*×*N*×*P* 输入数组 *A(i,j,k)* 和一个 *N*×1 输入向量 *V*。当 **Multiply along dimension** 参数设置为 `2` 时，模块的输出 *Y(i,j,k)* 为

Y(i,j,k)=A(i,j,k)\*V(j)

其中

1≤i≤M1≤j≤N1≤k≤P

Array-Vector Multiply 模块的输出与输入数组 *A* 的大小相同。此模块接受实数和复数浮点及定点输入。
