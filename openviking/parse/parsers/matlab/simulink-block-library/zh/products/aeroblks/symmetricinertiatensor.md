---
type: simulink-block
title: 'Symmetric Inertia Tensor'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Atmospheric Flight / Mass Properties'
documentation_page: 'symmetricinertiatensor'
documentation_source_path: 'symmetricinertiatensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Symmetric Inertia Tensor

## 端口

### 输入

### **Ixx** — 转动惯量标量

绕 *x* 轴的转动惯量，指定为标量。

**数据类型：** `double`

### **Ixy** — *xy* 平面内的惯性积标量

*xy* 平面内的惯性积，指定为标量。

**数据类型：** `double`

### **Ixz** — *xz* 平面内的惯性积标量

*xz* 平面内的惯性积，指定为标量。

**数据类型：** `double`

### **Iyy** — 绕 *y* 轴的转动惯量标量

绕 *y* 轴的转动惯量，指定为标量。

**数据类型：** `double`

### **Iyz** — *yz* 平面内的惯性积标量

*yz* 平面内的惯性积，指定为标量。

**数据类型：** `double`

### **Izz** — 绕 *z* 轴的转动惯量标量

绕 *z* 轴的转动惯量，指定为标量。

**数据类型：** `double`
### 输出

### **I** — 惯性张量 3×3 矩阵

对称惯性张量，返回为 3×3 矩阵。

**数据类型：** `double`

## 参数

R2025b 中未记录。

## 所属库

Aerospace Blockset / Mass Properties

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

根据转动惯量和惯性积创建惯性张量

每个输入对应于张量的一个元素。

惯性张量具有以下形式：

Inertia=[Ixx−Ixy−Ixz−IxyIyy−Iyz−Ixz−IyzIzz]
