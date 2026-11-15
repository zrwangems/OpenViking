---
type: simulink-block
title: 'RF PCB'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / S-Parameters and Linear Components / RF PCB'
documentation_page: 'rfpcb'
documentation_source_path: 'ref/rfpcb.html'
language: zh-CN
chinese_source: worker-translation
---

# RF PCB

## 端口

R2025b 中未记录。

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，从 **Simulation** 选项卡的 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **Object** — RF PCB 对象 `pcbobj`（默认）| PCB components catalog

从工作区指定一个 PCB 组件对象。您可以使用 PCB Components Catalog (RF PCB Toolbox) 中的任一对象，但 `viaSingleEnded` 对象除外。

**注意**

在模块中使用工作区中的 RF PCB 对象之前，至少对一个频率进行分析。要分析 RF PCB 对象，请将该 RF PCB 对象输入到 `sparameters` (RF PCB Toolbox) 对象。

#### RF PCB 几何

### **Layout** — RF PCB 组件布局按钮

点击此按钮可在图窗中可视化 RF PCB 组件的所有金属层和 PCB 形状。实心红色圆圈对应 PCB 馈电点，蓝色实心圆圈对应过孔。

#### 依赖关系

要启用 **Layout** 按钮，请从工作区将 PCB 对象输入到 **Object** 参数，然后单击 **Apply**。

### **3D Geometry** — RF PCB 组件几何按钮

选择此按钮可在图窗中可视化 RF PCB 组件的 3-D 几何。

#### 依赖关系

要启用 **Layout** 按钮，请从工作区将 PCB 对象输入到 **Object** 参数，然后单击 **Apply**。

#### 噪声和 RF 端子

### **Simulate noise** — 模拟热噪声 `'off'`（默认）| `'on'`

选择此参数以模拟天线中由于天线端子处实阻抗引起的热噪声。

#### 依赖关系

要在该模块中模拟热噪声，请首先在 Configuration 模块中选择 **Simulate noise**。

### **Ground and hide negative terminals** — 接地 RF 电路端子 `'on'`（默认）| `'off'`

选择此选项以接地并隐藏负端子。清除此参数以暴露负端子。通过暴露这些端子，您可以将它们连接到模型中的其他部分。

### 建模

要启用此选项卡，请对工作区中的 RF PCB 对象至少分析一个频率。

### **Modeling options** — 对 S-parameters 建模 `Time domain`（默认）| `Frequency domain`

对 S-parameters 建模，指定为：

- `Time domain` — 此选项创建一个解析 rational 模型，该模型近似整个数据范围。
- `Frequency domain` — 此选项针对每个载波频率独立计算基带冲激响应。此技术基于卷积。有关详细信息，请参阅 Compare Time and Frequency Domain Simulation Options for S-parameters。

#### 时域建模

### **Fitting options** — 数据拟合选项 `Share all poles`（默认）| `Fit individually` | `Share poles by column`

数据拟合选项，指定为 `Fit individually`、`Share poles by column` 或 `Share all poles`。此参数使您能够使用 `rational` 对象拟合数据。

拟合结果显示在 Rational fitting results 部分。该模块显示 **Number of independent fits**、**Number of required poles** 和 **Relative error achieved (dB)** 字段。

#### 依赖关系

要启用此参数，请在 **Modeling options** 中选择 `Time domain`。

### **Relative error desired (dB)** — rational 拟合可接受的相对误差 `-40`（默认）| scalar

rational 拟合可接受的相对误差，指定为以 decibels 为单位的 scalar。

#### 依赖关系

要启用此参数，请在 **Modeling options** 中选择 `Time domain`。

#### 频域建模

### **Automatically estimate impulse response duration** — 自动计算冲激响应的选项 `on` | `off`

选择此参数以自动计算冲激响应。清除此参数以使用 **Impulse response duration** 手动指定冲激响应持续时间。

#### 依赖关系

要启用此参数，请在 **Modeling options** 中选择 `Frequency domain`。

### **Impulse response duration** — 冲激响应持续时间 `1e-10`（默认）| scalar

冲激响应持续时间，指定为以 seconds 为单位的 scalar。

#### 依赖关系

要启用此参数：

