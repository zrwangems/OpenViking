---
type: simulink-block
title: 'Straight Maneuver Reference Generator'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'straightmaneuverreferencegenerator'
documentation_source_path: 'ref/straightmaneuverreferencegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Straight Maneuver Reference Generator

## 端口

### 输入

### **VehFdbk** — 车辆反馈 `Bus`

包含车辆反馈信号的 Bus，包括速度、加速度和方向盘扭矩。

### 输出

### **Ref** — 车辆参考信号 `Bus`

包含车辆参考信号的 Bus，包括纵向和横向位移以及转向。

## 参数

#### 机动参数

### **机动开始时间，t\_start** — 开始时间 `2`（默认）| `scalar`

机动开始时间，单位为 s。

### **在 t\_start 处的纵向加速度，ax** — 纵向加速度 `0.5`（默认）| `scalar`

机动开始时的纵向加速度，单位为 g。

### **纵向速度参考，xdot\_r** — 纵向速度参考，xdot\_r `20`（默认）| `scalar`

纵向速度参考，xdot\_r，单位由 **速度单位，xdotUnit** 指定。

### **速度单位，xdotUnit** — 单位 `m/s`（默认）| `km/h` | `char`

速度的单位。

### **制动踏板操作** — 减速度触发 `Longitudinal displacement`（默认）| `Time`

开始减速的方法。

选择 `Longitudinal displacement` 以指定开始使车辆减速的位移。

选择 `Time` 以指定开始使车辆减速的时间。

### **车辆 CG 的纵向位移，x\_brake** — 位移 `200`（默认）| `scalar`

开始减速时车辆 CG 的纵向位移，单位为 m。

#### 依赖关系

要启用此参数，请将 **制动踏板操作** 设置为 `Longitudinal displacement`。

### **制动操作时间，t\_brake** — 时间 `15`（默认）| `scalar`

开始减速的时间，单位为 s。

#### 依赖关系

要启用此参数，请将 **制动踏板操作** 设置为 `Time`。

### **在 t\_brake 处的纵向减速度，ax\_dec** — 减速度 `1`（默认）| `scalar`

制动时的纵向减速度，单位为 g。

### **传输延迟缓冲区大小，BufferSize** — 缓冲区 `4096`（默认）| `scalar`

传输延迟缓冲区大小。

### **制动后将方向盘转角设为 0 deg** — 选择 `on`（默认）| `off`

制动后将方向盘转角设为 0。

#### 跟踪参数

### **启用制动前故障跟踪** — 启用故障跟踪 `on`（默认）| `off`

选择此参数以启用制动前故障跟踪。在 split-mu 测试期间，使用这些参数指定制动前的故障条件。如果制动前车速、转向角或横摆角速度不在允许范围内，模块会设置故障条件。默认值表示符合 ISO 145121。

### **纵向速度和平均纵向速度，xdot\_rmax** — 最大速度容差 `1`（默认）| `scalar`

纵向速度和平均纵向速度容差。如果纵向速度或平均纵向速度超出允许范围，模块会设置故障条件。

#### 依赖关系

要启用此参数，请在 **跟踪参数** 选项卡上选择 **启用制动前故障跟踪**。

### **平均纵向速度和纵向速度参考，xdot\_rmean** — 平均速度容差 `2`（默认）| `scalar`

平均纵向速度和纵向速度参考容差。如果平均纵向速度或纵向速度超出允许范围，模块会设置故障条件。

#### 依赖关系

要启用此参数，请在 **跟踪参数** 选项卡上选择 **启用制动前故障跟踪**。

### **横摆角速度和平均横摆角速度，r\_max** — 横摆角速度容差 `1`（默认）| `scalar`

横摆角速度和平均横摆角速度容差，单位为 deg/s。如果横摆角速度或平均横摆角速度超出允许范围，模块会设置故障条件。

#### 依赖关系

要启用此参数，请在 **跟踪参数** 选项卡上选择 **启用制动前故障跟踪**。

### **方向盘转角和平均方向盘转角，hw\_max** — 方向盘转角容差 `3`（默认）| `scalar`

方向盘转角和平均方向盘转角，单位为 deg。如果方向盘转角或平均方向盘转角超出允许范围，模块会设置故障条件。

#### 依赖关系

要启用此参数，请在 **跟踪参数** 选项卡上选择 **启用制动前故障跟踪**。

### **发生故障时停止仿真** — 选择以停止仿真 `off`（默认）| `on`

选择此参数以在发生故障时停止仿真。

#### 依赖关系

要启用此参数，请在 **跟踪参数** 选项卡上选择 **启用制动前故障跟踪**。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

生成直线机动参考信号

Straight Maneuver Reference Generator 模块生成加速和制动命令，以执行制动测试的直线机动。加速度以指定速率开始，直到车辆达到纵向速度设定值。车辆控制器在指定的时间或距离内保持纵向速度设定值。然后控制器使车辆减速。

使用 **机动参数** 指定机动开始时间、速度设定值、加速度和减速度。

可选地，在 **跟踪参数** 选项卡上，选择 **启用制动前故障跟踪**。在 split-mu 测试期间，使用这些参数指定制动前的故障条件。如果制动前车速、转向角或横摆角速度不在允许范围内，模块会设置故障条件。默认值表示符合 ISO 145121。
