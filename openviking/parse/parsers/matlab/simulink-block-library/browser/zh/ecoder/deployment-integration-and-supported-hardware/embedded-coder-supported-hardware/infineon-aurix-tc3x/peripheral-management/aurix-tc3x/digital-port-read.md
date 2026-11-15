---
type: simulink-block
title: 'Digital Port Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'digitalportread'
documentation_source_path: 'infineonaurixtc3x/ref/digitalportread.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Port Read

## 端口

### 输入

### **msg** — SoC Blockset 仿真消息 `scalar`

此端口从接口模块接收消息，Digital Port Read 模块在仿真期间将 **msg** 转换为要在输出端口发出的数据。

#### 依赖项

要查看此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **SoC Data (Message based)**。

### **sig** — 基于 Simulink 的仿真信号 `scalar` | `vector`

该仅用于仿真的信号输入端口在仿真期间作为直通，连接到 Digital Port Read 模块的输出。

#### 依赖项

要查看此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **Signal**。
### 输出

### **Pin(s)** — GPIO 引脚状态 `scalar` | `vector`

此端口输出你在 Digital Port Read Peripheral Configuration 中的 **Port number** 和 **Pin number** 参数里选择的数字引脚的状态。

如果引脚号为 `1`，则端口将状态输出为 logical scalar；如果大于 `1`，则输出为 logical vector。

**数据类型：** `Boolean`

## 参数

### **Number of pins** — 要配置的引脚数 `1`（默认）| `2` | `3` | `...`

选择你想要在模块中配置其输出的引脚数（`1` 到 `15`）。

### **Sample time** — 模块读取输入引脚值的频率 `-1`（默认）| `scalar` | `vector`

以 seconds 为单位指定模块应多久读取一次引脚值。

当将此参数指定为 `-1` 时，Simulink® 将基于模型中的模块上下文确定该模块的最佳采样时间。

### **Enable simulation port** — 在模块中启用外设仿真端口 `off`（默认）| `on`

选择此参数以启用外设仿真功能。

### **Port Type** — 指定外设仿真端口的类型 `SoC Data (Message based)`（默认）| `Signal`

选择此参数可配置 SoC 兼容的仿真端口或基于 Simulink 信号的仿真端口，以启用外设仿真功能。

#### 依赖项

要查看此参数，请选择 **Enable simulation port** 参数。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

读取 GPIO 引脚状态
读取 Infineon AURIX TC3x Microcontrollers 的 GPIO 端口引脚的逻辑状态。
