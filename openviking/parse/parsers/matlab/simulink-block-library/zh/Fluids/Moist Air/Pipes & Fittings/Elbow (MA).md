---
type: simulink-block
title: 'Elbow (MA)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Moist Air / Pipes & Fittings'
documentation_page: 'elbowma'
documentation_source_path: 'ref/elbowma.html'
language: zh-CN
chinese_source: worker-translation
---

# Elbow (MA)

## 端口
```yaml
ports:
- name: A
  summary: 入口或出口湿空气
  direction: unspecified
- name: B
  summary: 入口或出口湿空气
  direction: unspecified
```

### 守恒

### **A** — 入口或出口湿空气

与管道入口或出口相关联的湿空气守恒端口。该模块没有固有的方向性。

### **B** — 入口或出口湿空气

与管道入口或出口相关联的湿空气守恒端口。该模块没有固有的方向性。
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

管段的弯头规格。当您将此参数设置为 `Sharp-edged (Miter)` 时，该模块会引入流动方向的急剧变化，例如在管道接头处，并使用来自逐渐转弯管段的单独经验数据来建模流动损失。

### **Elbow internal diameter** — 管道内径 `0.01 m`（默认）| 正标量

管道弯头段的内径。

### **Elbow angle** — 管道弯曲角度 `90 deg`（默认）| 正标量

扫掠管道曲线的角度。

### **Laminar flow pressure ratio** — 流动在层流和湍流状态之间转换时的压力比 `0.999`（默认）| 正标量

湿空气流动在层流和湍流状态之间转换时的压力比。
## 所属库

Simscape / Fluids / Moist Air / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

### R2024b：对悬浮在湿空气流中的水滴进行建模

湿空气域中的模块现在可以对悬浮在湿空气流中的水滴进行建模。要对水滴进行建模，请在连接到湿空气网络的 Moist Air Properties (MA) 模块中选择 **Enable entrained water droplets**。

## 描述

湿空气网络中的管道转弯

Elbow (MA) 模块对湿空气网络中的管道转弯处的流动进行建模。该模块计算管道转弯引起的压力损失，但忽略粘性摩擦的影响。该模块使用水力损失系数对损失进行建模，对于可以忽略可压缩流动效应的较低速流动，结果可能更准确。

您可以通过将 **Elbow type** 参数分别设置为 `Smoothly curved` 或 `Sharp-edged (Miter)` 来建模光滑弯曲或尖锐边缘的管道弯头。要对由于摩擦而产生损失的 90° 弯曲光滑管道进行建模，您也可以使用 Pipe Bend (MA) 模块。

### 损失系数

当 **Elbow type** 参数为 `Smoothly curved` 时，该模块按以下公式计算损失系数：

K=30fTCangle。

该模块根据 Keller [2] 计算 *Cangle*，即角度修正因子，公式为

Cangle=0.0148θ−3.9716⋅10−5θ2，

其中 *θ* 是 **Bend angle** 参数的值，以度为单位。该模块将摩擦因子 *f*T 定义为清洁商用钢的值。然后，该模块根据 Crane [1] 基于弯头内径对 *f*T 的表格数据进行插值。该表包含清洁商用钢管在完全湍流区域流动时的管道摩擦数据。

| *r/d* | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 20 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 20 *fT* | 14 *fT* | 12 *fT* | 12 *fT* | 14 *fT* | 17 *fT* | 24 *fT* | 30 *fT* | 34 *fT* | 38 *fT* | 42 *fT* | 50 *fT* | 58 *fT* |

Crane 提供的值适用于直径最大至 600 毫米的情况。对于更大直径或超出此范围的壁面粗糙度，摩擦因子通过最近邻外推法计算。

当 **Elbow type** 参数为 `Sharp-edged (Miter)` 时，该模块根据 Crane [1] 计算弯曲角度 *α* 对应的损失系数 *K*。

| *α* | 0° | 15° | 30° | 45° | 60° | 75° | 90° |
| --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 2 *fT* | 4 *fT* | 8 *fT* | 15 *fT* | 25 *fT* | 40 *fT* | 60 *fT* |

展示斜接弯头以及 K 值和对应弯曲角度表格的示意图。

### 质量流量

该模块通过管段守恒质量

m˙A+m˙B=0m˙wA+m˙wB=0m˙gA+m˙gB=0m˙dA+m˙dB=0

其中下标 *w* 表示水蒸气，下标 *g* 表示示踪气体，下标 *d* 表示水滴。

通过弯头的质量流量为

m˙=A2ρ¯KΔp[Δp2+Δpcrit2]1/4，

其中：

- *A* 是流通面积。
- ρ¯ 是平均流体密度。
- *Δp* 是管段压差，*pA* – *pB*。

临界压差 *Δpthreshold* 是层流和湍流之间转换的阈值

Δpthreshold=pA+pb2(1−Blam)，

其中：

- *pA* 是端口 **A** 处的压力。
- *pB* 是端口 **B** 处的压力。
- *Blam* 是 **Laminar flow pressure ratio** 参数的值。

### 能量平衡

该模块按以下方式平衡能量

ΦA+ΦB=0，

其中：

- *ϕA* 是端口 **A** 处的能量流率。
- *ϕB* 是端口 **B** 处的能量流率。
