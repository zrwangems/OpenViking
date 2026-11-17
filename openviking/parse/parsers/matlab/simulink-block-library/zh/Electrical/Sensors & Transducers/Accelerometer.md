---
type: simulink-block
title: 'Accelerometer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'accelerometer'
documentation_source_path: 'ref/accelerometer.html'
language: zh-CN
chinese_source: worker-translation
---

# Accelerometer

## 端口
```yaml
ports:
- name: R
  summary: 平移端口 mechanical
  direction: unspecified
- name: +
  summary: 正端口 electrical
  direction: unspecified
- name: '-'
  summary: 负端口 electrical
  direction: unspecified
```

### 守恒

### **R** — 平移端口 mechanical

与加速度计平移端口关联的机械守恒端口。

### **+** — 正端口 electrical

与加速度计正极端子关联的电气守恒端口。

### **-** — 负端口 electrical

与加速度计负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Output type
  summary: 模块输出类型 Voltage level（默认）| PWM duty cycle
  group: ''
- name: Sensitivity
  summary: 灵敏度 1000 mV/gee（默认）
  group: ''
- name: Output voltage for zero acceleration
  summary: 零加速度时的输出电压 2.5 V（默认）
  group: ''
- name: Maximum output voltage
  summary: 最大输出电压 4 V（默认）
  group: ''
- name: Minimum output voltage
  summary: 最小输出电压 1 V（默认）
  group: ''
- name: Duty cycle sensitivity (percent per unit acceleration)
  summary: 占空比灵敏度 10 1/gee（默认）
  group: ''
- name: Duty cycle for zero acceleration (percent)
  summary: 零加速度时的占空比 50（默认）
  group: ''
- name: Maximum duty cycle (percent)
  summary: 最大占空比 75（默认）
  group: ''
- name: Minimum duty cycle (percent)
  summary: 最小占空比 25（默认）
  group: ''
- name: PWM frequency
  summary: PWM 频率 1000 Hz（默认）
  group: ''
- name: Output voltage amplitude
  summary: 输出电压幅值 5 V（默认）
  group: ''
- name: Dynamics
  summary: 动态特性 No dynamics — Suitable for HIL（默认）| Model sensor bandwidth
  group: ''
- name: Bandwidth
  summary: 带宽 3 kHz（默认）
  group: ''
```

### **Output type** — 模块输出类型 `Voltage level`（默认）| `PWM duty cycle`

选择以下选项之一来定义模块输出类型：

- `Voltage level` — 输出电压的幅值与测得的加速度成正比。这是默认选项。
- `PWM duty cycle` — 占空比（导通时间除以脉冲总时间）与测得的加速度成正比。

### **Sensitivity** — 灵敏度 `1000` `mV/gee`（默认）

当输出未受限制时，每单位加速度变化引起的输出电压电平变化。

#### 依赖关系

仅当为 **Output type** 参数选择 `Voltage level` 时，此参数才可见。

### **Output voltage for zero acceleration** — 零加速度时的输出电压 `2.5` `V`（默认）

加速度为零时传感器的输出电压。

#### 依赖关系

仅当为 **Output type** 参数选择 `Voltage level` 时，此参数才可见。

### **Maximum output voltage** — 最大输出电压 `4` `V`（默认）

传感器的最大输出电压，它决定了传感器可测得的最大正加速度。

#### 依赖关系

仅当为 **Output type** 参数选择 `Voltage level` 时，此参数才可见。

### **Minimum output voltage** — 最小输出电压 `1` `V`（默认）

传感器的最小输出电压，它决定了传感器可测得的最大负加速度。仅当为 **Output type** 参数选择 `Voltage level` 时，此参数才可见。默认值为 `1` V。

### **Duty cycle sensitivity (percent per unit acceleration)** — 占空比灵敏度 `10` `1/gee`（默认）

每单位加速度引起的占空比变化。占空比以 PWM 周期的百分比表示。

#### 依赖关系

仅当为 **Output type** 参数选择 `PWM duty cycle` 时，此参数才可见。

### **Duty cycle for zero acceleration (percent)** — 零加速度时的占空比 `50`（默认）

加速度为零时传感器输出的占空比。

#### 依赖关系

仅当为 **Output type** 参数选择 `PWM duty cycle` 时，此参数才可见。

### **Maximum duty cycle (percent)** — 最大占空比 `75`（默认）

传感器输出的最大占空比。加速度超过此点后，占空比将不再增加。

#### 依赖关系

仅当为 **Output type** 参数选择 `PWM duty cycle` 时，此参数才可见。

### **Minimum duty cycle (percent)** — 最小占空比 `25`（默认）

传感器输出的最小占空比。加速度低于此点后，占空比将不再减小。

#### 依赖关系

仅当为 **Output type** 参数选择 `PWM duty cycle` 时，此参数才可见。

### **PWM frequency** — PWM 频率 `1000` `Hz`（默认）

输出脉冲序列的频率。

#### 依赖关系

仅当为 **Output type** 参数选择 `PWM duty cycle` 时，此参数才可见。

### **Output voltage amplitude** — 输出电压幅值 `5` `V`（默认）

输出脉冲序列为高电平时的幅值。

#### 依赖关系

仅当为 **Output type** 参数选择 `PWM duty cycle` 时，此参数才可见。

### **Dynamics** — 动态特性 `No dynamics — Suitable for HIL`（默认）| `Model sensor bandwidth`

选择以下选项之一来对传感器动态特性进行建模：

- `No dynamics — Suitable for HIL` — 不对传感器动态特性进行建模。当以固定步长运行仿真或为硬件在环测试生成代码时，请使用此选项，因为当传感器带宽较高时，这可避免需要较小的仿真时间步长。这是默认选项。
- `Model sensor bandwidth` — 基于 **Bandwidth** 参数值，使用一阶滞后近似对传感器动态特性进行建模。您可以通过指定 **Measured acceleration** 变量目标来控制滞后的初始条件。

### **Bandwidth** — 带宽 `3` `kHz`（默认）

假设一阶时间常数，指定测得加速度的 3dB 带宽。

#### 依赖关系

仅当为 **Dynamics** 参数选择 `Model sensor bandwidth` 时，此参数才可见。
## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

MEMS 加速度计的行为模型

Accelerometer 模块实现了微机电系统（MEMS）加速度计的行为模型。对于默认输出类型 `Voltage level`，加速度计提供的输出电压与机械平移物理端口 R 处呈现的加速度成正比。输出电压根据您为最大和最小输出电压提供的值进行限制。

该模块还具有另一种输出类型 `PWM duty cycle`。选择此选项时，模块的输出是一个 PWM 信号，其占空比与测得的加速度成正比。您可以将占空比的变化限制在指定范围内。

您还可以选择通过将 **Dynamics** 参数设置为 `Model sensor bandwidth` 来对传感器动态特性进行建模。包含动态特性会在端口 R 处呈现的角速率与施加到电气 + 和 - 端口的相应电压之间添加一阶滞后。

如果使用固定步长求解器运行仿真，或为硬件在环测试生成代码，MathWorks 建议您将 **Dynamics** 参数设置为 `No dynamics — Suitable for HIL`，因为当传感器带宽较高时，这可避免需要较小的仿真时间步长。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

**Measured acceleration** 变量目标指定传感器的初始输出。
