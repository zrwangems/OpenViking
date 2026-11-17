---
type: simulink-block
title: 'C28x SCI Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'c28xscitransmit'
documentation_source_path: 'ref/c28xscitransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# C28x SCI Transmit

## 端口
```yaml
ports:
- name: Data
  summary: 写入串行总线的数据 标量 | 向量
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single
- name: Status
  summary: 在给定时间步传输的数据 标量
  direction: output
  data_types: uint8 | uint16
```

### 输入

### **Data** — 写入串行总线的数据 标量 | 向量

写入串行通信总线的输入数据。

如果 SCI Transmit 的输入端口具有可变数据大小，并且可变数据的长度为 `0`，则该模块将仅发送包头和包尾。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single`
### 输出

### **Status** — 在给定时间步传输的数据 标量

如果在给定时间步传输了数据，则该端口输出 `0`。否则，它输出值 `1`，表示发送 FIFO 已满且数据传输不成功。

#### 依赖关系

要启用此端口，请选择 **Output status** 参数。

**数据类型：** `uint8` | `uint16`
## 参数
```yaml
parameters:
- name: SCI module
  summary: 用于通信的 SCI 模块 A（默认）| B | C | D
  group: ''
- name: Additional package header
  summary: 指示数据起始 'S'（默认）| 字符串 | 字符 | 0 到 255 之间的数字
  group: ''
- name: Additional package terminator
  summary: 指示数据结束 'E'（默认）| 字符串 | 字符 | 0 到 255 之间的数字
  group: ''
- name: Frame size
  summary: 指定要接收的数据长度 600（默认）| 任意正整数
  group: ''
- name: Wait until previous data transmitted
  summary: 等待上一步接收的数据发送完成 on（默认）| off
  group: ''
- name: Output status
  summary: 用于在数据传输期间显示发送状态的选项 off（默认）| on
  group: ''
```

### **SCI module** — 用于通信的 SCI 模块 `A`（默认）| `B` | `C` | `D`

用于通信的 SCI 模块。

### **Additional package header** — 指示数据起始 `'S'`（默认）| 字符串 | 字符 | 0 到 255 之间的数字

位于发送数据包开头的数据，它不属于正在传输的数据，用于指示数据的起始。附加包头必须使用 ASCII 字符表示。使用字符串或数字（0–255）。必须在此参数输入的字符串两侧添加单引号，但引号不会被发送，也不计入总字节数。要指定空值（无包头），仅输入两个单引号。

包头的数据类型与模块上提到的数据类型无关。

**注意**

附加包头或包尾应与主机 SCI Receive 模块中指定的内容匹配。

### **Additional package terminator** — 指示数据结束 `'E'`（默认）| 字符串 | 字符 | 0 到 255 之间的数字

位于发送数据包末尾的数据，它不属于正在传输的数据，用于指示数据的结束。附加包尾必须使用 ASCII 字符表示。使用字符串或数字（0–255）。必须在此字段输入的字符串两侧添加单引号，但引号不会被发送，也不计入总字节数。要指定空值（无包尾），仅输入两个单引号。

包尾的数据类型与模块上提到的数据类型无关。

### **Frame size** — 指定要接收的数据长度 `600`（默认）| 任意正整数

指定要传输的数据字节数。当发送速率高于接收速率时，可以使用此参数。

帧大小通过以下公式计算：接收速率/发送速率。例如，如果信号以 `50` 微秒传输，帧大小为 `600`，则可以以 `0.03` 秒接收数据。

当帧大小大于 `1` 时，附加包头和包尾会添加在帧的开头和结尾。例如，`<Header>DATA(1:frame size)<Terminator>`

其中，`DATA(1:frame size)` 表示要传输的信号，其长度为帧大小。

### **Wait until previous data transmitted** — 等待上一步接收的数据发送完成 `on`（默认）| `off`

- `on` — 选择此参数时，发送操作以阻塞模式运行。在此模式下，如果发送 FIFO 已满，则会等待先前数据发送完成，并验证 FIFO 中是否有空间来发送当前数据。

  如果在计划开始下一次发送操作时，目标硬件仍在等待所请求的数据发送完成，则会发生任务超限。要修复超限，请使用 **Sample time** 参数增大时间步。
- `off` — 清除此参数时，发送操作以非阻塞模式运行。在此模式下，如果模块仍在发送上一步接收的数据，则当前时间步输入端口的数据将被丢弃。

  在任一模式下，如果模块尚未建立发送主机与接收主机之间的连接，或者连接丢失，则输入端口的数据将被丢弃。

### **Output status** — 用于在数据传输期间显示发送状态的选项 `off`（默认）| `on`

选择此选项可在数据传输期间显示发送状态。

选择 Output status 参数时，模块会配置一个输出端口。模块上的该端口标记为 Status，表示模块在输出端口输出发送操作的状态。
## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

通过串行通信接口 (SCI) 将目标机的数据传输到主机

SCI Transmit 模块使用指定的 SCI 硬件模块传输标量或向量数据。采样率和数据类型继承自输入端口。

一个模型中每个模块只能包含一个 SCI Transmit 模块。C28x 处理器有四个 SCI 模块 — A、B、C 和 D。可用的 SCI 模块数量因所选处理器而异。您可以通过导航到 **Hardware Implementation** > **Target hardware resources** 来配置 SCI 模块。验证这些设置是否满足您的应用需求。验证这些设置是否满足您的应用需求。

**注意**

- 此模块不支持定点输入，但您可以使用 Data Type Conversion 模块将定点格式转换为原生数据类型。在 Data Type Conversion 模块中，将 **Input and output to have equal** 参数设置为 `Stored Integer (SI)`。
- 使用类似 SCI 模块模块的串行外部模式会导致冲突检查错误。

该模块以阻塞模式或非阻塞模式输出数据。在阻塞模式下，当发送 FIFO 已满时，模型会阻塞执行以进行等待。在非阻塞模式下，模型连续运行。要将模块设置为阻塞模式，请选择 **Wait until previous data transmitted** 选项。

**注意**

在非阻塞模式下尝试发送大于 FIFO 长度的数据时，可能会遇到数据丢失。
