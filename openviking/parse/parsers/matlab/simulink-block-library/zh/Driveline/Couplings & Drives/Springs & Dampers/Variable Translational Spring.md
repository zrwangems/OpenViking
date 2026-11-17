---
type: simulink-block
title: 'Variable Translational Spring'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'variabletranslationalspring'
documentation_source_path: 'ref/variabletranslationalspring.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Translational Spring

## 端口
```yaml
ports:
- name: K
  summary: 可变弹簧系数，N/m 物理信号
  direction: input
- name: C
  summary: 基座端口 机械平移
  direction: input
- name: R
  summary: 从动端口 机械平移
  direction: input
```

### 输入

### **K** — 可变弹簧系数，N/m 物理信号

与可变弹簧刚度关联的物理信号输入端口。
### 守恒

### **C** — 基座端口 机械平移

与弹簧负端关联的机械平移守恒端口。正方向从端口 **R** 指向端口
**C**。

### **R** — 从动端口 机械平移

与弹簧正端关联的机械平移守恒端口。正方向从端口 **R** 指向端口
**C**。
## 参数
```yaml
parameters:
- name: Minimum spring rate
  summary: 弹簧刚度限值 1 N/m（默认）| 正标量
  group: ''
```

### **Minimum spring rate** — 弹簧刚度限值 `1` `N/m`（默认）| 正标量

弹簧刚度允许的最小值。物理信号输入在低于指定值时饱和。
## 所属库

Simscape / Driveline / Couplings & Drives / Springs & Dampers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

具有可变弹簧刚度的平移弹簧

Variable Translational Spring 模块表示具有可变刚度的平移弹簧。物理信号输入端口提供可变弹簧刚度。弹簧力的大小等于物理信号输入与两个平移守恒端口之间相对线性位移的乘积。最小弹簧刚度可防止出现非物理值。

平移弹簧力满足以下表达式：

F={K⋅x,K≥KminKmin⋅x,K<Kmin

其中：

- *F* 是通过弹簧在两个平移守恒端口之间传递的力。
- *K* 是弹簧刚度系数。
- *Kmin* 是允许的最小弹簧刚度。
- *x* 是两个平移守恒端口之间的相对位移，根据 x=xinit+xR−xC。
- *xinit* 是初始弹簧变形。
- *xR* 是平移守恒端口 **R** 的绝对位移。
- *xC* 是平移守恒端口 **C** 的绝对位移。

该模块在两个平移守恒端口上施加大小相等、方向相反的弹簧力。作用在端口 **R** 上的弹簧力符号等于两个端口之间相对线性位移的符号。正线性速度对应于作用在端口 **R** 上的正弹簧力，以及作用在端口 **C** 上的大小相等的负弹簧力。

### 假设和限制

该模块将可变弹簧刚度的值限制为保持大于零。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期量级的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
