---
type: simulink-block
title: 'PRBS Signal Generator'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Frequency Response Estimation / Standalone Perturbation Signal Generation'
documentation_page: 'prbssignalgenerator'
documentation_source_path: 'ug/prbssignalgenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# PRBS Signal Generator

## 端口

### 输入

### **start/stop** — 启动和停止估计实验 标量

要启动和停止估计过程，请在 `start/stop` 端口提供信号。当信号值从以下状态变化时：

- 负值或零变为正值时，信号生成启动
- 正值变为负值或零时，信号生成停止

通常，您可以使用从 0 变为 1 的信号来启动实验，并使用从 1 变为 0 的信号来停止实验。当实验未运行时，模块不会在输出端口生成扰动。

让实验运行足够长时间，以便算法收集足够的数据，从而在它探测的所有频率上获得良好的估计。模块在模块参数的 **Signal Length** 部分显示建议的实验长度。此值基于实验模式以及您为实验指定的频率。

建议的实验长度为：

Ts(2n−1)Np，

其中：

- *T*s 是实验采样时间，由 **Sample time (Ts)** 参数指定。
- *n* 是 PRBS 信号阶数，由 **Signal order** 参数指定。
- *N*p 是 PRBS 信号中的周期数，由 **Number of periods** 参数指定。

在实验期间避免对被控对象造成任何负载扰动。负载扰动可能会使被控对象输出失真，并降低频率响应估计的精度。

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

### **prbs** — PRBS 扰动信号 标量

模块在此端口生成 PRBS 扰动信号。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® Toolstrip 中，在 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **Sample time (Ts)** — 采样时间 0.1 (默认) | 正标量 | –1

该模块是一个离散时间模块，以固定采样时间运行，该采样时间由本参数指定。您可以估计的最大频率是奈奎斯特频率 *π*/*Ts* rad/s。最佳实践是使用至少比奈奎斯特频率快五倍的采样时间。

*Ts* =
*π*/(5*ωmax*) ≅
0.6/*ωmax* 或
0.1/*fmax*，

这里，*ωmax* 是 **Frequencies** 参数中的最高频率，单位为 rad/s；*fmax* 是最高频率，单位为 Hz。采样时间必须足够小，以便估计所需的最快频率，但也不能小到引入不必要的计算负担。

如果将采样时间设置为 –1，则软件在编译时根据模块外部的源确定采样时间。将采样时间设置为 –1 会禁用模块内部用于确保您的估计频率低于奈奎斯特频率的检查。

#### 提示

如果您希望在应用程序中以不同的采样时间运行部署的模块，请将此参数设置为 –1，并将该模块放入 Triggered Subsystem 中。然后，以所需的采样时间触发该子系统。如果您不打算在部署后更改采样时间，请指定固定且有限的采样时间。

### **Data Type** — 浮点精度 `double` (默认) | `single`

根据仿真环境或硬件要求指定浮点精度。

### **Excitation signal source** — 激励信号源 **Block parameters** (默认) | **External ports**

指定是通过模块参数还是通过外部端口提供实验扰动信号的频率和幅值。

- **Block parameters** — 选择此项以启用 **Frequencies** 和 **Amplitudes** 参数。
- **External ports** — 选择此项以启用 **w** 和 **amp** 输入端口。如果您希望在部署后更改扰动信号的频率和幅值，请使用此选项。

### **Frequencies** — 用于估计的频率 [0.5 1 2] (默认) | 向量

用于估计被控对象频率响应的频率。模块会在这些频率中的每一个频率处注入扰动。您可以估计的最高频率受奈奎斯特频率 *π*/*Ts* rad/s 限制，其中 *Ts* 是您为 **Sample time (Ts)** 参数设置的值。

对于 PRBS 信号，频率范围会影响实验长度。最低频率值确定能够覆盖指定频率的最小信号阶数。降低最低频率范围会增加所需的最小信号阶数，因此会增加实验长度。但是，由于 PRBS 输入信号的宽带特性，增加更多频率点不会增加实验长度。

#### 提示

此参数不可调。要在部署后提供频率，请将 **Excitation Signal Source** 设置为 **External ports**，并使用 **w** 输入端口。

#### 依赖关系

要启用此参数，请将 **Excitation Signal Source** 设置为 **Block parameters**。

### **Amplitudes** — 注入扰动的幅值 1 (默认) | 标量 | 向量

指定注入被控对象的扰动信号的幅值。要对所有频率使用相同的幅值，请指定一个标量值。如果您知道响应在要估计的频率范围内变化显著，则可以使用向量为每个频率指定不同的幅值。例如，可以在已知谐振频率附近使用较小的值，而在滚降频率以上使用较大的值。该向量必须与您为 **Frequencies** 提供的向量长度相同。

幅值必须：

- 足够大，使扰动能够克服被控对象执行器中的任何死区，并生成高于噪声水平的响应
- 足够小，使被控对象在标称工作点附近的近似线性区域内运行，并避免使被控对象输入或输出饱和

#### 提示

此参数不可调。要在部署后提供幅值，请将 **Excitation Signal Source** 设置为 **External ports**，并使用 **amp** 输入端口。

#### 依赖关系

要启用此参数，请将 **Excitation Signal Source** 设置为 **Block parameters**。

### **Number of frequencies** — 外部提供的频率数量 3 (默认) | 正整数

当您通过外部端口 **w** 提供实验频率时，请使用此参数指定频率数量（即 **w** 处向量信号的长度）。

#### 依赖关系

要启用此参数，请将 **Excitation Signal Source** 设置为 **External ports**。

### **Number of periods** — PRBS 信号中的周期数 1 (默认) | 正整数

PRBS 信号中的周期数，指定为正整数。

根据指定的频率和采样时间，模块在模块对话框的 **信号长度** 部分显示此参数的建议值。

### **Signal order** — PRBS 信号阶数 12 (默认) | 正整数 ≤ 24

信号阶数，指定为正整数。PRBS 信号的最大长度为 2*n*–1，其中 *n* 是信号阶数。要获得准确的频率响应估计，PRBS 的长度必须足够大。

对于给定的采样时间，要获得更高的频率分辨率，请指定更大的信号阶数。请指定小于或等于 24 的值，以防止实验运行时间过长。

根据指定的频率和采样时间，模块在模块对话框的 **信号长度** 部分显示此参数的建议值。

### **Use Auto-Generated Value** — 自动设置 PRBS 信号参数 `off` (默认) | `on`

模块根据指定的频率和采样时间计算 **Number of periods** 和 **Signal order** 参数的建议值。启用此选项可对一个或两个 PRBS 信号参数使用自动生成的值。当您运行多个频率范围或采样时间变化的实验时，这非常有用。

## 所属库

Simulink Control Design / Signal Generation

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

生成用于被控对象频率响应估计的 PRBS 输入信号

使用此模块生成 PRBS 输入扰动信号。与使用 sinestream 输入信号相比，PRBS 信号可减少总估计时间，同时产生可比的估计结果。为了更快地进行配置，此模块允许您基于指定的频率使用关键参数的自动生成值。PRBS 信号可用于估计通信和电力电子应用的频率响应。有关详细信息，请参阅 PRBS Input Signals。

当您在桌面仿真中或通过代码生成在硬件上生成扰动信号以注入被控对象模型时，此模块会很有帮助。然后，您可以收集被控对象对扰动信号的响应数据，并执行自定义处理以辨识被控对象特性。
