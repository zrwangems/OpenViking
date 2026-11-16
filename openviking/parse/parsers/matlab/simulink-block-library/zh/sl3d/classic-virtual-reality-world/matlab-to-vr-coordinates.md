---
type: simulink-block
title: 'MATLAB to VR Coordinates'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'matlabtovrcoordinates'
documentation_source_path: 'matlabtovrcoordinates.html'
language: zh-CN
chinese_source: worker-translation
---

# MATLAB to VR Coordinates

## 端口

### 输入

### **M** — MATLAB 表示法中的坐标 3 元素向量

MATLAB 表示法中的点坐标，指定为 3 元素行向量。

**数据类型：** `single` | `double`
### 输出

### **VR** — VRML 表示法中的坐标 3 元素向量

VRML 表示法中的点坐标，以 3 元素行向量形式返回。

**数据类型：** `single` | `double`

## 参数

R2025b 中未记录。

## 所属库

Simulink 3D Animation / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

### R2023b：将被移除

`MATLAB to VR Coordinates` 将在未来版本中移除。请改用 `sim3d` 类和 Simulation 3D 模块，将 MATLAB 和 Simulink® 与 Unreal Engine® 3D 仿真环境对接。要开始使用，请参阅在 Unreal Engine 环境中创建 3D 仿真。

## 描述

（将被移除）将 MATLAB 坐标转换为 VR 坐标

MATLAB to VR Coordinates 模块将具有 MATLAB® 坐标系中坐标的点转换为 VRML 坐标系。

两个坐标系之间存在以下关系：

[*xm*,
*ym*,
*zm*] =
[*xv*,
*zv*,
-*yv*]

其中 MATLAB 坐标用下标 *m* 表示，虚拟世界坐标用下标 *v* 表示。
