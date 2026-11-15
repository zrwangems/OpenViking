---
type: simulink-block
title: 'VR Placeholder'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrplaceholder'
documentation_source_path: 'vrplaceholder.html'
language: zh-CN
chinese_source: worker-translation
---

# VR Placeholder

## 端口

### 输出

### **Output 1** — 输出信号 real scalar | real vector

输出信号以未指定值返回，用于驱动虚拟现实可视化。

**数据类型：** `double`

## 参数

### **Output width** — 向量 `1` 的长度（默认值）

包含占位符信号值的向量的长度。

## 所属库

Simulink 3D Animation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2006a 之前引入**

### R2023b：将被移除

`VR Placeholder` 将在未来版本中移除。请改用 `sim3d` 类和 Simulation 3D 模块，将 MATLAB® 和 Simulink® 与 Unreal Engine® 3D 仿真环境对接。要开始使用，请参阅 Create 3D Simulations in Unreal Engine Environment。

## 描述

（将移除）向 Simulink 3D Animation 模块发送未指定值

VR Placeholder 模块发出一个特殊值，该值会被 VR Sink 模块解释为“未指定”。当此值出现在 VR Sink 输入上时，无论它是作为单个值还是作为向量的一个元素，虚拟世界中对应的值都保持不变。使用此模块可以只更改较大向量中的一个值。例如，使用此模块只更改三维位置中的一个坐标。

VR Placeholder 模块输出的值在用于其他 VR 模块之前不应修改。

要打开“模块参数”对话框，请双击该模块。
