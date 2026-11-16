---
type: simulink-block
title: 'Elbow (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pipes & Fittings'
documentation_page: 'elbowil'
documentation_source_path: 'ref/elbowil.html'
language: zh-CN
chinese_source: worker-translation
---

# Elbow (IL)

## 端口

### 守恒

### **A** — 液体端口（等温液体）

液体进入或离开管段的端口。

### **B** — 液体端口（等温液体）

液体进入或离开管段的端口。

## 参数

### **弯头类型** — 弯头几何形状 `Smoothly curved`（默认）| `Sharp-edged (Miter)`

管段的弯头规格。锐边（或斜接）弯头会在流动方向上引入急剧变化，例如在管道接头处，其流动损失通过一组与逐渐转向管段不同的经验数据来建模。

### **弯头内径** — 管道内径 `0.01 m`（默认）| positive scalar

管道弯头段的内径。

### **弯头角度** — 管道曲线角度 `90 deg`（默认）| positive scalar

扫掠管道曲线的角度。

### **临界雷诺数** — 层流的上雷诺数限值 `150`（默认）| positive scalar

通过管段的层流的上雷诺数限值。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体网络中的管道转弯

Elbow (IL) 模块对等温液体网络中的管道转弯处的流动进行建模。计算由管道转弯引起的压力损失，但忽略黏性摩擦的影响。

有两种 **弯头类型** 设置可用：`Smoothly-curved` 和 `Sharp-edged (Miter)`。对于具有 90o 弯头且对摩擦损失建模的光滑管道，也可以使用 Pipe Bend (IL) 模块。

### 损失系数

当 **弯头类型** 参数为 `Smoothly curved` 时，模块按如下公式计算损失系数：

K=30fTCangle.

模块根据 Keller [2] 计算 *Cangle*，即角度修正因子：

Cangle=0.0148θ−3.9716⋅10−5θ2,

其中 *θ* 是 **弯头角度** 参数的值，单位为 degrees。模块将摩擦因子 *f*T 定义为洁净商业钢管的值。然后，模块根据 Crane [1] 基于弯头内径对 *fT* 的表格数据进行插值。该表包含洁净商业钢管在完全湍流区流动时的管道摩擦数据。

| *r/d* | 1 | 1.5 | 2 | 3 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 20 | 24 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 20 *fT* | 14 *fT* | 12 *fT* | 12 *fT* | 14 *fT* | 17 *fT* | 24 *fT* | 30 *fT* | 34 *fT* | 38 *fT* | 42 *fT* | 50 *fT* | 58 *fT* |

Crane 提供的值适用于直径最大为 600 millimeters 的情况。对于更大直径或超出此范围的壁面粗糙度，摩擦因子通过最近邻外推计算。

当 **弯头类型** 参数为 `Sharp-edged (Miter)` 时，模块根据 Crane [1] 计算弯头角度 *α* 的损失系数 *K*。

| *α* | 0° | 15° | 30° | 45° | 60° | 75° | 90° |
| --- | --- | --- | --- | --- | --- | --- | --- |
| *K* | 2 *fT* | 4 *fT* | 8 *fT* | 15 *fT* | 25 *fT* | 40 *fT* | 60 *fT* |

显示斜接弯头和 K 值及相应弯头角度表格的图。

### 质量流量

质量通过管段守恒：

m˙A+m˙B=0.

通过弯头的质量流量计算如下：

m˙=A2ρ¯KΔp[Δp2+Δpcrit2]1/4,

其中：

- *A* 是流动面积。
- ρ¯ 是平均流体密度。
- *Δp* 是管段压差，*p*A – *p*B。

临界压差 *Δp*crit 是与 **临界雷诺数** *Re*crit 相关的压差，*Re*crit 是层流与湍流之间的流态转变点：

Δpcrit=ρ¯2K(νRecritD)2,

其中

- *ν* 是流体运动黏度。
- *D* 是弯头内径。
