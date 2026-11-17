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
```yaml
ports:
- name: AH
  summary: 电芯容量，A\*Hr 标量 | 向量
  direction: input
- name: SOH
  summary: 电池健康状态 标量 | 向量
  direction: output
```

### 输入

### **AH** — 电芯容量，A\*Hr 标量 | 向量

电芯容量，以安时为单位，指定为单个电芯的标量或多个电芯的向量。
### 输出

### **SOH** — 电池健康状态 标量 | 向量

电池的健康状态，以标量或向量形式返回，其元素范围为 [0, 1]。此输出端口的大小等于 **AH** 输入端口的大小。
## 参数
```yaml
parameters:
- name: Cell capacity when battery is new, AH_new, (A\*Hr)
  summary: 电池全新时的电芯容量 27（默认）| 非负标量
  group: ''
- name: Cell capacity at end of life, AH_eol, (A\*Hr)
  summary: 寿命终止时的电芯容量 21.6（默认）| 非负标量
  group: ''
- name: Algorithm data type
  summary: '选择模块算法数据类型的选项 Inherit: auto（默认）| double | single | <data type expression>'
  group: ''
```

### **Cell capacity when battery is new, AH\_new, (A\*Hr)** — 电池全新时的电芯容量 `27`（默认）| 非负标量

电池全新时的电芯容量，以安时为单位。

### **Cell capacity at end of life, AH\_eol, (A\*Hr)** — 寿命终止时的电芯容量 `21.6`（默认）| 非负标量

电池寿命终止时的电芯容量，以安时为单位。

### **Algorithm data type** — 选择模块算法数据类型的选项 `Inherit: auto`（默认）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以以 `single` 和 `double` 精度对模块进行仿真。您必须将输入和参数显式指定为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant 和 Control Data Types of Signals。
## 所属库

Simscape / Battery / BMS / Estimators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

### R2025a: 使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

您现在可以使用 **Algorithm data type** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

## 描述

基于容量衰减的健康状态估计器

SOH Estimator (Capacity-Based) 模块实现了一个估计器，它基于容量衰减计算电池的健康状态 (SOH)。SOH 反映电池相对于其理想状况的状况。健康变化意味着电池的容量和功率随时间衰减。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用单精度浮点仿真，所有输入和参数的数据类型必须为 `single`。

此图显示了模块的结构：

### 方程

电芯容量是电池老化的重要指标。在电池的生命周期中，电芯容量随时间减少。通常，当电芯容量减少到其标称值的约 80% 时，电芯 SOH 为 0。

SOH Estimator (Capacity Based) 模块根据电芯容量 *Q* 计算 SOH：

SOHQ=Q−QeolQnew−Qeol，

其中 *Q*eol 是寿命终止容量，*Q*new 是电池全新时的容量。
