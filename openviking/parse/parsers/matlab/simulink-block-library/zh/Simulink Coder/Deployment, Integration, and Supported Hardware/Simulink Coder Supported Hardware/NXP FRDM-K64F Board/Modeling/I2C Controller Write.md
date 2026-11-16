---
type: simulink-block
title: 'I2C Controller Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / NXP FRDM-K64F Board / Modeling'
documentation_page: 'i2ccontrollerwrite'
documentation_source_path: 'freescalefrdmk64fboard/ref/i2ccontrollerwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# I2C Controller Write

## 端口

### 输入

### **Data** — 要写入 I2C 外设设备的数据 标量 | 向量

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`
### 输出

### **Status** — 写操作的状态 标量

选中 **Output error status**
参数时，模块会配置一个输出端口。模块上的该端口标记为 `Status`，表示模块在输出端口输出写操作的状态。

模块以 `uint8` 值形式输出状态。每个值对应一种数据传输状态。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `4` | `NO_ACKNOWLEDGE` |

**数据类型：** `uint8`

## 参数

### **I2C module** — 要写入数据的 I2C 模块 `0` (默认) | 1

指定板上要从其向 I2C 外设设备写入数据的 I2C 模块。

### **Peripheral address** — 要向其写入数据的 I2C 外设地址 `10` (默认) | `integer between 0 and 127`

指定要将数据写入到的 I2C 外设地址。I2C 外设设备地址是 7 位地址。

使用 `hex2dec()` 将该地址指定为整数或十六进制格式，例如，`hex2dec(‘61’)`。

### **Peripheral byte order** — I2C 外设设备支持的字节排序 `BigEndian` (默认) | `LittleEndian`

2 字节排序选项包括：

- BigEndian - 最高有效字节先通过 I2C 总线发送。
- LittleEndian - 最低有效字节先通过 I2C 总线发送。

### **Enable register access** — 用于写入特定 I2C 外设寄存器的选项 on (默认) | off

选中此参数时，模块将数据写入到你在 **Peripheral register address** 参数中指定的 I2C 外设寄存器。

清除此参数时，将显示 **Send NACK at the end of data transfer** 和 **Remove stop bit at the end of data transfer** 参数。使用这些参数，你可以根据需要修改写操作。

### **Peripheral register address** — 要写入数据的 I2C 外设寄存器地址 `0` (默认) | `integer between 0 and 255`

指定要将数据写入到的 I2C 外设寄存器地址。

使用 `hex2dec()` 将该地址指定为整数或十六进制格式，例如，`hex2dec(‘20’)`。

有关寄存器读/写的详细信息，请参阅 I2C 寄存器读/写。

#### 依赖关系

此参数仅在选中 **Enable register access** 参数时显示。

### **Send NACK at the end of data transfer** — 在数据传输结束时发送 Not Acknowledge 位的选项 off (默认) | on

选中此参数时，I2C Controller Write 模块将随最后一个字节向外设设备发送 NACK（Not Acknowledge）位。

当外设设备收到 NACK 后，它会等待来自 I2C Controller 模块的 STOP 条件。Controller 模块会生成用于中止传输的 STOP 条件，或用于启动新传输的重复 START 条件。

清除此参数时，I2C Controller Write 模块会在每个字节结束时向外设设备发送 ACK（Acknowledge）位。ACK 表示 I2C Controller Write 模块已准备好从外设设备读取下一个字节。

#### 依赖关系

此参数仅在清除 **Enable register access** 参数时显示。

### **Remove stop bit at the end of data transfer** — 在数据传输结束时移除 STOP 位的选项 off (默认) | on

清除此参数时，模块会发送 STOP 条件。此条件表示模块已终止数据传输，并且 I2C 总线空闲，可供任何其他 I2C Controller 模块发起读/写操作。

选中此参数时，模块会发送另一个 START 条件，后跟地址和读/写位。模块会递归地发送任意数量的 START 条件。此类重复 START 条件允许在不释放总线的情况下向外设设备执行写操作。其他 Controller 模块不会中断该操作。

#### 依赖关系

此参数仅在清除 **Enable register access** 参数时显示。

### **Output error status** — 在数据传输期间显示错误状态的选项 off (默认) | on

选中此参数时，模块会配置一个输出端口。模块上的该端口标记为 `Status`，表示模块在输出端口输出写操作的状态。

模块以 `uint8` 值形式输出状态。每个值对应一种数据传输状态。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `4` | `NO_ACKNOWLEDGE` |

## 所属库

Simulink Coder Support Package for NXP FRDM-K64F Board

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016b 中引入**

## 描述

将数据写入 I2C 外设设备或 I2C 外设设备寄存器

I2C Controller Write 模块将数据写入连接到板的 I2C 外设设备。使用此模块，你可以将数据写入 I2C 外设设备上的特定寄存器。

有关 I2C 通信的详细信息，请参阅支持 I2C 通信。
