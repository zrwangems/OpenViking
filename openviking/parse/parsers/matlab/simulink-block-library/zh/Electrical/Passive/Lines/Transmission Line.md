---
type: simulink-block
title: 'Transmission Line'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Lines'
documentation_page: 'transmissionline'
documentation_source_path: 'ref/transmissionline.html'
language: zh-CN
chinese_source: worker-translation
---

# Transmission Line

## 端口
```yaml
ports:
- name: p1
  summary: 内导体 1 电气
  direction: conserving
- name: n1
  summary: 外部屏蔽导体 1 电气
  direction: conserving
- name: p2
  summary: 内导体 2 电气
  direction: conserving
- name: n2
  summary: 外部屏蔽导体 2 电气
  direction: conserving
```

### 守恒端口

### **p1** — 内导体 1 电气

与传输线内导体一端相关联的电气守恒端口。

### **n1** — 外部屏蔽导体 1 电气

与传输线外部屏蔽导体一端相关联的电气守恒端口。

### **p2** — 内导体 2 电气

与传输线内导体一端相关联的电气守恒端口。

### **n2** — 外部屏蔽导体 2 电气

与传输线外部屏蔽导体一端相关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Model Type
  summary: 传输线模型 Delay-based and lossless（默认）| Delay-based and lossy | Lumped parameter L-section | Lumped parameter pi-section
    | Distributed parameter line
  group: ''
- name: Transmission delay
  summary: 总传输延迟 5 ns（默认）| 正标量
  group: ''
- name: Parameterization
  summary: 模型参数化 By characteristic impedance and capacitance（默认）| By inductance and capacitance
  group: ''
- name: Characteristic impedance
  summary: 特性阻抗 50 Ohm（默认）| 正标量
  group: ''
- name: Frequency used for rlcg specification
  summary: 用于 rlcg 规格的频率 60 Hz（默认）| 正标量
  group: ''
- name: Inductance per unit length
  summary: 单位长度电感 220 μH/m（默认）| 正标量
  group: ''
- name: Capacitance per unit length
  summary: 单位长度电容 90 pF/m（默认）
  group: ''
- name: Resistance per unit length
  summary: 单位长度电阻 0.3 Ohm/m（默认）
  group: ''
- name: Insulation conductance per unit length
  summary: 单位长度绝缘电导 5e-6 S/m（默认）| 非负标量
  group: ''
- name: Line length
  summary: 传输线总长度 1 m（默认）| 正标量
  group: ''
- name: Number of segments
  summary: 模型段数 1（默认）
  group: ''
