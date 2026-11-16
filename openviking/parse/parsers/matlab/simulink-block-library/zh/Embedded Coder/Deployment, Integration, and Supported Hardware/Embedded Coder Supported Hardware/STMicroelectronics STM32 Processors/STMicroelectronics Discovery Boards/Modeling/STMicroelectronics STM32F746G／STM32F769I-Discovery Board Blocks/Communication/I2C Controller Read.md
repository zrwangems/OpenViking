---
type: simulink-block
title: 'I2C Controller Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Communication'
documentation_page: 'i2ccontrollerreadblock'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/i2ccontrollerreadblock.html'
language: zh-CN
chinese_source: worker-translation
---

# I2C Controller Read

## 端口

### 输出

### **Data** — 来自 I2C 外设设备的数据向量

该端口从板上的 I2C 设备读取向量数据。数据大小是你在 **数据大小** 参数中指定的值。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — 读取操作的状态标量

选择 **输出错误状态** 参数时，将提供一个标记为 `Status` 的输出端口。

该端口按下表所述输出每个读取请求的状态：

**返回状态代码**

| **Status** | 描述 |
| --- | --- |
| `0` | SUCCESS |
| `1` | BUSY |
| `2` | ARBITRATION\_LOST |
| `4` | NO\_ACKNOWLEDGE |
| `8` | BUS\_ERROR |
| `16` | BUS\_NOT\_IN\_USE |

**数据类型：** `uint8`

## 参数

### **I2C 模块** — 用于读取数据的 I2C 模块 `0`（默认值）

指定板上要从 I2C 外设设备读取数据的 I2C 模块。

### **外设地址** — 要从中读取数据的 I2C 寄存器外设地址 `10`（默认值） | `大于或等于 0 的整数`

指定要读取数据的 I2C 外设地址。你可以使用十六进制格式 `hex2dec()` 指定此地址，例如，‘hex2dec(‘20’)’。

### **外设字节序** — 你的 I2C 外设设备支持的字节排序 `BigEndian`（默认值） | `LittleEndian`

2 字节排序选项包括：

- BigEndian - 最高有效字节先通过 I2C 总线发送。
- LittleEndian - 最低有效字节先通过 I2C 总线发送。

### **启用寄存器访问** — 从特定 I2C 外设寄存器读取的选项 on（默认值） | off

选择此参数时，模块从你在 **外设寄存器地址** 参数中指定的 I2C 外设寄存器读取数据。

清除此参数时，将显示 **在数据传输结束时发送 NACK** 和 **在数据传输结束时移除停止位** 参数。使用这些参数，可以根据需求修改读取操作。

### **外设寄存器地址** — 要读取数据的 I2C 外设寄存器地址 `0`（默认值） | `0 到 255 之间的整数`

指定要读取数据的 I2C 寄存器地址。

使用 `hex2dec()` 将此地址指定为整数或十六进制格式，例如，‘hex2dec(‘20’)’。

有关寄存器读/写的详细信息，请参阅 I2C Register Read/Write。

#### 依赖项

仅当选择 **启用寄存器访问** 参数时，此参数才会显示。

### **数据类型** — 来自 I2C 外设设备的数据的数据类型 `uint8`（默认值） | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

选择要从 I2C 外设设备读取的数据类型。

### **数据大小 (N)** — 要从 I2C 外设设备读取的数据大小 `1`（默认值） | `大于或等于 0 的整数`

指定要为所选数据类型从 I2C 外设设备读取的数据大小。

### **在数据传输结束时发送 NACK** — 在数据传输结束时发送 Not Acknowledge 位的选项 off（默认值） | on

选择此参数时，I2C Controller Read 模块会在最后一个字节向外设设备发送 NACK（Not Acknowledge）位。

当外设设备收到 NACK 时，它会等待来自 I2C Controller 模块的 STOP 条件。Controller 模块会生成 STOP 条件以中止传输，或生成重复 START 条件以开始新传输。

清除此参数时，I2C Controller Read 模块会在每个字节结束时向外设设备发送 ACK（Acknowledge）位。ACK 表示 I2C Controller Read 模块已准备好从外设设备读取下一个字节。

#### 依赖项

仅当清除 **启用寄存器访问** 参数时，此参数才会显示。

### **在数据传输结束时移除停止位** — 在数据传输结束时移除 STOP 位的选项 off（默认值） | on

清除此参数时，模块会发送 STOP 条件。此条件表示模块已终止数据传输，并且 I2C 总线空闲，可供任何其他 I2C Controller 模块启动新的读/写操作。

选择此参数时，模块会发送另一个 START 条件，后跟地址和读/写位。模块会递归地发送任意数量的 START 条件。这种重复 START 条件允许在不释放总线的情况下向外设设备执行写操作。没有其他 Controller 模块会中断该操作。

#### 依赖项

仅当清除 **启用寄存器访问** 参数时，此参数才会显示。

### **输出错误状态** — 在数据传输期间显示错误状态的选项 off（默认值） | on

选择此参数时，将提供一个标记为 `Status` 的输出端口。

该端口在读取操作成功时输出 `0`。

### **采样时间** — 从 I2C 外设设备读取数据的频率 `0.1`（默认值）

指定 I2C Controller Read 模块从 I2C 外设设备读取数据的频率。将此参数指定为 `-1` 时，模块会根据其在模型中的上下文继承采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F746G-Discovery

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018a 中引入**

## 描述

从 I2C 外设设备或 I2C 外设设备寄存器读取数据

I2C Controller Read 模块从连接到板的 I2C 外设设备读取串行数据。使用此模块，可以从 I2C 外设设备上的特定寄存器读取数据。

有关 I2C 通信的详细信息，请参阅 Support I2C Communication。
