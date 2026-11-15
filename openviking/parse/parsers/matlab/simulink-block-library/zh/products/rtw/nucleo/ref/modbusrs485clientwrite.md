---
type: simulink-block
title: 'Modbus RS485 Client Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'modbusrs485clientwrite'
documentation_source_path: 'nucleo/ref/modbusrs485clientwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus RS485 Client Write

## 端口

### 输入

### **data** — 输入数据向量

该模块的输入是客户端要写入服务器寄存器的数据，形式为 *N*×1 向量，其中 *N* 表示服务器设备上的寄存器数量。

- 如果选择线圈或离散输入写操作，则客户端以具有 Boolean 数据类型的 1-bit 写操作将数据写入服务器寄存器。
- 如果选择保持寄存器或输入寄存器写操作，则客户端以具有 uint16 数据类型的 16-bit 写操作将数据写入服务器寄存器。

**数据类型：** `Boolean` | `uint16`
### 输出

### **status** — 写操作状态 `0` | `1`

该模块在客户端设备寄存器上输出客户端写操作的状态。

- `1`：表示对服务器寄存器的写操作不成功，或在超时时间内未收到来自服务器的响应。
- `0`：表示对服务器寄存器的写操作成功，并在超时时间内收到预期响应。

#### 依赖关系

要启用此端口，请选择 **输出状态** 参数。

**数据类型：** `uint8`

## 参数

### **服务器地址（广播时为 0）** — 唯一的 8-bit Modbus 服务器标识符 `1`（默认）| [`1`, `255`] 范围内的标量

输入唯一的 8-bit Modbus 服务器地址或标识符，以标识客户端要将数据写入的服务器。

### **功能** — 写操作类型 `Write Coil`（默认）| `Write Holding register` | `Write Multiple Coils` | `Write Multiple Holding registers`

选择要在服务器寄存器上执行的写操作类型。指定以下任一项：

- `Write Coil`：将数据写入 **线圈地址** 参数中指定的线圈寄存器地址
- `Write Holding register`：将数据写入 **保持寄存器地址** 参数中指定的保持寄存器地址
- `Write Multiple Coils`：根据 **线圈地址** 和 **线圈数量** 参数中指定的值，将数据写入多个线圈寄存器
- `Write Multiple Holding registers`：根据 **保持寄存器地址** 和 **保持寄存器数量** 参数中指定的值，将数据写入多个保持寄存器

### **线圈地址** — 线圈寄存器地址 `0`（默认）| 标量

- 要通知客户端将数据写入特定线圈寄存器，请在此参数中指定线圈寄存器地址。例如，要让客户端将数据写入地址为 `10` 的线圈寄存器，请输入 `10`。
- 要通知客户端将数据写入一组线圈寄存器，请指定该组中第一个线圈寄存器的地址。例如，要让客户端将数据写入地址范围为 `10` 到 `14` 的线圈寄存器，请输入 `10`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Write Coil`。

### **线圈数量** — 客户端要写入的线圈寄存器数量 `1`（默认）| 标量

输入希望客户端向其写入数据的线圈寄存器数量。例如，要让客户端将数据写入地址范围为 `10` 到 `14` 的线圈寄存器，请输入 `5`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Write Multiple Coils`。

### **保持寄存器地址** — 保持寄存器地址 `0`（默认）| 标量

- 要通知客户端将数据写入特定保持寄存器，请在此参数中指定保持寄存器地址。例如，要让客户端将数据写入地址为 `37` 的保持寄存器，请输入 `37`。
- 要通知客户端将数据写入一组保持寄存器，请指定该组中第一个保持寄存器的地址。例如，要让客户端将数据写入地址范围为 `37` 到 `44` 的保持寄存器，请输入 `37`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Write Holding register`。

### **保持寄存器数量** — 客户端要写入的保持寄存器数量 `1`（默认）| 标量

输入希望客户端写入数据的保持寄存器数量。例如，要让客户端将数据写入地址范围为 `37` 到 `44` 的保持寄存器，请输入 `8`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Write Multiple Holding registers`。

### **输出状态** — 启用输出状态 `off`（默认）| `on`

当选择 **输出状态** 参数时，模块会配置一个输出端口 **Status**。该端口输出状态消息。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A)

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

客户端设备通过 RS485 网络将数据写入服务器设备寄存器

在 Modbus RS485 Client Write 模块中，客户端设备将数据写入服务器设备的寄存器。

Simulink® Coder™ Support Package for STMicroelectronics® Nucleo Boards 和 Embedded Coder® Support Package for STMicroelectronics Discovery Boards 支持通过 RS485 网络的 Modbus® 通信协议。客户端和服务器必须连接在同一 RS485 网络上，才能成功进行 Modbus 通信。RS485 网络上的每个设备都由唯一的 8-bit 地址或标识符引用。

下表对 Modbus 客户端设备引用的服务器设备寄存器进行分类。

| 寄存器类型 | 寄存器大小 | 允许的客户端对寄存器操作 |
| --- | --- | --- |
| 线圈 | 1-bit | 读和写 |
| 离散输入 | 1-bit | 读 |
| 保持寄存器 | 16-bit | 读和写 |
| 输入寄存器 | 16-bit | 读 |

客户端可以对服务器设备的寄存器执行读操作或写操作（具体取决于寄存器类型）。
