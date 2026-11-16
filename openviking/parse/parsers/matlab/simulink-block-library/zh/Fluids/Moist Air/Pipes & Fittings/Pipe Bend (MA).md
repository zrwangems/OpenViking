---
type: simulink-block
title: 'Pipe Bend (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Pipes & Fittings'
documentation_page: 'pipebendma'
documentation_source_path: 'ref/pipebendma.html'
language: zh-CN
chinese_source: worker-translation
---

# Pipe Bend (MA)

## 端口

### 守恒

### **A** — 湿空气液体端口

与液体入口或出口端口关联的湿空气守恒端口。

### **B** — 湿空气液体端口

与液体入口或出口端口关联的湿空气守恒端口。

## 参数

### 主要

### **Pipe diameter** — 管道直径 `0.01 m`（默认） | positive scalar

管道直径。

### **Bend radius** — 弯曲圆半径 `0.04 m`（默认） | positive scalar

管道弯曲形成的圆的半径。

### **Bend angle** — 管道弯曲的扫掠角度 `90 deg`（默认） | positive scalar

管道弯头的扫掠角度。

### **Internal surface absolute roughness** — 管壁粗糙度 `15e-6 m`（默认） | positive scalar

管壁绝对粗糙度。模块使用此参数确定 Darcy 摩擦因子，该因子影响管道中的压力损失。

### 效应和初始条件

### **Initial pressure** — 仿真开始时的湿空气压力 `0.101325 MPa`（默认） | positive scalar

仿真开始时的湿空气压力。

### **Initial pressure priority** — 压力参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **Initial pressure** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

### **Initial temperature** — 仿真开始时的温度 `293.15 K`（默认） | positive scalar

初始湿空气温度。

### **Initial temperature priority** — 温度参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **Initial temperature** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

### **Initial humidity specification** — 湿度指定 `Relative humidity`（默认） | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

指定初始湿空气湿度的方法。

### **Initial relative humidity** — 仿真开始时的相对湿度 `0.5`（默认） | scalar in the range of [0,1]

仿真开始时湿空气中的相对湿度。相对湿度是水蒸气分压与水蒸气饱和压力之比，或水蒸气摩尔分数与饱和水蒸气摩尔分数之比。

#### 依赖关系

要使能此参数，请将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial relative humidity priority** — 相对湿度参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **Initial relative humidity** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要使能此参数，请将 **Initial humidity specification** 设置为 `Relative humidity`。

### **Initial specific humidity** — 仿真开始时的比湿度 `0.01`（默认） | scalar in the range of [0,1]

仿真开始时的比湿度。比湿度是水蒸气质量与总质量（水蒸气、痕量气体和干空气）之比。

#### 依赖关系

要使能此参数，请将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial specific humidity priority** — 比湿度参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **Initial specific humidity** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要使能此参数，请将 **Initial humidity specification** 设置为 `Specific humidity`。

### **Initial water vapor mole fraction** — 仿真开始时水蒸气的摩尔分数 `0.01`（默认） | scalar in the range [0,1]

仿真开始时湿空气通道中水蒸气的摩尔分数。水蒸气摩尔分数是相对于水蒸气、痕量物质和干空气的总摩尔量。

#### 依赖关系

要使能此参数，请将 **Initial humidity specification** 设置为 `Mole fraction`。

### **Initial water vapor mole fraction priority** — 水蒸气摩尔分数湿度参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **Initial water vapor mole fraction** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要使能此参数，请将 **Initial humidity specification** 设置为 `Mole fraction`。

### **Initial humidity ratio** — 仿真开始时的湿度比 `0.01`（默认） | scalar in the range [0,1]

仿真开始时湿空气通道中的湿度比。湿度比是水蒸气质量与干空气和痕量气体质量之比。

#### 依赖关系

要使能此参数，请将 **Initial humidity specification** 设置为 `Humidity ratio`。

### **Initial humidity ratio priority** — 湿度比参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **Initial humidity ratio humidity** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要使能此参数，请将 **Initial humidity specification** 设置为 `Humidity ratio`。

### **Initial wet-bulb temperature** — 仿真开始时的湿球温度 `287 K`（默认） | scalar in the range [0,1]

仿真开始时的湿球温度。模块使用此值计算水分。

#### 依赖关系

要使能此参数，请将 **Initial humidity specification** 设置为 `Wet-bulb temperature`。

### **Initial wet-bulb temperature priority** — 湿球温度参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **Initial wet-bulb temperature** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要使能此参数，请将 **Initial humidity specification** 设置为 `Wet-bulb temperature`。

### **Initial trace gas specification** — 痕量气体的测量类型 `Mass fraction`（默认） | `Mole fraction`

