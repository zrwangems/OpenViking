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
```yaml
ports:
- name: ~1
  summary: 一次绕组电压电气端口
  direction: conserving
- name: ~2
  summary: Delta 二次绕组电压电气端口
  direction: conserving
- name: ~3
  summary: Wye 二次绕组电压电气端口
  direction: conserving
- name: n3
  summary: 第二二次绕组中性点电气端口
  direction: conserving
- name: ~1i
  summary: 曲折绕组互连端口电气端口
  direction: conserving
```

### 守恒端口

### **~1** — 一次绕组电压电气端口

与一次绕组三相 [*a1*
*b1*
*c1*] 电压相关联的可扩展三相电气守恒端口。

### **~2** — Delta 二次绕组电压电气端口

与第一个二次绕组三相 [*a2*
*b2*
*c2*] 电压相关联的可扩展三相电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Secondary connection**
设置为 `Delta` 或 `Wye and
Delta`。

### **~3** — Wye 二次绕组电压电气端口

与第二个二次绕组三相 [*a3*
*b3*
*c3*] 电压相关联的可扩展三相电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Secondary connection**
设置为 `Wye` 或 `Wye and
Delta`。

### **n3** — 第二二次绕组中性点电气端口

与 wye 二次绕组中性点相关联的电气守恒端口。

### **~1i** — 曲折绕组互连端口电气端口

与曲折绕组互连相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Zigzag configuration** 设置为
`Accessible winding
interconnects`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是对复合三相端口还是扩展三相端口进行建模 Composite three-phase ports（默认）| Expanded three-phase ports
  group: ''
- name: Rated apparent power
  summary: 额定容量下的视在功率 100e6 V*A（默认）| 正标量
  group: 主
- name: Rated electrical frequency
  summary: 所连接电网的电气频率 60 Hz（默认）| 正标量
  group: 主
- name: Primary rated voltage
  summary: 施加到一次绕组的均方根线电压 24e3 V（默认）| 正标量
  group: 主
- name: Zigzag configuration
  summary: 曲折绕组配置类型 Internal floating neutral（默认）| Accessible winding interconnects
  group: 主
- name: Secondary connection
  summary: 曲折绕组配置类型 Delta（默认）| Wye | Wye and Delta
  group: 主
- name: Delta connection type
  summary: Delta 连接类型 Delta 1 o'clock（默认）| Delta 11 o'clock
  group: 主
- name: Delta secondary rated voltage
  summary: 施加到 Delta 二次绕组的均方根线电压 4160 V（默认）| 正标量
  group: 主
- name: Wye secondary rated voltage
  summary: 施加到 Wye 二次绕组的均方根线电压 4160 V（默认）| 正标量
  group: 主
- name: Secondary phase shift
  summary: 二次绕组的相位偏移 -7.5 deg（默认）
  group: 主
- name: Primary winding resistance (pu)
  summary: 一次绕组功率损耗 0.01（默认）| 正标量
  group: 阻抗
- name: Delta secondary winding resistance (pu)
  summary: Delta 二次绕组功率损耗 0.01（默认）| 正标量
  group: 阻抗
- name: Wye secondary winding resistance (pu)
  summary: Wye 二次绕组功率损耗 0.01（默认）| 正标量
  group: 阻抗
- name: Leakage reactance
  summary: 漏电抗建模 Exclude（默认）| Include
  group: 阻抗
- name: Primary leakage reactance (pu)
  summary: 一次绕组磁通损耗 0.001（默认）| 正标量
  group: 阻抗
- name: Delta secondary leakage reactance (pu)
  summary: Delta 二次绕组磁通损耗 0.001（默认）| 正标量
  group: 阻抗
- name: Wye secondary leakage reactance (pu)
  summary: Wye 二次绕组磁通损耗 0.001（默认）| 正标量
  group: 阻抗
- name: Magnetizing resistance
  summary: 励磁电阻建模 Exclude（默认）| Include
  group: 阻抗
- name: Shunt magnetizing resistance (pu)
  summary: 变压器铁芯损耗 500（默认）| 正标量
  group: 阻抗
- name: Magnetizing reactance
  summary: 励磁电抗建模 Exclude（默认）| Include
  group: 阻抗
- name: Magnetic saturation representation
  summary: 磁饱和的表示方式 None（默认）| Lookup table (phi versus i)
  group: 阻抗
