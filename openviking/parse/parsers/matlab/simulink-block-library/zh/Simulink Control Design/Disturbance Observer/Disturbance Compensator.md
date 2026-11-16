---
type: simulink-block
title: 'Disturbance Compensator'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Disturbance Observer'
documentation_page: 'disturbancecompensator'
documentation_source_path: 'ug/disturbancecompensator.html'
language: zh-CN
chinese_source: worker-translation
---

# Disturbance Compensator

## 端口

### 输入

### **u0** — 标称控制器输入 标量 | 向量

指定模型的标称控制器输入，为 *Nu*×1 信号，其中 *Nu* 是模型中的输入数量。

### **y** — 测量输出 标量 | 向量

指定模型的测量输出，为 *Ny*×1 信号，其中 *Ny* 是模型中的输出数量。

### **A** — 状态矩阵 标量 | 向量 | 矩阵

指定状态矩阵，为 *Nx*×*Nx* 信号，其中 *Nx* 是模型中的状态数量。

#### 依赖项

要启用此端口，请选择 **Use external source for model matrices (A,Bu,Cm)** 和 **Use external source for L** 参数。

### **Bu** — 输入矩阵 标量 | 向量 | 矩阵

指定输入矩阵，为 *Nx*×*Nu* 信号，其中 *Nx* 是模型中的状态数量，*Nu* 是模型中的输入数量。

#### 依赖项

要启用此端口，请选择 **Use external source for model matrices (A,Bu,Cm)** 和 **Use external source for L** 参数。

### **Cm** — 输出矩阵 标量 | 向量 | 矩阵

指定输出矩阵，为 *Ny*×*Nx* 信号，其中 *Nx* 是模型中的状态数量，*Ny* 是模型中的输出数量。

#### 依赖项

要启用此端口，请选择 **Use external source for model matrices (A,Bu,Cm)** 和 **Use external source for L** 参数。

### **Bd** — 扰动矩阵 标量 | 向量 | 矩阵

指定扰动矩阵，为 *Nx*×*Nd* 信号，其中 *Nx* 是模型中的状态数量，*Nd* 是模型中的扰动数量。

#### 依赖项

要启用此端口，请选择 **Use external source for matrix Bd** 和 **Use external source for L** 参数。

### **S0** — 初始条件 标量 | 向量

指定扩展状态的初始条件，为长度为 *Nx* + *Nd* 的标量或向量，其中 *Nx* 是模型中的状态数量，*Nd* 是模型中的扰动数量。

#### 依赖项

要启用此端口，请选择 **Use external source for initial conditions S0 (x0,d0)**。

### **L** — 观测器矩阵 标量 | 向量 | 矩阵

指定观测器矩阵，为 (*Nx*+*Nd*)×*Ny* 信号。

#### 依赖项

要启用此端口，请选择 **Use external source for matrix L**。

### **Kd** — 补偿增益矩阵 标量 | 向量 | 矩阵

指定补偿增益矩阵 *Kd*，为 *Nu*×*Nd* 信号。

#### 依赖项

要启用此端口，请选择 **Use external source for matrix Kd**。

### 输出

### **u** — 修改后的控制输入 标量

修改后的控制输入，返回为 *Nu*×1 信号，其中 *Nu* 是模型中的输入数量。

### **dhat** — 估计扰动 向量

模型中估计的扰动，返回为 *Nd*×1 信号，其中 *Nd* 是模型中的扰动数量。

#### 依赖项

要启用此端口，请选择 **Output estimated disturbances dhat**。

### **xhat** — 估计状态 向量

模型的估计状态，返回为 *Nx*×1 信号，其中 *Nx* 是模型中的状态数量。

#### 依赖项

要启用此端口，请选择 **Output estimated model states xhat**。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。从 Simulink® Toolstrip 的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 参数选项卡

### **Time domain** — 控制器时域 **discrete-time**（默认）| **continuous-time**

指定控制器时域。

选择 **discrete-time** 时，使用 **Sample time** 参数指定采样时间。

### **LTI state-space variable** — 已知被控对象动态 `ss` 对象 | `idss` 对象

将已知被控对象动态指定为状态空间模型对象。您可以从被控对象的物理表示或近似表示获得此模型。

### **Use external source for model matrices (A,Bu,Cm)** — 在模块输入端口指定模型矩阵 `off`（默认）| `on`

选择此选项以使用模块输入端口 **A**、**Bu** 和 **Cm** 分别指定模型矩阵 *A*、*Bu* 和 *Cm*。

#### 依赖项

要启用此参数，您还必须选择 **Use external source for L** 参数。

### **Number of states** — 模型中的状态数量 `1`（默认）| 正整数

当您将模型矩阵指定为模块输入时，使用此参数指定模型中的状态数量。

#### 依赖项

要启用此参数，请选择 **Use external source for model matrices (A,Bu,Cm)** 和 **Use external source for L** 参数。

### **Number of inputs** — 模型中的输入数量 `1`（默认）| 正整数

当您将模型矩阵指定为模块输入时，使用此参数指定模型中的输入数量。

#### 依赖项

要启用此参数，请选择 **Use external source for model matrices (A,Bu,Cm)** 和 **Use external source for L** 参数。

### **Number of outputs** — 模型中的输出数量 `1`（默认）| 正整数

当您将模型矩阵指定为模块输入时，使用此参数指定模型中的输出数量。

#### 依赖项

