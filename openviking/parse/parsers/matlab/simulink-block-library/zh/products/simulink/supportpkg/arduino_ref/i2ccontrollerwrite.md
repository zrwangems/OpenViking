---
type: simulink-block
title: 'I2C Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / I2C'
documentation_page: 'i2ccontrollerwrite'
documentation_source_path: 'supportpkg/arduino_ref/i2ccontrollerwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# I2C Write

## 端口

### 输入

### **Data** — 用于将数据写入 I2C 外设设备的输入端口 [1xN] 和 [Nx1] 数组

该输入端口将数据写入 I2C 外设设备或 I2C 外设设备寄存器。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Status** — 写操作的状态，标量

用于显示错误状态的输出端口。有关详细信息，请参阅 Output error status

#### 依赖项

仅当您选择 **Output error status** 参数时，此端口才会出现。

**数据类型:** `uint8`

## 参数

### **I2C module** — I2C 通信模块 `0`（默认） | 标量

指定 Arduino 硬件上用于与传感器外设通信的 I2C 模块。有关 Arduino 引脚映射以及硬件板支持的模块的详细信息，请参阅 Arduino 定时器无关模块的引脚映射。

### **Peripheral address** — I2C 外设设备的地址 10（默认） | 标量

输入要将数据写入的 I2C 外设设备地址。I2C 外设设备地址是 7 位地址。

使用 `hex2dec()` 将此地址指定为整数或十六进制格式，例如 hex2dec(‘20’)。

### **Peripheral byte order** — I2C 外设设备支持的字节顺序 `BigEndian`（默认） | `LittleEndian`

选择您的 I2C 外设支持的字节顺序，以写入数据。

两种字节顺序选项为：

- `BigEndian` — 最高有效字节先通过 I2C 总线写入。此选项为默认选项。
- `LittleEndian` — 最低有效字节先通过 I2C 总线写入。

### **Enable register access** — 用于启用写入 I2C 外设设备上的寄存器的选项 on（默认） | off

选中此复选框可将数据写入特定的 I2C 外设寄存器。

清除此参数时，将显示 **Remove stop bit at the end of data transfer** 参数。使用此参数，您可以根据需求修改写操作。有关详细信息，请参阅 I2C 通信支持。

### **Remove stop bit at the end of data transfer** — 用于在数据传输结束时移除 STOP 位的选项 off（默认） | on

清除此参数时，模块发送 STOP 条件。此条件表示模块已终止数据传输，并且 I2C 总线空闲，可供任何其他 I2C 控制器模块发起读/写操作。

选择此参数时，模块发送另一个 START 条件，后跟地址和读/写位。模块会递归地发送任意数量的 START 条件。此类重复 START 条件允许在不释放总线的情况下对外设设备执行写操作。其他控制器模块不会中断该操作。

#### 依赖项

仅当您清除 **Enable register access** 参数时，此参数才会出现。

### **Peripheral register address** — I2C 外设设备寄存器地址 0（默认）（默认） | 标量

输入要将数据写入的外设设备寄存器地址。

#### 依赖项

仅当您选择 **Enable register access** 参数时，此参数才启用。

### **Output error status** — 用于显示输出错误状态的选项 off（默认） | on

选择此选项以显示输出错误状态。选择此参数时，模块会配置一个输出端口。模块上的端口标记为 `Status`，表示模块在输出端口输出写操作的状态。

模块将状态输出为 `uint8` 值。每个值对应一种数据传输状态。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `BUS_ERROR` |
| `16` | `BUS_NOT_IN_USE` |

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2015b 中引入**

## 描述

将数据写入 I2C 外设设备或 I2C 外设设备寄存器

将数据写入 Arduino® 硬件上的 I2C 设备。使用此模块，您还可以将数据写入 I2C 外设上的特定寄存器。

点击 **查看引脚映射** 打开 Arduino 引脚映射表。

要了解如何为该模块分配引脚，请参阅 Arduino 定时器无关模块的引脚映射。
