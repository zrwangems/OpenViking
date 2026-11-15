---
type: simulink-block
title: 'I2C Controller Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'i2ccontrollerwrite'
documentation_source_path: 'supportpkg/raspberrypi_ref/i2ccontrollerwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# I2C Controller Write

## 端口

### 输入

### **Data** — 用于将数据写入 I2C 外设设备或 I2C 外设设备寄存器的输入端口 [1xN] 和 [Nx1] 数组

该输入端口将数据写入 I2C 外设设备或 I2C 外设设备寄存器。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **Status** — 写操作的状态标量

用于显示错误状态的输出端口。有关更多信息，请参阅 Output error status。

#### 依赖关系

仅当您选择 **Output error status** 参数时，此端口才会出现。

**数据类型：** `uint8`

## 参数

### **Board** — 用于 I2C 通信的特定开发板 `Pi 2 Model B`（默认） | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

选择您正在使用的特定开发板。更改开发板会更新您可获得的引脚选项。

### **I2C module** — I2C 通信模块 `1`（默认） | `0`

指定 Raspberry Pi® 硬件上的 I2C 模块，以与 I2C 外设通信。有关 Raspberry Pi 引脚映射以及硬件开发板支持的模块的更多信息，请单击 **View pin map**。

要在您的 Raspberry Pi 硬件上启用辅助 I2C 总线，请按照 Enable Secondary I2C Bus of Raspberry Pi Hardware 中提到的步骤操作。

### **Peripheral address** — I2C 外设设备的地址 `10`（默认） | 标量

输入要向其写入数据的 I2C 外设设备地址。I2C 外设设备地址是一个 7 位地址。

将此地址指定为整数，或使用 `hex2dec()` 以十六进制格式指定，例如 hex2dec(‘61’)。

### **Peripheral byte order** — I2C 外设设备支持的字节顺序 `BigEndian`（默认） | `LittleEndian`

选择您的 I2C 外设支持的字节顺序。

两种字节顺序选项为：

- `BigEndian` — 最高有效字节先通过 I2C 总线写入。此选项是默认选项。
- `LittleEndian` — 最低有效字节先通过 I2C 总线写入。

### **Enable register access** — 用于启用写入 I2C 外设设备上的寄存器的选项 on（默认） | off

选中此复选框以将数据写入特定的 I2C 外设寄存器。

清除此参数后，将显示 **Send NACK at the end of data transfer** 和 **Remove stop bit at the end of data transfer** 参数。使用这些参数，您可以根据需求修改写操作。有关更多信息，请参阅 I2C Register Read/Write。

### **Peripheral register address** — I2C 外设设备寄存器地址 0（默认）（默认） | 标量

输入要向其写入数据的外设设备寄存器地址。

#### 依赖关系

仅当您选择 **Enable register access** 参数时，此参数才会启用。

### **Send NACK at the end of data transfer** — 用于在数据传输结束时发送 Not Acknowledge 位的选项 off（默认） | on

选择此参数时，I2C Controller Write 模块会随最后一个字节向外设设备发送一个 NACK（Not Acknowledge）位。

当外设设备收到 NACK 时，它会等待来自 I2C Controller Write 模块的 STOP 条件。控制器模块会生成 STOP 条件以中止传输，或生成重复 START 条件以开始新传输。

清除此参数时，I2C Controller Write 模块会在每个字节结束时向外设设备发送一个 ACK（Acknowledge）位。ACK 表示 I2C Controller Write 模块已准备好从外设设备读取下一个字节。

#### 依赖关系

仅当您清除 **Enable register access** 参数时，此参数才会出现。

### **Remove stop bit at the end of data transfer** — 用于在数据传输结束时移除 STOP 位的选项 off（默认） | on

清除此参数时，模块会发送一个 STOP 条件。此条件表示模块已终止数据传输，并且 I2C 总线可供任何其他 I2C 控制器模块发起读/写操作。

选择此参数时，模块会发送另一个 START 条件，后跟地址和读/写位。模块会递归地发送任意数量的 START 条件。此类重复 START 条件允许在不释放总线的情况下对外设设备执行写操作。没有其他控制器模块会中断该操作。

#### 依赖关系

仅当您清除 **Enable register access** 参数时，此参数才会出现。

### **Output error status** — 用于显示输出错误状态的选项 off（默认） | on

选择此选项以显示输出错误状态。选择此参数时，模块会配置一个输出端口。模块上的该端口标记为 `Status`，表示模块在输出端口处输出写操作的状态。

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

Simulink Support Package for Raspberry Pi Hardware / Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

将数据写入 I2C 外设设备或 I2C 外设设备寄存器

将数据写入 I2C 外设设备或 I2C 外设设备寄存器。使用此模块，您还可以将数据写入 I2C 外设上的特定寄存器。

有关 I2C 通信的更多信息，请参阅支持 I2C 通信和 Raspberry Pi I2C 接口。要打开 Raspberry Pi 开发板的引脚映射，请单击 **View pin map**。
