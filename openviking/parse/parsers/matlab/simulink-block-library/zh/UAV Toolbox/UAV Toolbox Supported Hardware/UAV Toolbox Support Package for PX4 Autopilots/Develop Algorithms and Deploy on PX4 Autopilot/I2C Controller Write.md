---
type: simulink-block
title: 'I2C Controller Write'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'i2ccontrollerwrite'
documentation_source_path: 'px4/ref/i2ccontrollerwrite.html'
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

选择 **Output error status** 参数后，将有一个标记为 `Status` 的输出端口可用。

该端口输出以下值之一：

- `0` 表示写操作成功。
- `1` 表示打开总线失败。
- `2` 表示写操作失败。

**数据类型：** `uint8`

## 参数

### **I2C Bus** — 板上 I2C 外设设备连接到的 I2C 总线，取值为 `1`（默认值） | `nonnegative integer`

指定板上用于向 I2C 外设设备写入数据的 I2C 总线。

### **Peripheral address** — 要写入数据的 I2C 外设地址 `10`（默认值）

指定要写入数据的 I2C 外设地址。I2C 外设设备地址是 7 位地址。

请将该地址指定为整数，或使用 `hex2dec()` 以十六进制格式指定，例如 `0x61`。

### **Peripheral byte order** — I2C 外设设备支持的字节序 `BigEndian`（默认值） | `LittleEndian`

2 字节排序选项包括：

- `BigEndian` - 最高有效字节先通过 I2C 总线发送。
- `LittleEndian` - 最低有效字节先通过 I2C 总线发送。

### **Enable register access** — 用于写入特定 I2C 外设寄存器的选项 on（默认值） | off

选择此参数后，模块会将数据写入 **Peripheral register address** 参数中指定的 I2C 外设寄存器。

### **Peripheral register address** — 要写入数据的 I2C 外设寄存器地址 `uint8(1)`（默认值）

指定要写入数据的 I2C 外设寄存器地址。

请以 8 位无符号整数或十六进制格式指定该地址。要以 8 位无符号整数指定该地址，请使用 `uint8()`，例如 ‘`uint8(20)`’。要以十六进制格式指定该地址，请使用 `hex2dec()`，例如 `0x20`。

#### 依赖关系

仅当选择 **Enable register access** 参数时，此参数才会显示。

### **Output error status** — 用于在数据传输期间显示错误状态的选项 `off`（默认值） | `on`

选择此参数后，将有一个标记为 `Status` 的输出端口可用。

该端口输出写操作的状态。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

未在 R2025b 中记录。

## 描述

将数据写入 I2C 外设设备或 I2C 外设设备寄存器

I2C Controller Write 模块将数据写入连接到板上的 I2C 外设设备。使用此模块，您可以将数据写入 I2C 外设设备上的特定寄存器。

要查看硬件板上总线编号与端口标签之间的映射，请单击 **View I2C Bus map**。有关总线映射的更多信息，请参阅 PX4 Autopilots 上标签的 I2C 总线端口编号。

在 Connected I/O 仿真期间，此模块将数据写入硬件的各外设。
