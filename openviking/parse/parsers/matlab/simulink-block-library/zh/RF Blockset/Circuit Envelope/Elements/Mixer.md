---
type: simulink-block
title: 'Mixer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'mixer'
documentation_source_path: 'ref/mixer.html'
language: zh-CN
chinese_source: worker-translation
---

# Mixer

## 端口

R2025b 中未记录。

## 参数

#### 主

### **Source of conversion gain** — 转换增益的来源参数 `Available power gain`（默认）| `Open circuit voltage gain` | `Polynomial coefficients`

转换增益的来源参数，指定为以下之一：

- `Available power gain` —
  该模块使用 Available power gain 参数的值来计算多项式 VCVS 的线性电压增益项 a1。
  此计算假设混频器为匹配负载端接。
- `Open circuit voltage gain` —
  该模块使用 Open circuit voltage gain 参数的值作为多项式 VCVS 的线性电压增益项 a1。
- `Polynomial coefficients` —
  该模块根据您指定的多项式实现非线性电压增益。多项式的阶数必须小于或等于 9，系数按升幂排列。如果向量 a 有 10 个系数，[*a*0,
   *a*1,
  *a*2, …,
  *a*9]，则其表示的多项式为 *V*out =
  *a*0 +
   *a*1
   *V*in +
  *a*2
  *V*in2+
  ⋯ +  *a*9
  *V*in9。在这种情况下，
  *a*1 表示线性增益项。

  例如，向量
  [*a*0,
  *a*1,
  *a*2,
  *a*3] 指定关系 *V*out =
  *a*0 +
  *a*1
  *V*in +
  *a*2
  *V*in2
  + ⋯ + *a*3
  *V*in3。

  末尾零被省略：如果
  *a*3 = 0，
  [*a*0,
  *a*1,
  *a*2] 定义的多项式与
  [*a*0,
  *a*1,
  *a*2, 0] 相同。此参数的默认值为 [0 1]，对应于线性关系 *V*o =
  *V*i。

### **Available power gain** — 混频器的线性增益 0 `dB`（默认）| 标量

混频器的线性增益，指定为以 dB 为单位的标量。从相应的下拉列表指定单位。

#### 依赖关系

要启用此参数，请在 **Source of conversion gain** 选项卡中选择 `Available power
gain`。

### **Open circuit voltage gain** — 开路电压增益 0 `dB`（默认）| 标量

混频器的开路电压，指定为以 dB 为单位的标量。从相应的下拉列表指定单位。

#### 依赖关系

要启用此参数，请在 **Source of conversion gain** 选项卡中选择 `Open circuit voltage
gain`。

### **Polynomial coefficients** — 多项式阶数 `[0 1]`（默认）| 向量

多项式阶数，指定为向量。

多项式的阶数必须小于或等于 9。系数按升幂排列。如果向量有 10 个系数，
`[a0,a1,a2,
... a9]`，则其表示的多项式为：

*Vout* = *a*0 + *a*1*Vin* + *a*2*Vin*2 + ...
 + *a*9*Vin*9

其中
*a*1 表示线性增益项。

例如，向量
`[a0,a1,a2,a32]`
指定关系 *Vo* = *a*0 + *a*1*V1* + *a*2*V1*2 + *a*3*V1*3。末尾零被省略。如果
*a*3 = 0，则
`[a0,a1,a2]`
定义的多项式与
[*a*0,*a*1,*a*2,0] 相同。
此参数的默认值为 [0,1]，对应于线性关系 *Vo* =
*Vi*。

#### 依赖关系

要启用此参数，请在 **Source of conversion gain** 选项卡中选择 `Polynomial coefficients`。

### **Input impedance (Ohm)** — 混频器的输入阻抗 `50`（默认）| 标量

混频器的输入阻抗，指定为标量。

### **Output impedance (Ohm)** — 混频器的输出阻抗 `50`（默认）| 标量

