---
type: simulink-block
title: 'Gear Box'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Mechanisms'
documentation_page: 'gearbox'
documentation_source_path: 'ref/gearbox.html'
language: zh-CN
chinese_source: official
---

# Gear Box

## 端口

### 守恒

### **S** — 输入轴 机械旋转

与输入轴相关联的机械旋转守恒端口。

### **O** — 输出轴 机械旋转

与输出轴相关联的机械旋转守恒端口。

## 参数

### **齿轮比** — 齿轮速度比 `5` (默认)

输入轴角速度与输出轴角速度的比值。您可以指定正值和负值。

## 所属库

Simscape / Foundation Library / Mechanical / Mechanisms

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

机械系统中的齿轮箱

Gear Box 模块表示理想的非行星固定齿轮比齿轮箱。齿轮比被确定为输入轴角速度与输出轴角速度的比值。

齿轮箱用以下方程描述：

ωS=N·ωO

TO=N⋅TS

PS=ωS⋅TS

PO=−ωO⋅TO

其中

- *ω*S 是输入轴角速度。
- *ω*O 是输出轴角速度。
- *N* 是齿轮比。
- *T*S 是输入轴上的扭矩。
- *T*O 是输出轴上的扭矩。
- *P*S 是输入轴上的功率。
- *P*O 是输出轴上的功率。在计算 *P*O 时，请注意减号。有一条网络规则是，如果流经守恒端口的功率从电路中被删除（耗散），则该功率为正；如果该组件为系统供电，则该功率为负。

连接端 S 和 O 分别是与齿轮箱输入轴和输出轴相关联的机械旋转守恒端口。此模块的正方向是从 S 到参考点以及从参考点到 O。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
