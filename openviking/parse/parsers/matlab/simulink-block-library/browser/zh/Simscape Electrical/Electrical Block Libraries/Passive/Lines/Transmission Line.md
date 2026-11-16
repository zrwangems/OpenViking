---
type: simulink-block
title: 'Transmission Line'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Lines'
documentation_page: 'transmissionline'
documentation_source_path: 'ref/transmissionline.html'
language: zh-CN
chinese_source: worker-translation
---

# Transmission Line

## 端口

### 守恒

### **p1** — 内导体 1 电气

与传输线内导体一端关联的电气守恒端口。

### **n1** — 外部屏蔽导体 1 电气

与传输线外部屏蔽导体一端关联的电气守恒端口。

### **p2** — 内导体 2 电气

与传输线内导体一端关联的电气守恒端口。

### **n2** — 外部屏蔽导体 2 电气

与传输线外部屏蔽导体一端关联的电气守恒端口。

## 参数

### **模型类型** — 传输线模型 `Delay-based and lossless`（默认）| `Delay-based and lossy` | `Lumped parameter L-section` | `Lumped parameter pi-section` | `Distributed parameter line`

选择以下传输线模型之一：

- `Delay-based and lossless` —
  将传输线建模为固定阻抗（与频率无关）加一个延迟项，如基于延迟且无损中所述。
  这是默认方法。它提供最佳仿真性能。
- `Delay-based and lossy` —
  将传输线建模为多个基于延迟的组件，通过一组电阻串联，如基于延迟且有损中所述。
- `Lumped parameter L-section` —
  将传输线建模为多个 L 线段，串联，如集总参数 L 段中所述。
- `Lumped parameter pi-section`
  — 将传输线建模为多个 pi 线段，串联，如集总参数 pi 段中所述。
- `Distributed parameter line` —
  将传输线建模为分布参数线路，如分布参数线路中所述。

### **传输延迟** — 总传输延迟 `5` `ns`（默认）| 正标量

总传输线延迟。参数值必须大于零。默认值为 `5` ns，这是一米同轴电缆的典型值。

#### 依赖关系

仅当为 **模型类型** 参数选择
`Delay-based and lossless` 或
`Delay-based and lossy` 时，此参数才可见。

### **参数化** — 模型参数化 `By characteristic impedance and capacitance`（默认）| `By inductance and capacitance`

选择模型参数化方法，如集总参数线路模型参数化中所述：

- `By characteristic impedance and
  capacitance` — 为
  **特性阻抗** 和
  **每单位长度电容** 参数指定值。
  这是默认方法。
- `By inductance and capacitance` —
  为 **每单位长度电感** 和
  **每单位长度电容** 参数指定值。

#### 依赖关系

仅当为 **模型类型** 参数选择 `Lumped
parameter L-section` 或 `Lumped parameter
pi-section` 时，此参数才可见。

### **特性阻抗** — 特性阻抗 `50` `Ohm`（默认）| 正标量

传输线的特性阻抗。参数值必须大于零。

#### 依赖关系

此参数仅在以下情况下可见：

- 为 **模型类型** 参数选择 `Delay-based and lossless` 或
  `Delay-based and lossy`。
- 为 **模型类型** 参数选择 `Lumped parameter L-section` 或 `Lumped parameter pi-section`，并且为
  **参数化** 参数选择 `By characteristic impedance and
  capacitance`。

### **用于 rlcg 规范的频率** — 用于 rlcg 规范的频率 `60` `Hz`（默认）| 正标量

用于 R、L、C、G 规范的频率，其中：

- *R* 是每单位长度线路电阻。
- *L* 是每单位长度线路电感。
- *C* 是每单位长度线路电容。
- *G* 是每单位长度线路电导。

#### 依赖关系

仅当为 **模型类型** 参数选择 `Lumped
parameter L-section`、`Lumped parameter
pi-section` 或 `Distributed parameter
line` 时，此参数才可见。

### **每单位长度电感** — 每单位长度电感 `220` `μH/m`（默认）| 正标量

传输线每单位长度的有效电感。参数值必须大于零。

#### 依赖关系

仅当为 **模型类型** 参数选择 `Lumped
parameter L-section`、`Lumped parameter
pi-section` 或 `Distributed parameter
line`，并且为 **参数化** 参数选择 `By inductance and capacitance` 时，此参数才可见。

### **每单位长度电容** — 每单位长度电容 `90` `pF/m`（默认）

传输线每单位长度的电容。

#### 依赖关系

仅当为 **模型类型** 参数选择 `Lumped
parameter L-section`、`Lumped parameter
pi-section` 或 `Distributed parameter
line` 时，此参数才可见。

### **每单位长度电阻** — 每单位长度电阻 `0.3` `Ohm/m`（默认）

每单位长度的传输线总电阻（即两条导电路径的电阻之和）。

#### 依赖关系

仅当为 **模型类型** 参数选择
`Delay-based and lossy`、
`Lumped parameter L-section`、
`Lumped parameter pi-section` 或
`Distributed parameter line` 时，此参数才可见。

