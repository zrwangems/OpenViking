---
type: simulink-block
title: 'I-F Controller'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Controls / Controllers'
documentation_page: 'ifcontroller'
documentation_source_path: 'ref/ifcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# I-F Controller

## 端口

### 输入

### **Enable** — 启用模块算法的选项 scalar

用于启用模块算法的信号：

- `1` — 启用模块算法。
- `0` — 重置模块算法。

**数据类型：** `single` | `double` | `fixed point`

### **θe** — 电机的电位置 scalar

转子的电位置。

**数据类型：** `single` | `double` | `fixed point`

### **ωm ref** — 参考电机机械速度 scalar

使用 I-F 控制运行电机时的参考机械速度。

**数据类型：** `single` | `double` | `fixed point`

### **ωm** — 电机机械速度 scalar

电机的实际机械速度。

**数据类型：** `single` | `double` | `fixed point`

### **Iq** — *q* 轴定子电流 scalar

沿旋转 *dq* 参考系的 *q* 轴的定子电流。

**数据类型：** `single` | `double` | `fixed point`

### **Vq** — *q* 轴定子电压 scalar

沿旋转 *dq* 参考系的 *q* 轴的定子电压。

**数据类型：** `single` | `double` | `fixed point`

### **ParameterBus** — I-F 控制器 bus 的计算参数

I-F Controller 模块的计算参数。此输入端口接受以下参数：

- **Number of pole pairs**
- **Speed to exit I-F controller (RPM), ω1**
- **Speed to re-enter I-F controller (RPM), ω2**
- **Maximum current (A), Imax**
- **Maximum rate of speed change (RPM/s)**
- **Maximum current decay rate (A/s)**
- **Idle time (s)**
- **Damping coefficient, ζ**

将此端口与 Compute Parameter 模块一起使用，以在运行时最优地更新上述模块参数。

#### 依赖关系

要启用此端口，请选择 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

**数据类型：** `single` | `double`

### 输出

### **Idref** — 参考 *d* 轴电流 scalar

产生驱动电机电流的参考 *d* 轴定子电流。

**数据类型：** `single` | `double` | `fixed point`

### **Iqref** — 参考 *q* 轴电流 scalar

产生驱动电机电流的参考 *q* 轴定子电流。

**数据类型：** `single` | `double` | `fixed point`

### **θeref** — 生成的电机参考电位置 scalar

由驱动电机的模块生成的电机参考电位置。

**数据类型：** `single` | `double` | `fixed point`

### **Status** — I-F 控制状态 scalar

I-F 控制算法的状态。

- `1` — 指示 I-F 控制未激活。
- `0` — 指示 I-F 控制已激活。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Enable speed damping** — 用于使模块应用速度振荡阻尼补偿的选项 `off` (默认) | on

选择此参数，以根据假定电机位置对具有速度振荡的电机电速度应用速度振荡阻尼。

### **Use input port for computed parameters (run-time motor swap)** — 用于启用输入端口以接受计算参数的选项 `off` (默认) | on

选择此参数以启用 **ParameterBus** 输入端口，并禁用以下参数：

- **Number of pole pairs**
- **Current unit**
- **Base current (A)**
- **Speed to exit I-F controller (RPM), ω1**
- **Speed to re-enter I-F controller (RPM), ω2**
- **Maximum current (A), Imax**
- **Maximum rate of speed change (RPM/s)**
- **Maximum current decay rate (A/s)**
- **Idle time (s)**
- **Voltage unit**
- **Base voltage (V)**
- **Damping coefficient, ζ**

此参数使您可以将输入端口与 Compute Parameter 模块一起使用，以在运行时最优地更新模块参数。

### **Number of pole pairs** — 电机中可用的极对数 `4` (默认) | scalar

电机中可用的极对数。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Position unit** — 电位置的单位 `Degrees` (默认) | `Radians` | `Per-unit`

该模块使用的 **θe** 输入和 **θeref** 输出的单位。

选择 `Per-unit` 以对参考电位置输入和输出使用 per-unit 系统。有关 per-unit 系统的详细信息，请参阅 Per-Unit System。

### **Speed unit** — 速度输入的单位 `Degrees/Sec` (默认) | `Radians/Sec` | `RPM` | `Per-unit`

**ωmref** 和 **ωm** 输入的单位。

选择 `Per-unit` 以对这两个速度输入使用 per-unit 系统。有关 per-unit 系统的详细信息，请参阅 Per-Unit System。

### **Per unit speed (RPM)** — 一个 per-unit 对应的速度 `6000` (默认) | scalar

一个 per-unit 对应的速度值。有关详细信息，请参阅 Per-Unit System。

#### 依赖关系

要启用此参数，请将 **Speed unit** 设置为 `Per-unit`。

### **Current unit** — 电机电流的单位 `SI unit` (默认) | `Per-unit`

