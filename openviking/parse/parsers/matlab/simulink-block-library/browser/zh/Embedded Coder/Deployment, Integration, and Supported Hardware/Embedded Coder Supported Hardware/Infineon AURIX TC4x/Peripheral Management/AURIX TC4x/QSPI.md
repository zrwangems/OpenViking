---
type: simulink-block
title: 'QSPI'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'qspi'
documentation_source_path: 'infineonaurix/ref/qspi.html'
language: zh-CN
chinese_source: worker-translation
---

# QSPI

## 端口

### 输入

### **SDO** — 串行数据输出 `scalar` | `vector`

该端口输入要与外设通信的数据。
数据类型基于模块掩码配置。

#### 依赖关系

要启用此端口，请将 **Transfer mode** 参数设置为 `SPI Transmit and Receive` 或 `SPI Transmit`。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **SDImsg** — SoC Blockset 仿真消息 `scalar`

如果 **Transfer mode** 设置为 `SPI Transmit and Receive` 或 `SPI Receive`，则 QSPI 模块在仿真期间将 SoC Blockset™ 消息 **SDImsg** 转换为 **SDI** 输出端口处的输出数据。

#### 依赖关系

要启用此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **SoC Data (Message based)**。

### **SDIsig** — 基于 Simulink 的仿真信号 `scalar` | `vector`

如果 **Transfer mode** 设置为 `SPI Transmit and Receive` 或 `SPI Receive`，则在仿真期间，此输入端口作为直通端口，与 QSPI 模块的 **SDI** 输出对应。

#### 依赖关系

要启用此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **Signal**。
### 输出

### **SDI** — 串行数据输入 `scalar` | `vector`

该端口输出从外设接收的数据。输出数据类型基于模块掩码配置。

#### 依赖关系

要启用此端口，请将 **Transfer mode** 参数设置为 `SPI Transmit and Receive` 或 `SPI Receive`。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **status** — QSPI 的状态 `scalar`

该模块将接收到的数据状态，或数据发送和接收期间发生的错误，输出为 `unit16` 标量值

|  |  |
| --- | --- |
| **位** | **状态** |
| `Bit 0` | 事务成功 |
| `Bit 1` | 忙 |
| `Bit 2` | 奇偶校验错误 |
| `Bit 3` | 配置错误 |
| `Bit 4` | 波特率错误 |
| `Bit 5` | 发送缓冲区 (Tx FIFO) 溢出错误 |
| `Bit 6` | Tx FIFO 下溢错误 |
| `Bit 7` | 接收缓冲区 (Rx FIFO) 溢出错误 |
| `Bit 8` | Rx FIFO 下溢错误 |
| `Bit 9` | 超时错误 |

例如，状态 17（设置第 4 位和第 0 位）表示事务成功且存在波特率错误。

#### 依赖关系

要启用此端口，请选择 **Enable status port** 参数。

**数据类型：** `uint16`

### **SDOmsg** — SoC Blockset 仿真消息 `scalar`

如果 **Transfer mode** 设置为 `SPI Transmit and Receive` 或 `SPI Transmit`，则该端口在仿真期间以消息形式输出在 **SDO** 端口接收到的数据。

#### 依赖关系

要启用此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **SoC Data (Message based)**。

### **SDOsig** — 基于 Simulink 的仿真信号 `scalar` | `vector`

如果 **Transfer mode** 设置为 `SPI Transmit and Receive` 或 `SPI Transmit`，则该端口在仿真期间输出在 **SDO** 端口接收到的数据。

#### 依赖关系

要启用此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **Signal**。

## 参数

### 基本

### **Transfer mode** — 选择数据传输模式 `SPI Transmit and Receive` (默认) | `SPI Transmit` | `SPI Receive`

选择 QSPI 传输模式。

- `SPI Transmit and Receive` - 在此传输模式下，算法会等待数据接收完成后再继续处理/进一步处理。

  选择此传输模式时，模块会同时配置输出端口和输入端口，即 `SDO` 和 `SDI`。
- `SPI Transmit` - 在此传输模式下，可以在不等待接收的情况下发送数据。在启动数据传输之前，请确保状态为 `1`，即 QSPI Receive 模块未处于进行中状态。

  选择此传输模式时，模块会配置一个输入端口 `SDO`。

  **注意**

  QSPI Receive 模块负责处理来自外设的接收数据。换言之，必须同时使用 QSPI Transmit 模块和 QSPI Receive 模块才能完成数据传输。
- `SPI Receive` - 在此传输模式下，可以从外设接收数据。

  选择此传输模式时，模块会配置一个输出端口 `SDI`。

  **注意**

  应在接收数据之前使用 QSPI Transmit 模块发送数据。换言之，必须同时使用 QSPI Transmit 和 QSPI Receive 模块才能完成数据传输。

### **Data bits** — 选择数据位 `2` (默认) | `5` | `6` | `...`

**Data bits** 参数提供 QSPI 通信中每个数据元素的帧长度。如果所选数据位在以下范围内：

- `2 to 8` - 有效数据类型为 `int8` 或 `unit8`。
- `9 to 16` - 有效数据类型为 `int16` 或 `unit16`。
- `17 to 32` - 有效数据类型为 `int32` 或 `unit32`。

### **Enable status port** — 启用以配置输出状态端口 `off` (默认) | `on`

选择此参数以输出数据传输状态。

当选择 Output Status 参数时，模块会配置一个输出端口 Status。

### **Sample time** — 模块读取输入数据的频率 `-1` (默认) | `scalar` | `vector`

以秒为单位指定模块应读取输入数据的频率。

当将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定模块的最佳采样时间。

#### 依赖关系

要启用此参数，请将 **Transfer mode** 设置为 `SPI Receive`

### **Enable simulation port** — 启用模块中的外设仿真端口 `off` (默认) | `on`

选择此参数以启用外设仿真功能。

### **Port Type** — 指定外设仿真端口的类型 `SoC Data (Message based)` (默认) | `Signal`

选择此参数以配置 SoC 兼容的仿真端口或基于 Simulink 信号的仿真端口，从而启用外设仿真功能。

#### 依赖关系

要查看此参数，请选择 **Enable simulation port** 参数。

### 高级

### **Output data length** — 指定要接收的数据长度 `1` (默认) | `positive integer`

指定要从外设接收的数据长度。

**注意**

指定的数据长度必须与使用 QSPI Transmit 模块发送的数据匹配。

#### 依赖关系

要启用此参数，请将 **Transfer mode** 设置为 `SPI Receive`

### **Output data type** — 选择输出数据类型 `1` (默认) | `positive integer`

根据所选数据位选择支持的数据类型。

#### 依赖关系

要启用此参数，请将 **Transfer mode** 设置为 `SPI Receive` 或 `SPI Transmit and Receive`

## 所属库

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022b 中引入**

## 描述

向 SPI 外设写入数据以及从 SPI 外设读取数据

向 SPI 外设写入数据以及从 SPI 外设读取数据

队列同步外设接口 (QSPI) 模块接受数据类型为 `int8`、`uint8`、`int16`、`uint16`、`int32` 和 `uint32` 的一维数组。
该模块输出与输入值大小和数据类型相同的数组。
