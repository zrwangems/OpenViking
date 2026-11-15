---
type: simulink-block
title: 'Interprocess Data Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / Interprocess Data Communication'
documentation_page: 'interprocessdataread'
documentation_source_path: 'ref/interprocessdataread.html'
language: zh-CN
chinese_source: worker-translation
---

# Interprocess Data Read

## 端口

### 输入

### **msg** — 来自进程间数据通道的数据消息标量

此消息端口从连接的 Interprocess Data Channel 模块接收数据消息。当 Task Manager 模块触发包含此模块的任务时，消息会被处理。有关消息的详细信息，请参阅消息。

#### 依赖项

仅当启用 **启用仿真端口** 参数时，此端口才会出现。

**数据类型：** `SoCData`

### 输出

### **data** — 从另一个处理器读取的数据帧向量

此端口发出通过 Interprocess Data Channel 模块连接的另一个处理器读取的数据帧。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `bus`

### **status** — 进程间数据读取状态 0 | 1 | 2 | 4 | 6

status 端口输出以下值之一：

- `0—`无错误
- `1—`数据不可用
- `2—`数据类型不匹配
- `4—`数据长度不匹配
- `6—`数据类型和数据长度不匹配

#### 依赖项

当禁用 **启用仿真端口** 参数时，此端口会出现。

## 参数

### **启用仿真端口** — 为模块启用外设仿真端口 `on`（默认） | `off`

选择此参数以配置 **msg** 输出端口，从而启用外设仿真能力。

### **数据类型** — 进程间数据通道的数据类型 `double`（默认） | `single` | `int8` | `int16` | `int32` | `int64` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `uint64` | `Boolean` | `bus`

输入进程间数据通道使用的数据类型。

您可以通过单击 >> 按钮或 << 按钮来选择性地显示或隐藏 **数据类型助手** 选项。有关详细信息，请参阅使用数据类型助手指定数据类型。

### **循环 FIFO 深度** — 存储缓冲区数量 `1`（默认） | 正整数

缓冲区是在共享消息 RAM 中创建的循环缓冲区。缓冲区数量是在共享消息 RAM 中一次存储的元素数量。这些不是 FIFO，但会在下一个实例被覆盖。

确保在 Tx 和 Rx 两侧指定的缓冲区数量必须相同。

#### 依赖项

此参数仅在禁用 **启用仿真端口** 参数时可见。

### **循环 FIFO 元素大小** — 从进程间数据通道读取的数据向量的大小 `1`（默认） | 正整数

输入从进程间数据通道读取的数据向量的循环 FIFO 元素大小。

### **通道号** — 选择通道号 `0`（默认） | `1` | `2` | `...`

选择要发送数据的通道。

#### 依赖项

此参数仅在禁用 **启用仿真端口** 参数时可见。

### **参与核心** — 选择处理器的参与核心 `选项因您选择的硬件板而异`

根据您在配置参数窗口中选择的 **硬件板** 选择参与核心。

#### 依赖项

此参数仅在禁用 **启用仿真端口** 参数时可见。

**注意**

确保模型中相应的 Interprocess Data Read 和 Interprocess Data Write 模块的 **通道号**、**缓冲区数量** 和 **参与核心** 参数一致。

### **采样时间** — 采样时间 `-1`（默认） | 正标量

输入要应用于定时器驱动任务子系统的模块采样时间。

## 所属库

SoC Blockset / Processor Interconnect C2000 Microcontroller Blockset / Target Communication Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Target Communication Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Target Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

使用进程间通信通道从另一个处理器接收消息

Interprocess Data Read 模块使用进程间数据通道异步接收来自 SoC 中另一个处理器的消息。Interprocess Data Read 模块连接到 Interprocess Data Channel 模块，后者类似地连接到包含在单独处理器参考模型中的 Interprocess Data Write 模块。在仿真中，来自另一个处理器的数据在包含 Interprocess Data Read 模块和关联异步任务的处理器中被异步接收和处理。此图显示了处理器间数据通道连接的一般视图。

**注意**

- 确保在 Tx 和 Rx 两侧指定的缓冲区数量必须相同。
- 如果您使用单个模型通过 Task Manager 触发多个核心的多处理器建模方法，请使用 Interprocess Data Read 和 Interprocess Data Write 模块在核心之间发送和接收数据。

进程间数据通道图。

要为您的 SoC 模型生成并执行 C 代码，此模块需要 Embedded Coder® Support Package for Infineon® AURIX™ TC4x Microcontrollers 或 Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers。
