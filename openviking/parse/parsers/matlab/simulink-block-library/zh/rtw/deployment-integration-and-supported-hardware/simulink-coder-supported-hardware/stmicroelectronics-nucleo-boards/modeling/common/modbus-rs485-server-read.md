---
type: simulink-block
title: 'Modbus RS485 Server Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'modbusrs485serverread'
documentation_source_path: 'nucleo/ref/modbusrs485serverread.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus RS485 Server Read

## 端口

### 输出

### **data** — 输出数据标量

该模块将服务器设备从其寄存器读取的数据输出为 1-bit 标量。

- 如果选择线圈或离散输入读取操作，服务器将其寄存器作为 1-bit 读取操作进行读取。该模块将读取的数据输出为 Boolean 数据类型。
- 如果选择保持寄存器或输入寄存器读取操作，服务器将其寄存器作为 16-bit 读取操作进行读取。该模块将读取的数据输出为 uint16 数据类型。

**数据类型：** `Boolean` | `uint16`

### **status** — 读取操作的状态 `0` | `1`

该模块输出服务器寄存器上服务器读取操作的状态。

- `1`：表示读取操作不成功，这意味着 **data** 端口上接收到的数据无效。
- `0`：表示读取操作成功，这意味着 **data** 端口上接收到的数据有效。

**数据类型：** `uint8`

## 参数

### **Function** — 读取操作的类型 `Read Coil`（默认） | `Read Discrete input` | `Read Holding register` | `Read Input register`

选择要在服务器寄存器上执行的读取操作类型。指定以下任意一项：

- `Read Coil`：从 **Coil Address** 参数中指定的线圈寄存器地址读取数据
- `Read Discrete input`：从 **Discrete Input Address** 参数中指定的离散输入寄存器地址读取数据
- `Read Holding register`：从 **Holding Register Address** 参数中指定的保持寄存器地址读取数据
- `Read Input register`：从 **Input Register Address** 参数中指定的输入寄存器地址读取数据

### **Coil Address** — 线圈寄存器的地址 `0`（默认） | 标量

要通知服务器从特定线圈寄存器读取数据，请在此参数中指定线圈寄存器地址。例如，要让服务器从地址为 `10` 的线圈寄存器读取数据，请输入 `10`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Coil`。

### **Discrete Input Address** — 离散输入寄存器的地址 `0`（默认） | 标量

要通知服务器从特定离散输入寄存器读取数据，请在此参数中指定离散输入寄存器地址。例如，要让服务器从地址为 `80` 的离散输入寄存器读取数据，请输入 `80`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Discrete input`。

### **Holding Register Address** — 保持寄存器的地址 `0`（默认） | 标量

要通知服务器从特定保持寄存器读取数据，请在此参数中指定保持寄存器地址。例如，要让服务器从地址为 `37` 的保持寄存器读取数据，请输入 `37`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Holding register`。

### **Input Register Address** — 输入寄存器的地址 `0`（默认） | 标量

要通知服务器从特定输入寄存器读取数据，请在此参数中指定输入寄存器地址。例如，要让服务器从地址为 `25` 的输入寄存器读取数据，请输入 `25`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Input register`。

### **Sample Time** — 服务器读取数据的时间间隔 `0.1`（默认） | 标量

输入服务器从其寄存器读取数据的时间间隔（单位：seconds）。

## 所属库

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A)

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

服务器设备通过 RS485 网络从服务器设备寄存器读取数据

在 Modbus RS485 Server Read 模块中，服务器设备从其寄存器读取数据。每次读取操作中，服务器只能从一个寄存器读取数据。

Simulink® Coder™ Support Package for STMicroelectronics® Nucleo Boards 和 Embedded Coder® Support Package for STMicroelectronics Discovery Boards 支持 RS485 网络上的 Modbus® 通信协议。RS485 网络上的每个设备都由唯一的 8-bit 地址或标识符引用。

此表对 Modbus 服务器设备引用的服务器寄存器进行了分类。

| 寄存器类型 | 寄存器大小 |
| --- | --- |
| 线圈 | 1-bit |
| 离散输入 | 1-bit |
| 保持寄存器 | 16-bit |
| 输入寄存器 | 16-bit |

服务器可以对其寄存器执行读取或写入操作。
