---
type: simulink-block
title: 'I-F Controller'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Controllers'
documentation_page: 'ifcontroller'
documentation_source_path: 'ref/ifcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# I-F Controller

## 端口
```yaml
ports:
- name: Enable
  summary: 启用模块算法的选项 标量
  direction: input
  data_types: single | double | fixed point
- name: θe
  summary: 电机电气位置 标量
  direction: input
  data_types: single | double | fixed point
- name: ωm ref
  summary: 参考电机机械转速 标量
  direction: input
  data_types: single | double | fixed point
- name: ωm
  summary: 电机机械转速 标量
  direction: input
  data_types: single | double | fixed point
- name: Iq
  summary: '*Q* 轴定子电流 标量'
  direction: input
  data_types: single | double | fixed point
- name: Vq
  summary: '*Q* 轴定子电压 标量'
  direction: input
  data_types: single | double | fixed point
- name: ParameterBus
  summary: I-F 控制器的计算参数 总线
  direction: input
  data_types: single | double
- name: Idref
  summary: 参考 *d* 轴电流 标量
  direction: output
  data_types: single | double | fixed point
- name: Iqref
  summary: 参考 *q* 轴电流 标量
  direction: output
  data_types: single | double | fixed point
- name: θeref
  summary: 生成的电机参考电气位置 标量
  direction: output
  data_types: single | double | fixed point
- name: Status
  summary: I-F 控制状态 标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **Enable** — 启用模块算法的选项 标量

启用模块算法的信号：

- `1` — 启用模块算法。
- `0` — 复位模块算法。

**数据类型：** `single` | `double` | `fixed point`

### **θe** — 电机电气位置 标量

转子的电气位置。

**数据类型：** `single` | `double` | `fixed point`

### **ωm ref** — 参考电机机械转速 标量

使用 I-F 控制运行电机时的参考机械转速。

**数据类型：** `single` | `double` | `fixed point`

### **ωm** — 电机机械转速 标量

电机的实际机械转速。

**数据类型：** `single` | `double` | `fixed point`

### **Iq** — *Q* 轴定子电流 标量

沿旋转 *dq* 参考坐标系 *q* 轴的定子电流。

**数据类型：** `single` | `double` | `fixed point`

### **Vq** — *Q* 轴定子电压 标量

沿旋转 *dq* 参考坐标系 *q* 轴的定子电压。

**数据类型：** `single` | `double` | `fixed point`

### **ParameterBus** — I-F 控制器的计算参数 总线

I-F Controller 模块的计算参数。该输入端口接受以下参数：

- **Number of pole pairs**
- **Speed to exit I-F controller (RPM), ω1**
- **Speed to re-enter I-F controller (RPM), ω2**
- **Maximum current (A), Imax**
- **Maximum rate of speed change (RPM/s)**
- **Maximum current decay rate (A/s)**
- **Idle time (s)**
- **Damping coefficient, ζ**

将此端口与 Compute Parameter 模块配合使用，可在运行时以最优方式更新上述模块参数。

#### 依赖关系

要启用此端口，请选择 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

**数据类型：** `single` | `double`
### 输出

### **Idref** — 参考 *d* 轴电流 标量

参考 *d* 轴定子电流，用于产生驱动电机的电流。

**数据类型：** `single` | `double` | `fixed point`

### **Iqref** — 参考 *q* 轴电流 标量

参考 *q* 轴定子电流，用于产生驱动电机的电流。

**数据类型：** `single` | `double` | `fixed point`

### **θeref** — 生成的电机参考电气位置 标量

由驱动电机的模块生成的电机参考电气位置。

**数据类型：** `single` | `double` | `fixed point`

### **Status** — I-F 控制状态 标量

I-F 控制算法的状态。

- `1` — 表示 I-F 控制未激活。
- `0` — 表示 I-F 控制已激活。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Enable speed damping
  summary: 启用模块以应用速度振荡阻尼补偿的选项 off（默认）| on
  group: ''
- name: Use input port for computed parameters (run-time motor swap)
  summary: 启用输入端口以接受计算参数的选项 off（默认）| on
  group: ''
- name: Number of pole pairs
  summary: 电机中可用的极对数 4（默认）| 标量
  group: ''
- name: 位置单位
  summary: 电位置单位 Degrees（默认）| Radians | Per-unit
  group: ''
- name: 速度单位
  summary: 速度输入的单位 Degrees/Sec（默认）| Radians/Sec | RPM | Per-unit
  group: ''
- name: 标幺速度（RPM）
  summary: 一个标幺值对应的速度 6000（默认）| 标量
  group: ''
- name: 电流单位
  summary: 电机电流的单位 SI unit（默认）| Per-unit
  group: ''
- name: 基准电流（A）
  summary: 一个标幺值对应的额定电流 21.4286（默认）| 标量
  group: ''
- name: 离散步长（s）
  summary: 连续模块执行之间的间隔 50e-6（默认）| 标量
  group: ''
- name: 退出 I-F 控制器的速度（RPM），ω1
  summary: I-F 控制停止时的速度（电机启动后） 410.7（默认）| 标量
  group: 控制器参数
- name: 重新进入 I-F 控制器的速度（RPM），ω2
  summary: 重新进入 I-F 控制所需的速度 287.49（默认）| 标量
  group: 控制器参数
- name: 最大电流（A），Imax
  summary: I-F 控制期间的最大电机电流 6.39（默认）| 标量
  group: 控制器参数
- name: 最大速度变化率（RPM/s）
  summary: I-F 控制期间的最大速度变化率 960（默认）| 标量
  group: 控制器参数
- name: Maximum current decay rate (A/s)
  summary: I-F 控制期间的最大电流衰减率 111.8250（默认）| 标量
  group: 控制器参数
- name: Idle time (s)
  summary: 恒定速度和电流的时间 1（默认）| 标量
  group: 控制器参数
- name: Minimum allowed position error for transition (rad)
  summary: 闭环切换的阈值误差 0.1745（默认）| 标量
  group: 控制器参数
- name: Voltage unit
  summary: 定子电压的单位 SI unit（默认）| Per-unit
  group: Advanced Parameters
- name: Base voltage (V)
  summary: 对应一个标幺值的标称电压 13.8564（默认）| 标量
  group: Advanced Parameters
- name: Damping coefficient, ζ
  summary: 速度振荡阻尼系数值 2.6172（默认）| 标量
  group: Advanced Parameters
```

