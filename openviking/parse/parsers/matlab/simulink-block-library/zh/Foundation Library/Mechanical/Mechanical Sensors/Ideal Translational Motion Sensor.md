---
type: simulink-block
title: 'Ideal Translational Motion Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanical Sensors'
documentation_page: 'idealtranslationalmotionsensor'
documentation_source_path: 'ref/idealtranslationalmotionsensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Ideal Translational Motion Sensor

## 端口
```yaml
ports:
- name: A
  summary: 加速度，m/s^2 物理信号
  direction: output
- name: V
  summary: 速度，m/s 物理信号
  direction: output
- name: P
  summary: 位置，m 物理信号
  direction: output
- name: R
  summary: 杆（正探头）机械平移
  direction: output
- name: C
  summary: 壳体（参考探头）机械平移
  direction: output
```

### 输出

### **A** — 加速度，m/s^2 物理信号

加速度的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Acceleration** 复选框。

### **V** — 速度，m/s 物理信号

速度的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Velocity** 复选框。

### **P** — 位置，m 物理信号

位置的物理信号输出端口。

#### 依赖

要启用此端口，请选中 **Position** 复选框。
### 守恒

### **R** — 杆（正探头）机械平移

与传感器正探头关联的机械平移守恒端口。

### **C** — 壳体（参考探头）机械平移

与传感器负（参考）探头关联的机械平移守恒端口。

#### 依赖

要启用此端口，请将 **Measurement reference** 参数设置为 `Difference`。
## 参数
```yaml
parameters:
- name: Measurement reference
  summary: 选择执行绝对测量还是相对测量 Difference（默认）| Absolute
  group: ''
- name: Acceleration
  summary: 控制输出端口可见性以测量加速度 关（默认）| 开
  group: ''
- name: Velocity
  summary: 控制输出端口可见性以测量速度 开（默认）| 关
  group: ''
- name: Position
  summary: 控制输出端口可见性以测量位置 开（默认）| 关
  group: ''
- name: Initial position
  summary: 传感器初始偏移 0 m（默认）
  group: ''
```

### **Measurement reference** — 选择执行绝对测量还是相对测量 `Difference`（默认）| `Absolute`

选择执行绝对测量还是相对测量：

- `Difference` — 测量端口 **R** 相对于端口 **C** 的加速度、速度和位置。
- `Absolute` — 禁用端口 **C**，并测量端口 **R** 相对于接地（内部参考节点）的加速度、速度和位置。

### **Acceleration** — 控制输出端口可见性以测量加速度 关（默认）| 开

选中此复选框将显示输出端口 **A**，可用于测量加速度。显示端口 **A** 还涉及额外计算，以基于速度测量加速度，因此该端口默认关闭。

### **Velocity** — 控制输出端口可见性以测量速度 开（默认）| 关

选中此复选框将显示输出端口 **V**，可用于测量速度。

### **Position** — 控制输出端口可见性以测量位置 开（默认）| 关

选中此复选框将显示输出端口 **P**，可用于测量位置。

### **Initial position** — 传感器初始偏移 `0 m`（默认）

传感器初始位置（偏移）。

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

### R2022b：测量加速度、相对于接地测量，以及以参数方式控制输出端口的可见性

模块增强功能包括：

- 新增一个物理信号输出端口 **A**，可用于测量加速度。
- 新增参数（**Acceleration**、**Velocity** 和 **Position**），用于控制物理信号输出端口的可见性，使您能够仅显示每个特定实例中实际用于测量的端口。此增强功能有助于提高模块图的可读性。此外，由于显示加速度测量端口涉及额外计算，该端口默认隐藏，建议除非需要测量加速度，否则不要显示该端口。
- 在以前的版本中，模块仅测量端口 **R** 相对于端口 **C** 的相对速度和位置。现在，新增的 **Measurement reference** 参数允许您禁用端口 **C** 并相对于接地（内部参考节点）进行测量。

这些增强功能对在以前版本中创建的模型没有兼容性影响。

## 描述

机械平移系统中的运动传感器

Ideal Translational Motion Sensor 模块表示一种设备，它将两个机械平移节点之间测量的跨变量转换为与加速度、速度或位置成比例的控制信号。您可以将初始位置（偏移）指定为模块参数。

该传感器是理想的，因为它不考虑惯性、摩擦、延迟、能量消耗等。

连接 **R** 和 **C** 是机械平移守恒端口，用于将模块连接到正在监测运动的节点。模块正方向为从端口 R 到端口 C。这意味着速度测量为 *v* = *v*R – *v*C，其中 *v*R、*v*C 分别是端口 **R** 和 **C** 处的绝对速度。**Measurement reference** 参数允许您禁用端口 **C** 并相对于接地进行测量。

连接 **A**、**V** 和 **P** 分别是加速度、速度和位置的物理信号输出端口。这些端口的可见性由模块参数控制。如果启用端口 **A**，模块将执行额外计算，以基于速度测量加速度。为避免不必要的模型复杂性，建议在模块的每个实例中仅启用实际用于测量的端口。
