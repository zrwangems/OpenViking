---
type: simulink-block
title: 'Poppet Valve (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Valves & Orifices / Flow Control Valves'
documentation_page: 'poppetvalveg'
documentation_source_path: 'ref/poppetvalveg.html'
language: zh-CN
chinese_source: worker-translation
---

# Poppet Valve (G)

## 端口

### 守恒端口

### **A** — 液体端口气体

与流体进入或离开阀门的开口相关联的气体守恒端口。

### **B** — 液体端口气体

与流体进入或离开阀门的开口相关联的气体守恒端口。

### 输入

### **L** — 归一化球位移，范围为 [0,1] 物理信号

归一化球位移。球位置由最大开启距离归一化。值为 0 表示阀门完全关闭，值为 1 表示阀门完全打开。

## 参数

### **Valve seat specification** — 阀座几何形状的定义 `Sharp-edged`（默认）| `Conical`

球阀座的几何形状。该参数决定阀门的开口面积。

### **Cone angle** — 阀锥形座与其中心线之间的角度 `120 deg`（默认）| 正标量

锥形座斜面与其中心线之间形成的角度。

#### 依赖关系

要启用此参数，请将 **Valve seat specification** 设置为 `Conical`。

### **Ball diameter** — 用于调节阀门开度的球的直径 `0.01 m`（默认）| 标量

球控制元件的直径。

### **Orifice diameter** — 阀门孔口的直径 `7e-3 m`（默认）| 标量

阀门恒定孔口的直径。对于锥形几何形状，为阀座根部的直径。

### **Valve parameterization** — 用于指定孔口流动特性的参数化方法 `Orifice area based on geometry`（默认）| `Cv flow coefficient` | `Kv flow coefficient` | `Sonic conductance`

计算质量流量的方法。

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。
- `Sonic conductance` — 稳态下阻性元件的声速导纳决定模块参数化。
- `Orifice area based on geometry` — 流动限制的尺寸决定模块参数化。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 范围 [0,1] 内的正标量

用于修正理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Orifice area based on geometry`。

### **Maximum Cv flow coefficient** — 对应最大开启状态的 Cv 系数 `4`（默认）| 正标量

当可用于流动的限制面积达到最大时的 *Cv* 流量系数值。该参数衡量气体在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient`。

### **xT pressure differential ratio factor at choked flow** — 压差比系数 `0.7`（默认）| 正标量

进口压力 *pin* 与出口压力 *pout* 之间的比值，定义为 (pin−pout)/pin，此时首次发生阻塞流。如果您没有此值，请查阅 ISA-75.01.01 [3] 中的表 2。否则，默认值 0.7 对许多阀门来说是合理的。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Cv flow coefficient` 或 `Kv flow coefficient`。

### **Maximum Kv flow coefficient** — 对应最大开启状态的 Kv 系数 `3.6`（默认）| 正标量

当可用于流动的限制面积达到最大时的 *Kv* 流量系数最大值。该参数衡量气体在压差驱动下通过阻性元件的难易程度。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Kv flow coefficient`。

### **最大声速流导** — 对应组件最大开启状态的声速流导 `12 l/(bar*s)`（默认）| 正标量

当可用于流动的横截面积达到最大值时的声速流导值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **临界压力比** — 流量首次阻塞时的下游与上游压力之比 `0.3`（默认）| 正标量

流量首次开始阻塞且流速达到最大值（由当地声速给出）时的压力比。压力比为出口压力除以入口压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **亚声速指数** — 用于表征亚声速流态中质量流量的指数 `0.5`（默认）| 正标量

用于更精确计算亚声速流态中质量流量的经验值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO 参考温度** — ISO 8778 参考温度 `293.15 K`（默认）| 标量

标准参考大气条件下的温度，在 ISO 8778 中定义为 293.15 K。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **ISO 参考密度** — ISO 8778 参考密度 `1.185 kg/m^3`（默认）| 正标量

标准参考大气条件下的密度，在 ISO 8778 中定义为 1.185 kg/m3。

