---
type: simulink-block
title: 'Encoder'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'encoder'
documentation_source_path: 'infineonaurix/ref/encoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Encoder

## 端口

### 输入

### **msg** — SoC Blockset 仿真消息 `scalar`

该模块将此输入 SoC Blockset™ 消息转换为编码器位置，并在仿真期间将其输出到
**ticks** 端口。

#### 依赖关系

要查看此端口，请选择 **Enable simulation
port** 参数并将端口类型设置为 **SoC
Data (Message based)**。

### **sig** — 基于 Simulink 的仿真信号 `scalar` | `vector`

仅用于仿真的 Simulink® 信号输入在仿真期间作为 Encoder 模块输出的直通。

#### 依赖关系

要启用此端口，请选择 **Enable simulation
port** 参数并将端口类型设置为
**Signal**。

### **offset\_in** — 启用添加电机偏移量 `scalar`

offset\_in 端口使您能够在需要时动态添加相对于电机的原始位置偏移量。

#### 依赖关系

要启用此端口，请选择 **Enable offset
inport** 参数。

**数据类型：** `int32`

### **rate\_in** — 启用更改数据速率 `scalar`

rate\_in 端口使您能够在运行时更改数据采样速率（单位为 seconds）。

#### 依赖关系

要启用此端口，请选择 **Enable refresh rate
inport** 参数。

**数据类型：** `Float32`
### 输出

### **ticks** — 计数形式的编码器位置 `scalar`

ticks 端口将计数形式的编码器位置作为
`int32` 值输出。

**数据类型：** `int32`

### **dir** — 当前电机方向 `scalar`

dir 端口将电机的当前方向输出为以下之一：

- `0` - 顺时针方向
- `1` - 逆时针方向

#### 依赖关系

要启用此端口，请选择 **Enable direction
port** 参数。

**数据类型：** `Boolean`

### **speed** — 电机机械速度 `scalar`

speed 端口将电机的机械速度（单位为 rad/s）作为
`float32` 值输出。

#### 依赖关系

要启用此端口，请选择 **Enable speed
port** 参数。

**数据类型：** `float32`

### **offset\_out** — 电机位置偏移量 `scalar`

offset\_out 端口将相对于电机的原始位置偏移量作为 **int32** 值输出。

#### 依赖关系

要启用此端口，请选择 **Enable offset
outport** 参数。

**数据类型：** `int32`

### **rate** — 编码器更新周期 `scalar`

rate 端口将数据采样速率（单位为 seconds）作为
`float32` 值输出。

#### 依赖关系

要启用此端口，请选择 **Enable rate
outport** 参数。

**数据类型：** `float32`

## 参数

### 输入

### **Enable offset inport** — 选择以启用偏移量输入端口 `off`（默认） | `on`

启用此参数可动态添加相对于电机的原始位置偏移量。

### **Enable refresh rate inport** — 选择以启用刷新速率输入端口 `off`（默认） | `on`

启用此参数可刷新数据采样速率。

### **Enable simulation port** — 启用模块中的外设仿真端口 `off`（默认） | `on`

选择此参数以启用外设仿真功能。

### **Port Type** — 指定外设仿真端口的类型 `SoC Data (Message based)`（默认） | `Signal`

选择此参数可配置 SoC 兼容的仿真端口或基于 simulink 信号的仿真端口，以启用外设仿真功能。

#### 依赖关系

要查看此参数，请选择 **Enable simulation
port** 参数。

### 输出

### **Enable direction port** — 选择以启用方向输出端口 `off`（默认） | `on`

启用此参数可输出电机的当前方向。

### **Enable speed port** — 选择以启用速度输出端口 `off`（默认） | `on`

启用此参数可输出电机的机械速度（单位为 rad/s）。

### **Enable offset outport** — 选择以启用偏移量输出端口 `off`（默认） | `on`

启用此参数可输出相对于电机的原始位置偏移量。

### **Enable refresh rate outport** — 选择以启用速率输出端口 `off`（默认） | `on`

启用此参数可输出数据采样速率（单位为 seconds）。

### **Sample time** — 模块对输入引脚采样的频率 `0.0001`（默认） | `scalar` | `vector`

以 seconds 为单位指定模块应读取引脚值的频率。

当将此参数指定为 `-1` 时，Simulink 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022b 中引入**

## 描述

以 ticks 为单位测量电机旋转

以 ticks 为单位测量电机的旋转。

ticks 端口将编码器 ticks 计数作为 `int32`
值输出。

启用时，**dir** 端口输出编码器的方向。

- `0` - 顺时针方向。
- `1` - 逆时针方向。

Encoder 模块基于 AURIX TC4x 设备中可用的 GPT12（通用定时器）模块开发，其中使用了定时器 T3 & T5（慢速计算）。
