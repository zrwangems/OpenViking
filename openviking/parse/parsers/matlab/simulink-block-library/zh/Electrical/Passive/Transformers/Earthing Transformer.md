---
type: simulink-block
title: 'Earthing Transformer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'earthingtransformer'
documentation_source_path: 'ref/earthingtransformer.html'
language: zh-CN
chinese_source: worker-translation
---

# Earthing Transformer

## 端口
```yaml
ports:
- name: '~'
  summary: 三相电压电气
  direction: unspecified
- name: n
  summary: 中性点电气
  direction: unspecified
```

### 守恒

### **~** — 三相电压电气

可扩展三相电气守恒端口，与三相电压相关联。

### **n** — 中性点电气

电气三相电气守恒端口，与中性点相关联。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是对复合三相端口还是扩展三相端口进行建模 Composite three-phase ports（默认）| Expanded three-phase ports
  group: ''
- name: Rated apparent power
  summary: 额定视在功率 100e6 V*A（默认）| 正标量
  group: ''
- name: Rated voltage
  summary: 额定电压 24e3 V（默认）| 正标量
  group: ''
- name: Rated electrical frequency
  summary: 额定电气频率 60 Hz（默认）| 正标量
  group: ''
- name: Units
  summary: 参数化单位制 Per unit（默认）| SI
  group: ''
- name: Zero-sequence resistance (pu)
  summary: 零序电阻 0.01（默认）| 正标量
  group: ''
- name: Zero-sequence reactance (pu)
  summary: 零序电抗 0.3（默认）| 正标量
  group: ''
- name: Shunt magnetizing resistance (pu)
  summary: 并联励磁电阻 500（默认）| 正标量
  group: ''
- name: Shunt magnetizing reactance (pu)
  summary: 并联励磁电抗 500（默认）| 正标量
  group: ''
- name: Zero-sequence resistance
  summary: 零序电阻 0.0576 Ohm（默认）| 正标量
  group: ''
- name: Zero-sequence inductance
  summary: 零序电感 1.728 H（默认）| 正标量
  group: ''
- name: Shunt magnetizing resistance
  summary: 并联励磁电阻 2880 Ohm（默认）| 正标量
  group: ''
- name: Shunt magnetizing inductance
  summary: 并联励磁电感 2880 H（默认）| 正标量
  group: ''
```

### **Modeling option** — 是对复合三相端口还是扩展三相端口进行建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是对复合三相端口还是扩展三相端口进行建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口来构建对应于三相电力系统单线图的模型。

扩展三相端口用三个独立的电气守恒端口表示三相系统的各相。

### **Rated apparent power** — 额定视在功率 `100e6` `V*A`（默认）| 正标量

以 SI 单位表示的额定视在功率。该值必须大于 `0`。

### **Rated voltage** — 额定电压 `24e3` `V`（默认）| 正标量

以 SI 单位表示的额定电压。该值必须大于 0。

### **Rated electrical frequency** — 额定电气频率 `60` `Hz`（默认）| 正标量

以 SI 单位表示的额定电气频率。该值必须大于 `0`。

### **Units** — 参数化单位制 `Per unit`（默认）| `SI`

用于阻抗参数化的单位制。

#### 依赖关系

其他参数的可见性取决于此参数的值。

### **Zero-sequence resistance (pu)** — 零序电阻 `0.01`（默认）| 正标量

标幺值零序电阻。该值必须大于 `0`。

#### 依赖关系

仅当 **Units** 参数设置为 `Per unit` 时，此参数才可见。

### **Zero-sequence reactance (pu)** — 零序电抗 `0.3`（默认）| 正标量

标幺值零序电抗。该值必须大于 `0`。

#### 依赖关系

仅当 **Units** 参数设置为 `Per unit` 时，此参数才可见。

### **Shunt magnetizing resistance (pu)** — 并联励磁电阻 `500`（默认）| 正标量

标幺值并联励磁电阻。该值必须大于 `0`。

#### 依赖关系

仅当 **Units** 参数设置为 `Per unit` 时，此参数才可见。

### **Shunt magnetizing reactance (pu)** — 并联励磁电抗 `500`（默认）| 正标量

标幺值并联励磁电抗。该值必须大于 `0`。

#### 依赖关系

仅当 **Units** 参数设置为 `Per unit` 时，此参数才可见。

### **Zero-sequence resistance** — 零序电阻 `0.0576` `Ohm`（默认）| 正标量

以 SI 单位表示的零序电阻。该值必须大于 `0`。

#### 依赖关系

仅当 **Units** 参数设置为 `SI` 时，此参数才可见。

### **Zero-sequence inductance** — 零序电感 `1.728` `H`（默认）| 正标量

以 SI 单位表示的零序电感。该值必须大于 `0`。

#### 依赖关系

仅当 **Units** 参数设置为 `SI` 时，此参数才可见。

### **Shunt magnetizing resistance** — 并联励磁电阻 `2880` `Ohm`（默认）| 正标量

以 SI 单位表示的并联励磁电阻。该值必须大于 `0`。

#### 依赖关系

仅当 **Units** 参数设置为 `SI` 时，此参数才可见。

### **Shunt magnetizing inductance** — 并联励磁电感 `2880` `H`（默认）| 正标量

以 SI 单位表示的并联励磁电感。该值必须大于 `0`。

#### 依赖关系

仅当 **Units** 参数设置为 `SI` 时，此参数才可见。
## 所属库

Simscape / Electrical / Passive / Transformers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

采用 zigzag 配置的三相接地变压器

Earthing Transformer 模块对三相 zigzag 连接接地变压器进行建模。该模块允许您在不接地三相电力系统中提供人工中性点。人工中性点为零序电流创建低阻抗路径，并正序电流创建高阻抗路径。为适应相中性点负载，返回路径允许三角形连接电源。

有关使用三相 zigzag 连接接地变压器的更多信息，请参阅 Engineering Applications

### 方程

此模块在电气域和磁域中实现，表示相绕组和磁芯的物理特性。该模块的等效电路包括绕组、磁阻和涡流。

对于磁路中的 zigzag 配置，*a*、*b* 和 *c* 相分别表示磁芯的每个芯柱。

您可以基于磁通守恒定律和 Hopkinson 定律，通过若干数学步骤获得电气特性与磁特性之间的关系。

对于接地变压器，各相之间以及所有绕组之间的耦合是相同的。在以下方程中：

- *n* 是绕组的匝数。
- *R* 是相间励磁磁阻。
- *RL* 是漏磁阻。
- *Leddy* 是相间涡流损耗引起的磁电感。

那么，电气域中的电感矩阵与磁域中的磁阻矩阵之间的关系可以写为：

L​=[L11L12L13L21L22L23L31L32L33]=[n2(2Rl+6R)−3n2R−3n2R−3n2Rn2(2Rl+6R)−3n2R−3n2R−3n2Rn2(2Rl+6R)]

对角线元素表示每相的漏电感和励磁电感之和，因此：

Ll=2n2Rl

因此：

RL=2n2Ll

R=9n2Lm

Leddy=9n2Rm
