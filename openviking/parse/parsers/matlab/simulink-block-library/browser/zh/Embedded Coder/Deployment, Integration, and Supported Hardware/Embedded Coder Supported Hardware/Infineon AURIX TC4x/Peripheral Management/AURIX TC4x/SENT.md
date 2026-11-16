---
type: simulink-block
title: 'SENT'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'sent'
documentation_source_path: 'infineonaurix/ref/sent.html'
language: zh-CN
chinese_source: worker-translation
---

# SENT

## 端口

### 输入

### **datasel** — 基于配置的特性或传感器进行数据选择 `scalar`

此输入端口基于 SENT 配置中的传感器或特性选择配置来请求数据。

**注意**

- 如果将 **SPC 模式** 参数选择为 `Feature selection`，则可以将输入提供为 1、2 或 3。
- 如果将 **SPC 模式** 参数选择为 `Sensor selection`，则可以将输入提供为 1、2、3 或 4（具体取决于 SENT 通道上接口的传感器数量）。

#### 依赖项

要将此端口启用，请将 **SENT 协议** 设置为 **SPC 模式**，并将 **SPC 模式** 参数选择为 `Feature selection` 或 `Sensor selection`。

**数据类型：** `uint8`

### 输出

### **data** — 32 位数据 `scalar` | `vector`

该模块输出表示传感器数据的 32 位值，将 8 个半字节（4 位数据）打包在一起。

**数据类型：** `uint32`

### **serial-data** — 16 位串行数据 `scalar` | `vector`

该模块输出表示传感器数据的 16 位串行数据。

#### 依赖项

要将此端口启用，请选择 **Serial** 参数。

**数据类型：** `uint16`

### **status & comm** — 状态和通信半字节数据（一个半字节） `scalar`

该模块输出传感器发送的状态和通信半字节数据（第 1 个半字节信息），通常提供诊断信息，如故障数据、零件号等。

#### 依赖项

要将此端口启用，请选择 **Status and Communication Nibble** 参数。

**数据类型：** `uint8`

### **channel status** — 通过 SENT 协议进行读取操作的状态 `scalar`

该模块以 `unit32` 标量值形式输出所读取数据的状态，或数据传输期间发生的错误。

| 位 | 状态 | 描述 |
| --- | --- | --- |
| 位 0 | 接收成功 | 在成功接收帧结束时设置此位。如果启用了 CRC 检查，它还表示 CRC 检查成功。 |
| 位 1 | 接收数据成功 | 当接收到的帧被移动到数据寄存器时设置此位。RSI 和 RDI 均是如此。 |
| 位 2 | 接收缓冲区溢出 | 当接收到新数据而旧数据尚未从数据寄存器中读取时设置此位。旧数据将被新数据覆盖。 |
| 位 3 | 传输数据 | 在检测到触发条件后设置此位。要传输的数据已在内部移动，可以将新值写入 SPC 控制寄存器。 |
| 位 4 | 发送缓冲区下溢 | 在数据成功传输后，且没有新数据写入 SPC 控制寄存器时设置此位。 |
| 位 5 | 频率范围错误 | 在接收到与标称值偏差超过 +/- 25% 的同步/校准脉冲后设置此位。 |
| 位 6 | 频率漂移错误 | 在接收到与其前一个脉冲偏差超过 1.5625% 的后续同步/校准脉冲后设置此位。 |
| 位 7 | 接收的半字节数量错误 | 如果接收到的半字节数量少于/多于预期，则设置此位。 |
| 位 8 | 半字节值超出范围 | 如果半字节值不在范围内，则设置此位。它小于 0 或大于 15。 |
| 位 9 | CRC 错误 | CRC 失败时设置此位。 |
| 位 10 | SC 半字节错误 | 如果状态和通信半字节在帧号不是 nx16 的帧中显示起始位，则设置此位。 |
| 位 11 | 收到串行数据 | 使用状态和通信半字节接收到所有串行数据位后设置此位。 |
| 位 12 | 串行数据 CRC 错误 | 如果串行消息的 CRC 失败，则设置此位。 |
| 位 13 | 看门狗错误 | 如果通道的看门狗定时器已过期，则设置此位。 |

#### 依赖项

要将此端口启用，请选择 **启用通道状态端口** 参数。

**数据类型：** `uint32`

## 参数

### 基础

### **数据格式选择** — 选择数据格式 `None` (default) | `Serial` | `Status and communication Nibble`

选择数据格式。

- `Serial` - 在此数据格式下，模块基于 SENT 协议输出串行数据。

  选择此选项时，模块配置 `Serial-data` 输出端口。
- `Status and Communication Nibble` - 在此数据格式下，模块基于 SENT 协议提供状态和通信半字节数据。

  选择此选项时，模块配置 `Status & Comm` 输出端口。

### **启用通道状态端口** — 启用输出数据，指定数据读取状态和错误 `off` (default) | `on`

基于按位分类，启用输出数据，指定数据读取状态和错误（如果有）。

### **采样时间** — 模块读取接收数据的频率 `-1` (default) | `scalar` | `vector`

以秒为单位指定模块应读取接收数据的频率。

当将此参数指定为 `-1` 时，Simulink® 将根据模型中的模块上下文确定模块的最佳采样时间。

### 高级

### **SENT 协议** — 选择 SENT 协议 `Standard` (default) | `SPC`

为通道选择 SENT 协议作为标准或短 PWM 码（SPC）传输。

将此参数选择为 `SPC` 会启用 SENT 配置中 **高级** 选项卡中的选项。

### **SPC 模式** — SPC 传输模式 `Synchronization` (default) | `Feature selection` | `Sensor selection`

选择 SPC 传输模式。

选择此参数会启用 SENT 配置中的相关参数。

#### 依赖项

要查看此参数，请将 **SENT 协议** 参数设置为 `SPC`。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023b 中引入**

## 描述

通过单边半字节传输（SENT）协议读取高分辨率传感器数据

SENT 模块从传感器读取高分辨率数据，并基于 SENT（单边半字节传输）协议（SAE J2716）提供 32 位数据输出。基于 SENT 协议的输出是从传感器到控制器的单向信号，以半字节（4 位数据）的形式编码传感器数据信息，将 8 个半字节打包在一起。

该模块还提供选项，用于启用有关状态和通信半字节、串行数据以及数据接收状态的附加输出。
