---
type: simulink-block
title: 'CAN Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / STM32H7'
documentation_page: 'canwrite'
documentation_source_path: 'nucleo/ref/canwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# CAN Write

## 端口

### 输入

### **Tx** — 输入数据端口 向量 | 标量

该模块接受 `Raw data` 或 `CAN Msg` 格式的消息。

- `Raw data` – 要将消息作为 `uint8` 向量数组接受，请将 **Data is input as** 设置为 `Raw data`。
- `CAN Msg` – 要以 CAN 消息格式接受消息，请将 **Data is input as** 设置为 `CAN Msg`。您可以创建消息，也可以上传 CAN 数据库文件。

**数据类型：** `uint8` | `CAN Msg`
### 输出

### **Status** — 数据传输状态 标量

输出端口，用于显示数据传输状态。

- `1` - 数据传输成功
- `0` - 数据传输不成功

#### 依赖关系

仅当您选择 **Output Status** 参数时，此端口才会出现。

## 参数

### **Module** — 用于通信的模块 `0`（默认）| `Any integer value`

CAN 设备连接到的模块。

**注意**

- 模块上的 CAN 0 Module 表示硬件上的 CAN 1 外设。
- 模块上的 CAN 1 Module 表示硬件上的 CAN 2 外设。

### **Data Format** — 数据输出类型 `Raw data`（默认）| `CAN Msg`

选择要写入消息的类型。

- `Raw data` – 要将消息写为 1-by-*N* `uint8` 数组，请将 **Data Format** 选择为 `Raw data`。
- `CAN Msg` – 要以 CAN 消息格式写入消息，请将 **Data Format** 选择为 `CAN Msg`，然后执行以下步骤：

  1. 从 Vehicle Network Toolbox™ 向模型添加 CAN pack 模块。
  2. 将 CAN Read pack 模块的输出连接到 **CAN Write** 模块的输入
  3. 使用 CAN Pack 模块的 **Data to be input as** 列表中的选项，指定是要创建消息还是要上传 CAN 数据库文件。如果选择上传 CAN 数据库文件，则 CAN Pack 会从上传的文件继承消息属性。

  **注意**

  要使用 CAN Pack 模块，您必须拥有 Vehicle Network Toolbox 许可证。

### **Identifier Type** — 消息标识符类型 `Standard (11-bit identifier)`（默认）| `Extended (29-bit identifier)`

消息标识符的类型。

#### 依赖关系

仅当您将 **Data Format** 选择为 `Raw data` 时，此参数才会出现。

### **Identifier** — 消息标识符 100（默认）| 长度为 11 或 29 位的数字标识符

标识符，对于标准帧大小为 11 位，对于扩展帧大小为 29 位，可用十进制、二进制或十六进制指定。对于二进制和十六进制格式，请分别使用 `bin2dec(' ')` 和 `hex2dec(' ')` 转换输入项。该标识符会被编码到发送到 CAN 总线的消息中。

#### 依赖关系

仅当您将 **Data Format** 选择为 `Raw data` 时，此参数才会出现。要输出 `CAN Msg` 的标识符，请选择 CAN Unpack 模块的 **Output identifier**。

### **Length (bytes)** — 消息长度 8（默认）| 小于或等于 8 的正整数

消息的长度，以 bytes 为单位。

#### 依赖关系

仅当您将 **Data Format** 选择为 `Raw data` 时，此参数才会出现。要输出 `CAN Msg` 的长度，请选择 CAN Unpack 模块的 **Output length**。

### **Remote Frame** — 启用远程消息 `off`（默认）| `on`

如果选择此参数，模块会在 CAN 消息中发送远程帧。输入端口处的数据不会在 CAN 消息中发送。

#### 依赖关系

仅当您将 **Data Format** 选择为 `Raw data` 时，此参数才会出现。对于 CAN Msg，Remote Frame 继承自 CAN Pack 模块中指定的请求。

### **Output Status** — 启用输出状态 `off`（默认）| `on`

当您选择 **Output Status** 参数时，模块会配置一个输出端口 **Status**。该端口输出状态消息。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / STM32H7

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

将消息写入 CAN 网络

CAN Write 模块将消息写入连接到硬件的控制器局域网（CAN）网络。

单击模块上的 **View pin map** 以打开 Nucleo Pin Mapping 表。

使用模块参数对话框指定 **Data Format** 及其属性。在配置参数中配置 CAN 模块的属性。

**注意**

**CAN Write** 模块目前仅支持 STM32 Nucleo H743ZI2。
