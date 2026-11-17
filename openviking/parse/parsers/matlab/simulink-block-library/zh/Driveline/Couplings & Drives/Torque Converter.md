---
type: simulink-block
title: 'Torque Converter'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'torqueconverter'
documentation_source_path: 'ref/torqueconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Torque Converter

## 端口
```yaml
ports:
- name: I
  summary: 泵轮机械旋转
  direction: conserving
- name: T
  summary: 涡轮机械旋转
  direction: conserving
```

### 守恒端口

### **I** — 泵轮机械旋转

与泵轮关联的机械旋转守恒端口。

### **T** — 涡轮机械旋转

与涡轮关联的机械旋转守恒端口。
## 参数
```yaml
parameters:
- name: Coast mode modeling
  summary: 滑行过渡仿真选项 Two-mode（默认）| Continuous
  group: 扭矩特性
- name: Drive mode speed ratio vector
  summary: 涡轮转速与泵轮转速之比 [0, .5, .6, .7, .8, .87, .92, .94, .96, .97, 1]（默认）| 向量
  group: 扭矩特性
- name: Drive mode torque ratio vector
  summary: 涡轮扭矩与泵轮扭矩之比 [2.232, 1.5462, 1.4058, 1.2746, 1.1528, 1.0732, 1.0192, 1, 1, 1, 1]（默认）| 向量
  group: 扭矩特性
- name: Drive mode capacity factor vector
  summary: 驱动模式的容量系数 1e-4 * [.72558, .66322, .63463, .59042, .51331, .4144, .29287, .22444, .12186, .04386, 0] m*N/rpm^2（默认）|
    向量
  group: 扭矩特性
- name: Coast mode speed ratio vector
  summary: 泵轮转速与涡轮转速之比 [0, .5, .6, .7, .8, .87, .92, .94, .96, .97, 1]（默认）| 向量
  group: 扭矩特性
- name: Coast mode capacity factor vector
  summary: 滑行模式的容量系数 1e-4 * [.5079, .4643, .4442, .4133, .3593, .2901, .205, .1571, .0853, .0307, 0] m*N/rpm^2（默认）| 向量
  group: 扭矩特性
- name: Initial mode
  summary: 仿真的初始模式 Drive mode（默认）| Coast mode
  group: 扭矩特性
- name: Mode transition threshold
  summary: 模式过渡阈值 1 rpm（默认）| 正标量
  group: 扭矩特性
- name: Speed ratio vector
  summary: 涡轮转速与泵轮转速之比 [0, .5, .6, .7, .8, .87, .92, .94, .96, .97]（默认）| 升序非负元素向量
  group: 扭矩特性
- name: Torque ratio vector
  summary: 涡轮扭矩与泵轮扭矩之比 [2.232, 1.5462, 1.4058, 1.2746, 1.1528, 1.0732, 1.0192, .9983, .9983, .9983, .9983]（默认）| 升序正元素向量
  group: 扭矩特性
- name: Capacity factor parameterization
  summary: 容量系数定义 Ratio of speed to square root of impeller torque（默认）| Ratio of impeller torque to square of speed
  group: 扭矩特性
- name: Capacity factor reference speed
  summary: 容量系数参考转速选项 Always impeller speed（默认）| Turbine speed for speed ratios greater than one
  group: 扭矩特性
- name: Capacity factor vector
  summary: 容量系数 [12.2938, 12.8588, 13.1452, 13.6285, 14.6163, 16.2675, 19.3503, 22.1046, 29.9986, 50] rad/(N^(1/2)*m^(1/2)*s)（默认）|
    向量
  group: 扭矩特性
- name: Model transmission lag
  summary: 传动滞后设置 No lag – Suitable for HIL simulation（默认）| Specify time constant and initial value
  group: 动力学
- name: Torque transmission time constant
  summary: 扭矩传递时间常数 .02 s（默认）| 正标量
  group: 动力学
- name: Initial turbine-to-impeller torque ratio
  summary: 涡轮与泵轮的初始扭矩比 0（默认）| 非负标量
  group: 动力学
- name: Interpolation method
  summary: 查找函数的插值方法 Linear（默认）| Smooth
  group: 动力学
- name: Extrapolation method
  summary: 查找函数的外推方法 Linear（默认）| Nearest | Error
  group: 动力学
```

### 扭矩特性

