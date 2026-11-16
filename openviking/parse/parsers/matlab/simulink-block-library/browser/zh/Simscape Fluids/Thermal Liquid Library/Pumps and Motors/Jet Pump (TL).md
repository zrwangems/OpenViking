---
type: simulink-block
title: 'Jet Pump (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Simscape Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid Library / Pumps and Motors'
documentation_page: 'jetpumptl'
documentation_source_path: 'ref/jetpumptl.html'
language: zh-CN
chinese_source: worker-translation
---

# Jet Pump (TL)

## 端口

### 守恒

### **A** — 液体端口 thermal liquid

与动力液体入口端口关联的 thermal liquid 守恒端口。

### **S** — 液体端口 thermal liquid

与吸入液体入口端口关联的 thermal liquid 守恒端口。

### **B** — 液体端口 thermal liquid

与混合流体出口端口关联的 thermal liquid 守恒端口。

## 参数

### **Nozzle exit area** — 喷嘴出口面积 `1e-4` `m^2`（默认值）| positive scalar

喷嘴出口在其最宽截面处的横截面积。

### **Nozzle exit to throat area ratio** — 喷嘴出口与喉部面积 `0.25`（默认值）| positive scalar

喷嘴出口与喉部横截面积的特性比。

### **Diffuser inlet to outlet area ratio** — 扩压器几何比 `0.25`（默认值）| positive scalar

扩压器入口与出口横截面积的特性比。

### **Primary flow nozzle loss coefficient** — 主流摩擦损失系数 `0.05`（默认值）| positive scalar

表征动力流中因喷嘴摩擦引起的压力损失的损失系数。

### **Secondary flow entry loss coefficient** — 二次流摩擦损失系数 `0.005`（默认值）| positive scalar

表征吸入流中因吸入口摩擦引起的压力损失的损失系数。

### **Throat loss coefficient** — 喉部摩擦损失系数 `0.1`（默认值）| positive scalar

表征混合物中因喉部摩擦引起的压力损失的损失系数。

### **Diffuser loss coefficient** — 扩压器摩擦损失系数 `0.1`（默认值）| positive scalar

表征混合流中因扩压器摩擦引起的压力损失的损失系数。

### **Minimum allowable nozzle pressure** — 喷嘴出口处最小压力 `1` `Pa`（默认值）| positive scalar

喷射泵中允许的最小压力。如果喷嘴出口处的压力降至该值以下，则该模块通过将流体速度限制为最小喷嘴压力下的速度来模拟汽蚀效应。

## 所属库

Simscape / Fluids / Thermal Liquid / Pumps & Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

热液体网络中的液-液喷射泵

Jet Pump (TL) 模块对热液体网络中的液-液喷射泵进行建模。喷射泵中的动力流体和吸入流体相同。动力流体在端口 **A** 进入主喷嘴，并通过输入端口 **S** 抽吸吸入流体。在喉部混合后，合并后的流体通过扩压器膨胀，并从端口 **B** 排出。泵上的总压力变化是泵各段中摩擦和面积变化的各自贡献以及喉部动量变化之和。方程的正负号约定对应于流入喉部的正向流动。

喷射泵示意图。一种液体流过喷嘴，并从喉部和扩压器流出。另一种液体通过第二个端口向上流动以推动第一种流体。第二种流体也从扩压器流出。

### 因面积变化引起的压力变化

泵中的质量流量守恒

m˙A+m˙S+m˙B=0,

其中 m˙A 是通过端口 **A** 的质量流量，m˙S 是通过端口 **S** 的质量流量，而 m˙A 是通过端口 **B** 的质量流量。

利用质量守恒和伯努利原理，可以将泵各段上的面积变化表示为压力变化的函数。与喷嘴相关的压力变化为

Δpa,Nozzle=m˙A4ρAN2,

或 0，以较大者为准。*AN* 是 **Nozzle exit area** 参数的值，*ρ* 是流体密度。

因吸入入口处面积引起的压力变化为

Δpa,Annulus=m˙S4ρ(AT−AN)2,

或 0，以较大者为准。*AT* 是喉部的横截面积。扩压器膨胀段上的压力变化为

Δpa,Diffuser=−m˙B22ρAT2(1−a2),

其中 *a* 是 **Diffuser inlet to outlet area ratio** 参数的值。

**反向流**

在反向流情况下，该模块不对喷嘴面积对压力变化的影响进行建模，并且从喉部流经喷嘴的流体不会获得任何压力增益。此行为可确保在反向流仿真期间模块的数值稳定性。

### 因混合引起的压力变化

动力流和吸入流在喉部混合。混合引起的压力变化为

Δpmixing=m˙A2b+m˙S21−b−m˙B2ρAT,

其中 *b* 是 **Nozzle exit to throat area ratio** 参数的值，该参数在喷嘴的最大和最小横截面积之间定义。

### 因摩擦引起的压力损失

流体因喷嘴、次级吸入入口、喉部和扩压器中的摩擦而损失压力。该模块基于各段的系数以及泵不同段之间的面积或面积比计算这些损失。无论流动方向如何，摩擦都会导致压力损失。喷嘴中因摩擦引起的压力损失为

Δpf,Nozzle=KNm˙A|m˙A|2ρAN2,

其中 *KN* 是 **Primary flow nozzle loss coefficient** 参数的值。通过环形空间的吸入流中因摩擦引起的压力损失为

Δpf,Annulus=KSm˙S|m˙S|2ρ(AT−AN)2,

其中 *KS* 是 **Secondary flow entry loss coefficient** 参数的值。喉部中因摩擦引起的压力损失为

Δpf,Throat=KTm˙B|m˙B|2ρAT2,

其中 *KT* 是 **Throat loss coefficient** 参数的值。扩压器中因摩擦引起的压力损失为

Δpf,Diffuser=KDm˙B|m˙B|2ρAT2,

其中 *KD* 是 **Diffuser loss coefficient** 参数的值。该符号对应于从喉部朝向端口 **B** 的负向流动。由于该模块为流体中速度最高的区域定义损失，因此在扩压器损失方程中使用喉部面积，该面积等于扩压器入口面积。

### 喷嘴中的饱和压力

当流体中的低压区域降至蒸汽饱和压力以下时，会发生汽蚀，这会在液体中形成汽泡，并阻碍通过泵的流量进一步增加。您可以通过指定最小喷嘴压力来对该流量限制进行建模。如果流体压力大于 **Minimum allowable nozzle pressure** 参数的值，则流体速度保持恒定。在喷嘴和扩压器之间，压力变化为

pB−pN=Δpmixing+Δpf,Throat+Δpf,Diffuser−Δpa,Diffuser

或 pB−pN,min，以较小者为准。

喷嘴中的总压力变化为

pA−pN=Δpa,Nozzle+Δpf,Nozzle.

环形空间中的总压力变化为

pS−pN=Δpa,Annulus+Δpf,Annulus.

### 能量平衡

该模块按如下方式平衡能量

ϕA+ϕB+ϕS=0,

其中：

- *ϕA* 是端口
  **A** 处的能量流率。
- *ϕB* 是端口
  **B** 处的能量流率。
- *ϕS* 是端口
  **S** 处的能量流率。

### 假设和限制

- 动力液体和吸入液体相同。
- 喉部中的混合均匀且完全。
- 喷嘴入口远大于喷嘴出口，并且吸入射流环隙远小于吸入入口。
- 对于反向流，该模块不对因喷嘴引起的压力变化进行建模。
- 该模块将汽蚀的任何影响建模为喉部流量的最大限制。
- 流动是绝热的。
