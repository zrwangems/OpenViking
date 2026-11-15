---
type: simulink-block
title: 'Serial Transmit'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Serial'
documentation_page: 'serialtransmit'
documentation_source_path: 'supportpkg/arduino_ref/serialtransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Transmit

## 端口

### 输入

### **Data** — 输入数据 [`Nx1`] 数组

该模块输入其通过 Arduino 串口传输到串行设备的数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Serial port** — 用于串行通信的 Arduino 端口号 `0`（默认）| 正整数

指定已连接 Arduino 板的串行端口号。有关固定端口和该模块所分配引脚的详细信息，请参阅 Pin Mapping for Arduino Timer-Independent Blocks。

可以将一个 Serial Transmit 模块和一个 Serial Receive 模块分配到同一个串行端口。不要将多个 Serial Receive 模块分配到同一个 Arduino 串行端口。不要将串行端口使用的 Arduino 引脚编号分配给同一 Simulink 模型中的其他模块。

`XCP over Serial` 通信接口在监视和调节模式下使用串行端口 0，因此不能在 Serial Transmit 模块中使用此端口。可以选择任何其他通信接口，或使用 build and deploy 模式来使用串行端口 0。

### **Send mode** — 数据传输模式 `write`（默认）| `print` | `println`

选择通过 Arduino 串口传输数据的模式。

- `write` — 将原始二进制数据写入 Arduino 串口。
- `print` — 将数据以 ASCII 文本形式打印到 Arduino 串口。
- `println` — 将数据以 ASCII 文本形式打印到 Arduino 串口，后跟回车字符 '\r' 和换行字符 '\n'。

使用 `print` 和 `println` 选项可打印消息，用于调试和记录目的。

### **Header** — 数据数值数组的标头 | 0 到 255（含）的整数

指定一个标头，用于指示数据块的开始。

此参数中指定的数值数组是相应 ASCII 字符的 `uint8` 整数表示。此参数的确切形式取决于 ASCII 字符的类型。

| ASCII 字符类型 | 示例 ASCII 字符 | MATLAB® 命令 | 参数值 |
| --- | --- | --- | --- |
| 特殊字符 | `"#"` | `uint8('#')` | `[35]` |
| 数字 | `"81"` | `uint8('81')` | `[56 49]` |
| 字母 | `"Start"` | `uint8('Start')` | `[83 116 97 114 116]` |

还可以使用 ASCII 字符的十六进制表示来指定此参数。

#### 依赖项

要启用此参数，请将 **Send mode** 设置为 `write`。

### **Terminator** — 数据字符数组的终止符（默认）

指定一个终止符，用于指示数据块的结束。

此参数中指定的数值数组是相应 ASCII 字符的 `uint8` 整数表示。此参数的确切形式取决于 ASCII 字符的类型。

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

还可以使用 ASCII 字符的十六进制表示来指定此参数。

#### 依赖项

要启用此参数，请将 **Send mode** 设置为 `write`。

### **Label** — 数据字符向量的标题

为要通过 Arduino 串口打印的数据指定标题。

#### 依赖项

要启用此参数，请将 **Send mode** 设置为 `print` 或 `println`。

### **Format** — 数据打印格式 `Decimal`（默认）| `Hexadecimal` | `Binary` | `Octal`

选择通过 Arduino 串口打印数据时使用的格式。

#### 依赖项

要启用此参数，请将 **Send mode** 设置为 `print` 或 `println`。

### **Precision** — 十进制数据格式的精度 `2`（默认）| 正整数

指定 Arduino 硬件通过串行通信传输的十进制数据格式的精度。

#### 依赖项

要启用此参数，请将 **Send mode** 设置为 `print` 或 `println`，并将 **Format** 设置为 `Decimal`。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

通过 Arduino 串口传输数据

使用 Serial Transmit 模块通过 Arduino® 串口将可变长度的 *N*x1 数据数组传输到串行设备。

在无硬件的仿真期间，此模块不会传输数据。如果在包含 Standard Servo Read、Standard Servo Write 或 Continuous Servo Write 模块的 Simulink® 模型中使用此模块，请使用更长的采样时间以避免超限。

**警告**

请勿在未限制电压的情况下将串口引脚连接到 RS-232 串行接口，例如计算机上的 DE-9M 连接器。RS-232 标准允许更高的电压，可能会损坏硬件。有关详细信息，请阅读 Arduino 硬件的文档。

**注意**

对于 Arduino Uno、Mega 和 Nano 板，double 数据类型占用 4 bytes。对于 Arduino SAMD、Due、ESP32 compatible、Teensy 和 Nano 33 BLE 硬件板，double 数据类型占用 8 bytes。
