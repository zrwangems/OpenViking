---
type: simulink-block
title: 'Noise'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Sources'
documentation_page: 'noise'
documentation_source_path: 'ref/noise.html'
language: zh-CN
chinese_source: worker-translation
---

# Noise

## 端口

R2025b 中未记录。

## 参数

### **Source type** — 噪声类型 `Ideal voltage`（默认）| `Ideal current`

噪声类型，指定为 `Ideal voltage` 或 `Ideal current`。

### **Noise distribution** — 噪声分布类型 `White`（默认）| `Piece-wise linear` | `Colored`

噪声分布类型，指定为 `White`、`Piece-wise linear` 或 `Colored`。

### **Noise power spectral density** — 单边噪声功率谱分布 `0`（默认）| 标量 | 向量

单边噪声功率谱分布（PSD），指定为以 V2/Hz 或 A2/Hz 为单位的标量或向量。单边 PSD 随噪声分布类型而变化。当您将 **Noise distribution** 参数设置为以下选项之一时：

- `White` — 将 **Noise power spectral density** 参数指定为非负标量。白噪声的噪声 PSD 在所有频率上恒定，噪声功率取决于载波的带宽或时间步长。这是一个非相关噪声源。
- `Piece-wise linear` — 将 **Noise power spectral density** 参数指定为向量。该向量的长度必须与您在 **Frequencies** 参数中指定的向量长度相同。

  对于每个载波，噪声源的行为类似于白噪声源。噪声源的噪声 PSD 取决于载波，您可以通过在噪声频谱密度曲线上对载波频率执行线性插值来计算它。

  噪声频谱密度曲线表示噪声 PSD 随频率的变化。该模块使用您在 **Noise power spectral density** 和 **Frequencies** 参数中指定的值来确定此曲线。
- `Colored` — 将 **Noise power spectral density** 参数指定为向量。该向量的长度必须与您在 **Frequencies** 参数中指定的向量长度相同。这是一个相关噪声源。

  载波频率处带宽内的噪声频谱密度由噪声频谱密度曲线确定，除非您将 **Impulse response duration** 参数设置为 `0`。

单边 PSD 的单位取决于 **Source type** 参数。当您将 **Source type** 参数设置为：

- `Ideal voltage` — 该模块以 V2/Hz 为单位模拟 PSD。
- `Ideal Current` — 该模块以 A2/Hz 为单位模拟 PSD。

### **Frequencies** — 分段线性噪声分布的频率 `0 Hz`（默认）| 非负频率向量 | `Hz` | `kHz` | `MHz` | `GHz`

分段线性噪声分布的频率，指定为非负频率向量。

### **Automatically estimate impulse response duration** — 估计冲激响应持续时间 `on`（默认）| `off`

选择此参数以使模块自动估计冲激响应持续时间，或清除此参数以使用 **Impulse response duration** 参数指定冲激响应持续时间。

#### 依赖关系

要启用此参数，请将 **Noise Distribution** 设置为 `Colored`。

### **Impulse response duration** — 用于模拟有色噪声的冲激响应持续时间 `1e-10 s`（默认）| 标量 | `s` | `ms` | `us` | `ns`

用于模拟有色噪声的冲激响应持续时间，指定为以 s、ms、us 或 ns 为单位的标量。当您将 **Impulse response duration** 参数设置为 `0` 时，软件会像 `Piece-wise linear` 噪声源一样进行线性插值。

#### 依赖关系

要启用此参数，请将 **Noise Distribution** 设置为 `Colored` 并清除 **Automatically estimate impulse response duration**。

### **Ground and hide negative terminals** — 接地并隐藏 RF 电路端子 `on`（默认）| `off`

选择此选项可在内部接地并隐藏负端子。要暴露负端子，请清除该选项。通过暴露这些端子，您可以将它们连接到模型的其他部分。

默认情况下，此选项处于选中状态。

## 所属库

RF Blockset / Circuit Envelope / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

### R2021b：Noise 模块图标已更新

从 R2021b 开始，Noise 模块图标已更新。当您打开在 R2021b 之前创建的包含 Noise 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

在 RF 系统中使用电流或电压噪声源对噪声进行建模

使用 Noise 模块将噪声建模为模块的理想电流或电压源。使用此模块，您可以选择噪声分布类型为白噪声、分段线性或有色噪声。当您使用 Noise 模块在 RF 模型中仿真噪声时，请在 Configuration 模块中选中 **Simulate noise** 复选框。否则，模型将在无噪声条件下进行仿真。Noise 模块不依赖于 Configuration 中的 **Temperature** 参数。

Noise 模块掩码图标是动态的，会显示当前的源类型。下表显示了此模块上的图标如何根据您在模块的 **Source type** 参数上设置的源类型而变化。

| Source type：`Ideal voltage` | Source type：`Ideal current` |
| --- | --- |
| 正弦波模块图标，Source type 设置为 Ideal voltage。 | 正弦波模块图标，Source type 设置为 Ideal current。 |
