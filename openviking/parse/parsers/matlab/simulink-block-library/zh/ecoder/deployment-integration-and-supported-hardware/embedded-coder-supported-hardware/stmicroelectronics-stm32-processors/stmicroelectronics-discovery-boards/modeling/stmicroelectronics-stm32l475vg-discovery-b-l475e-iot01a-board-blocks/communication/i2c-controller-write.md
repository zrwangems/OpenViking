---
type: simulink-block
title: 'I2C Controller Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Communication'
documentation_page: 'i2ccontrollerwriteblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/i2ccontrollerwriteblock.html'
language: zh-CN
chinese_source: worker-translation
---

# I2C Controller Write

## 端口

### 输入

### **Data** — 要写入 I2C 外设的数据 标量 | 向量

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`
### 输出

### **Status** — 写操作的状态 标量

当您选择 **Output error status** 参数时，一个标记为 `Status` 的输出端口将变为可用。

该端口在写操作成功时输出 `0`。

**数据类型：** `uint8`

## 参数

### **I2C module** — 要写入数据的 I2C 模块 `0`（默认） | `integer greater than or equal to 0`

指定板上的 I2C 模块，以将数据写入 I2C 外设。

### **Peripheral address** — 要写入数据的 I2C 外设地址 `hex2dec('48')`（默认）

指定要写入数据的 I2C 外设地址。I2C 外设设备地址是 7 位地址。

将此地址指定为整数或使用 `hex2dec()` 以十六进制格式指定，例如，‘hex2dec(‘61’)’。

### **Peripheral byte order** — I2C 外设支持的字节顺序 `BigEndian`（默认） | `LittleEndian`

2 字节顺序选项包括：

- BigEndian - 最高有效字节先通过 I2C 总线发送。
- LittleEndian - 最低有效字节先通过 I2C 总线发送。

### **Enable register access** — 写入特定 I2C 外设寄存器的选项 on（默认） | off

当您选择此参数时，模块将数据写入您在 **Peripheral register address** 参数中指定的 I2C 外设寄存器。

当您清除此参数时，将显示 **Send NACK at the end of data transfer** 和 **Remove stop bit at the end of data transfer** 参数。使用这些参数，您可以根据需求修改写操作。

### **Peripheral register address** — 要写入数据的 I2C 外设寄存器地址 `uint8(1)`（默认）

指定要写入数据的 I2C 外设寄存器地址。

将此地址指定为 8 位无符号整数或十六进制格式。要将地址指定为 8 位无符号整数，请使用 `uint8()`，例如，‘uint8(20)’。要将地址指定为十六进制格式，请使用 `hex2dec()`，例如，‘hex2dec(‘20’)’。

有关寄存器读/写的详细信息，请参阅 I2C Register Read/Write。

#### 依赖关系

此参数仅在您选择 **Enable register access** 参数时显示。

### **Send NACK at the end of data transfer** — 在数据传输结束时发送 Not Acknowledge 位的选项 off（默认） | on

当您选择此参数时，I2C Controller Write 模块将在最后一个字节向 I2C 外设发送 NACK（Not Acknowledge）位。

当 I2C 外设收到 NACK 时，它会等待来自 I2C 控制器模块的 STOP 条件。控制器模块生成 STOP 条件以中止传输，或生成重复 START 条件以开始新的传输。

当您清除此参数时，I2C Controller Write 模块在每个字节结束时向 I2C 外设发送 ACK（Acknowledge）位。ACK 表示 I2C Controller Write 模块已准备好从 I2C 外设读取下一个字节。

#### 依赖关系

此参数仅在您清除 **Enable register access** 参数时显示。

### **Remove stop bit at the end of data transfer** — 在数据传输结束时移除 STOP 位的选项 off（默认） | on

当您清除此参数时，模块发送 STOP 条件。此条件表示模块已终止数据传输，并且 I2C 总线空闲，任何其他 I2C 控制器模块都可以启动读/写操作。

当您选择此参数时，模块发送另一个 START 条件，后跟地址和读/写位。模块可以递归地发送任意数量的启动条件。这种重复 START 条件允许在不释放总线的情况下对 I2C 外设执行写操作。没有其他控制器模块会中断该操作。

#### 依赖关系

此参数仅在您清除 **Enable register access** 参数时显示。

### **Output error status** — 显示数据传输期间错误状态的选项 off（默认） | on

当您选择此参数时，一个标记为 `Status` 的输出端口将变为可用。

该端口在写操作成功时输出 `0`。

## 所属库

Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F746G-Discovery

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

将数据写入 I2C 外设或 I2C 外设寄存器

I2C Controller Write 模块将数据写入连接到板的 I2C 外设。使用此模块，您可以将数据写入 I2C 外设上的特定寄存器。

有关 I2C 通信的详细信息，请参阅 Support I2C Communication。
