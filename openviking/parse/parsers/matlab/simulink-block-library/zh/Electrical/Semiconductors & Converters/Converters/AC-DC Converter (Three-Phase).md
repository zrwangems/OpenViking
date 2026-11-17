---
type: simulink-block
title: 'AC-DC Converter (Three-Phase)'
family: 'semiconductors-converters'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'acdcconverterthreephase'
documentation_source_path: 'ref/acdcconverterthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# AC-DC Converter (Three-Phase)

## 端口

### 输入

### **Vref** — DC 电压参考（物理信号）

与 DC 电压参考的外部信号相关联的物理信号输入端口。

### 守恒

### **~** — 三相端口（电气）

可扩展三相端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a** — *a* 相（电气）

与 *a* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相（电气）

与 *b* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相（电气）

与 *c* 相相关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **+** — 正端子（电气）

与正端子相关联的电气守恒端口。

### **-** — 负端子（电气）

与负端子相关联的电气守恒端口。

## 参数

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

用于对复合或扩展三相端口建模的选项。

### **Output DC voltage droop with output current** — 1 A 时的电压跌落 `1``V/A`（默认）| nonnegative scalar

对于 1 A 的输出电流，输出 DC 电压从设定点跌落的电压量。

### **Voltage dynamics at DC side** — DC 侧动态模型 `No dynamics`（默认）| `Specify voltage regulation time constant`

用于包含电压调节动态的选项。如果将此参数设置为 `No dynamics`，则模块不考虑电压调节动态。如果将此参数设置为 `Specify voltage regulation time constant`，则模块会在定义 DC 电压源值的方程中添加一阶滞后。

### **Voltage regulation time constant at DC side** — DC 侧电压动态时间常数 `0.02` `s`（默认）| positive scalar

当 DC 侧的负载电流发生阶跃时，与 DC 侧电压瞬态相关联的时间常数。

#### 依赖项

要启用此参数，请将 **Voltage dynamics at DC side** 设置为 `Specify voltage regulation time constant`。

### **Initial output voltage at DC side** — 零时刻 DC 侧输出电压 `100` `V`（默认）| scalar

零时刻的 DC 侧输出电压。为了使模型在提供稳态负载电流时无瞬态地初始化，请使用此参数设置初始 DC 侧输出电压。

#### 依赖项

要启用此参数，请将 **Voltage dynamics at DC side** 设置为 `Specify voltage regulation time constant`。

### **Rated electrical frequency at AC side** — AC 侧额定电气频率 `60` `Hz`（默认）| positive scalar

AC 侧额定电气频率。

### **Minimum AC side voltage (phase-to-phase RMS)** — 最小 AC 侧电压 `80` `V`（默认）| positive scalar

转换器产生 DC 输出电压所需的最小相间 RMS AC 侧电压值。

### **Voltage time constant at AC side** — AC 侧电压时间常数 `0.01` `s`（默认）| positive scalar

与 AC 侧电压测量瞬态相关联的时间常数。

### **Initial voltage at AC side (phase-to-phase RMS)** — AC 侧初始电压 `100` `V`（默认）| positive scalar

零时刻 AC 侧的相间 RMS 电压。此参数的值必须大于 **Minimum AC side voltage (phase-to-phase RMS)** 参数的值。

### **Initial voltage angle at AC side** — AC 侧 *a* 相初始电压角 `0` `deg`（默认）| scalar

AC 侧 *a* 相在零时刻的初始电压角。

### **Power balance dynamics** — 包含功率平衡动态的选项 `Specify power time constant`（默认）| `No dynamics`

是否包含功率平衡动态。如果将此参数设置为 `No dynamics`，则模块不考虑功率平衡动态。如果将此参数设置为 `Specify power time constant`，则模块会在定义 AC 侧功率的方程中添加一阶滞后。当启用动态时，DC 侧输出功率变化会导致 AC 侧输入功率发生瞬态变化。

### **Power balance time constant** — 功率平衡动态的时间常数 `0.01` `s`（默认）| positive scalar

与 AC 侧和 DC 侧之间功率平衡瞬态相关联的时间常数。

#### 依赖项

要启用此参数，请将 **Power balance dynamics** 设置为 `Specify power time constant`。

### **Initial active power** — AC 侧初始有功功率 `1e3` `W`（默认）| scalar

零时刻 AC 侧的初始有功功率。

#### 依赖项

要启用此参数，请将 **Power balance dynamics** 设置为 `Specify power time constant`。

### **Parasitic conductance to electrical reference** — 到电气参考的寄生电导 `1e-6` `S`（默认）| nonnegative scalar

到电气参考的寄生电导。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

AC-DC converter 的行为模型

此模块表示 AC-DC converter 的行为模型。使用此模块可对 AC-DC converter 建模，而无需仿真各个开关事件。使用 DC 电压参考输入在 AC 侧和 DC 侧之间转换电能。

此模块与时间仿真模式和频率-时间仿真模式兼容。

### 方程

**DC 侧**

在 DC 侧，如果将 **Voltage dynamics at DC side** 参数设置为 `No dynamics`，则模块使用以下方程计算输出电压 *VDC*：

VDC=Vref−DIDC,

其中 *Vref* 是 **Vref** 端口处输入信号的值，D 是 **Output DC voltage droop with output current** 参数的值，*IDC* 是输出 DC 电流。

如果将 **Voltage dynamics at DC side** 参数设置为 `Specify voltage regulation time constant`，则模块使用以下方程计算输出电压 *VDC*：

τDCV˙DC+VDC=Vref−DIDC,

其中 *τDC* 是 **Voltage regulation time constant at DC side** 参数的值。

DC 侧功率为

PDC=VDCIDC.

**AC 侧**

如果将 **Power balance dynamics** 参数设置为 `No dynamics`，则 AC 侧的输入功率等于 DC 侧的输出功率。

PAC=PDC.

如果将 **Power balance dynamics** 参数设置为 `Specify power time constant`，则模块使用以下方程计算 AC 侧的输入功率：

τPP˙AC+PAC=PDC,

其中 *τP* 是 **Power balance time constant** 参数的值。

为了确定 AC 侧的三相输入电流，模块首先使用 Park 变换根据 *abc* 相电压 *va*、*vb* 和 *vc* 计算 *dq* 轴电压 *vd* 和 *vq*：

[vdvq]=23[sinθsin(θ−120°)sin(θ+120°)cosθcos(θ−120°)cos(θ+120°)][vavbvc]

其中 θ=2πFrated⋅t 是同步旋转参考系的角。

然后，模块使用这些功率方程计算三相 AC 电流 *ia*、*ib* 和 *ic*：

PAC=32(vdid+vqiq)QAC=0=32(vdid−vqiq).

根据这些方程，*dq* 轴电流 *id* 和 *iq* 为

id=23PACvdxvdx2+vqx2iq=23PACvqxvdx2+vqx2,

其中 *vdx* 和 *vqx* 由以下方程获得：

τACv˙dx+vdx=vdτACv˙qx+vqx=vq,

其中 *τAC* 是 **Voltage time constant at AC side** 参数的值。

最后，模块使用以下方程计算流入转换器的三相 AC 电流：

[iaibic]=[sinθcosθsin(θ−120°)cos(θ−120°)sin(θ+120°)cos(θ+120°)][idiq].
