---
type: simulink-block
title: 'Variable Rotational Spring'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'variablerotationalspring'
documentation_source_path: 'ref/variablerotationalspring.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Rotational Spring

## 端口

`K`
:   表示可变弹簧刚度的物理信号输入端口。

`C`
:   旋转守恒端口。

`R`
:   旋转守恒端口。

## 参数

**最小弹簧刚度**
:   弹簧刚度允许的最小值。当物理信号输入低于指定值时，该输入将饱和。该参数必须大于零。默认值为 `0.01`。默认单位为
    `(N*m/rad)`。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

具有可变弹簧刚度的旋转弹簧

该模块表示一个具有可变弹簧刚度的扭转弹簧。物理信号输入端口提供可变弹簧刚度的值。弹簧扭矩的大小等于物理信号输入与两个旋转守恒端口之间相对角位移的乘积。最小弹簧刚度值用于防止出现非物理值。

旋转弹簧扭矩满足以下表达式：

T={K⋅θK≥KminKmin⋅θK<Kmin,

参数为：

- *T* — 通过弹簧传递的扭矩
- *K* — 弹簧刚度
- *Kmin* — 允许的最小弹簧刚度
- *θ* — 根据 θ=θinit+θR−θC 在两个旋转守恒端口之间测得的相对角位移
- *θinit* — 两个旋转守恒端口之间的初始角变形
- *θR* — 旋转守恒端口 R 的绝对角位移
- *θC* — 旋转守恒端口 C 的绝对角位移

该模块对两个旋转守恒端口施加大小相等、方向相反的弹簧扭矩。作用于端口 R 的弹簧扭矩的符号与相对角速度的符号相同。正的相对角速度对应于作用于端口 R 的正阻尼扭矩，以及作用于端口 C 的大小相等的负阻尼扭矩。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅“设置模块变量的优先级和初始目标”。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的**标称值**部分。有关详细信息，请参阅“修改模块变量的标称值”。

### 假设和限制

弹簧刚度的值必须大于零。
