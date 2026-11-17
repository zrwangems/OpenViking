---
type: simulink-block
title: 'Elbow (TL)'
family: 'thermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Pipes & Fittings'
documentation_page: 'elbowtl'
documentation_source_path: 'ref/elbowtl.html'
language: zh-CN
chinese_source: worker-translation
---

# Elbow (TL)

## 端口

### 守恒

### **A** — 管道弯头入口或出口热液体

与管道弯头的液体入口或出口关联的热液体守恒端口。

### **B** — 管道弯头入口或出口热液体

与管道弯头的液体入口或出口关联的热液体守恒端口。

## 参数

### **Elbow type** — 弯曲几何形状 `Smoothly curved`（默认）| `Sharp-edged (Miter)`

管段的弯曲规格。尖锐边缘（或斜接）弯头会引入流动方向的急剧变化，例如在管道接头处，其流动损失由一组与逐渐转向管段不同的经验数据建模。

### **Elbow internal diameter** — 管道内径 `0.01 m`（默认）| 正标量

管道弯头段的内径。

### **Elbow angle** — 管道曲线角度 `90 deg`（默认）| 正标量

扫掠管道曲线的角度。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过管段的层流的上限雷诺数。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

热液体网络中的管道转弯

Elbow (TL) 模块表示热液体网络中管道转弯处的流动。该模块会计算由管道转弯引起的压力损失，但忽略黏性摩擦的影响。

有两种 **Elbow type** 设置可用：`Smoothly-curved` 和 `Sharp-edged (Miter)`。对于带 90° 弯头且考虑摩擦损失的平滑管道，也可以使用 Pipe Bend (TL) 模块。

### 损失系数

当 **Elbow type** 参数为 `Smoothly curved` 时，该模块按以下公式计算损失系数：

K=30fTCangle.

该模块根据 Keller [2] 按以下公式计算角度修正因子 *Cangle*：

Cangle=0.0148θ−3.9716⋅10−5θ2,

其中 *θ* 是 **Bend angle** 参数的值，以度为单位。该模块将摩擦因子 *f*T 定义为洁净商用钢的值。然后，该模块根据 Crane [1]，基于弯头内径对 *fT* 的值进行表格数据插值。该表包含流动处于完全湍流区时洁净商用钢管道的管道摩擦数据。

| *r/d* | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 20 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 20 *fT* | 14 *fT* | 12 *fT* | 12 *fT* | 14 *fT* | 17 *fT* | 24 *fT* | 30 *fT* | 34 *fT* | 38 *fT* | 42 *fT* | 50 *fT* | 58 *fT* |

Crane 中的值适用于直径最大到 600 毫米的情况。对于更大直径或超出此范围的壁面粗糙度，摩擦因子通过最近邻外推计算。

当 **Elbow type** 参数为 `Sharp-edged (Miter)` 时，该模块根据 Crane [1] 计算弯曲角度 *α* 的损失系数 *K*。

| *α* | 0° | 15° | 30° | 45° | 60° | 75° | 90° |
| --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 2 *fT* | 4 *fT* | 8 *fT* | 15 *fT* | 25 *fT* | 40 *fT* | 60 *fT* |

显示 Mitre 弯头以及 K 值和对应弯曲角度表格的示意图。

### 质量流量

通过管段的质量守恒：

m˙A+m˙B=0.

通过弯头的质量流量按以下公式计算：

m˙=A2ρ¯KΔp[Δp2+Δpcrit2]1/4,

其中：

- *A* 是流通面积。
- ρ¯ 是平均流体密度。
- *Δp* 是管段压差，*p*A – *p*B。

临界压差 *Δp*crit 是与 **Critical Reynolds number** *Re*crit 关联的压差，即层流与湍流之间的流态转变点：

Δpcrit=ρ¯2K(νRecritD)2,

其中

- *ν* 是流体运动黏度。
- *D* 是弯头内径。

### 能量平衡

该模块按如下方式平衡能量：

ΦA+ΦB=0,

其中：

- *ϕA* 是端口 **A** 处的能量流量。
- *ϕB* 是端口 **B** 处的能量流量。
