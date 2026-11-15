---
type: simulink-block
title: 'VR to MATLAB Coordinates'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrtomatlabcoordinates'
documentation_source_path: 'vrtomatlabcoordinates.html'
language: zh-CN
chinese_source: worker-translation
---

# VR to MATLAB Coordinates

## 端口

### 输入

### **VR** — 虚拟世界坐标系中的坐标 3 元素向量

点的坐标采用 VRML 表示法，指定为 3 元素行向量。

**数据类型：** `single` | `double`
### 输出

### **M** — MATLAB 坐标系中的坐标 3 元素向量

点的坐标采用 MATLAB 表示法，以 3 元素行向量形式返回。

**数据类型：** `single` | `double`

## 参数

未在 R2025b 中记录。

## 所属库

Simulink 3D Animation / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2023b：将被移除

`VR to MATLAB Coordinates` 将在未来版本中移除。请改用 `sim3d` 类和 Simulation 3D 模块，将 MATLAB 和 Simulink® 与 Unreal Engine® 3D 仿真环境对接。要开始使用，请参阅在 Unreal Engine 环境中创建 3D 仿真。

## 描述

（将被移除）将 VR 坐标转换为 MATLAB 坐标

VR to MATLAB Coordinates 模块将虚拟世界坐标系 (Znear) 中坐标表示的点转换为 MATLAB® 坐标系 (Zup) 中的点。

两个坐标系之间存在以下关系：

[*xm*,
*ym*,
*zm*] =
[*xv*,
-*zv*,
*yv*]

其中，MATLAB 坐标以下标 *m* 表示，虚拟世界坐标以下标 *v* 表示。
