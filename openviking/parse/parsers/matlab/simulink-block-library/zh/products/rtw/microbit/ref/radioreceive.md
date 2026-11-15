---
type: simulink-block
title: 'Radio Receive'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Radio'
documentation_page: 'radioreceive'
documentation_source_path: 'microbit/ref/radioreceive.html'
language: zh-CN
chinese_source: worker-translation
---

# Radio Receive

## 端口

### 输出

### **Data** — 接收的数据向量

在每个采样时间，该端口以 N-by-1 数组形式输出接收的数据，其类型由 数据类型 参数指定，大小由 **数据长度 (N)** 参数指定。

### **Status** — 接收数据的状态标量

Status 端口输出以下值之一：

- `1`—已接收到数据。
- `0`—未接收到数据。
- `–1`—接收期间
  数据损坏。

## 参数

### **信道号 (1–100)** — 选择用于接收数据的信道 `1`（默认） | 从 1 到 100（含）的任意整数

要用于接收数据的信道号。

**注意**

发送器和接收器必须设置为相同的信道号。

### **数据类型** — 要接收的数据类型 `double`（默认） | `string` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

模块接收的数据类型。每个元素的大小取决于其数据类型。

### **数据长度 (N)** — 要接收的数据单元数 `10`（默认） | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

每个采样时间接收的数据单元数。允许的单元数范围取决于数据类型，如下表所示：

| 数据类型 | 范围 |
| --- | --- |
| double | 1–31 |
| single | 1–63 |
| int8 | 1–254 |
| uint8 | 1–254 |
| int16 | 1–127 |
| uint16 | 1–127 |
| int32 | 1–63 |
| uint32 | 1–63 |
| boolean | 1–254 |

### **采样时间** — 模块读取数据的时间间隔 `0.2`（默认） | `-1` | 任意非负值

当将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for BBC micro:bit/Radio

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

## 描述

通过无线电从 micro:bit 设备接收数据

Radio Receive 模块通过无线连接从其他 micro:bit 设备接收数据。
