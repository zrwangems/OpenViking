---
type: simulink-block
title: 'Flow Resistance (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Elements'
documentation_page: 'flowresistance2p'
documentation_source_path: 'ref/flowresistance2p.html'
language: zh-CN
chinese_source: worker-translation
---

# Flow Resistance (2P)

## 端口
```yaml
ports:
- name: A
  summary: 流动阻力两相流体端口
  direction: conserving
- name: B
  summary: 流动阻力两相流体端口
  direction: conserving
```

### 守恒端口

### **A** — 流动阻力两相流体端口

两相流体进入或离开流动阻力的端口。

### **B** — 流动阻力两相流体端口

两相流体进入或离开流动阻力的端口。
## 参数
```yaml
parameters:
- name: Nominal pressure drop
  summary: 已知工况下的压降 0.001 MPa（默认）| 带压力单位的标量
  group: ''
- name: Nominal mass flow rate
  summary: 已知工况下的质量流量 0.1 kg/s（默认）| 带质量/时间单位的标量
  group: ''
- name: Nominal specific volume
  summary: 已知工况下的比体积 0 m^3/kg（默认）| 带体积/质量单位的标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 流动阻力端口处的流通面积 0.01 m^2（默认）| 带面积单位的标量
  group: ''
- name: Fraction of nominal mass flow rate for laminar flow
  summary: 阈值质量流量与标称质量流量之比 1e-3（默认）| 无量纲标量
  group: ''
- name: Mass flow rate into port A
  summary: 通过端口 A 进入阻力的质量流量 293.15 K（默认）| 带温度单位的正标量
  group: 变量
```

### **Nominal pressure drop** — 已知工况下的压降 0.001 MPa（默认）| 带压力单位的标量

在已知工况下从入口到出口的压降。该模块使用标称参数来计算压降与质量流量之间的比例常数。

### **Nominal mass flow rate** — 已知工况下的质量流量 0.1 kg/s（默认）| 带质量/时间单位的标量

在已知工况下通过组件的质量流量。该模块使用标称参数来计算压降与质量流量之间的比例常数。

### **Nominal specific volume** — 已知工况下的比体积 0 m^3/kg（默认）| 带体积/质量单位的标量

在已知工况下流动阻力内部的比体积。该模块使用标称参数来计算压降与质量流量之间的比例常数。将此参数设置为零以忽略压降对比体积的依赖性。

### **Cross-sectional area at ports A and B** — 流动阻力端口处的流通面积 0.01 m^2（默认）| 带面积单位的标量

流动阻力端口处的流通面积。假定各端口尺寸相同。

### **Fraction of nominal mass flow rate for laminar flow** — 阈值质量流量与标称质量流量之比 1e-3（默认）| 无量纲标量

阈值质量流量与标称质量流量之比。该模块使用此参数来计算阈值质量流量——并最终设置压降的线性化限值。

### 变量

### **Mass flow rate into port A** — 通过端口 A 进入阻力的质量流量 293.15 K（默认）| 带温度单位的正标量

仿真开始时通过端口 **A** 进入阻力的质量流量。
## 所属库

Simscape / Foundation Library / Two-Phase Fluid / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

两相流体支路中的通用阻力

Flow Resistance (2P) 模块对两相流体网络支路中的通用压降进行建模。压降与质量流量的平方以及两相流体的密度成正比。比例常数由模块对话框中指定的标称工况确定。

当组件的唯一可用数据是其压降随质量流量的变化关系时，请使用此模块。将该模块与其他模块组合，可以创建更准确地捕获其引起的压降的自定义组件——例如，基于腔室模块的热交换器。

### 质量平衡

假定流动阻力内部的流体体积可忽略不计。则通过一个端口流入的质量流量必须恰好等于通过另一个端口流出的质量流量：

m˙A+m˙B=0，

其中 m˙A 和 m˙B 分别定义为通过端口 **A** 和 **B** 流入组件的质量流量。

### Energy Balance

能量只能通过两个两相流体端口进入和离开流阻。壁面与环境之间不发生热交换。此外，流体不做功也不对其做功。因此，通过一个端口进入的能量流率必须恰好等于通过另一个端口流出的能量流率：

ϕA+ϕB=0，

其中 *ϕ*A 和 *ϕ*B 分别是通过端口 **A** 和 **B** 进入流阻的能量流率。

### Momentum Balance

作用在流体上的相关外力包括端口处由压力引起的力以及组件壁面处由粘性摩擦引起的力。重力以及其他体积力均被忽略。将摩擦力用损失系数 *ξ* 表示，可得到半经验表达式：

Δp=ξνm˙22S2，

其中：

- *Δp* 是从端口 **A** 到端口 **B** 的压降——即 *p*A + *p*B。
- *ξ* 是损失系数。
- *ν* 是比体积，即质量密度 *ρ* 的倒数——即 *1/**ρ*。
- *S* 是流通面积。

压降方程的实现有两处修改。首先，为了允许在流动方向反转时符号发生变化，将其改写为：

Δp=ξνm˙|m˙|2S2，

其中压降仅在质量流率也为正时才为正。其次，为了消除由流动反转引起的奇异性——这些奇异性可能在仿真期间对数值求解器构成挑战——在接近零流量的小区域内对其进行线性化：

Δp=ξνm˙m˙2+​m˙Th22S2，

其中 m˙Th 是阈值质量流率，低于该值时压降被线性化。图中显示了修改后的压降与局部质量流率的关系（曲线 **I**）：

- 高于 m˙Th 时，压降近似于原始方程（曲线 **II**）所表达的值，并且随 m˙2 变化。这种依赖性与湍流中观察到的情况一致。
- 低于 m˙Th 时，压降近似为一条直线，其斜率部分取决于 m˙Th（曲线 **III**），并且随 m˙ 变化。这种依赖性与层流中观察到的情况一致。

为便于建模，损失系数 *ξ* 不作为模块参数要求。相反，它根据模块对话框中指定的标称条件自动计算：

ξ2S2=Δp\*ν\*m˙\*2，

其中星号（\*）表示标称工况下的值。所有这些计算的基础是假设阈值质量流率 m˙Th 远小于标称值 m˙\*。将压降表达式中的分数 *ξ*/(2S2) 替换后得到：

Δp=νΔp\*ν\*m˙\*2(m˙m˙2+m˙Th2)。

或者等价地：

Δp=Cνm˙m˙2+m˙Th2，

其中 *C* 是流阻两端压降与局部质量流率之间的比例常数。其定义为：

C=Δp\*ν\*m˙\*2。

如果假设比体积——因此也包括质量密度——不变，则其标称值和实际值必须始终相等。当模块对话框中指定的标称值为 `0` 时就是这种情况——`0` 是一个特殊值，用于向模块表明比体积为常数。此时两者之比为 `1`，乘积 *C**ν* 简化为：

Cν=Δp\*m˙\*2。
