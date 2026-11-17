---
type: simulink-block
title: 'Variable Translational Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'variabletranslationaldamper'
documentation_source_path: 'ref/variabletranslationaldamper.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Translational Damper

## 端口

`B`
:   表示可变平动阻尼系数的物理信号输入端口。

`C`
:   平动守恒端口。

`R`
:   平动守恒端口。

## 参数

**Minimum damping coefficient**
:   可变阻尼系数允许的最小值。物理信号输入在低于指定值时饱和。该参数必须大于或等于零。默认值为 `0`
    `N/(m/s)`。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

具有可变阻尼系数的平动粘性阻尼器

该模块表示具有可变阻尼系数的平动粘性阻尼器。物理信号输入端口提供平动阻尼系数的大小。阻尼力的大小等于物理信号输入与两个平动守恒端口之间相对线速度的乘积。最小阻尼系数可防止出现非物理的负阻尼值。

平动阻尼力满足以下表达式：

F={B.v,B≥BminBmin⋅v,B<Bmin,

参数为：

- *F* — 通过两个平动守恒端口之间的平动阻尼器传递的力
- *B* — 粘性阻尼系数
- *Bmin* — 允许的最小阻尼系数
- *v* — 在两个平动守恒端口之间测得的相对线速度
- *vR* — 端口 R 的线速度
- *vC* — 端口 C 的线速度

该模块在两个平动守恒端口上施加大小相等、方向相反的阻尼力。作用在端口 R 上的阻尼力符号等于相对线速度的符号。正线速度对应于作用在端口 R 上的正阻尼力，以及作用在端口 C 上的大小相等的负阻尼力。

### 假设和限制

- 该模块表示严格的粘性阻尼。
- 阻尼系数的值必须大于或等于零。