混频器的输出阻抗，指定为标量。

### **LO impedance (Ohm)** — 混频器 LO 端口的阻抗 `inf`（默认）| 标量

混频器的输出阻抗，指定为标量。

### **Noise figure (dB)** — 混频器的单边带 IEEE 噪声系数 `dB`（默认）| 标量

混频器的单边带噪声系数，根据 IEEE® 定义指定为标量。

要在电路包络模型中使用 Noise、Amplifier 或 Mixer 模块对噪声进行建模，必须在 Configuration 模块对话框中选中 **Simulate noise** 复选框。

IEEE SSB 定义假设混频器输入端的镜像带宽噪声被完全抑制，而混频器内部在镜像带宽和信号带宽中都会产生噪声。因此，混频器输出端的噪声是两个贡献之和：

Nout=NinGmix+2NmixerGmix，

其中：

- *N*out 是混频器输出端的噪声。
- *N*in 是混频器输入端的噪声（假设镜像带宽中的噪声被完全抑制）。
- *N*mixer 是混频器在信号带宽和镜像带宽中内部产生的噪声。
- *G*mix 是混频器增益。

因此，根据 IEEE SSB 定义的噪声因子可以表示为

FSSB-IEEE=1+2Nmixer/Nin，

它通过以下关系与其他常用定义相关联

FSSB=2+2Nmixer/Nin=1+FSSB-IEEE,FDSB=1+Nmixer/Nin=12(1+FSSB-IEEE)。

在使用 Friis 公式进行链路预算分析时，可以直接应用 IEEE SSB 定义来描述混频器级。使用其他定义则需要修改 Friis 公式。RF Blockset™ 中的 Mixer 模块和 RF Toolbox™ 中的 RF Budget Analyzer 应用都使用 IEEE 定义。

这三种定义之间的解析关系允许您仿真混频器输出端的噪声水平。例如，

FSSB=4 dB⇒FSSB-IEEE=10log10(10FSSB/10−1)=1.79 dB,FDSB=4 dB⇒FSSB-IEEE=10log10(2×10FDSB/10−1)=6.04 dB。

如果您仿真 RF Blockset 混频器时未包含理想镜像抑制滤波器，则混频器输出端的噪声会大于噪声系数所预测的值，因为镜像带宽中的噪声实际上被折叠到了输出信号上。

因此，在生成模型时，Modulator 和 Demodulator 模块都会自动插入理想镜像抑制滤波器。（您可以在模块掩膜中移除该滤波。）

Noise Figure Testbench 模块测量 SSB 噪声系数，使您能够验证仿真噪声系数是否具有预期值。

- 如果您向模型添加理想镜像抑制滤波器，则有效噪声系数与解析值一致。
- 如果您移除镜像抑制滤波器，或者使用具有部分抑制的滤波器，则测得的噪声系数会大于解析值。

### **Ground and hide negative terminals** — 接地并隐藏 RF 电路端子 `on`（默认）| `off`

选择此参数可在内部接地并隐藏负端子。要暴露负端子，请清除此参数。通过暴露这些端子，您可以将它们连接到模型的其他部分。

默认情况下，此选项处于选中状态。

#### Nonlinearity

### **Nonlinear polynomial type** — 多项式非线性 `Even and odd order`（默认）| `Odd order`

多项式非线性，指定为以下选项之一：

- `Even and odd order`：当您选择 `Even and odd order` 时，放大器除产生线性项外，还可产生二阶和三阶互调频率。
- `Odd order`：当您选择 `Odd order` 时，放大器仅产生奇数阶互调频率。

  线性增益决定线性 *a*1 项。该模块根据指定的参数计算其余项。这些参数为 **IP3**、**1-dB gain compression power**、**Output saturation power** 和 **Gain compression at saturation**。您指定的约束数量决定了模型的阶数。下图展示了非线性混频器参数的图形化定义。

  输出功率与输入功率关系图展示了非线性混频器参数。

