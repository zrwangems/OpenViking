---
type: simulink-block
title: 'I2C Controller Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'i2ccontrollerwriteblock'
documentation_source_path: 'nucleo/ref/i2ccontrollerwriteblock.html'
language: zh-CN
chinese_source: official
---

# I2C Controller Write

## 端口

### 输入

### **Data** — 要写入 I2C 外围设备的数据 标量 | 向量

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`
### 输出

### **Status** — 写入操作的状态 标量

当您选择**输出错误状态**参数时，标签为 `Status` 的输出端口变为可用。

该端口输出 `0` 表示成功的写入操作。

**数据类型:** `uint8`

## 参数

### **I2C 模块** — 用于写入数据的 I2C 模块 `0` (默认) | `integer greater than or equal to 0`

指定板上用于向 I2C 外围设备写入数据的 I2C 模块。

### **外设地址** — 要写入数据的 I2C 外设地址 `hex2dec('48')` (默认)

指定要写入数据的 I2C 外设地址。I2C 外围设备地址是 7 位地址。

使用 `hex2dec()` 将此地址指定为整数或十六进制格式，例如，hex2dec(‘61’)。

### **外设字节顺序** — 您的 I2C 外围设备支持的字节顺序 **BigEndian** (默认) | **LittleEndian**

2 字节顺序选项为：

- BigEndian - 最高有效字节首先通过 I2C 总线发送。
- LittleEndian - 最低有效字节首先通过 I2C 总线发送。

### **启用寄存器访问** — 向特定 I2C 外设寄存器写入的选项 on (默认) | off

当您选择此参数时，模块向您在**外设寄存器地址**参数中指定的 I2C 外设寄存器写入数据。

当您清除此参数时，会显示**在数据传输结束时发送 NACK** 和**在数据传输结束时删除停止位**参数。使用这些参数，您可以根据需要修改写入操作。

### **外设寄存器地址** — 要写入数据的 I2C 外设寄存器地址 `uint8(1)` (默认)

指定要写入数据的 I2C 外设寄存器地址。

以 8 位无符号整数或十六进制格式指定此地址。要以 8 位无符号整数指定地址，请使用 `uint8()`，例如，uint8(20)。要以十六进制格式指定地址，请使用 `hex2dec()`，例如，hex2dec(‘20’)。

有关寄存器读/写的详细信息，请参阅 I2C 寄存器读/写。

#### 依赖关系

此参数仅在您选择**启用寄存器访问**参数时出现。

### **在数据传输结束时发送 NACK** — 在数据传输结束时发送未应答位的选项 off (默认) | on

当您选择此参数时，I2C Controller Write 模块向外围设备发送 NACK（未应答）位与最后一个字节。

当外围设备接收到 NACK 时，它等待来自 I2C Controller 模块的 STOP 条件。该控制器模块生成 STOP 条件以中止传输或生成重复 START 条件以开始新传输。

当您清除此参数时，I2C Controller Write 模块在每个字节结束时向外围设备发送 ACK（应答）位。ACK 指示 I2C Controller Write 模块已准备好从外围设备读取下一个字节。

#### 依赖关系

此参数仅在您清除**启用寄存器访问**参数时出现。

### **在数据传输结束时删除停止位** — 在数据传输结束时删除 STOP 位的选项 off (默认) | on

当您清除此参数时，模块会发送 STOP 条件。此条件指示模块已终止数据传输，并且 I2C 总线处于空闲状态，可供任何其他 I2C Controller 模块启动读取/写入操作。

当您选择此参数时，模块会发送另一个 START 条件，后跟地址和读取/写入位。模块以递归方式发送任意数量的开始条件。此类重复的 START 条件允许对外围设备进行写入操作而不释放总线。没有其他控制器模块中断该操作。

#### 依赖关系

此参数仅在您清除**启用寄存器访问**参数时出现。

### **输出错误状态** — 显示数据传输期间错误状态的选项 off (默认) | on

当您选择此参数时，标签为 `Status` 的输出端口将变为可用。

该端口输出 `0` 表示成功的写入操作。

## 所属库

Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F746G-Discovery

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2018a 中推出**

## 描述

向 I2C 外围设备或 I2C 外围设备寄存器写入数据

I2C Controller Write 模块向连接到板的 I2C 外围设备写入数据。使用此模块，您可以向 I2C 外围设备上的特定寄存器写入数据。

有关 I2C 通信的详细信息，请参阅支持 I2C 通信。
