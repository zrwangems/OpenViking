---
type: simulink-block
title: 'Gas-Charged Accumulator (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Tanks & Accumulators'
documentation_page: 'gaschargedaccumulatoril'
documentation_source_path: 'ref/gaschargedaccumulatoril.html'
language: zh-CN
chinese_source: worker-translation
---

# Gas-Charged Accumulator (IL)

## 端口
```yaml
ports:
- name: A
  summary: 液体端口，等温液体
  direction: conserving
```

### 守恒端口

### **A** — 液体端口，等温液体

与蓄能器入口关联的等温液体端口。如果液体流入蓄能器，则流量为正。
## 参数
```yaml
parameters:
- name: Total accumulator volume
  summary: 蓄能器容积 8e-3 m^3（默认）| 正标量
  group: ''
- name: Minimum gas volume
  summary: 气体腔死容积 4e-5 m^3（默认）| 正标量
  group: ''
- name: Precharge pressure
  summary: 气体腔压力 1.101325 MPa（默认）| 正标量
  group: ''
- name: Specific heat ratio
  summary: 比热比 1.4（默认）| 正标量
  group: ''
- name: Hard stop stiffness coefficient
  summary: 比例常数 1e4 MPa/m^3（默认）| 正标量
  group: ''
- name: Enable dynamic compressibility
  summary: 流体可压缩性 on（默认）| off
  group: ''
```

### **Total accumulator volume** — 蓄能器容积 `8e-3` `m^3`（默认）| 正标量

蓄能器的总容积，包括液体腔和气体腔。它是液体腔容量与最小气体容积之和。

### **Minimum gas volume** — 气体腔死容积 `4e-5` `m^3`（默认）| 正标量

气体腔死容积，定义为当液体腔充满时气体腔中仍然充满气体的一小部分容积。当液体腔达到容量时，该模块需要一个非零值以避免除零错误。

### **Precharge pressure** — 气体腔压力 `1.101325` `MPa`（默认）| 正标量

当液体腔为空时气体腔中的压力。

### **Specific heat ratio** — 比热比 `1.4`（默认）| 正标量

比热比（绝热指数）。为了考虑热交换，将其设置为通常在 1 到 2 之间的值，具体取决于气体腔中气体的性质。对于 20°C 的干燥空气，该值在等温过程中为 1，在绝热（及等熵）过程中为 1.4。

### **Hard stop stiffness coefficient** — 比例常数 `1e4` `MPa/m^3`（默认）| 正标量

硬止挡接触压力相对于渗入硬止挡的液体体积的比例常数。硬止挡用于将液体体积限制在零和液体腔容量之间。

### **Enable dynamic compressibility** — 流体可压缩性 `on`（默认）| `off`

是否对由流体可压缩性引起的流体密度变化进行建模。当您选择 **Enable dynamic compressibility** 时，除了由于压力变化引起的密度变化外，还会计算由于流入模块的质量流量引起的变化。在等温液体库中，所有模块都将密度计算为压力的函数。
## 所属库

Simscape / Fluids / Isothermal Liquid / Tanks & Accumulators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体网络中的充气式蓄能器

Gas-Charged Accumulator (IL) 模块表示等温液体网络中的充气式蓄能器。蓄能器由一个预充气气体腔和一个液体腔组成。两个腔由气囊、活塞或任何类型的隔膜隔开。

当蓄能器入口处的液体压力大于预充压力时，液体进入蓄能器并通过多变过程压缩气体。液体压力降低会导致气体膨胀并将储存的液体排入系统。当液体体积为零以及液体体积达到液体腔容量时，隔膜运动受到硬止挡的限制。液体腔容量是蓄能器总容积减去最小气体容积。

入口液体阻力以及隔膜特性（如惯性和阻尼）未建模。如果液体流入蓄能器，则流量为正。

此图表示一个充气式蓄能器。蓄能器总容积 `VT` 由垂直隔膜分为左侧的液体腔和右侧的气体腔。左侧与隔膜之间的距离定义液体体积 `VL`。右侧与隔膜之间的距离定义气体体积 `VG`。液体腔容量 `VC` 小于蓄能器总容积，因此气体体积永远不会变为零：

VL=VT−VGVC=VT−Vdead

其中：

- *VT* 是蓄能器的总容积，包括液体腔和气体腔。
- *VL* 是蓄能器中液体的体积。
- *VG* 是蓄能器中气体的体积。
- *VC* 是液体腔容量。
- *Vdead* 是气体腔死容积，即当液体腔达到容量时气体腔中仍然充满气体的一小部分。

硬止挡接触压力用刚度项和阻尼项建模。当前状态与预充状态之间气体压力和气体体积的关系是多变的，并且在隔膜处压力平衡：

pGVGksh=pprVTksh，

其中：

- *pG* 是气体腔中的气体压力。
- *ppr* 是当液体腔为空时气体腔中的压力
- *ksh* 是比热比（绝热指数）。

### 质量守恒

模块中的质量守恒为

{p˙IdρIdpIVL+ρIV˙L=m˙A,     compressibility onρ0V˙L=m˙A,                       compressibility off

其中：

- *pI* 是液体腔中的液体压力，等于蓄能器入口处的压力。
- m˙A 是进入端口 **A** 的液体质量流量。
- *ρI* 是液体腔中液体的密度。
- *ρ0* 是恒定液体密度。模块根据 **Precharge pressure** 参数计算该值。

V˙L={p˙IkshpGVG,            if 0 <VL<VCp˙IkshpGVG+Kstiff,                  else

其中 *Kstiff* 是硬止挡刚度系数。

### 动量守恒

动量守恒表示为：

pI=pG+pHS

其中 *pHS* 是硬止挡接触压力。

pHS={(VL−VC)Kstiff,    if VL≥VCVLKstiff,                          if VL ≤ 00,                                    else

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量级的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
