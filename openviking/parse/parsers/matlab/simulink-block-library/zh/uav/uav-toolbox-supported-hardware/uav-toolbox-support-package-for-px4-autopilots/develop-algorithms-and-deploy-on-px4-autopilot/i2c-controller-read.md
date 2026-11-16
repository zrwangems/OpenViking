---
type: simulink-block
title: 'I2C Controller Read'
family: 'uav'
product_id: 'uav'
product_name: 'UAV Toolbox'
documentation_release: R2025b
official_category: 'UAV Toolbox Supported Hardware / UAV Toolbox Support Package for PX4 Autopilots / Develop Algorithms and Deploy on PX4 Autopilot'
documentation_page: 'i2ccontrollerread'
documentation_source_path: 'px4/ref/i2ccontrollerread.html'
language: zh-CN
chinese_source: worker-translation
---

# I2C Controller Read

## 端口

### 输出

### **Data** — 来自 I2C 外设设备的数据向量

此端口从连接到板卡的 I2C 设备读取向量数据。数据大小是您在 **Data size** 参数中指定的值。

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `single` | `double`

### **Status** — 读取操作的状态标量

当您选择 **Output error status** 参数时，会提供一个标记为 `Status` 的输出端口。

此端口输出以下值之一：

- `0` 表示读取操作成功。
- `1` 表示打开总线失败。
- `2` 表示读取操作失败。

**Data Types:** `uint8`

## 参数

### **I2C Bus** — 用于读取数据的 I2C 总线 `1`（默认）

指定板卡上用于从 I2C 外设设备读取数据的 I2C 总线。

### **Peripheral address** — 要从中读取数据的 I2C 寄存器外设地址 `10`（默认） | 非负整数

指定要读取数据的 I2C 外设地址。您可以使用 `hex2dec()` 以十六进制格式指定此地址，例如 `0x20`。

### **Peripheral byte order** — I2C 外设设备支持的字节顺序 `BigEndian`（默认） | `LittleEndian`

2 字节顺序选项包括：

- `BigEndian` - 最高有效字节先通过 I2C 总线发送。
- `LittleEndian` - 最低有效字节先通过 I2C 总线发送。

### **Enable register access** — 从特定 I2C 外设寄存器读取的选项 `on`（默认） | `off`

当您选择此参数时，模块会从您在 **Peripheral register address** 参数中指定的 I2C 外设寄存器读取数据。

### **Peripheral register address** — 要读取数据的 I2C 外设寄存器地址 `2`（默认） | `integer between 0 and 255`

指定要读取数据的 I2C 寄存器地址。

请将该地址指定为整数，或使用 `hex2dec()` 以十六进制格式指定，例如 `0x20`。

#### 依赖关系

要启用此参数，请选择 **Enable register access** 参数。

### **Data type** — 来自 I2C 外设设备的数据的数据类型 `uint8`（默认） | `int8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double`

选择您要从 I2C 外设设备读取时使用的数据类型。

### **Data size (N)** — 要从 I2C 外设设备读取的数据大小 `1`（默认） | `nonnegative integer`

指定要针对所选数据类型从 I2C 外设设备读取的数据大小。

### **Output error status** — 在数据传输期间显示错误状态的选项 `off`（默认） | `on`

当您选择此参数时，会提供一个标记为 `Status` 的输出端口。

此端口输出以下值之一：

- `0` 表示读取操作成功。
- `1` 表示打开总线失败。
- `0` 表示读取或写入操作失败。

### **Sample time** — 从 I2C 外设设备读取数据的频率 `0.01`（默认）

指定 I2C Controller Read 模块从 I2C 外设设备读取数据的频率。当您将此参数指定为 `-1` 时，模块会根据模型中该模块的上下文继承其采样时间。

## 所属库

UAV Toolbox Support Package for PX4 Autopilots

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

R2025b 中未记录。

## 描述

从 I2C 外设设备或 I2C 外设设备寄存器读取数据

I2C Controller Read 模块从连接到板卡的 I2C 外设设备读取串行数据。使用此模块，您可以从 I2C 外设设备上的特定寄存器读取数据。

要查看总线编号与硬件板上的端口标签之间的映射，请点击 **View I2C Bus map**。有关总线映射的更多信息，请参阅 PX4 Autopilots 上标签的 I2C 总线端口编号。

在 Normal 模式仿真期间，模块输出零。

在 Connected I/O 仿真期间，此模块从硬件的外设读取数据。
