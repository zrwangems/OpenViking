---
type: simulink-block
title: 'I2C Controller Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'i2ccontrollerwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/i2ccontrollerwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# I2C Controller Write

## 端口

### 输入

### **Data** — 要写入 I2C 外设设备的数据 标量 | 向量

该端口将数据写入板上的 I2C 设备。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`
### 输出

### **Status** — 写操作的状态 标量

该端口在写操作成功时输出 `0`。

#### 依赖关系

要启用此端口，请选择 **输出错误状态** 参数。

**数据类型：** `uint8`

## 参数

### **I2C 模块** — 要写入数据的 I2C 模块 `I2C1`（默认） | `I2C2` | `I23C` | `...`

指定板上用于将数据写入 I2C 外设设备的 I2C 模块。

### **外设字节序** — I2C 外设设备支持的字节排序 `BigEndian`（默认） | `LittleEndian`

2 字节排序选项包括：

- BigEndian - 最高有效字节先通过 I2C 总线发送。
- LittleEndian - 最低有效字节先通过 I2C 总线发送。

### **外设地址来源** — I2C 的外设地址来源 `Dialog`（默认） | `Inport`

选择 I2C 控制器的外设地址来源。

### **外设地址** — 要写入数据的 I2C 外设地址 `10`（默认）

指定要写入数据的 I2C 外设地址。I2C 外设设备地址是 7 位地址。

使用 `hex2dec()` 将此地址指定为整数或十六进制格式，例如，‘hex2dec(‘61’)’。

### **启用寄存器访问地址模式** — 用于写入特定 I2C 外设寄存器的选项 on（默认） | off

选择此参数时，模块会将数据写入您在 **外设寄存器地址** 参数中指定的 I2C 外设寄存器。

清除此参数时，将显示 **在传输结束时发送非确认** 和 **在数据传输结束时移除停止位（重复起始）** 参数。使用这些参数，您可以根据需求修改写操作。

### **外设寄存器地址** — 要写入数据的 I2C 外设寄存器地址 `uint8(1)`（默认）

指定要写入数据的 I2C 外设寄存器地址。

使用 8 位无符号整数或十六进制格式指定此地址。要使用 8 位无符号整数指定地址，请使用 `uint8()`，例如，‘uint8(20)’。要使用十六进制格式指定地址，请使用 `hex2dec()`，例如，‘hex2dec(‘20’)’。

有关寄存器读/写的详细信息，请参阅 I2C 寄存器读/写。

#### 依赖关系

仅当选择 **启用寄存器访问地址模式** 参数时，此参数才会出现。

### **在数据传输结束时移除停止位（重复起始）** — 用于在数据传输结束时移除 STOP 位的选项 off（默认） | on

未选择此参数时，模块会发送 STOP 条件。此条件表示模块已终止数据传输，并且 I2C 总线空闲，可供任何其他 I2C Controller 模块启动新的读/写操作。

选择此参数时，模块会发送另一个 START 条件，后跟地址和读/写位。模块会递归地发送任意数量的起始条件。这种重复 START 条件允许在不释放总线的情况下向外设设备执行写操作。其他控制器模块不会中断该操作。

#### 依赖关系

要启用此参数，请取消选择 **启用寄存器访问地址模式** 参数。

### **在传输结束时发送非确认** — 用于在数据传输结束时发送 Not Acknowledge 位的选项 off（默认） | on

选择此参数时，I2C Controller Read 模块会随最后一个字节向外设设备发送 NACK（Not Acknowledge）位。

当外设设备收到 NACK 时，它会等待来自 I2C Controller 模块的 STOP 条件。控制器模块会生成 STOP 条件以中止传输，或生成重复 START 条件以启动新传输。

取消选择此参数时，I2C Controller Read 模块会在每个字节结束时向外设设备发送 ACK（Acknowledge）位。ACK 表示 I2C Controller Read 模块已准备好从外设设备读取下一个字节。

#### 依赖关系

要启用此参数，请取消选择 **启用寄存器访问地址模式** 参数。

### **输出错误状态** — 用于在数据传输期间显示错误状态的选项 off（默认） | on

选择此参数时，模块会配置一个输出端口。模块上的端口标记为 `Status`，表示模块在输出端口输出写操作的状态。

模块将状态输出为 `uint8` 值。每个值对应一种数据传输状态。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `I2C_BUS_ERROR` |

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F1xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G0xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32U5xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32WBxx Based Boards Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

未在 R2025b 中记录。

## 描述

将数据写入 I2C 外设设备或 I2C 外设设备寄存器

I2C Controller Write 模块将数据写入连接到板上的 I2C 外设设备。使用此模块，您可以将数据写入 I2C 外设设备上的特定寄存器。有关 I2C 通信的详细信息，请参阅支持 I2C 通信。

**注意**

您可以在基于 STM32 处理器的开发板上，以 Connected IO 模式运行包含 I2C Controller Write 模块的 Simulink® 模型。有关详细信息，请参阅使用 Connected IO 与硬件通信。
