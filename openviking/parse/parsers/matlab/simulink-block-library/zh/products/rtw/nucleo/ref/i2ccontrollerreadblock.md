---
type: simulink-block
title: 'I2C Controller Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'i2ccontrollerreadblock'
documentation_source_path: 'nucleo/ref/i2ccontrollerreadblock.html'
language: zh-CN
chinese_source: official
---

# I2C Controller Read

## 端口

### 输出

### **Data** — 来自 I2C 外围设备的数据 向量

该端口从板上的 I2C 设备读取向量数据。数据的大小是您在**数据大小**参数中指定的值。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — 读取操作的状态 标量

当您选择**输出错误状态**参数时，标签为 `Status` 的输出端口变为可用。

该端口输出每个读取请求的状态，如下表所示：

**返回状态代码**

| **状态** | 描述 |
| --- | --- |
| `0` | SUCCESS |
| `1` | BUSY |
| `2` | ARBITRATION\_LOST |
| `4` | NO\_ACKNOWLEDGE |
| `8` | BUS\_ERROR |
| `16` | BUS\_NOT\_IN\_USE |

**数据类型:** `uint8`

## 参数

### **I2C 模块** — 用于读取数据的 I2C 模块 `0` (默认)

指定板上用于从 I2C 外围设备读取数据的 I2C 模块。

### **外设地址** — 要从中读取数据的 I2C 寄存器外设地址 `10` (默认) | `integer greater than or equal to 0`

指定要读取数据的 I2C 外设地址。您可以使用十六进制格式 `hex2dec()` 指定此地址，例如，‘hex2dec(‘20’)’。

### **外设字节顺序** — 您的 I2C 外围设备支持的字节顺序 **BigEndian** (默认) | **LittleEndian**

2 字节顺序选项为：

- BigEndian - 最高有效字节首先通过 I2C 总线发送。
- LittleEndian - 最低有效字节首先通过 I2C 总线发送。

### **启用寄存器访问** — 从特定 I2C 外设寄存器读取的选项 on (默认) | off

当您选择此参数时，模块从您在**外设寄存器地址**参数中指定的 I2C 外设寄存器读取数据。

当您清除此参数时，会显示**在数据传输结束时发送 NACK** 和**在数据传输结束时删除停止位**参数。使用这些参数，您可以根据需要修改读取操作。

### **外设寄存器地址** — 要读取数据的 I2C 外设寄存器地址 `0` (默认) | `integer between 0 and 255`

指定要读取数据的 I2C 寄存器地址。

使用 `hex2dec()` 将此地址指定为整数或十六进制格式，例如，hex2dec(‘20’)。

有关寄存器读/写的详细信息，请参阅 I2C 寄存器读/写。

#### 依赖关系

此参数仅在您选择**启用寄存器访问**参数时出现。

### **数据类型** — 来自 I2C 外围设备的数据的数据类型 `uint8` (默认) | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

选择您要从 I2C 外围设备读取的数据类型。

### **数据大小(N)** — 要从 I2C 外围设备读取的数据大小 `1` (默认) | `integer greater than or equal to 0`

指定您要从 I2C 外围设备读取的选定数据类型的数据大小。

### **在数据传输结束时发送 NACK** — 在数据传输结束时发送未应答位的选项 off (默认) | on

当您选择此参数时，I2C Controller Read 模块向外围设备发送 NACK（未应答）位与最后一个字节。

当外围设备接收到 NACK 时，它会等待来自 I2C Controller 模块的 STOP 条件。该控制器模块生成 STOP 条件以中止传输或生成重复 START 条件以开始新传输。

当您清除此参数时，I2C Controller Read 模块在每个字节结束时向外围设备发送 ACK（应答）位。ACK 指示 I2C Controller Read 模块已准备好从外围设备读取下一个字节。

#### 依赖关系

此参数仅在您清除**启用寄存器访问**参数时出现。

### **在数据传输结束时删除停止位** — 在数据传输结束时删除 STOP 位的选项 off (默认) | on

当您清除此参数时，模块会发送 STOP 条件。此条件指示模块已终止数据传输，并且 I2C 总线处于空闲状态，可供任何其他 I2C Controller 模块启动新的读取/写入操作。

当您选择此参数时，模块会发送另一个 START 条件，后跟地址和读取/写入位。模块以递归方式发送任意数量的开始条件。此类重复的 START 条件允许对外围设备进行写入操作而不释放总线。没有其他控制器模块中断该操作。

#### 依赖关系

此参数仅在您清除**启用寄存器访问**参数时出现。

### **输出错误状态** — 显示数据传输期间错误状态的选项 off (默认) | on

当您选择此参数时，标签为 `Status` 的输出端口将变为可用。

该端口输出 `0` 表示读取操作成功。

### **采样时间** — 从 I2C 外围设备读取数据的频率 `0.1` (默认)

指定 I2C Controller Read 模块从 I2C 外围设备读取数据的频率。当您将此参数指定为 `-1` 时，模块根据其在模型中的上下文继承其采样时间。

## 所属库

Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics Discovery Boards / STM32F746G-Discovery

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2018a 中推出**

## 描述

从 I2C 外围设备或 I2C 外围设备寄存器读取数据

I2C Controller Read 模块从连接到板的 I2C 外围设备读取串行数据。使用此模块，您可以从 I2C 外围设备上的特定寄存器读取数据。

有关 I2C 通信的详细信息，请参阅支持 I2C 通信。
