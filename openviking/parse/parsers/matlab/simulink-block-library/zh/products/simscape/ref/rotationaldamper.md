---
type: simulink-block
title: 'Rotational Damper'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Rotational Elements'
documentation_page: 'rotationaldamper'
documentation_source_path: 'ref/rotationaldamper.html'
language: zh-CN
chinese_source: official
---

# Rotational Damper

## 端口

### 守恒

### **R** — 杆 机械旋转

与杆（即运动实体）相关联的机械旋转守恒端口。

### **C** — 外壳 机械旋转

与外壳（即静止实体）相关联的机械旋转守恒端口。

## 参数

### **阻尼系数** — 阻尼系数 `0.001 N*m/(rad/s)` (默认) | 标量

阻尼系数，由粘性摩擦定义。

## 所属库

Simscape / Foundation Library / Mechanical / Rotational Elements

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

机械旋转系统中的粘性阻尼器

Rotational Damper 模块表示理想的机械旋转粘性阻尼器，用以下方程描述：

T=D·ω

ω=ωR−ωC

其中

- *T* 是通过阻尼器传输的扭矩。
- *D* 是阻尼系数，由粘性摩擦定义。
- *ω* 是相对角速度。
- *ω*R 和 *ω*C 分别是端口 **R** 和 **C** 的绝对角速度。

此模块的正方向是从端口 **R** 到端口 **C**。这意味着，如果端口 **R** 的速度大于端口 **C** 的速度，则此模块将扭矩从端口 **R** 传递到端口 **C**。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
