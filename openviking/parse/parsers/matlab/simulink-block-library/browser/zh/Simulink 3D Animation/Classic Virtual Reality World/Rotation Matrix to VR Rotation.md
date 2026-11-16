---
type: simulink-block
title: 'Rotation Matrix to VR Rotation'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'rotationmatrixtovrrotation'
documentation_source_path: 'rotationmatrixtovrrotation.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotation Matrix to VR Rotation

## 端口

### 输入

### **输入 1** — 旋转矩阵 3×3 矩阵

3D 旋转，指定为按列定义的 3×3 矩阵，也称为方向余弦矩阵。

三维球面旋转的一种表示形式为 3×3 实正交矩阵 *R*：
*R*T*R* = *RR*T = *I*，其中 I 是 3×3 单位矩阵，*R*T 是 *R* 的转置。该矩阵也称为方向余弦矩阵 (DCM)。DCM 是对象在空间中相对于其父节点的朝向。

R=(R11R12R13R21R22R23R31R32R33)=(RxxRxyRxzRyxRyyRyzRzxRzyRzz)

**数据类型：** `single` | `double`

### 输出

### **端口 1** — 轴/角旋转 4 元素向量

输出旋转，以轴/角表示法返回为 4 元素向量。前三个元素指定旋转轴，第四个元素指定角度。

## 参数

### **将输入值视为零的最大值** — 有效零值 `1e-12`（默认）| 标量

如果输入信号值等于或低于此参数中设置的值，则将其视为零。默认情况下，该参数设置为 ε = 1e-12。

## 所属库

Simulink 3D Animation / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2019a 中引入**

### R2023b：将被删除

`Rotation Matrix to VR Rotation` 将在未来版本中删除。请改用 `sim3d` 类和 Simulation 3D 模块，以将 MATLAB® 和 Simulink® 与 Unreal Engine® 3D 仿真环境连接。有关入门信息，请参阅在 Unreal Engine 环境中创建 3D 仿真。

## 描述

（将删除）将旋转矩阵转换为轴/角旋转

Rotation Matrix to VR Rotation 将旋转矩阵（按列定义为 3×3 矩阵或 9 元素列向量）转换为用于在 VR 中定义旋转的轴/角旋转表示。
