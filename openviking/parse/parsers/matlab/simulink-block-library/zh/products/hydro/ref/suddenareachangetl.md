---
type: simulink-block
title: 'Sudden Area Change (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Pipes and Fittings'
documentation_page: 'suddenareachangetl'
documentation_source_path: 'ref/suddenareachangetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Sudden Area Change (TL)

## 端口

### 守恒

### **A** — 截面入口热液体

流体进入或离开面积变化段的入口或出口点。

### **B** — 截面入口热液体

流体进入或离开面积变化段的入口或出口点。

## 参数

### **Local loss parameterization** — 流动损失计算方法 `Semi-empirical`（默认） | `Tabulated data - loss coefficient vs. Reynolds number`

用于计算由于突然面积变化引起的损失系数的参数化方法。选择 `Semi-empirical formulation`，以根据端口 **A** 和 **B** 处的横截面积自动计算损失系数。选择 `Tabulated data - Loss coefficient vs. Reynolds number`，以指定损失系数相对于流动雷诺数的一维查找表。

### **Cross-sectional area at port A** — 在 A 处的入口面积 `0.02` `m^2`（默认） | 正标量

端口 **A** 处垂直于流动方向的面积。此值必须大于 **B** 处的横截面积。

### **Cross-sectional area at port B** — 在 B 处的入口面积 `0.01` `m^2`（默认） | 正标量

端口 **B** 处垂直于流动方向的面积。此值必须小于 **A** 处的横截面积。

### **Critical Reynolds number** — 与截面中最小面积相关的过渡雷诺数 `150`（默认） | 正标量

在突然面积变化的收缩部分中，流动在层流和湍流状态之间转变时的雷诺数。仅当 **Loss coefficient specification** 参数设置为 `Semi-empirical formulation` 时，此参数可见。

### **Contraction correction factor** — 损失系数缩放因子 `1`（默认） | 正标量

用于调整突然面积变化收缩部分损失系数值的缩放因子。模块将根据半经验表达式计算出的损失系数因子乘以该因子。仅当 **Loss coefficient specification** 参数设置为 `Semi-empirical formulation` 时，此参数可见。

### **Expansion correction factor** — 损失系数缩放因子 `1`（默认） | 正标量

用于调整突然面积变化扩张部分损失系数值的缩放因子。模块将根据半经验表达式计算出的损失系数因子乘以该因子。仅当 **Loss coefficient specification** 参数设置为 `Semi-empirical formulation` 时，此参数可见。

### **Reynolds number vector** — 用于表格化参数化的雷诺数向量 `[10, 20, 30, 40, 50, 100, 200, 500, 1000, 2000]`（默认） | 向量

用于损失系数表格化参数化的雷诺数向量。在这些雷诺数处指定 **Contraction loss coefficient vector** 和 **Expansion loss coefficient vector** 参数。

仅当 **Loss coefficient specification** 参数设置为 `Tabulated data - Loss coefficient vs. Reynolds number` 时，此参数可见。

### **Contraction loss coefficient vector** — 用于表格化参数化的损失系数向量 `[4, 2.7, 1.8, 1.46, 1.3, .9, .65, .42, .3, .2]`（默认） | 1-by-*n* 向量

用于面积变化收缩部分的损失系数向量。在 **Reynolds number vector** 参数中的雷诺数处指定损失系数。模块使用雷诺数和损失系数向量构造一维查找表。

仅当 **Loss coefficient specification** 参数设置为 `Tabulated data — Loss coefficient vs. Reynolds number` 时，此参数可见。

### **Expansion loss coefficient vector** — 用于表格化参数化的损失系数向量 `[4, 2.3, 1.65, 1.35, 1.15, .9, .75, .65, .9, .65]`（默认） | 1-by-*n* 向量

用于面积变化扩张部分的损失系数向量。在 **Reynolds number vector** 参数中的雷诺数处指定损失系数。模块使用雷诺数和损失系数向量构造一维查找表。

仅当 **Loss coefficient specification** 参数设置为 `Tabulated data — Loss coefficient vs. Reynolds number` 时，此参数可见。

## 所属库

Simscape / Fluids / Thermal Liquid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

流动面积的突然扩张或收缩

Sudden Area Change (TL) 模块对由于流动横截面积突然变化引起的局部压力损失进行建模。面积变化是从端口 **A** 到端口 **B** 的收缩，以及从端口 **B** 到端口 **A** 的扩张。该组件是绝热的。它不与周围环境交换热量。

**突然面积变化示意图**

突然扩张导致的压降主要归因于扩张区中的湍流混合。突然收缩导致的压降主要归因于收缩区入口处的流动分离。图中显示了突然面积变化的扩张区和收缩区。

### 质量平衡

突然面积变化中的质量守恒方程为

m˙A+m˙B=0,

其中：

- m˙A 和 m˙B 是经过端口 A 和 B 进入突然面积变化的质量流量。

### 动量平衡

突然面积变化中的动量守恒方程为

pA−pB=m˙22ρ(1SB2−1SA2)+ϕLoss,

其中：

- *p*A 和 *p*B 是端口 A 和 B 处的压力。
- m˙ 是平均质量流量。
- *ρ* 是平均流体密度。
- *S*A 和 *S*B 是端口 A 和 B 处的流动横截面积。
- *Φ*Loss 是由于突然面积变化引起的机械能损失。

机械能损失为

ϕLoss=KLossm˙22ρSB2,

其中：

- *K*Loss 是损失系数。

如果 **Loss coefficient specification** 参数设置为 `Semi-empirical formulation`，则突然扩张的损失系数计算为

KLoss=Ke(1−SBSA)2,

而突然收缩的损失系数计算为

KLoss=Kc2(1−SBSA),

其中：

- *K*e 是扩张区中的修正因子。
- *K*c 是收缩区中的修正因子。

在突然扩张和突然收缩行为之间的过渡区，模块对损失系数进行平滑处理

KLoss=Ke(1−SBSA)2+λ2[Kc2(1−SBSA)−Ke(1−SBSA)2],

其中

λ=tanh(3m˙am˙Cr)+1,

其中 *ṁCr* 是流动反向的阈值质量流量，

m˙Cr=ReCrμπ4SB.

如果 **Loss coefficient specification** 参数设置为 `Tabulated data — Loss coefficient vs. Reynolds number`，则模块从作为雷诺数函数提供的表格数据中获得损失系数。

### 能量平衡

突然面积变化中的能量守恒方程为

ϕA+ϕB=0,

其中：

- *Φ*A 和 *Φ*B 是经过端口 A 和 B 进入突然面积变化的能量流率。
