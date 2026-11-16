---
type: simulink-block
title: 'Average-Value Voltage Source Converter (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'averagevaluevoltagesourceconverterthreephase'
documentation_source_path: 'ref/averagevaluevoltagesourceconverterthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Average-Value Voltage Source Converter (Three-Phase)

## 端口

### 输入

### **ModWave** — 调制波向量

与归一化调制波关联的物理信号输入端口。

#### 依赖项

要启用此端口，请将 **Input type** 设置为 `Modulation wave`。

### **Vt** — 相间 RMS 电压标量

*自 R2024a 起*

与相间 RMS 电压关联的物理信号输入端口。

#### 依赖项

要启用此端口，请将 **Input type** 设置为 `Sinusoidal magnitude and phase shift`。

### **ph** — 相移标量

*自 R2024a 起*

与相移关联的物理信号输入端口。

#### 依赖项

要启用此端口，请将 **Input type** 设置为 `Sinusoidal magnitude and phase shift`。

### 守恒端口

### **~** — 电压电气

与电压关联的可扩展电气守恒端口。有关详细信息，请参阅 three-phase port。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a** — *a* 相电气

与 *a* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相电气

与 *b* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相电气

与 *c* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **+** — 正极端子电气

与正极端子相关联的电气守恒端口。

### **-** — 负极端子电气

与负极端子相关联的电气守恒端口。

### **H** — 热端口 热

热守恒端口。

#### 依赖项

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对热参数建模。

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是采用复合三相端口还是扩展三相端口。

### **AC frequency** — AC 频率 `Variable`（默认）| `Constant`

是否采用可变或恒定 AC 频率：

- `Variable` — 如果生成的 AC 电压频率变化，此选项支持变压变频（VVVF）和变压恒频（VVCF）应用，但模块仅以时间仿真模式工作。
- `Constant` — 如果生成的 AC 电压频率恒定，此选项支持变压恒频（VVCF）应用，并且模块可在时间和频率-时间仿真模式下工作。您还可以在三相调制波输入或幅值和相位调制输入之间选择。

### **Input type** — 输入类型 `Modulation wave`（默认）| `Sinusoidal magnitude and phase shift`

*自 R2024a 起*

用于将模块输入指定为三相调制波，或通过正弦幅值和相移指定的选项。

#### 依赖项

要启用此参数，请将 **AC frequency** 设置为 `Constant`。

### **Rated electrical frequency** — 额定电气频率 `60` `Hz` | scalar

额定电气频率。此参数的值必须等于模型中其他正弦源（如果存在）的额定电气频率值。

#### 依赖项

要启用此参数，请将 **AC frequency** 设置为 `Constant`。

### **Losses parameterization** — 损耗参数化 `Fixed`（默认）| `Coefficients: loss=Pfixed+ks*vdc*Irms+kc1*Irms+kc2*Irms^2` | `Profile: loss=f(Irms,vdc_nom)`

功率损耗的参数化选项。您可以选择以下选项之一：

- `Fixed` — 功率损耗固定，并等于 **Fixed power loss** 参数的值。
- `Coefficients: loss=Pfixed+ks*vdc*Irms+kc1*Irms+kc2*Irms^2` — 总功率损耗通过将开关损耗、导通损耗和静态损耗相加得到。
- `Profile: loss=f(Irms,vdc_nom)` — 功率损耗是 RMS 电流和标称直流母线电压的函数，并从功率损耗曲线获得。

### **Fixed power loss** — 功率损耗 `1` `W`（默认）

半导体组件上的固定功率损耗，单位为 W。输入功率等于固定功率损耗加上输出功率。

#### 依赖项

要启用此参数，请将 **Losses parameterization** 设置为 `Fixed` 或 `Coefficients: loss=Pfixed+ks*vdc*Irms+kc1*Irms+kc2*Irms^2`。

### **Switching losses coefficient, ks** — 开关损耗系数 `0.01`（默认）

比例常数，取决于开通和关断时间间隔以及开关频率。

#### 依赖项

要启用此参数，请将 **Losses parameterization** 设置为 `Coefficients: loss=Pfixed+ks*vdc*Irms+kc1*Irms+kc2*Irms^2`。

### **Conduction losses coefficient, kc1** — 导通损耗第一系数 `1.7` `V`（默认）

导通损耗系数，取决于晶体管的通态零电流集电极-发射极电压以及二极管的正向电压降。

#### 依赖项

要启用此参数，请将 **Losses parameterization** 设置为 `Coefficients: loss=Pfixed+ks*vdc*Irms+kc1*Irms+kc2*Irms^2`。

