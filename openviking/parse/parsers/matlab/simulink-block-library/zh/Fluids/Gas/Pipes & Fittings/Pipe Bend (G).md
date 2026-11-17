---
type: simulink-block
title: 'Pipe Bend (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Pipes & Fittings'
documentation_page: 'pipebendg'
documentation_source_path: 'ref/pipebendg.html'
language: zh-CN
chinese_source: worker-translation
---

# Pipe Bend (G)

## 端口

### 守恒端口

### **A** — 液体端口气体

与液体入口或出口端口关联的气体守恒端口

### **B** — 液体端口气体

与液体入口或出口端口关联的气体守恒端口

## 参数

### **Pipe diameter** — 管道直径 `0.01 m`（默认）| 正标量

管道的直径。

### **Bend radius** — 弯曲圆半径 `0.04 m`（默认）| 正标量

管道弯曲所形成的圆的半径。

### **Bend angle** — 弯曲角度 `90 deg`（默认）| 正标量

管道弯曲的扫掠角度。

### **Internal surface absolute roughness** — 管壁粗糙度 `15e-6 m`（默认）| 正标量

管壁绝对粗糙度。该模块使用此参数确定 Darcy 摩擦因子，该因子影响管道中的压力损失。

### **Enable dynamic compressibility** — 对气体通道中的压力动态建模的选项 `On`（默认）| `Off`

对气体通道中的压力动态建模的选项。如果清除此复选框，该模块将从组件能量和质量守恒方程中移除压力导数项。

### **Nominal temperature** — 额定工况下的温度 `293.15 K`（默认）| 标量

额定工况下的气体温度。当禁用动态可压缩性时，该模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Nominal pressure** — 额定工况下的压力 `0.101325 MPa`（默认）| 标量

额定工况下的气体压力。当禁用动态可压缩性时，该模块使用此值计算用于质量和能量守恒方程的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Initial pressure** — 仿真开始时的压力 `0.101325 MPa`（默认）| 标量

仿真开始时气体通道中的压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility**。

### **Initial pressure priority** — 压力参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给 **Initial pressure** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility**。

### **Initial temperature** — 仿真开始时的温度 `293.15 K`（默认）| 标量

仿真开始时气体通道中的温度。

### **Initial temperature priority** — 温度参数优先级 `High`（默认）| `Low` | `None`

求解器在初始化模块时分配给 **Initial temperature** 参数的优先级。

将此参数设置为 `High` 以定义初始条件。如果此初始条件与另一个模块的初始条件冲突，您可能需要将此参数设置为 `Low` 或 `None`。

## 所属库

Simscape / Fluids / Gas / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2025a：可选地对动态可压缩性建模

Pipe Bend (G) 模块现在可以通过 **Enable dynamic compressibility** 参数可选地对动态可压缩性建模。此前，该模块始终对压力动态建模，这可能导致模型需要更长时间才能达到稳态。清除 **Enable dynamic compressibility** 参数以防止动态可压缩性建模。

## 描述

气体网络中的管道弯曲段

Pipe Bend (G) 模块表示气体网络中的弯曲管道。您可以定义管道特性以计算由于摩擦和管道曲率引起的损失。该模块使用水力损失系数对损失建模，对于可以忽略可压缩流动效应的较低速流动，结果可能更准确。

### 管道曲率损失系数

由于几何变化引起的压力损失系数包括角度修正因子 *C*angle 和弯曲系数 *C*bend：

Kloss=CangleCbend。

该模块按如下公式计算 *Cangle*：

Cangle=0.0148θ−3.9716⋅10−5θ2，

其中 *θ* 是 **Bend angle** 参数的值，以度为单位。

该模块根据基于 Crane [1] 的数据，从 90° 弯曲的弯曲半径 *r* 与管道直径 *d* 之比的表格值计算 *Cbend*：

显示 90° 管道弯曲的示意图

