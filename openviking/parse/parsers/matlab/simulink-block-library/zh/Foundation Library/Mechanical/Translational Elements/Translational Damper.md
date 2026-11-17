---
type: simulink-block
title: 'Translational Damper'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Translational Elements'
documentation_page: 'translationaldamper'
documentation_source_path: 'ref/translationaldamper.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Damper

## 端口
```yaml
ports:
- name: R
  summary: 杆机械平移
  direction: conserving
- name: C
  summary: 壳体机械平移
  direction: conserving
```

### 守恒端口

### **R** — 杆机械平移

与杆（即运动体）关联的机械平移守恒端口。

### **C** — 壳体机械平移

与壳体（即静止体）关联的机械平移守恒端口。
## 参数
```yaml
parameters:
- name: Damping coefficient
  summary: 阻尼系数，由粘性摩擦定义 100 N/(m/s)（默认）| 标量
  group: ''
```

### **Damping coefficient** — 阻尼系数，由粘性摩擦定义 `100 N/(m/s)`（默认）| 标量

阻尼系数，由粘性摩擦定义。
## 所属库

Simscape / Foundation Library / Mechanical / Translational Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

机械平移系统中的粘性阻尼器

Translational Damper 模块表示一个理想的机械平移粘性阻尼器，用以下方程描述：

F=Dv

v=vR−vC

其中

- *F* 是通过阻尼器传递的力。
- *D* 是阻尼系数，由粘性摩擦定义。
- *v* 是相对速度。
- *v*R 和 *v*C 分别是端口 **R** 和 **C** 的绝对速度。

模块正方向是从端口 **R** 到端口 **C**。这意味着如果力沿从 **R** 到 **C** 的方向作用，则该力为正。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
