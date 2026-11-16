---
type: simulink-block
title: 'I2C Controller Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-KL25Z Board / Modeling'
documentation_page: 'i2ccontrollerread'
documentation_source_path: 'freedomboard/ref/i2ccontrollerread.html'
language: zh-CN
chinese_source: worker-translation
---

# I2C Controller Read

## 端口

### 输出

### **Data** — 该模块从 I2C 外设设备读取的数据向量

该模块从板上的 I2C 设备读取向量数据。数据大小是您在 **Data size** 参数中指定的值。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

### **Status** — 读取操作的状态标量

当您选中 **Output error status** 参数时，该模块会配置一个输出端口。模块上的该端口标记为 `Status`，表示该模块在输出端口处输出读取操作的状态。

该模块将状态输出为 `uint8` 值。每个值对应一种数据传输状态。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `I2C_BUS_ERROR` |

**数据类型：** `uint8`

## 参数

### **I2C module** — 要读取数据的 I2C 模块 `0`（默认）| 1

指定板上要从中读取 I2C 外设设备数据的 I2C 模块。

### **Peripheral address** — 要从中读取数据的 I2C 寄存器外设地址 `10`（默认）| `integer between 0 and 127`

指定要从中读取数据的 I2C 外设地址。您可以用十六进制格式 `hex2dec()` 指定该地址，例如，‘hex2dec(‘20’)’。

### **Peripheral byte order** — I2C 外设设备支持的字节排序 `BigEndian`（默认）| `LittleEndian`

2 字节排序选项包括：

- BigEndian - 最高有效字节首先通过 I2C
  总线发送。
- LittleEndian - 最低有效字节首先通过
  I2C 总线发送。

### **Enable register access** — 从特定 I2C 外设寄存器读取的选项 on（默认）| off

当您选中此参数时，该模块从您在 **Peripheral register address** 参数中指定的 I2C 外设寄存器读取数据。

当您清除此参数时，将显示 **Send NACK at the end of data transfer** 和 **Remove stop bit at the end of data transfer** 参数。使用这些参数，您可以根据需求修改读取操作。

### **Peripheral register address** — 要读取数据的 I2C 外设寄存器地址 `0`（默认）| `integer between 0 and 255`

指定要从中读取数据的 I2C 寄存器地址。

将该地址指定为整数，或使用 `hex2dec()` 以十六进制格式指定，例如，‘hex2dec(‘20’)’。

有关寄存器读/写的详细信息，请参阅 I2C Register Read/Write。

#### 依赖关系

此参数仅在您选中 **Enable register access** 参数时出现。

### **Data size (N)** — 要从 I2C 外设设备读取的数据大小 `1`（默认）| `integer greater than or equal to 0`

指定要为所选数据类型从 I2C 外设设备读取的数据大小。

### **Data type** — 来自 I2C 外设设备的数据的数据类型 `uint8`（默认）| `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

选择要从 I2C 外设设备读取的数据类型。

### **Send NACK at the end of data transfer** — 在数据传输结束时发送 Not Acknowledge 位的选项 off（默认）| on

当您选中此参数时，I2C Controller Read 模块会将 NACK（Not Acknowledge）位与最后一个字节一起发送到外设设备。

当外设设备收到 NACK 时，它会等待来自 I2C Controller 模块的 STOP 条件。Controller 模块生成 STOP 条件以中止传输，或生成重复 START 条件以开始新传输。

当您清除此参数时，I2C Controller Read 模块在每个字节结束时向外设设备发送 ACK（Acknowledge）位。ACK 表示 I2C Controller Read 模块已准备好从外设设备读取下一个字节。

#### 依赖关系

此参数仅在您清除 **Enable register access** 参数时出现。

### **Remove stop bit at the end of data transfer** — 在数据传输结束时移除 STOP 位的选项 off（默认）| on

当您清除此参数时，该模块发送 STOP 条件。此条件表示该模块已终止数据传输，并且 I2C 总线空闲，可供任何其他 I2C Controller 模块启动新的读/写操作。

当您选中此参数时，该模块发送另一个 START 条件，后跟地址和读/写位。该模块递归地发送任意数量的 START 条件。这样的重复 START 条件允许在不释放总线的情况下对外设设备执行写操作。其他 Controller 模块不会中断该操作。

#### 依赖关系

此参数仅在您清除 **Enable register access** 参数时出现。

### **Output error status** — 在数据传输期间显示错误状态的选项 off（默认）| on

当您选中此参数时，该模块会配置一个输出端口。模块上的该端口标记为 `Status`，表示该模块在输出端口处输出写操作的状态。

该模块将状态输出为 `uint8` 值。每个值对应一种数据传输状态。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `I2C_BUS_ERROR` |

### **Sample time** — 从 I2C 外设设备读取数据的频率 `0.1`（默认）

指定 I2C Controller Read 模块从 I2C 外设设备读取数据的频率。当您将此参数指定为`-1`时，该模块会根据模型中该模块的上下文继承其采样时间。

## 所属库

Simulink Coder Support Package for NXP FRDM-KL25Z Board/FRDM-KL25Z

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

从 I2C 外设设备或 I2C 外设设备寄存器读取数据

I2C Controller Read 模块从连接到板上的 I2C 外设设备读取串行数据。使用此模块，您可以从 I2C 外设设备上的特定寄存器读取数据。

有关 I2C 通信的详细信息，请参阅 Support I2C Communication。
