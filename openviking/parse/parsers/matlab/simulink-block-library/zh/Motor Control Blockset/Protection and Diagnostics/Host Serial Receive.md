---
type: simulink-block
title: 'Host Serial Receive'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Protection and Diagnostics'
documentation_page: 'hostserialreceive'
documentation_source_path: 'ref/hostserialreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# Host Serial Receive

## 端口

### 输出

### **data** — 输出接收数据的端口 标量

先进先出（FIFO）缓冲区接收数据。在每个时间步，`data` 端口从缓冲区输出请求的值。

**数据类型：** `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **status** — 事务状态 标量

事务的状态。状态可以是以下值之一：

- 0 — 无错误
- 1 — 模块等待接收数据时发生超时
- 2 — 接收数据中存在错误（校验和错误）
- 3 — SCI 奇偶校验错误标志 — 当接收到的字符存在不匹配时发生
- 4 — SCI 帧错误标志 — 当未找到预期的停止位时发生

#### 依赖

要启用此端口，请选择 **Output receiving status** 参数。

**数据类型：** `uint16`

## 参数

### **Serial Connection** — 用于接收数据的串口 `Serial 1`（默认）| `Serial 2` | `Serial 3` | `Serial 4`

指定一个串口以接收来自目标硬件的通信。从列表中选择一个可用的串口。您可以使用 Host Serial Setup 模块配置所选端口。如果您未配置串口，模块将提示您进行配置。每个 Host Serial Receive 模块必须有一个已配置的串口。如果您在仿真中使用多个端口，则必须分别配置每个端口。

### **Additional package header** — 包头部数据 `'S'`（默认）| 标量

指定位于接收数据包前端的数据，该数据不属于正在接收的数据，通常表示数据的起始。附加包头部必须是一个 ASCII 值。您可以使用文本值或范围在 (0–255) 内的数值。您必须在此字段中输入的文本两侧加上单引号，但引号不会被接收，也不计入总字节数。

### **Additional package terminator** — 包终止符数据 `'E'`（默认）| 标量

指定位于接收数据包末端的数据，该数据不属于正在接收的数据，通常表示数据的结束。附加包终止符必须是一个 ASCII 值。您可以使用文本值或范围在 (0–255) 内的数值。您必须在此字段中输入的文本两侧加上单引号，但引号不会被接收，也不计入总字节数。

### **Data type** — 输出数据类型 `single`（默认）| `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

指定模块输出的数据类型。

### **Data size** — 输出数据大小 `1`（默认）| 标量 | 矩阵

指定输出数据大小或每个仿真时间步应读取的值的数量。

### **Initial output** — 默认模块输出值 `0`（默认）| 标量

指定模块的初始或默认输出值。例如，如果发生连接超时且 **Action taken when connection times out** 参数设置为 `Output the last received value`，但模块尚未接收到任何值，则使用此值。

### **Action taken when connection times out** — 连接超时时模块采取的操作 `Output the last received value`（默认）| `Output custom value` | `Error`

指定发生连接超时时输出什么。

- `Output the last received value` — 模块输出在前一个时间步接收到的值。如果模块之前未接收到值，则输出 **Initial output** 参数的值。
- `Output custom value` — 模块输出用户定义的值。使用 **Output value when connection times out** 参数来定义此自定义值。
- `Error` — 模块输出错误。

### **连接超时时的输出值** — 连接超时时输出自定义值 `0`（默认）| 标量

指定当发生连接超时时模块输出的自定义值。

#### 依赖关系

要启用此参数，请将 **连接超时时的操作** 设置为 `Output custom value` 或 `Error`。

### **采样时间** — 模块执行的采样时间 `-1`（默认）| 标量

确定 Host Serial Receive 模块的调用频率（以秒为单位）。当您将此值设置为 `-1` 时，模型将继承模型的采样时间。要将此模块作为异步执行，请将 **采样时间** 设置为 `-1`。

### **输出接收状态** — 启用状态输出端口 `off`（默认）| `on`

选择此参数以启用 **status** 输出端口，该端口提供事务的状态。如果清除此参数，模块将隐藏 **status** 端口。

### **启用阻塞模式** — 在接收数据时阻塞仿真 `on`（默认）| `off`

选择此参数以在接收数据时阻塞仿真。如果您不希望读取操作阻塞仿真，请清除此参数。

如果启用阻塞模式，模型在等待接收所请求的数据时会阻塞仿真。如果未启用阻塞模式，仿真将持续运行。

## 所属库

Motor Control Blockset / Protection and Diagnostics

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

配置主机端串行通信接口以从串行端口接收数据

Host Serial Receive 模块指定其从目标硬件接收的数据的配置。

模块接收的数据包限制为 16 字节的 ASCII 字符，包括包头和包尾。通过包含包头、包尾或两者以及数据大小来计算包的大小。此表显示了每种数据类型的字节数。

| 数据类型 | 字节数 |
| --- | --- |
| `single` | 4 字节 |
| `int8` 和 `uint8` | 1 字节 |
| `int16` 和 `uint16` | 2 字节 |
| `int32` 和 `uint32` | 4 字节 |

例如，如果您的数据包具有包头 'S'（1 字节）和包尾 'E'（1 字节），则剩余 14 字节用于实际数据。如果您的数据为 `int8` 类型，则数据包中有空间容纳 14 个 `int8`。如果您的数据为 `uint16` 类型，则数据包中有空间容纳 7 个 `uint16`。如果您的数据为 `int32` 类型，则数据包中仅有空间容纳 3 个 `int32`，剩余 2 字节。即使剩余空间可以容纳两个 `int8` 或一个 `uint16`，您也不应这样做，因为您不能在同一包中混合数据类型。

可容纳到数据包中的数据类型数量决定了数据大小。在前面的示例中，`int8` 的数据大小为 14，`uint16` 的数据大小为 7。当数据大小超过 16 字节时，可能会发生意外行为，包括运行时错误。
