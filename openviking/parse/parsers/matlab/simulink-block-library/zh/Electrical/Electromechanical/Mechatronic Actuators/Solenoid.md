---
type: simulink-block
title: 'Solenoid'
family: 'sps'
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
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
- name: C
  summary: 壳体机械
  direction: conserving
- name: R
  summary: 柱塞机械
  direction: conserving
- name: H
  summary: 热端口热
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与电磁阀正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电磁阀负极端子关联的电气守恒端口。

### **C** — 壳体机械

与壳体关联的机械平移守恒端口。

### **R** — 柱塞机械

与柱塞关联的机械平移守恒端口。

### **H** — 热端口热

热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否启用热端口 No thermal port（默认）| Show thermal port
  group: ''
- name: Motion direction under excitation
  summary: 激励下的运动方向 Port R moves towards port C（默认）| Port R moves away from port C
  group: 磁力
- name: Pull-in forces [F1 F2]
  summary: 吸合力向量 [7.5, .75] N（默认）
  group: 磁力
- name: Stroke (air gap) [X1 X2]
  summary: 行程向量 [1, 5] mm（默认）
  group: 磁力
- name: Rated voltage Vdc
  summary: 额定电压 50 V（默认）
  group: 磁力
- name: Rated current Idc
  summary: 额定电流 0.05 A（默认）
  group: 磁力
- name: Spring constant
  summary: 弹簧刚度 200 N/m（默认）
  group: 机械
- name: Stroke for zero spring force
  summary: 零弹簧力时的行程 5 mm（默认）
  group: 机械
- name: Damping
  summary: 阻尼 1 N/(m/s)（默认）
  group: 机械
- name: Plunger mass
  summary: 柱塞质量 0.05 kg（默认）
  group: 机械
- name: Maximum stroke
  summary: 最大行程 Inf mm（默认）
  group: 机械
- name: Contact stiffness
  summary: 接触刚度 1e6 N/m（默认）
  group: 机械
- name: Contact damping
  summary: 接触阻尼 500 N/(m/s)（默认）
  group: 机械
- name: Resistance temperature coefficient
  summary: 电阻温度系数 3.93e-3 1/K（默认）
  group: 热
- name: Measurement temperature
  summary: 测量温度 25 degC（默认）
  group: 热
- name: Thermal mass
  summary: 热质量 100 J/K（默认）
  group: 热
```

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对将功率转化为热量的损耗效应进行建模。

### 磁力

### **Motion direction under excitation** — 激励下的运动方向 `Port R moves towards port C`（默认）| `Port R moves away from port C`

从以下激励下的运动方向类型选项中选择一项：

- `端口 R 远离端口
  C`
- `Port R moves towards port
  C`

### **Pull-in forces [F1 F2]** — 吸合力向量 `[7.5, .75]` `N`（默认）

力-行程曲线上两个点处的力值向量。第二个测量点的行程必须大于第一个测量点的行程。当制造商未提供力-行程曲线时，将 F1 设置为保持力（当 X1 = 0 时），将 F2 设置为在 **Rated voltage Vdc** 和 **Rated current
Idc** 值下运行电磁阀时的吸合力。

### **Stroke (air gap) [X1 X2]** — 行程向量 `[1, 5]` `mm`（默认）

力-行程曲线上两个点处的行程（柱塞距完全闭合位置的距离）值向量。第二个测量点的行程必须大于第一个测量点的行程。为确保力值有限，这些点必须满足以下条件

X2X1>F1F2

### **Rated voltage Vdc** — 额定电压 `50` `V`（默认）

电磁阀额定工作电压。此电压值用于测量 **Forces [F1 F2]** 和
**Stroke [X1 X2]** 值。

### **Rated current Idc** — 额定电流 `0.05` `A`（默认）

当电磁阀施加 **Rated voltage Vdc** 电压时流过的电流。

### 机械

### **Spring constant** — 弹簧刚度 `200` `N/m`（默认）

表示弹簧刚度的常数，该弹簧在电磁阀断电时使柱塞回位。当柱塞位移到 **Stroke for zero spring
force** 参数值时，力为零。如果没有弹簧，请将弹簧刚度设置为零。

### **Stroke for zero spring force** — 零弹簧力时的行程 `5` `mm`（默认）

弹簧不提供力时的行程。

### **Damping** — 阻尼 `1` `N/(m/s)`（默认）

柱塞运动方程中作为位置函数的项 λ，对柱塞运动进行线性阻尼。该值可以为零。

### **Plunger mass** — 柱塞质量 `0.05` `kg`（默认）

电磁阀柱塞的重量。该值可以为零。

### **Maximum stroke** — 最大行程 `Inf` `mm`（默认）

柱塞可以位移的最大量。您可以使用此参数来建模限制行程的硬限位。默认值为 `Inf` mm，表示无行程限制。

### **Contact stiffness** — 接触刚度 `1e6` `N/m`（默认）

柱塞接触的刚度，用于建模最小（*x* = 0）和最大（*x* =
**Maximum stroke**）柱塞位置处的硬限位。

### **Contact damping** — 接触阻尼 `500` `N/(m/s)`（默认）

柱塞接触的阻尼，用于建模最小（*x* = 0）和最大（*x* =
**Maximum stroke**）柱塞位置处的硬限位。

### 热

要启用这些参数，请将 **Modeling option** 设置为
`Show thermal port`。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）

电阻温度系数。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

执行器参数定义所对应的温度。

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

正电流和负电流都会产生将柱塞拉向绕组的力。这使磁阻最小化并减小行程。要增加行程，弹簧或外力必须克服磁力。

复位弹簧是可选的。要从模型中移除该弹簧的效应，请将 **Spring constant** 参数设置为 `0`。

为了显示电磁阀的作用方向，模块图标会根据 **Motion direction under excitation** 参数的值动态变化。

**注意**

如果您在模块周围放置外部位置传感器，请注意传感器方向和初始位置条件。您在传感器上指定的初始位置条件仅在您将传感器定向为与 **Motion direction under excitation** 参数值一致的方向时，才对应于 Solenoid 模块的 **Stroke,
X** 变量。

| 当 **Motion direction under excitation** 参数设置为... | 模块图标 |
| --- | --- |
| `Port R moves away from port C` |  |
| `Port R moves towards port C` |  |

柱塞作为位置 *x* 函数的运动方程为：

Fl+mx¨+λx˙+kx=Fe

其中 *Fe* 是电磁力，*Fl* 是负载力，*λ* 是粘性阻尼项，*m* 是柱塞质量。电磁力与电磁阀电流和电感的关系为：

Fe=12i2∂L(x)∂x

电感在 [1] 中推导得出，可以写为：

∂L(x)∂x=−β(α+βx)2

其中 *α* 和 *β* 是常数。将上述方程代入电磁力方程，得到电磁阀在电流 *i0* 下的力-行程关系：

F=12i02−β(α+βx)2

Solenoid 模块通过取两个指定的力和行程测量值并将其代入上述方程来求解 *α* 和 *β*。它求解所得方程以得到 *α* 和 *β*。

从电气 **+** 端口到 **-** 端口的正电流产生从机械 **C** 端口到 **R** 端口的负力（即拉力）。

### 热效应建模

您可以暴露热端口来对将功率转化为热量的损耗效应进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含一个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期量级。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或属性检查器中的 **Nominal
Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

使用 **Stroke, X** 变量来设置仿真开始时柱塞初始位置的目标。

**注意**

**Stroke, X** 变量是电磁阀的初始气隙或行程，因此应大于或等于
`0`。
