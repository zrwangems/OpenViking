---
type: simulink-block
title: 'PX4 CAN Receive'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4canreceive'
documentation_source_path: 'px4/ref/px4canreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# PX4 CAN Receive

## 端口

### 输出

### **Data** — 消息数据向量 | bus

该模块以 `uint8` 和 `CAN Msg` 格式输出消息。

- `uint8` – 要将消息输出为 `uint8` 向量数组，请将 **Data is output as** 选择为 `Raw data`。
- `CAN Msg` – 要以 CAN 消息格式输出消息，请将 **Data is input as** 选择为 `CAN Msg`。有关详细信息，请参阅 Data is input as。

**数据类型：** `uint8` | `CAN Msg`

### **Length** — 消息长度（标量）

消息的长度，单位为 bytes。

**数据类型：** `uint8` | `CAN Msg`

### **Status** — 已接收消息的状态（标量）

该端口输出消息接收状态。

该端口输出以下值之一：

- `0` 表示 CAN 接收成功。
- `1` 表示打开 CAN 失败。
- `2` 表示设置波特率失败。
- `3` 表示设置 CAN 测试模式失败。
- `4` 表示 CAN 接收失败。

#### 依赖关系

仅当您选择 **Output Status** 参数时，此端口才会出现。

**数据类型：** `uint8`

### **Remote** — 启用远程消息（标量）

该端口发送远程帧请求。

#### 依赖关系

仅当您选择 **Output Remote** 参数时，此端口才会出现。

## 参数

### **Data is input as** — 数据输入类型 `Raw data`（默认） | `CAN Msg`

选择接收消息的类型。

- `Raw data` – 要以 1-by-*N* `uint8` 数组接收消息，请将 **Data is input as** 选择为 `Raw data`。
- `CAN Msg` – 要以 CAN 消息格式接收消息，请将 **Data is input as** 选择为 `CAN Msg`，然后执行以下步骤：

  1. 将 Embedded Coder® / Vehicle Network Toolbox™ 中的 CAN Unpack 模块添加到您的模型。
  2. 将 CAN Receive 模块的输出连接到 CAN Unpack 模块的输入。
  3. 使用 CAN Unpack 模块的 **Data is input as** 列表中的选项，指定您是要创建消息还是上传 CAN 数据库文件。如果选择上传 CAN 数据库文件，则 CAN Unpack 会从上传的文件继承消息属性。

  **注意**

  要使用 CAN Unpack 模块，您必须具有 Embedded Coder / Vehicle Network Toolbox 许可证。

### **Message ID** — 消息标识符 100（默认） | 长度为 11 或 29 bits 的数值标识符

消息标识符，对于标准帧长度为 11 bits，对于扩展帧长度为 29 bits，可用十进制、二进制或十六进制指定。对于二进制和十六进制格式，请分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 转换输入项。消息标识符会被编码到发送到 CAN 总线的消息中。

#### 依赖关系

仅当您将 **Data is input as** 选择为 `Raw data` 时，此参数才会出现。要输出 `CAN Msg` 的标识符，请选择 CAN Unpack 模块的 **Output identifier**。

### **Identifier Type** — 消息标识符类型 `Standard (11-bit identifier)`（默认） | `Extended (29-bit identifier)`

消息标识符的类型。

#### 依赖关系

仅当您将 **Data is input as** 选择为 `Raw data` 时，此参数才会出现。

### **Sample Time** — 读取消息的时间间隔 0.1（默认） | -1 | 非负实数值

指定模块接收消息的频率，以 seconds 为单位。当您将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

### **Output Status** — 启用远程消息 `off`（默认） | `on`

当您选择 **Output Status** 参数时，该模块会配置一个输出端口 **Status**。该端口输出消息的远程帧状态。

### **Output Remote Flag** — 启用远程消息 `off`（默认） | `on`

当您选择 **Output Remote Flag** 参数时，该模块会配置一个输出端口 **Remote**。该端口输出消息的远程帧状态。

#### 依赖关系

仅当您将 **Data is input as** 选择为 `Raw data` 时，此参数才会出现。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022b 中引入**

## 描述

从 CAN 网络接收消息

PX4 CAN Receive 模块通过使用连接到硬件的 PX4 Autopilot CAN 端口，从控制器局域网 (CAN) 网络接收消息。

使用模块参数对话框指定消息类型及其属性。

如果在未连接硬件的情况下仿真包含 PX4 CAN Receive 模块的模型，该模块会输出零。有关详细信息，请参阅 Block Produces Zeros or Does Nothing in Simulation (Simulink)。

此外，如果 CAN 总线上没有消息，该模块会输出零。

在 Connected I/O 仿真期间，此模块从硬件的外设读取数据。

**注意**

为避免与 PX4 UAVCAN 冲突，在使用 PX4 CAN 模块之前，请禁用 UAVCAN。要禁用，请将 PX4 参数 `UAVCAN_ENABLE` 设置为 `0`。有关详细信息，请参阅 Finding/Updating Parameters。
