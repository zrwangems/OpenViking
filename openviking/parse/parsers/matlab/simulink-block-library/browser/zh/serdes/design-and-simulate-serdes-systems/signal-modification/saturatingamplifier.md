---
type: simulink-block
title: 'SaturatingAmplifier'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Design and Simulate SerDes Systems / Signal Modification'
documentation_page: 'saturatingamplifier'
documentation_source_path: 'ref/saturatingamplifier.html'
language: zh-CN
chinese_source: worker-translation
---

# SaturatingAmplifier

## 端口

### 输入

### **WaveIn** — 输入基带信号 标量 | 向量

输入基带信号，可以是指定为标量的逐样本信号，或脉冲响应向量信号。

**数据类型：** `double`

### 输出

### **WaveOut** — 削波输出电压 标量 | 向量

削波输出电压，由 SaturatingAmplifier 模块指定。如果输入信号是指定为标量的逐样本信号，则输出也是标量。如果输入信号是脉冲响应向量信号，则输出也是向量。

**数据类型：** `double`

## 参数

### **Mode** — 放大器工作模式 `On`（默认）| `Off`

放大器工作模式：

- `Off` — SaturatingAmplifier 被旁路，输入波形保持不变。
- `On` — SaturatingAmplifier 根据电压输入与电压输出响应缩放输入波形。

#### 编程用法

- 使用 `get_param(gcb,'Mode')` 查看饱和放大器的当前工作 **Mode**。
- 使用 `set_param(gcb,'Mode',value)` 将放大器设置为特定 **Mode**。

### **Specification** — 用于限制放大器输出的输入规格 `'Limit and Linear Gain'`（默认）| `'VinVout'`

用于限制放大器输出的输入规格：

- `'Limit and Linear Gain'` — 使用 **Limit** 和 **Linear Gain** 中指定的值创建软削波电压输入与电压输出响应。
- `'VinVout'` — 生成与 **VinVout** 中指定的输入电压对应的输出电压。该模块使用无记忆非线性响应将输入电压映射到输出电压。如果任何输入电压点落在指定值之外，则对该特定输入电压的输出进行插值。

#### 编程用法

- 使用 `get_param(gcb,'Specification')` 查看饱和放大器的当前 **Specification**。
- 使用 `set_param(gcb,'Specification',value)` 将饱和放大器设置为特定 **Specification**。

**数据类型：** `char`

### **Limit** — 限幅放大器的削波电压 `1.2`（默认）| 正实数标量

限幅放大器的削波电压，指定为以 V 为单位的正实数标量。

#### 依赖关系

仅当 **Specification** 选择为 `'Limit and Linear Gain'` 时，此参数可用。

#### 编程用法

- 使用 `get_param(gcb,'Limit')` 查看饱和放大器的 **Limit** 当前值。
- 使用 `set_param(gcb,'Limit',value)` 将 **Limit** 设置为特定值。

**数据类型：** `double`

### **LinearGain** — 线性区中的放大器增益 `1`（默认）| 正实数标量

线性区中的放大器增益，指定为无单位的正实数标量。

#### 依赖关系

仅当 **Specification** 选择为 `'Limit and Linear Gain'` 时，此参数可用。

#### 编程用法

- 使用 `get_param(gcb,'LinearGain')` 查看饱和放大器的 **LinearGain** 当前值。
- 使用 `set_param(gcb,'LinearGain',value)` 将 **LinearGain** 设置为特定值。

**数据类型：** `double`

### **VinVout** — 输入及对应输出电压响应 *N*×2 矩阵 | *N*×2×*M* 矩阵

输入及对应输出电压响应，指定为以 volts 为单位的 *N*×2 矩阵（2-D）或 *N*×2×*M* 矩阵（3-D）。*N* 是电压样本数，*M* 是切片数。

如果 **VinVout** 是 3-D 矩阵，则可以选择要使用 **VinVout** 的哪个切片。要了解有关定义 3-D **VinVout** 矩阵的更多信息，请参阅使用 3D VinVout 矩阵定义饱和放大器。

#### 依赖关系

仅当 **Specification** 选择为 `'VinVout'` 时，此参数可用。

#### 编程用法

- 使用 `get_param(gcb,'VinVout')` 查看饱和放大器的当前 **VinVout** 表格值。
- 使用 `set_param(gcb,'VinVout',value)` 将 **VinVout** 设置为特定值。

**数据类型：** `double`

### **Slice select** — 选择要使用的 3D GPZ 矩阵的哪个角 `0`（默认）| 非负标量整数

选择 CTLE 配置期间要使用的 3-D `VinVout` 矩阵的哪个切片、族或角。

必须将 **Specification** 参数设置为 `'VinVout'`，才能有效使用 **Slice Select** 参数。根据 `VinVout` 矩阵中可用的切片数量，您随后可以从下拉菜单中提供的从零开始的索引中选择感兴趣的切片。

#### 编程用法

- 使用 `get_param(gcb,'SliceSelect')` 查看 **Slice select** 的当前值。
- 使用 `set_param(gcb,'SliceSelect',value)` 将 **Slice select** 设置为特定值。

**数据类型：** `double`

### **Visualize Response** — 绘制输入与输出电压响应按钮

点击以绘制 Saturating Amplifier 模块的输入与输出电压响应。

#### IBIS-AMI 参数

### **Mode** — 在 IBIS-AMI 模型中包含 Mode 参数 on（默认）| off

选择以将 **Mode** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Mode**，则会将其从 AMI 文件中移除，从而有效地将 **Mode** 硬编码为其当前值。

### **Slice select** — 在 IBIS-AMI 模型中包含 Slice select 参数 on（默认）| off

选择以将 **Slice select** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Slice select**，则会将其从 AMI 文件中移除，从而有效地将 **Slice select** 硬编码为其当前值。

## 所属库

SerDes Toolbox / Datapath Blocks

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

### R2023b：Slice Select

现在，您可以选择 CTLE 配置期间要使用的 3-D GPZ 矩阵的哪个切片、族或角。

## 描述

对饱和放大器进行建模

SaturatingAmplifier 模块根据电压输入与电压输出响应缩放输入波形。电压输入与电压输出响应由 **Limit** 和 **Linear Gain** 定义的软削波响应指定，或由 **VinVout** 矩阵指定。SaturatingAmplifier 模块对输入波形应用无记忆非线性。
