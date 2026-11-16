---
type: simulink-block
title: 'SOH Estimator (Capacity-Based)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'sohestimatorcapacitybased'
documentation_source_path: 'ref/sohestimatorcapacitybased.html'
language: zh-CN
chinese_source: worker-translation
---

# SOH Estimator (Capacity-Based)

## 端口

### 输入

### **AH** — 电芯容量，A\*Hr 标量 | 向量

电芯容量，以安时为单位，对于单个电芯指定为标量，对于多个电芯指定为向量。
### 输出

### **SOH** — 电池健康状态 标量 | 向量

电池健康状态，返回为标量或向量，其元素在 [0, 1] 范围内。此输出端口的大小等于 **AH** 输入端口的大小。

## 参数

### **电池新时的电芯容量，AH\_new，(A\*Hr)** — 电池新时的电芯容量 `27`（默认值）| 非负标量

电池新时的电芯容量，以安时为单位。

### **电池寿命终止时的电芯容量，AH\_eol，(A\*Hr)** — 电池寿命终止时的电芯容量 `21.6`（默认值）| 非负标量

电池寿命终止时的电芯容量，以安时为单位。

### **算法数据类型** — 用于选择模块算法数据类型的选项 `Inherit: auto`（默认值）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

用于选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 可以在 `single` 和 `double` 精度下仿真该模块。必须显式将输入和参数提供为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为指定的数据类型对象。

单击 **显示数据类型助手** 按钮以显示 **数据类型助手**，它可帮助您设置数据类型属性。有关详细信息，请参阅使用数据类型助手指定数据类型和控制信号的数据类型。

## 所属库

Simscape / Battery / BMS / Estimators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2025a：使用 **算法数据类型** 参数在单精度和双精度浮点仿真之间切换

现在，您可以使用 **算法数据类型** 参数，轻松在模块算法的单精度和双精度浮点仿真之间切换。

## 描述

基于容量衰减的健康状态估计器

SOH Estimator (Capacity-Based) 模块实现了一个估计器，该估计器基于容量衰减计算电池的健康状态 (SOH)。SOH 反映电池相对于其理想状况的条件。健康变化意味着电池的容量和功率会随时间衰减。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用单精度浮点仿真，所有输入和参数的数据类型必须为 `single`。

此图显示了该模块的结构：

### 方程

电芯容量是电池老化的重要指标。在电池的生命周期内，电芯容量会随时间降低。通常，当电芯容量降低至其标称值的约 80% 时，电芯 SOH 为 0。

SOH Estimator (Capacity Based) 模块将 SOH 计算为电芯容量 *Q* 的函数：

SOHQ=Q−QeolQnew−Qeol,

其中 *Q*eol 是寿命终止时的容量，*Q*new 是电池新时的容量。
