---
type: simulink-block
title: 'Area Change (IL)'
family: 'isothermal-liquid'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Pipes & Fittings'
documentation_page: 'areachangeil'
documentation_source_path: 'ref/areachangeil.html'
language: zh-CN
chinese_source: worker-translation
---

# Area Change (IL)

## 端口

### 守恒

### **A** — 液体端口 isothermal liquid

液体入口端口。

### **B** — 液体端口 isothermal liquid

液体出口端口。

## 参数

### **Cone angle** — 渐变面积变化角度 `30`（默认） | positive scalar

以圆锥形式参数化的渐变面积变化的扩张角。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为 `Semi-empirical correlation - gradual area change`。

### **Local loss parameterization** — 水力损失模型 `Semi-empirical correlation - sudden area change`（默认） | `Semi-empirical correlation - gradual area change` | `Tabulated data - loss coefficient vs. Reynolds number`

由面积变化引起的水力损失模型。您可以从两个解析、半经验公式中选择，也可以通过选择 `Tabulated data - loss coefficient vs. Reynolds number` 提供自己的数据。

### **Cross-sectional area at port A** — 端口 A 处的面积 `0.02 m^2`（默认） | positive scalar

截面入口（端口 **A**）处的面积。

### **Cross-sectional area at port B** — 端口 B 处的面积 `0.01 m^2`（默认） | positive scalar

截面出口（端口 **B**）处的面积。

### **Reynolds number vector** — 用于表格参数化的 Reynolds 数值向量 `[10, 20, 30, 40, 50, 100, 200, 500, 1000, 2000]`（默认） | `1-by-n vector`

用于面积变化表格参数化的 Reynolds 数值向量。其元素必须与 **Contraction loss coefficient vector** 和 **Expansion loss coefficient vector** 参数的元素一一对应。向量值按升序列出。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为 `Tabulated data - loss coefficient vs. Reynolds number`。

### **Contraction loss coefficient vector** — 面积收缩的损失系数向量 `[5, 2.7, 1.8, 1.46, 1.3, .9, .65, .42, .3, .2]`（默认） | 1-by-*n* vector

面积收缩的损失系数向量，对应 **Reynolds number vector** 参数，其中 *n* 是 **Reynolds number vector** 的长度。元素按降序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为 `Tabulated data - loss coefficient vs. Reynolds number`。

### **Expansion loss coefficient vector** — 面积扩张的损失系数向量 `[3.1, 2.3, 1.65, 1.35, 1.15, .9, .75, .65, .9, .65]`（默认） | `1-by-n vector`

面积扩张的损失系数向量，对应 **Reynolds number vector** 参数，其中 *n* 是 **Reynolds number vector** 的长度。元素按降序列出，且必须大于 0。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为 `Tabulated data - loss coefficient vs. Reynolds number`。

### **Expansion correction factor** — 半经验损失因子方程中的系数 `1`（默认） | positive scalar

用于面积扩张损失因子半经验计算的系数。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为以下任一项：

- `Semi-empirical correlation - sudden area change`
- `Semi-empirical correlation - gradual area change`

### **Contraction correction factor** — 半经验损失因子方程中的系数 `1`（默认） | positive scalar

用于面积收缩损失因子半经验计算的系数。

#### 依赖关系

要启用此参数，请将 **Local loss parameterization** 设置为以下任一项：

- `Semi-empirical correlation - sudden area change`
- `Semi-empirical correlation - gradual area change`

### **Critical Reynolds number** — 层流的上限 Reynolds 数 `150`（默认） | positive scalar

通过孔口的层流的上限 Reynolds 数。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体网络中沿管道发生的面积扩张或收缩

Area Change (IL) 模块对沿管道的突然或渐变面积变化进行建模，管道面积固定且流动方向可变。当流体从端口 **A** 流向端口 **B** 时，会经历面积收缩。当流体从端口 **B** 流向端口 **A** 时，会经历面积扩张。入口和出口面积可以相等。

可以使用半经验和表格两种公式来关联流量与损失。

### 半经验公式

在半经验解析公式中，压力和速度损失由 *水力损失系数*、*K* 表征，其取决于用户定义的 **Contraction correction factor**、*C*contraction 和 **Expansion correction factor**、*C*expansion，来自 Crane [1]。表征面积变化的系数由扩张和收缩损失因子共同计算，并基于通过该模块的流量。

对于 0 到 45 度之间的渐变圆锥形面积收缩，收缩损失因子为：

Kcontraction=0.8Ccontractionsin(θ2)(1−R),

其中 *R* 是端口面积比 AsmallerAbigger。对于 45 到 180 度之间的渐变面积收缩：

Kcontraction=Ccontraction2sin(θ2)(1−R),

其中 *θ* 是 **Cone angle**。突然面积变化的角度为 180 度。在这种情况下，损失因子按 Kcontraction=C2(1−R) 计算。

对于 0 到 45 度之间的渐变圆锥形面积扩张，扩张损失因子为：

Kexpansion=2.6Cexpansionsin(θ2)(1−R)2,

而对于 45 到 180 度之间的渐变面积扩张：

Kexpansion=Cexpansion(1−R)2。

管道变化段的水力损失系数由这些值按以下公式计算：

K=Kexpansion+Kcontraction−Kexpansion2(tanh(3m˙Am˙th)+1),

其中：

- m˙A 是通过端口 **A** 的质量流量。通过该段的质量守恒：m˙A+m˙B=0。
- m˙th 是流动反向的阈值质量流量，其基于 **Critical Reynolds number**、*Re*c：

  m˙th=RecARυρ¯Dh,

  其中：

  - *A*R 是最小段面积（**Cross-sectional area at port A** 或 **Cross-sectional area at port B**）。
  - *ν* 是流体运动黏度。
  - ρ¯ 是平均流体密度。
  - *D*h 是 *A*R 处的水力直径：Dh=4ARπ。

### 表格数据参数化

损失因子也可以使用用户提供的数据进行参数化，这些数据根据最小面积处的 Reynolds 数插值得到，而该 Reynolds 数又是 **Critical Reynolds number** 的函数

K=TLU(Re)。

数据点之间采用线性插值，超出表格边界时采用最近邻外推。

### 压差

面积变化两端的压差为

pA−pB=m˙22ρ¯AR2(1−R2)+Δploss,

其中压力损失为：

Δploss=K2ρ¯AR2m˙Am˙A2+m˙th2。
