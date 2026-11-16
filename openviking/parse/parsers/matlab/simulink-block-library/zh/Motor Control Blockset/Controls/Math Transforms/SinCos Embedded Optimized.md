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

参考电压信号的位置或相位值，指定为 per-unit、radians 或 degrees 的标量。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **sin** — 正弦电压波形标量

正弦波形输出，其频率与位置或相位信号（`θe`）的频率相同。

**数据类型：** `single` | `double` | `fixed point`

### **cos** — 余弦电压波形标量

余弦波形输出，其频率与位置或相位信号（`θe`）的频率相同。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **为选定的嵌入式目标硬件优化** — 为选定硬件优化模块 `off` (default) | on

选择此参数可自动为正在使用的嵌入式目标硬件优化模块。如果选择此参数，模块会自动选择一种针对硬件目标优化的近似方法（用于计算正弦和余弦信号）。

例如，如果在包含此模块的 Simulink 模型的“配置参数”对话框的“硬件实现”选项卡中可用的 **硬件板** 参数中选择任何 Texas Instruments 硬件目标，则模块会自动将 **近似方法** 参数设置为 `TI IQMATH`。有关支持的近似方法的详细信息，请参阅近似方法参数。

### **近似方法** — 用于计算正弦和余弦信号的近似方法 `Lookup` (default) | `None` | `CORDIC` | `TI IQMATH`

指定用于计算正弦和余弦输出信号的近似类型。您可以选择以下值之一。

- `None` — 如果不想使用任何近似，请选择此值。
- `CORDIC` — 如果要使用 CORDIC 近似方法，请选择此值。
- `Lookup` — 如果要使用查找近似方法，请选择此值。
- `TI IQMATH` — 如果您使用 Texas Instruments 硬件目标，则模块选择此值。

#### 依赖关系

您不能手动选择值 `TI IQMATH`。当以下情况时，模块会自动选择此值：

- 您在包含此模块的 Simulink 模型的“配置参数”对话框的“硬件实现”选项卡中可用的 **硬件板** 参数中选择任何 Texas Instruments 硬件目标。
- 您选择 **为选定的嵌入式目标硬件优化** 参数。

### **Theta 单位** — `θe` 的单位 `Per-unit` (default) | `Radians` | `Degrees`

输入参考电压位置的単位。

#### 依赖关系

要启用此参数，请将 **近似方法** 参数设置为 `None` 或 `Lookup`。

### **查找表的数据点数量** — 查找表数组的大小 `1024` (default) | scalar

查找表数组的大小。此参数接受 125 到 4095 之间的值。

**注意**

根据您在此参数中输入的值，模块使用最接近 `(125*n)+2` 的值。模块执行此近似以优化硬件中的计算。

#### 依赖关系

要启用此参数，请将 **近似方法** 参数设置为 `Lookup`。

### **表数据类型** — 查找表数组的数据类型 `Inherit: Inherit via input` (default) | `double` | `single` | `fixdt(1,16,0)` | `<data type expression>`

查找表数组的数据类型，指定为：

- `Inherit: Inherit via input`
- `double`
- `single`
- `fixdt(1,16,0)`
- `<data type expression>`

有关设置数据类型的详细信息，请参阅控制信号的数据类型。

#### 依赖关系

要启用此参数，请将 **近似方法** 参数设置为 `Lookup`。

### **迭代次数** — CORDIC 算法的迭代次数 `11` (default) | positive integer, less than or equal to word length of fixed-point input

指定执行 CORDIC 算法的迭代次数。默认值为 11。

- 当模块输入使用 floating-point 数据类型时，迭代次数可以为正整数。
- 当模块输入为 fixed-point 数据类型时，迭代次数不能超过字长。

  例如，如果模块输入为 `fixdt(1,16,15)`，则字长为 16。在这种情况下，迭代次数不能超过 16。

#### 依赖关系

要启用此参数，请将 **近似方法** 参数设置为 `CORDIC`。

### **Theta 数据类型** — 查找表数组的数据类型 `fixdt([],16,0)` (default) | `double` | `single` | `<data type expression>`

查找表数组的数据类型，指定为：

- `double`
- `single`
- `fixdt([],16,0)`
- `<data type expression>`

有关设置数据类型的详细信息，请参阅控制信号的数据类型。

#### 依赖关系

要启用此参数，请通过以下方式将模块配置为使用 `TI IQMATH` 近似方法：

- 在包含此模块的 Simulink 模型的“配置参数”对话框的“硬件实现”选项卡中可用的 **硬件板** 参数中选择任何 Texas Instruments 硬件目标。
- 选择 **为选定的嵌入式目标硬件优化** 参数。

## 所属库

Motor Control Blockset / Controls / Math Transforms

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2024b 中引入**

## 描述

实现正弦和余弦函数

SinCos Embedded Optimized 模块使用指定的位置或相位输入信号实现正弦和余弦函数。

该模块支持 CORDIC、TI IQMATH 和基于查找的近似方法来计算正弦和余弦信号。下表列出了每种近似方法支持的数据类型、θe 输入单位以及用例。

| 近似方法 | 支持的数据类型 | 支持的 θe 输入单位 | 何时使用此方法 |
| --- | --- | --- | --- |
| None | Floating point | - Per-unit (0 to 1) - Radians (0 to 2π) - Degrees (0 to 360) | 您希望使用默认 Taylor 级数算法。 |
| CORDIC | Floating point and fixed point | Radians (-π to π) | 您需要快速、近似的迭代计算。 |
| Lookup | Floating point and fixed point | - Per-unit (0 to 1) - Radians (0 to 2π) - Degrees (0 to 360) | 您需要快速、近似的查找表实现。 |
| Texas Instruments® IQMATH | Fixed point  (`TI IQMATH` does not support 16-bit fixed point data type) | Per-unit (0 to 1) | 您不能手动选择此值。当您针对 Texas Instruments 硬件优化模块时，模块会自动选择此值。 |

该模块使您能够为在包含此模块的 Simulink® 模型的“配置参数”对话框的“硬件实现”选项卡中选择的硬件板自动选择优化的近似方法。

例如，如果您选择任何 Texas Instruments 硬件目标，该模块会自动选择 Texas Instruments IQ math 近似方法。

### CORDIC 近似方法

CORDIC 是 COordinate Rotation DIgital Computer 的首字母缩写。基于 Givens 旋转的 CORDIC 算法是可用硬件效率最高的算法之一，因为它仅需要迭代移位加法运算。有关详细信息，请参阅 CORDIC。模块输入有进一步要求。

有关选择 CORDIC 近似方法的详细信息，请参阅近似方法。

下表总结了无效输入时发生的情况。

| 模块用法 | 无效输入的影响 |
| --- | --- |
| 仿真模式 | 出现错误。 |
| 生成的代码 | 发生未定义行为。避免依赖生成代码的未定义行为。 |

### 查找近似方法

该模块支持查找表方法。当与 Motor Control Blockset™ 中提供的示例所采用的模型设置和配置一起使用时，此方法可实现优化的代码执行。您可以在 **查找表的数据点数量** 参数中指定查找表点的数量。

下图显示了输入位置以及模块使用查找近似方法生成的正弦和余弦输出信号：

有关选择查找近似方法的详细信息，请参阅近似方法。
