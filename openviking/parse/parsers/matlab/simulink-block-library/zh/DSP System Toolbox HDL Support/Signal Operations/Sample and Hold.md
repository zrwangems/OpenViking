---
type: simulink-block
title: 'Sample and Hold'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'sampleandhold'
documentation_source_path: '../dsp/ref/sampleandhold.html'
language: zh-CN
chinese_source: worker-translation
---

# Sample and Hold

## 端口
```yaml
ports:
- name: In
  summary: 信号端口 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Trigger
  summary: 触发端口 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_1
  summary: 采样和保持值 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **In** — 信号端口 标量 | 向量 | 矩阵

信号端口可以接受标量、向量或矩阵形式的数据。

#### 依赖关系

当您选中 **Latch (buffer) input** 参数时，此端口命名为 **In<Lo>**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Trigger** — 触发端口 标量

触发输入必须是基于采样的标量，其采样率等于信号端口处的输入帧速率。您使用 **Trigger type** 参数指定触发事件。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 采样和保持值 标量 | 向量 | 矩阵

采样和保持输出，以标量、向量或矩阵形式返回。当模块在触发端口接收到触发事件时，模块会在信号端口获取输入。然后模块保持所获取的数据，直到下一个触发事件发生。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Trigger type
  summary: 触发类型 Rising edge（默认）| Falling edge | Either edge
  group: ''
- name: Initial condition
  summary: 首次触发事件之前的模块输出 0（默认）| 标量 | 向量 | 矩阵
  group: ''
- name: Latch (buffer) input
  summary: 锁存缓冲输入 off（默认）| on
  group: ''
```

### **Trigger type** — 触发类型 `Rising edge`（默认）| `Falling edge` | `Either edge`

触发模块获取输入信号的事件类型：

- `Rising edge` —— 触发输入从负值或零上升为正值。
- `Falling edge` —— 触发输入从正值或零下降为负值。
- `Either edge` —— 触发输入从负值或零上升为正值，或从正值或零下降为负值。

### **Initial condition** — 首次触发事件之前的模块输出 `0`（默认）| 标量 | 向量 | 矩阵

使用 **Initial condition** 参数指定首次触发事件之前模块的输出。当获取的输入是 *M*×*N* 矩阵时，**Initial condition** 可以是 *M*×*N* 矩阵，或是在矩阵所有元素中重复的标量。当输入是长度为 *M* 的无向向量时，**Initial condition** 可以是长度为 *M* 的行向量或列向量，或是在向量所有元素中重复的标量。

### **Latch (buffer) input** — 锁存缓冲输入 `off`（默认）| `on`

如果您选中 **Latch (buffer) input** 复选框，模块会输出上一时间步的输入值，直到下一个触发事件发生。要在循环中使用此模块，请选中此复选框。
## 所属库

DSP System Toolbox / Signal Operations DSP System Toolbox HDL Support / Signal Operations

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

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

Sample and Hold 模块的 HDL 代码生成为 Triggered Subsystem。类似的限制适用于这两个模块。请参阅 Using Triggered Subsystems for HDL Code Generation (HDL Coder)。

**HDL 模块属性**

有关 HDL 模块属性描述，请参阅 HDL Block Properties: General (HDL Coder)。

**最佳实践**

在面向 HDL 代码生成的目标模型中使用 Sample and Hold 模块时，请考虑以下事项：

- 为使综合结果与 Simulink® 结果匹配，请使用 FPGA 上的寄存逻辑（带同步时钟）驱动触发端口。
- 在输出信号上放置单位延迟是一种良好实践。这样做可以防止代码生成器在 HDL 代码中插入额外的旁路寄存器。
- 使用触发子系统（如 Sample and Hold 模块）可能会通过以下方式影响综合结果：

  - 在某些情况下，系统时钟速度可能会小幅下降。
  - 生成的代码使用更多资源，资源量随触发子系统实例数量而增加。

**限制**

Sample and Hold 模块必须满足以下条件：

- DUT（即为其生成代码的顶层子系统）不能是 Sample and Hold 模块。
- 触发信号必须是标量。
- 触发信号的数据类型必须是 `boolean` 或 `ufix1`。
- Sample and Hold 模块的输出必须具有初始值 0。
- Sample and Hold 模块的输入、输出和触发信号必须以相同速率运行。如果输入或触发信号之一是 Signal Editor 模块的输出，请参阅 Using the Signal Editor Block (HDL Coder) 了解如何匹配速率。

## 版本历史

**在 R2006a 之前引入**

## 描述

采样和保持输入信号

当 Sample and Hold 模块在触发端口接收到触发事件（由 标记）时，模块会在信号端口获取输入。然后模块将输出保持为所获取的输入值，直到下一个触发事件发生。
