---
type: simulink-block
title: 'Counter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Buffers, Switches, and Counters'
documentation_page: 'counter'
documentation_source_path: 'ref/counter.html'
language: zh-CN
chinese_source: worker-translation
---

# Counter

## 端口

### 输入

### **Inc/Dec** — 用于触发计数事件的输入信号 标量 | 向量

用于确定模块何时递增或递减计数器的输入信号，指定为实数值标量或向量。如果 **Inc** 或 **Dec** 端口的输入是向量，则模块将该向量视为帧。每次在 **Inc** 或 **Dec** 输入端口发生触发事件时，模块会分别递增或递减计数器。您可以使用 **Count event** 参数控制触发事件的类型。

#### 依赖关系

当您将 **Count direction** 参数设置为 `Up` 时，模块启用 **Inc**（递增）端口。

当您将 **Count direction** 参数设置为 `Down` 时，模块启用 **Dec**（递减）端口。

当您将 **Count event** 参数设置为 `Free running` 时，模块禁用 **Inc**/**Dec** 输入端口。在自由运行模式下，模块以恒定时间间隔计数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Rst** — 复位信号 标量

用于确定模块何时复位计数器的输入信号，指定为实数值标量。**Rst** 端口必须与 **Inc** 或 **Dec** 输入端口具有相同的端口采样时间。每次在 **Rst** 端口发生触发事件时，模块会将计数器复位为其初始值。有关触发事件的详细信息，请参见 Count event。

#### 依赖关系

要启用此端口，请选中 **Reset input** 复选框。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Max** — 最大计数器大小 标量

将最大计数器大小指定为 **Count data type** 可以表示的任何无符号整数。计数器值范围为 `0` 到您作为 **Max** 端口输入指定的值。

#### 依赖关系

要启用此端口，请将 **Counter size** 参数设置为 `Specify via input port`。

**数据类型：** `uint8` | `uint16` | `uint32`

### 输出

### **Cnt** — 计数器的当前值 标量 | 向量

计数器的当前值，指定为标量或向量。当您将 **Count event** 参数设置为 `Free running` 时，**Cnt** 输出是一个 *M*×1 向量，其中包含 *M* 个连续采样时刻中每个时刻的计数值，其中 *M* 是您为 **Samples per output frame** 参数指定的值。

#### 依赖关系

要启用此端口，请将 **Output** 参数设置为 `Count` 或 `Count and Hit`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Hit** — 命中状态 标量 | 向量

您在 **Hit values** 参数中指定的整数值的命中状态。当计数中出现您指定的值时，模块会在 **Hit** 端口输出 `1`。

**注意**

根据 **Hit data type** 参数的设置，模块可能会从 **Hit** 输出端口输出 Boolean 值。

#### 依赖关系

要启用此端口，请将 **Output** 参数设置为 `Hit` 或 `Count and Hit`。

**数据类型：** `Boolean` | `Logical`

## 参数

### **Count direction** — 向上或向下计数 `Up`（默认）| `Down`

指定是 `Up` 计数还是 `Down` 计数。模块图标上的端口标签会根据此参数的值更改为 **Inc**（递增）或 **Dec**（递减）。

- 当您将 **Count direction** 参数设置为 `Up`，并且计数器达到计数器范围的上限时，下一次在 **Inc** 端口发生触发事件时，模块会将计数器重新从零开始。
- 当您将 **Count direction** 参数设置为 `Down`，并且计数器达到零时，下一次在 **Dec** 端口发生触发事件时，模块会将计数器重新从计数器范围的上限开始。

此参数在 Simulink® 正常模式下可调（Simulink）。

**可调：** 是

### **Count event** — 触发事件类型 `Rising edge`（默认）| `Falling edge` | `Either edge` | `Non-zero sample` | `Free running`

指定当在 **Inc**/**Dec** 或 **Rst** 端口收到事件时，触发模块递增、递减或复位计数器的事件类型。您可以选择：

- `Rising edge` — 当 **Inc**/**Dec** 或 **Rst** 端口的输入以下列方式之一表现时，触发计数或复位操作：

  - 从负值上升到正值或零。
  - 从零上升到正值，其中该上升不是从负值上升到零的延续（见下图）。

- `Falling edge` — 当 **Inc**/**Dec** 或 **Rst** 端口的输入以下列方式之一表现时，触发计数或复位操作：

  - 从正值下降到负值或零。
  - 从零下降到负值，其中该下降不是从正值下降到零的延续（见下图）。
- `Either edge` — 当 **Inc**/**Dec** 或 **Rst** 端口的输入是 `Rising edge` 或 `Falling edge` 时，触发计数或复位操作。
- `Non-zero sample` — 当 **Inc**/**Dec** 或 **Rst** 端口的输入在每个采样时间非零时，触发计数或复位操作。
- `Free running` — 禁用 **Inc**/**Dec** 端口，并启用 **Samples per output frame** 和 **Sample time** 模块参数。模块以恒定间隔 *Ts* 递增或递减计数器，该间隔由您使用 **Sample time** 参数指定。有关详细信息，请参见 Free-Running Operation。在此模式下，每当在 **Rst** 端口收到非零采样时，模块都会复位计数器。

#### 依赖关系

当您将此参数设置为 `Free running` 时，模块禁用 **Inc**/**Dec** 端口，并以 **Sample time** 参数指定的恒定间隔计数。

