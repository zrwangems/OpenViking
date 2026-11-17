---
type: simulink-block
title: 'Propagation Delay'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discrete'
documentation_page: 'propagationdelay'
documentation_source_path: 'slref/propagationdelay.html'
language: zh-CN
chinese_source: worker-translation
---

# Propagation Delay

## 端口

### 输入

### **u** — 要延迟的信号 标量

Propagation Delay 模块支持具有连续或离散采样时间的实数标量输入信号。输入信号数据类型可以是除 `int64` 和 `uint64` 之外的任何内置类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **dt** — 延迟信号 标量

延迟信号指定在仿真的每个时间步要施加的延迟量。您可以使用 Propagation Delay 模块来实现恒定或可变延迟。

延迟信号值必须满足以下约束：

- 延迟信号必须包含标量、实数、有限、正值且大于 `128*eps`，这是软件支持的最小时间分辨率。
- 延迟输入信号样本的输出时间必须单调递增。

  例如，假设延迟信号值在仿真时间 `0` 处为 `0.6`，下一个仿真步发生在时间 `0.5`。时间 `0.5` 处的延迟信号必须大于 `0.1`，以便输入信号样本 *U*0.5 的延迟输出时间大于输入信号样本 *U*0（`0.6`）的输出时间。
- 当您选择 **Run at fixed time intervals** 时，延迟信号值必须大于您为 **Sample time** 参数指定的值。

**数据类型：** `double`
### 输出

### **y** — 延迟信号 标量

输出信号与输入信号具有相同的数据类型。默认情况下，输出信号具有 fixed-in-minor-step 采样时间。当您选择 **Run at fixed time intervals** 时，输出信号具有您为 **Sample time** 参数指定的离散采样时间。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Initial output** — 输出信号的初始值 `0`（默认）| 标量

指定初始输出信号值 *Y*0。延迟信号的第一个样本 *D*0 决定模块输出何时从 **Initial output** 值变为延迟的输入信号值。

*y*(*t*) = *Y*0 当 *t* < *T*0 + *D*0

#### 编程使用

|  |
| --- |
| **模块参数**：`InitialOutput` |
| **类型**：string | character vector |
| **值**：numeric scalar |
| **默认值**：`0` |

### **Run at fixed time intervals** — 以固定速率执行模块的选项 `off`（默认）| `on`

此参数指定模块的执行方式以及输出信号的采样时间。

- `off` — 模块在每次输入样本的延迟时间到达时执行。输出信号具有 fixed-in-minor 采样时间。
- `on` — 模块以您使用 **Sample time** 参数指定的固定速率执行。输出信号具有您使用 **Sample time** 参数指定的采样时间。

当您选择 **Run at fixed time intervals** 时：

- 延迟信号值必须大于您为 **Sample time** 参数指定的值。
- 不是指定采样时间整数倍的延迟信号值将向下舍入到最接近的采样时间整数倍。例如，如果采样时间为 `0.1` 且延迟信号值为 `0.68`，软件会将延迟舍入为 `0.6`。

#### 编程使用

|  |
| --- |
| **模块参数**：`RunAtFixedTimeIntervals` |
| **类型**：string | character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Sample time** — 输出采样时间 `0.1`（默认）| 标量

指定模块输出信号的采样时间。延迟信号值必须大于指定的采样时间。

当延迟信号值不是指定采样时间的整数倍时，软件会将延迟值向下舍入到最接近的采样时间整数倍值。例如，如果采样时间为 `0.1` 且延迟值为 `0.68`，软件会将延迟舍入为 `0.6`。

#### 依赖关系

要启用此参数，请选择 **Run at fixed time intervals**。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：string | character vector |
| **值**：numeric scalar |
| **默认值**：`0.1` |

## 所属库

Simulink / Discrete

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要从使用 Propagation Delay 模块的模型生成代码，您必须将 Propagation Delay 模块配置为生成具有离散采样时间的输出。选择 **Run at fixed sample intervals** 并为 **Sample time** 参数指定离散速率。

Propagation Delay 模块动态分配内存以存储输入信号和延迟信号样本。代码生成的目标必须支持动态内存分配。

## 版本历史

**在 R2022b 中引入**

## 描述

对环路延迟、等待时间、脉冲延迟进行建模

Propagation Delay 模块将信号的当前值延迟到未来，延迟量由延迟信号指定。Propagation Delay 模块非常适合在离散系统中实现时间延迟。

在每个仿真步 *k*，模块采样信号输入 *U**k* 和延迟输入 *D**k*。模块输出值变为从当前仿真时间 *T**k* 起经过延迟时间 *D**k* 后的信号值。

*y*(*t*) = *U**k* 当 *t* = *T**k* + *D**k*

在仿真开始时，模块输出值为 **Initial output** 模块参数值 *Y*0。延迟信号的第一个样本 *D*0 决定模块输出何时从 **Initial output** 值变为延迟的输入信号值。

*y*(*t*) = *Y*0 当 *t* < *T*0 + *D*0

当仿真到达时间 *T*0 + *D*0 时，模块输出由信号和延迟样本决定。

*y*(*t*) = *U**k* 当 *T**k* + *D**k* ≤ *t* ≤ *T**k*+1 + *D**k*+1，

其中：

- *U**k* 是在 *t* = *T**k* 处采集的输入信号样本。
- *D**k* 是在 *t* = *T**k* 处采集的延迟信号样本。
- *T**k*+1 是采集下一个信号和延迟样本的仿真时间。
- *D**k*+1 是在时间 *T**k*+1 处采集的延迟样本。
