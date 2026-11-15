---
type: simulink-block
title: 'Modbus TCP/IP Client Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'modbustcpipclientread'
documentation_source_path: 'supportpkg/raspberrypi_ref/modbustcpipclientread.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus TCP/IP Client Read

## 端口

### 输出

### **Data** — 输出数据向量

该模块将客户端从服务器设备寄存器读取的数据输出为 *N*×1 向量，其中 *N* 表示服务器设备上的寄存器数量。

- 如果选择 Coil 或 Discrete Input 读取操作，则客户端将服务器寄存器作为 1-bit 读取操作进行读取。该模块将读取的数据输出为 `Boolean` 数据。
- 如果选择 Holding Register 或 Input Register 读取操作，则客户端将服务器寄存器作为 16-bit 读取操作进行读取。该模块将读取的数据输出为 `uint16` 数据。

**数据类型：** `Boolean` | `uint16`

### **Status** — 读取操作的状态 `0` | `1`

该模块输出客户端在服务器设备寄存器上执行读取操作的状态。

- `0`：表示读取操作未成功，这意味着 **data** 端口上接收的数据无效。
- `1`：表示读取操作成功，这意味着 **data** 端口上接收的数据有效。

**数据类型：** `uint8`

## 参数

### **服务器地址** — 服务器设备的唯一 IP 地址 `127.0.0.1` (默认) | IP 地址

输入服务器设备的 IP 地址。客户端从该服务器设备读取数据。

### **功能** — 客户端读取操作的类型 `Read Coil` (默认) | `Read Discrete input` | `Read Holding register` | `Read Input register` | `Read Multiple Coils` | `Read Multiple Discrete inputs` | `Read Multiple Holding registers` | `Read Multiple Input registers`

选择您要在服务器寄存器上执行的读取操作类型。指定以下任一项：

- `Read Coil`：从 **线圈地址** 参数中指定的线圈寄存器地址读取数据。
- `Read Discrete input`：从 **离散输入地址** 参数中指定的离散输入寄存器地址读取数据。
- `Read Holding register`：从 **保持寄存器地址** 参数中指定的保持寄存器地址读取数据。
- `Read Input register`：从 **输入寄存器地址** 参数中指定的输入寄存器地址读取数据。
- `Read Multiple Coils`：根据 **线圈地址** 和 **线圈数量** 参数中指定的值，从多个线圈寄存器读取数据。
- `Read Multiple Discrete inputs`：根据 **离散输入地址** 和 **离散输入数量** 参数中指定的值，从多个离散输入寄存器读取数据。
- `Read Multiple Holding registers`：根据 **保持寄存器地址** 和 **保持寄存器数量** 参数中指定的值，从多个保持寄存器读取数据。
- `Read Multiple Input registers`：根据 **输入寄存器地址** 和 **输入寄存器数量** 参数中指定的值，从多个输入寄存器读取数据。

### **线圈地址** — 线圈寄存器的地址 `0` (默认) | scalar

要通知客户端从特定线圈寄存器读取数据，请在此参数中指定线圈寄存器地址。例如，要让客户端从地址为 `10` 的线圈寄存器读取数据，请输入 `10`。

要通知客户端从一组线圈寄存器读取数据，请指定该组中第一个线圈寄存器的地址。例如，要让客户端从地址范围为 `10` 到 `14` 的线圈寄存器读取数据，请输入 `10`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Read Coil`。

### **线圈数量** — 客户端要读取的线圈寄存器数量 `1` (默认) | scalar

输入您希望客户端从中读取数据的线圈寄存器数量。例如，要让客户端从地址范围为 `10` 到 `14` 的线圈寄存器读取数据，请输入 `5`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Read Multiple Coils`。

### **离散输入地址** — 离散输入寄存器的地址 `0` (默认) | scalar

要通知客户端从特定离散输入寄存器读取数据，请在此参数中指定离散输入寄存器地址。例如，要让客户端从地址为 `80` 的离散输入寄存器读取数据，请输入 `80`。

要通知客户端从一组离散输入寄存器读取数据，请指定该组中第一个离散输入寄存器的地址。例如，要让客户端从地址范围为 `80` 到 `89` 的离散输入寄存器读取数据，请输入 `80`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Read Discrete input`。

### **离散输入数量** — 客户端要读取的离散输入寄存器数量 `1` (默认) | scalar

输入您希望客户端从中读取数据的离散输入寄存器数量。例如，要让客户端从地址范围为 `80` 到 `89` 的离散输入寄存器读取数据，请输入 `10`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Read Multiple Discrete inputs`。

### **保持寄存器地址** — 保持寄存器的地址 `0` (默认) | scalar

要通知客户端从特定保持寄存器读取数据，请在此参数中指定保持寄存器地址。例如，要让客户端从地址为 `37` 的保持寄存器读取数据，请输入 `37`。

要通知客户端从一组保持寄存器读取数据，请指定该组中第一个保持寄存器的地址。例如，要让客户端从地址范围为 `37` 到 `44` 的保持寄存器读取数据，请输入 `37`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Read Holding register`。

### **保持寄存器数量** — 客户端要读取的保持寄存器数量 `1` (默认) | scalar

输入您希望客户端从中读取数据的保持寄存器数量。例如，要让客户端从地址范围为 `37` 到 `44` 的保持寄存器读取数据，请输入 `8`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Read Multiple Holding registers`。

### **输入寄存器地址** — 输入寄存器的地址 `0` (默认) | scalar

- 要通知客户端从特定输入寄存器读取数据，请在此参数中指定输入寄存器地址。例如，要让客户端从地址为 `25` 的输入寄存器读取数据，请输入 `25`。
- 要通知客户端从一组输入寄存器读取数据，请指定该组中第一个输入寄存器的地址。例如，要让客户端从地址范围为 `25` 到 `26` 的输入寄存器读取数据，请输入 `25`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Read Input register`。

### **输入寄存器数量** — 客户端要读取的输入寄存器数量 `1` (默认) | scalar

输入您希望客户端从中读取数据的输入寄存器数量。例如，要让客户端从地址范围为 `25` 到 `26` 的输入寄存器读取数据，请输入 `2`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Read Multiple Input registers`。

### **采样时间** — 客户端读取数据的时间间隔 `0.1` (默认) | scalar

输入客户端从服务器设备寄存器读取数据的时间间隔（以 seconds 为单位）。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Network

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

客户端设备通过 TCP/IP 网络从服务器设备寄存器读取数据

在 Modbus TCP/IP Client Read 模块中，客户端设备从服务器设备的寄存器读取数据。

Simulink® Support Package for Raspberry Pi® Hardware 支持通过 TCP/IP 网络的 Modbus® 通信协议。客户端和服务器必须连接到 TCP/IP 网络，才能成功进行 Modbus 通信。

客户端可以对服务器寄存器执行读取、写入或读取和写入操作，具体取决于服务器寄存器类型。

| 寄存器类型 | 寄存器大小 | 客户端执行的操作 |
| --- | --- | --- |
| 线圈 | 1-bit | 读取和写入 |
| 离散输入 | 1-bit | 读取 |
| 保持寄存器 | 16-bit | 读取和写入 |
| 输入寄存器 | 16-bit | 读取 |

**注意**

要为该模块生成 C/C++ 代码，您必须拥有 Embedded Coder® 许可证。
