---
type: simulink-block
title: 'Gyro'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'gyro'
documentation_source_path: 'ref/gyro.html'
language: zh-CN
chinese_source: worker-translation
---

# Gyro

## 端口

### 守恒

### **R** — 机械平动端口

与陀螺仪平动端口关联的机械守恒端口。

### **+** — 正电气端口

与陀螺仪正端子关联的电气守恒端口。

### **-** — 负电气端口

与陀螺仪负端子关联的电气守恒端口。

## 参数

### **Sensitivity** — 灵敏度 `12.5` `s*mV/deg` （默认）

当输出不受限时，每单位旋转速率变化对应的输出电压电平变化量。

### **Output voltage for zero rotation** — 零旋转时的输出电压 `2.5` `V` （默认）

当旋转速率为零时传感器的输出电压。

### **Maximum output voltage** — 最大输出电压 `4` `V` （默认）

传感器的最大输出电压，它决定传感器最大可测量的旋转速率。

### **Minimum output voltage** — 最小输出电压 `1` `V` （默认）

传感器的最小输出电压，它决定传感器最小可测量的旋转速率。

### **Dynamics** — 动态特性建模选项 `No dynamics — Suitable for HIL` （默认） | `Model sensor bandwidth`

为传感器动态特性建模选择以下选项之一：

- `No dynamics — Suitable for HIL` — 不对传感器动态特性建模。当以固定步长运行仿真或为硬件在环测试生成代码时使用此选项，因为如果传感器带宽较高，这可避免需要较小的仿真时间步长。这是默认选项。
- `Model sensor bandwidth` — 基于 **Bandwidth** 参数值，使用一阶滞后近似对传感器动态特性建模。你可以通过指定 **Measured angular rate** 变量目标来控制滞后的初始条件。

### **Bandwidth** — 带宽 `3` `kHz` （默认）

假设一阶时间常数，指定测得旋转速率的 3dB 带宽。

#### 依赖项

仅当为 **Dynamics** 参数选择 `Model sensor bandwidth` 时，此参数可见。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

MEMS 陀螺仪的行为模型

Gyro 模块实现微机电系统 (MEMS) 陀螺仪的行为模型。该陀螺仪提供与机械旋转物理端口 R 处呈现的角旋转速率成正比的输出电压。输出电压根据你为最大和最小输出电压提供的值进行限制。

可选地，你可以通过将 **Dynamics** 参数设置为 `Model sensor bandwidth` 来对传感器动态特性建模。包含动态特性会在端口 R 处呈现的角速率与施加到电气 + 和 - 端口的对应电压之间增加一阶滞后。

如果使用固定步长求解器运行仿真，或为硬件在环测试生成代码，MathWorks 建议将 **Dynamics** 参数设置为 `No dynamics — Suitable for HIL`，因为如果传感器带宽较高，这可避免需要较小的仿真时间步长。

### 变量

若要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅设置模块变量的优先级和初始目标。

使用标称值指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真稳健性。标称值可来自不同来源。其中一个来源是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅按标称值进行系统缩放。

**Measured angular rate** 变量目标指定传感器的初始输出。
