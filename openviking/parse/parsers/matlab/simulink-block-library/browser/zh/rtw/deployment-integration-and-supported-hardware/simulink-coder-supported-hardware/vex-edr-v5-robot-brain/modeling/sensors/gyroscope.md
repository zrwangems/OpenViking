---
type: simulink-block
title: 'Gyroscope'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Sensors'
documentation_page: 'gyroscope'
documentation_source_path: 'vexv5/ref/gyroscope.html'
language: zh-CN
chinese_source: worker-translation
---

# Gyroscope

## 端口

### 输出

### **Port\_1** — 自上次启动或重置以来的偏航旋转（单位为 degrees）

沿陀螺仪传感器轴的偏航旋转，以 degrees 为单位。当您沿顺时针方向旋转陀螺仪传感器时，该值增大。当您沿逆时针方向旋转陀螺仪时，该值减小。

**数据类型：** `double`

## 参数

### **3-Wire Expander (smart port)** — 选择 3-Wire Expander 使用的 smart port `None`（默认） | `1` 到 `21`

如果您使用 3-Wire Expander，请指定 VEX® EDR V5 Robot Brain 上扩展器所连接的 smart port。

### **Port** — 陀螺仪连接到的 3-wire 端口 A（默认） | `B` | `C` | `D` | `E` | `F` | `G` | `H`

选择 VEX V5 Robot Brain 上陀螺仪连接到的 3-wire 端口。

### **Reset mode** — 用于重置陀螺仪传感器读数的重置模式 `No reset`（默认） | `Reset at each sample time` | `Reset by external signal`

- 在示例表中，假设模块采样时间为 1 second。在时刻 T = 0 时的旋转角度为 0 degrees。

  此模块支持的不同重置模式包括：

  - `No reset` – 陀螺仪读数不会重置，模块输出总旋转角度。

    例如，在表中，在 T = 1 时，陀螺仪传感器沿逆时针方向旋转 20 degrees，因此输出为 20。

    在 T = 1 和 T = 2 之间，陀螺仪传感器沿逆时针方向旋转 10 degrees。因此，在 T = 2 时偏航旋转为 30（来自 T = 1 的 20 和来自 T = 2 的 10）。

    在此重置模式下，任意时刻的输出是先前偏航旋转与当前偏航旋转的累积和。
  - `Reset at each sample time` – 对于每个采样周期，模块输出陀螺仪读数，然后将其重置为 0。

    例如，在表中，在 T = 1 时，陀螺仪传感器沿逆时针方向旋转 20 degrees，因此输出为 20。

    在 T = 1 和 T = 2 之间，陀螺仪传感器沿逆时针方向旋转 10 degrees，因此输出为 10。

    在此重置模式下，输出是特定时刻的偏航旋转。
  - `Reset by external signal` – 根据 `Rst` 端口的输入值将陀螺仪读数重置为 0。当您向模块输入发送非 0 值时，陀螺仪读数会重置为 0。对于每个采样周期，模块输出自上次重置以来的陀螺仪读数。

    例如，在表中，当外部信号为 0 时，输出的计算方式与 `No reset` 模式相同。当外部信号非零时，输出的计算方式与 `Reset at each sample time` 模式相同。

### **Sample time** — 模块读取值的时间间隔 `0.2`（默认） | 正标量 | -1

输入模块从陀螺仪读取值的时间间隔。

当您将此参数设置为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。如果在 **Reset mode** 参数中选择 `Reset by external signal` 选项，则 **Sample time** 参数会隐藏，并且该值会被继承（Sample time = -1）。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

表示已连接的陀螺仪并测量偏航角

Gyroscope 模块表示连接到 VEX V5 Robot brain 的 3-wire 端口的陀螺仪，并测量沿陀螺仪传感器偏航轴的角度（以 degrees 为单位）。

该模块以 double-precision 标量值的形式输出角度，单位为 degrees。当您沿顺时针方向旋转陀螺仪传感器时，角度增大。当您沿逆时针方向旋转传感器时，该值减小。

在启动程序时，不要移动机器人几秒钟，以便 Gyroscope 正确初始化。
