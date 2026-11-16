---
type: simulink-block
title: 'Radar Target'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'radartarget'
documentation_source_path: 'ref/radartarget.html'
language: zh-CN
chinese_source: worker-translation
---

# Radar Target

## 端口

### 输入

### **X** — 入射信号，复值 *N*×*1* 列向量 | 复值 *N*×*M* 矩阵

入射信号，指定为复值 *N*×*1* 列向量或复值 *N*×*M* 矩阵。*M* 的值是信号数。每个信号对应一个不同的目标。*N* 的值是每个信号中的样本数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`

### **RCS** — 平均雷达横截面，非负标量 | 1×*M* 的非负值行向量

平均雷达横截面，指定为非负标量或 1×*M* 的非负值行向量。*M* 是目标数。此参数适用于起伏和非起伏目标。如果指定 *M* 个入射信号，则可以将雷达横截面指定为标量或 1×*M* 向量。对于标量，同一值将应用于所有信号。单位为 m²。

#### 依赖关系

要启用此端口，请将 **Source of mean radar cross section** 下拉菜单设置为 `Input port`。

**数据类型：** `double`

### **Update** — 用于更新雷达横截面的指示符 0 | 1

用于更新起伏目标的雷达横截面的指示符，指定为 0 或 1。当设置为 0 时，雷达横截面恒定。当设置为 1 时，雷达横截面起伏。

#### 依赖关系

要启用此端口，请将 **Fluctuation model** 下拉菜单设置为除 `Nonfluctuating` 之外的任何值。

**数据类型：** `double`

### 输出

### **Out** — 反射信号，复值 *N*×*1* 列向量 | 复值 *N*×*M* 矩阵

反射信号，返回为复值 *N*×*1* 列向量或复值 *N*×*M* 矩阵。*M* 的值是信号数。每个信号对应一个不同的目标。*N* 的值是每个信号中的样本数。

## 参数

### **Source of mean radar cross section** — 平均雷达横截面的来源 `Property`（默认） | `Input port`

指定目标的平均雷达横截面 (RCS) 值是来自此模块的 **Mean radar cross section** 参数还是来自输入端口。此参数的值为

|  |  |
| --- | --- |
| `Property` | 此模块的 **Mean radar cross section** 参数指定平均 RCS 值。 |
| `Input port` | 选择此值会创建 `RCS` 输入端口，以指定平均雷达横截面。 |

### **Mean radar cross section (m^2)** — 平均雷达横截面 `1`

将目标雷达横截面的平均值指定为非负标量，单位为平方米。仅当 **Source of mean radar cross section** 参数设置为 `Property` 时，此参数才会出现。

### **Fluctuation model** — 起伏模型 `Nonfluctuating`（默认） | `Swerling1` | `Swerling2` | `Swerling3` | `Swerling4`

将目标的统计模型指定为 `Nonfluctuating`、`Swerling1`、`Swerling2`、`Swerling3` 或 `Swerling4` 之一。将此参数设置为除 `Nonfluctuating` 之外的值，允许通过输入端口 `Update` 设置横截面参数。

### **Propagation speed (m/s)** — 信号传播速度 `physconst('LightSpeed')`（默认） | 正标量

信号传播速度，指定为实值正标量。光速的默认值是 `physconst('LightSpeed')` 返回的值。

**数据类型：** `double`

### **Operating frequency (Hz)** — 工作频率 `3e8`（默认） | 正实标量

指定从目标反射的信号的载波频率，以赫兹为单位的正标量。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认） | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间来编译，但通常运行更快。

当您在开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅“选择仿真模式”(Simulink)。

#### 编程用法

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Environment and Target

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014b 中引入**

## 描述

雷达目标

Radar Target 模块对雷达目标建模，该目标根据指定的雷达横截面 (RCS) 反射信号。该模块支持非起伏目标模型和所有四种 Swerling 目标模型。该模块不支持极化信号。
