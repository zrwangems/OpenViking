---
type: simulink-block
title: 'Digital Port Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'digitalportwrite'
documentation_source_path: 'infineonaurixtc3x/ref/digitalportwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Port Write

## 端口

### 输入

### **Pin(s)** — GPIO 引脚的状态 `scalar` | `vector`

在此端口指定一个值，以设置 GPIO 引脚的状态。您可以指定一个非负标量或由非负元素组成的向量。

- 指定 `0` 将引脚设置为低值。
- 指定 `nonzero` 值将引脚设置为高值。

可用输入端口的大小取决于 **Number of pins** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **msg** — SoC 仿真消息 `scalar`

Digital Port Write 模块将在输入端口接收到的数据转换为 SoC Blockset™ 消息形式，并且 **msg** 端口在仿真期间输出该消息。

#### 依赖关系

要查看此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **SoC Data (Message based)**。

### **sig** — 基于 Simulink 的仿真信号 `scalar` | `vector`

此端口在仿真期间输出在输入端口接收到的数据。

#### 依赖关系

要查看此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **Signal**。

## 参数

### **Number of pins** — 要配置的引脚数 `1`（默认） | `2` | `3` | `...`

选择要在模块中配置其输出的引脚数（`1` 到 `15`）。

### **Enable simulation port** — 启用模块中的外设仿真端口 `off`（默认） | `on`

选择此参数以启用外设仿真功能。

### **Port Type** — 指定外设仿真端口的类型 `SoC Data (Message based)`（默认） | `Signal`

选择此参数可配置 SoC 兼容的仿真端口或基于 Simulink® 信号的仿真端口，以启用外设仿真功能。

#### 依赖关系

要查看此参数，请选择 **Enable simulation port** 参数。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2024a 中引入**

## 描述

设置 GPIO 引脚状态

为 Infineon AURIX TC3x Microcontrollers 写入 GPIO 端口的引脚逻辑状态。