要启用此参数，请选择 **Use external source for model matrices (A,Bu,Cm)** 和 **Use external source for L** 参数。

### **Specify gain k (such that Bd = k\*Bu)** — 用于计算扰动输入矩阵的增益值 `1`（默认）| 非零标量

指定用于计算扰动矩阵 *Bd* 的增益值 *k*，使得 *Bd* = *k×Bu*。

### **Use external source for matrix Bd** — 在模块输入端口指定扰动矩阵 `off`（默认）| `on`

选择此选项以使用模块输入端口 **Bd** 指定扰动矩阵 *Bd*。

#### 依赖项

要启用此参数，您还必须选择 **Use external source for L** 参数。

### **Number of disturbances** — 模型中的扰动数量 `1`（默认）| 正整数

当您将扰动矩阵指定为模块输入时，使用此参数指定模型中的输入数量。

#### 依赖项

要启用此参数，请选择 **Use external source for matrix Bd** 和 **Use external source for L** 参数。

### **Initial conditions** — 扩展状态的初始条件 `0`（默认）| 标量 | 向量

指定扩展状态的初始条件，为长度为 *Nx* + *Nd* 的标量或向量，其中 *Nx* 是模型中的状态数量，*Nd* 是模型中的扰动数量。

### **Use external source for initial conditions S0 (x0,d0)** — 在模块输入端口指定初始条件 `off`（默认）| `on`

选择此选项以使用模块输入端口 **S0** 指定初始条件。

### 整定选项卡

### **Bandwidth (rad/s)** — 观测器带宽 `1`（默认）| 正标量

将观测器带宽 *ωo* 指定为正标量。

### **Spacing (rad/s)** — 观测器带宽间距 `0.01`（默认）| 正标量

指定闭环极点的间距。对于给定的观测器带宽 *ωo* 和极点间距 *δ*，模块将闭环极点放置在 [ωoωo+δωo+δ×2…ωo+δ×n]，其中 *n* 是闭环极点的数量。

### **Use external source for matrix L** — 在模块输入端口指定观测器矩阵 `off`（默认）| `on`

选择此选项以使用模块输入端口 **L** 指定观测器矩阵。

### **Use external source for matrix Kd** — 在模块输入端口指定补偿增益矩阵 `off`（默认）| `on`

选择此选项以使用模块输入端口 **Kd** 指定观测器矩阵。

### 模块选项卡

### **Limit output (u)** — 将模块输出限制到指定的饱和限值 `off`（默认）| `on`

将模块输出限制到指定的饱和限值的选项。使用 **Upper limit** 和 **Lower limit** 参数指定输出饱和限值。

### **Upper limit** — 模块输出的饱和上限 `inf`（默认）| 标量

指定模块输出的上限。当模块输出否则将超过此值时，模块输出保持在此值。

#### 依赖项

要启用此参数，请选择 **Limit output (u)** 参数。

### **Lower limit** — 模块输出的饱和下限 `–inf`（默认）| 标量

指定模块输出的下限。当模块输出否则将低于此值时，模块输出保持在此值。

#### 依赖项

要启用此参数，请选择 **Limit output (u)** 参数。

### **Data type** — 浮点精度 `double`（默认）| `single`

根据仿真环境或硬件要求指定浮点精度。

对于连续时间模型，模块仅支持 `double` 数据类型。

### **Time delay** — 指定时间延迟 `1`（默认）| 正标量 | 向量

将模型中的时间延迟指定为长度为 *Nu* 的标量或向量，其中 *Nu* 是模型中的输入数量。

对于离散时间模型，将延迟指定为采样时间的整数倍 *k*。离散时间中的延迟由 *Td* = *k*×*Ts* 给出。

#### 依赖项

要启用此参数，请选择 **Specify input delays** 参数。

### **Output estimated model states xhat** — 在模块输出端口输出估计状态 `off`（默认）| `on`

选择此选项以在模块输出 **xhat** 处输出估计的模型状态。

### **Output estimated model states dhat** — 在模块输出端口输出估计扰动 `off`（默认）| `on`

选择此选项以在模块输出 **dhat** 处输出估计的模型状态。

## 所属库

Simulink Control Design / Disturbance Observer

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

修改控制动作以补偿未知动态和扰动

使用 Disturbance Compensator 模块修改标称控制器的控制动作，以抑制和补偿模型中的扰动。为补偿扰动，Disturbance Compensator 模块使用扩展状态观测器来估计模型中的总扰动，并返回可用作被控对象输入的修改后控制器动作。

该模块按如下方式扩展了 ESO 的实现。

x˙/x+=Ax+Buu+Bddym=Cmxu=u0+Kdd^

其中：

- *x* 是被控对象状态。
- x˙ 是连续时间中的状态导数，*x+* 是离散时间中的状态更新 *x*[*k*+1]。
- *A*、*Bu* 和 *Cm* 是被控对象动态。
- *ym* 是可测被控对象输出。
- *Bd* 是扰动输入矩阵。
- *d* 是模型中的总扰动，包括未知动态以及内部和外部扰动。
- *u* 是修改后的控制器动作。
- *u0* 是标称控制器动作。
- *Kd* 是补偿增益矩阵。

该模块不要求您提供被控对象的实际模型。您可以指定从被控对象的物理表示或近似表示获得的动态。因此，扰动抑制的精度将取决于您所提供的被控对象近似的精度。

有关详细信息，请参阅使用扩展状态观测器进行控制设计与扰动补偿。
