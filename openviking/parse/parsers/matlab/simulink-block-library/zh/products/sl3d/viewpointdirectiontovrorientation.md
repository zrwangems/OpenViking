---
type: simulink-block
title: 'Viewpoint Direction to VRML Orientation'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'viewpointdirectiontovrorientation'
documentation_source_path: 'viewpointdirectiontovrorientation.html'
language: zh-CN
chinese_source: worker-translation
---

# Viewpoint Direction to VRML Orientation

## 端口

### 输入

### **输入 1** — 视点方向 3 元素向量

视点方向，指定为 3 元素向量。

**数据类型：** `single` | `double`
### 输出

### **端口 1** — 轴/角旋转 4 元素向量

输出旋转，以轴/角表示法返回为 4 元素向量。前三个元素指定旋转轴，第四个元素指定角度。

## 参数

R2025b 中未记录。

## 所属库

Simulink 3D Animation / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际支持的数据类型或功能取决于模块实现。

## 版本历史

**在 R2006a 中引入**

### R2023b：将移除

`Viewpoint Direction to VR Orientation` 将在未来版本中移除。而应使用 `sim3d` 类和 Simulation 3D 模块将 MATLAB® 和 Simulink® 与 Unreal Engine® 3D 仿真环境连接起来。若要开始使用，请参阅“在 Unreal Engine 环境中创建 3D 仿真”。

## 描述

（将移除）将视点方向转换为虚拟世界朝向

Viewpoint Direction to VR Orientation 将视点方向（3 元素向量）作为输入，并输出对应的虚拟世界视点朝向（4 元素旋转向量）。

要打开“模块参数”对话框，请双击该模块。
