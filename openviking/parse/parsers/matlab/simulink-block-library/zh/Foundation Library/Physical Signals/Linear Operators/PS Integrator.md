---
type: simulink-block
title: 'PS Integrator'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Linear Operators'
documentation_page: 'psintegrator'
documentation_source_path: 'ref/psintegrator.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Integrator

## 端口

### 输入

### **I** — Input physical signal, *u*, untyped physical signal

输入物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

### **R** — Reset physical signal, *R*, untyped physical signal

复位物理信号。根据 **External reset** 参数的值，模块在复位信号的上升沿、下降沿或上升沿和下降沿两者时，将输出复位到初始条件。

#### 依赖关系

要启用此端口，请将 **External reset** 参数设置为 `Rising`、`Falling` 或 `Either`。

### **X0** — Initial condition physical signal, *XO*, untyped physical signal

物理信号输入端口，用于指定模块的初始条件。此信号的单位必须与输出信号 *y* 的单位一致。

#### 依赖关系

要启用此端口，请将 **Initial condition source** 参数设置为 `External`。

### **U** — Upper saturation bound physical signal, *U*, untyped physical signal

物理信号输入端口，用于指定模块输出的上限饱和边界。此信号的单位必须与输出信号 *y* 的单位一致。

#### 依赖关系

要启用此端口，请将 **Limit output** 参数设置为 `Upper` 或 `Both`，并将 **Limit output source** 参数设置为 `External`。

### **L** — Lower saturation bound physical signal, *L*, untyped physical signal

物理信号输入端口，用于指定模块输出的下限饱和边界。此信号的单位必须与输出信号 *y* 的单位一致。

#### 依赖关系

要启用此端口，请将 **Limit output** 参数设置为 `Lower` 或 `Both`，并将 **Limit output source** 参数设置为 `External`。

### 输出

### **O** — Output physical signal, *y*, untyped physical signal

输出物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

## 参数

### **External reset** — Whether block resets to initial condition based on external reset signal `None`（默认） | `Rising` | `Falling` | `Either`

您可以指定模块基于外部信号将其状态复位到指定的初始条件。默认情况下，模块不复位其状态。将此参数设置为 `None` 以外的选项会显示输入端口 **R**。根据参数值，模块在复位信号的上升沿、下降沿或上升沿和下降沿两者时复位其状态。

### **Initial condition source** — Whether to specify initial condition as block parameter or additional input signal `Internal`（默认） | `External`

您可以将模块的初始条件指定为模块参数或输入信号：

- `Internal` — 使用 **Initial condition** 参数定义积分的初始条件。
- `External` — 使用端口 **X0** 处的外部物理信号定义积分的初始条件。

### **Limit output** — Whether to limit integrator output `None`（默认） | `Upper` | `Lower` | `Both`

您可以为输出信号指定上限和下限，并使模块用作受限积分器：

- `None` — 不限制输出。
- `Upper` — 将输出限制在上限。
- `Lower` — 将输出限制在下限。
- `Upper` — 将输出同时限制在上限和下限。

有关详细信息，请参阅限制输出。

### **Limit output source** — Whether to specify saturation bounds as block parameters or input signals `Internal`（默认） | `External`

选择在限制输出时指定上限和下限的方式：

- `Internal` — 使用 **Upper limit** 和 **Lower limit** 参数定义饱和边界。
- `External` — 使用端口 **U** 和 **L** 处的外部物理信号定义饱和边界。

#### 依赖关系

要启用此参数，请将 **Limit output** 参数设置为 `None` 以外的值。

### **Initial condition** — Initial state for the integration `0 s`（默认） | scalar

用于在仿真运行开始时计算模块初始状态的初始条件。

为 **Initial condition** 参数指定的单位必须与输出信号的单位匹配。默认情况下，输入信号无单位。此时输出信号以 `s` 为单位，**Initial condition** 参数的单位也为 `s`。如果您的输入信号具有物理单位，请将此单位乘以时间单位，以为 **Initial condition** 参数设置正确的单位。例如，如果输入信号以 `m/s` 为单位，则应将 **Initial condition** 参数的单位指定为 `m`。

#### 依赖关系

要启用此参数，请将 **Initial condition source** 设置为 `Internal`。

### **Upper limit** — Upper saturation limit for block output `inf s`（默认） | scalar