仅当您使用的声速流导值是在不同参考值下获得时，才需要调整 ISO 参考参数值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Sonic conductance`。

### **泄漏流量分数** — 流量比 `1e-6`（默认）| 正标量

节流孔关闭时与开启时的流量之比。

### **平滑因子** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，当节流孔处于接近开启或接近关闭位置时，为流量响应引入一层渐变变化。将此参数设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

### **层流压力比** — 流量在层流和湍流流态之间过渡时的压力比 `0.999`（默认）| 正标量

流量在层流和湍流流态之间过渡时的压力比。压力比为出口压力除以入口压力。典型值范围为 `0.995` 到 `0.999`。

### **端口 A 和 B 处的横截面积** — 气体端口处的流通面积 `0.01 m^2`（默认）| 正标量

每个端口处垂直于流动路径的面积。各端口尺寸相同。此参数的值应与阻性元件所连接组件的入口面积相匹配。

## 所属库

Simscape / Fluids / Gas / Valves & Orifices / Flow Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2022b: 使用改进的流量计算对气体系统建模

在之前的版本中，气体库中的模块使用转换因子来根据声速导纳实现不同的孔口参数化。您可以使用 **Valve parameterization** 参数来指定参数化。

新的参数化还包括新参数：

- **xT pressure differential ratio factor at choked flow**
- **Discharge coefficient**
- **Leakage flow fraction**。此参数替换了 **Cv coefficient (USCS) at leakage flow**、**Kv coefficient (SI) at leakage flow**、**Sonic conductance at leakage flow** 和 **Restriction area at leakage flow** 参数。

为提高清晰度：

- **Opening parameterization** 参数已重命名为 **Opening characteristic**。
- **Reference temperature** 和 **Reference density** 参数已分别重命名为 **ISO reference temperature** 和 **ISO reference density**。
- **Cv coefficient (USCS) at maximum flow** 和 **Kv coefficient (USCS) at maximum flow** 参数已分别重命名为 **Maximum Cv coefficient** 和 **Maximum Kv coefficient**。
- **Sonic conductance at maximum flow** 参数已重命名为 **Maximum sonic conductance**。

### R2022b: 更新了模块名称

Ball Valve (G) 模块的标题已更改为 Poppet Valve (G)。要在气体系统中使用球阀，请使用 Ball Valve (G) 模块。

### R2022b: 移除了 Offset 参数

该模块不再具有 **Valve lift control offset** 参数，并且该模块不再对输入信号进行偏移。此更改不会影响兼容性。

## 描述

气体网络中的提升阀

Poppet Valve (G) 模块表示一个带有平移球的孔口，用于调节通过阀门的流量。在完全关闭位置，球停留在多孔阀座上，完全阻止流体在端口 **A** 和 **B** 之间通过。球与阀座之间的区域即为阀门的开口面积。

流动可以是层流或湍流，并且可以达到声速。最大速度发生在阀门喉部，此处流动最窄且最快。当下游压力下降不再能增加速度时，流动发生阻塞，速度饱和。当背压比达到阀门的临界值时，发生阻塞。该模块不捕获超音速流动。

### 球机械特性

该模块对球的位移进行建模，但不建模阀门打开或关闭的动态特性。端口 **L** 处的信号提供归一化球位置 *L*。请注意，*L* 是介于 0 和 1 之间的归一化距离，分别表示完全关闭的阀门和完全打开的阀门。如果计算返回超出此范围的数字，则该数字会被设置为最接近的边界值。

**数值平滑**

当 **Smoothing factor** 参数非零时，该模块对归一化球位置 *L* 应用数值平滑。启用平滑有助于在仿真中保持数值鲁棒性。

有关详细信息，请参阅数值平滑。

### 开口面积

阀门的开口面积取决于 **Valve seat geometry** 参数，该参数可以是 `Sharp-edged` 或 `Conical`。**Leakage flow fraction** 参数是阀门关闭时流量与打开时流量之比。**Leakage flow fraction** 允许在完全关闭位置时球与阀座之间存在微小接触间隙。该参数还保持流量连续性以提升求解器性能。

下图展示了提升阀的阀座类型。

**锐边阀座几何**

模块按如下公式计算阀门的开口面积

Sopen,sharp−edged=πrO(Gsharp+h)2+rO2[1−rB2(Gsharp+h)2+rO2]，

其中：

- *h* 是圆柱外边缘与阀座之间的距离。
- *rO* 是阀座孔口半径，模块根据 **Orifice diameter** 参数计算该值。
- *rB* 是球的半径，模块根据 **Ball diameter** 参数计算该值。
- *Gsharp* 是几何参数：Gsharp=rB2−rO2。

最大位移 *hmax* 限制开口面积：

hmax=2rB2−rO2+rOrO2+4rB22−Gsharp。

对于任何大于 *hmax* 的球位移，*Sopen* 为最大孔口面积值：

Sopen=π4dO2。

当端口 **L** 处的信号小于 0 时，阀门关闭，**Leakage flow fraction** 参数决定质量流量。

**锥形阀座几何**

模块按如下公式计算阀门的开口面积：

Sopen,conical=Gconicalh+π2sin(θ)sin(θ2)h2，

其中：

- *h* 是圆柱外边缘与阀座之间的垂直距离。
- *θ* 是 **Cone angle** 参数的值。
- *Gconical* 是几何参数，Gconical=πrBsin(θ)，其中 *rB* 是球半径。

最大位移 *hmax* 限制开口面积：

hmax=rB2+rO2cos(θ2)−rBsin(θ2)。

对于任何大于 *hmax* 的球位移，*Sopen* 为最大孔口面积值：

Sopen=π4dO2。

当端口 **L** 处的信号小于 0 时，阀门关闭，**Leakage flow fraction** 参数决定质量流量。

### 阀门参数化

模块行为取决于 **Valve parametrization** 参数：

- `Cv flow coefficient` — 流量系数 *C*v 决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Kv flow coefficient` — 流量系数 *K*v，其中 Kv=0.865Cv，决定模块参数化。流量系数衡量气体在特定压差驱动下流动的难易程度。
- `Sonic conductance` — 稳态下阻力元件的声速导决定模块参数化。声速导衡量气体在 *阻塞* 状态下流动的难易程度，阻塞是指流速达到当地声速的状态。当下游压力与上游压力之比达到称为 *临界压力比* 的临界值时，会发生阻塞。
- `Orifice area based on geometry` — 流动限制的尺寸决定模块参数化。

