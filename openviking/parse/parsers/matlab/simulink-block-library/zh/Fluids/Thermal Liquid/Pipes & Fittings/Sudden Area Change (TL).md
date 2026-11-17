---
type: simulink-block
title: 'Sudden Area Change (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Pipes & Fittings'
documentation_page: 'suddenareachangetl'
documentation_source_path: 'ref/suddenareachangetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Sudden Area Change (TL)

## 端口

### 守恒端口

### **A** — 截面入口热液体

面积变化截面的流体入口或出口点。

### **B** — 截面入口热液体

面积变化截面的流体入口或出口点。

## 参数

### **局部损失参数化** — 流量损失计算方法 `Semi-empirical`（默认）| `Tabulated data - loss coefficient vs. Reynolds number`

用于计算突扩面积变化引起的损失系数的参数化方法。选择 `Semi-empirical formulation` 可根据端口 **A** 和 **B** 处的横截面积自动计算损失系数。选择 `Tabulated data - Loss coefficient vs. Reynolds number` 可指定一个一维查找表，用于根据流动雷诺数确定损失系数。

### **端口 A 处的横截面积** — A 处的入口面积 `0.02` `m^2`（默认）| 正标量

入口 **A** 处垂直于流动方向的面积。该值必须大于 **B** 处的横截面积。

### **端口 B 处的横截面积** — B 处的入口面积 `0.01` `m^2`（默认）| 正标量

**B** 处垂直于流动方向的面积。该值必须小于 **A** 处的横截面积。

### **临界雷诺数** — 与截面中最小面积相关的过渡雷诺数 `150`（默认）| 正标量

在突扩面积变化的收缩部分中，流动在层流和湍流状态之间过渡时的雷诺数。仅当 **损失系数设定** 参数设置为 `Semi-empirical formulation` 时，此参数才可见。

### **收缩修正因子** — 损失系数缩放因子 `1`（默认）| 正标量

用于调整突扩面积变化收缩部分损失系数值的缩放因子。该模块将根据半经验表达式计算得到的损失系数乘以该因子。仅当 **损失系数设定** 参数设置为 `Semi-empirical formulation` 时，此参数才可见。

### **膨胀修正因子** — 损失系数缩放因子 `1`（默认）| 正标量

用于调整突扩面积变化膨胀部分损失系数值的缩放因子。该模块将根据半经验表达式计算得到的损失系数乘以该因子。仅当 **损失系数设定** 参数设置为 `Semi-empirical formulation` 时，此参数才可见。

### **雷诺数向量** — 用于表格参数化的雷诺数向量 `[10, 20, 30, 40, 50, 100, 200, 500, 1000, 2000]`（默认）| 向量

用于损失系数表格参数化的雷诺数向量。在这些雷诺数下指定 **收缩损失系数向量** 和 **膨胀损失系数向量** 参数。

仅当 **损失系数设定** 参数设置为 `Tabulated data - Loss coefficient vs. Reynolds number` 时，此参数才可见。

### **收缩损失系数向量** — 用于表格参数化的损失系数向量 `[4, 2.7, 1.8, 1.46, 1.3, .9, .65, .42, .3, .2]`（默认）| 1×*n* 向量

面积变化收缩部分的损失系数向量。在 **雷诺数向量** 参数中的雷诺数处指定损失系数。该模块使用雷诺数向量和损失系数向量构建一维查找表。

仅当 **损失系数设定** 参数设置为 `Tabulated data — Loss coefficient vs. Reynolds number` 时，此参数才可见。

### **膨胀损失系数向量** — 用于表格参数化的损失系数向量 `[4, 2.3, 1.65, 1.35, 1.15, .9, .75, .65, .9, .65]`（默认）| 1×*n* 向量

面积变化膨胀部分的损失系数向量。在 **雷诺数向量** 参数中的雷诺数处指定损失系数。该模块使用雷诺数向量和损失系数向量构建一维查找表。

仅当 **损失系数设定** 参数设置为 `Tabulated data — Loss coefficient vs. Reynolds number` 时，此参数才可见。

## 所属库

Simscape / Fluids / Thermal Liquid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

流动面积的突扩或突缩

Sudden Area Change (TL) 模块用于对流动横截面积突然变化引起的局部压力损失进行建模。该面积变化表现为从端口 **A** 到端口 **B** 的收缩，以及从端口 **B** 到端口 **A** 的膨胀。该组件是绝热的。它不与周围环境进行热交换。

**突扩面积变化示意图**

突扩过程中的压降主要归因于膨胀区中的湍流混合。突缩过程中的压降主要归因于收缩区入口处的流动分离。图中显示了突扩面积变化的膨胀区和收缩区。

### 质量平衡

突扩面积变化中的质量守恒方程为

m˙A+m˙B=0，

其中：

- m˙A 和 m˙B 分别是通过端口 A 和 B 流入突扩面积变化的质量流量。

### 动量平衡

突扩面积变化中的动量守恒方程为

pA−pB=m˙22ρ(1SB2−1SA2)+ϕLoss，

其中：

- *p*A 和 *p*B 分别是端口 A 和 B 处的压力。
- m˙ 是平均质量流量。
- *ρ* 是平均流体密度。
- *S*A 和 *S*B 分别是端口 A 和 B 处的流动横截面积。
- *Φ*Loss 是由于突扩面积变化引起的机械能损失。

机械能损失为

ϕLoss=KLossm˙22ρSB2，

其中：

- *K*Loss 是损失系数。

如果 **损失系数设定** 参数设置为 `Semi-empirical formulation`，则突扩的损失系数计算为

KLoss=Ke(1−SBSA)2，

而突缩的损失系数计算为

KLoss=Kc2(1−SBSA)，

其中：

- *K*e 是膨胀区中的修正因子。
- *K*c 是收缩区中的修正因子。

在突扩与突缩行为之间的过渡区中，该模块对损失系数进行平滑处理

KLoss=Ke(1−SBSA)2+λ2[Kc2(1−SBSA)−Ke(1−SBSA)2]，

其中

λ=tanh(3m˙am˙Cr)+1，

其中 *ṁCr* 是流动反向的阈值质量流量，

m˙Cr=ReCrμπ4SB。

如果 **损失系数设定** 参数设置为 `Tabulated data — Loss coefficient vs. Reynolds number`，则该模块从作为雷诺数函数提供的表格数据中获取损失系数。

### 能量平衡

突扩面积变化中的能量守恒方程为

ϕA+ϕB=0，

其中：

- *Φ*A 和 *Φ*B 分别是通过端口 A 和 B 流入突扩面积变化的能量流量。
