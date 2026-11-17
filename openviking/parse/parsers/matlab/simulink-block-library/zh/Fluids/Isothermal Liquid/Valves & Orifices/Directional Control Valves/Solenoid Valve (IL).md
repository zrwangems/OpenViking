---
type: simulink-block
title: 'Solenoid Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: 'solenoidvalveil'
documentation_source_path: 'ref/solenoidvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Solenoid Valve (IL)

## 端口
```yaml
ports:
- name: S
  summary: 控制阀门的信号，无量纲物理信号
  direction: input
- name: A
  summary: 液体端口，等温液体
  direction: input
- name: B
  summary: 液体端口，等温液体
  direction: input
- name: +
  summary: 正极端子，电气
  direction: input
- name: '-'
  summary: 负极端子，电气
  direction: input
```

### 输入

### **S** — 控制阀门的信号，无量纲物理信号

控制阀门的物理信号。当端口 **S** 处的信号高于 0.5 时，电磁铁开启，阀门打开。当端口 **S** 处的信号降至 0.5 以下时，电磁铁关闭，阀门关闭。

#### 依赖关系

要启用此端口，请将 **Solenoid control** 设置为 `Physical signal`。
### 守恒

### **A** — 液体端口，等温液体

液体进入或出口端口。

### **B** — 液体端口，等温液体

液体进入或出口端口。

### **+** — 正极端子，电气

与阀门控制正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Solenoid control** 设置为 `Electrical ports`。

### **-** — 负极端子，电气

与阀门控制负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Solenoid control** 设置为 `Electrical ports`。
## 参数
```yaml
parameters:
- name: Solenoid control
  summary: 选择阀门控制方法 Physical signal（默认）| Electrical ports
  group: ''
- name: Valve initial position
  summary: 阀门的初始位置 Closed（默认）| Open
  group: ''
- name: Opening switching time
  summary: 打开时流量上升的时间 0.05 s（默认）| 正标量
  group: ''
- name: Closing switching time
  summary: 关闭时流量下降的时间 0.1 s（默认）| 正标量
  group: ''
- name: Maximum opening area
  summary: 完全打开阀门的面积 1e-4 m^2（默认）| 正标量
  group: ''
- name: Leakage area
  summary: 完全关闭位置时的阀门间隙面积 1e-10 m^2（默认）
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 阀门入口或出口处的面积 inf m^2（默认）| 正标量
  group: ''
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: ''
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: ''
- name: Pressure recovery
  summary: 是否考虑面积扩大中的压力增加 off（默认）| on
  group: ''
- name: Rated voltage
  summary: 电磁铁额定电压 12 V（默认）| 正标量
  group: ''
- name: Nominal current
  summary: 稳态电流 2e-4 A（默认）| 正标量
  group: ''
- name: Solenoid inductance
  summary: 线性电磁铁电感 1e-6 H（默认）| 正标量
  group: ''
- name: Plunger distance of travel
  summary: 柱塞行程距离 1.8e-3 m（默认）| 正标量
  group: ''
- name: Initial current
  summary: 电磁铁初始电流 0 A（默认）| 正标量
  group: ''
```

### **Solenoid control** — 选择阀门控制方法 `Physical signal`（默认）| `Electrical ports`

选择模块用于控制阀门的方法。如果选择 `Physical signal`，模块使用物理信号 **S** 来控制阀门。如果选择 `Electrical network`，模块启用电气 **+** 和 **-** 端口并建模电气响应。

### **Valve initial position** — 阀门的初始位置 `Closed`（默认）| `Open`

阀门的初始位置是打开还是关闭。

### **Opening switching time** — 打开时流量上升的时间 `0.05` `s`（默认）| 正标量

从电磁铁开启到流量达到其最大值和最小值之间 90% 处的时间。

如果 **Solenoid control** 设置为 `Electrical ports`，请使用阶跃输入在 **Rated voltage** 参数值处计算此参数。

### **Closing switching time** — 关闭时流量下降的时间 `0.1` `s`（默认）| 正标量

