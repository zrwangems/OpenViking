---
type: simulink-block
title: 'Driver Commands'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Virtual Vehicles'
documentation_page: 'drivercommandsvirtualvehiclemodels'
documentation_source_path: 'ref/drivercommandsvirtualvehiclemodels.html'
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

### **Env** — 环境信号 `Bus`

包含环境信号的 Bus。

### 输出

### **Driver** — 命令信号 `Bus`

包含命令的 Bus，包括转向、加速、制动和挡位命令。

## 参数

### **Vehicle command mode** — 启用 3D 可视化 `Longitudinal Driver`（默认） | `Predictive Driver` | `Predictive Stanley Driver` | `Open Loop` | `Dashboard Widgets` | `Game Wheel Hardware` | `No Driver`

指定驾驶员模型。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2024b 中引入**

## 描述

在已配置的虚拟车辆模型和 Powertrain Blockset 参考应用中配置驾驶员

Driver Commands 子系统实现驾驶员模型，该模型生成加速、制动、挡位和转向命令。该子系统包含与典型驾驶员车辆输入（如转向、加速器、减速器和变速器命令）交互的变体。这些变体包括适用于纵向和横向参考跟踪、游戏硬件、交互式画布小部件以及直通或外部信号输入的驾驶员模型。

| 车辆命令模式设置 | 实现 |
| --- | --- |
| `Longitudinal Driver` | Longitudinal Driver 模块 — 纵向速度跟踪控制器。基于参考速度和反馈速度，该模块生成可在 0 到 1 之间变化的归一化加速和制动命令。使用该模块可对驾驶员的动态响应建模，或生成跟踪纵向驾驶循环所需的命令。  **注意**  `Longitudinal Driver` 设置是 Powertrain Blockset™ 参考应用中实现的唯一配置。 |
| `Predictive Driver` | Predictive Driver (Vehicle Dynamics Blockset) 模块 — 控制器，生成归一化转向、加速和制动命令，以跟踪纵向速度和横向参考位移。归一化命令可在 -1 到 1 之间变化。该控制器使用单轨（自行车）模型进行最优单点预瞄控制。 |
| `Predictive Stanley Driver` | Predictive Driver (Vehicle Dynamics Blockset) 模块 — 控制器，生成归一化转向、加速和制动命令，以跟踪纵向速度和横向参考位移。对于横向控制，实现 Stanley 方法。 |
| `Open Loop` | 实现开环系统，以便您可以为参考应用配置恒定或基于信号的转向、加速、制动和挡位命令输入。 |
| `Dashboard Widgets` | 实现用于加速器和制动控制的仪表板小部件。 |
| `Game Wheel Hardware` | 实现用于 3D 仿真的游戏方向盘。需要 Simulink® 3D Animation™。 |
| `No Driver` | 未实现驾驶员。 |