| *r/d* | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 20 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 20 *fT* | 14 *fT* | 12 *fT* | 12 *fT* | 14 *fT* | 17 *fT* | 24 *fT* | 30 *fT* | 34 *fT* | 38 *fT* | 42 *fT* | 50 *fT* | 58 *fT* |

该模块根据基于管道直径的表格数据插值清洁商用钢的摩擦因子 *f*T [1]。此表包含在完全湍流区域流动的清洁商用钢管道的摩擦数据。

| 公称尺寸 (mm) | 5 | 10 | 15 | 20 | 25 | 32 | 40 | 50 | 72.5 | 100 | 125 | 150 | 225 | 350 | 609.5 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 摩擦因子，*fT* | .035 | .029 | .027 | .025 | .023 | .022 | .021 | .019 | .018 | .017 | .016 | .015 | .014 | .013 | .012 |

修正因子在弯曲半径与直径之比介于 1 到 24 之间时有效。超出此范围，该模块采用最近邻外推。

### 层流中由于摩擦引起的损失

端口 **A** 和 **B** 处的流动的压力损失公式相同。

当管道中的流动为完全层流，或低于 *Re* = 2000 时，弯曲处的压力损失为

Δploss=μλ2ρId2AL2m˙port，

其中：

- *μ* 是相对湿度。
- *λ* 是 Darcy 摩擦因子常数，对于层流为 64。
- *ρI* 是内部流体密度。
- *d* 是管道直径。
- *L* 是弯曲长度段，为 **Bend radius** 和 **Bend angle** 参数的乘积：Lbend=rbendθ。
- *A* 是管道横截面积，π4d2。
- m˙port 是相应端口处的质量流量。

### 湍流中由于摩擦引起的损失

当流动为完全湍流，或大于 *Re* = 4000 时，管道中的压力损失为：

Δploss=(fDL2d+Kloss2)m˙port|m˙port|2ρIA2，

其中 *f*D 是 Darcy 摩擦因子。该模块使用经验 Haaland 方程和 **Internal surface absolute roughness** 参数近似此值。该模块对管道段的每一半取微分，即在端口 **A** 与内部节点之间，以及内部节点与端口 **B** 之间。

### 压差

该模块基于内部流体体积压力 *pI* 计算弯曲处的压力损失：

pA−pI=Δploss,A

pB−pI=Δploss,B

### 质量平衡

质量守恒将质量流量与表示气体体积的内部节点的压力和温度动态相关联。当您选中 **Enable dynamic compressibility** 时，质量平衡为

∂M∂pdpIdt+∂M∂TdTIdt=m˙A+m˙B，

其中：

- ∂M∂p 是气体体积的质量在恒定温度和体积下对压力的偏导数。
- ∂M∂T 是气体体积的质量在恒定压力和体积下对温度的偏导数。
- *pI* 是气体体积的压力。
- *TI* 是气体体积的温度。
- *t* 是时间。
- m˙A 和 m˙B 分别是端口 **A** 和 **B** 处的质量流量。当气体通过某端口流入模块时，该端口处的流量为正。

当您清除 **Enable dynamic compressibility** 复选框时，流入管道的质量流量等于流出管道的质量流量

m˙A+m˙B=0。

### 能量平衡

能量守恒将能量和热流量与表示气体体积的内部节点的压力和温度动态相关联。当您选中 **Enable dynamic compressibility** 时，能量平衡为

∂U∂pdpIdt+∂U∂TdTIdt=ΦA+ΦB，

其中：

- ∂U∂p 是气体体积的内能在恒定温度和体积下对压力的偏导数。
- ∂U∂T 是气体体积的内能在恒定压力和体积下对温度的偏导数。
- *ΦA* 和 *ΦB* 分别是端口 **A** 和 **B** 处的能量流量。

当您清除 **Enable dynamic compressibility** 复选框时，能量平衡为

ρ0cpVdTdt=ΦA+ΦB，

其中：

- *cp* 是气体比热。
- *V* 是管道体积。
- *ρ0* 是气体密度。该模块根据 **Nominal liquid temperature** 和 **Nominal liquid pressure** 参数计算此常数值。
