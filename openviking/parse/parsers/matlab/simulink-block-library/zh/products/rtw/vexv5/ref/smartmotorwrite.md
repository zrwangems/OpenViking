---
type: simulink-block
title: 'Smart Motor Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / VEX EDR V5 Robot Brain / Modeling / Actuators'
documentation_page: 'smartmotorwrite'
documentation_source_path: 'vexv5/ref/smartmotorwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Smart Motor Write

## 端口

### 输入

### **Velocity** — 输入模拟信号，用于设置电机速度 RPM，整数，范围为 [–100 100]

Smart Block Write 模块的输入速度范围为 –100 到 100。符号决定电机旋转方向，幅值决定以 RPM 为单位的速度。正值使电机顺时针旋转，负值使电机逆时针旋转。模块输入值 `0` 会停止电机。

对于超出 -100 到 100 范围的输入速度值，模块按幅值 100 提供功率。

**数据类型：** `double`

### **Position** — 设置目标电机位置的编码器 tick 计数整数

Position 输入以 tick 计数为单位设置电机的目标位置。当此输入值等于 V5 Smart Motor 内置编码器的 tick 计数时，即达到电机的目标位置。

例如，要在 2 圈后停止电机：

- 对于 36:1 的齿轮比，将 Position 输入设置为 `3600`
- 对于 18:1 的齿轮比，将 Position 输入设置为 `1800`
- 对于 6:1 的齿轮比，将 Position 输入设置为 `600`

#### 依赖关系

仅当将 **Control mode** 参数设置为 `Position Control` 时，此输入才会出现。

**数据类型：** `double`

## 参数

### **Smart Port** — 选择 V5 Smart Motor 连接到的 Smart Port 1（默认）| `1` 到 `21`

选择 VEX EDR V5 Robot Brain 上 V5 Smart Motor 所连接到的 Smart Port。VEX EDR V5 Robot Brain 上有 21 个 Smart Port 可用于连接 V5 Smart Motor。

模型中的每个模块必须具有唯一的 Smart Port。如果使用多个具有相同端口的 Smart Motor Write 模块，则可能只有最后执行的 Smart Motor Write 模块处于活动状态。对于 Vex Robotics Competition，可以在 driver mode 或 autonomous mode 中使用具有相同 Smart Port 的同一 Smart Motor Write 模块。

### **Gearing Ratio** — 选择 V5 Smart Motor 的齿轮比 36:1（默认）| `18:1` | `6:1`

选择用于驱动 V5 Smart Motor 的内部齿轮比。

### **Braking mode** — 选择 V5 Smart Motor 的制动模式 `Coast`（默认）| `Brake` | `Hold`

选择与 V5 Smart Motor 所用制动机制相匹配的制动模式：

- l`Coast` – 将电机设置为滑行至停止
- l`Brake` – 将电机设置为通过施加制动立即停止
- l`Hold` – 将电机设置为通过施加制动立即停止，并尝试保持其位置

### **Control mode** — 选择 V5 Smart Motor 的控制模式 `Velocity Control`（默认）| `Position Control`

选择控制模式，以在速度控制与位置控制之间切换，或反之。

当选择 `Position Control` 时，会增加一个附加输入 – `Position` –，该输入用于设置电机的目标位置。

`Position Control` 模式用于将电机轴转动到编码器 tick 值（对应一个角度）。例如，将机械爪打开到某个角度。`Velocity control` 模式用于需要连续运动范围的情况。例如，控制传动系统电机。

## 所属库

Simulink Coder Support Package for VEX EDR V5 Robot Brain / Actuators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018b 中引入**

## 描述

表示已连接的 V5 Smart Motor 并设置其速度和位置

Smart Motor Write 模块表示连接到 VEX® EDR V5 Robot Brain 上指定端口的 V5 Smart Motor，并设置该电机的速度和位置。
