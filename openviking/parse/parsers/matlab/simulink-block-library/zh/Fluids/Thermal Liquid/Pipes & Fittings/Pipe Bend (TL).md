---
type: simulink-block
title: 'Pipe Bend (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Pipes & Fittings'
documentation_page: 'pipebendtl'
documentation_source_path: 'ref/pipebendtl.html'
language: zh-CN
chinese_source: worker-translation
---

# Pipe Bend (TL)

## 端口

### 守恒端口

### **A** — 液体端口（热液体）

与管道弯头一端相关联的热液体守恒端口。

### **B** — 液体端口（热液体）

与管道弯头一端相关联的热液体守恒端口。

## 参数

### **Pipe diameter** — 管道直径 `0.01 m`（默认）| 正标量

管道的直径。

### **Bend radius** — 弯曲圆半径 `0.04 m`（默认）| 正标量

管道弯头所形成圆的半径。

### **Bend angle** — 弯曲角度 `90 deg`（默认）| 正标量

管道弯头的扫掠角度。

### **Elevation gain from port A to port B** — 管道高程变化 `0 m`（默认）| 标量

沿管道长度从端口 **A** 到端口 **B** 的高程变化。

### **Gravitational acceleration** — 重力加速度 `9.81 m/s^2`（默认）| 标量

重力加速度。仅当 **Elevation gain from port A to port B** 参数的值不为 `0` 时，模块才使用此参数。

### **Internal surface absolute roughness** — 管壁粗糙度 `15e-6 m`（默认）| 正标量

管壁绝对粗糙度。此参数用于确定 Darcy 摩擦因子，该因子影响管道中的压力损失。

### **Enable dynamic compressibility** — 是否对流体可压缩性建模 `off`（默认）| `on`

是否对由流体可压缩性引起的流体质量变化进行建模。当您选择 **Enable dynamic compressibility** 时，将计算由于段内流体密度变化引起的质量变化。管道中的流体体积保持不变。

### **Initial liquid temperature** — 仿真开始时的液体温度 `293.15` `K`（默认）

仿真开始时的液体温度。

### **Initial liquid pressure** — 仿真开始时的管道压力 `0.101325 MPa`（默认）| 正标量

仿真开始时的管道压力。

#### 依赖关系

要启用此参数，请选择 **Enable dynamic compressibility**。

### **Nominal liquid temperature** — 标称工况下的温度 `293.15 K`（默认）| 标量

标称工况下的液体温度。当动态可压缩性禁用时，模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Nominal liquid pressure** — 标称工况下的压力 `0.101325 MPa`（默认）| 标量

标称工况下的液体压力。当动态可压缩性禁用时，模块使用此值计算用于质量和能量守恒方程的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

### R2025a：管道弯头高程的模型更改

使用 **Elevation gain from port A to port B** 参数指定沿管道弯头长度方向的高程变化。

## 描述

热液体网络中的管道弯头段

Pipe Bend (TL) 模块对热液体网络中的弯曲管道进行建模。您可以定义管道特性以计算由于摩擦和管道曲率引起的损失，并可选择对流体可压缩性进行建模。

### 管道曲率损失系数

由于几何形状变化引起的压力损失系数由角度修正因子 *C*angle 和弯曲系数 *C*bend 组成：

Kloss=CangleCbend。

模块按如下方式计算 *Cangle*：

Cangle=0.0148θ−3.9716⋅10−5θ2，

其中 *θ* 是 **Bend angle** 参数的值，以度为单位。

模块根据基于 Crane [1] 的数据，从 90° 弯头的弯曲半径 *r* 与管道直径 *d* 之比的表格数据中计算 *Cbend*：

显示 90° 管道弯头的示意图

| *r/d* | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 20 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 20 *fT* | 14 *fT* | 12 *fT* | 12 *fT* | 14 *fT* | 17 *fT* | 24 *fT* | 30 *fT* | 34 *fT* | 38 *fT* | 42 *fT* | 50 *fT* | 58 *fT* |

模块根据管道直径从基于 [1] 的表格数据中插值计算清洁商用钢的摩擦因子 *f*T。此表包含在完全湍流区域流动的清洁商用钢管道的管道摩擦数据。

| 标称尺寸 (mm) | 5 | 10 | 15 | 20 | 25 | 32 | 40 | 50 | 72.5 | 100 | 125 | 150 | 225 | 350 | 609.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 摩擦因子，*fT* | .035 | .029 | .027 | .025 | .023 | .022 | .021 | .019 | .018 | .017 | .016 | .015 | .014 | .013 | .012 |

修正因子在弯曲半径与直径之比介于 1 到 24 之间时有效。超出此范围时，模块采用最近邻外推。

### 层流中由于摩擦引起的损失

端口 **A** 和 **B** 处的流动压力损失公式相同。

当管道中的流动为完全层流，即低于 *Re* = 2000 时，弯头的压力损失为：

Δploss=μλ2ρId2AL2m˙port，

其中：

- *μ* 是流体动力粘度。
- *λ* 是 Darcy 摩擦因子常数，层流时为 64。
- *ρ*I 是内部流体密度。
- *d* 是管道直径。
- *L* 是弯曲长度段，即 **Bend radius** 与 **Bend angle** 的乘积：Lbend=rbendθ。
- *A* 是管道横截面积，π4d2。
- m˙port 是相应端口处的质量流量。

### 湍流中由于摩擦引起的损失

当流动为完全湍流，即大于 *Re* = 4000 时，管道中的压力损失为：

Δploss=(fDL2d+Kloss2)m˙port|m˙port|2ρIA2，

其中 *f*D 是 Darcy 摩擦因子。这由经验 Haaland 方程近似，并基于 **Internal surface absolute roughness**。微分在管道段的一半上进行，即端口 **A** 与内部节点之间，以及内部节点与端口 **B** 之间。

### 不可压缩流体的压差

当流动不可压缩时，弯头的压力损失为

pA−pB=Δploss,A−Δploss,B+ρIgΔz，

其中 *g* 是 **Gravitational acceleration** 参数的值，*Δz* 是 **Elevation gain from port A to port B** 参数的值。

### 可压缩流体的压差

当流动可压缩时，模块基于内部流体体积压力 *p*I 计算弯头的压力损失，

pA−pI=Δploss,A+ρIgΔz2pB−pI=Δploss,B−ρIgΔz2

### 质量守恒

当您清除 **Enable dynamic compressibility** 复选框时，流入管道的质量流量等于流出管道的质量流量：

m˙A+m˙B=0。

当选择 **Enable dynamic compressibility** 时，管道质量守恒方程为

m˙A+m˙B=ρIV˙+ρIV(p˙IβI−αIT˙I)，

其中：

- *pI* 是内部节点 I 处的热液体压力。
- T˙I 是内部节点 I 处热液体温度的变化率。
- *βI* 是热液体体积模量。
- *α* 是液体热膨胀系数。

### Energy Conservation

模块的能量守恒方程为

E˙=ϕA+ϕB−m˙avggΔz，

其中：

- *ϕA* 是端口 **A** 处的能量流率。
- *ϕB* 是端口 **B** 处的能量流率。

如果流体不可压缩，能量累积率为

E˙=ρ0cpIVdTIdt，

其中：

- *cpI*
  是模块内部节点处的流体比热。
- *V* 是管道体积。
- *ρ0* 是流体密度。模块根据 **Nominal liquid
  temperature** 和 **Nominal liquid
  pressure** 参数计算该值。

如果流体可压缩，能量累积率为

E˙=dpIdtdUdp+dTdtdUdT。