模块按阀门开度比例缩放指定的流通能力。当阀门开度比例从 `0` 上升到 `1` 时，流通能力的度量从其指定的最小值缩放到指定的最大值。

### 质量流量

模块方程取决于 **Orifice parametrization** 参数。
当您将 **Orifice parametrization** 设置为 `Cv
flow coefficient parameterization` 时，质量流量 m˙ 为

m˙=CvSopenSMaxN6Y(pin−pout)ρin，

其中：

- *Cv* 是
  **Maximum Cv flow coefficient**
  参数的值。
- *Sopen* 是阀门
  开口面积。
- *SMax* 是阀门完全打开时的最大
  阀门面积。
- *N6* 是一个常数，当质量流量单位为 kg/hr、压力单位为 bar、密度单位为
  kg/m3 时，其值等于 27.3。
- *Y* 是膨胀系数。
- *pin* 是入口
  压力。
- *pout* 是出口
  压力。
- *ρin* 是入口
  密度。

膨胀系数为

Y=1−pin−pout3pinFγxT，

其中：

- *Fγ* 是
  等熵指数与 1.4 的比值。
- *xT* 是
  **xT pressure differential ratio factor at choked
  flow** 参数的值。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数
*Blam* 的值以上时，模块会平滑过渡到方程的线性化形式，

m˙=CvSopenSMaxN6Ylamρavgpavg(1−Blam)(pin−pout)，

其中：

Ylam=1−1−Blam3FγxT。

当压力比 pout/pin 降至 1−FγxT 以下时，孔口变为阻塞状态，模块切换到
以下方程

m˙=23CvSopenSMaxN6FγxTpinρin。

