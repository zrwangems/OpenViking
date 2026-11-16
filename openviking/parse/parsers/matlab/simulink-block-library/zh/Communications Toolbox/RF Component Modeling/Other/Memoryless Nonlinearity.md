---
type: simulink-block
title: 'Memoryless Nonlinearity'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Component Modeling / Other'
documentation_page: 'legacymemorylessnonlinearity'
documentation_source_path: 'ref/legacymemorylessnonlinearity.html'
language: zh-CN
chinese_source: worker-translation
---

# Memoryless Nonlinearity

## 端口

### 输入

### **In1** — 输入 RF 基带信号 标量 | 列向量

输入 RF 基带信号，指定为标量或列向量。
此输入中的值必须为复数。

**数据类型：** `double`
**复数支持：** Yes
### 输出

### **Out1** — 输出 RF 基带信号 标量 | 列向量

输出 RF 基带信号，以标量或列向量形式返回。输出的数据类型与输入相同。

## 参数

### **Method** — 非线性建模方法 `Cubic polynomial` (默认) | `Hyperbolic tangent` | `Saleh model` | `Ghorbani model` | `Rapp model`

非线性建模方法，指定为 `Cubic polynomial`、`Hyperbolic tangent`、`Saleh model`、`Ghorbani model`、`Rapp model` 或 `Lookup table`。有关详细信息，请参阅无记忆非线性损伤。

### **Linear gain (dB)** — 线性增益 `0` (默认) | 标量

线性增益，以 dB 为单位，指定为标量。此参数缩放输出信号的功率增益。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Cubic polynomial`、`Hyperbolic tangent` 或 `Rapp model`。

### **IIP3 (dBm)** — 三阶输入截取点 `30` (默认) | 标量

三阶输入截取点，以 dBm 为单位，指定为标量。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Cubic polynomial` 或 `Hyperbolic tangent`。

### **AM/PM conversion (degrees per dB)** — AM/PM 转换因子 `10` (默认) | 标量

AM/PM 转换因子，以 degrees per decibel 为单位，指定为标量。有关详细信息，请参阅 Cubic Polynomial 和 Hyperbolic Tangent 模型方法。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Cubic polynomial` 或 `Hyperbolic tangent`。

### **Lower input power limit for AM/PM conversion (dBm)** — 输入功率下限 `10` (默认) | 标量

输入功率下限，以 dBm 为单位，指定为小于 **Upper input power limit for AM/PM conversion (dBm)** 参数值的标量。对于 **[**Lower input power limit for AM/PM conversion (dBm)**, **Upper input power limit for AM/PM conversion (dBm)**]** 范围内的输入功率值，AM/PM 转换线性缩放。如果输入信号功率低于输入功率下限，则由 AM/PM 转换引起的相移为零。有关详细信息，请参阅 Cubic Polynomial 和 Hyperbolic Tangent 模型方法。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Cubic polynomial` 或 `Hyperbolic tangent`。

### **Upper input power limit for AM/PM conversion (dBm)** — 输入功率上限 `inf` (默认) | 标量

输入功率上限，以 dBm 为单位，指定为大于 **Lower input power limit for AM/PM conversion (dBm)** 参数值的标量。对于 **[**Lower input power limit for AM/PM conversion (dBm)**, **Upper input power limit for AM/PM conversion (dBm)**]** 范围内的输入功率值，AM/PM 转换线性缩放。如果输入信号功率低于输入功率下限，则由 AM/PM 转换引起的相移为零。有关详细信息，请参阅 Cubic Polynomial 和 Hyperbolic Tangent 模型方法。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Cubic polynomial` 或 `Hyperbolic tangent`。

### **Input scaling (dB)** — 输入信号缩放因子 `0` (默认) | 标量

输入信号缩放因子，以 dB 为单位，指定为标量。此参数缩放输入信号的功率增益。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Saleh model` 或 `Ghorbani model`。

