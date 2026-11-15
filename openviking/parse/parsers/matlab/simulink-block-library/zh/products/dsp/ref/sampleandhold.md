---
type: simulink-block
title: 'Sample and Hold'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Operations / Rate Conversion'
documentation_page: 'sampleandhold'
documentation_source_path: 'ref/sampleandhold.html'
language: zh-CN
chinese_source: official
---

# Sample and Hold

## 端口

### 输入

### **In** — 信号端口 标量 | 向量 | 矩阵

信号端口可以接受标量、向量或矩阵形式的数据。

#### 依赖关系

当您选择**锁存(缓冲)输入**参数时，此端口命名为 **In<Lo>**。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Trigger** — 触发端口 标量

触发输入必须为基于采样的标量，其采样率等于在信号端口上的输入帧速率。您使用**触发器类型**参数指定触发事件。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 采样和保持值 标量 | 向量 | 矩阵

采样和保持输出，以标量、向量或矩阵形式返回。该模块每当在触发端口接收到触发事件时都在信号端口采集输入。然后，该模块保持采集的数据，直到下一个触发事件发生。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### **触发器类型** — 触发器的类型 **上升沿** (默认) | **下降沿** | **任一沿**

触发模块以采集输入信号的事件的类型：

- **上升沿** - 触发输入从负值或零上升到正值。
- **下降沿** - 触发输入从正值或零下降到负值。
- **任一沿** - 触发输入从负值或零上升到正值，或从正值或零下降到负值。

### **初始条件** — 第一个触发事件前的模块输出 `0` (默认) | 标量 | 向量 | 矩阵

使用**初始条件**参数指定第一个触发事件前模块的输出。当采集的输入是 *M*×*N* 矩阵时，**初始条件**可以是 *M*×*N* 矩阵或在矩阵所有元素上重复的标量。当输入是长度为 *M* 的无向向量时，**初始条件**可以是长度为 *M* 的行向量或列向量，或在向量的所有元素上重复的标量。

### **锁存(缓冲)输入** — 锁存缓冲输入 `off` (默认) | `on`

如果选中**锁存(缓冲)输入**复选框，则模块输出来自前一个时间步的输入的值，直到下一个触发事件发生。要以循环方式使用此模块，请选中此复选框。

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

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

Sample and Hold 模块的 HDL 代码生成为 Triggered Subsystem。类似的限制适用于这两个模块。请参阅Using Triggered Subsystems for HDL Code Generation (HDL Coder)。

**HDL 模块属性**

有关 HDL 模块属性描述，请参阅 HDL Block Properties: General (HDL Coder)。

**最佳做法**

在针对 HDL 代码生成的模型中使用 Sample and Hold 模块时，请考虑以下事项：

- 为了使综合结果与 Simulink® 结果相匹配，请使用 FPGA 上的已向同步时钟注册的逻辑来驱动触发端口。
- 良好的做法是在输出信号上放置一个单位延迟。这样做可以防止代码生成器在 HDL 代码中插入额外的旁路寄存器。
- 使用触发子系统，例如 Sample and Hold 模块，可以通过以下方式影响综合结果：

  - 在某些情况下，系统时钟速度可能会稍有下降。
  - 生成的代码使用更多资源，根据触发子系统的实例数量而缩放。

**限制**

Sample and Hold 模块必须满足以下条件：

- DUT（即为其生成代码的顶层子系统）不能为 Sample and Hold 模块。
- 触发信号必须为标量。
- 触发信号的数据类型必须为 `boolean` 或 `ufix1`。
- Sample and Hold 模块的输出必须具有初始值 0。
- Sample and Hold 模块的输入、输出和触发信号必须以相同速率运行。如果输入或触发信号之一是 Signal Editor 模块的输出，请参阅Using the Signal Editor Block (HDL Coder)了解如何匹配速率。

## 版本历史

**在 R2006a 之前推出**

## 描述

采样和保持输入信号

Sample and Hold 模块每当在触发端口（由  标记）接收到触发事件时都在信号端口采集输入。然后，该模块将输出保持在采集的输入值上，直到下一个触发事件发生。