### **每单位长度绝缘电导** — 每单位长度绝缘电导 `5e-6` `S/m`（默认）| 非负标量

每单位长度两条传输线导体之间的电导。参数值必须大于或等于零。

#### 依赖关系

仅当为 **模型类型** 参数选择 `Lumped
parameter L-section`、`Lumped parameter
pi-section` 或 `Distributed parameter
line` 时，此参数才可见。

### **线路长度** — 总传输线长度 `1` `m`（默认）| 正标量

总传输线长度。参数值必须大于零。

#### 依赖关系

仅当为 **模型类型** 参数选择
`Delay-based and lossy`、
`Lumped parameter L-section`、
`Lumped parameter pi-section` 或
`Distributed parameter line` 时，此参数才可见。

### **段数** — 模型段数 `1`（默认）

用于表示传输线的模型段数。参数值必须是大于或等于 1 的整数。

#### 依赖关系

仅当为 **模型类型** 参数选择
`Delay-based and lossy`、
`Lumped parameter L-section` 或
`Lumped parameter pi-section` 时，此参数才可见。

## 所属库

Simscape / Electrical / Passive / Lines

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

基于延迟或集总参数的传输线

Transmission Line 模块允许您在以下传输线模型之间进行选择：

1. Delay-based and lossless
2. Delay-based and lossy
3. Lumped parameter L-section
4. Lumped parameter pi-section
5. Distributed parameter line

第一个选项提供最佳仿真性能，选项 2、3 和 4 需要逐渐更多的计算能力。

### 基于延迟且无损

第一个选项 `Delay-based and lossless` 将传输线建模为固定阻抗（与频率无关）加一个延迟项。定义方程为：

|  |  |
| --- | --- |
| *v1*( *t* ) – *i1*( *t* ) *Z0* = *v2*( *t* – *τ* ) + *i*( *t* – *τ* ) *Z*0 | **(1)** |

2

|  |  |
| --- | --- |
| *v*2( *t* ) – *i2*( *t* ) *Z*0 = *v1*( *t* – *τ* ) + *i1*( *t* – *τ* ) *Z0* | **(2)** |

其中：

- *v1* 是传输线左端电压。
- *i1* 是流入传输线左端的电流。
- *v2* 是传输线右端电压。
- *i2* 是流入传输线右端的电流。
- *τ* 是传输线延迟。
- *Z0* 是线路特性阻抗。

### 基于延迟且有损

为了引入损耗，第二个选项 `Delay-based and
lossy` 将 *N* 个基于延迟的组件（每个组件由上述方程定义）通过一组电阻串联，如下图所示。

*N* 是大于或等于 1 的整数。*r* = *R* · *LEN* / *N*，其中 *R* 是每单位长度线路电阻，*LEN* 是线路长度。

### 集总参数 L 段

以下模块图显示一个 L 线段的模型。

集总参数参数化使用 *N* 个上述段模型的副本串联。

参数如下：

- *R* 是每单位长度线路电阻。
- *L* 是每单位长度线路电感。
- *C* 是每单位长度线路电容。
- *G* 是每单位长度线路电导。
- *LEN* 是线路长度。
- *N* 是串联段数。

### 集总参数 pi 段

以下模块图显示一个 pi 线段的模型。

集总参数参数化使用 *N* 个上述段模型的副本串联。参数与 L 段传输线模型的定义相同。与 L 段模型不同，pi 段模型是对称的。

### 集总参数线路模型参数化

集总参数模型（L 段或 pi 段）最难仿真，通常比基于延迟且有损模型需要多得多的段数（更大的 N）[1]。

电缆制造商通常不会给出每单位长度的电感值，而是给出特性阻抗。电感、电容和特性阻抗的关系为：

|  |  |
| --- | --- |
| *L* = *C* · *Z*02 | **(3)** |

使用集总参数模型时，该模块允许您指定 *L* 或 *Z*0。

### 分布参数线路

与模块提供的其他选项相比，分布参数线路在特定频率下可提供更准确的仿真。但是，这不是频率相关模型。在 **用于 rlcg 规范的频率** 参数指定的频率点之外，模型精度会下降。

对于频率相关传输线模型，请参阅 Frequency-Dependent Overhead Line (Three-Phase)。

多导体传输线的电磁行为由电报方程描述。

|  |  |
| --- | --- |
| I2−YcV2=−H(I1+YcV1) | **(4)** |

|  |  |
| --- | --- |
| I1−YcV1=−H(I2+YcV2) | **(5)** |

定义：

- Ish,1=YcV1 — 由注入电压 *V1* 在端子 1 产生的分流电流向量
- Ish,2=YcV2 — 由注入电压 *V2* 在端子 2 产生的分流电流向量
- Irfl,1=12(I1+YcV1) — 端子 1 的反射电流
- Irfl,2=12(I2+YcV2) — 端子 2 的反射电流

然后您可以重写并求解方程 4 和 5：

I1=Ish,1−2HIrfl,2

I2=Ish,2−2HIrfl,1

以下模块图显示分布参数线路的等效电路。