模块输出的上限饱和限制。为 **Upper limit** 参数指定的单位必须与输出信号的单位匹配。

#### 依赖关系

要启用此参数，请将 **Limit output** 参数设置为 `Upper` 或 `Both`，并将 **Limit output source** 参数设置为 `Internal`。

### **Lower limit** — Lower saturation limit for block output `-inf s`（默认） | scalar

模块输出的下限饱和限制。为 **Lower limit** 参数指定的单位必须与输出信号的单位匹配。

#### 依赖关系

要启用此参数，请将 **Limit output** 参数设置为 `Lower` 或 `Both`，并将 **Limit output source** 参数设置为 `Internal`。

## 所属库

Simscape / Foundation Library / Physical Signals / Linear Operators

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

### R2022b: 使用饱和边界限制模块输出

模块包含 **Limit output**、**Limit output source**、**Upper limit** 和 **Lower limit** 参数。使用这些参数限制输出信号。有关详细信息，请参阅限制输出。

### R2021a: 在事件时复位模块状态

模块包含一个附加参数 **External reset**，它允许您指定当端口 **R** 处的物理信号触发复位时，模块输出复位到初始条件。初始条件来源现在可以是物理信号或模块参数。如果将 **Initial condition source** 参数设置为 `External`，则端口 **X0** 处的物理信号提供用于积分和复位的初始条件值。

### R2019a: 单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含不支持单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅升级包含旧版物理信号模块的模型。

## 描述

对物理信号进行积分

PS Integrator 模块输出其输入在当前时间步的积分。以下方程表示该模块的输出：

y(t)=∫t0tu(t)dt+y0

其中：

- *u* 是输入端口 **I** 处的物理信号。
- *y*0 是初始条件。
- *y* 是输出端口 **O** 处的物理信号。
- *t* 是时间。

PS Integrator 模块是一个具有一个状态（其输出）的动态系统。PS Integrator 模块的输入是状态的时间导数：

x=y(t)

x0=y0

x˙=u(t)

求解器通过使用当前输入值和上一时间步的状态值，计算 PS Integrator 模块在当前时间步的输出。PS Integrator 模块保存其在当前时间步的输出，以供求解器计算下一时间步的输出时使用。该模块还向求解器提供初始条件，以用于在仿真运行开始时计算模块的初始状态。初始条件的默认值为 0 s。您可以将初始条件指定为模块参数或输入信号，以指定另一个值：

- 要将初始条件定义为模块参数，请将 **Initial condition source** 参数指定为 `Internal`，并为 **Initial condition** 参数输入值和单位。
- 要从外部来源提供初始条件，请将 **Initial condition source** 参数指定为 `External`。选择此选项会显示端口 **X0**。将外部初始条件信号连接到此端口。

由于该模块对输入信号随时间进行积分，输出信号的单位等于输入信号的单位乘以时间单位 s。例如，如果输入信号以 `m/s` 为单位，则输出信号以 `m` 为单位。为 **Initial condition** 参数指定的单位，或端口 **X0** 处的外部初始条件信号的单位，必须与输出信号的单位一致。

### 复位状态

该模块可以基于外部信号将其状态复位到指定的初始条件。默认情况下，**External reset** 参数设置为 `None`。要使模块复位其状态，请选择其他 **External reset** 选项之一：

- 选择 `Rising`，以在复位信号从负值或零上升到正值时复位状态。
- 选择 `Falling`，以在复位信号从正值下降到零或负值时复位状态。
- 选择 `Either`，以在复位信号从零变为非零值、从非零值变为零或改变符号时复位状态。

选择其中任一选项都会显示一个触发端口 **R**。将复位物理信号连接到此端口。

### 限制输出

该模块可以用作受限积分器，将其输出保持在指定的饱和边界内：

- 当积分小于或等于下限饱和限制时，模块将输出保持在下限饱和限制。
- 当积分位于下限饱和限制和上限饱和限制之间时，输出为积分值。
- 当积分大于或等于上限饱和限制时，模块将输出保持在上限饱和限制。

使用 **Limit output** 参数指定是在下限、上限还是两者处限制输出。**Limit output source** 参数提供了两种指定上限和下限的方式：

- `Internal` — 使用 **Upper limit** 和 **Lower limit** 参数定义饱和边界。
- `External` — 使用端口 **U** 和 **L** 处的外部物理信号定义饱和边界。
