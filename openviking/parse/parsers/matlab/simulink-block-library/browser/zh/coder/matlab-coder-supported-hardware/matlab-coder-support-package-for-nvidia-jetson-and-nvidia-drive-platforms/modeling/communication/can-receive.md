---
type: simulink-block
title: 'CAN Receive'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Communication'
documentation_page: 'canreceive'
documentation_source_path: 'nvidia/ref/canreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Receive

## 端口

### 输出

### **Data** — 消息数据端口 向量 | 标量

接收到的消息数据，以向量或标量形式返回。

如果 **Data to be output as** 设置为 `Raw data`，则接收到的消息数据是类型为 `uint8` 的 1-by-N 数组。

如果 **Data to be output as** 设置为 `CAN Msg`，则数据端口重命名为 **CAN Msg**，并且接收到的消息数据输出为 Simulink® 总线信号。要从 Simulink 总线信号中提取数据，请使用 Vehicle Network Toolbox 中的 CAN Unpack 模块。

**数据类型：** `uint8` | `CAN Msg`

### **Status** — 输出消息的状态 标量

接收到的输出消息的状态。

**数据类型：** `uint8`

### **Error** — 错误代码 标量

错误代码。

#### 依赖关系

要启用此参数，请选择 **Output Error**。

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | 00 | 00 | 00 | RXWAR | RXEP | RX0OVR | RX1OVR |
| bit7 | bit6 | bit5 | bit4 | bit3 | bit2 | bit1 | bit0 |

RX1OVR：接收缓冲区 1 溢出标志位

RX0OVR：接收缓冲区 0 溢出标志位

RXEP：接收错误被动标志位

RXWAR：接收错误警告标志位

### **Remote** — 远程消息标志 标量

远程消息标志。

#### 依赖关系

要启用此参数，请选择 **Output Remote**。

## 参数

### **CAN interface** — CAN 接口名称 can0（默认）| 有效设备名称

指定要使用的真实或虚拟 CAN 接口的名称。

### **Set up CAN interface** — 启用 CAN 接口 `off`（默认）| on

选择此参数以在接收 CAN 帧之前，在 NVIDIA 目标上启用 CAN 接口。

### **CAN interface type** — CAN 接口类型 `Real`（默认）| `Virtual`

选择 CAN 接口类型。

- 如果 CAN 接口类型为 `Real`，将此参数设置为 `Real`。在这些情况下，将此参数设置为 `Real` 不会启用 CAN 接口。

  - 接口已在目标上启用，但其 CAN-Bus Speed 与 **CAN Bus Speed (kBit/s)** 参数不匹配。模块将不会传输 CAN 帧。在启用此参数之前，请先禁用现有接口。
  - 如果接口已在目标上启用，且其 CAN-Bus Speed 与 **CAN Bus Speed (kBit/s)** 参数匹配。模块将传输 CAN 帧。
- 如果 CAN 接口类型为 `Virtual`，将此参数设置为 `Virtual`。

#### 依赖关系

要启用此参数，请选择 **Set up CAN interface**。

### **Data to be output as** — 数据输出类型 `Raw data`（默认）| `CAN Msg`

用于接收消息的数据类型。

### **Identifier Type** — 消息标识符类型 `Standard (11-bit identifier)`（默认）| `Extended (29-bit identifier)`

消息标识符类型。

#### 依赖关系

要启用此参数，请将 **Data to be output as** 设置为 `Raw data`。

### **Message ID** — 消息标识符 100（默认）| 长度为 11 bits 或 29 bits 的数字标识符

消息标识符，对于标准帧大小为 11 bits，对于扩展帧大小为 29 bits，以十进制、二进制或十六进制指定。对于二进制和十六进制格式，请分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 转换输入。消息标识符会被编码到发送到 CAN 总线的消息中。

#### 依赖关系

要启用此参数，请将 **Data to be output as** 设置为 `Raw data`。

### **Message Length** — 消息长度 8（默认）| 正整数

消息长度。

#### 依赖关系

要启用此参数，请将 **Data to be output as** 设置为 `Raw data`。

### **Sample time (seconds)** — 模块接收数据的时间频率 `0.1`（默认）| `scalar`

指定模块读取端口缓冲区的频率。输入大于 `0` 的值，或输入 `-1`（用于继承采样时间）。

当您将此参数指定为 -1 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

此值默认为采样时间 `0.1` seconds。较小的值要求处理器在更短时间内完成相同数量的指令，这可能会导致任务超限。

### **Output Error** — 输出错误代码 `off`（默认）| on

如果消息传输失败，选择此项以输出错误代码。

### **Output Remote** — 启用远程消息 `off`（默认）| on

选择此项以输出远程消息。

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2021b 中引入**

## 描述

从控制器局域网 (CAN) 总线接收消息

CAN Receive 模块通过 NVIDIA® 嵌入式板卡上可用的时间触发 CAN (TTCAN) 控制器从 CAN 总线接收消息。此模块使用 SocketCAN 接口与 NVIDIA 板卡上的 CAN 控制器硬件通信。

您也可以使用此模块与虚拟 CAN 接口交互。虚拟 CAN 接口允许在没有与真实硬件关联的原生 CAN 接口的情况下传输和接收 CAN 帧。有关如何设置虚拟 CAN 接口的更多信息，请参阅 Setup Virtual CAN Interface。

CAN Receive 模块支持 `Raw data` 和 `CAN Msg` 作为输出类型。要使用 CANdb（CAN 数据库）文件或手动指定信号，请使用 `CAN Msg` 输出类型和 CAN Unpack 模块。CAN Unpack 模块可从 Vehicle Network Toolbox™ 获取。
