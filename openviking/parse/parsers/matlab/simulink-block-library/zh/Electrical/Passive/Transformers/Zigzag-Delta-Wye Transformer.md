---
type: simulink-block
title: 'Zigzag-Delta-Wye Transformer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'zigzagdeltawyetransformer'
documentation_source_path: 'ref/zigzagdeltawyetransformer.html'
language: zh-CN
chinese_source: worker-translation
---

# Zigzag-Delta-Wye Transformer

## 端口

### 守恒

### **~1** — Primary winding voltage electrical

与一次绕组的三相 [*a1* *b1* *c1*] 电压关联的可扩展三相电气守恒端口。

### **~2** — Delta secondary winding voltage electrical

与第一个二次绕组的三相 [*a2* *b2* *c2*] 电压关联的可扩展三相电气守恒端口。

#### 依赖项

要启用此端口，请将 **Secondary connection** 设置为 `Delta` 或 `Wye and Delta`。

### **~3** — Wye secondary winding voltage electrical

与第二个二次绕组的三相 [*a3* *b3* *c3*] 电压关联的可扩展三相电气守恒端口。

#### 依赖项

要启用此端口，请将 **Secondary connection** 设置为 `Wye` 或 `Wye and Delta`。

### **n3** — Second secondary winding neutral point electrical

与 wye 二次绕组中性点关联的电气守恒端口。

### **~1i** — Zigzag winding interconnection port electrical

与 zigzag 绕组互连关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Zigzag configuration** 设置为 `Accessible winding interconnects`。

## 参数

### **Modeling option** — 是否对复合或扩展三相端口建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是否对复合或扩展三相端口建模。

复合三相端口用单个模块端口表示三个单独的电气守恒端口。您可以使用复合三相端口构建与三相电气系统单线图对应的模型。

扩展三相端口使用三个单独的电气守恒端口表示三相系统的各个相。

### 主要

### **Rated apparent power** — 额定容量下的视在功率 `100e6` `V*A`（默认）| positive scalar

变压器在额定容量下运行时流过的视在功率，单位为 V\*A。

### **Rated electrical frequency** — 所连接电网的电气频率 `60` `Hz`（默认）| positive scalar

变压器所连接交流电网的额定或标称频率，单位为 Hz。该值必须大于 `0`。

### **Primary rated voltage** — 施加到一次绕组的均方根线电压 `24e3` `V`（默认）| positive scalar

正常操作条件下施加到一次绕组的 RMS 线电压，单位为 V。该值必须大于 `0`。

### **Zigzag configuration** — Zigzag 配置类型 `Internal floating neutral`（默认）| `Accessible winding interconnects`

zigzag 绕组的配置。

### **Secondary connection** — Zigzag configuration type `Delta`（默认）| `Wye` | `Wye and Delta`

二次连接的配置。

### **Delta connection type** — Delta 连接类型 `Delta 1 o'clock`（默认）| `Delta 11 o'clock`

delta 连接的类型。

#### 依赖项

要启用此参数，请将 **Secondary connection** 设置为 `Delta` 或 `Wye and Delta`。

### **Delta secondary rated voltage** — 施加到 delta 二次绕组的均方根线电压 `4160` `V`（默认）| positive scalar

正常操作条件下施加到 delta 二次绕组的 RMS 线电压，单位为 V。该值必须大于 `0`。

#### 依赖项

要启用此参数，请将 **Secondary connection** 设置为 `Delta` 或 `Wye and Delta`。

### **Wye secondary rated voltage** — 施加到 wye 二次绕组的均方根线电压 `4160` `V`（默认）| positive scalar

正常操作条件下施加到 wye 二次绕组的 RMS 线电压，单位为 V。该值必须大于 `0`。

#### 依赖项

要启用此参数，请将 **Secondary connection** 设置为 `Wye` 或 `Wye and Delta`。

### **Secondary phase shift** — 二次绕组的相位偏移 `-7.5` `deg`（默认）

zigzag 绕组和二次绕组之间的相位偏移。

### 阻抗

### **Primary winding resistance (pu)** — 一次绕组功率损耗 `0.01`（默认）| positive scalar

一次绕组中的标幺功率损耗。该值必须大于 `0`。

### **Delta secondary winding resistance (pu)** — Delta 二次绕组功率损耗 `0.01`（默认）| positive scalar

delta 二次绕组中的标幺功率损耗。该值必须大于 `0`。

#### 依赖项

要启用此参数，请将 **Secondary connection** 设置为 `Delta` 或 `Wye and Delta`。

### **Wye secondary winding resistance (pu)** — Wye 二次绕组功率损耗 `0.01`（默认）| positive scalar

wye 二次绕组中的标幺功率损耗。该值必须大于 `0`。

#### 依赖项

要启用此参数，请将 **Secondary connection** 设置为 `Wye` 或 `Wye and Delta`。

### **Leakage reactance** — 漏电抗建模 `Exclude`（默认）| `Include`

