---
type: simulink-block
title: 'Pipe Bend (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid Library / Pipes and Fittings'
documentation_page: 'pipebendil'
documentation_source_path: 'ref/pipebendil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pipe Bend (IL)

## 端口

### 守恒

### **A** — 液体端口 isothermal liquid

液体进入或离开端口。

### **B** — 液体端口 isothermal liquid

液体进入或离开端口。

## 参数

### **Pipe diameter** — 管道直径 `0.01 m`（默认） | 正标量

管道的直径。

### **Bend radius** — 弯头圆半径 `0.04 m`（默认） | 正标量

管道弯头所形成的圆的半径。

### **Bend angle** — 弯曲角度 `90 deg`（默认） | 正标量

管道弯头扫过的角度。

### **Elevation gain from port A to port B** — 管道高程变化 `0 m`（默认） | 标量

沿管道从端口 **A** 到端口 **B** 的高程变化。

### **Gravitational acceleration** — 重力加速度 `9.81 m/s^2`（默认） | 标量

重力加速度。仅当 **Elevation gain from port A to port B** 参数的值不为 `0` 时，模块才使用此参数。

### **Internal surface absolute roughness** — 管道壁面粗糙度 `15e-6 m`（默认） | 正标量

管道壁面绝对粗糙度。此参数用于确定 Darcy 摩擦因子，该因子会造成管道中的压力损失。

### **Enable dynamic compressibility** — 是否对流体可压缩性建模 `off`（默认） | `on`

是否对由流体可压缩性引起的任何流体质量变化进行建模。当您选择 **Fluid compressibility** 时，将计算由于段内流体密度变化引起的质量变化。管道中的流体体积保持恒定。在 Isothermal Liquid 库中，所有模块将密度计算为压力的函数。

### **Initial liquid pressure** — 仿真开始时的管道压力 `0.101325 MPa`（默认） | 正标量

仿真开始时的管道压力。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2025a：管道弯头高程中的模型变更

使用 **Elevation gain from port A to port B** 参数指定沿管道弯头长度方向的高程变化。

## 描述

等温液体网络中的管道弯头段

Pipe Bend (IL) 模块对等温液体网络中的弯曲管道进行建模。您可以定义管道特性，以计算由摩擦和管道曲率引起的损失，并可选择对流体可压缩性建模。

### 管道曲率损失系数

由几何变化引起的压力损失系数由角度修正因子 *C*angle 和弯头系数 *C*bend 组成：

Kloss=CangleCbend.

模块按如下方式计算 *Cangle*：

Cangle=0.0148θ−3.9716⋅10−5θ2,

其中 *θ* 是 **Bend angle** 参数的值，以度为单位。

模块根据基于 Crane [1] 的数据，针对 90° 弯头，从弯曲半径 *r* 与管道直径 *d* 之比的表格数据中计算 *Cbend*：

显示 90° 管道弯头的示意图

| *r/d* | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 20 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 20 *fT* | 14 *fT* | 12 *fT* | 12 *fT* | 14 *fT* | 17 *fT* | 24 *fT* | 30 *fT* | 34 *fT* | 38 *fT* | 42 *fT* | 50 *fT* | 58 *fT* |

模块根据管道直径 [1]，从表格数据中插值计算洁净商用钢的摩擦因子 *f*T。此表包含流动处于完全湍流区时洁净商用钢管道的管道摩擦数据。

| 公称尺寸 (mm) | 5 | 10 | 15 | 20 | 25 | 32 | 40 | 50 | 72.5 | 100 | 125 | 150 | 225 | 350 | 609.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 摩擦因子，*fT* | .035 | .029 | .027 | .025 | .023 | .022 | .021 | .019 | .018 | .017 | .016 | .015 | .014 | .013 | .012 |

该修正因子适用于弯曲半径与直径之比介于 1 和 24 之间的情况。超出此范围时，模块采用最近邻外推。

### 层流中由摩擦引起的损失

端口 **A** 和 **B** 处流动的压力损失公式相同。

当管道中的流动为完全层流，或低于 *Re* = 2000 时，弯头的压力损失为：

Δploss=μλ2ρId2AL2m˙port,

其中：

- *μ* 是流体动力黏度。
- *λ* 是 Darcy 摩擦因子常数，层流时为 64。
- *ρ*I 是内部流体密度。
- *d* 是管道直径。
- *L* 是弯头长度段，为 **Bend radius** 和 **Bend angle** 的乘积：Lbend=rbendθ。
- *A* 是管道横截面积，π4d2。
- m˙port 是相应端口处的质量流量。

### 湍流中由摩擦引起的损失

当流动为完全湍流，或大于 *Re* = 4000 时，管道中的压力损失为：

Δploss=(fDL2d+Kloss2)m˙port|m˙port|2ρIA2,

其中 *f*D 是 Darcy 摩擦因子。该因子通过经验 Haaland 方程近似，并基于 **Internal surface absolute roughness**。差分是在管段的一半上取得，即端口 **A** 到内部节点之间，以及内部节点到端口 **B** 之间。

### 不可压缩流体的压差

当流动不可压缩时，弯头的压力损失为

pA−pB=Δploss,A−Δploss,B+ρIgΔz,

其中 *g* 是 **Gravitational acceleration** 参数的值，*Δz* 是 **Elevation gain from port A to port B** 参数的值。

### 可压缩流体的压差

当流动可压缩时，模块基于内部流体体积压力 *p*I 计算弯头的压力损失，

pA−pI=Δploss,A+ρIgΔz2pB−pI=Δploss,B−ρIgΔz2

### 质量守恒

当清除 **Enable dynamic compressibility** 复选框时，流入管道的质量流量等于流出管道的质量流量

m˙A+m˙B=0.

当选择 **Enable dynamic compressibility** 时，流入和流出管道的质量流量之差取决于由可压缩性引起的流体密度变化

m˙A+m˙B=p˙IdρIdpIV,

其中 *V* 是管道横截面积和弯头长度的乘积，*AL*。
