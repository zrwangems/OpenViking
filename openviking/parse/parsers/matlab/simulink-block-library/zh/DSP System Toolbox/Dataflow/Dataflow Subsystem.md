---
type: simulink-block
title: 'Dataflow Subsystem'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Dataflow'
documentation_page: 'dataflowsubsystem'
documentation_source_path: 'ref/dataflowsubsystem.html'
language: zh-CN
chinese_source: worker-translation
---

# Dataflow Subsystem

## 端口

### 输入

### **In** — 数据流子系统的信号输入 标量 | 向量 | 矩阵

在子系统中放置 Inport 模块会为该模块添加一个外部输入端口。子系统模块上的端口标签即为 Inport 模块的名称。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
### 输出

### **Out** — 数据流子系统的信号输出 标量 | 向量 | 矩阵

在子系统中放置 Outport 模块会为该模块添加一个输出端口。子系统模块上的端口标签即为 Outport 模块的名称。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

Dataflow Subsystem 模块使用与 Subsystem 模块相同的参数。有关参数说明和程序化使用信息，请参阅 Subsystem, Atomic Subsystem, Nonvirtual Subsystem, CodeReuse Subsystem (Simulink)。

**注意**

最顶层的数据流子系统被视为原子子系统。所有子数据流子系统均被视为虚拟子系统。

### **Latency** — 数据流子系统的延迟 0（默认）| 标量整数

为提高系统吞吐量，增加系统延迟可能是有利的。在属性检查器的 **Execution** 选项卡中指定 **Latency** 值。有关详细信息，请参阅 Latency。

#### 程序化使用

|  |
| --- |
| **模块参数**：`Latency` |
| **类型**：字符向量 |
| **值**：标量整数 |
|  |
| **默认值**：`'0'` |

### **Automatic frame size calculation** — 自动计算帧大小并插入缓冲区 0（默认）| 1

当启用 **Automatic frame size calculation** 参数时，数据流域会自动计算帧大小并向模型中插入缓冲区，从而避免多速率信号处理系统中的信号大小传播错误。有关详细信息，请参阅 Automatic Frame Size Calculation。

#### 程序化使用

|  |
| --- |
| **模块参数**：`AutoFrameSizeCalculation` |
| **类型**：字符向量 |
| **值**：`'off'`|`'on'` |
|  |
| **默认值**：`'off'` |

## 所属库

DSP System Toolbox / Dataflow

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `integera` | `singlea` | `stringa` |
| **直接馈通** | `no` |
| **多维信号** | `yesa` |
| **可变大小信号** | `yesa` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 实际数据类型或功能支持取决于模块实现。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

数据流子系统可以生成单核或多核代码。有关为代码生成设置数据流子系统的详细信息，请参阅 Multicore Simulation and Code Generation of Dataflow Domains。

## 版本历史

**在 R2018b 中引入**

## 描述

执行域设置为 Dataflow 的子系统

Dataflow Subsystem 模块是一个预配置的执行域设置为 dataflow 的 Subsystem 模块。Dataflow Subsystem 使用同步数据流作为计算模型，该模型是数据驱动且静态调度的。

Dataflow Subsystem 有助于

- 通过多线程执行提高仿真吞吐量

  数据流域利用主机的多核 CPU 架构，可以显著提高仿真速度。它会自动对模型进行分区，并使用多个线程对系统进行仿真。通过向系统添加延迟，您可以进一步提高并发性并改善模型的仿真吞吐量。
- 自动推断基于帧的多速率模型的信号大小

有关详细信息，请参阅 Dataflow Domain。
