---
type: simulink-block
title: 'Serial Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Serial'
documentation_page: 'serialreceive'
documentation_source_path: 'supportpkg/arduino_ref/serialreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Receive

## 端口

### 输出

### **Data** — 输出数据 [`Nx1`] 数组

该模块输出其从 Arduino 串口接收到的数据。当 Arduino 串口上没有可用数据时，该模块输出零。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Status** — 输入数据长度的状态 `0` | `1`

该模块输出 Arduino 串口接收到的输入数据长度的状态。

- `0` — 表示 Arduino 串口上接收到的输入数据长度小于或等于 **Data length** 参数中指定的数据长度。
- `1` — 表示 Arduino 串口上接收到的输入数据长度大于 **Data length** 参数中指定的数据长度。

#### 依赖关系

要启用此参数，请将 **Data length option** 设置为 `Length via dialog` 或 `Length via input port`。

**数据类型：** `uint8`

### **Length** — 读取操作的状态标量

该模块输出 Arduino 串口接收到的数据长度。

#### 依赖关系

要启用此参数，请将 **Data length option** 设置为 `Variable length`。

**数据类型：** `uint8`

## 参数

### **Port number** — 用于串行通信的 Arduino 端口号 `0`（默认）| 正整数

指定已连接 Arduino 板的串口号。有关该模块的固定端口和已分配引脚的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

您可以将一个 Serial Transmit 模块和一个 Serial Receive 模块分配到同一个串口。不要将多个 Serial Receive 模块分配到同一个 Arduino 串口。不要将串口所使用的 Arduino 引脚编号分配给同一 Simulink 模型中的其他模块。

`XCP over Serial` 通信接口在 monitor and tune 模式下使用串口 0，因此，您无法在 Serial Transmit 模块中使用此端口。您可以选择任何其他通信接口，或使用 build and deploy 模式来使用串口 0。

### **Data type** — 输出数据的类型 `uint8`（默认）| `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

选择输出数据的数据类型。

### 数据帧

### **Data length option** — 数据长度 `Length via dialog`（默认）| `Length via input port` | `Variable length`

选择一个选项来指定数据长度。

- `Length via dialog` — 该模块从 **Data length** 参数中指定的输入获取数据长度。
- `Length via input port` — 该模块从其输入端口获取数据长度。
- `Variable length` — 该模块接收数据，直到您在 **Terminator** 参数中指定的值与 Arduino 串口上的数据匹配。当 Arduino 串口上没有可用数据时，该模块会等待直到超时值。该模块还会在 **Length** 输出端口上输出 Arduino 硬件接收到的数据长度。

### **Data length** — 数据长度（以字节为单位） `1`（默认）| 正整数

指定对于您在 **Data type** 参数中设置的数据类型，该模块必须在 Arduino 串口上接收的数据字节数。

#### 依赖关系

要启用此参数，请将 **Data length option** 设置为 `Length via dialog`。

### **Maximum data length** — 数据最大长度（以字节为单位） `10`（默认）| 正整数

指定该模块应根据输入端口中指定的 Serial Receive (Instrument Control Toolbox)length 在 Arduino 串口上应接收的最大数据字节数。

#### 依赖关系

要启用此参数，请将 **Data length option** 设置为 `Length via input port`。

### **Header** — 数据的头部数值数组 | 从 0 到 255（含）的整数

指定一个头部，用于指示数据块的开始。

此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示。此参数的确切形式取决于 ASCII 字符的类型。

| ASCII 字符类型 | 示例 ASCII 字符 | MATLAB® 命令 | 参数值 |
| --- | --- | --- | --- |
| 特殊字符 | `"#"` | `uint8('#')` | `[35]` |
| 数字 | `"81"` | `uint8('81')` | `[56 49]` |
| 字母 | `"Start"` | `uint8('Start')` | `[83 116 97 114 116]` |

您也可以使用 ASCII 字符的十六进制表示来指定此参数。

### **Terminator** — 数据字符数组的终止符（默认）

指定一个终止符，用于指示数据块的结束。

此参数中指定的数值数组是对应 ASCII 字符的 `uint8` 整数表示。此参数的确切形式取决于 ASCII 字符的类型。

| ASCII 字符类型 | 示例 ASCII 字符 | MATLAB 命令 | 参数值 |
| --- | --- | --- | --- |
| 特殊字符 | `"#"` | `uint8('#')` | `[35]` |
| 数字 | `"81"` | `uint8('81')` | `[56 49]` |
| 字母 | `"End"` | `uint8('End')` | `[69 110 100]` |

| ASCII 字符类型 | 示例 ASCII 字符 | MATLAB 命令 | 参数值 |
| --- | --- | --- | --- |
| 特殊字符 | `"#"` | `uint8('#')` | `[35]` |
| 数字 | `"81"` | `uint8('81')` | `[56 49]` |
| 字母 | `"End"` | `uint8('End')` | `[69 110 100]` |

您也可以使用 ASCII 字符的十六进制表示来指定此参数。

### **Sample time** — 模块从 Arduino 串口读取数据的频率 `0.1`（默认）| 标量

指定该模块读取 Arduino 串口上可用数据的频率。

### **Timeout (ms)** — 模块等待接收数据的时间 `0`（默认）| 正标量

指定当 Arduino 串口上没有可供读取的数据时，该模块在每个时间步中必须等待的时间（以毫秒为单位）。如果发生超时，该模块将中止读取操作。

#### 依赖关系

要启用此参数，请将 **Data length option** 设置为 `Variable length`。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

通过 Arduino 串口接收数据

使用 Serial Receive 模块在 Arduino® 串口上接收 *N*x1 的可变长度数据数组。

在没有硬件的仿真期间，此模块输出零。如果您在包含 Standard Servo Read、Standard Servo Write 或 Continuous Servo Write 模块的 Simulink® 模型中使用此模块，请指定更长的采样时间以避免溢出。

**警告**

在未限制电压的情况下，不要将串口引脚连接到 RS-232 串行接口，例如计算机上的 DE-9M 连接器。RS-232 标准允许更高的电压，这可能会损坏您的硬件。有关详细信息，请阅读 Arduino 硬件的文档。
