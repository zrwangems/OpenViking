---
type: simulink-block
title: 'SOH Estimator'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'sohestimator'
documentation_source_path: 'ref/sohestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# SOH Estimator

## 端口
```yaml
ports:
- name: SOC
  summary: 电池荷电状态，无量纲标量 | 向量
  direction: input
- name: Temperature
  summary: 电芯温度 标量 | 向量
  direction: input
- name: R0
  summary: 端子电阻，欧姆 标量 | 向量
  direction: input
- name: SOH
  summary: 电池健康状态 标量 | 向量
  direction: output
```

### 输入

### **SOC** — 电池荷电状态，无量纲标量 | 向量

电池的荷电状态，指定为范围 [0, 1] 内的标量或向量。此输入端口的尺寸必须与 **Temperature** 和 **R0** 输入端口的尺寸相等。

### **Temperature** — 电芯温度 标量 | 向量

电池电芯的温度，单个电芯时指定为标量，多个电芯时指定为向量。此输入端口的尺寸必须与 **SOC** 和 **R0** 输入端口的尺寸相等。

### **R0** — 端子电阻，欧姆 标量 | 向量

端子电阻，单个电芯时指定为标量，多个电芯时指定为向量。此输入端口的尺寸必须与 **SOC** 和 **Temperature** 输入端口的尺寸相等。
### 输出

### **SOH** — 电池健康状态 标量 | 向量

电池的健康状态，返回为范围 [0, 1] 内的标量或向量。此输出端口的尺寸等于输入端口处向量的尺寸。
## 参数
```yaml
parameters:
- name: Vector of state-of-charge values, SOC (-)
  summary: SOC 断点 [0, .1, .25, .5, .75, .9, 1]（默认）| 0 到 1 之间的非负标量向量
  group: ''
- name: Vector of temperatures, T
  summary: 温度断点 [278, 293, 313]（默认）| 正标量向量
  group: ''
- name: Terminal resistance when battery cell is new, R0new(SOC,T), (ohm)
  summary: 电池电芯全新时的端子电阻 [.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091;
    .0113, .0085, .0089; .0116, .0085, .0089]（默认）| 非负标量矩阵
  group: ''
- name: Terminal resistance at end of life, R0eol(SOC,T), (ohm)
  summary: 寿命终止时的端子电阻 [.0234,.017,.018;.022,.017,.018;.0228,.0174,.0184;.0214,.0164,.0176;.0214,.0166,.0182;.0226,.017,.0178;.0232,.017,.0178]（默认）|
    非负标量矩阵
  group: ''
- name: Algorithm data type
  summary: '选择模块算法数据类型的选项 Inherit: auto（默认）| double | single | <data type expression>'
  group: ''
```

### **Vector of state-of-charge values, SOC (-)** — SOC 断点 `[0, .1, .25, .5, .75, .9, 1]`（默认）| `0` 到 `1` 之间的非负标量向量

SOC 断点向量，定义您指定查找数据的点。此向量必须严格递增。

### **Vector of temperatures, T** — 温度断点 `[278, 293, 313]`（默认）| 正标量向量

温度断点向量，定义您指定查找数据的点。此向量必须严格递增且大于 `0` `K`。此参数的物理单位必须与 **Temperature** 输入端口的物理单位相同。

### **Terminal resistance when battery cell is new, R0new(SOC,T), (ohm)** — 电池电芯全新时的端子电阻 `[.0117, .0085, .009; .011, .0085, .009; .0114, .0087, .0092; .0107, .0082, .0088; .0107, .0083, .0091; .0113, .0085, .0089; .0116, .0085, .0089]`（默认）| 非负标量矩阵

电池电芯全新时的端子电阻，单位为欧姆。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

### **Terminal resistance at end of life, R0eol(SOC,T), (ohm)** — 寿命终止时的端子电阻 `[.0234,.017,.018;.022,.017,.018;.0228,.0174,.0184;.0214,.0164,.0176;.0214,.0166,.0182;.0226,.017,.0178;.0232,.017,.0178]`（默认）| 非负标量矩阵

电池寿命终止时的端子电阻，单位为欧姆。此矩阵的行数等于 **Vector of state-of-charge values, SOC (-)** 参数的大小。此矩阵的列数等于 **Vector of temperatures, T** 参数的大小。

### **Algorithm data type** — 选择模块算法数据类型的选项 `Inherit: auto`（默认）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以以 `single` 和 `double` 精度仿真该模块。您必须将输入和参数显式指定为 `single` 或 `double`。
- `double` — 模块算法将所有输入和参数转换为 `double` 数据类型。
- `single` — 模块算法将所有输入和参数转换为 `single` 数据类型。
- `<data type expression>` — 模块算法将所有输入和参数转换为您指定的数据类型对象。

点击 **Show data type assistant** 按钮 以显示 **Data Type Assistant**，它可帮助您设置数据类型属性。有关详细信息，请参阅 Specify Data Types Using Data Type Assistant 和 Control Data Types of Signals。
## 所属库

Simscape / Battery / BMS / Estimators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

### R2025a：使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

您现在可以使用 **Algorithm data type** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

## 描述

健康状态估计器

SOH Estimator 模块实现了一个估计器，用于计算电池的健康状态（SOH）。SOH 反映电池相对于其理想条件的状况。健康变化意味着电池的容量和功率随时间衰减。

此模块支持单精度和双精度浮点仿真。

**注意**

要启用单精度浮点仿真，所有输入和参数的数据类型必须为 `single`。

此图显示了该模块的结构：

### 方程

端子电阻 *R*0 是电池老化的重要指标。您可以使用 SOC Estimator (Adaptive Kalman Filter) 模块来估计端子电阻。SOH Estimator 模块根据端子电阻 *R*0 计算 SOH：

SOH=REOL−R0REOL−R0,new

其中 *R*EOL 是寿命终止时的电阻，*R*0,new 是电池全新时的端子电阻。
