---
type: simulink-block
title: 'Event Source'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Scheduling'
documentation_page: 'eventsource'
documentation_source_path: 'ref/eventsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Event Source

## 端口

### 输入

### **data** — 输入数据 数值向量

输入数据，指定为数值向量。该模块将此数据转换为与输入数据速率对应的事件。您可以使用此事件在 Task Manager 模块中驱动事件驱动任务。

#### 依赖关系

要启用此端口，请将 **Input** 参数设置为 `From input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **event** — 任务事件信号 标量

此端口发送任务事件信号，触发 Task Manager (SoC Blockset) 模块执行关联的事件驱动任务。

**数据类型：** `rteEvent`

## 参数

### **Input** — 输入数据源 `From dialog`（默认）| `From input port` | `From timeseries object`

通过选择以下值之一来设置模块的输入数据源。

- `From dialog` — 使用函数输入一维数据数组。为 **Value** 参数指定此函数。
- `From input port` — 使用模块上的输入端口输入数据和信号。
- `From timeseries object` — 使用您在 MATLAB® 中创建的 timeseries 对象输入数据和时间值。有关详细信息，请参阅 Time Series Objects and Collections。

### **Sample time** — 采样时间间隔 `-1`（默认）| 非负标量

指定模块输出数据的离散时间间隔，以秒为单位。

#### 依赖关系

要启用此参数，请将 **Input** 参数设置为 `From dialog`。

### **Object name** — timeseries 对象名称 `[]`（默认）| timeseries 对象

指定一个 `timeseries` 对象。此 `timeseries` 对象为模块提供输入数据。有关时间序列对象的详细信息，请参阅 Time Series Objects and Collections。

#### 依赖关系

要启用此参数，请将 **Input** 参数设置为 `From timeseries object`。

## 所属库

SoC Blockset / Processor Testbench C2000 Microcontroller Blockset / Scheduling Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / Test Bench Blocks Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / Test Bench Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024a 中引入**

## 描述

仿真和回放记录的任务事件

Event Source 模块连接到 Task Manager (SoC Blockset) 模块，使您能够在 Simulink® 模型中仿真任务事件。任务时序数据可以从模块掩码、外部文件或由其他模型信号驱动的输入端口提供。
