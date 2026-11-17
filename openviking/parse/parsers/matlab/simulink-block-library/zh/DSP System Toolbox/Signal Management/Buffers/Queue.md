---
type: simulink-block
title: 'Queue'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Buffers'
documentation_page: 'queue'
documentation_source_path: 'ref/queue.html'
language: zh-CN
chinese_source: worker-translation
---

# Queue

## 端口
```yaml
ports:
- name: In
  summary: FIFO 寄存器的输入 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Push
  summary: 将队列推入的触发信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Pop
  summary: 将队列弹出的触发信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Rst
  summary: 清空队列的触发信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Out
  summary: FIFO 寄存器的输出 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Empty
  summary: 指示队列是否为空 1 | 0
  direction: output
  data_types: double | Boolean
- name: Full
  summary: 指示队列是否已满 1 | 0
  direction: output
  data_types: double | Boolean
- name: Num
  summary: 跟踪队列中的元素数量 标量
  direction: output
  data_types: double | uint32
```

### 输入

### **In** — FIFO 寄存器的输入 标量 | 向量 | 矩阵

将 FIFO 寄存器的输入指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Push** — 将队列推入的触发信号 标量

将队列推入的触发信号指定为实数标量。

**Push** 端口的输入必须与 **Pop** 和 **Rst** 端口的输入具有相同的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Pop** — 将队列弹出的触发信号 标量

将队列弹出的触发信号指定为实数标量。

**Pop** 端口的输入必须与 **Push** 和 **Rst** 端口的输入具有相同的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Rst** — 清空队列的触发信号 标量

将队列清空的触发信号指定为实数标量。

**Rst** 端口的输入必须与 **Push** 和 **Pop** 端口的输入具有相同的数据类型。

#### 依赖关系

要启用此端口，请选择 **Show reset port (Rst) to clear internal stack buffer**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out** — FIFO 寄存器的输出 标量 | 向量 | 矩阵

FIFO 寄存器的输出，以标量、向量或矩阵形式返回。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Empty** — 指示队列是否为空 `1` | `0`

模块在此端口返回 `1` 表示队列为空，否则返回 `0`。

#### 依赖关系

要启用此端口，请选择 **Show empty register indicator port (Empty)**。

**数据类型：** `double` | `Boolean`

### **Full** — 指示队列是否已满 `1` | `0`

模块在此端口返回 `1` 表示队列已满，否则返回 `0`。

如果在 **Push onto full register** 参数中选择 `Dynamic reallocation`，则 **Full** 端口保持为 `0`。

#### 依赖关系

要启用此端口，请选择 **Show full register indicator port (Full)**。

**数据类型：** `double` | `Boolean`

### **Num** — 跟踪队列中的元素数量 标量

跟踪任意给定时刻队列中的元素数量。

如果 **In** 端口的数据类型为 `double`，则 **Num** 端口的数据类型为 `double`。否则，**Num** 端口的数据类型为 `uint32`。

#### 依赖关系

要启用此端口，请选择 **Show number of register entries port (Num)**。

**数据类型：** `double` | `uint32`
## 参数
```yaml
parameters:
- name: Register size
  summary: FIFO 寄存器可容纳的条目数 8（默认）| 正整数
  group: ''
- name: Trigger type
  summary: Push、Pop 和 Rst 端口的触发事件类型 Rising edge（默认）| Falling edge | Either edge | Non-zero sample
  group: ''
- name: Push onto full register
  summary: 指定寄存器已满时推入请求的模块行为 Dynamic reallocation（默认）| Ignore | Warning | Error
  group: ''
- name: Pop empty register
  summary: 指定寄存器为空时弹出请求的模块行为 Warning（默认）| Ignore | Error
  group: ''
- name: Show empty register indicator port (Empty)
  summary: 启用 Empty 输出端口 off（默认）| on
  group: ''
- name: Show full register indicator port (Full)
  summary: 启用 Full 输出端口 off（默认）| on
  group: ''
- name: Show number of register entries port (Num)
  summary: 启用 Num 输出端口 off（默认）| on
  group: ''
- name: Show reset port (Rst) to clear internal stack buffer
  summary: 启用 Rst 输入端口 off（默认）| on
  group: ''
- name: Clear output port on reset
  summary: 清空队列时将 Out 端口设置为 0 off（默认）| on
  group: ''
- name: Allow direct feedthrough
  summary: 允许输入数据在 Out 端口立即可用 on（默认）| off
  group: ''
```

### **Register size** — FIFO 寄存器可容纳的条目数 8（默认）| 正整数

FIFO 寄存器可容纳的条目数，指定为正整数。

### **Trigger type** — Push、Pop 和 Rst 端口的触发事件类型 `Rising edge`（默认）| `Falling edge` | `Either edge` | `Non-zero sample`

触发模块执行的事件类型。选择以下选项之一：

