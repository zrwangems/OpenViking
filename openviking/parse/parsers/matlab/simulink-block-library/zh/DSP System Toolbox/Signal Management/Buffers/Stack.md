---
type: simulink-block
title: 'Stack'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Buffers'
documentation_page: 'stack'
documentation_source_path: 'ref/stack.html'
language: zh-CN
chinese_source: worker-translation
---

# Stack

## 端口
```yaml
ports:
- name: In
  summary: 输入标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Push
  summary: 将输入标量推入栈的触发事件
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Pop
  summary: 弹出元素的触发事件 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Rst
  summary: 清空栈内容 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Out
  summary: 输出标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Empty
  summary: 空栈指示端口 标量
  direction: output
  data_types: Boolean
- name: Full
  summary: 满栈指示端口 标量
  direction: output
  data_types: Boolean
- name: Num
  summary: 栈条目数端口 标量
  direction: output
  data_types: double | uint32
```

### 输入

### **In** — 输入标量 | 向量 | 矩阵

将输入指定为标量、向量或矩阵。

当模块在 **Push** 端口接收到触发事件时，模块将 **In** 端口的输入推入栈顶。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是

### **Push** — 将输入标量推入栈的触发事件

在此端口指定触发事件，以将 **In** 端口的输入推入栈顶。模块最后推入栈的输入始终是最先被弹出的。

此端口的输入必须与 **Pop** 和 **Rst** 输入端口的输入具有相同的内置数据类型

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Pop** — 弹出元素的触发事件 标量

在此端口指定触发事件，以弹出栈顶元素并将 **Out** 端口保持在该值。模块最后推入栈的输入始终是最先被弹出的。

此端口的输入必须与 **Push** 和 **Rst** 输入端口的输入具有相同的内置数据类型

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Rst** — 清空栈内容 标量

在此端口指定触发事件，以清空栈内容。当您选择 **Clear output port on reset** 时，**Rst** 端口上的触发事件将清空栈并将 **Out** 端口的值设置为零。此设置同样适用于包含 Stack 模块的已禁用子系统被重新启用的情况。在这种情况下，当您选择 **Clear output port on reset** 时，**Out** 端口的值仅被重置为零。

此端口的输入必须与 **Push** 和 **Pop** 输入端口的输入具有相同的内置数据类型。

#### 依赖关系

要启用此端口，请选择 **Show reset port (Rst) to clear internal stack buffer**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — 输出标量 | 向量 | 矩阵

栈输出，以标量、向量或矩阵形式返回。当您在 **Pop** 端口指定触发事件时，模块弹出栈顶元素并将 **Out** 端口保持在该值。模块最后推入栈的输入始终是最先被弹出的。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
**复数支持：** 是

### **Empty** — 空栈指示端口 标量

当栈为空时，**Empty** 端口输出高电平（1），否则输出低电平（0）。

#### 依赖关系

要启用此端口，请选择 **Show empty stack indicator port (Empty)**。

**数据类型：** `Boolean`

### **Full** — 满栈指示端口 标量

当栈为满时，**Full** 端口输出高电平（1），否则输出低电平（0）。当您在 **Push full stack** 参数中选择 `Dynamic reallocation` 时，**Full** 端口保持低电平。

#### 依赖关系

要启用此端口，请选择 **Show full stack indicator port (Full)**。

**数据类型：** `Boolean`

### **Num** — 栈条目数端口 标量

**Num** 端口通过此端口输出栈条目数。此值表示当前栈上的条目数。当 **In** 端口的输入为双精度浮点数据类型时，模块在此端口输出双精度浮点值。当 **In** 端口的输入不是双精度浮点值时，模块在此端口输出 32 位无符号整数值。

#### 依赖关系

要启用此端口，请选择 **Show number of stack entries port (Num)**。

**数据类型：** `double` | `uint32`
## 参数
```yaml
parameters:
- name: Stack depth
  summary: 栈可容纳的条目数 8（默认）| 正整数
  group: ''
- name: Trigger type
  summary: 触发类型 Rising edge（默认）| Falling edge | Either edge | Non-zero sample
  group: ''
- name: Push full stack
  summary: 满栈时推入 Dynamic reallocation（默认）| Ignore | Warning | Error
  group: ''
- name: Pop empty stack
  summary: 空栈时弹出 Warning（默认）| Ignore | Error
  group: ''
- name: Show empty stack indicator port (Empty)
  summary: 启用空栈指示端口 off（默认）| on
  group: ''
- name: Show full stack indicator port (Full)
  summary: 启用满栈指示端口 off（默认）| on
  group: ''
- name: Show number of stack entries port (Num)
  summary: 启用栈条目数端口 off（默认）| on
  group: ''
- name: Show reset port (Rst) to clear internal stack buffer
  summary: 启用复位端口 off（默认）| on
  group: ''
- name: Clear output port on reset
  summary: 复位时清除输出端口 off（默认）| on
  group: ''
```

### **Stack depth** — 栈可容纳的条目数 `8`（默认）| 正整数

将 LIFO 寄存器可容纳的条目数指定为正整数。

### **Trigger type** — 触发类型 `Rising edge`（默认）| `Falling edge` | `Either edge` | `Non-zero sample`