痕量气体的测量类型。

### **Initial trace gas mass fraction** — 湿空气通道中痕量气体的量 `0.001`（默认） | scalar in the range [0,1]

仿真开始时湿空气中痕量气体的量（按质量分数）。质量分数是相对于水蒸气、痕量气体和干空气的总质量。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数为 `None`，则模块忽略此参数。

#### 依赖关系

要使能此参数，请将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **Initial trace gas mass fraction priority** — 痕量气体质量分数参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **Initial trace gas mass fraction priority** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要使能此参数，请将 **Initial trace gas specification** 设置为 `Mass fraction`。

### **Initial trace gas mole fraction** — 仿真开始时痕量气体的摩尔分数 `0.001`（默认） | scalar in the range [0,1]

仿真开始时湿空气通道中痕量气体的量（按摩尔分数）。摩尔分数是相对于水蒸气、痕量气体和干空气的总摩尔量。

如果 Moist Air Properties (MA) 模块中的 **Trace gas model** 参数为 `None`，则模块忽略此参数。

#### 依赖关系

要使能此参数，请将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **Initial trace gas mole fraction priority** — 痕量气体摩尔分数参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **Initial trace gas mole fraction priority** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要使能此参数，请将 **Initial trace gas specification** 设置为 `Mole fraction`。

### **Initial mass ratio of water droplets to moist air** — 水滴与湿空气之比 `0`（默认） | positive scalar

水滴与湿空气的初始质量比。

### **Initial mass ratio of water droplets to moist air priority** — 水滴与湿空气质量比参数优先级 `High`（默认） | `Low` | `None`

求解器在初始化模块时分配给 **Initial mass ratio of water droplets to moist air priority** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，可能需要将此参数设置为 `Low` 或 `None`。

### **Relative humidity at saturation** — 凝结的相对湿度点 `1`（默认） | scalar in the range [0,1]

凝结的相对湿度点。高于此值会发生凝结。大于 1 的值表示过饱和蒸汽。

### **Water vapor condensation time constant** — 凝结的时间尺度 `1e-3 s`（默认） | positive scalar

过饱和湿空气体积通过凝结多余水分回到饱和状态的特征时间尺度。

### **Water droplets evaporation time constant** — 蒸发的时间尺度 `1e-3 s`（默认） | positive scalar

水滴蒸发为蒸汽的特征时间尺度。

### **Fraction of condensate entrained as water droplets** — 水滴中凝结物的比例 `1`（默认） | scalar in the range [0,1]

湿空气中作为水滴夹带的凝结物比例。

## 所属库

Simscape / Fluids / Moist Air / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2023a 中引入**

### R2024b：对湿空气流中悬浮的水滴建模

湿空气域中的模块现在可以对湿空气流中悬浮的水滴建模。要对水滴建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

### R2024b：更新了初始条件选项

现在可以将模块的初始条件指定为参数。

## 描述

湿空气网络中的管道弯头段

Pipe Bend (MA) 模块表示湿空气网络中的弯曲管道。可以定义管道特性以计算因摩擦和管道曲率造成的损失。该模块使用水力损失系数对损失建模，对于可忽略可压缩流动效应的较低速流动，结果可能更准确。

### 管道曲率损失系数

因几何变化引起的压力损失系数包括角度修正因子 *Cangle* 和弯曲系数 *Cbend*：

Kloss=CangleCbend.

模块按以下公式计算 *Cangle*：

Cangle=0.0148θ−3.9716⋅10−5θ2,

其中 *θ* 是 **Bend angle** 参数的值，单位为度。

模块根据基于 Crane [1] 的数据，由弯曲半径 *r* 与管道直径 *d* 之比（针对 90° 弯头）的表格计算 *Cbend*：

显示 90° 管道弯头的图示

| *r/d* | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 20 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 20 *fT* | 14 *fT* | 12 *fT* | 12 *fT* | 14 *fT* | 17 *fT* | 24 *fT* | 30 *fT* | 34 *fT* | 38 *fT* | 42 *fT* | 50 *fT* | 58 *fT* |

模块根据管道直径 [1]，从表格数据中插值干净商用钢的摩擦因子 *fT*。此表包含干净商用钢管在完全湍流区流动时的管道摩擦数据。

| 公称尺寸 (mm) | 5 | 10 | 15 | 20 | 25 | 32 | 40 | 50 | 72.5 | 100 | 125 | 150 | 225 | 350 | 609.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 摩擦因子, *fT* | .035 | .029 | .027 | .025 | .023 | .022 | .021 | .019 | .018 | .017 | .016 | .015 | .014 | .013 | .012 |