### **Enable speed damping** — 启用模块以应用速度振荡阻尼补偿的选项 `off`（默认）| on

选择此参数可对存在速度振荡的电机电气速度（根据假定的电机位置）应用速度振荡阻尼。

### **Use input port for computed parameters (run-time motor swap)** — 启用输入端口以接受计算参数的选项 `off`（默认）| on

选择此参数可启用 **ParameterBus** 输入端口并禁用以下参数：

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

此参数使您能够将输入端口与 Compute Parameter 模块配合使用，以便在运行时以最优方式更新模块参数。

### **Number of pole pairs** — 电机中可用的极对数 `4`（默认）| 标量

电机中可用的极对数。

#### 依赖关系

要启用此参数，请清除 **高级选项** 部分中提供的 **使用输入端口计算参数（运行时电机切换）** 参数。

### **位置单位** — 电位置单位 `Degrees`（默认）| `Radians` | `Per-unit`

模块使用的 **θe** 输入和 **θeref** 输出的单位。

选择 `Per-unit` 以对参考电位置输入和输出使用标幺制。有关标幺制的更多信息，请参阅标幺制。

### **速度单位** — 速度输入的单位 `Degrees/Sec`（默认）| `Radians/Sec` | `RPM` | `Per-unit`

**ωmref** 和 **ωm** 输入的单位。

选择 `Per-unit` 以对两个速度输入使用标幺制。有关标幺制的更多信息，请参阅标幺制。

### **标幺速度（RPM）** — 一个标幺值对应的速度 `6000`（默认）| 标量

一个标幺值对应的速度值。有关详细信息，请参阅标幺制。

#### 依赖关系

要启用此参数，请将 **速度单位** 设置为 `Per-unit`。

### **电流单位** — 电机电流的单位 `SI unit`（默认）| `Per-unit`

模块的 **Iq** 输入以及 **Idref** 和 **Iqref** 输出的单位。

选择 `Per-unit` 以对这些电机电流使用标幺制。有关标幺制的更多信息，请参阅标幺制。

#### 依赖关系

要启用此参数，请清除 **高级选项** 部分中提供的 **使用输入端口计算参数（运行时电机切换）** 参数。

### **基准电流（A）** — 一个标幺值对应的额定电流 `21.4286`（默认）| 标量

一个标幺值对应的额定电流值。有关详细信息，请参阅标幺制。

#### 依赖关系

要启用此参数：

- 清除 **高级选项** 部分中提供的 **使用输入端口计算参数（运行时电机切换）** 参数。
- 将 **电流单位** 设置为 `Per-unit`。

### **离散步长（s）** — 连续模块执行之间的间隔 `50e-6`（默认）| 标量

两次连续模块执行实例之间的固定时间间隔，以秒为单位。

### 控制器参数

### **退出 I-F 控制器的速度（RPM），ω1** — I-F 控制停止时的速度（电机启动后） `410.7`（默认）| 标量

