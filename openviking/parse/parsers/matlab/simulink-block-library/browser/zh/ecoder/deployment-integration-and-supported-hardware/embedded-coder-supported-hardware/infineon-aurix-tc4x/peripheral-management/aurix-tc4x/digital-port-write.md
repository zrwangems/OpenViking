---
type: simulink-block
title: 'Digital Port Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'digitalportwrite'
documentation_source_path: 'infineonaurix/ref/digitalportwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Port Write

## 端口

### 输入

### **pin(s)** — GPIO pin(s) 的状态 `scalar` | `vector`

在此端口指定一个值以设置 GPIO pin(s) 的状态。您可以指定一个非负标量或一个由非负元素组成的向量。

- 指定 `0` 可将 pin(s) 设置为低电平。
- 指定 `nonzero` 值可将 pin(s) 设置为高电平。

可用的输入端口大小取决于 **Number of pins** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **msg** — SoC Blockset 仿真消息 `scalar`

Digital Port Write 模块将输入端口接收到的数据转换为 SoC Blockset™ 消息形式，并且 **msg** 端口在仿真期间输出该消息。

#### 依赖关系

要查看此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **SoC Data (Message based)**。

### **sig** — 基于 Simulink 的仿真信号 `scalar` | `vector`

此端口在仿真期间输出输入端口接收到的数据。

#### 依赖关系

要查看此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **Signal**。

## 参数

### **Number of pins** — 要配置的引脚数 `1`（默认） | `2` | `3` | `...`

选择您想要在模块中配置其输出的引脚数（`1` 到 `16`）。

### **Enable simulation port** — 启用模块中的外设仿真端口 `off`（默认） | `on`

选择此参数以启用外设仿真功能。

### **Port Type** — 指定外设仿真端口的类型 `SoC Data (Message based)`（默认） | `Signal`

选择此参数可配置 SoC 兼容的仿真端口或基于 Simulink® 信号的仿真端口，以启用外设仿真功能。

#### 依赖关系

要查看此参数，请选择 **Enable simulation port** 参数。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

设置 GPIO pin(s) 状态

为 Infineon AURIX TC4x Microcontrollers 写入 GPIO 端口的引脚逻辑状态。
