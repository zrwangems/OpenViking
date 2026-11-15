---
type: simulink-block
title: 'I2C Register Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Communication Protocol Blocks'
documentation_page: 'i2cregisterread'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/i2cregisterread.html'
language: zh-CN
chinese_source: worker-translation
---

# I2C Register Read

## 端口

### 输出

### **Data** — 输出数据向量

模块将控制器从外设设备或外设设备寄存器读取的数据输出为 *N*×1 向量，其中 *N* 表示数据大小。

**数据类型：** `uint8` | `uint16` | `uint32`

### **Status** — 控制器读取操作的状态 `0` | `1`

模块输出控制器对外设设备或外设设备寄存器执行读取操作的状态。

- `0`：表示读取操作成功，这意味着 **Data** 端口上接收到的数据有效。
- `1`：表示读取操作未成功，这意味着 **Data** 端口上接收到的数据无效。

#### 依赖关系

要启用此端口，请选择 **输出错误状态**。

**数据类型：** `uint8`

## 参数

### **EV3 brick 输入端口号** — 连接到外设设备的输入端口 `4`（默认）| `1` | `2` | `3`

选择外设设备所连接的 EV3 brick 上的输入端口。硬件上有四个端口，您可以选择其中任意一个端口。如果连接多个外设设备，请为每个外设设备指定唯一的端口。

### **外设地址** — I2C 外设设备地址或标识符 `10`（默认）| 范围 [`0`, `127`] 中的标量

输入主设备执行读取操作的 I2C 外设设备地址（十进制格式）。

### **外设寄存器地址** — I2C 外设设备寄存器地址 `0`（默认）| 范围 [`0`, `255`] 中的标量

输入控制器执行读取操作的 I2C 外设设备寄存器地址（十进制格式）。

### **数据类型** — 控制器读取的数据类型 `uint8`（默认）| `uint16` | `uint32`

选择控制器从外设设备或外设设备寄存器读取的数据类型。控制器在单次读取操作中最多只能读取 32 bytes 的数据。

### **数据大小 (N)** — 数据大小 `1`（默认）| 标量

输入控制器从外设设备或外设设备寄存器读取的数据大小。

例如，当您指定值为 5 时，控制器将从 **外设寄存器地址** 参数中指定的寄存器地址开始，从五个连续的外设设备寄存器读取数据。

**注意**

控制器只能对连续的外设设备寄存器执行组读取操作。

### **采样时间** — 控制器读取数据的时间间隔 `0.1`（默认）| 范围 [`0.01`, `1`] 中的标量

输入控制器从外设设备或外设设备寄存器读取数据的时间间隔（以 seconds 为单位）。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

控制器设备从 I2C 外设设备或 I2C 外设设备寄存器读取数据

在 I2C Register Read 模块中，控制器设备从 I2C 外设设备或 I2C 外设设备寄存器读取数据。EV3 brick 充当控制器设备。任何 I2C 设备（例如颜色传感器）都可以充当外设设备。为实现成功通信，控制器和外设设备都必须连接到同一个 I2C 网络。

Simulink® Support Package for LEGO® MINDSTORMS® EV3 Hardware 支持 I2C 串行数据通信协议，其中 I2C 网络上的每个设备都通过唯一的 8-bit 地址或标识符引用。
