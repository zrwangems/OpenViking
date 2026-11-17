---
type: simulink-block
title: 'Pipe (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'pipeil'
documentation_source_path: 'ref/pipeil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pipe (IL)

## 端口

### 守恒端口

### **A** — 入口或出口等温液体

与管道入口或出口相关联的等温液体守恒端口。
该模块没有固有方向性。

### **B** — 入口或出口等温液体

与管道入口或出口相关联的等温液体守恒端口。
该模块没有固有方向性。

## 参数

### 几何

### **Pipe length** — 管道长度 `5 m`（默认）| 正标量

管道沿流动方向的长度。

### **Cross-sectional area** — 管道内部面积 `0.01 m^2`（默认）| 正标量

管道垂直于流动方向的内部面积。

### **Hydraulic diameter** — 具有相同横截面积的等效圆柱形管道直径 `0.1128 m`（默认）| 正标量

具有相同横截面积的等效圆柱形管道直径。

### 摩擦

### **Aggregate equivalent length of local resistances** — 管道中所有局部阻力的总长度 `1 m`（默认）| 正标量

管道中所有局部阻力的总长度。局部阻力包括弯头、管件、附件以及管道入口和出口。局部阻力的作用是增加管段的等效长度。该长度仅在摩擦计算中添加到管道几何长度上。管道内的液体体积仅取决于由 **Pipe length** 参数定义的管道几何长度。

### **Internal surface absolute roughness** — 管道内表面所有表面缺陷的平均深度 `15e-6 m`（默认）| 正标量

管道内表面所有表面缺陷的平均深度，影响湍流流态下的压力损失。

### **Laminar flow upper Reynolds number limit** — 流动开始从层流过渡到湍流的上限雷诺数 `2000`（默认）| 大于 1 的标量

流动开始从层流过渡到湍流的上限雷诺数。该数值等于完全发展层流对应的最大雷诺数。

### **Turbulent flow lower Reynolds number limit** — 流动开始从湍流过渡到层流的下限雷诺数 `4000`（默认）| 大于 **Laminar flow upper Reynolds number limit** 值的标量

流动开始从湍流过渡到层流的下限雷诺数。该数值等于完全发展湍流对应的最小雷诺数。

### **Laminar friction constant for Darcy friction factor** — 管道几何形状对粘性摩擦损失的影响 `64`（默认）| 正标量

无量纲因子，表征管道横截面几何形状对层流流态下粘性摩擦损失的影响。典型值为：圆形横截面为 64，方形横截面为 57，长宽比为 2 的矩形横截面为 62，薄环形横截面为 96 [1]。

### 效应和初始条件

### **Enable dynamic compressibility** — 选择是否对流体动态可压缩性建模 `On`（默认）| `Off`

选择是否考虑液体的动态可压缩性。动态可压缩性使液体密度依赖于压力，在小时间尺度上影响系统的瞬态响应。

### **Enable fluid inertia** — 选择是否对流体惯性建模 `Off`（默认）| `On`

选择是否考虑液体的流动惯性。流动惯性使液体对质量流量的变化产生阻力。

#### 依赖关系

要启用此复选框，请选中 **Enable dynamic compressibility** 复选框。

### **Initial liquid pressure** — 零时刻的液体压力 `0.101325 MPa`（默认）| 正标量

仿真开始时管道中的液体压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility** 复选框。

### **Initial mass flow rate from port A to port B** — 零时刻的质量流量 `0 kg/s`（默认）| 标量

零时刻从端口 **A** 到端口 **B** 的质量流量。

#### 依赖关系

要启用此参数，请选中 **Enable fluid inertia** 复选框。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中用于流体流动的刚性导管

Pipe (IL) 模块对等温液体网络中的管道流动动力学进行建模。该模块考虑粘性摩擦损失，还可以考虑动态可压缩性和流体惯性。

管道包含恒定体积的液体。液体由于粘性摩擦而经历压力损失，遵循 Darcy-Weisbach 方程。

### 管道效应

该模块允许您包含动态可压缩性和流体惯性效应。开启这些效应中的每一个都可以提高模型保真度，但代价是方程复杂性增加以及可能的仿真成本增加：

