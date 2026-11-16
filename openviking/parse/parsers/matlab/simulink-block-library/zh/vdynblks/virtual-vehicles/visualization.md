---
type: simulink-block
title: 'Visualization'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Virtual Vehicles'
documentation_page: 'visualization'
documentation_source_path: 'ref/visualization.html'
language: zh-CN
chinese_source: worker-translation
---

# Visualization

## 端口

### 输入

### **Vis** — 可视化参考信号 `Bus`

Bus 包含可视化参考信号，包括纵向和横向位移以及转向。

### **VehRef** — 车辆参考信号 `Bus`

Bus 包含车辆参考信号，包括纵向和横向位移以及转向。

### **Fdbk** — 车辆位置反馈信号 `Bus`

Bus 包含车辆位移反馈信号。

### 输出

### **ExtVehFdbk** — 命令信号 `Bus`

Bus 包含命令，包括转向、加速、制动和挡位命令。

#### 依赖项

要创建此端口，请选择 **Vehicle feedback**。

## 参数

### **Vehicle feedback** — 启用车辆反馈输出端口 `off`（默认）| `on`

指定创建顶层模型非虚拟总线端口反馈输出端口 `ExtVehFdbk`，其中包含车辆系统信号。考虑选择此项，以使模型与其他系统一起仿真时信号可用。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2024b 中引入**

## 描述

配置可视化

Visualization 子系统包含信号记录、示波器和其他可视化功能。选择 **Vehicle feedback** 会创建顶层模型非虚拟总线端口，使常用车辆系统信号在模型与其他系统一起仿真时可用。
