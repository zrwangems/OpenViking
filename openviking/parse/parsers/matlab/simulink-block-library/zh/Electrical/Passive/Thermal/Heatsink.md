---
type: simulink-block
title: 'Heatsink'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Thermal'
documentation_page: 'heatsink'
documentation_source_path: 'ref/heatsink.html'
language: zh-CN
chinese_source: worker-translation
---

# Heatsink

## 端口

### 输入

### **v** — 流速物理信号

与流速关联的物理输入端口。

#### 依赖关系

要启用此端口，请将 **Convection** 设置为
`Forced - specify flow speed`。
### 守恒

### **A** — 环境温度热端口

与环境温度关联的热守恒端口。

### **C** — 壳体热端口

与壳体关联的热守恒端口。

## 参数

### 稳态

### **Parameterization** — 参数化类型 `Assume rectangular parallel fins`（默认）| `Datasheet` | `Tabulated convection and fin efficiency`

是将模块参数化为矩形平行翅片的函数、数据手册，还是表格化的对流和翅片效率。

### **Convection** — 对流类型 `Natural`（默认）| `Forced - specify flow speed`

模块是模拟自然对流，还是使用输入端口提供的对流值。

### **Fin height** — 翅片高度 `38.1e-3` `m`（默认）| 正标量

翅片的高度。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Assume
rectangular parallel fins`。

### **Fin thickness** — 翅片厚度 `6.5e-4` `m`（默认）| 正标量

翅片的厚度。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Assume
rectangular parallel fins`。

### **Fin depth** — 翅片深度 `139.7e-3` `m`（默认）| 正标量

翅片的深度。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Assume
rectangular parallel fins`。

### **Gap between fins** — 翅片间隙 `9.4e-3` `m`（默认）| 正标量

翅片之间的间隙。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Assume
rectangular parallel fins`，并将
**Convection** 设置为 `Forced - specify
flow speed`。

### **Number of fins** — 翅片数量 `11`（默认）| 正标量

翅片的数量。此参数的值必须等于或
大于 `1`。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Assume
rectangular parallel fins`。

### **Fin thermal conductivity** — 翅片热导率 `237` `W/(m*K)`（默认）| 正标量

翅片的热导率。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Assume
rectangular parallel fins`。

### **Vector of temperature rises above ambient, T** — 高于环境温度的温升向量 `[10, 30, 50, 70, 90]` `K`（默认）| 正标量向量

高于环境温度的温升向量。此参数中的值
必须为正且严格递增。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Datasheet` 或 `Tabulated
convection and fin efficiency`。

### **Vector of fluid flow speed, v** — 流体流速向量 `[0, 1, 2, 3]` `m/s`（默认）| 正标量向量

流体流速向量。此参数中的值必须为正且严格
递增。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Datasheet` 或 `Tabulated
convection and fin efficiency`，并将
**Convection** 设置为 `Forced - specify
flow speed`。

### **Corresponding heat dissipated to ambient, Q\_TLU1(T)** — 与环境温度对应的散热热量 `[6.1, 23.6, 44.5, 67.5, 92.3]` `W`（默认）| 正标量向量

根据高于环境温度的温升表格化的、散发到环境温度的热量值
向量。此参数中的值
对应于 **Vector of
temperature rises above ambient, T** 参数中的值。此
参数中的值必须为正且递增。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Datasheet`，并将
**Convection** 设置为
`Natural`。

### **Corresponding heat dissipated to ambient, Q\_TLU2(T, v)** — 与温度和流速对应的散热热量 `[6.1, 18.8, 22.8, 25.7; 23.6, 61.1, 73, 81.5; 44.5, 106.4, 125.9, 140.1; 67.5, 153.5, 180.7, 200.3; 92.3, 202.1, 236.9, 262]` `W`（默认）| 正标量向量

根据流速和高于环境温度的温升表格化的、散发到环境温度的热量值
向量。此参数中的值
对应于 **Vector of
temperature rises above ambient, T** 参数中的值。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为
`Datasheet`，并将
**Convection** 设置为 `Forced - specify
flow speed`。

### **Corresponding convective heat transfer coefficient, h\_TLU1(T)** — 与温度对应的对流换热系数 `[5.4, 7.02, 7.98, 8.68, 9.26]` `W/(m^2*K)`（默认）| 正标量向量

根据高于环境温度的温升表格化的
对流换热系数。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Tabulated
convection and fin efficiency`，并将
**Convection** 设置为
`Natural`。

### **Corresponding convective heat transfer coefficient, h\_TLU2(T, v)** — 与温度和流速对应的对流换热系数 `[5.4, 17.86, 22.17, 25.41; 7.02, 19.49, 23.8, 27.03; 7.97, 20.44, 24.75, 27.99; 8.68, 21.15, 25.46, 28.69; 9.26, 21.73, 26.04, 29.27]`（默认）| `W/(m^2*K)` | 正标量向量

根据强制对流引起的流体流速以及自然对流引起的
高于环境温度的温升表格化的
对流换热系数。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Tabulated
convection and fin efficiency`，并将
**Convection** 设置为 `Forced - specify
flow speed`。

### **Vector of convective heat transfer coefficients, h** — 对流换热系数向量 `[5, 10, 15, 20, 25, 30]` `W/(m^2*K)`（默认）| 正标量向量

对流换热系数。此参数取决于自然对流引起的温差，
以及强制对流引起的流体流速。
此参数的值必须为正且
严格递增。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Tabulated
convection and fin efficiency`。

