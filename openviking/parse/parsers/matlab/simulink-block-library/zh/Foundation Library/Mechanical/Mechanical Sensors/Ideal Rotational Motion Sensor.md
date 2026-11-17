---
type: simulink-block
title: 'Ideal Rotational Motion Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanical Sensors'
documentation_page: 'idealrotationalmotionsensor'
documentation_source_path: 'ref/idealrotationalmotionsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Ideal Rotational Motion Sensor

## 端口
```yaml
ports:
- name: α
  summary: 加速度，rad/s^2 物理信号
  direction: output
- name: W
  summary: 角速度，rad/s 物理信号
  direction: output
- name: A
  summary: 位置（角位移），rad 物理信号
  direction: output
- name: R
  summary: 杆（正探头）机械旋转
  direction: output
- name: C
  summary: 壳体（参考探头）机械旋转
  direction: output
```

### 输出

### **α** — 加速度，rad/s^2 物理信号

角加速度的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Acceleration** 复选框。

### **W** — 角速度，rad/s 物理信号

角速度的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Velocity** 复选框。

### **A** — 位置（角位移），rad 物理信号

角位移的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Position** 复选框。
### 守恒

### **R** — 杆（正探头）机械旋转

与传感器正探头关联的机械旋转守恒端口。

### **C** — 壳体（参考探头）机械旋转

与传感器负（参考）探头关联的机械旋转守恒端口。

#### 依赖

要启用此端口，请将 **Measurement reference** 参数设置为 `Difference`。
## 参数
```yaml
parameters:
- name: Measurement reference
  summary: 选择执行绝对测量还是相对测量 Difference（默认）| Absolute
  group: ''
- name: Acceleration
  summary: 控制输出端口可见性以测量角加速度 off（默认）| on
  group: ''
- name: Velocity
  summary: 控制输出端口可见性以测量角速度 on（默认）| off
  group: ''
- name: Position
  summary: 控制输出端口可见性以测量角位移 on（默认）| off
  group: ''
- name: Wrap angle to [0, 2\*pi]
  summary: 控制角位移的输出范围 off（默认）| on
  group: ''
- name: Initial angle
  summary: 传感器初始偏移 0 rad（默认）
  group: ''
```

### **Measurement reference** — 选择执行绝对测量还是相对测量 `Difference`（默认）| `Absolute`

选择执行绝对测量还是相对测量：

- `Difference` — 测量端口 **R** 相对于端口 **C** 的加速度、速度和位置。
- `Absolute` — 禁用端口 **C**，并测量端口 **R** 相对于接地（内部参考节点）的加速度、速度和位置。

### **Acceleration** — 控制输出端口可见性以测量角加速度 off（默认）| on

选中此复选框将显示输出端口 **α**，可用于测量角加速度。显示端口 **α** 还涉及额外计算，以基于速度测量加速度，因此该端口默认关闭。

### **Velocity** — 控制输出端口可见性以测量角速度 on（默认）| off

选中此复选框将显示输出端口 **W**，可用于测量角速度。

### **Position** — 控制输出端口可见性以测量角位移 on（默认）| off

选中此复选框将显示输出端口 **A**，可用于测量位置（角位移）。

### **Wrap angle to [0, 2\*pi]** — 控制角位移的输出范围 off（默认）| on

当设置为 `On` 时，无论物体执行的旋转圈数和旋转方向如何，传感器输出的角位移均保持在 0 到 2π 弧度（360 度）范围内。当设置为 `Off` 时，输出范围不受限制。

选中此复选框可简化模型参数与旋转角度之间关系复杂的模型开发，例如泵和电机。

#### 依赖

要启用此参数，请选中 **Position** 复选框。

### **Initial angle** — 传感器初始偏移 `0 rad`（默认）

传感器初始角位置（偏移）。

#### 依赖

要启用此参数，请选中 **Position** 复选框。
## 所属库

Simscape / Foundation Library / Mechanical / Mechanical Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2022b：测量加速度、相对于地面测量，以及以参数化方式控制输出端口的可见性

模块增强包括：

- 新增一个物理信号输出端口 **α**，可用于测量角加速度。
- 新增参数（**Acceleration**、**Velocity** 和 **Position**），用于控制物理信号输出端口的可见性，使您能够仅暴露每个特定实例中实际用于测量的端口。此增强有助于提高框图的可读性。此外，由于暴露加速度测量端口会涉及额外计算，该端口默认隐藏，建议除非需要测量加速度，否则不要暴露该端口。
- 在之前的版本中，这些模块仅测量端口 **R** 相对于端口 **C** 的相对速度和位置。现在，新增的 **Measurement reference** 参数允许您禁用端口 **C**，并相对于地面（内部参考节点）进行测量。

这些增强对在之前版本中创建的模型没有兼容性影响。

## 描述

机械旋转系统中的运动传感器

Ideal Rotational Motion Sensor 模块表示一个理想的机械旋转运动传感器，即一种将两个机械旋转节点之间测量的跨变量转换为与加速度、角速度或位置（角度）成比例的控制信号的设备。您可以将初始角位置（偏移）指定为模块参数。

该传感器是理想的，因为它不考虑惯性、摩擦、延迟、能量消耗等。

连接 **R** 和 **C** 是机械旋转守恒端口，用于将模块连接到正在监测运动的节点。模块正方向为从端口 R 到端口 C。这意味着速度按 *ω* = *ω*R – *ω*C 测量，其中 *ω*R、*ω*C 分别是端口 **R** 和 **C** 处的绝对角速度。**Measurement reference** 参数允许您禁用端口 **C**，并相对于地面进行测量。

连接 **α**、**W** 和 **A** 分别是角加速度、速度和位移的物理信号输出端口。这些端口的可见性由模块参数控制。如果启用端口 **α**，模块将执行额外计算，以基于速度测量加速度。为避免不必要的模型复杂性，建议在模块的每个实例中仅启用您实际用于测量的端口。

**Wrap angle to [0, 2\*pi]** 复选框允许您控制角位移输出范围。选中时，无论物体执行的转数和旋转方向如何，它都会将角位移保持在 0 到 2π 弧度（360 度）的范围内。清除此复选框时，输出范围不受限制。

该图展示了这两个选项之间的差异。

传感器输出的两个图。

在此示例中，物体在前 5 秒内以 6 rad/s 沿正方向运动，然后以相同速度切换到负方向。默认角位移输出（线 1）显示物体向前转动了 30 rad，然后沿负方向转回，持续到 –20 rad。如果选中 **Wrap angle to [0, 2\*pi]** 复选框，输出（线 2）将保持在 0 到 2π rad 的范围内。

选中 **Wrap angle to [0, 2\*pi]** 复选框可简化模型参数与旋转角度之间关系复杂的模型（如泵和电机）的开发。