I-F 控制器保持激活状态的速度（电机启动后）（以 RPM 为单位）。当电机速度超过此值时，I-F 控制器变为非激活状态，**Status** 模块输出变为 true。

#### 依赖关系

要启用此参数，请清除 **高级选项** 部分中提供的 **使用输入端口计算参数（运行时电机切换）** 参数。

### **重新进入 I-F 控制器的速度（RPM），ω2** — 重新进入 I-F 控制所需的速度 `287.49`（默认）| 标量

退出 I-F 控制（并进入闭环控制）后，重新激活 I-F 控制器所需的速度（以 RPM 为单位）。当电机速度降至该值以下时，I-F 控制器再次变为激活状态，**Status** 模块输出变为 false。

#### 依赖关系

要启用此参数，请清除 **高级选项** 部分中提供的 **使用输入端口计算参数（运行时电机切换）** 参数。

### **最大电流（A），Imax** — I-F 控制期间的最大电机电流 `6.39`（默认）| 标量

I-F 控制激活时提供给电机的最大电流（以安培为单位）。

#### 依赖关系

要启用此参数，请清除 **高级选项** 部分中提供的 **使用输入端口计算参数（运行时电机切换）** 参数。

### **最大速度变化率（RPM/s）** — I-F 控制期间的最大速度变化率 `960`（默认）| 标量

I-F 控制激活时电机速度可以变化的最大速率（以 RPM/s 为单位）。

#### 依赖关系

要启用此参数，请清除 **高级选项** 部分中提供的 **使用输入端口计算参数（运行时电机切换）** 参数。

### **Maximum current decay rate (A/s)** — I-F 控制期间的最大电流衰减率 `111.8250`（默认）| 标量

当 I-F 控制激活时，电机电流可以衰减的最大速率（单位：安培/秒）。

#### 依赖

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Idle time (s)** — 恒定速度和电流的时间 `1`（默认）| 标量

当 I-F 控制激活时，电机速度和电流均保持恒定的时间（单位：秒）。

#### 依赖

要启用此参数，请清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Minimum allowed position error for transition (rad)** — 闭环切换的阈值误差 `0.1745`（默认）| 标量

阈值电角度位置误差（介于 **θe** 和 **θeref** 之间），低于该值时模块从 I-F 控制切换到闭环控制。

### Advanced Parameters

要启用此选项卡，请选择 **Enable speed damping** 参数。

### **Voltage unit** — 定子电压的单位 `SI unit`（默认）| `Per-unit`

*Vα* 和 *Vβ* 定子电压的单位。

选择 `Per-unit` 以对这些电压使用标幺制。有关标幺制的更多信息，请参阅 Per-Unit System。

#### 依赖

要启用此参数：

- 选择 **Enable speed damping** 参数。
- 清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。

### **Base voltage (V)** — 对应一个标幺值的标称电压 `13.8564`（默认）| 标量

对应一个标幺值的标称电压值。有关标幺制的详细信息，请参阅 Per-Unit System。

#### 依赖

要启用此参数：

- 选择 **Enable speed damping** 参数。
- 清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。
- 将 **Voltage unit** 设置为 `Per-unit`。

### **Damping coefficient, ζ** — 速度振荡阻尼系数值 `2.6172`（默认）| 标量

模块应使用的速度振荡阻尼系数（*K*）的值。

#### 依赖

要启用此参数：

- 选择 **Enable speed damping** 参数。
- 清除 **Advanced Options** 部分中提供的 **Use input port for computed parameters (run-time motor swap)** 参数。
## 所属库

Motor Control Blockset / Controls / Controllers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2024a 中引入**

## 描述

实现三相永磁同步电机的 I-F 控制

I-F Controller 模块为三相永磁同步电机（PMSM）实现基于 I-F 控制的无传感器启动算法。

与 VbyF Controller 模块类似，I-F Controller 模块可实现无传感器电机启动，但 I-F Controller 会在电机中产生更高的启动转矩。

该模块计算 PMSM 的 *d* 轴和 *q* 轴参考电流以及参考电位置。它接受电位置、*q* 轴电流以及参考和实际机械转速作为输入。

该模块同时支持 SI 单位制和标幺（PU）制。有关标幺制的更多信息，请参阅 Per-Unit System。

此外，您可以使用高级选项启用 **ParameterBus** 输入端口，您可以将其与 Compute Parameter 模块一起使用，以在运行时最优地更新模块参数。当电机参数可能随时间变化时，例如在构建可能需要在运行时更换电机的应用时，您可以使用此功能。

有关该模块算法的信息，请参阅 Algorithm。