### **Corresponding fin efficiency (percent), eff\_TLU(h)** — 与换热系数对应的翅片效率 `[96.97, 94.16, 91.53, 89.08, 86.78, 84.62]`（默认）| 正标量向量

根据不同对流换热系数表格化的
翅片效率。翅片效率是翅片实际散发的热量
除以当其全部体积均处于壳体温度时
会散发的热量。此参数取决于翅片几何形状和翅片热
导率。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Tabulated
convection and fin efficiency`。

### **Total heat exchange surface area** — 总换热表面积 `0.1171` `m^2`（默认）| 正标量

换热表面的总面积。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Tabulated
convection and fin efficiency`。

### 流体属性

要启用这些设置，请将 **Parameterization** 设置为 `Assume
rectangular parallel fins`。

### **Fluid kinematic viscosity** — 流体运动黏度 `1.51e-5` `m^2/s`（默认）| 正标量

流体的运动黏度。

### **Fluid thermal diffusivity** — 流体热扩散率 `2.07e-5` `m^2/s`（默认）| 正标量

流体的热扩散率。

### **Fluid thermal conductivity** — 流体热导率 `25e-3` `W/(m*K)`（默认）| 正标量

流体的热导率。

### **Fluid coefficient of volume thermal expansion** — 流体体积热膨胀系数 `3.3e-3` `1/K`（默认）| 正标量

流体的体积热膨胀系数。

### 动态特性

### **Heatsink mass** — 散热器质量 `0.35` `kg`（默认）| 正标量

散热器的质量。

### **Heatsink specific heat** — 散热器比热容 `437` `J/(K*kg)`（默认）| 正标量

散热器的比热容。

## 所属库

Simscape / Electrical / Passive / Thermal

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

将功率半导体的热量散发到环境温度

Heatsink 模块对散热器进行建模，该散热器将功率半导体的热量
散发出去。来自壳体的热量通过翅片传导，并
通过对流散发到环境温度。环境和工作流体
相同

您可以从数据手册、表格化的传热属性，
或假设经验对流关联式的几何结构来参数化此模块。如果将
**Convection** 参数设置为 `Forced - specify flow
speed`，则 **v** 输入端口指定流速。

### 参数化：数据手册

要从数据手册参数化 Heatsink 模块，请将
**Parameterization** 参数设置为
`Datasheet`，并同时指定 **Vector of
temperature rises above ambient, T** 和 **Corresponding heat
dissipated to ambient, Q\_TLU1(T)** 参数。

如果通过将 **Convection** 设置为
`Forced - specify flow speed` 在系统中启用强制对流，请同时指定
**Vector of temperature rises above ambient, T** 和
**Corresponding heat dissipated to ambient, Q\_TLU2(T,v)**
参数。

### 参数化：表格化对流和翅片效率

要基于作为冷却剂流速和环境温度温差函数的对流
系数，以及作为对流系数函数的翅片效率来参数化 Heatsink 模块，
请将 **Parameterization** 参数设置为
`Tabulated convection and fin efficiency`。

模块使用以下方程计算散热量：

Qdissipated=h(vfluid,ΔT)⋅Atotal⋅Eff(h)100⋅(Theatsink−Tambient)，

其中：

- `h(vfluid,ΔT)` 是根据流体流速
  （对于强制对流）和高于环境温度的温升
  表格化的对流换热系数。
- `Atotal` 是总换热
  表面积。
- `Eff(h)` 是根据不同对流换热系数
  表格化的翅片效率（以百分比值表示）。翅片效率是
  翅片实际散发的热量除以当其全部体积均处于壳体温度时
  会散发的热量。
  此值取决于翅片几何形状和翅片热导率。

### 参数化：假设矩形平行翅片

如果将 **Parameterization** 参数设置为
`Assume rectangular parallel fins`，模块使用以下
方程计算散热量：

Qdissipated=h(vfluid,ΔT)⋅Atotal⋅Eff(h)100⋅(Theatsink−Tambient)，

其中：

- h(vfluid,ΔT)=hnatural(ΔT)+hforced(vfluid)
- hnatural(ΔT)=kfluidH(0.825+0.387RaH1/6(1+(0.492Pr)9/16)8/27)2
- hforced(vfluid)=kfluidb(1(RePr2)3+1(0.664RePr0.331+3.65Re)3)−0.33
- RaH=gβναH3abs(ΔT) 是瑞利数。
- Re=b2νdabs(vfluid) 是雷诺数。
- `g = 9.81 m/s2` 是
  重力加速度。
- `β` 是流体的体积热膨胀系数。
- `ν` 是流体运动黏度。
- `α` 是流体热扩散率。
- `kfluid` 是流体热
  导率。
- `H` 是翅片高度。
- `d` 是翅片深度。
- `t` 是翅片厚度。
- `b` 是翅片间隙。

如果尺寸为 `t x d` 的一侧焊接在基座中，则以下方程
计算总换热面积：

Atotal=(2H(d+t)+dt)N。

然后以下方程计算矩形翅片的效率：

Eff(h)=100tanh(2hktH)2hktH

其中 `k` 是翅片热
导率。