修正因子适用于弯曲半径与直径之比在 1 到 24 之间。超出此范围时，模块采用最近邻外插。

### 层流中因摩擦造成的损失

端口 **A** 和 **B** 处流动的压力损失公式相同。

当管道中的流动完全层流，或低于 *Re* = 2000 时，弯头的压力损失为

Δploss=μλ2ρId2AL2m˙port,

其中：

- *μ* 是相对湿度。
- *λ* 是 Darcy 摩擦因子常数，对于层流为 64。
- *ρI* 是内部流体密度。
- *d* 是管道直径。
- *L* 是弯头长度段，它是 **Bend radius** 和 **Bend angle** 参数的乘积：Lbend=rbendθ。
- *A* 是管道横截面积，π4d2。
- m˙port 是相应端口处的质量流量。

### 湍流中因摩擦造成的损失

当流动完全湍流，或大于 *Re* = 4000 时，管道中的压力损失为：

Δploss=(fDL2d+Kloss2)m˙port|m˙port|2ρIA2,

其中 *f*D 是 Darcy 摩擦因子。模块使用经验 Haaland 方程和 **Internal surface absolute roughness** 参数来近似此值。模块对管道段的每一半取微分，即在端口 **A** 到内部节点之间，以及内部节点到端口 **B** 之间。

### 压差

模块基于内部流体体积压力 *pI* 计算弯头的压力损失：

pA−pI=Δploss,A

pB−pI=Δploss,B

### 质量与能量平衡

进入弯管内湿空气体积的净流率为

m˙total=m˙A+m˙B-m˙w,cond-m˙w,conv+m˙d,evapm˙w,total=m˙wA+m˙wB-m˙w,cond-m˙w,conv+m˙d,evapm˙g,total=m˙gA+m˙gBm˙d,total=m˙dA+m˙dB+λd(m˙w,cond+m˙w,conv)-m˙d,evap

其中：

- m˙ 是质量流量。下标 *w* 表示
  水蒸气，下标 *g* 表示痕量气体，下标
  *d* 表示水滴。
- *λd* 是 **Fraction
  of condensate entrained as water droplets** 参数的值。
- m˙w,cond 是由于流体体积饱和导致的水蒸气冷凝
  速率。
- m˙w,conv 是壁面上的冷凝速率。
- m˙d,evap 是水滴蒸发
  速率。
- *Φ* 是能量流率。

混合物的质量守恒方程将压力、温度以及
内部湿空气体积质量分数关联起来

(1pIdpIdt−1TIdTIdt)ρIV+Ra−RwRI(m˙w,total−xwm˙total)+Ra−RgRI(m˙g,total−xgm˙total)=m˙total,

其中：

- *pI* 是内部体积的压力。
- *ρI* 是内部体积的密度。
- *TI* 是内部体积的温度。
- *V* 是体积。
- *Ra*、
  *Rg*、
  *Rw* 和
  *RI* 分别是空气、气体、水蒸气和内部体积的
  比气体常数。
- *xw* 是比湿度。
- *xg* 是痕量气体质量分数。

能量守恒方程将能量流率与压力、温度以及
内部湿空气体积质量分数关联起来

(cpI−RI+rdcpdI)VρIdTIdt+uaIm˙MA,total+(uwI−uaI)m˙w,total+(ugI−uaI)m˙g,total+hdIm˙d,total=     ϕA+ϕB−(1−λd)(m˙w,condhdI),

其中：

- *uI* 是内能。
- *cpI* 是比热。
- *rd* 是水滴与湿空气的质量比。
- *cpdI* 是水滴比热。
- m˙d,total 是总水滴质量流量。
- *hdI* 是水滴比焓。
- *ϕA* 是端口 **A** 处的能量流率。
- *ϕB* 是端口 **B** 处的能量流率。
- m˙w,cond 是由于流体体积饱和导致的水蒸气冷凝
  速率。
- *λd* 是
  **Fraction of condensate entrained as water droplets**
  参数的值。
- *ϕA* 是端口 **A** 处的能量流率。
- *ϕB* 是端口 **B** 处的能量流率。

水滴质量守恒方程将水蒸气质量流量
与内部湿空气体积水分水平关联起来

dxwIdtρIV+xwIm˙total=m˙w,total.

痕量气体质量守恒方程将痕量气体质量流量与
内部湿空气体积痕量气体水平关联起来

dxgIdtρIV+xgIm˙total=m˙g,total.

水滴质量守恒方程将水滴质量流量
与内部湿空气体积中夹带水滴的动力学关联起来

drdIdtρIV+rdIm˙total=m˙d,total.