- 在 **Modeling options** 中选择 `Frequency domain`
- 清除 `Automatically estimate impulse response duration`。

### 可视化

要启用此选项卡，请对工作区中的 RF PCB 对象至少分析一个频率。

### **Source of frequency data** — 频率数据源 `Extracted from data source`（默认）| `User-defined`

频率数据源，指定为：

- `Extracted from data source` — 要启用此选项，请将 **Data source** 设置为 `Data file`。验证该文件包含频率数据。
- `User-specified` — 选择此选项可在 **Frequency data** 中指定频率向量，并在相应下拉列表中指定频率单位。

当 **Source of frequency data** 为 `Extracted from data source` 时，**Data source** 必须设置为 `Data file`。验证指定的 **Data file** 包含频率数据。

当 **Source of frequency data** 为 `User-specified` 时，在 **Frequency data** 参数中指定频率向量。此外，从相应下拉列表中指定单位。

### **Frequency data** — 频率数据范围 `[1e9:1e6:3e9]`（默认）| finite vector

频率数据范围，指定为 finite vector。从相应下拉列表中选择频率单位。

#### 依赖关系

要启用此参数，请将 **Source of frequency data** 设置为 `User-specified`。

### **Plot type** — 数据绘图类型 `X-Y plane`（默认）| `Polar plane` | `Z Smith chart` | `Y Smith chart` | `ZY Smith chart`

数据绘图类型，指定为以下之一：

- `X-Y plane` — 生成数据随频率变化的笛卡尔图。要创建 linear、semilog 或 log-log 图，请相应地设置 **Y-axis scale** 和 **X-axis scale**。
- `Polar plane` — 生成数据的极坐标图。该模块仅绘制与指定频率对应的数据。
- `Z smith chart`、`Y smith chart` 和 `ZY smith chart` — 生成 Smith® 图。该模块仅绘制与指定频率对应的数据。

### **Parameter 1** — 要绘制的 S-Parameters 类型 `S(1,1)`（默认）| `S(1,2)` | `S(2,1)` | `S(2,2)`

要绘制的 S-Parameters 类型，指定为 `S(1,1)`、`S(1,2)`、`S(2,1)` 或 `S(2,2)`。对于 N-port 设备，**Parameter 1** 列出绘制 N-port S-parameters 的所有选项。

### **Parameter 2** — 要绘制的 S-Parameters 类型 `None`（默认）| `S(1,1)` | `S(1,2)` | `S(2,1)` | `S(2,2)` | ...

要绘制的 S-Parameters 类型，指定为 `S(1,1)`、`S(1,2)`、`S(2,1)` 或 `S(2,2)`。

### **Format1** — 绘图格式 `Magnitude (dB)`（默认）| `Magnitude (linear)` | `Angle(degrees)` | `Real` | `Imaginary`

绘图格式，指定为 `Magnitude (dB)`、`Angle(degrees)`、`Real` 或 `Imaginary`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Format2** — 绘图格式 `Magnitude (dB)`（默认）| `Magnitude (linear)` | `Angle(degrees)` | `Real` | `Imaginary`

绘图格式，指定为 `Magnitude (dB)`、`Angle(degrees)`、`Real` 或 `Imaginary`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Y-axis scale** — Y 轴刻度 `Linear`（默认）| `Logarithmic`

Y 轴刻度，指定为 `Linear` 或 `Logarithmic`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **X-axis scale** — X 轴刻度 `Linear`（默认）| `Logarithmic`

X 轴刻度，指定为 `Linear` 或 `Logarithmic`。

#### 依赖关系

要启用此参数，请将 **Plot type** 设置为 `X-Y plane`。

### **Plot** — 绘制指定数据按钮

点击此按钮绘制数据。

## 所属库

RF Blockset / Circuit Envelope / PCB

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

对 RF PCB 组件建模

RF PCB 模块使您能够在 RF Blockset™ circuit envelope 仿真环境中创建、可视化和分析印刷电路板 (PCB) 上所用组件的特性。您可以从 PCB Components Catalog (RF PCB Toolbox) 创建传输线、分路器、耦合器、巴伦及其他组件，但 `viaSingleEnded` 对象除外。

**注意**

要使用此模块，您需要 RF PCB Toolbox™ 许可证。