### **Counter size** — 要进行计数的整数值范围 `8 bits`（默认）| `16 bits` | `32 bits` | `User defined` | `Specify via input port`

指定模块进行计数的整数值范围。当模块计数经过整个计数器范围后，下一次在 **Inc**/**Dec** 端口发生触发事件时，模块会按如下方式复位计数器：

- 当您将 **Count direction** 参数设置为 `Up`，并且计数器达到计数器范围的上限时，模块会将计数器重新从零开始。
- 当您将 **Count direction** 参数设置为 `Down`，并且计数器达到零时，模块会将计数器重新从计数器范围的上限开始。

您可以将 **Counter size** 参数设置为以下选项之一：

- `8 bits` — 指定范围为 `0` 到 `255` 的计数器。
- `16 bits` — 指定范围为 `0` 到 `65535` 的计数器。
- `32 bits` — 指定范围为 `0` 到 `2`32–`1` 的计数器。
- `User defined` — 启用 **Maximum count** 参数，该参数允许您将向上计数上限指定为 **Count data type** 可以表示的任何任意无符号整数。计数器值范围为 `0` 到 **Maximum count** 参数的值。
- `Specify via input port` — 启用 **Max** 输入端口，该端口允许您将向上计数上限指定为 **Count data type** 可以表示的任何任意无符号整数。计数器值范围为 `0` 到您作为 **Max** 端口输入指定的值。

### **Maximum count** — 计数器最大值 `255`（默认）| 正整数

将计数器最大值指定为 **Counter data type** 参数所指定数据类型可表示的任何无符号整数。在 Simulink 正常模式下可调（Simulink）。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Counter size** 设置为 `User defined`。

### **Initial count** — 计数器初始值 `0`（默认）| 整数 ≥ 0

将计数器初始值指定为由 **Counter size** 参数定义范围内的任何无符号整数。模块在仿真开始时使用计数器的初始值，并且每次在 **Rst** 端口发生触发事件时，都会将计数器复位回该初始值。

**可调：** 是

### **Output** — 输出计数值、命中值或两者 `Count`（默认）| `Hit` | `Count and Hit`

选择要启用的输出端口。您可以选择启用 `Count`、`Hit` 或 `Count and Hit` 端口。

### **Hit values** — 要标记的计数值 `32`（默认）| 标量 | 向量

指定一个整数或整数向量，当其出现在计数中时，应通过在（可选）**Hit** 输出端口输出 `1` 来标记。仅当您将 **Output** 参数设置为 `Hit` 或 `Count and Hit` 时，此参数才会显示。

**可调：** 是

### **Reset input** — 启用 Rst 输入端口 `on`（默认）| `off`

选中此复选框可启用 **Rst** 输入端口。启用 **Rst** 端口后，每次在 **Rst** 端口发生触发事件时，模块都会将计数器复位为其初始值。要指定触发计数器复位的事件类型，请设置 **Count event** 参数。当您清除 **Reset input** 复选框时，仿真期间无法复位计数器。

### **Samples per output frame** — 每个输出向量中的采样数 `1`（默认）| 正整数

将每个输出向量中的采样数 *M* 指定为正整数。

#### 依赖关系

要启用此参数，请将 **Count event** 设置为 `Free running`。

### **Sample time** — `Free Running` 模式下的采样时间 `1`（默认）| `-1` | 标量 ≥ 0

指定自由运行模式下模块递增或递减计数器的恒定间隔 *T*s。您可以指定大于或等于零的标量，或指定值 `-1` 以继承采样时间。

例如，要使模块每 `5` seconds 递增一次计数器，请将 **Count direction** 参数设置为 `Up`，将 **Count event** 参数设置为 `Free running`，并为 **Sample time** 参数指定值 `5`。在自由运行模式下，输出端口的采样时间始终为 *M**T*s。

#### 依赖关系

要启用此参数，请将 **Count event** 设置为 `Free running`。

### **Count data type** — Cnt 端口的数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

指定 **Cnt** 端口输出的数据类型。

#### 依赖关系

要启用此参数，请将 **Output** 参数设置为 `Count` 或 `Count and Hit`。

### **Hit data type** — Hit 端口的数据类型 `Logical`（默认）| `Boolean`

指定 **Hit** 端口输出的数据类型。

#### 依赖关系

要启用此参数，请将 **Output** 参数设置为 `Hit`，或将其设置为 `Count and Hit`，并将 **Count data type** 参数设置为 `Double`。

## 所属库

DSP System Toolbox / Signal Management / Switches and Counters

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **零交叉检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**早于 R2006a 引入**

## 描述

向上或向下在指定数字范围内计数

Counter 模块在指定数字范围内向上或向下计数。当您将 **Count direction** 参数设置为 `Up` 时，模块启用 **Inc**（递增）端口。当您将 **Count direction** 参数设置为 `Down` 时，模块启用 **Dec**（递减）端口。如果您将 **Count event** 参数设置为 `Free running`，则模块禁用 **Inc** 或 **Dec** 端口，并以恒定时间间隔计数。对于 **Count event** 参数的所有其他设置，每次在 **Inc** 或 **Dec** 输入端口发生触发事件时，模块都会递增或递减计数器。当在可选 **Rst** 端口发生触发事件时，模块会将计数器复位到其初始状态。

Counter 模块接受单通道输入。有关标量输入操作、向量输入操作和自由运行操作的详细信息，请参见算法。
