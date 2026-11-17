---
type: simulink-block
title: 'Elbow (G)'
family: 'gas'
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

### 守恒

### **A** — 入口或出口气体

与管道入口或出口关联的气体守恒端口。
此模块没有固有方向性。

### **B** — 入口或出口气体

与管道入口或出口关联的气体守恒端口。
此模块没有固有方向性。

## 参数

### **Elbow type** — 弯头几何形状 `Smoothly curved` （默认） | `Sharp-edged (Miter)`

管道段的弯头规格。当您将此参数设置为
`Sharp-edged (Miter)` 时，模块会引入流动方向的急剧变化，例如在管道接头处，并使用一组不同于逐渐转弯管道段的经验数据来模拟流动损失。

### **Elbow internal diameter** — 管道内径 `0.01 m` （默认） | positive scalar

管道弯头段的内径。

### **Elbow angle** — 管道弯管角度 `90 deg` （默认） | positive scalar

扫掠管道曲线的角度。

### **Laminar flow pressure ratio** — 流动在层流和湍流状态之间转换时的压力比 `0.999` （默认） | positive scalar

气体流动在层流和湍流状态之间转换时的压力比。

## 所属库

Simscape / Fluids / Gas / Pipes & Fittings

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

气体网络中的管道转弯

Elbow (G) 模块对气体网络中管道转弯处的流动进行建模。该模块计算由管道转弯造成的压力损失，但忽略黏性摩擦的影响。该模块使用水力损失系数对损失进行建模，对于可忽略可压缩流动效应的较低速流动，其结果可能更准确。

您可以通过将 **Elbow type** 参数分别设置为 `Smoothly curved` 或 `Sharp-edged (Miter)`，来对平滑弯曲或尖锐边缘的管道弯头进行建模。要对带 90° 弯头且对由摩擦造成的损失进行建模的光滑管道进行建模，您还可以使用 Pipe Bend (G) 模块。

### 损失系数

当 **Elbow type** 参数为 `Smoothly curved` 时，模块按如下公式计算损失系数：

K=30fTCangle.

模块根据 Keller [2] 按如下公式计算角度修正因子
*Cangle*：

Cangle=0.0148θ−3.9716⋅10−5θ2,

其中 *θ* 是 **Bend angle** 参数的值，单位为 degrees。模块将摩擦因子
*f*T 定义为洁净商用钢管的值。然后，模块根据弯头内径，基于
Crane [1] 从表格数据中插值得到 *fT* 的值。此表包含流动处于完全湍流区时洁净商用钢管的管道摩擦数据。

| *r/d* | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 20 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 20 *fT* | 14 *fT* | 12 *fT* | 12 *fT* | 14 *fT* | 17 *fT* | 24 *fT* | 30 *fT* | 34 *fT* | 38 *fT* | 42 *fT* | 50 *fT* | 58 *fT* |

Crane 提供的值适用于直径最大为 600 millimeters 的情况。对于更大直径或超出此范围的壁面粗糙度，摩擦因子通过最近邻外推计算。

当 **Elbow type** 参数为 `Sharp-edged (Miter)` 时，模块根据 Crane [1] 计算弯管角度 *α* 的损失系数
*K*。

| *α* | 0° | 15° | 30° | 45° | 60° | 75° | 90° |
| --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 2 *fT* | 4 *fT* | 8 *fT* | 15 *fT* | 25 *fT* | 40 *fT* | 60 *fT* |

显示斜接弯管以及 K 值和相应弯管角度表格的示意图。

### 质量流量

质量通过管道段守恒

m˙A+m˙B=0.

通过弯头的质量流量为

m˙=A2ρ¯KΔp[Δp2+Δpcrit2]1/4,

其中：

- *A* 是流通面积。
- ρ¯ 是平均流体密度。
- *Δp* 是管道段压差，*pA* – *pB*。

临界压差 *Δpthreshold* 是层流和湍流之间转换的阈值

Δpthreshold=pA+pb2(1−Blam),

其中：

- *pA* 是端口 **A** 处的压力。
- *pB* 是端口 **B** 处的压力。
- *Blam* 是 **Laminar flow pressure ratio** 参数的值。

### 能量平衡

模块按如下方式平衡能量

ΦA+ΦB=0,

其中：

- *ϕA* 是端口 **A** 处的能量流率。
- *ϕB* 是端口 **B** 处的能量流率。