- 当动态可压缩性关闭时，假设液体在管道体积中停留的时间可忽略不计。因此，管道中没有质量积累，质量流入等于质量流出。这是最简单的选项。当管道中的液体质量占系统中总液体质量的比例可忽略不计时，此选项是合适的。
- 当动态可压缩性开启时，质量流入和质量流出的不平衡可能导致液体在管道中积累或减少。因此，管道体积中的压力可以动态上升和下降，这为系统提供了一定的顺应性并调节快速压力变化。这是默认选项。
- 如果动态可压缩性开启，您还可以开启流体惯性。此效应除了摩擦阻力外，还会产生额外的流动阻力。此额外阻力与质量流量的变化率成正比。考虑流体惯性会减慢流量的快速变化，但也可能导致流量超调和振荡。此选项适用于非常长的管道。开启流体惯性并将多个管段串联连接，以模拟压力波沿管道的传播，例如水锤现象。

### 质量平衡

管道的质量守恒方程为

m˙A+m˙B={0,if fluid dynamic compressibility is offp˙IβIρIV,if fluid dynamic compressibility is on

其中：

- m˙A 和 m˙B 是通过端口 **A** 和 **B** 的质量流量。
- *V* 是管道流体体积。
- *p*I 是管道内的压力。
- *ρ*I 是管道内的流体密度。
- *β*I 是管道内的流体体积模量。

流体可以是纯液体和少量夹带空气的混合物，如连接到回路的 Isothermal Liquid Properties (IL) 模块所指定。用于计算 *ρ*I 和 *β*I 的方程，以及每个半管道的粘性摩擦压力损失方程中的端口密度 *ρ*A 和 *ρ*B，取决于所选的等温液体模型。有关详细信息，请参阅 Isothermal Liquid Modeling Options。

### Momentum Balance

该表显示了每个半管道的动量守恒方程。

|  |  |
| --- | --- |
| 对于与端口 **A** 相邻的半管道 | pA−pI={Δpv,A,if fluid inertia is offΔpv,A+L2Sm¨A,if fluid inertia is on |
| 对于与端口 **B** 相邻的半管道 | pB−pI={Δpv,B,if fluid inertia is offΔpv,B+L2Sm¨B,if fluid inertia is on |

在方程中：

- *p*、*p*A 和
  *p*B 分别是端口
  **A** 和端口 **B** 处的液体压力。
- *Δp*v,A 和
  *Δp*v,B 是管道体积中心与端口 **A** 和
  **B** 之间的粘性摩擦压力
  损失。
- *L* 是管道长度。
- *S* 是管道横截面积。

### Viscous Friction Pressure Losses

该表显示了每个半管道的粘性摩擦压力损失方程。

|  |  |
| --- | --- |
| 对于与端口 **A** 相邻的半管道 | Δpv,A={λμ(L+Leq2)m˙A2ρIDh2S,if ReA<RelamfA(L+Leq2)m˙A|m˙A|2ρIDhS2,if ReA>Retur |
| 对于与端口 **B** 相邻的半管道 | Δpv,B={λμ(L+Leq2)m˙B2ρIDh2S,if ReB<RelamfB(L+Leq2)m˙B|m˙B|2ρIDhS2,if ReB≥Retur |

在方程中：

- *λ* 是管道形状因子，用于计算层流状态下的达西摩擦
  因子。
- *μ* 是管道中液体的动力粘度。
- *L*eq 是局部管道阻力的总等效长度。
- *D*h 是管道的
  水力直径。
- *f*A 和
  *f*B 是与端口 **A** 和 **B** 相邻的管道半段中的
  达西摩擦因子。
- *Re*A 和
  *Re*B 是端口
  **A** 和 **B** 处的雷诺数。
- *Re*lam 是流动转变为湍流时对应的
  雷诺数下限。
- *Re*tur 是流动转变为层流时对应的
  雷诺数上限。

当雷诺数介于 *Re*lam 和
*Re*tur 之间时，流动处于层流与湍流之间的过渡状态。过渡
区域中由粘性摩擦引起的压力损失在层流状态和
湍流状态之间平滑连接。

该模块根据通过相应端口的质量流量计算端口 **A** 和
**B** 处的雷诺数：

Re=|m˙|DhμS.

达西摩擦因子由湍流状态下的 Haaland 近似给出：

f=1(−1.8log10(6.9Re+(13.7rDh)1.11))2,

其中：

- *f* 是达西摩擦因子。
- *r* 是管道表面粗糙度。

### 假设和限制

- 管壁是刚性的。
- 流动是充分发展的。
- 重力的影响可以忽略不计。
