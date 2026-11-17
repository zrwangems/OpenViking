---
type: simulink-block
title: 'Solenoid'
family: 'electromechanical'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Mechatronic Actuators'
documentation_page: 'solenoid'
documentation_source_path: 'ref/solenoid.html'
language: zh-CN
chinese_source: worker-translation
---

# Solenoid

## 端口

### 守恒

### **+** — 正极端子 电气

与电磁阀正极端子相关联的电气守恒端口。

### **-** — 负极端子 电气

与电磁阀负极端子相关联的电气守恒端口。

### **C** — 壳体 机械

与壳体相关联的机械平移守恒端口。

### **R** — 柱塞 机械

与柱塞相关联的机械平移守恒端口。

### **H** — 热端口 thermal

热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认） | `Show thermal port`

是否启用模块的热端口并对将功率转换为热量的损耗效应进行建模。

### 磁力

### **Motion direction under excitation** — 激励下的运动方向 `Port R moves towards port C`（默认） | `Port R moves away from port C`

为激励下的运动方向类型选择以下选项之一：

- `Port R moves away from port
  C`
- `Port R moves towards port
  C`

### **Pull-in forces [F1 F2]** — 吸合力向量 `[7.5, .75]` `N`（默认）

力-行程曲线上两个点处的力值向量。第二个测量点处的行程必须大于第一个测量点处的行程。当制造商未提供力-行程曲线时，将 F1 设置为保持力（当 X1 = 0 时），并将 F2 设置为在 **Rated voltage Vdc** 和 **Rated current Idc** 值下运行电磁阀时的吸合力。

### **Stroke (air gap) [X1 X2]** — 行程向量 `[1, 5]` `mm`（默认）

力-行程曲线上两个点处的行程（柱塞距完全关闭位置的距离）值向量。第二个测量点处的行程必须大于第一个测量点处的行程。为确保力值为有限值，这些点必须满足条件

X2X1>F1F2

### **Rated voltage Vdc** — 额定电压 `50` `V`（默认）

电磁阀额定工作电压。此电压值用于测量 **Forces [F1 F2]** 和 **Stroke [X1 X2]** 值。

### **Rated current Idc** — 额定电流 `0.05` `A`（默认）

当电磁阀施加 **Rated voltage Vdc** 电压时流过的电流。

### 机械

### **Spring constant** — 弹簧常数 `200` `N/m`（默认）

表示弹簧刚度的常数，该弹簧用于在电磁阀断电时使柱塞回缩。当柱塞位移到 **Stroke for zero spring force** 参数值时，力为零。如果没有弹簧，将弹簧常数设置为零。

### **Stroke for zero spring force** — 零弹簧力行程 `5` `mm`（默认）

弹簧不提供作用力的行程。

### **Damping** — 阻尼 `1` `N/(m/s)`（默认）

柱塞运动方程中随位置变化的项 λ，它对柱塞运动进行线性阻尼。该值可以为零。

### **Plunger mass** — 柱塞质量 `0.05` `kg`（默认）

电磁阀柱塞的质量。该值可以为零。

### **Maximum stroke** — 最大行程 `Inf` `mm`（默认）

柱塞可位移的最大量。您可以使用此参数对限制行程的硬限位进行建模。默认值为 `Inf` mm，表示无行程限制。

### **Contact stiffness** — 接触刚度 `1e6` `N/m`（默认）

柱塞接触的刚度，用于对最小（*x* = 0）和最大（*x* = **Maximum stroke**）柱塞位置处的硬限位进行建模。

### **Contact damping** — 接触阻尼 `500` `N/(m/s)`（默认）

柱塞接触的阻尼，用于对最小（*x* = 0）和最大（*x* = **Maximum stroke**）柱塞位置处的硬限位进行建模。

### 热

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）

电阻温度系数。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

定义执行器参数所对应的温度。

### **Thermal mass** — 热质量 `100` `J/K`（默认）

热质量是使温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Mechatronic Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

电磁阀的电气特性和产生的力

Solenoid 模块表示下图中电磁阀的电气特性和产生的力：

正电流和负电流都会产生将柱塞拉向绕组的力。这会最小化磁阻并减小行程。要增大行程，弹簧或外力必须克服磁力。

复位弹簧是可选的。要从模型中移除该弹簧的影响，请将 **Spring constant** 参数设置为 `0`。

为显示电磁阀的作用方向，模块图标会根据 **Motion direction under excitation** 参数的值动态变化。

**注意**

如果在模块周围放置外部位置传感器，请注意传感器方向和初始位置条件。仅当您将传感器定向为与 **Motion direction under excitation** 参数的值一致的方向时，您在传感器上指定的初始位置条件才对应于 Solenoid 模块的 **Stroke, X** 变量。

| 当 **Motion direction under excitation** 参数设置为...时 | 模块图标 |
| --- | --- |
| `Port R moves away from port C` |  |
| `Port R moves towards port C` |  |

柱塞随位置 *x* 变化的运动方程为：

Fl+mx¨+λx˙+kx=Fe

其中 *Fe* 是电磁力，*Fl* 是负载力，*λ* 是粘性阻尼项，*m* 是柱塞质量。电磁力与电磁阀电流和电感的关系为：

Fe=12i2∂L(x)∂x

电感（在 [1] 中推导）可以写为：

∂L(x)∂x=−β(α+βx)2

其中 *α* 和 *β* 是常数。将上述方程代入电磁力方程，可得到电磁阀在电流 *i0* 下的力-行程关系：

F=12i02−β(α+βx)2

Solenoid 模块通过采用两个指定的力和行程测量值并将其代入上述方程来求解 *α* 和 *β*。它求解所得方程以得到 *α* 和 *β*。

从电气 **+** 到 **-** 端口的正电流会产生从机械 **C** 到 **R** 端口的负力（即拉力）。

### 热效应建模

您可以公开热端口，以对将功率转换为热量的损耗效应进行建模。要公开热端口，请将 **Modeling option** 参数设置为以下任一项：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含一个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值指定模型中变量的预期量级。基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

使用 **Stroke, X** 变量设置仿真开始时柱塞初始位置的目标。

**注意**

**Stroke, X** 变量是电磁阀的初始气隙或行程，因此应大于或等于 `0`。
