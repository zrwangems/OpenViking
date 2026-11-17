---
type: simulink-block
title: 'Pilot-Operated Check Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: 'pilotoperatedcheckvalvetl'
documentation_source_path: 'ref/pilotoperatedcheckvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Pilot-Operated Check Valve (TL)

## 端口
```yaml
ports:
- name: A
  summary: 阀入口，热液体
  direction: conserving
- name: B
  summary: 阀入口，热液体
  direction: conserving
- name: X
  summary: 先导端口，热液体
  direction: conserving
```

### 守恒端口

### **A** — 阀入口，热液体

正常工作期间（当先导机构禁用时），工作流体必须通过该开口进入阀门的通道。仅当先导端口被加压到足够程度时，该端口才能用作出口。

### **B** — 阀入口，热液体

正常工作期间（当先导机构禁用时），工作流体必须通过该开口离开阀门的通道。

### **X** — 先导端口，热液体

通过该开口（施加足够的压力）来致动先导机构，从而打开阀门以实现反向流动。
## 参数
```yaml
parameters:
- name: Pressure control specification
  summary: 选择用作阀门控制信号的压力测量值 Pressure difference of port X relative to port A（默认）| Pressure at port X
  group: ''
- name: Cracking pressure differential
  summary: 阀门首次打开时的有效控制压力 0.01 MPa（默认）| 以压力为单位的正标量
  group: ''
- name: Maximum opening pressure differential
  summary: 阀门完全打开时的有效控制压力 0.02 MPa（默认）| 以压力为单位的正标量
  group: ''
- name: Pilot ratio
  summary: 先导端口面积与入口端口面积之比 1（默认）| 正的无量纲标量
  group: ''
- name: Maximum opening area
  summary: 由于密封不完美，完全打开位置时的开口面积 1e-4 m^2（默认）| 以面积为单位的正标量
  group: ''
- name: Leakage area
  summary: 由于密封不完美，最大关闭位置时的开口面积 1e-10 m^2（默认）| 以面积为单位的正标量
  group: ''
- name: Smoothing factor
  summary: 应用于阀门开口面积函数的平滑量 0（默认）
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 阀门端口处垂直于流动路径的面积 0.01 m^2（默认）| 以面积为单位的正标量
  group: ''
- name: Discharge coefficient
  summary: 定义为实际质量流量与理想质量流量之比的经验因子 0.64（默认）| 正的无量纲标量
  group: ''
- name: Critical Reynolds number
  summary: 层流与湍流流态之间边界处的雷诺数 150（默认）| 正的无量纲标量
  group: ''
```

### **Pressure control specification** — 选择用作阀门控制信号的压力测量值 `Pressure difference of port X relative to port A`（默认）| `Pressure at port X`

选择用作先导控制信号的压力测量值。该模块使用所选测量值来计算阀门的控制压力。（有关计算方法，请参见模块描述。）

在默认设置 `Pressure difference of port X relative to port A` 下，控制压力是先导端口（**X**）到入口（**A**）之间压降的函数。在替代设置 `Pressure at port X` 下，它是入口处表压的函数。

### **Cracking pressure differential** — 阀门首次打开时的有效控制压力 `0.01 MPa`（默认）| 以压力为单位的正标量

阀门开始打开时的有效压差。该压差——模块描述中的*控制压力*——是入口到出口的压降与先导压力和先导比的乘积之和。（所使用的先导压力取决于 **Pressure control specification** 参数的设置。）

### **Maximum opening pressure differential** — 阀门完全打开时的有效控制压力 `0.02 MPa`（默认）| 以压力为单位的正标量

阀门完全打开时的有效压差。该压差——模块描述中的*控制压力*——是入口到出口的压降与先导压力和先导比的乘积之和。（所使用的先导压力取决于 **Pressure control specification** 参数的设置。）

### **Pilot ratio** — 先导端口面积与入口端口面积之比 `1`（默认）| 正的无量纲标量

先导端口面积与入口端口面积之比。

### **Maximum opening area** — 由于密封不完美，完全打开位置时的开口面积 `1e-4 m^2`（默认）| 以面积为单位的正标量

