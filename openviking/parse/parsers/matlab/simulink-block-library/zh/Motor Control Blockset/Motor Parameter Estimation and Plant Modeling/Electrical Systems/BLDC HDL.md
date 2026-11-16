---
type: simulink-block
title: 'BLDC HDL'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Electrical Systems'
documentation_page: 'bldchdl'
documentation_source_path: 'ref/bldchdl.html'
language: zh-CN
chinese_source: official
---

# BLDC HDL

## 端口

### 输入

### **Config** — 模块配置信号 矢量

包含模块配置参数的 BLDC HDL 模块的配置信号。有关组成参数的详细信息，请参阅 BLDC Configuration 模块中的**配置**输出端口描述。

**数据类型:** `single`

### **PhaseVolt** — 定子端电压 `1`×`3` 数组

定子端电压 *Va*、*Vb* 和 *Vc*，以 V 为单位。

**数据类型:** `single`

### **LdTrq/Spd** — 电机上的负载转矩或电机轴的转速 标量

根据多路复用**配置**输入中可用的**端口配置**参数定义的工作模式，该端口支持以下输入之一：

- *Tm* - 电机轴上的负载转矩，以 N·m 为单位。
- *ωm* - 电机的角速度，以弧度/秒为单位。

**数据类型:** `single`

### **Reset** — 重置总线信号 标量

总线信号，模块用它来重置内部积分器。

**数据类型:** `Boolean`
### 输出

### **Info** — 总线信号 总线

总线信号包含以下模块计算。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `IaStator` | | | 定子相电流 A | *ia* | A |
| `IbStator` | | | 定子相电流 B | *ib* | A |
| `IcStator` | | | 定子相电流 C | *ic* | A |
| `IdSync` | | | *d'* 轴电流 | *id'* | A |
| `IqSync` | | | *q'* 轴电流 | *iq'* | A |
| `VdSync` | | | *d'* 轴电压 | *vd'* | V |
| `VqSync` | | | *q'* 轴电压 | *vq'* | V |
| `MtrSpd` | | | 电机的机械角速度 | *ωm* | 弧度/秒 |
| `MtrPos` | | | 电机的机械角位置 | *θm* | 弧度 |
| `MtrTrq` | | | 电磁转矩 | *Te* | N·m |
| `MtrHall` | | | 霍尔传感器输出 | - | - |
| `BackEMF` | | | 电机中生成的反电动势 | *Ea* , *Eb* , *Ec* | V/m/s |

### **PhaseCurr** — a、b、c 相电流 1×3 数组

a、b、c 相电流分别为 *ia* 、*ib*  和 *ic* ，以 A 为单位。

### **Torque** — 电机转矩 `scalar`

电机转矩 *Tmtr*，以 N·m 为单位。

### **Speed** — 电机转速 `scalar`

电机的角速度 *ωmtr*，以弧度/秒为单位。

### **MtrElecAngle** — 电机电角 标量

电机的电气位置 *θe*，以弧度为单位。

**数据类型:** `single`

## 参数

### **采样时间(秒)** — 模块的采样时间 `1e-6` (默认) | 标量

连续的模块执行实例之间的固定时间间隔（以秒为单位）。

## 所属库

Motor Control Blockset HDL Support / Electrical Systems / Motors

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 要通过移动设计中的现有延迟来放置在输出端的寄存器的数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2023b 中推出**

## 描述

具有梯形磁通分布的三相无刷 DC 电机

BLDC 模块实现三相无刷 DC (BLDC) 电机，其梯形反电动势在电相位差为 120 度的位置范围内保持恒定。该模块使用三相输入电压来调节各相电流，从而控制电机转矩或转速。

### 电机构造

此图显示具有单个极对的电机。

永磁体产生的转子磁场会随着电机角度的变化而产生梯形磁通变化率。

对于轴约定，当电机角度 *θr*  为零时，相位 *a* 与 *d* 轴对齐。

### 三相正弦模型电气系统

该模块使用由以下变换方程定义的 *d’q’* 参考系，而不是标准的 *dq* 参考系。

