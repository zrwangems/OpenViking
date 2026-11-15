---
type: simulink-block
title: 'Driver Commands'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Vehicle Reference Applications'
documentation_page: 'drivercommands'
documentation_source_path: 'ref/drivercommands.html'
language: zh-CN
chinese_source: worker-translation
---

# Driver Commands

## 端口

### 输入

### **VehRef** — 车辆参考信号 `Bus`

包含车辆参考信号的 Bus，包括纵向和横向位移以及转向。

### **VehFdbk** — 车辆反馈信号 `Bus`

包含车辆位移反馈信号的 Bus。

### **Steer** — 转向角标量

转向角，指定为标量。

#### 依赖项

要启用此端口，请将 **Vehicle command mode** 设置为 `Open Loop`。

### **Accel** — 车辆加速度标量

车辆加速度，指定为标量。

#### 依赖项

要启用此端口，请将 **Vehicle command mode** 设置为 `Open Loop`。

### **Brake** — 车辆减速度标量

车辆减速度，指定为标量。

#### 依赖项

要启用此端口，请将 **Vehicle command mode** 设置为 `Open Loop`。

### **Gear** — 车辆挡位标量

车辆挡位，指定为标量。

#### 依赖项

要启用此端口，请将 **Vehicle command mode** 设置为 `Open Loop`。

### 输出

### **Driver** — 命令信号 `Bus`

包含这些转向、加速、制动和挡位命令的 Bus。

| 信号 | 描述 |
| --- | --- |
| `SteerCmd` | 指令转向角。 |
| `AccelCmd` | 指令车辆加速度。 |
| `DecelCmd` | 指令车辆减速度。 |
| `GearCmd` | 指令车辆挡位。 |

## 参数

### **Vehicle command mode** — 启用 3D 可视化 `Predictive Driver`（默认） | `Longitudinal Driver` | `Open Loop`

指定驾驶员模型。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

配置驾驶员

Driver Commands 模块实现参考应用用于生成加速、制动、挡位和转向命令的驾驶员模型。默认情况下，如果选择 Reference Generator 模块参数 **Use maneuver-specific driver, initial position, and scene**，则参考应用会为指定的机动选择驾驶员。

| 车辆命令模式设置 | 实现 |
| --- | --- |
| `Longitudinal Driver` | Longitudinal Driver 模块 — 纵向速度跟踪控制器。基于参考速度和反馈速度，该模块生成归一化加速和制动命令，其范围可从 0 到 1。使用该模块对驾驶员的动态响应建模，或生成跟踪纵向驾驶循环所需的命令。 |
| `Predictive Driver`（默认） | Predictive Driver 模块 — 生成归一化转向、加速和制动命令以跟踪纵向速度和横向参考位移的控制器。归一化命令可在 -1 到 1 之间变化。该控制器使用单轨（自行车）模型进行最优单点预瞄控制。 |
| `Open Loop` | 实现开环系统，以便你可以为参考应用配置恒定或基于信号的转向、加速、制动和挡位命令输入。 |