### **Intercept points convention** — 截点约定 `Output`（默认）| `Input`

截点约定，指定为 `Input` 参考或 `Output` 参考。将此规范用于截点、1-dB 增益压缩功率和饱和功率。

### **IP2** — 二阶截点 `inf``dBm`（默认）| 标量

二阶截点，指定为标量。默认值 `inf` `dBm` 对应于未指定的点。

#### 依赖关系

要启用此参数，请在 **Nonlinear polynomial type** 选项卡中选择 `Even and odd order`。

### **IP3** — 三阶截点 `inf` `dBm`（默认）| 标量

三阶截点，指定为标量。默认值 `inf` `dBm` 对应于未指定的点。

### **1-dB gain compression power** — 1-dB 增益压缩功率 `inf``dBm`（默认）| 标量

1-dB 增益压缩功率，指定为标量。1-dB 增益压缩点必须小于输出饱和功率。

#### 依赖关系

要启用此参数，请在 **Nonlinear polynomial type** 选项卡中选择 `Odd order`。

### **Output saturation power** — 输出饱和功率 `inf``dBm`（默认）| 标量

输出饱和功率，指定为标量。该模块使用此值计算非线性模型中使用的电压饱和点。在这种情况下，多项式的一阶导数为零，二阶导数为负。

#### 依赖关系

要启用此参数，请在 **Nonlinear polynomial type** 选项卡中选择 `Odd order` 并设置 **Output saturation power**。

### **Gain compression at saturation** — 饱和时的增益压缩 `inf``dBm`（默认）| 标量

饱和时的增益压缩，指定为标量。

#### 依赖关系

要启用此参数，请在 **Nonlinear polynomial type** 选项卡中选择 `Odd order` 并设置 **Output saturation power**。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

### R2025a：改进的多项式模型以计算非线性

Mixer 模块现在支持改进的多项式模型来计算非线性，该模型更好地遵循用户规范。

当您打开在 R2025a 之前创建的包含 Mixer 模块的模型时，软件使用改进的多项式模型来计算非线性，数值结果可能会有所不同。

### R2021b：Mixer 模块图标已更新

从 R2021b 开始，Mixer 模块图标已更新。模块图标现在是动态的，并显示噪声参数的当前状态。

当您打开在 R2021b 之前创建的包含 Mixer 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

对射频系统中的混频器进行建模

混频器模块执行信号频率变换和非线性放大。

对于给定的射频输入信号 *V*RF = *A*RFcos(*ω*RFt) 和本振输入信号 *V*LO = *A*cLOcos(*ω*LOt)，混频器将输入端口处的信号相乘：

VinVLO=Aincos(ωint)ALOcos(ωLOt)=AinALO2cos[(ωin+ωLO)t]+AinALO2cos[(ωin−ωLO)t]

该混频将射频信号的频率转换为 *ωRF* + *ωLO* 和 *ωRF* – *ωLO*。为使混频器正确执行此操作，您必须在 Configuration 模块计算的仿真频率中包含频率 *ωRF* + *ωLO* 或 *ωRF* – *ωLO*。

该模块的功率增益规格将单边带（SSB）的功率与输入相关联。

在混合射频和本振信号之后，混频器模块执行放大。为对线性放大进行建模，混频器按系数 a1 对信号进行缩放。用多项式指定的压控电压源（VCVS）实现非线性放大。该多项式自动包含饱和效应，并产生额外的互调频率。

混频器模块掩码图标是动态的，指示所应用噪声参数的当前状态。下表显示了该模块上的图标如何根据模块上 **Noise figure (dB)** 参数的状态而变化。

| Noise figure (dB)：`10` | Noise figure (dB)：`0` |
| --- | --- |
| 电阻模块图标，Simulate noise 设置为 on。 | 电阻模块图标，Simulate noise 设置为 off。 |
