---
type: simulink-block
title: 'Elbow (G)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Gas / Pipes & Fittings'
documentation_page: 'elbowg'
documentation_source_path: 'ref/elbowg.html'
language: zh-CN
chinese_source: worker-translation
---

# Elbow (G)

## 端口
```yaml
ports:
- name: A
  summary: 入口或出口气体
  direction: unspecified
- name: B
  summary: 入口或出口气体
  direction: unspecified
```

### 守恒

### **A** — 入口或出口气体

与管道入口或出口关联的气体守恒端口。
该模块没有固有方向性。

### **B** — 入口或出口气体

与管道入口或出口关联的气体守恒端口。
该模块没有固有方向性。
## 参数
```yaml
parameters:
- name: Elbow type
  summary: 弯头几何形状 Smoothly curved（默认）| Sharp-edged (Miter)
  group: ''
- name: Elbow internal diameter
  summary: 管道内径 0.01 m（默认）| 正标量
  group: ''
- name: Elbow angle
  summary: 管道弯曲角度 90 deg（默认）| 正标量
  group: ''
- name: Laminar flow pressure ratio
  summary: 流动在层流和湍流状态之间转换时的压力比 0.999（默认）| 正标量
  group: ''
```

### **Elbow type** — 弯头几何形状 `Smoothly curved`（默认）| `Sharp-edged (Miter)`

管段的弯头规格。当您将此参数设置为
`Sharp-edged (Miter)` 时，该模块会在流动方向上引入
急剧变化，例如在管道接头处，并使用来自逐渐转弯管段的
单独经验数据集来建模流动损失。

### **Elbow internal diameter** — 管道内径 `0.01 m`（默认）| 正标量

管道弯头段的内径。

### **Elbow angle** — 管道弯曲角度 `90 deg`（默认）| 正标量

扫掠管道曲线的角度。

### **Laminar flow pressure ratio** — 流动在层流和湍流状态之间转换时的压力比 `0.999`（默认）| 正标量

气体流动在层流和湍流状态之间转换时的压力比。
## 所属库

Simscape / Fluids / Gas / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

气体网络中的管道转弯

Elbow (G) 模块对气体网络中的管道转弯中的流动进行建模。该模块计算
由管道转弯引起的压力损失，但忽略粘性摩擦的影响。该模块
使用水力损失系数对损失进行建模，对于可以忽略可压缩流动效应的
低速流动，结果可能更准确。

您可以通过将 **Elbow type** 参数分别设置为 `Smoothly
curved` 或 `Sharp-edged (Miter)` 来建模光滑弯曲或锐边管道弯头。
要对具有 90° 弯头并建模摩擦损失的
光滑管道进行建模，您也可以使用 Pipe Bend
(G) 模块。

### 损失系数

当 **Elbow type** 参数为 `Smoothly
curved` 时，该模块将损失系数计算为：

K=30fTCangle。

该模块根据 Keller [2] 计算
*Cangle*，即角度修正因子，
如下：

Cangle=0.0148θ−3.9716⋅10−5θ2，

其中 *θ* 是 **Bend
angle** 参数的值，以度为单位。该模块将摩擦系数
*f*T 定义为清洁商用
钢的值。然后，该模块根据
Crane [1] 基于 *fT* 的内径弯头直径从表格数据中插值。该表包含
在完全湍流区域流动的清洁商用钢管的管道摩擦数据。

| *r/d* | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 20 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 20 *fT* | 14 *fT* | 12 *fT* | 12 *fT* | 14 *fT* | 17 *fT* | 24 *fT* | 30 *fT* | 34 *fT* | 38 *fT* | 42 *fT* | 50 *fT* | 58 *fT* |

Crane 提供的值适用于直径最大为 600
毫米的情况。对于更大直径或超出此范围的壁面粗糙度，摩擦系数
通过最近邻外推法计算。

当 **Elbow type** 参数为 `Sharp-edged
(Miter)` 时，该模块根据
Crane [1] 计算弯头角度 *α* 的损失系数
*K*。

| *α* | 0° | 15° | 30° | 45° | 60° | 75° | 90° |
| --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 2 *fT* | 4 *fT* | 8 *fT* | 15 *fT* | 25 *fT* | 40 *fT* | 60 *fT* |

显示斜接弯头和 K 值及对应弯头角度表格的图。

### 质量流量

质量通过管段守恒

m˙A+m˙B=0。

通过弯头的质量流量为

m˙=A2ρ¯KΔp[Δp2+Δpcrit2]1/4，

其中：

- *A* 是流动面积。
- ρ¯ 是平均流体密度。
- *Δp* 是管段压力差，
  *pA* –
  *pB*。

临界压力差，
*Δpthreshold*，是层流和湍流之间
转换的阈值

Δpthreshold=pA+pb2(1−Blam)，

其中：

- *pA* 是端口
  **A** 处的压力。
- *pB* 是端口
  **B** 处的压力。
- *Blam* 是
  **Laminar flow pressure ratio** 参数的值。

### 能量平衡

该模块平衡能量使得

ΦA+ΦB=0，

其中：

- *ϕA* 是端口 **A** 处的
  能量流率。
- *ϕB* 是端口 **B** 处的
  能量流率。
