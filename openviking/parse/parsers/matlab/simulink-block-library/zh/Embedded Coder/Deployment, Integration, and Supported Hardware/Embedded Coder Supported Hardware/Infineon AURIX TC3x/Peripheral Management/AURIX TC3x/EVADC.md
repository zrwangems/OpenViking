---
type: simulink-block
title: 'EVADC'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'evadc'
documentation_source_path: 'infineonaurixtc3x/ref/evadc.html'
language: zh-CN
chinese_source: worker-translation
---

# EVADC

## 端口

### 输入

### **trigger** — 触发转换 标量

通过软件触发来触发 EVADC 输入引脚以进行转换。

#### 依赖项

要启用此端口，请将 **Mode** 参数设置为 `ADC trigger`。

**数据类型：** `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **msg** — SoC 仿真消息 `scalar`

此端口从接口模块接收消息，EVADC 模块会转换此消息，并在仿真期间将其输出到 **result** 端口。

#### 依赖项

要查看此输入端口，请将 **Mode** 参数设置为 `ADC read`，选择 **Enable simulation port** 参数，并将端口类型设置为 **SoC Data (Message based)**。

### **sig** — 基于 Simulink® 的仿真信号 `scalar` | `vector`

仅用于仿真的 Simulink 信号输入端口在仿真期间充当 EVADC 模块输出的直通。

#### 依赖项

要查看此输入端口，请将 **Mode** 参数设置为 `ADC read`，选择 **Enable simulation port** 参数，并将端口类型设置为 **Signal**。
### 输出

### **result** — 以 12-bit 值表示的电压 标量 | 向量

模块将输入电压作为 12-bit 值输出到 `N-by-1` 数组中，其中 N 根据 **Number of channels** 参数中指定的通道数定义。

**数据类型：** `uint16`

### **status** — 读取操作的状态 标量

模块将读取操作的状态输出到 `1-by-N` 数组中，其中 N 表示 **Number of channels** 参数中指定的通道数。每个数组元素表示单个通道的读取操作状态，为以下值之一：

- `0 —` 转换结果可用
- `1 —` 转换结果不可用

#### 依赖项

要启用此端口，请将 **Mode** 参数设置为 `ADC read`，并启用 **Status** 参数。

**数据类型：** `uint8`

### **event** — 启动转换的事件消息 `scalar`

此端口在仿真期间每次触发时输出事件消息以启动转换。

#### 依赖项

要查看此端口，请将 **Mode** 参数设置为 `ADC trigger`，选择 **Enable simulation port** 参数，并将端口类型设置为 **SoC Data (Message based)**。

### **triggersig** — 用于仿真的基于 Simulink 的触发信号 `scalar` | `vector`

此端口在仿真期间将 **trigger** 输入端口接收到的数据作为信号输出。

#### 依赖项

要查看此端口，请将 **Mode** 参数设置为 `ADC trigger`，选择 **Enable simulation port** 参数，并将端口类型设置为 **Signal**。

## 参数

### **Mode** — EVADC 模块的操作模式 `ADC read`（默认） | `ADC trigger`

选择以下操作模式之一：

- `ADC read —` 选择此选项可使模块读取所选通道的结果。此选项会启用输出端口 **result**。选择此模式会在 EVADC Peripheral Configuration 中启用 **Input #** 选项卡和 **Group select** 选项卡中的选项。
- `ADC trigger —` 选择此选项可通过软件触发来触发所选通道。此选项会启用输入端口 **trigger**。选择此模式会在 EVADC Peripheral Configuration 中启用 **Group select** 选项卡中的选项。

  **注意**

  由于模块在此模式下不显示转换结果，您必须使用另一个 **Mode** 参数设置为 `ADC read` 的 EVADC 模块来显示转换结果。

### **Number of channels** — 选择通道数 `1`（默认） | `2` | `3` | `...`

选择所需的通道数，范围为 `1` 到 `16`。

### **Status** — 启用状态端口的选项 `off`（默认） | `on`

选择此参数时，模块会配置 **status** 输出端口以输出转换结果的状态。

#### 依赖项

要启用此端口，请将 **Mode** 参数设置为 `ADC read`。

### **Sample time** — 模块读取输入模拟引脚的频率 `-1`（默认） | 标量 | 向量

以 seconds 为单位指定模块读取模拟引脚的频率。

当您将此参数设置为 `-1` 时，Simulink 会根据模型中的模块上下文确定模块的最佳采样时间。

#### 依赖项

要启用 **Sample time** 参数，请将 **Mode** 参数设置为 `ADC read`。

### **Enable simulation port** — 在模块中启用外设仿真端口 `off`（默认） | `on`

选择此参数以启用外设仿真功能。

### **Port Type** — 指定外设仿真端口的类型 `SoC Data (Message based)`（默认） | `Signal`

选择此参数可配置基于 SoC 消息或基于 Simulink 信号的仿真端口，以启用外设仿真功能。

#### 依赖项

要查看此参数，请选择 **Enable simulation port** 参数。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

测量模拟输入引脚的电压

测量模拟输入引脚的电压。

Enhanced Versatile Analog to Digital Converter (EVADC) 模块将输入信号的电压作为 12-bit 值输出到 `N-by-1` 数组中，其中 N 根据所选通道数定义。

**注意**

如果在单个 EVADC 模块的多个通道中添加同一引脚，则某些通道在外部模式和 Synopsys Virtualizer Studio 中无法捕获转换结果。
