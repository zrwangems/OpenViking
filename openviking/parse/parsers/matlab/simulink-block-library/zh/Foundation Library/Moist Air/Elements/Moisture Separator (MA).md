---
type: simulink-block
title: 'Moisture Separator (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'moistureseparatorma'
documentation_source_path: 'ref/moistureseparatorma.html'
language: zh-CN
chinese_source: worker-translation
---

# Moisture Separator (MA)

## 端口
```yaml
ports:
- name: W
  summary: 去除的水蒸气速率，kg/s 物理信号
  direction: output
- name: D
  summary: 去除的水滴速率，kg/s 物理信号
  direction: output
- name: A
  summary: 入口或出口湿空气
  direction: output
- name: B
  summary: 入口或出口湿空气
  direction: output
```

### 输出

### **W** — 去除的水蒸气速率，kg/s 物理信号

输出去除的水蒸气速率的物理信号，单位为 kg/s。

### **D** — 去除的水滴速率，kg/s 物理信号

输出去除的水滴速率的物理信号，单位为 kg/s。
### 守恒

### **A** — 入口或出口湿空气

与水分分离器入口或出口相关联的湿空气守恒端口。该模块没有固有方向性。

### **B** — 入口或出口湿空气

与水分分离器入口或出口相关联的湿空气守恒端口。该模块没有固有方向性。
## 参数
```yaml
parameters:
- name: Fraction of water vapor removed
  summary: 水蒸气去除比例 0.5（默认）| [0,1] 范围内的标量
  group: ''
- name: Removed water vapor condensed to liquid
  summary: 是否将去除的水蒸气冷凝为液体 off（默认）| on
  group: ''
- name: Fraction of water droplets removed
  summary: 水滴去除比例 0.5（默认）| [0,1] 范围内的标量
  group: ''
- name: Nominal pressure drop
  summary: 额定工况下的压降 0.001 MPa（默认）| 标量
  group: ''
- name: Nominal mass flow rate
  summary: 额定工况下的质量流量 0.1 kg/s（默认）| 正标量
  group: ''
- name: Nominal density
  summary: 额定工况下的密度 0 kg/m^3（默认）| 正标量
  group: ''
- name: Cross-sectional area at ports A and B
  summary: 端口处的流通面积 0.01 m^2（默认）| 正标量
  group: ''
- name: Fraction of nominal mixture mass flow rate for laminar flow transition
  summary: 阈值与额定质量流量之比 1e-3（默认）| 正标量
  group: ''
```

### **Fraction of water vapor removed** — 水蒸气去除比例 `0.5`（默认）| [0,1] 范围内的标量

从流经该模块的湿空气中去除的水蒸气比例。

### **Removed water vapor condensed to liquid** — 是否将去除的水蒸气冷凝为液体 `off`（默认）| `on`

将去除的水蒸气冷凝为液体的选项。当您选中此复选框时，模块会在去除水蒸气之前将其转换为液体，这意味着水蒸气的潜热保留在流体中。在这种情况下，模块两端的温度变化可能更为显著。

### **Fraction of water droplets removed** — 水滴去除比例 `0.5`（默认）| [0,1] 范围内的标量

从流经该模块的湿空气中去除的水滴比例。

### **Nominal pressure drop** — 额定工况下的压降 `0.001 MPa`（默认）| 标量

额定工况下从入口到出口的压降。模块使用额定参数来计算压降与质量流量之间的比例常数。

### **Nominal mass flow rate** — 额定工况下的质量流量 `0.1 kg/s`（默认）| 正标量

额定工况下通过该模块的空气混合物质量流量。模块使用额定参数来计算压降与质量流量之间的比例常数。

### **Nominal density** — 额定工况下的密度 `0 kg/m^3`（默认）| 正标量

额定工况下流动阻力内部湿空气混合物的质量密度。模块使用额定参数来计算压降与质量流量之间的比例常数。将此参数设置为零以忽略压降对空气混合物密度的依赖性。

