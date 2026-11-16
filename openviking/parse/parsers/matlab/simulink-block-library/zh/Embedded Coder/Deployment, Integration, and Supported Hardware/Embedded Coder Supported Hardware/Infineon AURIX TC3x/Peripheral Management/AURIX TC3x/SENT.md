---
type: simulink-block
title: 'SENT'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'sent'
documentation_source_path: 'infineonaurixtc3x/ref/sent.html'
language: zh-CN
chinese_source: worker-translation
---

# SENT

## 端口

### 输入

### **DataSel** — 基于功能或传感器配置的数据选择 `scalar`

此输入端口基于 SENT Configuration 中的传感器或功能选择配置请求数据。

**注意**

- 如果选择 **SPC 模式** 参数为 `Feature selection`，则可以将输入提供为 1、2 或 3。
- 如果选择 **SPC 模式** 参数为 `Sensor selection`，则可以将输入提供为 1、2、3 或 4（取决于 SENT 通道上接口的传感器数量）。

#### 依赖关系

要启用此端口，请将 **SENT 协议** 设置为 **SPC 模式**，并选择 **SPC 模式** 参数为 `Feature selection` 或 `Sensor selection`。

**数据类型：** `uint8`

### 输出

### **Data** — 32-bit 数据 `scalar` | `vector`

该模块输出表示传感器数据的 32-bit 值，将 8 个 nibble（4-bit 数据）打包在一起。

**数据类型：** `uint32`

### **Serial-data** — 16-bit 串行数据 `scalar` | `vector`

该模块输出表示传感器数据的 16-bit 串行数据。

#### 依赖关系

要启用此端口，请选择 **Serial** 参数。

**数据类型：** `uint16`

### **Status & Comm** — Status and Communication nibble 数据（一个 nibble） `scalar`

该模块输出传感器发送的 Status and Communication nibble 数据（第 1 个 nibble 信息），通常提供诊断信息，如故障数据、零件号等。

#### 依赖关系

要启用此端口，请选择 **Status and communication nibble** 参数。

**数据类型：** `uint8`

### **Channel status** — SENT 协议上读取操作的状态 `scalar`

该模块以 `unit32` scalar 值输出已读取数据的状态，或数据传输期间发生的错误。

| Bit | 状态 | 描述 |
| --- | --- | --- |
| Bit 0 | 接收成功 | 当帧成功接收结束时置位此位。如果启用了 CRC 检查，它还指示 CRC 检查成功。 |
| Bit 1 | 接收数据成功 | 当接收到的帧被移动到数据寄存器时置位此位。包括 RSI 和 RDI。 |
| Bit 2 | 接收缓冲区溢出 | 当接收到新数据而旧数据仍未从数据寄存器读取时，置位此位。旧数据会被新数据覆盖。 |
| Bit 3 | 传输数据 | 检测到触发条件后置位此位。要传输的数据已在内部移动，新值可以写入 SPC control register。 |
| Bit 4 | 发送缓冲区下溢 | 数据成功传输后且没有新数据写入 SPC control register 时，置位此位。 |
| Bit 5 | 频率范围错误 | 接收到偏离标称值超过 +/- 25% 的 Synchronization / Calibration 脉冲后，置位此位。 |
| Bit 6 | 频率漂移错误 | 接收到与其前一个脉冲偏差超过 1.5625% 的后续 Synchronization / Calibration 脉冲后，置位此位。 |
| Bit 7 | 接收到的 nibble 数量错误 | 如果接收到的 nibble 少于/多于预期，则置位此位。 |
| Bit 8 | nibble 值超出范围 | 如果 nibble 的值不在范围内，则置位此位。它小于 0 或大于 15。 |
| Bit 9 | CRC 错误 | 当 CRC 失败时置位此位。 |
| Bit 10 | SC nibble 错误 | 如果 Status and Communication nibble 在帧号不是 nx16 的帧中显示起始位，则置位此位。 |
| Bit 11 | 串行数据已接收 | 使用 Status and Communication nibble 接收到所有串行数据位后，置位此位。 |
| Bit 12 | 串行数据 CRC 错误 | 如果串行消息的 CRC 失败，则置位此位。 |
| Bit 13 | 看门狗错误 | 如果通道的看门狗定时器已到期，则置位此位。 |

#### 依赖关系

要启用此端口，请选择 **启用通道状态端口** 参数。

**数据类型：** `uint32`

## 参数

### 基础

### **数据格式选择** — 选择数据格式 `None` (default) | `Serial` | `Status and Communication Nibble`

选择数据格式。

- `Serial` - 在此数据格式中，该模块基于 SENT 协议输出串行数据。

  选择此选项时，该模块配置 `Serial-data` 输出端口。
- `Status and Communication Nibble` - 在此数据格式中，该模块基于 SENT 协议提供 Status and Communication nibble 数据。

  选择此选项时，该模块配置 `Status & Comm` 输出端口。

### **启用通道状态端口** — 启用指定数据读取状态和错误的输出数据 `off` (default) | `on`

启用基于按位分类指定数据读取状态和错误（如果有）的输出数据。

### **采样时间** — 模块读取接收数据的频率 `-1` (default) | `scalar` | `vector`

以秒为单位指定该模块应读取接收数据的频率。

当将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

### 高级

### **SENT 协议** — 选择 SENT 协议 `Standard` (default) | `SPC`

选择 SENT 协议为通道的标准或短 PWM 代码 (SPC) 传输。

将此参数选择为 `SPC` 会启用 SENT Configuration 中 **高级** 选项卡中的选项。

### **SPC 模式** — SPC 传输模式 `Synchronization` (default) | `Feature selection` | `Sensor selection`

选择 SPC 传输模式。

选择此参数会启用 SENT Configuration 中的相关参数。

#### 依赖关系

要查看此参数，请将 **SENT 协议** 参数设置为 `SPC Mode`。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

通过单边半字节传输 (SENT) 协议读取高分辨率传感器数据

SENT 模块从传感器读取高分辨率数据，并基于 SENT（单边半字节传输）协议 (SAE J2716) 提供 32-bit 数据输出。基于 SENT 协议的输出是从传感器到控制器的单向信号，以 nibble（4-bit 数据）形式编码传感器数据信息，将 8 个 nibble 打包在一起。

该模块还提供选项，以启用关于 Status and Communication nibble、串行数据以及数据接收状态的附加输出。
