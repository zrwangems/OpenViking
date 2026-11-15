---
type: simulink-block
title: 'I2C Controller Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Communication'
documentation_page: 'i2ccontrollerread'
documentation_source_path: 'supportpkg/raspberrypi_ref/i2ccontrollerread.html'
language: zh-CN
chinese_source: worker-translation
---

# I2C Controller Read

## 端口

### 输出

### **Data** — 用于从 I2C 外围设备读取数据的输出端口 [Nx1] 数组

用于从 I2C 外围设备读取数据的输出端口。端口发出的数据大小取决于 **Data size (N)** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Status** — 读操作的状态 标量

输出端口，用于显示错误状态。有关更多信息，请参阅 Output error status。

#### 依赖关系

此端口仅在您选择 **Output error status** 参数时出现。

**数据类型：** `uint8`

## 参数

### **Board** — 用于 I2C 通信的特定开发板 `Pi 2 Model B`（默认） | `Model B Rev1` | `Model B Rev2` | `Model B+` | `Pi 3 Model B` | `Pi 3 Model B+` | `Pi Zero W` | `Pi 4 Model B` | `Pi Zero 2 W` | `Compute Module 4` | `Pi 5 Model`

选择您正在使用的特定开发板。更改开发板会更新您获得的引脚选项。

### **I2C module** — I2C 通信模块 `1`（默认） | `0`

指定 Raspberry Pi® 硬件上用于与 I2C 外围设备通信的 I2C 模块。有关 Raspberry Pi 引脚映射和硬件开发板支持的模块的更多信息，请点击 **View pin map**。

要在您的 Raspberry Pi 硬件上启用辅助 I2C 总线，请按照 Enable Secondary I2C Bus of Raspberry Pi Hardware 中所述的步骤操作。

### **Peripheral address** — I2C 外围设备地址 `10`（默认） | scalar

输入要从中读取数据的 I2C 外围设备地址。您可以以十六进制格式 hex2dec() 指定此地址，例如 hex2dec(‘20')。

### **Peripheral byte order** — I2C 外围设备支持的字节顺序 `BigEndian`（默认） | `LittleEndian`

选择您的 I2C 外围设备支持的字节顺序。

两种字节顺序选项为：

- `BigEndian` — 在 I2C 总线上首先读取最高有效字节。此选项为默认选项。
- `LittleEndian` — 在 I2C 总线上首先读取最低有效字节。

### **Enable register address** — 用于启用从 I2C 外围设备寄存器读取的选项 `on`（默认） | `off`

选中此复选框可启用从 I2C 外围设备上的特定寄存器读取数据。

当您清除此参数时，会显示 **Send NACK at the end of data transfer** 和 **Remove stop bit at the end of data transfer** 参数。使用这些参数，您可以根据需求修改读取操作。

### **Peripheral register address** — 要读取数据的 I2C 外围设备寄存器地址 0（默认） | scalar

输入要从中读取数据的外围设备寄存器地址。

使用 `hex2dec()` 将此地址指定为整数或十六进制格式，例如 hex2dec(‘20’)。

#### 依赖关系

仅当您选择 **Enable register access** 参数时，此参数才会启用。

### **Data type** — 要从 I2C 外围设备读取的数据类型 uint8（默认） | int8 | int16 | uint16 | int32 | uint32 | single | double

选择要从 I2C 外围设备读取的数据类型。

### **Send NACK at the end of data transfer** — 在数据传输结束时发送 Not Acknowledge 位的选项 off（默认） | on

当您选择此参数时，I2C Controller Read 模块会在最后一个字节向 I2C 外围设备发送 NACK（Not Acknowledge）位。

当外围设备接收到 NACK 时，它会等待来自 I2C Controller Read 模块的 STOP 条件。控制器模块会生成 STOP 条件以中止传输，或生成重复的 START 条件以启动新传输。

当您清除此参数时，I2C Controller Read 模块会在每个字节结束时向外围设备发送 ACK（Acknowledge）位。ACK 表示 I2C Controller Read 模块已准备好从外围设备读取下一个字节。

#### 依赖关系

此参数仅在您清除 **Enable register access** 参数时出现。

### **Remove stop bit at the end of data transfer** — 在数据传输结束时移除 STOP 位的选项 off（默认） | on

当您清除此参数时，模块会发送 STOP 条件。此条件表示模块已终止数据传输，并且 I2C 总线可自由供任何其他 I2C 控制器模块启动新的读/写操作。

当您选择此参数时，模块会发送另一个 START 条件，后跟地址和读/写位。模块会递归地发送任意数量的 start 条件。这种重复的 START 条件允许在不释放总线的情况下向外围设备执行写操作。没有其他控制器模块会中断该操作。

#### 依赖关系

此参数仅在您清除 **Enable register access** 参数时出现。

### **Data size (N)** — 要从 I2C 外围设备读取的数据大小 1（默认） | scalar

输入要针对所选数据类型从 I2C 外围设备读取的数据大小。

### **Output error status** — 用于在数据传输期间显示错误状态的选项 off（默认） | on

选择此选项可在数据传输期间显示错误状态。

当您选择 **Output error status** 参数时，模块会配置一个输出端口。模块上的该端口标记为 `Status`，表示模块在输出端口输出读操作的状态。

模块将状态输出为 `uint8` 值。每个值对应一种数据传输状态。

| 状态值 | 状态描述 |
| --- | --- |
| `0` | `SUCCESS` |
| `1` | `BUSY` |
| `2` | `ARBITRATION_LOST` |
| `4` | `NO_ACKNOWLEDGE` |
| `8` | `BUS_ERROR` |
| `16` | `BUS_NOT_IN_USE` |

### **Sample time** — 模块读取数据的时间频率 0.1（默认） | scalar

指定此模块从 I2C 外围设备读取数据的频率。输入大于零的值。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Communication

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017a 中引入**

## 描述

从 I2C 外围设备或 I2C 外围设备寄存器读取数据

从 I2C 外围设备读取串行数据。使用此模块，您还可以从 I2C 外围设备上的特定寄存器读取数据。

有关 I2C 通信的更多信息，请参阅 Support I2C Communication 和 Raspberry Pi I2C Interface。

要打开 Raspberry Pi 开发板的引脚映射，请点击 **View pin map** 按钮。
