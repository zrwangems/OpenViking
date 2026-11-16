---
type: simulink-block
title: 'CAN Transmit'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Communication'
documentation_page: 'cantransmit'
documentation_source_path: 'nvidia/ref/cantransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Transmit

## 端口

### 输入

### **Port1** — 消息数据向量 | 标量

消息数据，指定为向量或标量。

**数据类型：** `uint8` | `CAN Msg`
### 输出

### **Port1** — 状态向量 | 标量

输出状态。

#### 依赖关系

要启用此参数，请选择 **Output Status**

## 参数

### **CAN interface** — CAN 设备 ID can0（默认） | 有效的 CAN ID

要使用的 CAN 控制器的设备 ID。

### **Set up CAN interface** — 启动 CAN 接口 `off`（默认） | on

选择此参数以在发送 CAN 帧之前启动 NVIDIA 目标上的 CAN 接口。

### **CAN interface type** — CAN 接口类型 `Real`（默认） | `Virtual`

选择 CAN 接口类型。

- 如果 CAN 接口类型为 `Real`，将此参数设置为 `Real`。在这些情况下，将此参数设置为 `Real` 不会启动 CAN 接口。

  - 目标上的接口已启动，且其 CAN 总线速度与 **CAN Bus Speed (kBit/s)** 参数不匹配。该模块不会发送 CAN 帧。在启用此参数之前，请先关闭现有接口。
  - 如果目标上的接口已启动，且其 CAN 总线速度与 **CAN Bus Speed (kBit/s)** 参数匹配。该模块将发送 CAN 帧。
- 如果 CAN 接口类型为 `Virtual`，将此参数设置为 `Virtual`。

#### 依赖关系

要启用此参数，请选择 **Set up CAN interface**。

### **Data is input as** — 数据输入类型 `Raw data`（默认） | `CAN Msg`

用于发送消息的数据输入类型。

### **Output Status** — 指示输出状态 `off`（默认） | `on`

选择此选项以指示消息传输状态。状态端口在成功发送时输出 `0`，在失败时输出错误代码。错误代码列于下表中。

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | 00 | ABTF | MLOA | TXERR | TXBO | TXEP | TXWAR |
| bit7 | bit6 | bit5 | bit4 | bit3 | bit2 | bit1 | bit0 |

ABTF：消息中止标志位

MLOA：消息丢失仲裁位

TXERR：检测到传输错误位

TXBO：总线关闭错误标志位

TXEP：发送错误被动标志位

TXWAR：发送错误警告标志位

### **Wait until data sent** — 等待直到数据发送完成 `off`（默认） | `on`

选中后，该模块在传输数据前会等待 **Time out in seconds** 参数指定的时间。

### **Time out in seconds** — 发送数据的等待时间 1（默认） | integer

传输数据的等待时间。经过指定时间后，该模块超时。

#### 依赖关系

要启用此参数，请选择 **Wait until data sent**。

### **Identifier Type** — 消息标识符类型 `Standard (11-bit identifier)`（默认） | `Extended (29-bit identifier)`

消息标识符类型。

#### 依赖关系

要启用此参数，请将 **Data is input as** 设置为 `Raw data`。

### **Message ID** — 消息标识符 100（默认） | 长度为 11 或 29 位的数字标识符

消息标识符，对于标准帧大小为 11 位，对于扩展帧大小为 29 位，以十进制、二进制或十六进制指定。对于二进制和十六进制格式，分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 转换输入。消息标识符被编码到发送到 CAN 总线的消息中。

#### 依赖关系

要启用此参数，请将 **Data is input as** 设置为 `Raw data`。

### **Message Length** — 消息长度 8（默认） | positive integer

消息长度。

#### 依赖关系

要启用此参数，请将 **Data is input as** 设置为 `Raw data`。

### **Request Remote Frame** — 启用远程消息 `off`（默认） | `on`

选中后，该模块发送远程帧请求。

#### 依赖关系

要启用此参数，请将 **Data is input as** 设置为 `Raw data`。

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2021b 中引入**

## 描述

在控制器局域网 (CAN) 总线上发送消息

CAN Transmit 模块通过 NVIDIA® 嵌入式板上可用的时间触发 CAN (TTCAN) 控制器在 CAN 总线上发送消息。此模块使用 SocketCAN 接口与 NVIDIA 板上的 CAN 控制器硬件通信。

您还可以使用此模块与虚拟 CAN 接口交互。虚拟 CAN 接口允许在没有与真实硬件关联的原生 CAN 接口的情况下发送和接收 CAN 帧。有关如何设置虚拟 CAN 接口的详细信息，请参阅 Setup Virtual CAN Interface。

CAN Transmit 模块支持 `Raw data` 和 `CAN Msg` 作为输入类型。要使用 CANdb (CAN 数据库) 文件或手动指定信号，请使用 `CAN Msg` 输入类型和 CAN Pack 模块。CAN Pack 模块可从 Vehicle Network Toolbox™ 获取。