| 触发类型 | 描述 |
| --- | --- |
| `Rising edge` | 当触发输入执行以下操作之一时触发模块执行：  - 从负值上升到零或正值。 - 从零上升到正值但不是持续上升。 |
| `Falling edge` | 当触发输入执行以下操作之一时触发模块执行：  - 从正值下降到零或负值。 - 从零下降到负值但不是持续下降。 |
| `Either edge` | 当触发输入类型为 `Rising edge` 或 `Falling edge`（如上所述）时触发模块执行。 |
| `Non-zero sample` | 在触发输入不为零的每个采样时间触发模块执行。 |

触发信号的速率必须与数据信号输入的速率相同。

### **Push onto full register** — 指定寄存器已满时推入请求的模块行为 `Dynamic reallocation`（默认）| `Ignore` | `Warning` | `Error`

指定当模块在 **Push** 端口接收到触发但寄存器已满时的行为。可用选项包括：

- `Dynamic reallocation` — 动态调整寄存器大小，以在内存允许的情况下接受尽可能多的额外输入。

  要使用此选项，请将模型配置参数对话框中 **Code Generation** 窗格上的 **System target file** 参数设置为 `grt_malloc.tlc – Generic Real-Time Target with dynamic memory allocation`。

  **注意**

  如果您的模型包含任何引用的模型，这些模型使用了 **Push onto full register** 参数设置为 `Dynamic reallocation` 的 Queue 模块，则无法在 Simulink® 的加速模式下仿真顶层模型。
- `Ignore` — 忽略触发事件并继续仿真。
- `Warning` — 忽略触发事件但在 MATLAB® 命令窗口中显示警告消息。
- `Error` — 显示错误对话框并终止仿真。

**注意**

**Push onto full register** 是一个诊断参数。与配置参数对话框中的所有诊断参数一样，此参数在 Simulink Coder™ 代码生成软件为此模块生成的代码中设置为 `Ignore`。

### **Pop empty register** — 指定寄存器为空时弹出请求的模块行为 `Warning`（默认）| `Ignore` | `Error`

指定当模块在 **Pop** 端口接收到触发但寄存器为空时的行为。可用选项包括：

- `Ignore` — 忽略触发事件并继续仿真。
- `Warning` — 忽略触发事件但在 MATLAB 命令窗口中显示警告消息。
- `Error` — 显示错误对话框并终止仿真。

**注意**

**Pop empty register** 是一个诊断参数。与配置参数对话框中的所有诊断参数一样，此参数在 Simulink Coder 代码生成软件为此模块生成的代码中设置为 `Ignore`。

### **Show empty register indicator port (Empty)** — 启用 Empty 输出端口 off（默认）| on

选择以启用 **Empty** 输出端口以指示空寄存器。

### **Show full register indicator port (Full)** — 启用 Full 输出端口 off（默认）| on

选择以启用 **Full** 输出端口以指示满寄存器。

### **Show number of register entries port (Num)** — 启用 Num 输出端口 off（默认）| on

选择以启用 **Num** 输出端口以显示寄存器条目数。

### **Show reset port (Rst) to clear internal stack buffer** — 启用 Rst 输入端口 off（默认）| on

选择以启用 **Rst** 输入端口。模块在此端口接收到触发时清空队列。

### **Clear output port on reset** — 清空队列时将 Out 端口设置为 `0` off（默认）| on

如果选择 **Clear output port on reset**，则 **Rst** 端口上的触发事件会清空队列并将 **Out** 端口的值设置为 `0`。此设置同样适用于包含 Queue 模块的已禁用子系统被重新启用时。

#### 依赖关系

要启用此参数，请选择 **Show reset port (Rst) to clear internal stack buffer** 参数。

### **Allow direct feedthrough** — 允许输入数据在 Out 端口立即可用 on（默认）| off

选择以允许输入数据在模块的 **Out** 端口立即可用。清除以将输入数据延迟一个额外帧。

当您选择 **Allow direct feedthrough** 参数并在同一时间步触发两个或更多控制输入端口时，模块按以下顺序执行操作：

1. Reset
2. Push
3. Pop

当您清除 **Allow direct feedthrough** 参数并在同一时间步触发两个或更多控制输入端口时，模块按以下顺序执行操作：

1. Reset
2. Pop
3. Push

触发信号的速率必须与数据信号输入的速率相同。
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
- 当您选择 `Dynamic reallocation` 时，必须将配置参数对话框中 **Code Generation** 窗格上的 **System target file** 参数设置为 `grt_malloc.tlc - Generic Real-Time Target with dynamic memory allocation`。

## 版本历史

**在 R2006a 之前引入**

## 描述

将输入存储在 FIFO 寄存器中

Queue 模块将一系列输入采样存储在先入先出（FIFO）寄存器中。根据端口上的输入，模块可以推入、弹出或清空队列。

当模块在 **Push** 端口接收到触发事件时，它将 **In** 端口上的输入推入队列末尾。当模块在 **Pop** 端口接收到触发事件时，它从队列中弹出第一个元素并将 **Out** 端口保持在该值。第一个被推入队列的输入总是第一个被弹出。
