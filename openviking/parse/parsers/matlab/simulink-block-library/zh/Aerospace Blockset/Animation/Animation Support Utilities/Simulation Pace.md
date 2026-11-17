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
```yaml
ports:
- name: Port_1
  summary: 步调误差标量
  direction: output
  data_types: double
```

### 输出

### **Port\_1** — 步调误差标量

步调误差，指定为标量。

该模块可选地输出步调误差值（*simulationTime* 减去 *ClockTime*），单位为秒。如果仿真运行速度快于指定步调，则步调误差为正；如果慢于指定步调，则为负。

从模块输出步调误差可以让您记录仿真期间达到的整体步调，或将信号路由到其他模块以确定仿真是否太慢而无法跟上指定步调。

#### 依赖关系

要启用此端口，请选中 **Output pace error (sec)** 复选框。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Simulation pace
  summary: 仿真时间与时钟时间的比率 1（默认）| 标量
  group: ''
  block_parameter: OutputPaceError
  type: 字符向量
  values: '''1'' | 标量'
  default: '''1'''
- name: Sleep mode
  summary: 控制仿真步调 Auto（默认）| MATLAB Thread | Off | Busy-Wait
  group: ''
  block_parameter: SleepMode
  type: 字符向量
  values: '''MATLAB Thread'' | ''Off'' | ''Busy-Wait'' | ''Auto'''
  default: '''Auto'''
- name: Output pace error
  summary: 显示步调误差 off（默认）| on
  group: ''
  block_parameter: OutputPaceError
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: Sample time
  summary: 采样时间 1/30（默认）| -1 | 标量 | 向量
  group: ''
  block_parameter: SampleTime
  type: 字符向量
  values: 标量 | 向量
  default: '''1/30'''
```

### **Simulation pace** — 仿真时间与时钟时间的比率 `1`（默认）| 标量

仿真时间与时钟时间的比率，指定为标量，单位为每时钟时间秒的仿真时间秒数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`OutputPaceError` |
| **类型**：字符向量 |
| **值：**`'1'` | 标量 |
| **默认值**：`'1'` |

### **Sleep mode** — 控制仿真步调 `Auto`（默认）| `MATLAB Thread` | `Off` | `Busy-Wait`

使用以下方法之一控制模型的仿真步调。`MATLAB Thread`、`Busy-Wait` 和 `Auto` 会在仿真秒 0.1 处减慢仿真步调，以等待挂钟时间到达时间 1。当仿真一秒在几个挂钟时间毫秒内完成时，请使用此参数。

- `Auto` — 使用模型配置参数设置 **Enable pacing to slow down simulation** 来控制仿真步调。如果未选中模型配置参数设置 **Enable pacing to slow down simulation**，则该模块的行为如同选中了 `MATLAB Thread` 选项。
- `MATLAB Thread` — 在仿真期间使用操作系统 `sleep` 函数等待挂钟时间到达时间 1。
- `Off` — 禁用步调功能，让仿真尽可能快地运行。
- `Busy-Wait` — 结合 Simstruct 使用 while 循环，让仿真等待挂钟时间到达时间 1。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SleepMode` |
| **类型**：字符向量 |
| **值：**`'MATLAB Thread'` | `'Off'` | `'Busy-Wait'` | `'Auto'` |
| **默认值**：`'Auto'` |

### **Output pace error** — 显示步调误差 `off`（默认）| `on`

选中此复选框可输出步调误差值（*simulationTime* 减去 *ClockTime*），单位为秒。如果仿真运行速度快于指定步调，则步调误差为正；如果慢于指定步调，则为负。要禁用显示，请清除此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数**：`OutputPaceError` |
| **类型**：字符向量 |
| **值：**`'off' | 'on'` |
| **默认值**：`'off'` |

### **Sample time** — 采样时间 1/30（默认）| `-1` | 标量 | 向量

将采样时间指定为标量。默认值 1/30 秒对应于每秒 30 帧的可视化速率（台式计算机的典型值）。使用此参数可设置 Simulink 界面与挂钟时间同步的频率。

模块采样时间必须为：

- 离散
- 大于 0.0 或继承采样时间（-1）

模块采样时间及其可选偏移时间（[`Ts``, To`]）必须为有限且离散的值。

**注意**

根据需要选择尽可能慢的采样时间以实现平滑动画，因为过采样几乎没有好处，而欠采样可能导致动画跳跃。欠采样还可能阻塞您计算机上的 MATLAB® 主线程。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：字符向量 |
| **值**：标量 | 向量 |
| **默认值**：`'1/30'` |
## 所属库

Aerospace Blockset / Animation / Animation Support Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2023a：Simulation Pace 模块对引用模型的支持

Simulation Pace 模块在加速器或快速加速器模式下不支持用于仿真的引用模型。从 R2023a 开始，要在这些模式下减慢仿真速度，请在 Simulink Editor 工具条的 **Simulation** 选项卡中，选择 **Run** > **Simulation Pacing**。

## 描述

设置动画查看的仿真速率

Simulation Pace 模块允许您以较慢的速度运行模型仿真，以便您可以舒适地查看连接的动画并理解和观察系统行为。以较慢的速率可视化仿真可以更容易地理解底层系统设计、识别设计问题并展示接近实时的行为。您可以在仿真进行时查看结果并检查系统。

在仿真一秒在几个挂钟时间毫秒内完成的场景中使用此模块。

配置此模块时，还要考虑模块采样时间，它会影响仿真步调。默认值为 1/30 秒，对应于每秒 30 帧的可视化速率（台式计算机的典型值）。有关详细信息，请参阅 Sample time。

要使用此模块：

- 将模型求解器设置为 `Fixed-step`。
- 使用离散采样时间。

**提示**

Simulation Pace 模块：

- 不生成可部署代码。
- 在加速器或快速加速器模式下不支持用于仿真的引用模型。要在这些模式下减慢仿真速度，请在 Simulink® Editor 工具条的 **Simulation** 选项卡中，选择 **Run** > **Simulation Pacing**。
