---
type: simulink-block
title: 'C28x I2C Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'c28xi2creceive'
documentation_source_path: 'ref/c28xi2creceive.html'
language: zh-CN
chinese_source: worker-translation
---

# C28x I2C Receive

## 端口
```yaml
ports:
- name: SAR
  summary: 外设地址寄存器值 标量
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: RD
  summary: 从 I2C 总线接收的数据 标量 | 向量
  direction: output
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32
- name: status
  summary: I2C 通信状态 标量
  direction: output
  data_types: uint16
```

### 输入

### **SAR** — 外设地址寄存器值 标量

外设地址寄存器值。

#### 依赖

此端口仅在 **Peripheral address source** 设置为 `Input port` 时出现。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`
### 输出

### **RD** — 从 I2C 总线接收的数据 标量 | 向量

从 I2C 总线读取的数据。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **status** — I2C 通信状态 标量

来自 I2C 状态寄存器 (I2CSTR) 的状态值。

#### 依赖

此端口仅在选中 **Output receiving status** 时出现。

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
- name: Peripheral address source
  summary: I2C 外设的外设地址来源 Specify via dialog（默认）| Input port
  group: ''
- name: Peripheral address register
  summary: 外设地址寄存器值 80（默认）| 标量
  group: ''
- name: Bit count
  summary: 通信的位数 8（默认）| [1 8] 范围内的整数
  group: ''
- name: Read data length
  summary: 接收数据的长度 1（默认）| 标量
  group: ''
- name: Initial output
  summary: I2C 节点输出到模型的值 0（默认）| 标量 | 向量
  group: ''
- name: Set NACK bit
  summary: I2C 应答周期期间的 NACK 位 off（默认）| on
  group: ''
- name: Enable stop condition
  summary: 向 I2C Transmit 模块发送停止消息 off（默认）| on
  group: ''
- name: Output receiving status
  summary: 指示 I2C Receive 模块何时接收到消息 off（默认）| on
  group: ''
- name: Sample time
  summary: 从 I2C 设备读取数据的频率 0.001（默认）| –1 | 标量
  group: ''
- name: Data type
  summary: 数据向量中的数据类型 int8（默认）| uint8 | int16 | uint16 | int32 | uint32
  group: ''
```

### **Module** — 用于通信的模块 `I2C_A`（默认）| `I2C_B`

用于通信的 I2C 模块。不同 C2000™ 处理器支持的 I2C 模块数量有所不同。

### **Addressing format** — 通信的地址格式 `7–Bit addressing`（默认）| `10–Bit addressing` | `Free data format`

通信的地址格式。下图显示了每个选项的格式。I2C Receive 模块将 R/W 位设置为 0。

S — 起始位

R/W — 读/写

ACK — 应答

P — 停止位

MSB — 最高有效位

LSB — 最低有效位

### **Peripheral address source** — I2C 外设的外设地址来源 `Specify via dialog`（默认）| `Input port`

设置 I2C 外设的外设地址寄存器的方法。

### **Peripheral address register** — 外设地址寄存器值 `80`（默认）| 标量

根据所选的地址格式，输入 7 位或 10 位外设地址。

#### 依赖

此参数仅在 **Peripheral address source** 设置为 `Specify via dialog` 时出现。

### **Bit count** — 通信的位数 `8`（默认）| [1 8] 范围内的整数

I2C 模块接收的数据字节中的位数。

### **Read data length** — 接收数据的长度 `1`（默认）| 标量

模块接收的 **Data type** 的数量（不是字节数）。如果此参数设置为大于 `1` 的值，则输出将为向量。

### **Initial output** — I2C 节点输出到模型的值 `0`（默认）| 标量 | 向量

I2C 节点在接收到数据之前输出到模型的值。默认情况下，如果未接收到 I2C 值，模块输出 `0`。

### **Set NACK bit** — I2C 应答周期期间的 NACK 位 `off`（默认）| `on`

在 I2C 应答周期期间生成无应答位 (NACK)，并忽略来自发送 I2C 节点的新位。

### **Enable stop condition** — 向 I2C Transmit 模块发送停止消息 `off`（默认）| `on`

使 I2C Receive 模块（控制器）能够向 I2C Transmit 模块（外设）发送停止消息。

### **Output receiving status** — 指示 I2C Receive 模块何时接收到消息 `off`（默认）| `on`

启用状态输出端口，该端口指示 I2C Receive 模块何时接收到消息。

### **Sample time** — 从 I2C 设备读取数据的频率 `0.001`（默认）| `–1` | 标量

模块的采样时间，以秒为单位。要异步执行此模块，请将此参数设置为 `-1`。

### **Data type** — 数据向量中的数据类型 `int8`（默认）| `uint8` | `int16` | `uint16` | `int32` | `uint32`

设置所接收数据的数据类型。如果接收数据的大小小于 8 位，则数据右对齐。
## 所属库

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

配置 inter-integrated circuit (I2C) 模块以从 I2C 总线接收数据

I2C Receive 模块配置 inter-integrated circuit (I2C) 模块以从两线 I2C 串行总线接收数据。I2C Receive 模块支持处理器与外部外设或其他控制器之间的 I2C 总线通信。该模块可以在外设模式或控制器模式下运行。

当 I2C 模块配置为控制器时，该模块从外设接收数据。当 I2C 模块配置为外设时，该模块从控制器接收数据。通过导航到 **Configuration Parameters** > **Hardware Implementation** > **Target hardware resources** 来配置 I2C 模块。

要从外设读取数据，请使用 I2C Transmit 模块将要读取的寄存器地址发送到外设。确保在通过 I2C Receive 模块从外设读取数据之前，数据已从 Tx FIFO 发送到外设。有关详细信息，请参阅 Using the I2C Bus to Access Sensors。