### **Coast mode modeling** — 滑行过渡仿真选项 `Two-mode`（默认）| `Continuous`

滑行模式过渡方法。当您选择 `Continuous` 时，模块在驱动模式和滑行模式之间平滑过渡，但在过渡附近建模时精度和鲁棒性会降低。当您选择 `Two-mode` 时，模块使用模式图，在模式过渡时可提供更好的鲁棒性和精度。

### **Drive mode speed ratio vector** — 涡轮转速与泵轮转速之比 `[0, .5, .6, .7, .8, .87, .92, .94, .96, .97, 1]`（默认）| 向量

驱动模式的速比 Rω。向量元素必须按升序排列，从 0 开始，到 1 结束。

Rω=ωT/ωI

#### 依赖关系

要启用此参数，请将 **Coast mode modeling** 设置为 `Two-mode`。

### **Drive mode torque ratio vector** — 涡轮扭矩与泵轮扭矩之比 `[2.232, 1.5462, 1.4058, 1.2746, 1.1528, 1.0732, 1.0192, 1, 1, 1, 1]`（默认）| 向量

驱动模式的扭矩比 Rτ。向量的每个元素必须大于或等于 1，且最后一个元素必须为 1。模块将驱动模式的扭矩比定义为：

Rτ=τT/τI

#### 依赖关系

要启用此参数，请将 **Coast mode modeling** 设置为 `Two-mode`。

### **Drive mode capacity factor vector** — 驱动模式的容量系数 `1e-4 * [.72558, .66322, .63463, .59042, .51331, .4144, .29287, .22444, .12186, .04386, 0]` `m*N/rpm^2`（默认）| 向量

驱动模式的容量系数 K\*。向量的每个元素必须为非负值，且最后一个元素必须为 0。模块将驱动模式的容量系数定义为：

K\*=τI/ωI2

#### 依赖关系

要启用此参数，请将 **Coast mode modeling** 设置为 `Two-mode`。

### **Coast mode speed ratio vector** — 泵轮转速与涡轮转速之比 `[0, .5, .6, .7, .8, .87, .92, .94, .96, .97, 1]`（默认）| 向量

滑行模式的速比 R^ω。向量元素必须按升序排列，从 0 开始，到 1 结束。模块将滑行模式的速比定义为：

R^ω=ωI/ωT

#### 依赖关系

要启用此参数，请将 **Coast mode modeling** 设置为 `Two-mode`。

### **Coast mode capacity factor vector** — 滑行模式的容量系数 `1e-4 * [.5079, .4643, .4442, .4133, .3593, .2901, .205, .1571, .0853, .0307, 0]` `m*N/rpm^2`（默认）| 向量

滑行模式的容量系数 K^\*。向量的每个元素必须为非负值，且最后一个元素必须为 0。模块将滑行模式的容量系数定义为：

K^\*=τT/ωT2

#### 依赖关系

要启用此参数，请将 **Coast mode modeling** 设置为 `Two-mode`。

### **Initial mode** — 仿真的初始模式 `Drive mode`（默认）| `Coast mode`

仿真的初始模式，指定为 `Drive mode` 或 `Coast mode`。

#### 依赖关系

要启用此参数，请将 **Coast mode modeling** 设置为 `Two-mode`。

### **Mode transition threshold** — 模式过渡阈值 `1` `rpm`（默认）| 正标量

仿真的模式过渡阈值。设置模式过渡阈值可以通过避免高频模式切换来提高仿真鲁棒性。

#### 依赖关系

要启用此参数，请将 **Coast mode modeling** 设置为 `Two-mode`。

### **Speed ratio vector** — 涡轮转速与泵轮转速之比 `[0, .5, .6, .7, .8, .87, .92, .94, .96, .97]`（默认）| 升序非负元素向量

液力变矩器的速比 Rω。向量的每个元素必须按升序排列且为非负值。模块将速比定义为 Rω=ωT/ωI。如果 *Rω* 超过最后一个元素，模块将根据 **Extrapolation method** 参数进行外推。

#### 依赖关系

要启用此参数，请将 **Coast mode modeling** 设置为 `Continuous`。

### **Torque ratio vector** — 涡轮扭矩与泵轮扭矩之比 `[2.232, 1.5462, 1.4058, 1.2746, 1.1528, 1.0732, 1.0192, .9983, .9983, .9983, .9983]`（默认）| 升序正元素向量

