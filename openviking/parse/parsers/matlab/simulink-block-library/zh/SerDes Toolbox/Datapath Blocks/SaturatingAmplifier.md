---
type: simulink-block
title: 'SaturatingAmplifier'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'saturatingamplifier'
documentation_source_path: 'ref/saturatingamplifier.html'
language: zh-CN
chinese_source: worker-translation
---

# SaturatingAmplifier

## 端口
```yaml
ports:
- name: WaveIn
  summary: 输入基带信号 标量 | 向量
  direction: input
  data_types: double
- name: WaveOut
  summary: 限幅输出电压 标量 | 向量
  direction: output
  data_types: double
```

### 输入

### **WaveIn** — 输入基带信号 标量 | 向量

输入基带信号，可以是按样本指定的标量信号，也可以是冲激响应向量信号。

**数据类型：** `double`
### 输出

### **WaveOut** — 限幅输出电压 标量 | 向量

由 SaturatingAmplifier 模块指定的限幅输出电压。如果输入信号是按样本指定的标量信号，则输出也是标量。如果输入信号是冲激响应向量信号，则输出也是向量。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Mode
  summary: 放大器工作模式 On（默认）| Off
  group: ''
- name: Specification
  summary: 限幅放大器输出的输入规格 'Limit and Linear Gain'（默认）| 'VinVout'
  group: ''
- name: Limit
  summary: 限幅放大器的限幅电压 1.2（默认）| 实正标量
  group: ''
- name: LinearGain
  summary: 线性区域的放大器增益 1（默认）| 实正标量
  group: ''
- name: VinVout
  summary: 输入及对应的输出电压响应 *N*×2 矩阵 | *N*×2×*M* 矩阵
  group: ''
- name: Slice select
  summary: 选择要使用的 3D GPZ 矩阵的哪个角 0（默认）| 非负标量整数
  group: ''
- name: Visualize Response
  summary: 绘制输入与输出电压响应按钮
  group: ''
- name: Mode
  summary: 在 IBIS-AMI 模型中包含 Mode 参数 on（默认）| off
  group: ''
- name: Slice select
  summary: 在 IBIS-AMI 模型中包含 Slice select 参数 on（默认）| off
  group: ''
```

### **Mode** — 放大器工作模式 `On`（默认）| `Off`

放大器工作模式：

- `Off` — 旁路 SaturatingAmplifier，输入波形保持不变。
- `On` — SaturatingAmplifier 根据电压输入与电压输出响应曲线对输入波形进行缩放。

#### 程序化使用

- 使用 `get_param(gcb,'Mode')` 查看当前饱和放大器的工作**模式**。
- 使用 `set_param(gcb,'Mode',value)` 将放大器设置为特定的**模式**。

### **Specification** — 限幅放大器输出的输入规格 `'Limit and Linear Gain'`（默认）| `'VinVout'`

限幅放大器输出的输入规格：

- `'Limit and Linear Gain'` — 使用**Limit**和**Linear Gain**中指定的值创建软限幅电压输入与电压输出响应曲线。
- `'VinVout'` — 生成与**VinVout**中指定的输入电压对应的输出电压。该模块使用无记忆非线性响应将输入电压映射到输出电压。如果任何输入电压点超出指定值范围，则该特定输入电压的输出将通过插值计算。

#### 程序化使用

- 使用 `get_param(gcb,'Specification')` 查看饱和放大器当前的**Specification**。
- 使用 `set_param(gcb,'Specification',value)` 将饱和放大器设置为特定的**Specification**。

**数据类型：** `char`

### **Limit** — 限幅放大器的限幅电压 `1.2`（默认）| 实正标量

限幅放大器的限幅电压，指定为以 V 为单位的实正标量。

#### 依赖关系

此参数仅在**Specification**选择为 `'Limit and Linear Gain'` 时可用。

#### 程序化使用

- 使用 `get_param(gcb,'Limit')` 查看饱和放大器**Limit**的当前值。
- 使用 `set_param(gcb,'Limit',value)` 将**Limit**设置为特定值。

**数据类型：** `double`

### **LinearGain** — 线性区域的放大器增益 `1`（默认）| 实正标量

线性区域的放大器增益，指定为无量纲的实正标量。

#### 依赖关系

此参数仅在**Specification**选择为 `'Limit and Linear Gain'` 时可用。

#### 程序化使用

- 使用 `get_param(gcb,'LinearGain')` 查看饱和放大器**LinearGain**的当前值。
- 使用 `set_param(gcb,'LinearGain',value)` 将**LinearGain**设置为特定值。

**数据类型：** `double`

### **VinVout** — 输入及对应的输出电压响应 *N*×2 矩阵 | *N*×2×*M* 矩阵

输入及对应的输出电压响应，指定为以伏特为单位的 *N*×2 矩阵（2-D）或 *N*×2×*M* 矩阵（3-D）。*N* 是电压样本数，*M* 是切片数。

如果**VinVout**是 3-D 矩阵，您可以选择使用**VinVout**的哪个切片。要了解有关定义 3-D **VinVout**矩阵的更多信息，请参阅 Define Saturating Amplifier with 3D VinVout Matrix。

#### 依赖关系

此参数仅在**Specification**选择为 `'VinVout'` 时可用。

#### 程序化使用

- 使用 `get_param(gcb,'VinVout')` 查看饱和放大器**VinVout**表的当前值。
- 使用 `set_param(gcb,'VinVout',value)` 将**VinVout**设置为特定值。

**数据类型：** `double`

### **Slice select** — 选择要使用的 3D GPZ 矩阵的哪个角 `0`（默认）| 非负标量整数

选择在 CTLE 配置期间要使用的 3-D `VinVout` 矩阵的哪个切片、族或角。

你必须将 **Specification** 参数设置为 `'VinVout'`，才能有效使用 **Slice Select** 参数。根据你的 `VinVout` 矩阵中有多少切片可用，你可以随后从下拉菜单中提供的从零开始的索引中选择你感兴趣的切片。

#### 程序化使用

- 使用 `get_param(gcb,'SliceSelect')` 查看 **Slice select** 的当前值。
- 使用 `set_param(gcb,'SliceSelect',value)` 将 **Slice select** 设置为特定值。

**数据类型：** `double`

### **Visualize Response** — 绘制输入与输出电压响应按钮

点击以绘制 Saturating Amplifier 模块的输入与输出电压响应。

#### IBIS-AMI 参数

### **Mode** — 在 IBIS-AMI 模型中包含 Mode 参数 on（默认）| off

选择以在 IBIS-AMI 文件中将 **Mode** 作为参数包含。如果你取消选择 **Mode**，它将从 AMI 文件中移除，实际上会将 **Mode** 硬编码为其当前值。

### **Slice select** — 在 IBIS-AMI 模型中包含 Slice select 参数 on（默认）| off

选择以在 IBIS-AMI 文件中将 **Slice select** 作为参数包含。如果你取消选择 **Slice select**，它将从 AMI 文件中移除，实际上会将 **Slice select** 硬编码为其当前值。
## 所属库

SerDes Toolbox / Datapath Blocks

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

### R2023b: Slice Select

你现在可以选择在 CTLE 配置期间要使用的 3-D GPZ 矩阵的哪个切片、族或角。

## 描述

对饱和放大器进行建模

SaturatingAmplifier 模块根据电压输入与电压输出响应来缩放输入波形。电压输入与电压输出响应由 **Limit** 和 **Linear Gain** 定义的软削波响应指定，或由 **VinVout** 矩阵指定。SaturatingAmplifier 模块对输入波形应用无记忆非线性。
