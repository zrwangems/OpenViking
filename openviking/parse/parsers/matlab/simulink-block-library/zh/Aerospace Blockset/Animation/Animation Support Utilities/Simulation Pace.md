---
type: simulink-block
title: 'Simulation Pace'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Animation / Animation Support Utilities'
documentation_page: 'simulationpace'
documentation_source_path: 'simulationpace.html'
language: zh-CN
chinese_source: worker-translation
---

# Simulation Pace

## 端口

### 输出

### **Port\_1** — 步调误差 scalar

步调误差，指定为 scalar。

该模块可选地输出步调误差值（*simulationTime* 减 *ClockTime*），以 seconds 为单位。如果仿真运行速度快于指定的步调，则步调误差为正；如果慢于指定的步调，则为负。

从该模块输出步调误差，使您可以记录仿真期间达到的总体步调，或将信号路由到其他模块，以确定仿真是否太慢而无法跟上指定的步调。

#### 依赖项

要启用此端口，请选中 **输出步调误差 (sec)** 复选框。

**数据类型：** `double`

## 参数

### **仿真步调** — 仿真时间与时钟时间的比率 `1`（默认） | scalar

仿真时间与时钟时间的比率，指定为 scalar，以每 1 second 时钟时间对应的仿真时间 seconds 为单位。

#### 编程用法

|  |
| --- |
| **模块参数**: `OutputPaceError` |
| **类型**: character vector |
| **值：**`'1'` | scalar |
| **默认值**: `'1'` |

### **睡眠模式** — 控制仿真步调 `Auto`（默认） | `MATLAB Thread` | `Off` | `Busy-Wait`

使用以下方法之一控制模型的仿真步调。`MATLAB Thread`、`Busy-Wait` 和 `Auto` 会在 simulation-second 0.1 处减慢仿真步调，以等待挂钟到达时间 1。当一个 simulation-second 在几个挂钟时间 milliseconds 内完成时，使用此参数。

- `Auto` — 使用模型配置参数设置 **启用步调控制以减慢仿真** 控制仿真步调。如果未选择模型配置参数设置 **启用步调控制以减慢仿真**，则该模块的行为就好像选择了 `MATLAB Thread` 选项。
- `MATLAB Thread` — 在仿真期间使用操作系统 `sleep` 函数等待挂钟到达时间 1。
- `Off` — 禁用步调功能，让仿真尽可能快地运行。
- `Busy-Wait` — 结合 Simstruct 使用 while 循环，使仿真等待挂钟到达时间 1。

#### 编程用法

|  |
| --- |
| **模块参数**: `SleepMode` |
| **类型**: character vector |
| **值：**`'MATLAB Thread'` | `'Off'` | `'Busy-Wait'` | `'Auto'` |
| **默认值**: `'Auto'` |

### **输出步调误差** — 显示步调误差 `off`（默认） | `on`

选中此复选框以输出步调误差值（*simulationTime* 减 *ClockTime*），以 seconds 为单位。如果仿真运行速度快于指定的步调，则步调误差为正；如果慢于指定的步调，则为负。要禁用显示，请清除此复选框。

#### 编程用法

|  |
| --- |
| **模块参数**: `OutputPaceError` |
| **类型**: character vector |
| **值：**`'off' | 'on'` |
| **默认值**: `'off'` |

### **采样时间** — 采样时间 1/30（默认） | `-1` | scalar | vector

将采样时间指定为 scalar。默认值 1/30 second 对应于 30 frames-per-second 的可视化速率（桌面计算机的典型值）。要设置 Simulink 界面与挂钟同步的频率，请使用此参数。

模块采样时间必须为：

- 离散
- 大于 0.0 或继承采样时间 (-1)

模块采样时间及其可选偏移时间（[`Ts``,
To`]）必须为有限且离散。

**注意**

为获得平滑动画，请按需选择尽可能慢的采样时间，因为过采样几乎没有好处，而欠采样可能导致动画跳动。欠采样还可能会阻塞计算机上的 MATLAB® 主线程。

#### 编程用法

|  |
| --- |
| **模块参数**: `SampleTime` |
| **类型**: character vector |
| **值**: scalar | vector |
| **默认值**: `'1/30'` |

## 所属库

Aerospace Blockset / Animation / Animation Support Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2023a：Simulation Pace 模块对引用模型的支持

Simulation Pace 模块在加速模式或快速加速模式下对引用模型进行仿真时不受支持。从 R2023a 开始，要在这些模式下减慢仿真，请在 Simulink Editor 工具条的 **仿真** 选项卡中，选择 **运行** > **仿真步调控制**。

## 描述

设置用于动画查看的仿真速率

Simulation Pace 模块允许您以较慢的步调运行模型仿真，以便您可以舒适地查看连接动画并理解和观察系统行为。以较慢的速率可视化仿真更容易理解底层系统设计、识别设计问题并演示接近实时的行为。您可以在仿真进行期间查看结果并检查系统。

在一个 simulation-second 在几个挂钟时间 milliseconds 内完成的情况下使用此模块。

配置此模块时，还要考虑模块采样时间，它会影响仿真步调。默认值为 1/30 second，对应于 30 frames-per-second 的可视化速率（桌面计算机的典型值）。有关详细信息，请参阅采样时间。

要使用此模块：

- 将模型求解器设置为 `Fixed-step`。
- 使用离散采样时间。

**提示**

Simulation Pace 模块：

- 不会生成可部署代码。
- 在加速模式或快速加速模式下对引用模型进行仿真时不受支持。要在这些模式下减慢仿真，请在 Simulink® Editor 工具条的 **仿真** 选项卡中，选择 **运行** > **仿真步调控制**。
