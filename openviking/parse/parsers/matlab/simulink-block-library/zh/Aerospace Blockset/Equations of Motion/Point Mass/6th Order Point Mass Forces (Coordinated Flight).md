---
type: simulink-block
title: '6th Order Point Mass Forces (Coordinated Flight)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / Point Mass'
documentation_page: '6thorderpointmassforcescoordinatedflight'
documentation_source_path: '6thorderpointmassforcescoordinatedflight.html'
language: zh-CN
chinese_source: worker-translation
---

# 6th Order Point Mass Forces (Coordinated Flight)

## 端口

### 输入

### **Lift** — Lift 标量 | 数组

Lift，指定为标量或数组，以力为单位。

**数据类型：** `double`

### **Drag** — Drag 标量 | 数组

Drag，指定为标量或数组，以力为单位。

**数据类型：** `double`

### **Weight** — Weight 标量 | 数组

Weight，指定为标量或数组，以力为单位。

**数据类型：** `double`

### **Thrust** — Thrust 标量 | 数组

Thrust，指定为标量或数组，以力为单位。

**数据类型：** `double`

### **ɣ** — 飞行航迹角标量 | 数组

飞行航迹角，指定为标量或数组，以 radians 为单位。

**数据类型：** `double`

### **μ** — 倾侧角标量 | 数组

倾侧角，指定为标量或数组，以 radians 为单位。

**数据类型：** `double`

### **ɑ** — 迎角标量 | 数组

迎角，指定为标量或数组，以 radians 为单位。

**数据类型：** `double`
### 输出

### **Fx** — *x* 轴中的力 标量 | 数组

*x* 轴中的力，指定为标量或数组，以力为单位。

**数据类型：** `double`

### **Fy** — *y* 轴中的力 标量 | 数组

*y* 轴中的力，指定为标量或数组，以力为单位。

**数据类型：** `double`

### **Fz** — *z* 轴中的力 标量 | 数组

*z* 轴中的力，指定为标量或数组，以力为单位。

**数据类型：** `double`

## 参数

R2025b 中未记录。

## 所属库

Aerospace Blockset / Equations of Motion / Point Mass

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算协调飞行中六阶点质量所使用的力

6th Order Point Mass Forces (Coordinated Flight) 模块计算单个点质量或多个点质量的作用力。有关施加力的系统的更多信息，请参阅算法。