**Iq** 输入以及该模块的 **Idref** 和 **Iqref** 输出的单位。

选择 `Per-unit` 以对这些电机电流使用 per-unit 系统。有关 per-unit 系统的详细信息，请参阅 Per-Unit System。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Base current (A)** — 一个 per-unit 对应的标称电流 `21.4286` (默认) | scalar

一个 per-unit 对应的标称电流值。有关详细信息，请参阅 Per-Unit System。

#### 依赖关系

要启用此参数：

- 清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。
- 将 **Current unit** 设置为 `Per-unit`。

### **Discrete step size (s)** — 连续模块执行之间的间隔 `50e-6` (默认) | scalar

两次连续模块执行实例之间的固定时间间隔（以秒为单位）。

### 控制器参数

### **Speed to exit I-F controller (RPM), ω1** — 电机启动后 I-F 控制停止时的速度 `410.7` (默认) | scalar

电机启动后，I-F 控制器保持活动状态的速度（以 RPM 为单位）。当电机速度超过此值时，I-F 控制器变为非活动状态，并且 **Status** 模块输出变为 true。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Speed to re-enter I-F controller (RPM), ω2** — 重新进入 I-F 控制所需的速度 `287.49` (默认) | scalar

在退出 I-F 控制（并进入闭环控制）后，重新激活 I-F 控制器所需的速度（以 RPM 为单位）。当电机速度降至该值以下时，I-F 控制器再次变为活动状态，并且 **Status** 模块输出变为 false。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Maximum current (A), Imax** — I-F 控制期间的最大电机电流 `6.39` (默认) | scalar

I-F 控制激活时提供给电机的最大电流（以安培为单位）。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Maximum rate of speed change (RPM/s)** — I-F 控制期间的最大速度变化率 `960` (默认) | scalar

I-F 控制激活时电机速度可变化的最大速率（以 RPM/s 为单位）。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Maximum current decay rate (A/s)** — I-F 控制期间的最大电流衰减率 `111.8250` (默认) | scalar

I-F 控制激活时电机电流可衰减的最大速率（以安培/秒为单位）。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Idle time (s)** — 恒定速度和电流的时间 `1` (默认) | scalar

I-F 控制激活时电机速度和电流均保持恒定的时间（以秒为单位）。

#### 依赖关系

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Minimum allowed position error for transition (rad)** — 闭环转换的阈值误差 `0.1745` (默认) | scalar

阈值电位置误差（介于 **θe** 和 **θeref** 之间），低于该误差时模块从 I-F 控制转换为闭环控制。

### 高级参数

要启用此选项卡，请选择 **Enable speed damping** 参数。

### **Voltage unit** — 定子电压的单位 `SI unit` (默认) | `Per-unit`

*Vα* 和 *Vβ* 定子电压的单位。

选择 `Per-unit` 以对这些电压使用 per-unit 系统。有关 per-unit 系统的详细信息，请参阅 Per-Unit System。

#### 依赖关系

要启用此参数：

- 选择 **Enable speed damping** 参数。
- 清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Base voltage (V)** — 一个 per-unit 对应的标称电压 `13.8564` (默认) | scalar

一个 per-unit 对应的标称电压值。有关 per-unit 系统的详细信息，请参阅 Per-Unit System。

#### 依赖关系

要启用此参数：

- 选择 **Enable speed damping** 参数。
- 清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。
- 将 **Voltage unit** 设置为 `Per-unit`。

### **Damping coefficient, ζ** — 速度振荡阻尼系数值 `2.6172` (默认) | scalar

模块应使用的速度振荡阻尼系数 (*K*) 的值。

#### 依赖关系

要启用此参数：

- 选择 **Enable speed damping** 参数。
- 清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

## 所属库

Motor Control Blockset / Controls / Controllers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2024a 中引入**

## 描述

为三相永磁同步电机实现 I-F 控制

I-F Controller 模块为三相永磁同步电机 (PMSM) 实现基于 I-F 控制的无传感器启动算法。

与 VbyF Controller 模块类似，I-F Controller 模块可实现无传感器电机启动，但 I-F Controller 在电机中产生更高的启动转矩。

该模块为 PMSM 计算 *d* 轴和 *q* 轴参考电流以及参考电位置。它接受电位置、*q* 轴电流以及参考和实际机械速度作为输入。

该模块同时支持 SI unit 和 per-unit (PU) 系统。有关 per-unit 系统的详细信息，请参阅 Per-Unit System。

此外，您可以使用高级选项启用 **ParameterBus** 输入端口，并将其与 Compute Parameter 模块一起使用，以在运行时最优地更新模块参数。当电机参数可能随时间变化时（例如，在构建可能需要在运行时切换电机的应用时），您可以使用此功能。

有关模块算法的信息，请参阅算法。