- name: Current vector (pu), i
  summary: 电流的标幺向量 [0, .002, 1, 2]（默认）
  group: 阻抗
- name: Magnetic flux vector (pu), phi
  summary: 磁通的标幺向量 [0, 1.2, 1.5, 1.51]（默认）
  group: 阻抗
- name: Shunt magnetizing reactance (pu)
  summary: 变压器铁芯磁效应 500（默认）| 正标量
  group: 阻抗
```

### **Modeling option** — 是对复合三相端口还是扩展三相端口进行建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是对复合三相端口还是扩展三相端口进行建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建与三相电力系统单线图相对应的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

### 主

### **Rated apparent power** — 额定容量下的视在功率 `100e6` `V*A`（默认）| 正标量

变压器在额定容量下运行时流过的视在功率，单位为 V\*A。

### **Rated electrical frequency** — 所连接电网的电气频率 `60` `Hz`（默认）| 正标量

变压器所连接交流电网的额定或标称频率，单位为 Hz。该值必须大于
`0`。

### **Primary rated voltage** — 施加到一次绕组的均方根线电压 `24e3` `V`（默认）| 正标量

正常运行条件下施加到一次绕组的 RMS 线电压，单位为 V。该值必须大于
`0`。

### **Zigzag configuration** — 曲折绕组配置类型 `Internal floating neutral`（默认）| `Accessible winding interconnects`

曲折绕组的配置。

### **Secondary connection** — 曲折绕组配置类型 `Delta`（默认）| `Wye` | `Wye and Delta`

二次侧连接的配置。

### **Delta connection type** — Delta 连接类型 `Delta 1 o'clock`（默认）| `Delta 11 o'clock`

Delta 连接的类型。

#### 依赖关系

要启用此参数，请将 **Secondary
connection** 设置为 `Delta` 或
`Wye and Delta`。

### **Delta secondary rated voltage** — 施加到 Delta 二次绕组的均方根线电压 `4160` `V`（默认）| 正标量

正常运行条件下施加到 Delta 二次绕组的 RMS 线电压，单位为 V。该值必须大于
`0`。

#### 依赖关系

要启用此参数，请将 **Secondary
connection** 设置为 `Delta` 或
`Wye and Delta`。

### **Wye secondary rated voltage** — 施加到 Wye 二次绕组的均方根线电压 `4160` `V`（默认）| 正标量

正常运行条件下施加到 Wye 二次绕组的 RMS 线电压，单位为 V。该值必须大于
`0`。

#### 依赖关系

要启用此参数，请将 **Secondary
connection** 设置为 `Wye` 或
`Wye and Delta`。

### **Secondary phase shift** — 二次绕组的相位偏移 `-7.5` `deg`（默认）

曲折绕组与二次绕组之间的相位偏移。

### 阻抗

### **Primary winding resistance (pu)** — 一次绕组功率损耗 `0.01`（默认）| 正标量

一次绕组的标幺功率损耗。该值必须大于
`0`。

### **Delta secondary winding resistance (pu)** — Delta 二次绕组功率损耗 `0.01`（默认）| 正标量

Delta 二次绕组的标幺功率损耗。该值必须大于 `0`。

#### 依赖关系

要启用此参数，请将 **Secondary
connection** 设置为 `Delta` 或
`Wye and Delta`。

### **Wye secondary winding resistance (pu)** — Wye 二次绕组功率损耗 `0.01`（默认）| 正标量

Wye 二次绕组的标幺功率损耗。该值必须大于 `0`。

#### 依赖关系

要启用此参数，请将 **Secondary
connection** 设置为 `Wye` 或
`Wye and Delta`。

### **Leakage reactance** — 漏电抗建模 `Exclude`（默认）| `Include`

是否对磁通损耗进行建模。

### **Primary leakage reactance (pu)** — 一次绕组磁通损耗 `0.001`（默认）| 正标量

一次绕组的标幺磁通损耗。该值必须大于 `0`。

#### 依赖关系

要启用此参数，请将 **Leakage
reactance** 设置为
`Include`。

### **Delta secondary leakage reactance (pu)** — Delta 二次绕组磁通损耗 `0.001`（默认）| 正标量

Delta 二次绕组的标幺磁通损耗。该值必须大于 `0`。

#### 依赖关系

要启用此参数，请将 **Leakage reactance** 设置为
`Include`，并将 **Secondary
connection** 设置为 `Delta`
或 `Wye and Delta`。

### **Wye secondary leakage reactance (pu)** — Wye 二次绕组磁通损耗 `0.001`（默认）| 正标量

Wye 二次绕组的标幺磁通损耗。该值必须大于 `0`。

#### 依赖关系

要启用此参数，请将 **Leakage reactance** 设置为
`Include`，并将 **Secondary
connection** 设置为 `Wye`
或 `Wye and Delta`。

### **Magnetizing resistance** — 励磁电阻建模 `Exclude`（默认）| `Include`

是否对变压器铁芯损耗进行建模。

### **Shunt magnetizing resistance (pu)** — 变压器铁芯损耗 `500`（默认）| 正标量

变压器铁芯的标幺损耗。该值必须大于
`0`。

#### 依赖关系

要启用此参数，请将 **Magnetizing
resistance** 设置为
`Include`。

### **Magnetizing reactance** — 励磁电抗建模 `Exclude`（默认）| `Include`

是否对变压器铁芯的磁效应进行建模。

### **Magnetic saturation representation** — 磁饱和的表示方式 `None`（默认）| `Lookup table (phi versus i)`

是否表示磁饱和。

#### 依赖关系

要启用此参数，请将 **Magnetizing
reactance** 设置为
`Include`。

### **Current vector (pu), i** — 电流的标幺向量 `[0, .002, 1, 2]`（默认）

电流的标幺向量。第一个值必须为
`0`。此参数必须严格递增。

#### 依赖关系

要启用此参数，请将 **Magnetizing reactance** 设置为
`Include`，并将 **Magnetic
saturation representation** 设置为 `Lookup
table (phi versus i)`。

### **Magnetic flux vector (pu), phi** — 磁通的标幺向量 `[0, 1.2, 1.5, 1.51]`（默认）

磁通的标幺向量。第一个值必须为
`0`。此参数必须严格递增。

#### 依赖关系

要启用此参数，请将 **Magnetizing reactance** 设置为
`Include`，并将 **Magnetic
saturation representation** 设置为 `Lookup
table (phi versus i)`。

### **Shunt magnetizing reactance (pu)** — 变压器铁芯磁效应 `500`（默认）| 正标量

变压器铁芯在线性区域运行时的标幺磁效应。该值必须大于
`0`。

#### 依赖关系

要启用此参数，请将 **Magnetizing reactance** 设置为
`Include`，并将 **Magnetic
saturation representation** 设置为
`None`。
## 所属库

Simscape / Electrical / Passive / Transformers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

具有三柱铁芯和饱和能力的线性非理想曲折-Delta-Wye 变压器

Zigzag-Delta-Wye Transformer 模块对具有三柱铁芯的线性非理想变压器进行建模，该变压器具有一次曲折绕组以及二次 Delta、Wye 或 Delta 和 Wye 绕组。您可以使用 **Wye secondary phase
shift** 参数指定曲折绕组与 Wye 绕组之间的相位偏移，并使用标幺值对模块阻抗进行参数化。该模块包含线性绕组漏磁和线性铁芯磁化效应。

Delta 绕组类型的配置选项包括：

- Delta 1 o'clock — 相对于所连接 Wye 配置的电压具有滞后 30 度相位偏移的网状配置
- Delta 11 o'clock — 相对于所连接 Wye 配置的电压具有超前 30 度相位偏移的网状配置

这些等效电路图分别显示了 Delta 1 o'clock 和 Delta 11 o'clock 配置下的曲折-Delta-Wye 变压器。

在这些图中：

- *Rw1* 是一次绕组电阻。
- *Ll1* 是一次漏电抗。
- *Rw2* 是 Delta 二次绕组电阻。
- *Ll2* 是 Delta 二次漏电抗。
- *Rw3* 是 Wye 二次绕组电阻。
- *Ll3* 是 Wye 二次漏电抗。
- *Rm* 是并联励磁电阻。
- *Lm* 是并联励磁电抗。

### 变量

使用 **Variables** 设置可在仿真前指定模块变量的优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

要启用 **Wye secondary currents** 变量，请将 **Secondary connection** 设置为 `Wye` 或
`Wye and Delta`。

要启用 **Delta secondary currents** 变量，请将 **Secondary connection** 设置为 `Delta` 或
`Wye and Delta`。