是否对磁通损耗建模。

### **Primary leakage reactance (pu)** — 一次绕组磁通损耗 `0.001`（默认）| positive scalar

一次绕组中的标幺磁通损耗。该值必须大于 `0`。

#### 依赖项

要启用此参数，请将 **Leakage reactance** 设置为 `Include`。

### **Delta secondary leakage reactance (pu)** — Delta 二次绕组磁通损耗 `0.001`（默认）| positive scalar

delta 二次绕组中的标幺磁通损耗。该值必须大于 `0`。

#### 依赖项

要启用此参数，请将 **Leakage reactance** 设置为 `Include`，并将 **Secondary connection** 设置为 `Delta` 或 `Wye and Delta`。

### **Wye secondary leakage reactance (pu)** — Wye 二次绕组磁通损耗 `0.001`（默认）| positive scalar

wye 二次绕组中的标幺磁通损耗。该值必须大于 `0`。

#### 依赖项

要启用此参数，请将 **Leakage reactance** 设置为 `Include`，并将 **Secondary connection** 设置为 `Wye` 或 `Wye and Delta`。

### **Magnetizing resistance** — 磁化电阻建模 `Exclude`（默认）| `Include`

是否对变压器铁芯损耗建模。

### **Shunt magnetizing resistance (pu)** — 变压器铁芯损耗 `500`（默认）| positive scalar

变压器铁芯中的标幺损耗。该值必须大于 `0`。

#### 依赖项

要启用此参数，请将 **Magnetizing resistance** 设置为 `Include`。

### **Magnetizing reactance** — 磁化电抗建模 `Exclude`（默认）| `Include`

是否对变压器铁芯的磁效应建模。

### **Magnetic saturation representation** — 磁饱和的表示 `None`（默认）| `Lookup table (phi versus i)`

是否表示磁饱和。

#### 依赖项

要启用此参数，请将 **Magnetizing reactance** 设置为 `Include`。

### **Current vector (pu), i** — 电流的标幺向量 `[0, .002, 1, 2]`（默认）

电流的标幺向量。第一个值必须为 `0`。此参数必须严格递增。

#### 依赖项

要启用此参数，请将 **Magnetizing reactance** 设置为 `Include`，并将 **Magnetic saturation representation** 设置为 `Lookup table (phi versus i)`。

### **Magnetic flux vector (pu), phi** — 磁通的标幺向量 `[0, 1.2, 1.5, 1.51]`（默认）

磁通的标幺向量。第一个值必须为 `0`。此参数必须严格递增。

#### 依赖项

要启用此参数，请将 **Magnetizing reactance** 设置为 `Include`，并将 **Magnetic saturation representation** 设置为 `Lookup table (phi versus i)`。

### **Shunt magnetizing reactance (pu)** — 变压器铁芯磁效应 `500`（默认）| positive scalar

变压器铁芯在线性区域工作时的标幺磁效应。该值必须大于 `0`。

#### 依赖项

要启用此参数，请将 **Magnetizing reactance** 设置为 `Include`，并将 **Magnetic saturation representation** 设置为 `None`。

## 所属库

Simscape / Electrical / Passive / Transformers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

具有饱和能力的线性、非理想三柱铁芯 zigzag-delta-wye 变压器

Zigzag-Delta-Wye Transformer 模块对线性、非理想变压器进行建模，该变压器具有三柱铁芯，铁芯带有一侧 zigzag 绕组以及二次侧 delta、wye 或 delta and wye 绕组。您可以使用 **Wye secondary phase shift** 参数指定 zigzag 绕组和 wye 绕组之间的相位偏移，并使用标幺值参数化模块阻抗。模块包含线性绕组漏感和线性铁芯磁化效应。

delta 绕组类型的配置选项包括：

- Delta 1 o'clock — 网形配置，相对于所连接 wye 配置的电压具有滞后 30 度相移
- Delta 11 o'clock — 网形配置，相对于所连接 wye 配置的电压具有超前 30 度相移

这些等效电路图分别显示 delta 1 o'clock 和 delta 11 o'clock 配置下的 zigzag-delta-wye 变压器。

在这些图中：

- *Rw1* 是一次绕组电阻。
- *Ll1* 是一次漏电抗。
- *Rw2* 是 delta 二次绕组电阻。
- *Ll2* 是 delta 二次漏电抗。
- *Rw3* 是 wye 二次绕组电阻。
- *Ll3* 是 wye 二次漏电抗。
- *Rm* 是并联磁化电阻。
- *Lm* 是并联磁化电抗。

### 变量

使用 **Variables** 设置在仿真前指定模块变量的优先级和初始目标值。有关详细信息，请参阅设置模块变量的优先级和初始目标。

要启用 **Wye secondary currents** 变量，请将 **Secondary connection** 设置为 `Wye` 或 `Wye and Delta`。

要启用 **Delta secondary currents** 变量，请将 **Secondary connection** 设置为 `Delta` 或 `Wye and Delta`。
