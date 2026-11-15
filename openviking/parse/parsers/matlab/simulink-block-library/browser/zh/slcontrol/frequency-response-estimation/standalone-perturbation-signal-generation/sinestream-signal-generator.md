---
type: simulink-block
title: 'Sinestream Signal Generator'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Frequency Response Estimation / Standalone Perturbation Signal Generation'
documentation_page: 'sinestreamsignalgenerator'
documentation_source_path: 'ug/sinestreamsignalgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Sinestream Signal Generator

## 端口

### 输入

### **start/stop** — 启动和停止信号生成 标量

要启动和停止信号生成过程，请在 **start/stop** 端口提供信号。当该信号的值从以下状态变化时：

- 负值或零变为正值，信号生成启动
- 正值变为负值或零，信号生成停止

通常，您可以使用从 0 变为 1 的信号来启动实验，并使用从 1 变为 0 的信号来停止实验。当实验未运行时，模块不会在输出端口生成扰动。

生成足够长的扰动信号，使算法能够收集充足的数据，从而对其探测的所有频率都能获得良好的估计。模块会在模块参数的 **信号长度** 部分显示推荐的实验长度。该值基于实验模式和您为实验指定的频率。

推荐的实验长度为：

∑i2πωiNp,i+2TsNfreq,

其中：

- *ωi* 是在 **Frequencies** 参数中指定的第 *i* 个频率（单位为 rad/s）。
- *Nfreq* 是 **Frequencies** 中的频率数量。
- *N**p*,*i* 是 **Number of signal periods** 参数的对应值。
- *Ts* 是由 **Sample time (Ts)** 参数指定的实验采样时间。

在实验期间避免对被控对象造成任何负载扰动。负载扰动会使被控对象输出发生畸变，并降低频率响应估计的精度。

**数据类型：** `single` | `double`

### **w** — 用于估计实验的频率 向量

为 **Frequencies** 参数提供值。有关如何选择频率的信息，请参阅 **Frequencies** 参数。

当您通过此端口提供频率时，请使用 **Number of frequencies in the excitation signal** 参数指定频率数量。

#### 依赖关系

要启用此端口，请在 **Excitation Signal Source** 中选择 **External ports**。

**数据类型：** `single` | `double`

### **amp** — 扰动幅值 标量 | 向量

为 **Amplitudes** 参数提供值。有关详细信息，请参阅 **Amplitudes** 参数。

#### 依赖关系

要启用此端口，请在 **Excitation Signal Source** 中选择 **External Ports**。

**数据类型：** `single` | `double`

### 输出

### **sin**, **cos**, **sincos** — Sinestream 扰动信号 标量 | 向量

Sinestream 扰动信号。

**数据类型：** `single` | `double`

### **3ϕ-sin**, **3ϕ-cos**, **3ϕ-sincos** — 三相 Sinestream 扰动信号 向量

三相 Sinestream 扰动信号。

要提取输出信号中的各相，请使用 Demux 模块。

#### 依赖关系

要启用此端口，请选择 **Generate three-phase perturbation signal**。

**数据类型：** `single` | `double`

### **idx w** — 输出频率索引 标量 | 向量

此端口处的信号输出所生成频率分量的对应索引。

#### 依赖关系

**数据类型：** `single` | `double`

## 参数

要以交互方式编辑模块参数，请使用 **属性检查器**。在 Simulink® 工具条中，在 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **Sample time (Ts)** — 采样时间 0.1（默认）| 正标量 | –1

模块是一个离散时间模块，以固定采样时间运行，该采样时间由此参数指定。您可以估计的最大频率是 Nyquist 频率，*π*/*Ts* rad/s。最佳实践是使用至少比 Nyquist 频率快五倍的采样时间。

*Ts* = *π*/(5*ωmax*) ≅ 0.6/*ωmax* 或 0.1/*fmax*,

这里，*ωmax* 是 **Frequencies** 参数中的最高频率，单位为 rad/s；*fmax* 是最高频率，单位为 Hz。采样时间必须足够小，以便估计所需的最快频率，但也不能小到引入不必要的计算负担。

如果将该采样时间设置为 –1，则软件会在编译时根据模块外部的源确定采样时间。将采样时间设置为 –1 会禁用模块中的内部检查，这些检查用于确保您的估计频率低于 Nyquist 频率。

#### 提示

如果您希望在应用程序中以不同的采样时间运行部署后的模块，请将此参数设置为 –1，并将该模块放入 Triggered Subsystem 中。然后，以所需的采样时间触发该子系统。如果您不打算在部署后更改采样时间，请指定一个固定且有限的采样时间。

### **Data Type** — 浮点精度 `double`（默认）| `single`

根据仿真环境或硬件要求指定浮点精度。

### **Excitation signal source** — 激励信号源 **Block parameters**（默认）| **External ports**

指定是通过模块参数还是通过外部端口提供实验扰动信号的频率和幅值。

- **Block parameters** — 选择此项可启用 **Frequencies** 和 **Amplitudes** 参数。
- **External ports** — 选择此项可启用 **w** 和 **amp** 输入端口。如果您希望在部署后更改扰动信号的频率和幅值，请使用此选项。

### **Frequencies** — 用于估计的频率 [0.5 1 2]（默认）| 向量

用于估计被控对象频率响应的频率。模块会在每个这些频率处注入扰动。您可以估计的最高频率受 Nyquist 频率 *π*/*Ts* rad/s 限制，其中 *Ts* 是您为 **Sample time (Ts)** 参数设置的值。