### **AM/AM parameters [alpha beta]** — Saleh model 的 AM/AM 参数 `[2.1587 1.1517]` (默认) | 二元素向量

Saleh model 的 AM/AM 参数，用于计算输入信号的幅度增益，指定为二元素向量。有关详细信息，请参阅 Saleh Model 方法。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Saleh model`。

### **AM/PM parameters [alpha beta]** — Saleh model 的 AM/PM 参数 `[4.0033 9.1040]` (默认) | 二元素向量

Saleh model 的 AM/PM 参数，用于计算输入信号的相位变化，指定为二元素向量。有关详细信息，请参阅 Saleh Model 方法。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Saleh model`。

### **AM/AM parameters [x1 x2 x3 x4]** — Ghorbani model 的 AM/AM 参数 `[8.1081 1.5413 6.5202 -0.0718]` (默认) | 四元素向量

Ghorbani model 的 AM/AM 参数，用于计算输入信号的幅度增益，指定为四元素向量。有关详细信息，请参阅 Ghorbani Model 方法。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Ghorbani model`。

### **AM/PM parameters [y1 y2 y3 y4]** — Ghorbani model 的 AM/PM 参数 `[4.6645 2.0965 10.88 -0.003]` (默认) | 四元素向量

Ghorbani model 的 AM/PM 参数，用于计算输入信号的相位变化，指定为四元素向量。有关详细信息，请参阅 Ghorbani Model 方法。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Ghorbani model`。

### **Output scaling (dB)** — 输出信号缩放因子 `0` (默认) | 标量

输出信号缩放因子，以 dB 为单位，指定为标量。此参数缩放输出信号的功率增益。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Saleh model` 或 `Ghorbani model`。

### **Smoothness factor** — 平滑因子 `0.5` (默认) | 标量

平滑因子，指定为标量。有关详细信息，请参阅 Rapp Model 方法。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Rapp model`。

### **Output saturation level** — 输出饱和电平 `1` (默认) | 标量

输出饱和电平，指定为标量。有关详细信息，请参阅 Rapp Model 方法。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Rapp model`。

## 所属库

Communications Toolbox / RF Impairments and Components

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2025a: 此旧版接口已移除

(Legacy) Memoryless Nonlinearity 模块已被移除。要将无记忆非线性应用于复基带信号，请使用 Memoryless Nonlinearity 模块。

### R2024a: 此旧版接口将不再受支持

在 R2023a 中，Memoryless Nonlinearity 模块更新了在放大器模型中应用无记忆非线性损伤的方法。要加载模块的更新版本，请在使用了 (Legacy) Memoryless Nonlinearity 模块的 pre-R2023a 仿真上运行 **Update Model**。

### R2023a: 此旧版接口将不再受支持

在 R2023a 中，Memoryless Nonlinearity 模块更新了在放大器模型中应用无记忆非线性损伤的方法。具有旧版接口的模块运行时不会发出警告，但建议使用更新后的模块。要加载模块的更新版本，请在使用了 (Legacy) Memoryless Nonlinearity 模块的 pre-R2023a 仿真上运行 **Update Model**。

更新后的模块移除了 Hyperbolic tangent 和 Ghorbani 方法，将 Rapp 方法替换为 modified Rapp 方法，修改参数以应用 cubic polynomial 方法，并添加了使用 lookup table 定义损伤设置的 AM/AM-AM/PM 方法。有关新接口，请参阅 Memoryless Nonlinearity 参考页。

## 描述

（已移除）将无记忆非线性应用于复基带信号

(Legacy) Memoryless Nonlinearity 模块将无记忆非线性损伤应用于复基带信号。使用此模块对由射频 (RF) 发射机或接收机中的信号放大引起的无记忆非线性损伤进行建模。有关详细信息，请参阅无记忆非线性损伤。

**注意**

所有功率值均假设标称阻抗为 1 ohm。
