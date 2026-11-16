---
type: simulink-block
title: 'C28x I2C Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xi2ctransmit'
documentation_source_path: 'ref/c28xi2ctransmit.html'
language: zh-CN
chinese_source: official
---

# C28x I2C Transmit

## 端口

### 输入

### **SAR** — 外设地址寄存器值 标量

外设地址寄存器的值。

#### 依赖关系

只有当 **peripheral address source** 设置为**输入端口**时，才会出现此端口。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **WD** — 写入 I2C 总线的数据 标量 | 向量

写入 I2C 总线的数据。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### 输出

### **status** — I2C 通信状态 标量

来自 I2C 状态寄存器 (I2CSTR) 的状态值。

#### 依赖关系

仅当选择 **Output transmitting status** 时才会显示此端口。

**数据类型:** `uint16`

## 参数

### **模块** — 通信模块 **I2C\_A** (默认) | **I2C\_B**

用于通信的 I2C 模块。不同 C2000™ 处理器支持的 I2C 模块数量各不相同。

### **寻址格式** — 通信地址格式 **7 位寻址** (默认) | **10 位寻址** | **自由数据格式**

通信地址格式。该图显示了每种选项的格式。I2C Transmit 模块将 R/W 位设置为 1。

S - 开始位

R/W - 读/写

ACK - 确认

P - 停止位

MSB - 最高有效位

LSB - 最低有效位

### **外设地址源** — I2C 外设的外设地址源 **通过对话框指定** (默认) | **输入端口**

设置 I2C 外设地址寄存器的方法。

### **外设地址寄存器** — 外设地址寄存器值 `80` (默认) | 标量

根据所选的寻址格式，输入 7 位或 10 位外设地址。

#### 依赖关系

只有当 **Peripheral address source** 设置为**通过对话框指定**时，此参数才会出现。

### **位计数** — 通信比特计数 **8** (默认) | [1 8] 范围内的整数

I2C 模块接收到的数据字节中的位数。

### **启用停止条件** — 发送停止位以指示数据传输完成 `off` (默认) | `on`

当 I2C 模块配置为控制器时，I2C 模块会向 I2C 总线发送停止位，以指示数据传输已完成。I2C 总线可供任何其他 I2C 模块发起读/写操作。

### **启用重复模式** — 重新传输数据，直到检测到停止或启动条件。 `off` (默认) | `on`

启用重复模式后，I2C 模块会持续传输数据，直到检测到停止或开始条件为止。如果您使用此模式，还应考虑选择 **Enable stop condition** 以确保在停止条件之后数据传输停止。

如果禁用重复模式，I2C 模块将以标准模式运行，一次性发送特定数量的数据值。

### **输出传输状态** — 指示 I2C 发送模块何时发送消息 `off` (默认) | `on`

启用状态输出端口，该端口指示 I2C 发送模块何时发送消息。

## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

R2025b 官方文档未提供。

## 描述

配置集成电路间通信 (I2C) 模块，使其向 I2C 总线传输数据。

I2C Transmit 模块配置集成电路间 (I2C) 模块，使其向双线 I2C 串行总线传输数据。I2C Transmit 模块支持处理器与外部外设或其他控制器之间的 I2C 总线通信。该模块既可以运行在外设模式下，也可以运行在控制器模式下。

当 I2C 模块配置为控制器时，该模块会从外围设备接收数据。当 I2C 模块配置为外设时，该模块会从控制器接收数据。通过导航至 **配置参数** > **硬件实现** > **Target hardware resources** 配置 I2C 模块。

要从外设读取数据，请使用 I2C Transmit 模块将要读取的寄存器的地址发送到外设。使用 I2C Receive 模块从外设读取数据之前，确保数据已从 Tx FIFO 发送到外设。有关更多信息，请参阅使用 I2C 总线访问传感器。
