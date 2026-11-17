---
type: simulink-block
title: 'Inductor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'inductor'
documentation_source_path: 'ref/inductor.html'
language: zh-CN
chinese_source: worker-translation
---

# Inductor

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与电感正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电感负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Inductance
  summary: 电感的电感值 1e-6 H（默认）| 正标量
  group: ''
- name: Series resistance
  summary: 小寄生效应 0 Ohm（默认）| 非负标量
  group: ''
- name: Parallel conductance
  summary: 小寄生效应 1e-9 1/Ohm（默认）| 非负标量
  group: ''
```

### **Inductance** — 电感的电感值 `1e-6 H`（默认）| 正标量

电感值。

### **Series resistance** — 小寄生效应 `0 Ohm`（默认）| 非负标量

表示小寄生效应。串联电阻可用于表示直流绕组电阻或趋肤效应引起的电阻。

### **Parallel conductance** — 小寄生效应 `1e-9 1/Ohm`（默认）| 非负标量

表示小寄生效应。某些电路的仿真可能需要存在一个小的并联电导。
## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

电气系统中的线性电感

Inductor 模块对线性电感进行建模，用以下方程描述：

V=LdIdt

其中：

- *V* 是电压。
- *L* 是电感。
- *I* 是电流。
- *t* 是时间。

**Series resistance** 和 **Parallel conductance** 参数表示小寄生效应。串联电阻可用于表示直流绕组电阻或趋肤效应引起的电阻。某些电路的仿真可能需要存在一个小的并联电导。有关更多信息，请参阅 Modeling Best Practices。

连接 + 和 – 是对应于电感正极和负极端子的守恒电气端口。如果电流从正极流向负极，则电流为正，电感两端的电压等于正极端子电压与负极端子电压之差，*V*(+) – *V*(–)。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 Modify Nominal Values for a Block Variable。