指定触发模块执行的事件类型。触发信号的速率必须与数据信号输入的速率相同。

将 **Push**、**Pop** 和 **Rst** 端口的触发事件指定为以下选项之一：

- `Rising edge` — 当触发输入执行以下操作之一时触发模块执行：

  - 从负值上升到正值或 0
  - 从 0 上升到正值，其中该上升不是从负值到 0 的上升的延续（见图）
- `Falling edge` — 当触发输入执行以下操作之一时触发模块执行：

  - 从正值下降到负值或 0
  - 从 0 下降到负值，其中该下降不是从正值到 0 的下降的延续（见图）

- `Either edge` — 当触发输入表现为 `Rising edge` 或 `Falling edge` 中所述的行为时触发模块执行。
- `Non-zero sample` — 在触发输入不为 0 的每个采样时间触发模块执行。

### **Push full stack** — 满栈时推入 `Dynamic reallocation`（默认）| `Ignore` | `Warning` | `Error`

使用此参数指定当寄存器已满时模块如何响应 **Push** 端口上的触发。

- `Dynamic reallocation` —— 动态调整寄存器大小，以在内存允许的情况下接受尽可能多的额外输入。要了解给定时间栈上有多少元素，请通过选择 **Show number of stack entries port** 参数来启用 **Num** 输出端口。

  要选择此选项，您必须将“模型配置参数”对话框中 **Code Generation** 窗格上的 **System target file** 参数设置为 `grt_malloc.tlc – Generic Real-Time Target with dynamic memory allocation`。

  **注意**

  如果您的模型包含任何引用模型，且这些引用模型使用的 Stack 模块的 **Push full stack** 参数设置为 `Dynamic reallocation`，则无法在 Simulink® Accelerator 模式下仿真顶层模型。
- `Ignore` — 忽略触发事件并继续仿真。
- `Warning` — 忽略触发事件但在 MATLAB® 命令窗口中显示警告消息。
- `Error` — 显示错误对话框并终止仿真。

**注意**

**Push full stack** 参数是诊断参数。与“配置参数”对话框上的所有诊断参数一样，Simulink Coder™ 代码生成软件为此模块生成的代码中，此参数设置为 `Ignore`。

### **Pop empty stack** — 空栈时弹出 `Warning`（默认）| `Ignore` | `Error`

使用此参数指定当寄存器为空时模块如何响应 **Pop** 端口上的触发。

- `Warning` — 忽略触发事件但在 MATLAB 命令窗口中显示警告消息。
- `Ignore` — 忽略触发事件并继续仿真。
- `Error` — 显示错误对话框并终止仿真。

**注意**

**Pop empty stack** 参数是诊断参数。与“配置参数”对话框上的所有诊断参数一样，Simulink Coder 代码生成软件为此模块生成的代码中，此参数设置为 `Ignore`。

### **Show empty stack indicator port (Empty)** — 启用空栈指示端口 `off`（默认）| `on`

启用 **Empty** 输出端口，当栈为空时为高电平（`1`），否则为低电平（`0`）。

### **Show full stack indicator port (Full)** — 启用满栈指示端口 `off`（默认）| `on`

启用 **Full** 输出端口，当栈为满时为高电平（`1`），否则为低电平（`0`）。当您在 **Push full stack** 参数中选择 `Dynamic reallocation` 时，`Full` 端口保持低电平。

### **Show number of stack entries port (Num)** — 启用栈条目数端口 `off`（默认）| `on`

启用 **Num** 输出端口，该端口跟踪当前栈上的条目数。当 **In** 端口的输入为双精度值时，**Num** 端口的输出也为双精度值。否则，**Num** 端口的输出为 32 位无符号整数值。

### **Show reset port (Rst) to clear internal stack buffer** — 启用复位端口 `off`（默认）| `on`

启用 **Rst** 输入端口，以便在模块接收到 **Trigger type** 参数中指定的触发时清空栈。

### **Clear output port on reset** — 复位时清除输出端口 `off`（默认）| `on`

当模块在 **Rst** 输入端口接收到触发时，将 **Out** 端口重置为 0（除清空栈之外）。
## 所属库

DSP System Toolbox / Signal Management / Buffers

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

以下限制适用：

- 生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。
- 当您选择 `Dynamic reallocation` 时，“配置参数”对话框中 **Code Generation** 窗格上的 **System target file** 参数必须设置为 `grt_malloc.tlc - Generic Real-Time Target with dynamic memory allocation`。

## 版本历史

**在 R2006a 之前推出**

## 描述

将输入存储到 LIFO 寄存器中

Stack 模块将一系列输入采样存储在先进后出（LIFO）寄存器中。您可以在 **Stack depth** 参数中设置寄存器容量。模块的输入可以是标量、向量或矩阵。

当模块在 **Push** 端口接收到触发事件时，它将 **In** 端口的输入推入栈顶。当它在 **Pop** 端口接收到触发事件时，模块弹出栈顶元素并将 **Out** 端口保持在该值。模块最后推入栈的输入始终是最先被弹出的。

当您在同一时间步触发两个或多个控制输入端口时，模块按以下顺序执行操作：

1. 复位（Rst）
2. 推入（Push）
3. 弹出（Pop）
