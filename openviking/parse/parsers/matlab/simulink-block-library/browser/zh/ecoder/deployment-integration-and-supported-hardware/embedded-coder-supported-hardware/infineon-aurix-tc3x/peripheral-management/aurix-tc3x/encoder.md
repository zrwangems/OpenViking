---
type: simulink-block
title: 'Encoder'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'encoder'
documentation_source_path: 'infineonaurixtc3x/ref/encoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Encoder

## 端口

### 输入

### **msg** — SoC 仿真消息 `scalar`

该模块在仿真期间将此输入 SoC 消息转换为编码器位置，并通过 **ticks** 端口输出。

#### 依赖关系

要查看此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **SoC Data (Message based)**。

### **sig** — 基于 Simulink 的仿真信号 `scalar` | `vector`

仅用于仿真的 Simulink® 信号输入在仿真期间作为 Encoder 模块输出的直通。

#### 依赖关系

要启用此端口，请选择 **Enable simulation port** 参数，并将端口类型设置为 **Signal**。

### **offset\_in** — 启用后添加电机偏移 `scalar`

offset\_in 端口使您能够在需要时相对于电机动态添加原始位置中的偏移。

#### 依赖关系

要启用此端口，请选择 **Enable offset inport** 参数。

**数据类型：** `int32`

### **rate\_in** — 启用后更改数据速率 `scalar`

rate\_in 端口使您能够更改运行时数据采样速率（以秒为单位）。

#### 依赖关系

要启用此端口，请选择 **Enable refresh rate inport** 参数。

**数据类型：** `Float32`

### 输出

### **ticks** — 以 count 为单位的编码器位置 `scalar`

ticks 端口以 `int32` 值输出以 count 为单位的编码器位置。

**数据类型：** `int32`

### **dir** — 当前电机方向 `scalar`

dir 端口输出电机的当前方向，取值为以下之一：

- `0` - 顺时针方向
- `1` - 逆时针方向

#### 依赖关系

要启用此端口，请选择 **Enable direction port** 参数。

**数据类型：** `Boolean`

### **speed** — 电机机械速度 `scalar`

speed 端口以 `float32` 值输出电机的机械速度（单位为 rad/s）。

**注意**

- 如果将 **Enable slow speed detection** 参数设置为测量低速，则必须将该模块的 **sample time** 参数设置为大于一个编码器 tick 持续时间，否则读取的速度为零。
- 编码器 tick 在高位回滚会导致速度计算中出现离群值。您必须使用 Delay 模块来校正电机速度。

#### 依赖关系

要启用此端口，请选择 **Enable speed port** 参数。

**数据类型：** `float32`

## 参数

### 输出

### **Enable direction port** — 选择以启用方向输出端口 `off` (默认) | `on`

启用此参数以输出电机的当前方向。

### **Enable speed port** — 选择以启用速度输出端口 `off` (默认) | `on`

启用此参数以输出电机的机械速度（单位为 rad/s）。

### 输入

### **Enable refresh rate inport** — 选择以启用刷新速率输入端口 `off` (默认) | `on`

启用此参数以刷新数据采样速率。

#### 依赖关系

要查看此参数，请选择 **Enable speed port** 参数。

### **Enable offset inport** — 选择以启用偏移输入端口 `off` (默认) | `on`

启用此参数以相对于电机动态添加原始位置中的偏移。

### **Sample time** — 模块对输入引脚采样的频率 `-1` (默认) | `scalar` | `vector`

以秒为单位指定该模块读取引脚值的频率。

当将此参数指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

### **Enable simulation port** — 启用模块中的外设仿真端口 `off` (默认) | `on`

选择此参数以启用外设仿真功能。

### **Port Type** — 指定外设仿真端口的类型 `SoC Data (Message based)` (默认) | `Signal`

选择此参数以配置 SoC 兼容或基于 Simulink 信号的仿真端口，从而启用外设仿真功能。

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

以 tick 为单位测量电机旋转

以 tick 为单位测量电机的旋转。

ticks 端口以 `int32` 值输出编码器 tick 计数。

启用后，**dir** 端口输出编码器的方向。

- `0` - 顺时针方向。
- `1` - 逆时针方向。

Encoder 模块基于 AURIX TC3x 器件中可用的 GPT12（通用定时器）模块开发，其中使用了定时器 T3 和 T5（低速计算）。