对于频率的数量或范围没有推荐限制。然而，由于 Sinestream 扰动的顺序特性，您添加的每个频率点都会增加所需的实验时间（有关详细信息，请参阅 **start/stop** 输入端口）。此外，频率范围过宽会要求您为高频使用快速采样时间，而这对于较低频率而言效率低下。

#### 提示

此参数不可调。要在部署后提供频率，请将 **Excitation Signal Source** 设置为 **External ports**，并使用 **w** 输入端口。

#### 依赖关系

要启用此参数，请将 **Excitation Signal Source** 设置为 **Block parameters**。

### **Amplitudes** — 注入扰动的幅值 1（默认）| 标量 | 向量

指定注入到被控对象中的扰动信号的幅值。要对所有频率使用相同的幅值，请指定一个标量值。如果您知道响应在要估计的频率范围内变化显著，则可以使用向量为每个频率指定不同的幅值。例如，您可以在已知谐振频率附近使用较小的值，并在滚降频率以上使用较大的值。该向量必须与您为 **Frequencies** 提供的向量长度相同。

幅值必须：

- 足够大，以使扰动克服被控对象执行器中的任何死区，并生成高于噪声水平的响应
- 足够小，以使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

#### 提示

此参数不可调。要在部署后提供幅值，请将 **Excitation Signal Source** 设置为 **External ports**，并使用 **amp** 输入端口。

#### 依赖关系

要启用此参数，请将 **Excitation Signal Source** 设置为 **Block parameters**。

### **Number of frequencies** — 外部提供的频率数量 3（默认）| 正整数

当您通过外部端口 **w** 提供实验频率时，请使用此参数指定频率数量（即 **w** 处向量信号的长度）。

#### 依赖关系

要启用此参数，请将 **Excitation Signal Source** 设置为 **External ports**。

### **Number of signal periods** — 每个正弦波处于最大幅值的周期数 6（默认）| 标量 | 向量

每个正弦波处于最大幅值的周期数，指定为以下之一：

- 标量 — 对所有频率使用相同的周期数。
- 长度等于 **Frequency** 长度的向量 — 对每个频率使用不同的周期数。

### 高级设置

### **Waveform Type** — 波形类型 **sine**（默认）| **cosine** | **both**

将扰动信号的波形类型指定为 sine、cosine 或同时为两者（sincos）。

### **Phase Shift** — 波的相移 0（默认）| 标量 | 向量

指定波形中的相移。

### **Generate three-phase perturbation signal** — 生成三相扰动信号 `off`（默认）| `on`

生成波之间相位差为 120° 的三相扰动信号。当您想要辨识三相交流电力系统的频率响应时，三相信号很有用。

### **Show frequency index port** — 启用频率索引端口 `off`（默认）| `on`

选择此选项可启用 **idx w** 端口。

## 所属库

Simulink Control Design / Signal Generation

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

生成用于被控对象频率响应估计的 Sinestream 输入信号

使用此模块生成 Sinestream 输入扰动信号。此模块允许您生成标量或向量信号，包括三相 sin、cos 或两者（sincos）信号。当您想要辨识三相交流电力系统的频率响应时，三相信号很有用。例如，您可以使用生成的信号来测量将可再生能源连接到三相交流电网的功率逆变器的阻抗。有关 Sinestream 输入信号的详细信息，请参阅 Sinestream 输入信号。

当您想要生成扰动信号，以在桌面仿真中或通过代码生成在硬件上注入到您的被控对象模型中时，此模块很有用。然后，您可以收集被控对象对扰动信号的响应数据，并执行自定义处理以辨识被控对象特性。
