---
type: simulink-block
title: 'VR Rotation to Rotation Matrix'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'vrrotationtorotationmatrix'
documentation_source_path: 'vrrotationtorotationmatrix.html'
language: zh-CN
chinese_source: worker-translation
---

# VR Rotation to Rotation Matrix

## 端口

### 输入

### **Input 1** — 数组/角度旋转 4 元素向量

输入旋转，指定为数组/角度表示法中的 4 元素向量。前三个元素指定旋转的数组，第四个元素指定角度。

**数据类型：** `single` | `double`
### 输出

### **Output 1** — 旋转矩阵 3×3 矩阵

三维旋转，返回为按列定义的 3×3 矩阵，也称为方向余弦矩阵。

三维球面旋转表示为 3×3 实正交矩阵 *R*：
*R*T*R*
= *RR*T =
*I*，其中 *I* 是
3×3 单位矩阵，
*R*T 是 *R* 的转置。该矩阵
也称为方向余弦矩阵（DCM）。DCM 是
对象在空间中相对于其父节点的方位。

R=(R11R12R13R21R22R23R31R32R33)=(RxxRxyRxzRyxRyyRyzRzxRzyRzz)

**数据类型：** `single` | `double`

## 参数

### **将输入值视为零的最大值** — 有效零值 `1e-12`（默认） | scalar

如果输入信号值等于或低于此参数中设置的值，则将其视为零。默认情况下，该参数设置为 ε = 1e-12。

## 所属库

Simulink 3D Animation / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

### R2023b：将移除

`VR Rotation to Rotation Matrix` 将在未来版本中移除。请改用 `sim3d` 类和 Simulation 3D 模块，将 MATLAB® 和 Simulink® 与 Unreal Engine® 3D 仿真环境连接。要开始使用，请参阅在 Unreal Engine 环境中创建 3D 仿真。

## 描述

（将移除）将数组/角度旋转转换为旋转矩阵

VR Rotation to Rotation Matrix 模块将用于在虚拟现实中定义旋转的数组/角度旋转表示转换为 3×3 旋转矩阵
