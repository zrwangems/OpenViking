---
type: simulink-block
title: 'Thermal Resistance'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Elements'
documentation_page: 'thermalresistance'
documentation_source_path: 'ref/thermalresistance.html'
language: zh-CN
chinese_source: official
---

# Thermal Resistance

## 端口

### 守恒

### **A** — A 层 热

与 A 层关联的热守恒端口。

### **B** — B 层 热

与 B 层关联的热守恒端口。

## 参数

### **热阻** — 热阻值 1 K/W (默认)

热阻值。

## 所属库

Simscape / Foundation Library / Thermal / Thermal Elements

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2017b 中推出**

## 描述

热系统中的恒定电阻

热阻是一个抽象量，它与热导率、传热系数和辐射系数有关。Thermal Resistance 模块可让您以广义项对热传递进行建模，无论是通过传导、对流、辐射还是它们的组合进行热传递。

Thermal Resistance 模块的传热方程为：

R⋅Q=ΔT

其中：

- *R* 是热阻。
- *Q* 是热流量。
- *ΔT* 是层与层之间的温差。

热阻与其他传热量的关系如下：

R=Dk⋅A=1h⋅A=1r⋅A(TA2+TB2)(TA+TB)

其中：

- *D* 是材料厚度，即层与层之间的距离。
- *A* 是垂直于热流方向的面积。
- *k* 是材料的热导率。
- *h* 为对流传热系数。
- *r* 是辐射系数。
- *T*A 和 *T*B 分别是端口 A 和 B 处的温度。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
