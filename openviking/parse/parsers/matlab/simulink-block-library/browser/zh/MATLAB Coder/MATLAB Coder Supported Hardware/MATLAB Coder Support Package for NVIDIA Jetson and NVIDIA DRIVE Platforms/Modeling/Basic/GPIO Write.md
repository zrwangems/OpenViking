---
type: simulink-block
title: 'GPIO Write'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Basic'
documentation_page: 'gpiowrite'
documentation_source_path: 'nvidia/ref/gpiowrite.html'
language: zh-CN
chinese_source: worker-translation
---

# GPIO Write

## 端口

### 输入

### **Port\_1** — 设置 GPIO 引脚状态的标量

用于设置 GPIO 引脚状态的输入端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Board** — 目标板名称 `NVIDIA Jetson TX1`（默认） | `NVIDIA Jetson TX2` | `NVIDIA Jetson Nano` | `NVIDIA Jetson AGX Xavier` | `NVIDIA Jetson Xavier NX`

指定目标板的名称。此选择会影响可用于通用输入和输出的引脚。

#### 编程用法

|  |
| --- |
| **模块参数：** `Board` |
| **类型：** character vector, string |
| **值：** `'NVIDIA Jetson TX1'`|`'NVIDIA Jetson TX2'`|`'NVIDIA Jetson Nano'`|`'NVIDIA Jetson AGX Xavier'`|`'NVIDIA Jetson Xavier NX'` |
| **默认值：**  `'NVIDIA Jetson TX1'` |

### **GPIO 编号** — 要写入逻辑状态的 GPIO 引脚，0（默认） | scalar

选择要写入逻辑状态的 GPIO 引脚。

要打开引脚映射表，请点击 **查看引脚映射**。确保为模型的不同模块分配不同的引脚编号。

### **采样时间 (seconds)** — 模块接收数据的时间频率 `0.1`（默认） | `scalar`

指定模块应多久读取一次端口缓冲区。输入大于 `0` 的值或 `-1`（用于继承采样时间）。

当您将此参数指定为 -1 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

此值默认为 `0.1` seconds 的采样时间。较小的值要求处理器在更短时间内完成相同数量的指令，这可能导致任务超限。

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Basic

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

## 描述

设置输出引脚的逻辑状态

使用此模块可：

- 创建到 GPIO 引脚的实际输出。
- 从模型中的其他模块接收逻辑值，作为布尔值流。
- 按由 **采样时间** 确定的时间间隔将逻辑值写入 GPIO 引脚。

**警告**

您可能通过以下方式损坏目标硬件：

- 将 GPIO 引脚短接到地。
- 将高压 GPIO 引脚短接到低压 GPIO 引脚。
- 将 GPIO 引脚连接到高于最大电压的电压源。
- 同时将多个 GPIO 引脚驱动为高电平，从而超过最大电流。
