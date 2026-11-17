---
type: simulink-block
title: 'SOC Estimator (Coulomb Counting, Variable Capacity)'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'BMS / Estimators'
documentation_page: 'socestimatorcoulombcountingvariablecapacity'
documentation_source_path: 'ref/socestimatorcoulombcountingvariablecapacity.html'
language: zh-CN
chinese_source: worker-translation
---

# SOC Estimator (Coulomb Counting, Variable Capacity)

## 端口
```yaml
ports:
- name: Current
  summary: 电池电流，安培标量 | 向量
  direction: input
- name: InitialSOC
  summary: 初始荷电状态，无量纲标量 | 向量
  direction: input
- name: AH
  summary: 电池电芯容量，A\*Hr 非负标量
  direction: input
- name: SOC
  summary: 电池荷电状态 标量 | 向量
  direction: output
```

### 输入

### **Current** — 电池电流，安培标量 | 向量

电池电流，单位为安培，指定为单个电芯的标量或多个电芯的向量。要将此输入指定为电芯电流向量，请选择 **Specify Current input as cell current(s)** 参数。

### **InitialSOC** — 初始荷电状态，无量纲标量 | 向量

初始荷电状态，指定为范围 [0, 1] 内的标量或向量。此输入端口的尺寸必须等于 **Current** 输入端口的尺寸。

### **AH** — 电池电芯容量，A\*Hr 非负标量

电池的电芯容量，单位为安时，指定为严格正标量。该模块通过将累积电荷除以此值来计算荷电状态。该模块通过对电池电流进行积分来计算累积电荷。

### 输出

### **SOC** — 电池荷电状态 标量 | 向量

电池的荷电状态，以标量或向量形式返回。此输出端口的尺寸等于 **Current** 和 **InitialSOC** 输入端口的尺寸。
## 参数
```yaml
parameters:
- name: Specify Current input as cell current(s)
  summary: 将电流输入端口指定为向量的选项 on（默认）| off
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 1（默认）| 0 | -1 | 整数
  group: ''
- name: Algorithm data type
  summary: '选择模块算法数据类型的选项 Inherit: auto（默认）| double | single | <data type expression>'
  group: ''
```

### **Specify Current input as cell current(s)** — 将电流输入端口指定为向量的选项 `on`（默认）| `off`

*自 R2023b 起*

将 **Current** 输入端口的值指定为电芯电流向量的选项。如果选择此参数，**Current** 输入端口的值可以是标量或尺寸等于模块输入尺寸的向量。

### **Sample time (-1 for inherited)** — 模块采样时间 `1`（默认）| 0 | -1 | 整数

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数指定为 `-1`。对于离散时间操作，请将此参数指定为正整数。对于连续时间操作，请将此参数指定为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

### **Algorithm data type** — 选择模块算法数据类型的选项 `Inherit: auto`（默认）| `double` | `single` | `<data type expression>`

*自 R2025a 起*

选择模块算法数据类型的选项，指定为以下值之一：

- `Inherit: auto` — 您可以以 `single` 和 `double` 精度对模块进行仿真。您必须将输入和参数显式提供为 `single` 或 `double`。
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

**在 R2023a 中引入**

### R2025a：使用 **Algorithm data type** 参数在单精度和双精度浮点仿真之间切换

您现在可以使用 **Algorithm data type** 参数轻松地在模块算法的单精度和双精度浮点仿真之间切换。

### R2023b: 将 Current 输入的值指定为电池单体电流向量

现在，您可以将 **Current** 输入端口的值指定为电池单体电流向量。

要启用向量化输入，请选择 **Specify Current input as cell current(s)** 参数。如果选择此参数，**Current** 输入端口必须与其他输入具有相同的大小，并表示各个电池单体的电流。

## 描述

使用库仑计数和可变容量进行荷电状态估计

SOC Estimator (Coulomb Counting, Variable Capacity) 模块实现了一个估计器，该估计器使用库仑计数法计算电池的荷电状态 (SOC)。电池的电池单体容量是该模块的一个输入。该模块通过将累积电荷除以该输入的值来计算荷电状态。然后，该模块通过对电池电流进行积分来计算累积电荷。

SOC 是可释放容量 *C*releasable 与额定容量 *C*rated 的比率。制造商提供每个电池额定容量的值，该值表示电池中的最大电荷量：

SOC=CreleasableCrated。

该模块支持单精度和双精度浮点仿真。

**注意**

要启用继承的单精度浮点仿真，所有输入和参数（**Sample time (-1 for inherited)** 参数除外）的数据类型都必须为 `single`。

您可以使用 **Sample time (-1 for inherited)** 参数在模块的连续实现和离散实现之间切换。要将模块配置为连续时间，请将 **Sample time (-1 for inherited)** 参数设置为 `0`。要将模块配置为离散时间，请将 **Sample time (-1 for inherited)** 参数设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

**注意**

该模块的连续时间实现仅在双精度浮点仿真中有效。如果您提供单精度浮点参数和输入，该模块会将它们转换为双精度浮点值以防止错误。

下图显示了该模块的结构：

### 方程

为了计算电池的 SOC，SOC Estimator (Coulomb Counting, Variable Capacity) 模块对安时和电流积分进行计数：

SOC=SOC(t0)+1Crated∫t0t0+τIbatt，

其中 *C*rated 是标称电池容量，*I*batt 是电池电流。
