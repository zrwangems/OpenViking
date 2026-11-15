---
type: simulink-block
title: 'Optical Shaft Encoder'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'opticalshaftencoder'
documentation_source_path: 'vexv5/ref/opticalshaftencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Optical Shaft Encoder

## 端口

### 输入

### **Rst** — 用于重置编码器读数整数的信号（0 = 不重置；整数 ≥ 1 = 重置）

连接到用于重置 Optical Shaft Encoder 的信号。

#### 依赖关系

仅当您将 **Reset mode** 参数设置为 `Reset by external signal` 时，此输入才会出现。

**数据类型：** `double`
### 输出

### **Tick** — 从 Optical Shaft Encoder tick count 读取的 tick 数

从连接到 VEX V5 Robot Brain 的 Optical Shaft Encoder 读取的 tick 数量。旋转一圈对应 360 个 tick。电机轴逆时针旋转时该值递增，顺时针旋转时递减。

**数据类型：** `double`

## 参数

### **3-Wire Expander (smart port)** — 选择 3-Wire Expander 使用的 smart port `None`（默认） | `1` 到 `21`

如果您正在使用 3-Wire Expander，请指定 VEX® EDR V5 Robot Brain 上该 expander 所连接的 smart port。

### **Top port** — Optical Shaft Encoder 的顶部端口所连接的 3-wire 端口 A（默认） | `C` | `E` | `G`

选择 VEX V5 Robot Brain 上 Optical Shaft Encoder 的顶部端口所连接的 3-wire 端口。要了解顶部端口，请单击 **What is Top and Bottom Port?** 按钮。

在模块中选择 **Top port** 后，默认下一个连续的 3-wire 端口连接到编码器的底部端口。例如，如果您选择 `A` 作为 **Top port**，则假定 `B` 连接到编码器的底部端口。

### **Reset mode** — 选择用于读取值的重置模式 `Reset at each sample time`（默认） | `No reset` | `Reset by external signal`

选择从 Optical Shaft Encoder 读取值时的重置模式。

当您选择 `Reset by external signal` 时，模块会新增一个输入 – `Rst` – 该输入可连接到重置信号。

此模块支持的不同重置模式如下：

- `No reset` – 不重置测量值，模块输出旋转的总 tick 数。

  例如，在下表中，在 T = 1 时，编码器沿逆时针方向移动了 20 个 tick 计数，因此输出为 20。在 T = 1 与 T = 2 之间，编码器移动了 10 个 tick 计数。

  因此，在 T = 2 时 tick 计数为 30（来自 T = 1 的 20 加上来自 T = 2 的 10）。在此重置模式下，任意时刻的输出是先前计数与当前计数的累积和。
- `Reset at each sample time`  – 对于每个采样周期，模块输出测量值，然后将其重置为 0。

  例如，在下表中，在 T = 1 时，编码器沿逆时针方向移动了 20 个 tick 计数，因此输出为 20。在 T = 1 与 T = 2 之间，编码器移动了 10 个 tick 计数，因此输出为 10。在此重置模式下，输出是特定时刻的 tick 计数。
- `Reset by external signal`  – 测量值根据模块输入值重置为 0。当您向模块输入发送非 0 值时，测量值重置为 0。对于每个采样周期，模块输出自上次重置以来的测量值。

  例如，在下表中，当外部信号为 0 时，输出基于 ‘No reset’ 模式；当外部信号非零时，输出基于 ‘Reset at each sample time’ 模式。

### **Sample time** — 模块读取值的时间间隔 `0.2`（默认） | 正标量 | -1

输入模块从 Optical Shaft Encoder 读取值的时间间隔。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。如果您在 **Reset mode** 参数中选择 `Reset by external signal` 选项，**Sample time** 参数将隐藏，并且该值会被继承（Sample time = -1）。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

表示连接的 Optical Shaft Encoder，并以 tick 为单位读取电机轴的相对位置

Optical Shaft Encoder 模块表示连接到 VEX EDR V5 Robot Brain 的 3-wire 端口的 Optical Shaft Encoder，并以 tick 为单位读取电机轴的相对位置。电机轴逆时针旋转时该值递增，顺时针旋转时递减。

tick 计数还取决于您选择的 Reset mode。
