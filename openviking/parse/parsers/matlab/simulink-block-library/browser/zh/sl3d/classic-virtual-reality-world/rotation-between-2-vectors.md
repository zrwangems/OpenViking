---
type: simulink-block
title: 'Rotation Between 2 Vectors'
family: 'sl3d'
product_id: 'sl3d'
product_name: 'Simulink 3D Animation'
documentation_release: R2025b
official_category: 'Classic Virtual Reality World'
documentation_page: 'rotationbetween2vectors'
documentation_source_path: 'rotationbetween2vectors.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotation Between 2 Vectors

## 端口

### 输入

### **端口 1** — 输入信号 3 元素向量

输入信号是一个 3 元素向量，其元素分别对应于沿 i^,j^,k^ 单位向量的幅值。

**数据类型：** `double`

### **端口 2** — 输入信号 3 元素向量

输入信号是一个 3 元素向量，其元素分别对应于沿 i^,j^,k^ 单位向量的幅值。

**数据类型：** `double`

### 输出

### **输出 1** — 轴角旋转 4 元素向量

模块的输出是将第一个输入向量变换为第二个输入向量所需旋转的轴角表示。

**数据类型：** `double`

## 参数

R2025b 中未记录。

## 所属库

Simulink 3D Animation / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

实际的数据类型或功能支持取决于模块实现。

## 版本历史

**在 R2006a 中引入**

### R2023b：将被移除

`Rotation Between 2 Vectors` 将在未来版本中移除。取而代之，请使用 `sim3d` 类和 Simulation 3D 模块将 MATLAB® 和 Simulink® 与 Unreal Engine® 3D 仿真环境对接。要开始使用，请参阅在 Unreal Engine 环境中创建 3D 仿真。

## 描述

（将移除）两个 3-D 向量之间的虚拟世界旋转

Rotation Between 2 Vectors 接受两个 3×1 向量作为输入，并返回将第一个输入向量变换为第二个输入向量所需的虚拟世界旋转（指定为定义轴和角的 4 元素向量）。