从电磁铁关闭到流量降至其最大值和最小值之间 10% 处的时间。

如果 **Solenoid control** 设置为 `Electrical ports`，请使用阶跃输入在 **Rated voltage** 参数值处计算此参数。

### **Maximum opening area** — 完全打开阀门的面积 `1e-4` `m^2`（默认）| 正标量

阀门处于完全打开位置时的横截面积。

### **Leakage area** — 完全关闭位置时的阀门间隙面积 `1e-10` `m^2`（默认）

阀门处于完全关闭位置时所有间隙的总和。模块将任何小于此值的阀门面积饱和到指定的泄漏面积。泄漏面积通过保持流动的连续性来帮助数值稳定性。

### **Cross-sectional area at ports A and B** — 阀门入口或出口处的面积 `inf` `m^2`（默认）| 正标量

入口和出口端口 **A** 和 **B** 处的横截面积。模块在确定通过阀门的质量流量的压力-流量方程中使用此面积。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

考虑理论流动中排放损失的修正因子。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀门的层流的上限雷诺数。

### **Pressure recovery** — 是否考虑面积扩大中的压力增加 `off`（默认）| `on`

模块是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

### **Rated voltage** — 电磁铁额定电压 `12` `V`（默认）| 正标量

电磁铁的额定电压。使用阶跃输入在此电压下计算 **Opening switching time** 和 **Closing switching time** 参数的值。

#### 依赖关系

要启用此参数，请将 **Solenoid control** 设置为 `Electrical ports`。

### **Nominal current** — 稳态电流 `2e-4` `A`（默认）| 正标量

电磁铁在 **Rated voltage** 参数值处的稳态电流。

#### 依赖关系

要启用此参数，请将 **Solenoid control** 设置为 `Electrical ports`。

### **Solenoid inductance** — 线性电磁铁电感 `1e-6` `H`（默认）| 正标量

电磁铁的线性电感。模块将电感近似为线性。

#### 依赖关系

要启用此参数，请将 **Solenoid control** 设置为 `Electrical ports`。

### **Plunger distance of travel** — 柱塞行程距离 `1.8e-3` `m`（默认）| 正标量

柱塞在完全关闭和完全打开阀门位置之间行进的距离。

#### 依赖关系

要启用此参数，请将 **Solenoid control** 设置为 `Electrical ports`。

### **Initial current** — 电磁铁初始电流 `0` `A`（默认）| 正标量

电磁铁中的初始电流。

#### 依赖关系

要启用此参数，请将 **Solenoid control** 设置为 `Electrical ports`。
## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2023b：将阀门直接连接到电气网络

您现在可以通过将模块直接连接到电气网络来控制它。将 **Solenoid control** 参数设置为 Electrical network 以建模电气响应并启用电气 + 和 - 端口。

## 描述

等温液体系统中的电磁阀

Solenoid Valve (IL) 模块模拟等温液体网络中通过电磁阀的流动。该阀门由一个带电磁执行器的两位方向控制阀组成。端口 **S** 处的物理信号控制电磁铁。当端口 **S** 处的信号高于 0.5 时，电磁铁开启，阀门打开。当端口 **S** 处的信号降至 0.5 以下时，电磁铁关闭，阀门关闭。

电磁阀由一个阀体组成，阀体内有一个由电磁铁操作的弹簧加载柱塞。当电磁铁开启时，磁力提升阀芯，允许流体流动。当电磁铁关闭时，弹簧将柱塞推回原位，停止流动。模块不显式建模电磁铁的力学，而是使用打开和关闭切换时间来表征阀门的打开和关闭。

### 质量流量

通过阀门的质量流量为

m˙=CdA2ρ¯(1−AAport)Δp(Δp2+Δpcrit2)1/4,

其中：

