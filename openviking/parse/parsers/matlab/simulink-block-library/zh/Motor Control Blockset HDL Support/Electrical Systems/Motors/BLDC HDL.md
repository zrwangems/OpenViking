---
type: simulink-block
title: 'BLDC HDL'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Electrical Systems / Motors'
documentation_page: 'bldchdl'
documentation_source_path: '../mcb/ref/bldchdl.html'
language: zh-CN
chinese_source: worker-translation
---

# BLDC HDL

## 端口

### 输入

### **Config** — 模块配置信号向量

BLDC HDL 模块的配置信号，包含模块配置参数。有关组成参数的详细信息，请参阅 BLDC Configuration 模块中的 **Config** 输出端口描述。

**数据类型：** `single`

### **PhaseVolt** — 定子端电压 `1`×`3` 数组

定子端电压 *Va*、*Vb* 和 *Vc*，单位为 V。

**数据类型：** `single`

### **LdTrq/Spd** — 电机负载转矩或电机轴转速 标量

根据多路复用 **Config** 输入中 **Port Configuration** 参数定义的工作模式，该端口支持以下输入之一：

- *Tm* — 电机轴上的负载转矩，单位为 N·m。
- *ωm* — 电机的角速度，单位为 rad/s。

**数据类型：** `single`

### **Reset** — 复位总线信号 标量

模块用于复位内部积分器的总线信号。

**数据类型：** `Boolean`
### 输出

### **Info** — 总线信号 总线

该总线信号包含以下模块计算结果。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `IaStator` | | | 定子 A 相电流 | *ia* | A |
| `IbStator` | | | 定子 B 相电流 | *ib* | A |
| `IcStator` | | | 定子 C 相电流 | *ic* | A |
| `IdSync` | | | *d'* 轴电流 | *id'* | A |
| `IqSync` | | | *q'* 轴电流 | *iq'* | A |
| `VdSync` | | | *d'* 轴电压 | *vd'* | V |
| `VqSync` | | | *q'* 轴电压 | *vq'* | V |
| `MtrSpd` | | | 电机的机械角速度 | *ωm* | rad/s |
| `MtrPos` | | | 电机机械角位置 | *θm* | rad |
| `MtrTrq` | | | 电磁转矩 | *Te* | N·m |
| `MtrHall` | | | 霍尔传感器输出 | - | - |
| `BackEMF` | | | 电机中产生的反电动势 | *Ea*、*Eb*、*Ec* | V/m/s |

### **PhaseCurr** — a、b、c 相电流 1×3 数组

a、b、c 相的相电流 *ia*、*ib* 和 *ic*，单位为 A。

### **Torque** — 电机转矩 `标量`

电机转矩 *Tmtr*，单位为 N·m。

### **Speed** — 电机转速 `标量`

电机的角速度 *ωmtr*，单位为 rad/s。

### **MtrElecAngle** — 电机电角度 标量

电机的电位置 *θe*，单位为 rad。

**数据类型：** `single`

## 参数

### **Sample time (s)** — 模块采样时间 `1e-6`（默认）| 标量

模块连续执行实例之间的固定时间间隔（以秒为单位）。

## 所属库

Motor Control Blockset HDL Support / Electrical Systems / Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
|  |  |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2023b 中引入**

## 描述

具有梯形磁通分布的三相无刷直流电机

BLDC 模块实现了一个三相无刷直流（BLDC）电机，其反电动势为梯形波，在 120 电角度位置范围内保持恒定。该模块使用三相输入电压来调节各相电流，从而控制电机转矩或转速。

### 电机结构

该图展示了一个单极对电机。

由永磁体产生的转子磁场随电机角度产生梯形磁通变化率。

对于轴约定，当电机角度 *θr* 为零时，相 *a* 与 *d* 轴对齐。

### 三相正弦模型电气系统

该模块不使用标准 *dq* 参考坐标系，而是使用 *d’q’* 参考坐标系，其由以下变换方程定义。

