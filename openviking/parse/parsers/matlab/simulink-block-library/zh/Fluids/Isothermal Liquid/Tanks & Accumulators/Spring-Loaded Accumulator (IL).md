---
type: simulink-block
title: 'Spring-Loaded Accumulator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Tanks & Accumulators'
documentation_page: 'springloadedaccumulatoril'
documentation_source_path: 'ref/springloadedaccumulatoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Spring-Loaded Accumulator (IL)

## 端口
```yaml
ports:
- name: A
  summary: 液压守恒端口 hydraulic conserving
  direction: conserving
```

### 守恒端口

### **A** — 液压守恒端口 hydraulic conserving

与蓄能器入口相关联的液压守恒端口。如果液体流入蓄能器，则流量为正。
## 参数
```yaml
parameters:
- name: Liquid capacity
  summary: 液体容量 8e-3 m^3（默认）| 正标量
  group: ''
- name: Preload pressure
  summary: 弹簧压力 1.01325 MPa（默认）| 正标量
  group: ''
- name: Pressure at full capacity
  summary: 弹簧压力 3.01325 MPa（默认）| 正标量
  group: ''
- name: Hard stop stiffness coefficient
  summary: 比例常数 1e4 MPa/m^3（默认）| 正标量
  group: ''
- name: Enable dynamic compressibility
  summary: 流体可压缩性 on（默认）| off
  group: ''
```

### **Liquid capacity** — 液体容量 `8e-3 m^3`（默认）| 正标量

蓄能器能够容纳的液体量。

### **Preload pressure** — 弹簧压力 `1.01325 MPa`（默认）| 正标量

液体腔为空时的弹簧压力。

### **Pressure at full capacity** — 弹簧压力 `3.01325 MPa`（默认）| 正标量

液体腔达到容量时的弹簧压力。

### **Hard stop stiffness coefficient** — 比例常数 `1e4 MPa/m^3`（默认）| 正标量

硬限位接触压力相对于压入硬限位的液体体积的比例常数。硬限位用于将液体体积限制在零和液体腔容量之间。

### **Enable dynamic compressibility** — 流体可压缩性 `on`（默认）| `off`

是否对由流体可压缩性引起的流体密度变化进行建模。当您选择 **Enable dynamic compressibility** 时，除了由压力变化引起的密度变化外，还会计算由流入模块的质量流量引起的变化。在 Isothermal Liquid 库中，所有模块都将密度计算为压力的函数。
## 所属库

Simscape / Fluids / Isothermal Liquid / Tanks & Accumulators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

用于等温液体系统中能量存储的弹簧式蓄能器

该模块对等温液体网络中的弹簧充能蓄能器进行建模。该蓄能器由一个预加载弹簧和一个液体腔组成。

当蓄能器入口处的液体压力大于预加载压力时，液体进入蓄能器并压缩弹簧。液体压力降低会导致弹簧减压，并将储存的液体排入系统。当液体体积为零以及液体体积达到液体腔容量时，分离器的运动受到硬限位的限制。

入口液体阻力和弹簧特性（例如弹簧惯性和阻尼）未建模。假设弹簧压力相对于液体体积呈线性关系。如果液体流入蓄能器，则流量为正。

下图表示弹簧式蓄能器。

|  |  |
| --- | --- |
| `VL` | 蓄能器中液体的体积。 |
| `VC` | 液体腔容量 |
| `pmax` | 满容量时的压力 |
| `pI` | 液体腔中的液体压力，等于蓄能器入口处的压力。 |
| `pHS` | 硬限位接触压力。 |
| `Kstiff` | 硬限位刚度系数。 |
| `Kspring` | 弹簧增益。 |
| m˙`A` | 流入端口 A 的液体质量流量。 |
| `ρI` | 液体腔中液体的密度。 |

### 质量守恒

模块中的质量守恒为

{p˙IdρIdpIVL+ρIV˙L=m˙A,     compressibility onρ0V˙L=m˙A,                       compressibility off

其中

V˙L={p˙IKspring,            if 0 <VL<VCp˙IKspring+Kstiff,                  else

*ρ0* 是恒定液体密度。模块根据 **Preload pressure** 参数计算该值。

### 动量守恒

动量守恒由以下方程表示。

pI=pspring+pHS

其中

pspring=ppr+KspringVL

pHS={(VL−VC)Kstiff,    if VL≥VCVLKstiff,                          if VL ≤ 00,                                    else

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
