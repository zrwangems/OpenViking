---
type: simulink-block
title: 'CORDIC co-processor'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Computing Peripherals'
documentation_page: 'cordiccoprocessor'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/cordiccoprocessor.html'
language: zh-CN
chinese_source: worker-translation
---

# CORDIC co-processor

## 端口

### 输入

### **theta** — sin/cos/sinh/cosh 标量

Theta 是弧度角除以 ᴨ (pi)，对于 sin 或 cos 函数范围为 [-1,1]。

Theta 是双曲函数的角度 [-0.559, 0.559]。对于双曲函数，超出范围的输入值会被饱和。

#### 依赖关系

要启用此端口，请将 **Function** 设置为 `sin`、`cos`、`sin and cos` 或 `sinh and cosh`。

**数据类型：** `fixdt(1,32,31)` | `int32`

### **x and y** — atan2/mod 标量

- `x` - x 坐标
- `y` - y 坐标

范围为 [-1, 1]。

#### 依赖关系

要启用此端口，请将 **Function** 设置为 `atan2`、`mod`、`atan2 and mod`。

**数据类型：** `fixdt(1,32,31)` | `int32`

### 输出

### **function** — CORDIC 函数的结果 boolean

该模块输出所选函数的结果。例如，如果您选择函数为 `sin and cos`，则模块输出 sin and cos 函数的结果。

**注意**

对于双曲函数 `sinh` 或 `cosh`，必须在输出上添加 2 的增益。

**数据类型：** `fixdt(1,32,31)`

### **Status** — 执行状态标量

该模块输出 CORDIC 执行状态。

- `0` - 成功
- `1` - 不成功

#### 依赖关系

要启用此端口，请选择 **Output status** 参数。

**数据类型：** `Boolean`

### **Executed func** — 执行函数状态标量

该模块输出 CORDIC 执行函数状态。

已执行的 CORDIC 函数提供以下状态：

- `0` - cos
- `1` - sin 或 sin and cos
- `2` - atan2 或 atan2 and mod
- `3` - mod
- `5` - cosh
- `6` - sinh 或 sinh and cosh

#### 依赖关系

要启用此端口，请将 DMA mode 设置为 Read only 并选择 **Execution function** 参数。

**数据类型：** `int32`

### **Executed iters** — 执行迭代状态标量

该模块输出上一次计算中已执行的迭代次数。

已执行的 CORDIC 迭代提供以下状态：

- `0` - cos
- `1` - sin 或 sin and cos
- `2` - atan2 或 atan2 and mod
- `3` - mod
- `5` - cosh
- `6` - sinh 或 sinh and cosh

#### 依赖关系

要启用此端口，请将 DMA mode 设置为 Read only 并选择 **Execution iteration** 参数。

**数据类型：** `int32`

### **Executed array size** — 执行数组大小状态标量

该模块输出上一次计算中已执行的数组大小。

已执行的 CORDIC 数组大小提供以下状态：

- `0` - cos
- `1` - sin 或 sin and cos
- `2` - atan2 或 atan2 and mod
- `3` - mod
- `5` - cosh
- `6` - sinh 或 sinh and cosh

#### 依赖关系

要启用此端口，请将 DMA mode 设置为 Read only 并选择 **Execution array size** 参数。

**数据类型：** `int32`

## 参数

### **Function** — 选择数学函数 `sin and cos` (default) | `sinh and cosh` | `atan2 and mod` | `sin` | `cos` | `sinh` | `cosh` | `atan2` | `mod`

选择三角函数或双曲函数。

### **Number of iterations** — 选择迭代次数 `24` (default) | `4` | `8` | `12` | `16` | `…`

选择迭代次数以提高结果的精度。

### **CORDIC mode** — 选择 CORDIC 模式 `DMA` (default) | `Zero overhead`

选择 **DMA** 或 **Zero overhead** 作为 CORDIC 模式。

- `Zero overhead` - 数据从 CORDIC co-processor 单独写入和读取。
- `DMA` - 遍历元素数组的过程由 DMA 完成。

### **DMA mode** — 选择 DMA 模式 `Write and Read` (default) | `Write only` | `Read only`

使用户能够从单个模块执行 DMA 的写入和读取操作。

- `Write only` - 执行 DMA 的写操作
- `Read` - 执行 DMA 的读操作

#### 依赖关系

要启用此参数，请将 **CORDIC mode** 设置为 DMA。

### **Output data type** — 选择 DMA 输出数据类型 `fixdt(1,32,31)` (default) | `int32` | `Read only`

指定 CORDIC co-processor 的输出数据类型。

#### 依赖关系

要启用此参数，请将 **DMA mode** 设置为 **Read only**。

### **Input size** — 指定 DMA 输入大小 `1` (default)

指定 CORDIC co-processor 的输入大小。

当此参数与写入模块的输入大小对齐时，用户将获得有效输出。

#### 依赖关系

要启用此参数，请将 **DMA mode** 设置为 **Read only**。

### **Executed function** — 启用已执行函数 `off` (default) | `on`

当您选择此参数时，模块将配置 **Executed func** 输出端口。该端口输出上一步中已执行的函数。

#### 依赖关系

要启用此参数，请将 **DMA mode** 设置为 **Read only**。

### **Executed iterations** — 启用已执行迭代次数 `off` (default) | `on`

当您选择此参数时，模块将配置 **Executed iters** 输出端口。该端口输出上一步中已执行的迭代次数。

#### 依赖关系

要启用此参数，请将 **DMA mode** 设置为 **Read only**。

### **Executed array size** — 启用已执行数组大小 `off` (default) | `on`

当您选择此参数时，模块将配置 **Executed array size** 输出端口。该端口输出上一步中已执行的数组大小。

#### 依赖关系

要启用此参数，请将 **DMA mode** 设置为 **Read only**。

### **Sample time** — 模块读取引脚值的频率 `-1` (default) | `non-negative real value`

指定模块读取引脚值的频率（以秒为单位）。输入大于零的值。当您将此参数指定为 -1 时，Simulink 将根据模型中的模块上下文确定模块的最佳采样时间。

#### 依赖关系

要启用此参数，请将 **DMA mode** 设置为 **Read only**。

### **Timeout (in ms)** — DMA 超时 `10` (default)

指定 DMA 超时（以微秒为单位）。

### **Enable preemption** — 选择启用抢占 `off` (default) | `on`

选择以启用抢占。

### **Output status** — 启用输出状态 `off` (default) | `on`

当您选择此参数时，模块将配置 **Status** 输出端口。Status 端口输出执行状态。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32H7xx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2023b 中引入**

## 描述

启用三角和双曲数学函数的硬件加速

CORDIC co-processor 模块为计算密集型应用中使用的三角和双曲数学函数提供硬件加速，以执行其他任务。CORDIC co-processor 模块支持 zero overhead 模式。
