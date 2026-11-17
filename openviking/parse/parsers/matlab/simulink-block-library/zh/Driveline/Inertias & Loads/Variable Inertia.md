---
type: simulink-block
title: 'Variable Inertia'
family: 'inertias-loads'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Inertias & Loads'
documentation_page: 'variableinertia'
documentation_source_path: 'ref/variableinertia.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Inertia

## 端口

### 输入

### **LConn 1** — Inertia, kg/m2 physical signal

与惯性关联的物理输入信号，单位为
kg/m2。
### 守恒

### **LConn 2** — 旋转连接 mechanical rotational

mechanical rotational 守恒端口。

## 参数

### **Minimum inertia** — 最小惯性 `0.1` `kg*m^2` (默认) | 正标量

可变惯性在仿真期间可以取的最小值。physical signal 输入在该值处饱和。如果输入低于最小惯性，则将其设置为等于最小惯性值。

## 所属库

Simscape / Driveline / Inertias & Loads

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

作为 physical signal 输入的时变惯性

Variable Inertia 模块表示时变惯性的影响。具有可变惯性的组件包括展开太阳能电池板阵列的卫星。一个 physical signal 输入端口在仿真过程中的每个时间步提供瞬时惯性。为尽量减小求解器误差，请避免输入信号中的不连续和突变。

随着组件惯性变化，作用在该组件上的惯性力矩也会变化：

TI=Iω˙,

其中：

- *TI* 是惯性
  力矩。
- *I* 是可变惯性。
- *ω* 是惯性的角速度。

physical signal 输入在模块属性检查器中指定的最小惯性处饱和。每当输入低于最小惯性时，模块改为基于最小惯性执行计算。惯性力矩变为：

TI=IMinω˙,

其中 *IMin* 是允许的最小惯性。

可变惯性的角动量守恒。在没有外部力矩的情况下，惯性矩的减小会导致角速度成比例增加。角动量保持恒定，直到净外部力矩使其改变。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
