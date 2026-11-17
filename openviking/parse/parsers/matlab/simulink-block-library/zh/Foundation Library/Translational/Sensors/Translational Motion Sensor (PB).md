---
type: simulink-block
title: 'Translational Motion Sensor (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Sensors'
documentation_page: 'translationalmotionsensorpb'
documentation_source_path: 'ref/translationalmotionsensorpb.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Motion Sensor (PB)

## 端口

### 输出

### **A** — 加速度，m/s^2 物理信号

加速度的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **Acceleration** 复选框。

### **V** — 速度，m/s 物理信号

速度的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **Velocity** 复选框。

### **P** — 位置，m 物理信号

位置的物理信号输出端口。

#### 依赖关系

要启用此端口，请选中 **Position** 复选框。

### 守恒

### **B** — 基座端口，基于位置的机械平移

基于位置的机械平移守恒端口，表示基座连接。

### **F** — 从动端口，基于位置的机械平移

基于位置的机械平移守恒端口，表示从动连接。

#### 依赖关系

要启用此端口，请将 **Measurement reference** 参数设置为 `Difference`。

## 参数

### **Measurement reference** — 选择执行绝对测量还是相对测量 `Difference`（默认）| `Absolute`

选择执行绝对测量还是相对测量：

- `Difference` — 测量端口 **F** 相对于端口 **B** 的加速度、速度和位置。
- `Absolute` — 禁用端口 **B**，并测量端口 **F** 相对于世界坐标系的加速度、速度和位置。

### **Acceleration** — 控制输出端口可见性以测量加速度 off（默认）| on

选中此复选框将显示输出端口 **A**，可用于测量加速度。显示端口 **A** 还涉及额外的计算，以基于速度测量加速度，因此该端口默认关闭。

### **Velocity** — 控制输出端口可见性以测量速度 on（默认）| off

选中此复选框将显示输出端口 **V**，可用于测量速度。

### **Position** — 控制输出端口可见性以测量位置 on（默认）| off

选中此复选框将显示输出端口 **P**，可用于测量位置。

## 所属库

Simscape / Foundation Library / Translational / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

基于位置的机械平移系统中的运动传感器

Translational Motion Sensor (PB) 模块测量基于位置的平移网络中的绝对或相对位置、速度和加速度。当端口 **F** 处的运动大于端口 **B** 处时，测量值为正。传感器不对网络施加力。

连接 **B** 和 **F** 是基于位置的机械平移守恒端口。

连接 **A**、**V** 和 **P** 分别是加速度、速度和位置的物理信号输出端口。这些端口的可见性由模块参数控制。如果启用端口 **A**，模块将执行额外计算，以基于速度测量加速度。为避免不必要的模型复杂性，建议在模块的每个实例中仅启用实际用于测量的端口。
