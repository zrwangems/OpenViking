---
type: simulink-block
title: 'Digital Port Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'digitalportread'
documentation_source_path: 'infineonaurix/ref/digitalportread.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Port Read

## 端口

### 输入

### **msg** — SoC Blockset 仿真消息 `scalar`

此端口从接口模块接收 SoC Blockset™ 消息，Digital Port Read 模块在仿真期间将 **msg** 转换为要在输出端口发出的数据。

#### 依赖项

要查看此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **SoC Data (Message based)**。

### **sig** — 基于 Simulink 的仿真信号 `scalar` | `vector`

仅用于仿真的信号输入端口在仿真期间与 Digital Port Read 模块的输出直通。

#### 依赖项

要查看此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **Signal**。

### 输出

### **pin(s)** — GPIO 引脚状态 `scalar` | `vector`

该端口输出你在 Digital Port Read Peripheral Configuration 的 **Port number** 和 **Pin number** 参数中选择的数字引脚的状态。

如果引脚号为 `1`，该端口将状态输出为逻辑标量；如果大于 `1`，则输出为逻辑向量。

**数据类型：** `Boolean`

## 参数

### **Number of pins** — 你要配置的引脚数 `1`（默认）| `2` | `3` | `...`

选择你要在模块中配置其输出的引脚数（`1` 到 `16`）。

### **Sample time** — 模块读取输入引脚值的频率 `-1`（默认）| `scalar` | `vector`

以秒为单位指定模块读取引脚值的频率。

当将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

### **Enable simulation port** — 启用模块中的外设仿真端口 `off`（默认）| `on`

选择此参数以启用外设仿真功能。

### **Port Type** — 指定外设仿真端口的类型 `SoC Data (Message based)`（默认）| `Signal`

选择此参数可配置 SoC 兼容的仿真端口或基于 Simulink 信号的仿真端口，以启用外设仿真功能。

#### 依赖项

要查看此参数，请选择 **Enable simulation port** 参数。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022b 中引入**

## 描述

读取 GPIO 引脚状态

读取 Infineon AURIX TC4x Microcontrollers 的 GPIO 端口引脚的逻辑状态。