当阀门处于压力调节范围上限时，阀门在完全打开位置的开口面积。

### **Leakage area** — 由于密封不完美，最大关闭位置时的开口面积 `1e-10 m^2`（默认）| 以面积为单位的正标量

当仅存在端口之间的内部泄漏时，阀门在最大关闭位置的开口面积。该参数主要用于确保阀门关闭不会导致流体网络的部分被隔离（已知这种状况会在仿真中引发问题）。此处指定的确切值不如其为一个大于零的（非常小的）数值重要。

### **Smoothing factor** — 应用于阀门开口面积函数的平滑量 `0`（默认）

应用于阀门开口面积函数的平滑量。该参数确定要平滑的区域的宽度——一个位于完全打开位置，另一个位于完全关闭位置。

平滑在每个开口面积函数区域上叠加一个非线性段（一个三阶多项式函数，平滑由此产生）。此处指定的值越大，平滑程度越大，非线性段越宽。

在默认值 `0` 下，不应用平滑。此时向最大关闭位置和完全打开位置的过渡会引入不连续性（与零交叉相关），这往往会降低仿真速率。

### **Cross-sectional area at ports A and B** — 阀门端口处垂直于流动路径的面积 `0.01 m^2`（默认）| 以面积为单位的正标量

阀门端口处垂直于流动路径的面积。假定各端口尺寸相同。此处指定的流动面积理想情况下应与相邻组件的入口面积相匹配。

### **Discharge coefficient** — 定义为实际质量流量与理想质量流量之比的经验因子 `0.64`（默认）| 正的无量纲标量

通过阀门的实际流量与其在理想阀门中会具有的理论值之比。该半经验参数衡量允许通过阀门的流量：其值越大，流量越大。如有阀门数据表，请参阅该参数。

### **Critical Reynolds number** — 层流与湍流流态之间边界处的雷诺数 `150`（默认）| 正的无量纲标量

假定流动在层流与湍流流态之间过渡时的雷诺数。
## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

带控制端口的单向阀，用于实现反向流动

Pilot-Operated Check Valve (TL) 模块对带超驰机构的单向阀进行建模，以便在激活时允许回流。（单向阀则是一种带单向开启机构的节流孔，安装该机构正是为了防止回流。）

超驰机构为阀门增加了第三个端口——*先导*端口。在正常工作期间，先导端口不活动，阀门的行为与任何其他单向阀相同。此时，仅当其上的压力梯度从入口到出口下降时，其节流孔才打开。需要反向压力梯度的回流不会发生。该模式保护阀门上游的组件免受来自下游点的压力冲击、温度尖峰以及（在实际系统中）化学污染的影响。

当需要回流时，先导端口被加压，阀门的控制元件——通常是球或活塞——被推离其阀座。此时阀门对两个方向的流动均打开，反向压降（从出口指向入口）足以驱动流体向上游流动。（位于流动路径中的阀座决定阀门是否打开。当其被覆盖时——被球、活塞或其他控制元件——流动被切断，阀门关闭。）

阀门逐渐打开，从其开启压力开始，一直持续到其压力调节范围的末端。开启压力给出了阀门必须克服的初始阻力（由于摩擦或弹簧力），以打开一丝缝隙（或*开启*）。低于该阈值时，阀门关闭，仅泄漏流可以通过。超过压力调节范围的末端后，阀门完全打开，流量达到最大值（由瞬时压力条件决定）。

开启压力在倒置安装的单向阀中起着重要作用。在那里，开启元件——如球或活塞——的重量以及流体的高程压头可能起到打开阀门的作用。（在模型中，当入口上游的管道垂直或倾斜时，可能产生高程压头。）足够的开启压力可防止阀门即使以不利角度放置时也不经意地打开。

### 控制压力

阀门的开度取决于先导压力和从入口到出口的压降：

pCtl=kXpX+pA−pB，

其中 *p* 是表压，*k* 是先导比——先导开口面积 (*S*X) 与阀门开口面积 (*S*R) 的比例。下标 `X` 表示先导值，下标 `A` 和 `B` 分别表示入口和出口值。端口压力是在仿真期间确定的变量（相对于绝对零压）。

