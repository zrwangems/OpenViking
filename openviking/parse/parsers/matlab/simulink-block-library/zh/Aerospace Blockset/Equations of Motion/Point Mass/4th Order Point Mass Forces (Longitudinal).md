---
type: simulink-block
title: '4th Order Point Mass Forces (Longitudinal)'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / Point Mass'
documentation_page: '4thorderpointmassforceslongitudinal'
documentation_source_path: '4thorderpointmassforceslongitudinal.html'
language: zh-CN
chinese_source: worker-translation
---

# 4th Order Point Mass Forces (Longitudinal)

## 端口

### 输入

### **Lift** — Lift 标量 | 数组

Lift，指定为标量或数组，以力的单位表示。

**数据类型：** `double`

### **Drag** — Drag 标量 | 数组

Drag，指定为标量或数组，以力的单位表示。

**数据类型：** `double`

### **Weight** — Weight 标量 | 数组

Weight，指定为标量或数组，以力的单位表示。

**数据类型：** `double`

### **Thrust** — Thrust 标量 | 数组

Thrust，指定为标量或数组，以力的单位表示。

**数据类型：** `double`

### **ɣ** — 飞行路径角 标量 | 数组

飞行路径角，指定为标量或数组，以 radians 为单位。

**数据类型：** `double`

### **μ** — 滚转角 标量 | 数组

滚转角，指定为标量或数组，以 radians 为单位。

**数据类型：** `double`

### **ɑ** — 迎角 标量 | 数组

迎角，指定为标量或数组，以 radians 为单位。

**数据类型：** `double`
### 输出

### **Fx** — 沿 *x* 轴的力 标量 | 数组

沿 *x* 轴的力，以标量或数组形式返回，以力的单位表示。

**数据类型：** `double`

### **Fz** — 沿 *z* 轴的力 标量 | 数组

沿 *z* 轴的力，以标量或数组形式返回，以力的单位表示。

**数据类型：** `double`

## 参数

在 R2025b 中未记录。

## 所属库

Aerospace Blockset / Equations of Motion / Point Mass

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

计算四阶点质量所使用的力

4th Order Point Mass Forces (Longitudinal) 模块计算单个点质量或多个点质量的施加力。有关施加力所用系统的详细信息，请参见 Algorithms。
