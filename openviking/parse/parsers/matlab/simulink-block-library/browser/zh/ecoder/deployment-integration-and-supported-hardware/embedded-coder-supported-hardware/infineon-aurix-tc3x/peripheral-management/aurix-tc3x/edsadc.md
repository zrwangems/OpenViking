---
type: simulink-block
title: 'EDSADC'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'edsadc'
documentation_source_path: 'infineonaurixtc3x/ref/edsadc.html'
language: zh-CN
chinese_source: worker-translation
---

# EDSADC

## 端口

### 输出

### **result** — 模拟输入引脚的电压 `scalar` | `vector`

当您将 **Result type** 参数设置为 `Voltage` 时，模块将测得的电压输出为单精度浮点数。当您将 **Result type** 参数设置为 `Counts` 时，模块将电压输出为 16 位计数值，格式为 `N`×1 数组，其中 `N` 根据参数值而变化，如下表所示。

| 读取模式 | FIFO | 时间戳 | 有效 FIFO 级别 | 结果大小 |
| --- | --- | --- | --- | --- |
| Number of 16-bit data to read: **1** | Disable | Disable | Stage 1 | 1×1 |
| Enable | Disable | Stage 1 | 1×1 |
| Stage 2 | 2×1 |
| Stage 3 | 3×1 |
| Stage 4 | 4×1 |
| Enable | Stage 2 | 1×1 |
| Stage 3 | 2×1 |
| Stage 4 | 3×1 |
| Number of 16-bit data to read: **2** | Enable | Disable | Stage 2 | 2×1 |
| Stage 4 | 4×1 |
| Enable | Stage 4 | 3×1 |

**数据类型：** `uint16` | `int16` | `single`

### **aux\_result** — 作为有符号或无符号 16 位值的辅助结果 `scalar`

模块将辅助结果输出为有符号 16 位值或单精度浮点数，具体取决于 **Result type** 参数的选择。使用此端口可在转换期间绕过偏移和积分器滤波级，获得转换的即时结果。

#### 依赖项

要启用此端口，请选择 **Auxiliary result** 参数。

**数据类型：** `int16` | `single`

### **timestamp** — 16 位计数器值的时间戳 `scalar`

模块输出 16 位时间戳计数器的当前值。

#### 依赖项

要启用此端口，请选择 **Enable timestamp** 参数。

**数据类型：** `uint16`

## 参数

### **Enable timestamp** — 启用时间戳输出的选项 `off` (default) | `on`

选择此参数以启用 **timestamp** 输出端口。

选择此参数还会启用 EDSADC Peripheral Configuration 工具中 **Timestamp** 选项卡以及 **Events** 选项卡下的 Timestamp 事件中的选项。

**注意**

由于时间戳始终与触发信号关联，因此请在选择 **Enable timestamp** 参数之前配置触发信号。

### **Auxiliary result** — 启用辅助结果输出 `off` (default) | `on`

选择此参数以启用 **aux\_result** 输出端口。模块将辅助结果输出为单精度浮点数或有符号 16 位值。

选择此参数会启用 EDSADC Peripheral Configuration 工具中的相关参数。

### **Enable FIFO** — 启用 FIFO 寄存器的选项 `off` (default) | `on`

选择此参数以启用 FIFO 寄存器。

### **Number of 16 bit data to read** — 要读取的 16 位输出数据数量 `1` (default) | `2`

指定要读取的 16 位输出数据的数量。

指定 `2` 以更快地从 FIFO 寄存器中获取数据。

#### 依赖项

要启用 **Number of 16 bit data to read** 参数，请选择 **Enable FIFO** 参数。

### **FIFO level** — FIFO 寄存器级别 `4` (default) | `3` | `2` | `1`

用于数据传输的 FIFO 寄存器级别。

如果禁用 **Enable Timestamp**，则会出现选项 `1`

#### 依赖项

要启用 **FIFO level** 参数，请选择 **Enable FIFO** 参数。

### **Result type** — 转换结果的类型 `Counts` (default) | `Voltage`

指定 **result** 端口输出的类型。

### **Main result type** — 结果的数据类型 `Signed` (default) | `Unsigned`

指定 **result** 端口输出的数据类型。

#### 依赖项

要启用此参数，请将 **Result type** 参数设置为 `Counts`。

### **Sample time** — 模块读取输入模拟引脚的频率 `-1` (default) | `scalar`

以秒为单位指定模块应读取模拟引脚的频率。

当您将此参数指定为 `-1` 时，Simulink® 将根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

使用 delta-sigma 转换测量模拟输入引脚的电压

EDSADC 模块使用 delta-sigma 转换测量模拟输入引脚的电压。

它将电压输出为单精度浮点数、无符号或有符号 16 位计数值，格式为 N×1 数组。delta-sigma 转换过程可以使用片上调制器或外部调制器，您可在 EDSADC Peripheral Configuration 工具中选择。该模块根据您在 Hardware Mapping 工具中配置 EDSADC 外设时指定的滤波器参数，连续提供转换结果。
