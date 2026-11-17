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
chinese_source: worker-translation
---

# Thermal Resistance

## 端口
```yaml
ports:
- name: A
  summary: 层 A 热
  direction: unspecified
- name: B
  summary: 层 B 热
  direction: unspecified
```

### 守恒

### **A** — 层 A 热

与层 A 关联的热守恒端口。

### **B** — 层 B 热

与层 B 关联的热守恒端口。
## 参数
```yaml
parameters:
- name: Thermal resistance
  summary: 热阻值 1 K/W（默认）
  group: ''
```

### **Thermal resistance** — 热阻值 1 K/W（默认）

热阻值。
## 所属库

Simscape / Foundation Library / Thermal / Thermal Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

热系统中的恒定热阻

热阻是一个抽象量，它将热导率、传热系数和辐射系数联系起来。Thermal Resistance 模块允许您以广义术语对传热进行建模，而不论其是通过传导、对流、辐射还是它们的组合实现的。

Thermal Resistance 模块的传热方程为：

R⋅Q=ΔT

其中：

- *R* 是热阻。
- *Q* 是热流率。
- *ΔT* 是层之间的温差。

热阻与其他传热量之间的关系如下：

R=Dk⋅A=1h⋅A=1r⋅A(TA2+TB2)(TA+TB)

其中：

- *D* 是材料厚度，即层之间的距离。
- *A* 是垂直于热流方向的面积。
- *k* 是材料的热导率。
- *h* 是对流传热系数。
- *r* 是辐射系数。
- *T*A 和
  *T*B 分别是端口 A 和
  B 处的温度。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
