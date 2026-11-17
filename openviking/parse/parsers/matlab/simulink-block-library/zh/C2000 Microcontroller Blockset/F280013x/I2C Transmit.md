---
type: simulink-block
title: 'C28x I2C Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'c28xi2ctransmit'
documentation_source_path: 'ref/c28xi2ctransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# C28x I2C Transmit

## 端口
```yaml
ports:
- name: SAR
  summary: 外设地址寄存器值 标量
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: WD
  summary: 写入 I2C 总线的数据 标量 | 向量
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32
- name: status
  summary: I2C 通信状态 标量
  direction: output
  data_types: uint16
```

### 输入

### **SAR** — 外设地址寄存器值 标量

外设地址寄存器值。

#### 依赖关系

此端口仅在 **peripheral address source** 设置为 `Input port` 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **WD** — 写入 I2C 总线的数据 标量 | 向量

写入 I2C 总线的数据。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### 输出

### **status** — I2C 通信状态 标量

来自 I2C 状态寄存器 (I2CSTR) 的状态值。

#### 依赖关系

此端口仅在选中 **Output transmitting status** 时出现。

**数据类型：** `uint16`
## 参数
```yaml
parameters:
- name: Module
  summary: 用于通信的模块 I2C_A（默认）| I2C_B
  group: ''
- name: Addressing format
  summary: 通信的地址格式 7–Bit addressing（默认）| 10–Bit addressing | Free data format
  group: ''
- name: peripheral address source
  summary: I2C 外设的外设地址来源 Specify via dialog（默认）| Input port
  group: ''
- name: Peripheral address register
  summary: 外设地址寄存器值 80（默认）| 标量
  group: ''
- name: Bit count
  summary: 通信的位数 8（默认）| [1 8] 范围内的整数
  group: ''
- name: Enable stop condition
  summary: 发送停止位以指示数据传输完成 off（默认）| on
  group: ''
- name: Enable repeat mode
  summary: 重复传输数据直到检测到停止或起始条件 off（默认）| on
  group: ''
- name: Output transmitting status
  summary: 指示 I2C 发送模块何时传输消息 off（默认）| on
  group: ''
```

### **Module** — 用于通信的模块 `I2C_A`（默认）| `I2C_B`

用于通信的 I2C 模块。支持的 I2C 模块数量因不同的 C2000™ 处理器而异。

### **Addressing format** — 通信的地址格式 `7–Bit addressing`（默认）| `10–Bit addressing` | `Free data format`

通信的地址格式。图中显示了每个选项的格式。I2C Transmit 模块将 R/W 位设置为 1。

S — 起始位

R/W — 读/写

ACK — 应答

P — 停止位

MSB — 最高有效位

LSB — 最低有效位

### **peripheral address source** — I2C 外设的外设地址来源 `Specify via dialog`（默认）| `Input port`

设置 I2C 外设的外设地址寄存器的方法。

### **Peripheral address register** — 外设地址寄存器值 `80`（默认）| 标量

根据所选的地址格式，输入 7 位或 10 位外设地址。

#### 依赖关系

此参数仅在 **Peripheral address source** 设置为 `Specify via dialog` 时出现。

### **Bit count** — 通信的位数 `8`（默认）| [1 8] 范围内的整数

I2C 模块接收的数据字节中的位数。

### **Enable stop condition** — 发送停止位以指示数据传输完成 `off`（默认）| `on`

当 I2C 模块配置为控制器时，I2C 模块向 I2C 总线发送停止位以指示数据传输完成。I2C 总线空闲，可供任何其他 I2C 模块发起读/写操作。

### **Enable repeat mode** — 重复传输数据直到检测到停止或起始条件 `off`（默认）| `on`

当您启用重复模式时，I2C 模块持续传输数据，直到检测到停止或起始条件。如果使用此模式，还应考虑选择 **Enable stop condition**，以确保在停止条件之后数据传输停止。

如果禁用重复模式，I2C 模块以标准模式运行，发送一次特定数量的数据值。

### **Output transmitting status** — 指示 I2C 发送模块何时传输消息 `off`（默认）| `on`

启用状态输出端口，该端口指示 I2C 发送模块何时传输消息。
## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

配置 inter-integrated circuit (I2C) 模块以将数据传输到 I2C 总线

I2C Transmit 模块配置 inter-integrated circuit (I2C) 模块以将数据传输到两线 I2C 串行总线。I2C Transmit 模块支持处理器与外部外设或其他控制器之间的 I2C 总线通信。该模块可以在外设模式或控制器模式下运行。

当 I2C 模块配置为控制器时，该模块从外设接收数据。当 I2C 模块配置为外设时，该模块从控制器接收数据。通过导航到 **Configuration Parameters** > **Hardware Implementation** > **Target hardware resources** 来配置 I2C 模块。

要从外设读取数据，请使用 I2C Transmit 模块将要读取的寄存器地址发送到外设。确保在使用 I2C Receive 模块从外设读取数据之前，数据已从 Tx FIFO 发送到外设。有关更多信息，请参阅 Using the I2C Bus to Access Sensors。