vd'=23((va−Ria−Ea)cosθe+(vb−Rib−Eb)cos(θe−2π3)+(vc−Ric−Ec)cos(θe+2π3))

vq'=−2π3((va−Ria−Ea)sinθe+(vb−Rib−Eb)sin(θe−2π3)+(vc−Ric−Ec)sin(θe+2π3))

Ea=Pωm∂ψa∂θeEb=Pωm∂ψb∂θeEc=Pωm∂ψc∂θe

ia=id'cosθe−iq'sinθeib=id'cos(θe−2π3)−iq'sin(θe−2π3)ic=id'cos(θe+2π3)−iq'sin(θe+2π3)

该模块实现以下在 BLDC 电机的 *dq* 和 *d’q’* 参考系中表示的方程。电机参考系中的所有量都与定子相 A 相关。

ωe=Pωmddtid'=1Ldvd'+LqLdPωmiq'

ddtiq'=1Lqvq'−LdLqPωmid'

Te=1.5P((Ld−Lq)id'iq')+P(∂ψa∂θeia+∂ψb∂θeib+∂ψc∂θeic)

下表描述了在这些方程中使用的变量。

|  |  |
| --- | --- |
| *Lq* , *Ld* | q 轴和 d 轴电感 (H) |
| *R* | 定子绕组的电阻 (ohm) |
| *iq'* , *id'* | *q'* 轴和 *d'* 轴电流 (A) |
| *vq'* , *vd'* | *q'* 轴和 *d'* 轴电压 (V) |
| *ωm* | 电机的机械角速度（弧度/秒） |
| *ωe* | 电机的电气角速度（弧度/秒） |
| *P* | 极对数 |
| *Te* | 电磁转矩 (Nm) |
| *θe* | 电气角（弧度） |
| *va* , *vb* , *vc* | 定子 A、B 和 C 相电压 (V) |
| *ia* , *ib* , *ic* | 定子 A、B 和 C 相电流 (A) |
| *Ea* , *Eb* , *Ec* | 定子相 A、B 和 C 的反电动势 (V/m/s) |
| *ψa* , *ψb* , *ψc* | 链接每个定子绕组的总磁通 (Wb) |

### 机械系统

电机角速度由下式给出：

ddtωm=1J(Te−Tf−Fωm−Tm)dθmdt=ωm

上述方程用到了以下变量。

|  |  |
| --- | --- |
| *J* | 电机和负载的组合惯量 (kgm^2) |
| *F* | 电机和负载的组合粘性摩擦（N·m/（弧度/秒）） |
| *θm* | 电机机械角位置（弧度） |
| *Tm* | 电机轴转矩 (Nm) |
| *Te* | 电磁转矩 (Nm) |
| *Tf* | 电机轴静态摩擦转矩 (Nm) |
| *ωm* | 电机的机械角速度（弧度/秒） |

### 振幅不变的 *dq* 变换

该模块使用下列方程来实现幅值不变的 *dq* 变换，以确保 *dq* 和三相振幅相等。

[vsdvsq]= 23 [cos(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda)−sin(Θda−2π3)−sin(Θda+2π3)][vavbvc]

[iaibic]=   [cos(Θda)−sin(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda−2π3)−sin(Θda+2π3)][isdisq]

上述方程用到了以下变量。

|  |  |
| --- | --- |
| *Θda* | *dq* 定子相对于转子 *a* 轴的电角（弧度） |
| *vsq*, *vsd* | 定子 *q* 轴和 *d* 轴电压 (V) |
| *isq*, *isd* | 定子 *q* 轴和 *d* 轴电流 (A) |
| *va*, *vb*, *vc* | 定子电压相位 *a*、*b*、*c* (V) |
| *ia*, *ib*, *ic* | 定子电流相 *a*、*b*、*c* (A) |

### 梯形磁通变化率

永磁体产生的转子磁场会随着转子角度的变化而产生梯形磁通变化率。此图显示三相 BLDC 电机三个相位的磁通变化率。
