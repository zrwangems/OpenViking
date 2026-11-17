---
type: simulink-block
title: 'Frequency-Dependent Overhead Line (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Lines'
documentation_page: 'frequencydependentoverheadlinethreephase'
documentation_source_path: 'ref/frequencydependentoverheadlinethreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Frequency-Dependent Overhead Line (Three-Phase)

## 端口

### 守恒端口

### **~1** — 三相交流电压 1 electrical

与交流电压 1 关联的可扩展电气守恒三相端口。

### **~2** — 三相交流电压 2 electrical

与交流电压 2 关联的可扩展电气守恒三相端口。

## 参数

### **Modeling option** — 是对复合三相端口还是扩展三相端口进行建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是对复合三相端口还是扩展三相端口进行建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口来构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口来表示三相系统的各个相。

### **X position of the line** — 线路水平位置 `[-6, 0, 6]` `m`（默认）| 三元素向量

线路在参考坐标系 *x* 轴上的位置。

### **Y position of the line** — 线路垂直位置 `[16, 26, 16]` `m`（默认）| 三个正元素向量

线路在参考坐标系 *y* 轴上的位置。向量的元素必须大于 `0`。

### **Resistivity of the conductor** — 导体电阻率 `2.7e-8` `m*Ohm`（默认）| 正标量

导体电阻率。该值必须大于 `0`。

### **Resistivity of the earth** — 大地回流电阻率 `100` `m*Ohm`（默认）| 正标量

大地回流电阻率。该值必须大于 `0`。

### **Radius of the conductor** — 导体半径 `0.017` `m`（默认）| 正标量

导体半径。该值必须大于 `0`。

### **Length of the line** — 线路长度 `150e3` `m`（默认）| 范围 [1, 300000] 内的标量

频率相关架空线路的长度。

### **Ground configuration** — 接地节点可访问性 `Internally grounded`（默认）| `Accessible ground nodes`

接地节点的配置。

## 所属库

Simscape / Electrical / Passive / Lines

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

包含随频率变化效应的三相架空线路

Frequency-Dependent Overhead Line (Three-Phase) 模块表示一条高保真频率相关架空线路，可在 0.01 Hz 至 100 kHz 范围内提供准确的瞬态响应仿真。

该模块计算频率相关阻抗矩阵和导纳矩阵。计算还取决于回流路径的损耗、电感和电容。

有关使用频率相关架空线路（三相）的更多信息，请参阅工程应用。

### 方程

**线路模型**

多导体传输线的电磁行为由电报方程描述。

−dVdx=ZI

−dIdx=YV

其中：

- *V* 是线路相电压向量。
- *I* 是相电流向量。
- *Z* 是单位长度的串联阻抗矩阵。
- *Y* 是单位长度的并联导纳矩阵。

这些是电流和电压向量的一般解。

|  |  |
| --- | --- |
| I(x)=e−ΨxC1+eΨxC2 | **(1)** |

|  |  |
| --- | --- |
| YcV(x)= e−ΨxC1−eΨxC2 | **(2)** |

其中 Ψ=YZ 是传播矩阵，Yc=(YZ)−1Y 是特征导纳。

现在考虑长度为 *x* = *l* 的传输线段。在其某一端的起点处，当 *x* = *0* 时，方程 1 和 2 的计算如下。

|  |  |
| --- | --- |
| I1=C1+C2 | **(3)** |

|  |  |
| --- | --- |
| YcV1= C1−C2 | **(4)** |

积分常数向量 *C1* 和 *C2* 可以用 *I0* 和 *V0* 表示。

|  |  |
| --- | --- |
| C1=(I1+YcV1)2 | **(5)** |

|  |  |
| --- | --- |
| C2=(I1−YcV1)2 | **(6)** |

类似地，在 *x* = *l* 处，方程 1 和 2 的计算如下。

|  |  |
| --- | --- |
| I2=e−ΨlC1+eΨlC2 | **(7)** |

|  |  |
| --- | --- |
| YcV2=e−ΨlC1−eΨlC2 | **(8)** |

为了获得传输线模型的两个基本方程，首先使用方程 7 和 8 执行此计算。

|  |  |
| --- | --- |
| I2−YcV2=−2e−ΨlC1 | **(9)** |

然后将方程 5 代入方程 9。

|  |  |
| --- | --- |
| I2−YcV2=−H(I1+YcV1) | **(10)** |

其中 H=e−Ψl 是传播因子矩阵。方程 10 建立了多导体线路段端子处电压与电流之间的关系。

您可以获得为 *x* = *0* 处端子 1 提供模型的伴随表达式。

|  |  |
| --- | --- |
| I1−YcV1=−H(I2+YcV2) | **(11)** |

定义：

- Ish,1=YcV1 — 由注入电压 *V1* 在端子 1 处产生的并联电流向量
- Ish,2=YcV2 — 由注入电压 *V2* 在端子 2 处产生的并联电流向量
- Irfl,1=12(I1+YcV1) — 端子 1 的反射电流
- Irfl,2=12(I2+YcV2) — 端子 2 的反射电流

最后将方程 10 和 11 重写如下：

I1=Ish,1−2HIrfl,2

I2=Ish,2−2HIrfl,1

这些方程构成了长度为 L 的线路段的行波线路模型。

特别是对于带大地回流的传输线，参数高度依赖于频率。模型求解随后直接在相域中进行。该模块会在整个频率范围内自动计算阻抗矩阵和特征导纳矩阵，并通过有理拟合执行近似。

该模型的有理拟合通过使用矢量拟合（VF）过程执行。有关相域线路模型和状态空间分析的更多信息，请参阅 *Wide-Band Line Model Implementation in Matlab for EMT Analysis* [1]。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同来源指定标称值，包括模块对话框或属性检查器中的 **Nominal Values** 部分。有关更多信息，请参阅 System Scaling by Nominal Values。
