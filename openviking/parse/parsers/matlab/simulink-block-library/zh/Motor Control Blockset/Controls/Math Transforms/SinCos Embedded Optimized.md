---
type: simulink-block
title: 'SinCos Embedded Optimized'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Math Transforms'
documentation_page: 'sincosembeddedoptimized'
documentation_source_path: 'ref/sincosembeddedoptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# SinCos Embedded Optimized

## 端口

### 输入

### **θe** — 参考电压位置标量

参考电压信号的位置或相位值，指定为标量，单位可以是标幺值、弧度或度。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **sin** — 正弦电压波形标量

正弦波形输出，其频率与位置或相位信号（`θe`）的频率相同。

**数据类型：** `single` | `double` | `fixed point`

### **cos** — 余弦电压波形标量

余弦波形输出，其频率与位置或相位信号（`θe`）的频率相同。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Optimize for selected embedded target hardware** — 为所选硬件优化模块 `off`（默认）| on

选择此参数可针对您所使用的嵌入式目标硬件自动优化模块。如果选择此参数，模块会自动选择一种针对您的硬件目标优化的近似方法（用于计算正弦和余弦信号）。

例如，如果您在包含此模块的 Simulink 模型的配置参数对话框的 **Hardware Implementation** 选项卡中的 **Hardware board** 参数中选择了任何 Texas Instruments 硬件目标，模块会自动将 **Approximation method** 参数设置为 `TI IQMATH`。有关支持的近似方法的详细信息，请参阅 Approximation method 参数。

### **Approximation method** — 计算正弦和余弦信号的近似方法 `Lookup`（默认）| `None` | `CORDIC` | `TI IQMATH`

指定用于计算正弦和余弦输出信号的近似类型。您可以选择以下值之一。

- `None` — 如果您不想使用任何近似方法，请选择此值。
- `CORDIC` — 如果您想使用 CORDIC 近似方法，请选择此值。
- `Lookup` — 如果您想使用查找近似方法，请选择此值。
- `TI IQMATH` — 如果您使用的是 Texas Instruments 硬件目标，模块会选择此值。

#### 依赖关系

您无法手动选择 `TI IQMATH` 值。模块会在以下情况下自动选择此值：

- 您在包含此模块的 Simulink 模型的配置参数对话框的 **Hardware Implementation** 选项卡中的 **Hardware board** 参数中选择了任何 Texas Instruments 硬件目标。
- 您选择了 **Optimize for selected embedded target hardware** 参数。

### **Theta units** — `θe` 的单位 `Per-unit`（默认）| `Radians` | `Degrees`

输入参考电压位置的单位。

#### 依赖关系

要启用此参数，请将 **Approximation method** 参数设置为 `None` 或 `Lookup`。

### **Number of data points for lookup table** — 查找表数组的大小 `1024`（默认）| 标量

查找表数组的大小。此参数接受 125 到 4095 之间的值。

**注意**

根据您在此参数中输入的值，模块会使用最接近 `(125*n)+2` 的值。模块执行此近似以优化硬件中的计算。

#### 依赖关系

要启用此参数，请将 **Approximation method** 参数设置为 `Lookup`。

### **Table data type** — 查找表数组的数据类型 `Inherit: Inherit via input`（默认）| `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

查找表数组的数据类型，指定为：

- `Inherit: Inherit via input`
- `double`
- `single`
- `fixdt(1,16,0)`
- `<data type expression>`

有关设置数据类型的详细信息，请参阅 Control Data Types of Signals。

#### 依赖关系

要启用此参数，请将 **Approximation method** 参数设置为 `Lookup`。

### **Number of iterations** — CORDIC 算法的迭代次数 `11`（默认）| 正整数，小于或等于定点输入的位字长

指定执行 CORDIC 算法的迭代次数。默认值为 11。

- 当模块输入使用浮点数据类型时，迭代次数可以是正整数。
- 当模块输入为定点数据类型时，迭代次数不能超过位字长。

  例如，如果模块输入为 `fixdt(1,16,15)`，则位字长为 16。在这种情况下，迭代次数不能超过 16。

#### 依赖关系

要启用此参数，请将 **Approximation method** 参数设置为 `CORDIC`。

### **Theta data type** — 查找表数组的数据类型 `fixdt([],16,0)`（默认）| `double` | `single` | `<data type expression>`

查找表数组的数据类型，指定为：

- `double`
- `single`
- `fixdt([],16,0)`
- `<data type expression>`

有关设置数据类型的详细信息，请参阅 Control Data Types of Signals。

#### 依赖关系

要启用此参数，请通过以下方式将模块配置为使用 `TI IQMATH` 近似方法：

- 在包含此模块的 Simulink 模型的配置参数对话框的 **Hardware Implementation** 选项卡中，在 **Hardware board** 参数中选择任意 Texas Instruments 硬件目标。
- 选择 **Optimize for selected embedded target hardware** 参数。

## 所属库

Motor Control Blockset / Controls / Math Transforms

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2024b 中引入**

## 描述

实现正弦和余弦函数

SinCos Embedded Optimized 模块使用指定的位置或相位输入信号实现正弦和余弦函数。

该模块支持 CORDIC、TI IQMATH 和基于查找表的近似方法来计算正弦和余弦信号。下表列出了每种近似方法支持的数据类型、θe 输入单位以及使用场景。

| 近似方法 | 支持的数据类型 | 支持的 θe 输入单位 | 何时使用此方法 |
| --- | --- | --- | --- |
| None | 浮点 | - 标幺值（0 到 1）- 弧度（0 到 2π）- 度（0 到 360） | 您希望使用默认的泰勒级数算法。 |
| CORDIC | 浮点和定点 | 弧度（-π 到 π） | 您希望进行快速、近似的迭代计算。 |
| Lookup | 浮点和定点 | - 标幺值（0 到 1）- 弧度（0 到 2π）- 度（0 到 360） | 您希望使用快速、近似的查找表实现。 |
| Texas Instruments® IQMATH | 定点（`TI IQMATH` 不支持 16 位定点数据类型） | 标幺值（0 到 1） | 您无法手动选择此值。当您针对 Texas Instruments 硬件优化模块时，模块会自动选择此值。 |

该模块使您能够为在包含此模块的 Simulink® 模型的配置参数对话框的 **Hardware Implementation** 选项卡中选择的硬件板自动选择优化的近似方法。

例如，如果您选择任意 Texas Instruments 硬件目标，模块会自动选择 Texas Instruments IQ math 近似方法。

### CORDIC 近似方法

CORDIC 是 COordinate Rotation DIgital Computer（坐标旋转数字计算机）的缩写。基于 Givens 旋转的 CORDIC 算法是现有硬件效率最高的算法之一，因为它只需要迭代的移位-加法运算。有关更多信息，请参阅 CORDIC。该模块输入还有进一步的要求。

有关选择 CORDIC 近似方法的更多信息，请参阅近似方法。

下表总结了无效输入时会发生的情况。

| 模块使用 | 无效输入的影响 |
| --- | --- |
| 仿真模式 | 出现错误。 |
| 生成的代码 | 发生未定义行为。避免依赖生成代码的未定义行为。 |

### 查找近似方法

该模块支持查找表方法。当与 Motor Control Blockset™ 中附带的示例所采用的模型设置和配置一起使用时，此方法可实现优化的代码执行。您可以在 **Number of data points for lookup table** 参数中指定查找表点的数量。

下图显示了输入位置以及该模块使用查找近似方法生成的 sine 和 cosine 输出信号：

有关选择查找近似方法的更多信息，请参阅近似方法。