- *A* 是阀门的横截面积。
- *Aport* 是 **Cross-sectional area at ports A and B** 参数的值。
- *Cd* 是 **Discharge coefficient** 参数的值。
- ρ¯ 是阀门中的平均流体密度。
- *Δp* 是阀门两端的压力变化。
- *Δpcrit* 是临界压力，

  Δpcrit=π8Aρ¯(μRecritCd)2,

  其中 *Recrit* 是 **Critical Reynolds number** 参数的值，*μ* 是流体粘度。

### 打开动力学

模块假设电磁铁表现为电阻-电感串联电路，表示为

V=iR+L∂i∂t,

其中：

- *V* 是电磁铁电感两端的电压。
- *R* 是电磁铁电感的电阻。
- *L* 是电磁铁的电感。
- *i* 是通过电磁铁电感的电流。

电磁铁产生与电流平方成正比的力，Fmag=−12Ki2，其中 *K* 是比例常数。阀门横截面积 *A(t)* 的表达式取决于 **Solenoid control** 参数的值。

**使用物理信号控制的阀门**

当您将 **Solenoid control** 设置为 `Physical signal` 时，模块基于端口 **S** 处的信号计算打开面积。当阀门打开时，

A(t)=Amax−Aleak7(e−2t−t0τopen−8et−t0τopen)+Amaxt0=tstart+log(4−16−7Amax−A0Amax−Aleak)τopen。

当阀门关闭时，

A(t)=(Amax−Aleak)e−t−t0τclose+Aleakt0=tstart+log(A0−AleakAmax−Aleak)τclose，

其中：

- *Amax* 是 **Maximum opening area** 参数的值。
- *Aleak* 是 **Leakage area** 参数的值。
- *tstart* 是电磁铁开启或关闭的时间。
- *A0* 是电磁铁开启或关闭时的阀门面积。
- τopen=−tswitchopenlog(4−15.3)，其中 *tswitchopen* 是 **Opening switching time** 参数的值。
- τclose=tswitchcloselog(0.1)，其中 *tswitchclose* 是 **Closing switching time** 参数的值。

**使用电气端口控制的阀门**

当您将 **Solenoid control** 设置为 `Electrical ports` 时，模块基于在端口 **+** 和 **-** 处连接到电磁阀的电气网络计算打开面积。

打开面积为

A=xl(Amax−Aleak)+Aleak，

其中 *x* 是柱塞位置，*l* 是 **Plunger distance of travel** 参数的值。

模块使用力平衡表达式建模柱塞运动

mcorex¨=Fmagnetic−Fspring+Fhardstop,

其中：

- *mcore* 是电磁阀中运动部件的质量。
- *Fspring* 是电磁铁关闭时弹簧施加的关闭阀门的力。
- *Fhardstop* 是防止柱塞移动超过完全打开和完全关闭位置的硬停止力。模块使用模式图计算硬停止。有关详细信息，请参阅 Mode Chart Modeling。
- *Fmagnetic* 是电磁铁产生的力，

  Fmagnetic=−12Ki2.

模块使用力平衡表达式的解在 **Rated voltage**、**Nominal current**、**Opening switching time** 和 **Closing switching time** 参数值处计算 *mcore*、*Fspring* 和 *K*。然后模块使用这些 *mcore*、*Fspring* 和 *K* 值来求解所有其他时间的柱塞位置。

### 切换时间

模块通过分别由 **Opening switching time** 和 **Closing switching time** 参数指定的阀门打开和关闭切换时间来表征电磁阀。**Opening switching time** 参数是从电磁铁开启到流量上升至其最大值和最小值之间 90% 处的时间。

显示阀门打开时阀门面积随时间增加的图。当时间达到打开切换时间时，阀门面积开始趋于平稳。

**Closing switching time** 参数是从电磁铁关闭到流量下降至其最大值和最小值之间 10% 处的时间。

显示阀门关闭时阀门面积随时间减小的图。当时间达到关闭切换时间时，阀门面积开始趋于平稳。

### 假设和限制

- 最大电磁力与弹簧产生的力相同。
- 电磁铁内部的阻尼和压力流动力可忽略不计。
- 阀芯是平衡的。
- 电磁铁行程距离足够短，模块假设电感是线性的。
