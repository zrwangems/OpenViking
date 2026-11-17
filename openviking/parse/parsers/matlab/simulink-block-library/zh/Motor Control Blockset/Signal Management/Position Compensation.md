---
type: simulink-block
title: 'Position Compensation'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Signal Management'
documentation_page: 'positioncompensation'
documentation_source_path: 'ref/positioncompensation.html'
language: zh-CN
chinese_source: worker-translation
---

# Position Compensation

## 端口
```yaml
ports:
- name: θin
  summary: 位置输入值 标量
  direction: input
  data_types: single | double | fixed point
- name: ϕ
  summary: 位置偏移 标量
  direction: input
  data_types: single | double | fixed point
- name: ω
  summary: 角速度 标量
  direction: input
  data_types: single | double | fixed point
- name: θout
  summary: 位置输出值 标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **θin** — 位置输入值 标量

需要进行偏移校正的位置输入值。此端口支持以下值范围：

- -2π 至 +2π 弧度
- 0 至 1 标幺值
- -360 至 +360 度

**数据类型：** `single` | `double` | `fixed point`

### **ϕ** — 位置偏移 标量

外部计算的位置偏移值。此值必须与 *θin* 输入具有相同的单位。此端口支持以下值范围：

- -2π 至 +2π 弧度
- 0 至 1 标幺值
- -360 至 +360 度

#### 依赖关系

要启用此端口，请将 **Nature of offset** 参数设置为 `External delay`。

**数据类型：** `single` | `double` | `fixed point`

### **ω** — 角速度 标量

外部计算的角速度。此值表示 *θin* 输入的变化。

#### 依赖关系

要启用此端口，请将 **Nature of offset** 参数设置为 `Sample delay`、`High-pass filter delay` 或 `Low-pass filter delay`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **θout** — 位置输出值 标量

经过偏移校正的位置输出值。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Nature of offset
  summary: 偏移类型 Sample delay（默认）| Constant delay | External delay | High-pass filter delay | Low-pass filter delay
  group: ''
- name: Offset value
  summary: 位置偏移值 0.1（默认）| 标量
  group: ''
- name: Number of sample delay
  summary: 模块执行时间采样数 1（默认）| 标量
  group: ''
- name: Discrete step size (s)
  summary: 模块再次执行的采样时间 50e-6（默认）| 标量
  group: ''
- name: Cut-off frequency (Hz)
  summary: 滤波器截止频率 9.578（默认）| 标量
  group: ''
- name: Position unit
  summary: 位置输入的单位 Radians（默认）| Degrees | Per unit
  group: ''
- name: Speed unit
  summary: 角速度输入的单位 RPM（默认）| Degrees/Sec | Radians/Sec | Per unit
  group: ''
- name: Maximum application speed (RPM)
  summary: 角速度上限 4000（默认）| 标量
  group: ''
```

### **Nature of offset** — 偏移类型 `Sample delay`（默认）| `Constant delay` | `External delay` | `High-pass filter delay` | `Low-pass filter delay`

系统中需要补偿的延迟或偏移类型。选择以下值之一：

- Constant delay — 补偿固定延迟或偏移。
- External delay — 使用外部计算的位置偏移值补偿恒定延迟。
- Sample delay — 基于离散步长或模块执行时间补偿延迟。
- High-pass filter delay — 使用截止频率值补偿一阶巴特沃斯高通滤波器的延迟。
- Low-pass filter delay — 使用截止频率值补偿一阶巴特沃斯低通滤波器的延迟。

### **Offset value** — 位置偏移值 `0.1`（默认）| 标量

系统中恒定延迟的位置偏移。

#### 依赖关系

要启用此参数，请将 **Nature of offset** 设置为 `Constant delay`。

### **Number of sample delay** — 模块执行时间采样数 `1`（默认）| 标量

模块用于位置偏移补偿的模块执行时间采样数。

#### 依赖关系

要启用此参数，请将 **Nature of offset** 设置为 `Sample delay`。

### **Discrete step size (s)** — 模块再次执行的采样时间 `50e-6`（默认）| 标量

模块连续执行实例之间的固定时间间隔（以秒为单位）。

#### 依赖关系

要启用此参数，请将 **Nature of offset** 设置为 `Sample delay`。

### **Cut-off frequency (Hz)** — 滤波器截止频率 `9.578`（默认）| 标量

一阶巴特沃斯高通或低通滤波器的截止频率。

#### 依赖关系

要启用此参数，请将 **Nature of offset** 设置为 `High-pass filter delay` 或 `Low-pass filter delay`。

### **Position unit** — 位置输入的单位 `Radians`（默认）| `Degrees` | `Per unit`

位置输入 *θin* 的单位。

### **Speed unit** — 角速度输入的单位 `RPM`（默认）| `Degrees/Sec` | `Radians/Sec` | `Per unit`

角速度输入 *ω* 的单位。

#### 依赖关系

要启用此参数，请将 **Nature of offset** 设置为 `Sample delay`、`High-pass filter delay` 或 `Low-pass filter delay`。

### **Maximum application speed (RPM)** — 角速度上限 `4000`（默认）| 标量

角速度输入 *ω* 的上限或最大可能值，以 RPM 为单位。

#### 依赖关系

要启用此参数，请将 **Nature of offset** 设置为 `Sample delay`、`High-pass filter delay` 或 `Low-pass filter delay`。
## 所属库

Motor Control Blockset / Signal Management

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2022b 中引入**

## 描述

补偿由不同类型延迟引起的位置偏移

Position Compensation 模块补偿系统中由不同类型延迟引起的位置偏移。

电机控制算法可能由于延迟和滤波器等不同算法实体而在计算位置中引入偏移。这些偏移会影响磁场定向控制 (FOC) 和直接转矩控制 (DTC) 等电机控制算法的精度。您可以使用此模块来补偿电机控制算法中的偏移。

该模块使用以下计算进行采样延迟补偿。

延迟引入的偏移 = 应用的补偿 = (− 采样时间) × (延迟数量) × (角速度) 弧度

该模块使用以下计算进行一阶巴特沃斯高通和低通滤波器补偿。

- 对于高通滤波器：

  相位偏移=π2−arctan(ωspeedωcutoff)=arctan(ωcutoffωspeed)

  相位补偿=−arctan(ωcutoffωspeed)
- 对于低通滤波器：

  相位偏移=−arctan(ωspeedωcutoff)

  相位补偿=arctan(ωspeedωcutoff)