当您将 **Orifice parametrization** 设置为 `Kv flow
coefficient parameterization` 时，模块使用这些相同的
方程，但通过关系式 Kv=0.865Cv 将 *Cv* 替换为
*Kv*。有关当
**Orifice parametrization** 参数为 `Kv
flow coefficient parameterization` 或 `Cv flow
coefficient parameterization` 时的质量流量方程的更多信息，请参阅 [2][3]。

当您将 **Orifice parametrization** 设置为 `Sonic
conductance parameterization` 时，质量流量 m˙ 为

m˙=CSopenSMaxρrefpinTrefTin[1−(poutpin−Bcrit1−Bcrit)2]m，

其中：

- *C* 是 **Maximum sonic
  conductance** 参数的值。
- *Bcrit* 是临界
  压力比。
- *m* 是 **Subsonic
  index** 参数的值。
- *Tref* 是
  **ISO reference temperature** 参数的值。
- *ρref* 是
  **ISO reference density** 参数的值。
- *Tin* 是入口
  温度。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数
*Blam* 的值以上时，模块会平滑过渡到方程的线性化形式，

m˙=CSopenSMaxρrefTrefTavg[1−(Blam−Bcrit1−Bcrit)2]m(pin−pout1−Blam)。

当压力比 pout/pin 降至临界压力比
*Bcrit* 以下时，孔口变为
阻塞状态，模块切换到方程

m˙=CSopenSMaxρrefpinTrefTin。

**Valve parameterization** 参数的 `Sonic conductance` 设置
适用于气动应用。如果您将此设置用于空气以外的气体，可能需要
按比重的平方根对声导进行缩放。

有关当 **Orifice
parametrization** 参数为 `Sonic conductance
parameterization` 时的质量流量方程的更多信息，请参阅 [1]。

当您将 **Orifice parametrization** 设置为
`Orifice area based on geometry` 时，质量流量
m˙ 为

m˙=CdSopen2γγ−1pinρin(poutpin)2γ[1−(poutpin)γ−1γ1−(SopenS)2(poutpin)2γ]，

其中：

- *Sopen* 是阀门
  开口面积。
- *S* 是 **Cross-sectional
  area at ports A and B** 参数的值。
- *Cd* 是
  **Discharge coefficient** 参数的值。
- *γ* 是等熵指数。

当压力比 pout/pin 升至 **Laminar flow pressure
ratio** 参数 *Blam* 的值以上时，模块会平滑过渡到方程的线性化形式，

m˙=CdSopen2γγ−1pavg2−γγρavgBlam2γ[1− Blamγ−1γ1−(SopenS)2Blam2γ](pinγ−1γ−poutγ−1γ1−Blamγ−1γ)。

当压力比 pout/pin 降至 (2γ+1)γγ−1 以下时，孔口变为阻塞状态，模块切换到
以下方程

m˙=CdSopen2γγ+1pinρin1(γ+12)2γ−1−(SopenS)2。

当 **Orifice parametrization** 参数为 `Orifice area based on
geometry` 时，关于质量流量方程的更多信息，请参阅 [4]。

### 能量平衡

该模块的阻性元件是绝热元件。流体与其周围壁面之间不会发生热交换。流体从入口流到出口时，没有对流体做功，也没有流体对外做功。能量只能通过端口 **A** 和 **B** 以平流方式流动。根据能量守恒原理，端口能量流之和始终等于零

ϕA+ϕB=0，

其中 *ϕ* 是通过端口 **A** 或 **B** 流入阀门的能量流率。

### 质量平衡

该模块假设阀门内流体的体积和质量非常小，并忽略这些值。因此，不会有任何流体在阀门中积聚。根据质量守恒原理，通过一个端口流入阀门的质量流率等于通过另一个端口流出阀门的质量流率

m˙A+m˙B=0，

其中 m˙ 定义为通过由 **A** 或 **B** 下标所指示的端口流入阀门的质量流率。

### 假设与限制

- `Orifice area based on
  geometry` 参数化方程对于远离理想气体的气体不太准确。
- 该模块不建模超声速流动。