vd'=23((va−Ria−Ea)cosθe+(vb−Rib−Eb)cos(θe−2π3)+(vc−Ric−Ec)cos(θe+2π3))

vq'=−2π3((va−Ria−Ea)sinθe+(vb−Rib−Eb)sin(θe−2π3)+(vc−Ric−Ec)sin(θe+2π3))

Ea=Pωm∂ψa∂θeEb=Pωm∂ψb∂θeEc=Pωm∂ψc∂θe

ia=id'cosθe−iq'sinθeib=id'cos(θe−2π3)−iq'sin(θe−2π3)ic=id'cos(θe+2π3)−iq'sin(θe+2π3)

该模块实现了以 BLDC 电机 *dq* 和 *d’q’* 参考坐标系表示的这些方程。电机参考坐标系中的所有量均相对于定子 A 相。

ωe=Pωmddtid'=1Ldvd'+LqLdPωmiq'

ddtiq'=1Lqvq'−LdLqPωmid'

Te=1.5P((Ld−Lq)id'iq')+P(∂ψa∂θeia+∂ψb∂θeib+∂ψc∂θeic)

该表描述了这些方程中使用的变量。

|  |  |
| --- | --- |
| *Lq*，*Ld* | q 轴和 d 轴电感（H） |
| *R* | 定子绕组电阻（ohm） |
| *iq'*，*id'* | *q'* 轴和 *d'* 轴电流（A） |
| *vq'*，*vd'* | *q'* 轴和 *d'* 轴电压（V） |
| *ωm* | 电机机械角速度（rad/s） |
| *ωe* | 电机电角速度（rad/s） |
| *P* | 极对数 |
| *Te* | 电磁转矩（Nm） |
| *θe* | 电角度（rad） |
| *va*，*vb*，*vc* | 定子 A、B、C 相电压（V） |
| *ia*，*ib*，*ic* | 定子 A、B、C 相电流（A） |
| *Ea*，*Eb*，*Ec* | 定子 A、B、C 相反电动势（V/m/s） |
| *ψa*，*ψb*，*ψc* | 链接每个定子绕组的总磁通（Wb） |

### 机械系统

电机角速度由下式给出：

ddtωm=1J(Te−Tf−Fωm−Tm)dθmdt=ωm

这些方程使用以下变量。

|  |  |
| --- | --- |
| *J* | 电机和负载的组合惯量（kgm^2） |
| *F* | 电机和负载的组合粘性摩擦（N·m/(rad/s)） |
| *θm* | 电机机械角位置（rad） |
| *Tm* | 电机轴转矩（Nm） |
| *Te* | 电磁转矩（Nm） |
| *Tf* | 电机轴静摩擦转矩（Nm） |
| *ωm* | 电机机械角速度（rad/s） |

### 幅值不变 *dq* 变换

该模块使用这些方程来实现幅值不变 *dq* 变换，以确保 *dq* 幅值与三相幅值相等。

[vsdvsq]= 23 [cos(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda)−sin(Θda−2π3)−sin(Θda+2π3)][vavbvc]

[iaibic]=   [cos(Θda)−sin(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda−2π3)−sin(Θda+2π3)][isdisq]

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Θda* | 相对于转子 *a* 轴的 *dq* 定子电角度（rad） |
| *vsq*，*vsd* | 定子 *q* 轴和 *d* 轴电压（V） |
| *isq*，*isd* | 定子 *q* 轴和 *d* 轴电流（A） |
| *va*，*vb*，*vc* | 定子 *a*、*b*、*c* 相电压（V） |
| *ia*，*ib*，*ic* | 定子 *a*、*b*、*c* 相电流（A） |

### 梯形磁通变化率

由永磁体产生的转子磁场随转子角度产生梯形磁通变化率。该图展示了三相 BLDC 电机三相的磁通变化率。