```

### **Model Type** — 传输线模型 `Delay-based and lossless`（默认）| `Delay-based and lossy` | `Lumped parameter L-section` | `Lumped parameter pi-section` | `Distributed parameter line`

选择以下传输线模型之一：

- `Delay-based and lossless` —
  将传输线建模为固定阻抗（与频率无关）加上延迟项，如基于延迟且无损中所述。
  这是默认方法。它提供最佳的仿真性能。
- `Delay-based and lossy` —
  将传输线建模为若干基于延迟的组件，通过一组电阻串联连接，如基于延迟且有损中所述。
- `Lumped parameter L-section` —
  将传输线建模为若干 L 型线段，串联连接，如集总参数 L 型段中所述。
- `Lumped parameter pi-section`
  — 将传输线建模为若干 π 型线段，串联连接，如集总参数 π 型段中所述。
- `Distributed parameter line` —
  将传输线建模为分布参数线路，如分布参数线路中所述。

### **Transmission delay** — 总传输延迟 `5` `ns`（默认）| 正标量

传输线的总延迟。参数值必须大于零。默认值为 `5` ns，这是一米同轴电缆的典型值。

#### 依赖关系

仅当为 **Model type** 参数选择
`Delay-based and lossless` 或
`Delay-based and lossy` 时，此参数才可见。

### **Parameterization** — 模型参数化 `By characteristic impedance and capacitance`（默认）| `By inductance and capacitance`

选择模型参数化方法，如集总参数线路模型参数化中所述：

- `By characteristic impedance and
  capacitance` — 为
  **Characteristic impedance** 和
  **Capacitance per unit length** 参数指定值。
  这是默认方法。
- `By inductance and capacitance` —
  为 **Inductance per unit
  length** 和 **Capacitance per unit
  length** 参数指定值。

#### 依赖关系

仅当为 **Model type** 参数选择 `Lumped
parameter L-section` 或 `Lumped parameter
pi-section` 时，此参数才可见。

### **Characteristic impedance** — 特性阻抗 `50` `Ohm`（默认）| 正标量

传输线的特性阻抗。参数值必须大于零。

#### 依赖关系

仅当选择以下任一情况时，此参数才可见：

- 为 **Model type** 参数选择
  `Delay-based and lossless` 或
  `Delay-based and lossy`。
- 为 **Model type** 参数选择
  `Lumped parameter L-section` 或
  `Lumped parameter pi-section`，并为
  **Parameterization** 参数选择
  `By characteristic impedance and
  capacitance`。

### **Frequency used for rlcg specification** — 用于 rlcg 规格的频率 `60` `Hz`（默认）| 正标量

用于 R、L、C、G 规格的频率，其中：

- *R* 是单位长度线路电阻。
- *L* 是单位长度线路电感。
- *C* 是单位长度线路电容。
- *G* 是单位长度线路电导。

#### 依赖关系

仅当为 **Model type** 参数选择 `Lumped
parameter L-section`、`Lumped parameter
pi-section` 或 `Distributed parameter
line` 时，此参数才可见。

### **Inductance per unit length** — 单位长度电感 `220` `μH/m`（默认）| 正标量

传输线的单位长度有效电感。参数值必须大于零。

#### 依赖关系

仅当为 **Model type** 参数选择 `Lumped
parameter L-section`、`Lumped parameter
pi-section` 或 `Distributed parameter
line`，并为 **Parameterization** 参数选择
`By inductance and capacitance` 时，此参数才可见。

### **Capacitance per unit length** — 单位长度电容 `90` `pF/m`（默认）

传输线的单位长度电容。

#### 依赖关系

仅当为 **Model type** 参数选择 `Lumped
parameter L-section`、`Lumped parameter
pi-section` 或 `Distributed parameter
line` 时，此参数才可见。

### **Resistance per unit length** — 单位长度电阻 `0.3` `Ohm/m`（默认）

传输线的单位长度总电阻（即两条导电路径的电阻之和）。

#### 依赖关系

仅当为 **Model type** 参数选择
`Delay-based and lossy`、
`Lumped parameter L-section`、
`Lumped parameter pi-section` 或
`Distributed parameter line` 时，此参数才可见。

### **Insulation conductance per unit length** — 单位长度绝缘电导 `5e-6` `S/m`（默认）| 非负标量

传输线两条导体之间的单位长度电导。参数值必须大于或等于零。

#### 依赖关系

仅当为 **Model type** 参数选择 `Lumped
parameter L-section`、`Lumped parameter
pi-section` 或 `Distributed parameter
line` 时，此参数才可见。

### **Line length** — 传输线总长度 `1` `m`（默认）| 正标量

传输线的总长度。参数值必须大于零。

#### 依赖关系

仅当为 **Model type** 参数选择
`Delay-based and lossy`、
`Lumped parameter L-section`、
`Lumped parameter pi-section` 或
`Distributed parameter line` 时，此参数才可见。

### **Number of segments** — 模型段数 `1`（默认）

用于表示传输线的模型段数。参数值必须是大于或等于 1 的整数。

#### 依赖关系

仅当为 **Model type** 参数选择
`Delay-based and lossy`、
`Lumped parameter L-section` 或
`Lumped parameter pi-section` 时，此参数才可见。
## 所属库

Simscape / Electrical / Passive / Lines

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

基于延迟或集总参数传输线

Transmission Line 模块允许您在以下传输线模型之间进行选择：

1. 基于延迟且无损
2. 基于延迟且有损
3. 集总参数 L 型段
4. 集总参数 π 型段
5. 分布参数线路

第一个选项提供最佳的仿真性能，选项 2、3 和 4 需要逐渐更多的计算能力。

### 基于延迟且无损

第一个选项 `Delay-based and lossless` 将传输线建模为固定阻抗（与频率无关）加上延迟项。定义方程为：

|  |  |
| --- | --- |
| *v1*( *t* ) – *i1*( *t* ) *Z0* = *v2*( *t* – *τ* ) + *i*( *t* – *τ* ) *Z*0 | **(1)** |

2

|  |  |
| --- | --- |
| *v*2( *t* ) – *i2*( *t* ) *Z*0 = *v1*( *t* – *τ* ) + *i1*( *t* – *τ* ) *Z0* | **(2)** |

其中：

- *v1* 是传输线左端的电压。
- *i1* 是流入传输线左端的电流。
- *v2* 是传输线右端的电压。
- *i2* 是流入传输线右端的电流。
- *τ* 是传输线延迟。
- *Z0* 是线路特性阻抗。

### 基于延迟且有损

为了引入损耗，第二个选项 `Delay-based and
lossy` 将 *N* 个基于延迟的组件（每个由上述方程定义）通过一组电阻串联连接，如下图所示。

*N* 是大于或等于 1 的整数。*r* = *R* ·
*LEN* / *N*，其中 *R* 是单位长度线路电阻，*LEN* 是线路长度。

### 集总参数 L 型段

以下框图显示了一个 L 型线段的模型。

集总参数参数化使用 *N* 个上述段模型的副本串联连接。

参数如下：

- *R* 是单位长度线路电阻。
- *L* 是单位长度线路电感。
- *C* 是单位长度线路电容。
- *G* 是单位长度线路电导。
- *LEN* 是线路长度。
- *N* 是串联段数。

### 集总参数 π 型段

以下框图显示了一个 π 型线段的模型。

集总参数参数化使用 *N* 个上述段模型的副本串联连接。参数与 L 型段传输线模型定义相同。与 L 型段模型不同，π 型段模型是对称的。

### 集总参数线路模型参数化

集总参数模型（L 型段或 π 型段）是最难仿真的，通常需要比基于延迟且有损模型更多的段数（更大的 N）[1]。

电缆制造商通常不提供单位长度电感值，而是给出特性阻抗。电感、电容和特性阻抗之间的关系为：

|  |  |
| --- | --- |
| *L* = *C* · *Z*02 | **(3)** |

该模块允许您在使用集总参数模型时指定 *L* 或 *Z*0。

### 分布参数线路

与其他选项相比，分布参数线路在特定频率下提供更精确的仿真。然而，这不是频率相关模型。在 **Frequency used for rlcg
specification** 参数中指定的频率点之外，模型的精度会下降。

对于频率相关传输线模型，请参阅 Frequency-Dependent
Overhead Line (Three-Phase)。

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

然后可以重写并求解方程 4 和 5：

I1=Ish,1−2HIrfl,2

I2=Ish,2−2HIrfl,1

以下框图显示了分布参数线路的等效电路。
