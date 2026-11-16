---
type: simulink-block
title: 'PS Transfer Function'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Linear Operators'
documentation_page: 'pstransferfunction'
documentation_source_path: 'ref/pstransferfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Transfer Function

## 端口

### 输入

### **U** — 输入物理信号，untyped physical signal

输入物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

### **R** — 重置物理信号，*R*，untyped physical signal

重置物理信号。根据 **External reset** 参数值，模块在重置信号的上升沿、下降沿或上升沿和下降沿两者将输出重置为初始条件。

#### 依赖关系

要启用此端口，请将 **External reset** 参数设置为 `Rising`、`Falling` 或 `Either`。

### **Y0** — 初始输出物理信号，*YO*，untyped physical signal

物理信号输入端口，用于指定模块的初始输出，该输出也是重置后的输出值。

#### 依赖关系

要启用此端口，请将 **Initial output source** 参数设置为 `External`。

### 输出

### **Y** — 输出物理信号，untyped physical signal

输出物理信号。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的 **描述** 选项卡中的 **源代码** 链接，在底层源文件中看到此名称。

## 参数

### **Transfer function type** — 指定低通滤波器类型 `Lag`（默认） | `Lead-lag`

选择低通滤波器的类型：

- `Lag` — 对一阶低通滤波器建模。
- `Lead-lag` — 对超前-滞后滤波器建模。

### **Lag time constant, T** — 一阶低通滤波器的滞后时间常数 `1 s`（默认） | 正标量

一阶低通滤波器的滞后时间常数。

#### 依赖关系

当 **Transfer function type** 参数设置为 `Lag` 时启用。

### **Lead time constant, T1** — 超前-滞后滤波器的超前时间常数 `2 s`（默认） | 正标量

超前-滞后滤波器的超前时间常数。

#### 依赖关系

当 **Transfer function type** 参数设置为 `Lead-lag` 时启用。

### **Lag time constant, T2** — 超前-滞后滤波器的滞后时间常数 `1 s`（默认） | 正标量

超前-滞后滤波器的滞后时间常数。

#### 依赖关系

当 **Transfer function type** 参数设置为 `Lead-lag` 时启用。

### **External reset** — 指定模块是否基于外部重置信号将其状态重置为初始输出 `None`（默认） | `Rising` | `Falling` | `Either`

默认情况下，模块不会将其状态重置为初始输出。将此参数设置为 `None` 以外的选项会显示输入端口 **R**。根据参数值，模块在重置信号的上升沿、下降沿或上升沿和下降沿两者重置其状态。

### **Initial output source** — 选择将初始输出值指定为模块参数还是附加输入信号 `Internal`（默认） | `External`

您可以将模块的初始输出指定为模块参数或附加输入信号：

- `Internal` — 使用 **Initial output** 参数定义初始输出。
- `External` — 使用端口 **Y0** 处的外部物理信号定义初始输出。

### **Initial output** — 仿真开始和重置后的输出信号值和单位 `0 1`（默认） | 标量、向量或矩阵

仿真运行开始时和重置后的输出信号值和单位。第一个编辑框表示信号值。此值可以是标量、向量或矩阵，与端口 **Y** 处输出信号的大小匹配。

第二个组合框表示信号单位，其必须与端口 **Y** 处输出信号的单位一致。默认情况下，单位为 `1`（无单位）。您可以从下拉列表中选择单位，或键入所需单位名称（如 `rpm`）或有效表达式（如 `rad/s`）。有关更多信息以及单位缩写列表，请参阅如何在模块对话框中指定单位和单位定义。

#### 依赖关系

要启用此参数，请将 **Initial output source** 设置为 `Internal`。

## 所属库

Simscape / Foundation Library / Physical Signals / Linear Operators

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2022b：在事件时重置模块输出

该模块包含一个附加参数 **External reset**，用于在事件时重置输出信号。您可以指定当端口 **R** 处的物理信号触发重置时，模块输出重置为初始输出。此外，初始输出源现在可以是物理信号或模块参数。如果将 **Initial output source** 参数设置为 `External`，则端口 **Y0** 处的物理信号提供初始输出值，该值也是重置后的输出信号值。

### R2019a：单位传播

在 R2019a 之前，此模块不会传播物理单位。

如果您的模型包含没有单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关更多信息，请参阅 Upgrading Models with Legacy Physical Signal Blocks。

## 描述

对低通和超前-滞后滤波器建模

PS Transfer Function 模块允许您对一阶低通滤波器或超前-滞后滤波器建模。在 Simscape™ 网络中同时对被控对象和控制器建模可提高仿真效率。PS Transfer Function 模块允许您轻松地按所需配置参数化滤波器：

- `Lag` — 对一阶低通滤波器建模。您必须将滞后时间常数和初始输出作为模块参数提供。
- `Lead-lag` — 对超前-滞后滤波器建模。您必须将超前时间常数、滞后时间常数和初始输出作为模块参数提供。

模块图标根据 **Transfer function type** 参数的值而变化。

| 限制类型 | 模块图标 |
| --- | --- |
| `Lag` |  |
| `Lead-lag` |  |

无类型物理端口便于单位传播。输出信号具有与输入信号相同的物理单位。

您可以将初始模块输出指定为模块参数或附加输入信号：

- 要将初始条件定义为模块参数，请将 **Initial output source** 参数指定为 `Internal`，并在 **Initial output** 字段中输入值和单位。
- 要从外部源提供初始输出值，请将 **Initial output source** 参数指定为 `External`。一个附加物理信号输入端口 **Y0** 出现在模块图标顶部。将外部物理信号连接到端口 **Y0**。

### 重置状态

模块可以基于外部信号将其状态重置为指定的初始输出。默认情况下，**External reset** 参数设置为 `None`。要使模块重置其状态，请选择其他 **External reset** 选项之一：

- 选择 `Rising` 以在重置信号从负值或零上升到正值时重置状态。
- 选择 `Falling` 以在重置信号从正值下降到零或负值时重置状态。
- 选择 `Either` 以在重置信号从零变为非零、从非零变为零或改变符号时重置状态。

当您选择其中任一选项时，触发端口 **R** 出现在模块图标顶部。将重置物理信号连接到端口 **R**。

### 假设和限制

- 该模块假设低频增益为单位增益。要对非单位增益建模，请将 PS Gain 模块与 PS Transfer Function 模块串联连接。