液力变矩器的扭矩比 Rτ。向量的每个元素必须为正值。模块将扭矩比定义为 Rτ=τT/τI。如果 *Rω* 超过 **Speed ratio vector** 参数的最后一个元素，模块将根据 **Extrapolation method** 参数进行外推。

#### 依赖关系

要启用此参数，请将 **Coast mode modeling** 设置为 `Continuous`。

### **Capacity factor parameterization** — 容量系数定义 `Ratio of speed to square root of impeller torque`（默认）| `Ratio of impeller torque to square of speed`

容量系数的定义。

| `Ratio of speed to square root of impeller torque` | `Ratio of impeller torque to the square of the speed` |
| --- | --- |
| K=ω/τI | K\*=τI/ω2 |

当您选择 `Ratio of impeller torque to square of speed` 时，默认值为 `1e-3 * [6.616, 6.048, 5.787, 5.384, 4.681, 3.779, 2.671, 2.047, 1.111, .4]` `N*m/(rad/s)^2`。

#### 依赖关系

要启用此参数，请将 **Coast mode modeling** 设置为 `Continuous`。

### **Capacity factor reference speed** — 容量系数参考转速选项 `Always impeller speed`（默认）| `Turbine speed for speed ratios greater than one`

是始终使用泵轮转速作为参考转速，还是在速比大于 1 时使用涡轮转速。

- `Always impeller speed`：对所有 Rω 值使用泵轮转速 ωI。
- `Turbine speed for speed ratios greater than one`：对所有 Rω < 1 的值使用泵轮转速 ωI，当 Rω > 1 时使用涡轮转速 ωT。

#### 依赖关系

要启用此参数，请将 **Coast mode modeling** 设置为 `Continuous`。

### **Capacity factor vector** — 容量系数 `[12.2938, 12.8588, 13.1452, 13.6285, 14.6163, 16.2675, 19.3503, 22.1046, 29.9986, 50]` `rad/(N^(1/2)*m^(1/2)*s)`（默认）| 向量

液力变矩器的容量系数。模块根据下表定义容量系数：

**注意**

如果您未指定速比为 1 时的容量系数数据，模块将使用容量系数值 10\**KMax*，其中 *K*Max 是指定容量系数向量中的最大值。相应的扭矩比假定为 0。对于查找表数据中未明确指定的所有其他速比值，模块分别使用 **Interpolation method** 或 **Extrapolation method** 参数指定的插值或外推方法。

#### 依赖关系

要启用此参数，请将 **Coast mode modeling** 设置为 `Continuous`。

### 动力学

要启用这些参数，请将 **Coast mode modeling** 参数设置为 `Continuous`

### **Model transmission lag** — 传动滞后设置 `No lag – Suitable for HIL simulation`（默认）| `Specify time constant and initial value`

是否在仿真中包含传动滞后。当您选择：

- `No lag – Suitable for HIL simulation` 时，扭矩传递是瞬时的。当没有时间滞后时，输入泵轮扭矩 τI 和输出涡轮扭矩 τT 为：

  τI=sgn(1−ωT/ωI)(ωI/K)2

  τT=τTRτ
- `Specify time constant and initial value` 时，模块以时间滞后传递扭矩。如果选择此选项，您可以指定 **Torque transmission time constant** 和 **Initial turbine-to-impeller torque ratio** 参数。

### **Torque transmission time constant** — 扭矩传递时间常数 `.02` `s`（默认）| 正标量

扭矩传递时间。时间滞后会增加模型保真度和计算成本。有关详细信息，请参阅 Adjust Model Fidelity。

#### 依赖关系

要启用此参数，请将 **Model transmission lag** 设置为 `Specify time constant and initial value`。

### **Initial turbine-to-impeller torque ratio** — 涡轮与泵轮的初始扭矩比 `0`（默认）| 非负标量

涡轮与泵轮的初始扭矩比。

#### 依赖关系

要启用此参数，请将 **Model transmission lag** 设置为 `Specify time constant and initial value`。

### **Interpolation method** — 查找函数的插值方法 `Linear`（默认）| `Smooth`

查找函数的插值方法，指定为 `Linear` 或 `Smooth`。该方法在定义范围内的离散相对速度值之间插值扭矩比和容量系数函数。有关 `Linear` 和 `Smooth` 的详细信息，请参阅 `tablelookup`。

