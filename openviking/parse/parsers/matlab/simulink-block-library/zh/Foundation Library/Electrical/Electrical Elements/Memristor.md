---
type: simulink-block
title: 'Memristor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'memristor'
documentation_source_path: 'ref/memristor.html'
language: zh-CN
chinese_source: worker-translation
---

# Memristor

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: unspecified
- name: '-'
  summary: 负极端子电气
  direction: unspecified
```

### 守恒

### **+** — 正极端子电气

与忆阻器正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与忆阻器负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Resistance of state A
  summary: 整个忆阻器处于状态 A 时的电阻 1 Ohm（默认）| 正标量
  group: ''
- name: Resistance of state B
  summary: 整个忆阻器处于状态 B 时的电阻 100 Ohm（默认）| 正标量
  group: ''
- name: Total charge required for full state transition
  summary: 状态之间完全转换所需的电荷 10 mC（默认）| 正标量
  group: ''
- name: State A fraction at t=0
  summary: 仿真开始时忆阻器处于状态 A 的比例 0（默认）| 最小值/最大值：(0,1)
  group: ''
- name: Exponent of the window function
  summary: 边界处的漂移控制 2（默认）| 正整标量
  group: ''
```

### **Resistance of state A** — 整个忆阻器处于状态 A 时的电阻 `1 Ohm`（默认）| 正标量

当整个忆阻器处于状态 A 时的电阻，即当 *ξ* = 1 时。该值应大于 0。

### **Resistance of state B** — 整个忆阻器处于状态 B 时的电阻 `100 Ohm`（默认）| 正标量

当整个忆阻器处于状态 B 时的电阻，即当 *ξ* = 0 时。该值应大于 0。

### **Total charge required for full state transition** — 状态之间完全转换所需的电荷 `10 mC`（默认）| 正标量

使忆阻器从完全处于一种状态转换到完全处于另一种状态所需的总电荷流量。

### **State A fraction at t=0** — 仿真开始时忆阻器处于状态 A 的比例 `0`（默认）| 最小值/最大值：(0,1)

仿真开始时 *ξ* 的初始条件。该参数在模块内设置一个高优先级变量目标。该值应大于或等于 0 且小于或等于 1。

### **Exponent of the window function** — 边界处的漂移控制 `2`（默认）| 正整标量

窗函数的指数 *p*，用于将 *ξ* 的值保持在 0 和 1 之间。
## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

采用非线性掺杂漂移方法的理想忆阻器

该模块允许您对采用非线性掺杂漂移方法的理想忆阻器进行建模。忆阻器的行为类似于电阻器，不同之处在于其电阻（也称为忆阻）是流过该器件的电流的函数。忆阻由两种状态 A 和 B 定义，在给定时刻，器件的一部分处于其中一种状态。

非线性掺杂漂移模型 [1] 由以下方程描述：

*V* =
*M*·*I*

*M* =
*ξ**·R*A+(1 –
*ξ*)*·R*B

dξdt=IQ0Fp(ξ)

其中

- *V* 是忆阻器两端的电压。
- *M* 是忆阻。
- *I* 是进入 + 端子的电流。
- *R*A 和
  *R*B 分别是状态 A 和状态 B 的电阻。
- *ξ* 是忆阻器中处于状态 A 的比例。从 + 端子到 - 端子的正电流会增加 *ξ*。
  类似地，从 - 端子到 + 端子的正电流会减小
  *ξ*。*ξ* 的值受 0 和 1 约束。
- *t* 是时间。
- *Q*0 是使忆阻器从完全处于一种状态转换到完全处于另一种状态所需的总电荷。
- *Fp(ξ)* 是一个“窗”函数，它将 *ξ* 保持在 1 和 0 之间的窗口内，因此使器件边界处的漂移为零。

窗函数为

*F*p(*ξ*) = 1 –
(2*ξ* –
1)2*p*

其中 *p* 是正整数。当 *ξ* 接近 0 或 1 时，该函数会被修改，以提高数值稳定性。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
