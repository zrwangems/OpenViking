---
type: simulink-block
title: 'PX4 CAN Transmit'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'px4cantransmit'
documentation_source_path: 'px4/ref/px4cantransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# PX4 CAN Transmit

## 端口

### 输入

### **Port1** — 消息数据向量 | 标量

该模块接受 `Raw data` 和 `CAN Msg` 格式的消息。

- `Raw data` – 要将消息作为 `uint8` 向量数组接受，请将 **Data is input as** 设置为 `Raw data`。
- `CAN Msg` – 要以 CAN 消息格式接受消息，请将 **Data is input as** 设置为 `CAN Msg`。您可以创建消息或上传 CAN 数据库文件。有关详细信息，请参阅 Data is input as。

#### 依赖关系

仅当选择 **Remote Frame** 参数时，此端口才会出现。

**数据类型：** `uint8` | `CAN Msg`

### 输出

### **Port1** — 数据传输状态标量

用于显示数据传输状态的输出端口。

该端口输出以下值之一：

- `0`：CAN 传输成功。
- `1`：打开 CAN 失败。
- `2`：设置 Baud rate 失败。
- `3`：设置 CAN Test mode 失败。
- `4`：CAN 传输失败。

有关详细信息，请参阅 Output Status。

#### 依赖关系

仅当选择 **Output Status** 参数时，此端口才会出现。

## 参数

### **Data is input as** — 数据输入类型 `Raw data`（默认）| `CAN Msg`

选择输入端口处消息的类型。

- `Raw data` – 要将消息作为 `uint8` 向量数组接受，请将 **Data is input as** 设置为 `Raw data`。
- `CAN Msg` – 要以 CAN 消息格式接受消息，请将 **Data is input as** 设置为 `CAN Msg`，然后执行以下步骤：

  1. 从 Embedded Coder® / Vehicle Network Toolbox™ 向模型中添加一个 CAN Pack (Vehicle Network Toolbox) 模块。
  2. 将 CAN Pack 模块的输出连接到 CAN Transmit 模块的输入端口。
  3. 使用 CAN Pack 模块的 **Data is input as** 列表中的选项，指定是要创建消息还是要上传 CAN 数据库文件。如果选择上传 CAN 数据库文件，则 CAN Pack 会从上传的文件继承消息属性。

  **注意**

  要使用 CAN Pack 模块，您必须拥有 Embedded Coder / Vehicle Network Toolbox 许可证。

### **Identifier Type** — 消息标识符类型 `Standard (11-bit identifier)`（默认）| `Extended (29-bit identifier)`

消息标识符的类型。

#### 依赖关系

仅当将 **Data is input as** 选择为 `Raw data` 时，此参数才会出现。对于 `CAN Msg`，**Identifier Type** 继承自 CAN Pack 模块中指定的类型。

### **Message ID** — 消息标识符 100（默认）| 长度为 11 或 29 位的数字标识符

消息标识符，对于标准帧长度为 11 位，对于扩展帧长度为 29 位，可用十进制、二进制或十六进制指定。对于二进制和十六进制格式，分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 转换输入项。消息标识符会被编码到发送至 CAN 总线的消息中。

#### 依赖关系

仅当将 **Data is input as** 选择为 `Raw data` 时，此参数才会出现。对于 `CAN Msg`，**Message ID** 继承自 CAN Pack 模块中指定的标识符。

### **Data Field Length** — 消息长度 3（默认）| 正整数

消息的长度，以字节为单位。

#### 依赖关系

仅当将 **Data is input as** 选择为 `Raw data` 时，此参数才会出现。对于 `CAN Msg`，**Message Length** 继承自 CAN Pack 模块的长度。

### **Output Status** — 数据传输状态 `off`（默认）| `on`

当选择 **Output Status** 参数时，该模块会配置一个输出端口。该端口将数据传输状态输出为 `uint8` 整数。该整数中的每一位对应数据传输期间发生的错误类型。输出为 `0` 表示传输成功。

### **Remote Frame** — 启用远程消息 `off`（默认）| `on`

当选择 **Remote Frame** 参数时，消息的远程帧会设置为 1，表示该模块正在请求传输特定标识符。

#### 依赖关系

仅当将 **Data is input as** 选择为 `Raw data` 时，此参数才会出现。对于 `CAN Msg`，**Remote Frame** 继承自 CAN Pack 模块中指定的请求。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

向 CAN 网络传输消息

PX4 CAN Transmit 模块使用 PX4 Autopilot CAN 端口将消息传输到控制器局域网（CAN）网络。

使用模块参数对话框指定消息类型及其属性。

如果在未连接硬件的情况下仿真包含 PX4 CAN Transmit 模块的模型，该模块不会执行任何操作。有关详细信息，请参阅 Block Produces Zeros or Does Nothing in Simulation (Simulink)。

在 Connected I/O 仿真期间，此模块将数据写入硬件的
外设。

**注意**

为避免与 PX4 UAVCAN 冲突，在使用 PX4 CAN 模块之前，请禁用 UAVCAN。要禁用，请将 PX4 参数 `UAVCAN_ENABLE` 设置为 `0`。有关详细信息，请参阅 Finding/Updating Parameters。