### **Conduction losses coefficient, kc2** — 导通损耗第二系数 `0.01` `Ohm`（默认）

导通损耗系数，取决于晶体管和反并联二极管的状态电阻。

#### 依赖项

要启用此参数，请将 **Losses parameterization** 设置为 `Coefficients: loss=Pfixed+ks*vdc*Irms+kc1*Irms+kc2*Irms^2`。

### **Converter losses** — 变换器损耗向量 `[100, 800, 1870, 3250, 4900]` `W`（默认）

功率损耗值的向量。

#### 依赖项

要启用此参数，请将 **Losses parameterization** 设置为 `Profile: loss=f(Irms,vdc_nom)`。

### **RMS current for converter losses** — RMS 电流向量 `[10, 100, 200, 300, 400]` `A`（默认）

与 **Converter losses** 参数值关联的均方根电流向量。

#### 依赖项

要启用此参数，请将 **Losses parameterization** 设置为 `Profile: loss=f(Irms,vdc_nom)`。

### **Nominal dc-link voltage** — 标称直流母线电压 `300` `V`（默认）

标称电压。

#### 依赖项

要启用此参数，请将 **Losses parameterization** 设置为 `Profile: loss=f(Irms,vdc_nom)`。

### **Thermal mass** — 热质量 `30000` `J/K`（默认）

热质量。

#### 依赖项

要启用此参数，请将 **Modeling option** 设置为 `Show thermal port`。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024a：指定幅值和相位调制输入

您现在可以使用相量（如幅值和相移）作为模块输入。要指定幅值和相位调制输入，请将 **AC frequency** 参数设置为 `Constant`，并将 **Input type** 参数设置为 `Sinusoidal magnitude and phase shift`。

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在较早版本中保存的模型内，请检查此模块的 **Electrical connection** 参数。

## 描述

三相平均值双向 AC/DC 电压源变换器

Average-Value Voltage Source Converter (Three-Phase) 模块根据输入三相调制波将电能从 AC 转换为 DC 电压，或从 DC 转换为 AC 电压。您可以直接指定调制波，或通过相量（如幅值和相移）指定。相应的输入功率等于固定功率损耗与输出功率之和。

此模块可在时间和频率-时间仿真模式下工作。如果将 **AC frequency** 参数设置为 `Variable`，此模块仅以时间仿真模式工作。如果选择 `Constant`，此模块可在时间和频率-时间仿真模式下工作。有关详细信息，请参阅 Frequency and Time Simulation Mode。

### 损耗参数化

开关损耗、导通损耗和静态损耗是变换器的主要热源。

开关损耗由以下方程定义：

Pswitching=ksvdcIrms

其中：

- *ks* 是比例常数，取决于开通和关断时间间隔以及开关频率。通过设置 **Switching losses coefficient, ks** 参数来指定此值。
- *vdc* 是直流母线电压。
- Irms=(ia−idc)2+(ib−idc)2+(ic−idc)23 是均方根 (RMS) 相电流，其中 idc=ia+ib+ic3。

导通损耗由以下方程定义：

Pconduction=kc1Irms+kc2Irms2

其中：

- *kc1* 是导通损耗系数，取决于晶体管的通态零电流集电极-发射极电压以及二极管的正向电压降。通过设置 **Conduction losses coefficient, kc1** 参数来指定此值。
- *kc2* 是导通损耗系数，取决于晶体管和反并联二极管的状态电阻。通过设置 **Conduction losses coefficient, kc2** 参数来指定此值。

静态损耗由 **Fixed power loss** 参数 *Pfixed* 定义。

开关损耗、导通损耗和静态损耗之和定义变换器的总功率损耗：

Ploss=Pswitching+Pconduction+Pfixed.

如果不可用，您还可以通过将 **Losses parameterization** 参数设置为 `Profile: loss=f(Irms,vdc_nom)`，从功率损耗曲线获得 *ks*、*kc1*、*kc2* 和 *Pfixed* 参数值。然后该模块求解此方程并计算参数值：

[P1⋮Pn]=[1vdc\_nomIrms,1Irms,1Irms,12⋮⋮⋮⋮1vdc\_nomIrms,nIrms,nIrms,n2][Pfixedkskc1kc2]

其中 [P1⋮Pn] 是功率损耗值向量 **Converter losses**，对应于 **RMS current for converter losses** 参数 [Irms,1⋮Irms,n]，以及 **Nominal dc-link voltage** *vdc\_nom*。

### 对热效应建模

此模块有一个可选热端口。要控制热端口的可见性，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含一个热守恒端口。