### **Cross-sectional area at ports A and B** — 端口处的流通面积 `0.01 m^2`（默认）| 正标量

分离器端口处的流通面积。模块假定各端口尺寸相同。

### **Fraction of nominal mixture mass flow rate for laminar flow transition** — 阈值与额定质量流量之比 `1e-3`（默认）| 正标量

空气混合物阈值质量流量与额定质量流量之比。模块使用此参数来设置压降线性化的阈值。
## 所属库

Simscape / Foundation Library / Moist Air / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

从湿空气流中去除水蒸气和液滴

Moisture Separator (MA) 模块在湿空气网络中从通过该模块的流体中去除指定比例的水蒸气和液滴。该模块假设去除水分的方法为机械方法，并且流体在端口之间的温度变化可忽略不计。

如果 **Nominal density** 参数 *ρnom* 大于零，则压降为

pA−pB=K1m˙Am˙A2+(flamm˙nom)2RTinpin

其中：

- *ṁA* 是端口 **A** 处的质量流量。
- *ṁnom* 是 **Nominal mass flow rate** 参数的值。
- *flam* 是层流过渡的标称混合物流量质量流量的比例。
- *pin* 是入口压力，*p*A 或 *pB*，取决于流动方向。
- *Tin* 是入口温度，*T*A 或 *TB*，取决于流动方向。
- *R* 是比气体常数。

比例常数 *K1* 为

K1=Δpnomρnomm˙nom2

其中 *ρnom* 是 **Nominal density** 参数的值，*Δpnom* 是 **Nominal pressure drop** 参数的值。

如果 **Nominal density** 参数为零，则压降为

pA−pB=K2m˙Am˙A2+(flamm˙nom)2

其中比例常数 *K1* 为

K2=Δpnomm˙nom2

由于该模块假设流动阻力为绝热，混合物比总焓相等，

hA+12(m˙ARTASpA)2=hB+12(m˙BRTBSpB)2

其中：

- *hA* 和 *hB* 分别是端口 **A** 和 **B** 处的比焓。
- *S* 是 **Cross-sectional area at ports A and B** 参数的值。

### 质量和能量平衡

湿空气、水蒸气、示踪气体和液滴的质量平衡方程为

m˙A+m˙B−m˙w,removed=0m˙wA+m˙wB−m˙w,removed=0m˙gA+m˙gB=0m˙dA+m˙dB−m˙d,removed=0

其中：

- *ṁwA* 和 *ṁwB* 分别是端口 **A** 和 **B** 处的水蒸气质量流量。
- *ṁgA* 和 *ṁgB* 分别是端口 **A** 和 **B** 处的示踪气体质量流量。
- *ṁdA* 和 *ṁdB* 分别是端口 **A** 和 **B** 处的液滴质量流量。

水蒸气去除率为

m˙w,removed=θwm˙MA,inxw,in,

其中：

- *θw* 是 **Fraction of water vapor removed** 参数的值。
- *ṁMA,in* 是流入端口的湿空气质量流量，该端口可以是端口 **A** 或 **B**。
- *xw,in* 是流入端口处的水蒸气质量分数，该端口可以是端口 **A** 或 **B**。

液滴去除率为

m˙d,removed=θdm˙MA,inrd,in,

其中：

- *θd* 是 **Fraction of water droplets removed** 参数的值。
- *rd,in* 是流入端口处液滴与湿空气的质量比，该端口可以是端口 **A** 或 **B**。

能量平衡方程为

ΦA+ΦB−Φremoved=0,

其中 *ΦA* 和 *ΦB* 分别是流经端口 **A** 和 **B** 的能量流率。

*Φremoved* 是去除的水蒸气和液滴的能量流率。该项不代表热量或功，仅包含去除的水蒸气和液滴的比焓贡献，

Φremoved=m˙w,removedhw,in+m˙d,removedhd,in,

其中 *hw,in* 和 *hd,in* 是流入端口处的水蒸气和液滴比焓。

### 假设和限制

该模块不对与去除水蒸气和液滴相关的任何物理或热力学效应进行建模。
