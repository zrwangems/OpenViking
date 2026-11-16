---
type: simulink-block
title: 'I2C Master Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Communication'
documentation_page: 'i2ccontrollerread'
documentation_source_path: 'beagleboneblue/ref/i2ccontrollerread.html'
language: zh-CN
chinese_source: worker-translation
---

# I2C Master Read

## 端口

### 输出

### **Data** — 用于从 I2C 外设设备读取数据的输出端口 [Nx1] 数组

用于从 I2C 外设设备读取数据的输出端口。该端口发出的数据大小基于 **Data size (N)** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Status** — 读取操作的状态 scalar

输出端口，用于显示错误状态。有关详细信息，请参阅 Output error status。

#### 依赖关系

此端口仅在您选择 **Output error status** 参数时出现。

**数据类型：** `uint8`

## 参数

### **Peripheral address** — I2C 外设设备地址 10 (default) | scalar

输入要从其读取数据的 I2C 外设设备地址。您可以使用十六进制格式 hex2dec() 指定此地址，例如 hex2dec(‘10')。

### **Peripheral byte order** — I2C 外设设备支持的字节顺序 BigEndian (default) | LittleEndian

选择您的 I2C 外设支持的字节顺序。

两种字节顺序选项为：

- Big Endian — 首先通过 I2C 总线读取最高有效字节。此选项为默认选项。
- Little Endian — 首先通过 I2C 总线读取最低有效字节。

### **Enable register address** — 用于启用从 I2C 外设寄存器读取的选项 On (default) | Off

选中此复选框可启用从 I2C 外设设备上的特定寄存器读取数据。

清除此参数时，将显示 **Send NACK at the end of data transfer** 和 **Remove stop bit at the end of data transfer** 参数。使用这些参数，您可以根据需求修改读取操作。

### **Send NACK at the end of data transfer** — 用于在数据传输结束时发送 Not Acknowledge 位的选项 off (default) | on

当您选择此参数时，I2C Controller Read 模块会在最后一个字节时向 I2C 外设设备发送 NACK（Not Acknowledge）位。

当 I2C 外设设备接收到 NACK 时，它会等待来自 I2C 控制器模块的 STOP 条件。控制器模块会生成 STOP 条件以中止传输，或生成重复 START 条件以开始新的传输。

当您清除此参数时，I2C Controller Read 模块会在每个字节结束时向 I2C 外设设备发送 ACK（Acknowledge）位。ACK 表示 I2C Controller Read 模块已准备好从 I2C 外设设备读取下一个字节。

#### 依赖关系

此参数仅在您清除 **Enable register access** 参数时出现。

### **Remove stop bit at the end of data transfer** — 用于在数据传输结束时移除 STOP 位的选项 off (default) | on

当您清除此参数时，模块会发送 STOP 条件。此条件表示模块已终止数据传输，并且 I2C 总线空闲，可供任何其他 I2C 控制器模块发起新的读/写操作。

当您选择此参数时，模块会发送另一个 START 条件，后跟地址和读/写位。模块会递归地发送任意数量的 START 条件。这种重复 START 条件允许在不释放总线的情况下对 I2C 外设设备执行写操作。没有其他控制器模块会中断该操作。

#### 依赖关系

此参数仅在您清除 **Enable register access** 参数时出现。

### **Peripheral register address** — 要读取数据的 I2C 外设设备寄存器地址 0 (default) | scalar

输入要从中读取数据的外设设备寄存器地址。

将此地址指定为整数，或使用 `hex2dec()` 以十六进制格式指定，例如 hex2dec(‘10’)。

#### 依赖关系

此参数仅在您选择 **Enable register access** 参数时启用。

### **Data type** — 要从 I2C 外设设备读取的数据类型 uint8 (default) | int8 | int16 | uint16 | int32 | uint32 | single | double

选择要从 I2C 外设设备读取的数据类型。

### **Data size (N)** — 要从 I2C 外设设备读取的数据大小 1 (default) | scalar

输入要针对所选数据类型从 I2C 外设设备读取的数据大小。

### **Output error status** — 用于在数据传输期间显示错误状态的选项 Off (default) | On

选择此选项可在数据传输期间显示错误状态。

当您选择 **Output error status** 参数时，模块会配置一个输出端口。模块上的该端口标记为 `Status`，表示模块在输出端口输出读取操作的状态。

模块将状态输出为 `uint8` 值。每个值对应一种数据传输状态。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `BUS_ERROR` |
| `16` | `BUS_NOT_IN_USE` |

### **Sample time** — 模块读取数据的频率 0.1 (default) | scalar

指定此模块从 I2C 外设读取数据的频率。输入大于零的值。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Communication

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

从 I2C 外设设备或 I2C 外设设备寄存器读取数据

从 I2C 外设读取串行数据。使用此模块，您还可以从 I2C 外设设备上的特定寄存器读取数据。

有关 I2C 通信的详细信息，请参阅 Support I2C Communication。

要打开 BeagleBone® Blue 板的引脚图，请点击 **View pin map** 按钮。
