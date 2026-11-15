---
type: simulink-block
title: 'CAN Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / STM32H7'
documentation_page: 'canread'
documentation_source_path: 'nucleo/ref/canread.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Read

## 端口

### 输出

### **Data** — 消息数据向量 | 标量

该模块以 `uint8` 或 `CAN Msg` 格式输出消息。

- `uint8` – 若要将消息输出为 `uint8` 向量数组，请将 **Data Format** 选择为 `Raw data`。
- `CAN Msg` – 若要以 CAN 消息格式输出消息，请将 **Data Format** 选择为 `CAN Msg`。

如果接收到的 CAN 消息是远程帧，则此端口输出 `0`。

**数据类型：** `uint8` | `CAN Msg`

### **Status** — 接收到的消息的状态 标量

该端口输出消息读取状态。

- 如果模块读取到新消息，则状态为 `1`。
- 如果模块未读取到新消息，则状态为 `0`。

#### 依赖关系

仅当您选择 **Output Status** 参数时，此端口才会出现。

**数据类型：** `uint8`

### **Remote** — 启用远程消息 标量

如果接收到的 CAN 消息是远程帧，则该端口输出 1。

#### 依赖关系

仅当您选择 **Output Remote** 参数时，此端口才会出现。

## 参数

### **Module** — 用于通信的模块 `0`（默认） | 任意整数值

CAN 设备连接到的模块。

**注意**

- 模块上的 CAN 0 Module 表示硬件上的 CAN 1 外设。
- 模块上的 CAN 1 Module 表示硬件上的 CAN 2 外设。

### **Data Format** — 数据输出类型 `Raw data`（默认） | `CAN Msg`

选择一种读取消息的类型。

- `Raw data` – 若要将消息读取为 1 乘 *N* 的 `uint8` 数组，请将 **Data Format** 选择为 `Raw data`。
- `CAN Msg` – 若要以 CAN 消息格式读取消息，请将 **Data Format** 选择为 `CAN Msg`，然后执行以下步骤：

  1. 将 Vehicle Network Toolbox™ 中的 CAN Unpack 模块添加到您的模型。
  2. 将 CAN Read 模块的输出连接到 CAN Unpack 模块的输入。
  3. 使用 CAN Unpack 模块的 **Data to be output as** 列表中的选项，指定您是要创建消息还是要上传 CAN 数据库文件。如果您选择上传 CAN 数据库文件，CAN Unpack 会继承所上传文件中的消息属性。

  **注意**

  要使用 CAN Unpack 模块，您必须具有 Vehicle Network Toolbox 许可证。

### **Identifier Type** — 消息标识符类型 `Standard (11-bit identifier)`（默认） | `Extended (29-bit identifier)`

消息标识符的类型。

#### 依赖关系

仅当您将 **Data Format** 选择为 `Raw data` 时，此参数才会出现。

### **Identifier** — 消息标识符 100（默认） | 长度为 11 或 29 位的数字标识符

标识符，对于标准帧大小为 11 位，对于扩展帧大小为 29 位，可用十进制、二进制或十六进制指定。对于二进制和十六进制格式，请分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 来转换条目。标识符会被编码到发送至 CAN 总线的消息中。

#### 依赖关系

仅当您将 **Data Format** 选择为 `Raw data` 时，此参数才会出现。要输出 `CAN Msg` 的标识符，请选择 CAN Unpack 模块的 **Output identifier**。

### **Length (bytes)** — 消息长度 8（默认） | 小于或等于 8 的正整数

消息的长度，以字节为单位。

#### 依赖关系

仅当您将 **Data Format** 选择为 `Raw data` 时，此参数才会出现。要输出 `CAN Msg` 的长度，请选择 CAN Unpack 模块的 **Output length**。

### **Sample Time** — 读取消息的时间间隔 -1（默认） | 0.1 | 非负实数值

指定模块接收消息的频率，以秒为单位。当您将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

### **Output Remote** — 启用远程消息 `off`（默认） | `on`

当您选择 **Output Remote** 参数时，该模块会配置一个输出端口 **Remote**。该端口输出消息远程帧状态。

#### 依赖关系

仅当您将 **Data Format** 选择为 `Raw data` 时，此参数才会出现。

### **Output Status** — 启用输出状态 `off`（默认） | `on`

当您选择 **Output Status** 参数时，该模块会配置一个输出端口 **Status**。该端口输出状态消息。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

从 CAN 网络读取消息

CAN Read 模块从连接到硬件的控制器局域网 (CAN) 网络读取消息。

点击 **View pin map** 以打开 Nucleo Pin Mapping 表。

使用模块参数对话框指定 **Data Format** 及其属性。在 Configuration Parameters 中配置 CAN 模块的属性。

**注意**

- **CAN Read** 模块目前仅支持 STM32 Nucleo H743ZI2。
- CAN Read 模块的每个实例都会配置一个 CAN 过滤器，以接受具有指定标识符的消息。
- 已配置的过滤器接受 CAN 消息并将其保存在单元素缓冲区中，在接受新消息之前需要先读取该消息。
