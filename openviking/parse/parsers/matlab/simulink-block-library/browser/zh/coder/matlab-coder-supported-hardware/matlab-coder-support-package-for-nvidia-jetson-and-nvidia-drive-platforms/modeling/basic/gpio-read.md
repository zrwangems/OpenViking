---
type: simulink-block
title: 'GPIO Read'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Basic'
documentation_page: 'gpioread'
documentation_source_path: 'nvidia/ref/gpioread.html'
language: zh-CN
chinese_source: worker-translation
---

# GPIO Read

## 端口

### 输出

### **output** — GPIO 引脚状态 0 | 1

输入引脚在由 **Sample time** 确定的时间间隔处的逻辑状态。

**数据类型：** `Boolean`

## 参数

### **Board** — 目标开发板名称 `NVIDIA Jetson TX1`（默认） | `NVIDIA Jetson TX2` | `NVIDIA Jetson Nano` | `NVIDIA Jetson AGX Xavier` | `NVIDIA Jetson Xavier NX`

指定目标开发板的名称。此选择会影响可用于通用输入和输出的引脚。

#### 编程用法

|  |
| --- |
| **模块参数：** `Board` |
| **类型：** character vector, string |
| **值：** `'NVIDIA Jetson TX1'`|`'NVIDIA Jetson TX2'`|`'NVIDIA Jetson Nano'`|`'NVIDIA Jetson AGX Xavier'`|`'NVIDIA Jetson Xavier NX'` |
| **默认值：**  `'NVIDIA Jetson TX1'` |

### **GPIO number** — 要读取逻辑状态的 GPIO 引脚 0（默认） | scalar

选择要读取逻辑状态的 GPIO 引脚。

要打开引脚映射表，请点击 **View pin map**。确保为模型的不同模块分配不同的引脚编号。

### **Sample time (seconds)** — 模块接收数据的时间频率 `0.1`（默认） | `scalar`

指定模块读取端口缓冲区的频率。输入大于 `0` 的值，或输入 `-1`（用于继承采样时间）。

当将此参数指定为 -1 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

此值默认为采样时间 `0.1` seconds。较小的值要求处理器在更短时间内完成相同数量的指令，这可能会导致任务超限。

## 所属库

NVIDIA Jetson 和 NVIDIA DRIVE / Basic

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

读取输入引脚的逻辑状态

使用此模块可以：

- 从 GPIO 引脚创建物理输入。
- 在由 **Sample time** 确定的时间间隔读取 GPIO 引脚的逻辑值。
- 将逻辑值作为布尔值流发送到模型中的其他模块。

**警告**

以下操作可能会损坏目标硬件：

- 将 GPIO 引脚短接到地。
- 将高压 GPIO 引脚短接到低压 GPIO 引脚。
- 将 GPIO 引脚连接到高于最大电压的电压源。
- 同时将多个 GPIO 引脚驱动为高电平，从而超过最大电流。
