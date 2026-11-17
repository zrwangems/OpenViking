---
type: simulink-block
title: 'Variable Mass'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Inertias & Loads'
documentation_page: 'variablemass'
documentation_source_path: 'ref/variablemass.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Mass

## 端口
```yaml
ports: []
```

该模块具有一个守恒平动端口和一个物理信号输入端口。
守恒平动端口标识质量随时间变化的传动系统组件。物理信号输入端口提供将质量指定为时间函数的方式。
## 参数
```yaml
parameters: []
```

**Minimum mass**
:   可变质量在仿真期间可以取的最小值。物理信号输入在该值处饱和。如果输入低于最小质量，则将其设置为等于最小质量值。默认值为 `0.1` `kg`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

指定为物理信号输入的时变质量

该模块对时变质量的影响进行建模。具有可变质量的组件包括燃料含量逐渐降低的燃料箱。物理信号输入端口在仿真过程中的每个时间步提供瞬时质量。为最小化求解器误差，请避免输入信号中的不连续性和突变。

随着组件质量的变化，作用在该组件上的惯性力也会变化：

FI=mv˙,

其中：

- *F*I 是惯性力。
- *m* 是可变质量。
- *v* 是质量的速度。

物理信号输入在模块属性检查器中指定的最小质量处饱和。每当输入低于最小质量时，模块改为对最小质量执行计算。惯性力变为：

FI=mMinv˙,

其中：

- *m*Min 是允许的最小质量。

可变质量的线动量是守恒的。在没有外力的情况下，质量的减少会导致线速度成比例增加。线动量保持恒定，直到净外力使其发生变化。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