先导压力可以是相对于入口（端口 **A**）的差值，也可以是表压值（相对于环境）。您可以使用 **Pressure control specification** 下拉列表选择适当的设置——`Pressure difference of port X relative to port A` 或 `Pressure at port X`。如果您选择 `Pressure at port X`，

pX=pX,Abs−pAtm，

其中下标 `Atm` 表示大气值（从模型的热液体设置 (TL) 或热液体属性 (TL) 模块获得）。下标 `X,Abs` 表示先导端口处的绝对值。如果您选择 `Pressure difference of port X relative to port A`，

pX=pX,Abs−pA,Abs

其中下标 `A,Abs` 类似地表示阀门入口（端口 **A**）处的绝对值。先导压差被约束为大于或等于零——如果其计算值应为负，则在控制压力计算中假定为零。

### 控制压力超调

控制压力超过开启压力的程度决定了阀门将打开多少。压力超调在此表示为压力调节范围（宽度）的分数：

p^=pCtl−PCrkPMax−PCrk。

控制压力 *pCtl*、开启压力 *pCrk* 和最大开启压力 *P*Max 对应于所选择的控制压力规格：`Pressure differential` 或 `Pressure at port A`。

该分数——技术上称为*归一化*超调——在阀门完全关闭时取值为 `0`，在阀门完全打开时取值为 `1`。如果计算应返回超出这些界限的值，则改用两者中最近的值。（换句话说，该分数在 `0` 和 `1` 处*饱和*。）

### 开度参数化

阀门面积的线性参数化为

Avalve=p^(Amax−Aleak)+Aleak，

其中归一化压力 p^ 为

p^=pcontrol−pcrackingpmax−pcracking。

当阀门在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，该模块会在 *pcracking* 和 *pmax* 之间平滑地饱和控制压力。有关更多信息，请参阅数值平滑。

### 开口面积

阀门面积随平滑后的控制压力线性打开，

S=(SMax−SMin)p^+SMin，

其中 *SMax* 是最大阀门面积，*SMin* 是 **Leakage area** 参数的值。

### 动量平衡

阀门通道中产生的那些压力损失的原因在模块中被忽略。无论它们的性质如何——面积突变、流道扭曲——在仿真期间只考虑它们的累积效应。该效应在模块中通过流量系数来体现，流量系数是衡量通过阀门的质量流量相对于理想阀门中理论值的量度。将阀门中的动量平衡表示为流动中引起的压降：

pA−pB=m˙Avgm˙Avg2+m˙Crit22ρAvgCDS\*2[1−(S\*S)2]ξp，

其中 *ρ* 是密度，*C*D 是流量系数，*ξ*p 是压降比——衡量出口处压力恢复对阀门总压降贡献程度的量度。下标 Avg 表示热液体端口处值的平均值。临界质量流量 m˙Crit 由临界雷诺数计算——在该雷诺数下，假定阀门中的流动从层流转变为湍流：

m˙Crit=ReCritμAvgπ4S，

其中 *μ* 表示动力粘度。压降比计算为：

ξp=1−(S\*S)2(1−CD2)−CDS\*S1−(S\*S)2(1−CD2)+CDS\*S。

### 质量平衡

阀门内部的流体体积，因此其质量，被假定为非常小，并且出于建模目的被忽略。因此，不会有任何量的流体在那里积聚。根据质量守恒原理，通过一个端口进入阀门的质量流量必须等于通过另一个端口离开阀门的质量流量：

m˙A+m˙B=0，

其中 m˙ 定义为通过端口 **A** 或 **B** *进入*阀门的质量流量。

### 能量平衡

阀门被建模为绝热组件。流体与其周围壁之间不能发生热交换。流体从入口到出口流动时，没有对流体做功或由流体做功。在这些假设下，能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口能量流之和必须始终等于零：

ϕA+ϕB=0，

其中 *ϕ* 定义为通过其中一个端口（**A** 或 **B**）*进入*阀门的能量流率。