### **Extrapolation method** — 查找函数的外推方法 `Linear`（默认）| `Nearest` | `Error`

查找函数的外推方法，指定为 `Linear`、`Smooth` 或 `Error`。该方法外推扭矩比和容量系数函数。有关详细信息，请参阅 `tablelookup`。
## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2020b：使用模式图仿真滑行模式

要使用模式图来提高模式过渡期间的仿真鲁棒性，请将 **Coast mode modeling** 设置为 `Two-mode`。

## 描述

两个驱动轴之间的液力变矩器耦合

Torque Converter 模块表示一个汽车液力变矩器，由泵轮、涡轮和导轮组成。泵轮和涡轮构成液力耦合器，导轮通过改变返回泵轮的液流方向来增加扭矩。当轴带动泵轮旋转时，离心力将流体向外甩向涡轮叶片，使涡轮旋转，同时流体向中心流动并向外流向导轮。使用该模块将发动机连接到自动变速器。将端口 **I** 连接到发动机，将端口 **T** 连接到变速器。

液力变矩器横截面。流体从泵轮叶片连续流向涡轮叶片，然后通过导轮返回泵轮叶片。

默认情况下，模块在给定时间步长内将端口 **T** 处的扭矩 τT 和端口 **I** 处的扭矩 τI 相互约束。您可以选择性地包含由内部流体流动和可压缩性引起的扭矩传递时间滞后效应。要包含传动滞后，请将 **Model transmission lag** 设置为 `Specify time constant and initial value`。模块引入滞后并求出端口 **I** 处的稳态扭矩，使得

tc(dτI/dt)+τI=τI(steadystate)。

容量系数 *K* 的瞬时函数决定了 *τI* 的稳态值。当功率从端口 **I** 流向端口 **T** 时，模块在驱动模式下运行。当功率反向流动时，模块在滑行模式下运行。您可以连续仿真滑行模式过渡，或使用模式图进行仿真。模块使用液力变矩器的容量系数根据角速度计算扭矩。

### 双模式滑行过渡

当您将 **Coast mode modeling** 设置为 `Two mode` 时，模块对滑行和驱动使用单独的模式。模块根据角速度计算扭矩，使得

τ=K\*ω2，

其中 *K\** 是 **Drive mode capacity factor vector** 参数，*ω* 是端口 **I** 或端口 **T** 的角速度。容量系数是速比的函数。在驱动模式下，模块将速比定义为

Rω=ωT/ωI，

其中 *ωT* 和 *ωI* 分别表示端口 **T** 和 **I** 处的转速。在滑行模式下，模块将速比定义为

R^ω=ωI/ωT。

由于速比定义不同，模块还对滑行模式使用单独的容量系数 K^\*，即 **Coast mode capacity factor vector** 参数。**Mode transition parameter** 决定模块切换模式时的转速。图中展示了这两种模式。模式图示意图，其中驱动模式和滑行模式共享一个过渡区域。涡轮和泵轮转速匹配。在滑行模式极端处，泵轮转速为零。在驱动模式极端处，涡轮转速为零。

### 连续滑行过渡

当您将 **Coast mode modeling** 设置为 `Continuous` 时，模块在驱动模式和滑行模式之间平滑过渡。您还可以添加动力学。模块仿真在过渡区域附近运行时精度较低。

模块将速比定义为 Rω=ωT/ωI，将扭矩比定义为 Rτ=τT/τI。**Capacity factor parameterization** 参数控制模块如何定义容量系数。当您选择：

- `Ratio of speed to square root of impeller torque` 时，模块使用 K=ω/τI。
- `Ratio of impeller torque to square of speed` 时，模块使用 K\*=τI/ω2。

为了提高保真度，您可以在仿真中包含传动引起的滞后。当您将 **Model transmission lag** 设置为 `Specify time constant and initial value` 时，模块为扭矩传递添加恒定时间延迟。

当您将 **Coast mode modeling** 设置为 `Continuous` 时：

- 泵轮轴必须始终沿正方向旋转。仿真在 ωI < 0 时无效。
- 如果您使用扭矩源（如 Generic Engine 模块）驱动 Torque Converter 模块，则必须在源中包含惯量，以表示发动机、轴惯量或其他源组件。为确保泵轮以正方向开始旋转，请将此惯量的初始转速设置为正值。
