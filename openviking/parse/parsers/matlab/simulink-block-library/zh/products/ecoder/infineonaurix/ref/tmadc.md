---
type: simulink-block
title: 'TMADC'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'tmadc'
documentation_source_path: 'infineonaurix/ref/tmadc.html'
language: zh-CN
chinese_source: worker-translation
---

# TMADC

## 端口

### 输入

### **trigger** — 用于触发转换的端口 `scalar`

通过软件触发来触发 TMADC 输入引脚进行转换。

当 mode 设置为 Trigger only 时，从 trigger 端口使您能够提供采样时间。

- `1—` TMADC 转换启动被触发
- `0—`TMADC 转换启动未被触发

#### 依赖关系

要查看此端口，请将 **Mode** 参数设置为 `Trigger only`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **msg** — SoC Blockset 仿真消息 `scalar`

此端口从接口模块接收 SoC Blockset™ 消息，TMADC 模块在仿真期间转换此消息并将其输出到 **result** 端口。

#### 依赖关系

要查看此输入端口，请将 **Mode** 设置为 `Trigger and read` 或 `Read results only`，选择 **Enable simulation port** 参数，并将端口类型设置为 **SoC Data (Message based)**。

### **sig** — 基于 Simulink 的仿真信号 `scalar` | `vector`

仅用于仿真的 Simulink® 信号输入端口在仿真期间充当 TMADC 模块输出的直通。

#### 依赖关系

要查看此端口，请将 **Mode** 设置为 `Trigger and read` 或 `Read results only`，选择 **Enable simulation port** 参数，并将端口类型设置为 **Signal**。

### 输出

### **result** — 作为 12-bit 值的电压 `scalar` | `vector`

模块将电压输出为 12-bit 值，输出端口是数组 `N x 1`，其中 **N** 根据所选通道数定义。

#### 依赖关系

要启用此端口，请将 **Mode** 参数设置为 `Trigger and read` 或 `Read results only`。

**数据类型：** `uint16`

### **status** — 读取操作的状态 `scalar`

模块在此端口输出读取操作的状态，为以下值之一：

- `0—`在成功触发对应通道后读取结果时没有错误
- `1—`在成功触发对应通道后读取结果时出错

#### 依赖关系

要启用此端口，请将 **Mode** 设置为 `Read results only`，并选择 **Enable status port** 参数。

**数据类型：** `double`

### **timestamp** — 16-bit 计数器值的状态 `scalar` | `vector`

该端口输出 timestamp 计数器的 16-bit 计数器值的状态。

#### 依赖关系

要启用此端口，请选择 **Enable timestamp** 参数。

**数据类型：** `Boolean`

### **event** — 用于启动转换的事件消息 `scalar`

此端口在每次触发时输出事件消息，以在仿真期间启动转换。

#### 依赖关系

要查看此端口，请将 **Mode** 设置为 `Trigger only`，选择 **Enable simulation port** 参数，并将端口类型设置为 **SoC Data (Message based)**。

### **triggersig** — 用于仿真的基于 Simulink 的触发信号 `scalar` | `vector`

此端口在仿真期间将在 **trigger** 输入端口接收到的数据作为信号输出。

#### 依赖关系

要查看此端口，请将 **Mode** 设置为 `Trigger only`，选择 **Enable simulation port** 参数，并将端口类型设置为 **Signal**。

## 参数

### **Mode** — 模块的操作模式 `Trigger and read`（默认） | `Trigger only` | `Read results only`

选择以下操作模式之一：

- `Trigger and read—` 选择此选项以在每个采样时间触发转换。模块等待转换完成并输出结果。此选项启用输出端口 **result**。
- `Trigger only—` 选择此选项以通过软件触发所选通道。此选项启用输入端口 **trigger**。由于模块在此模式下不显示转换结果，您必须使用另一个 **Mode** 参数设置为 `Read results only` 的 TMADC 模块来显示转换结果。
- `Read results only—` 选择此选项以使模块读取所选通道的结果。如果模块能够读取结果，则在 **status** 端口输出 `0`，否则输出 `1`。此选项启用输出端口 **result**。

### **Number of channels** — 选择所需通道 `1`（默认） | `2` | `3` | `...`

如果将 **Mode** 设置为 `Trigger and read`，则选择所需通道数，范围为 `1` 到 `16`。如果将 **Mode** 设置为 `Trigger only` 或 `Read results only`，则通道数限制为 1。

### **Enable timestamp** — 启用 timestamp `off`（默认） | `on`

选择此项以启用 timestamp。

当您选择 `Enable timestamp` 参数时，模块会配置一个额外的输出端口 timestamp，类似于 result 端口，用于读取 timestamp。

**注意**

- TMADC 模块具有 16-bit timestamp 计数器，该计数器在每次计数器溢出后复位。
- 当 Mode 设置为 `Trigger only` 时，Enable timestamp 参数不可用。

### **Enable status port** — 配置 status 端口 `off`（默认） | `on`

当您选择此参数时，模块会配置 **status** 输出端口。**status** 端口输出转换结果的状态。

#### 依赖关系

要启用此端口，请将 **Mode** 参数设置为 `Read results only`。

### **Sample time** — 模块读取输入模拟引脚的频率 `-1`（默认） | `scalar` | `vector`

以 seconds 为单位指定模块应读取模拟引脚的频率。

当您将此参数指定为 `-1` 时，Simulink 会根据模块在模型中的上下文确定模块的最佳采样时间。

#### 依赖关系

要启用 **Sample time** 参数，请将 **Mode** 参数设置为 `Trigger and read` 或 `Read results only`。

### **Enable simulation port** — 在模块中启用外设仿真端口 `off`（默认） | `on`

选择此参数以启用外设仿真功能。

### **Port Type** — 指定外设仿真端口的类型 `SoC Data (Message based)`（默认） | `Signal`

选择此参数以配置兼容的或基于 Simulink 信号的仿真端口，以启用外设仿真功能。

#### 依赖关系

要查看此参数，请选择 **Enable simulation port** 参数。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022b 中引入**

## 描述

测量模拟输入引脚的电压

测量模拟输入引脚的电压。

Time Multiplexed Analog to Digital Converter (TMADC) 模块将电压输出为 12-bit 值，输出端口是数组 `N x 1`，其中 **N** 根据所选通道数定义。
