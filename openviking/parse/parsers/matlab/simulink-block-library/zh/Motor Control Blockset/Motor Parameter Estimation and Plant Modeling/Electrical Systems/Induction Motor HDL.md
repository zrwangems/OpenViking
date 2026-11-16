---
type: simulink-block
title: 'Induction Motor HDL'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Electrical Systems'
documentation_page: 'inductionmotorhdl'
documentation_source_path: 'ref/inductionmotorhdl.html'
language: zh-CN
chinese_source: official
---

# Induction Motor HDL

## 端口

### 输入

### **Config** — 模块配置信号 矢量

包含模块配置参数的感应电机 HDL 模块的配置信号。

**数据类型:** `single`

### **PhaseVolt** — 定子端电压 `1`×`3` 数组

定子端电压 *Va*、*Vb* 和 *Vc*，以 V 为单位。

**数据类型:** `single`

### **LdTrq/Spd** — 电机上的负载转矩或电机轴的转速 标量

该端口支持以下输入之一：

- *Tm* - 电机轴上的负载转矩，以 N·m 为单位。
- *ωm* - 电机的角速度，以弧度/秒为单位。

**数据类型:** `single`

### **Reset** — 重置总线信号 标量

重置总线信号，模块用它来重置内部积分器。

**数据类型:** `Boolean`
### 输出

### **Info** — 总线信号 总线

总线信号包含以下模块计算。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `IaStator` | | | 定子相电流 A | *ia* | A |
| `IbStator` | | | 定子相电流 B | *ib* | A |
| `IcStator` | | | 定子相电流 C | *ic* | A |
| `IdSync` | | | 直轴电流 | *id* | A |
| `IqSync` | | | 交轴电流 | *iq* | A |
| `VdSync` | | | 直轴电压 | *vd* | V |
| `VqSync` | | | 交轴电压 | *vq* | V |
| `MtrSpd` | | | 转子的机械角速度 | *ωm* | 弧度/秒 |
| `MtrMechPos` | | | 转子机械角位置 | *θm* | 弧度 |
| `MtrPos` | | | 转子电角位置 | *θe* | 弧度 |
| `MtrTrq` | | | 电磁转矩 | *Te* | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | 机械功率 | *Pmot* | W |
| `PwrBus` | 电功率 | *Pbus* | W |
| `PwrNotTrnsfrd` | `PwrElecLoss` | 电阻功率损失 | *Pelec* | W |
| `PwrMechLoss` | 机械功率损失 | *Pmech* | W |
| `PwrStored` | `PwrMtrStored` | 储存的电机功率 | *Pstr* | W |

### **PhaseCurr** — 相位 *a*、*b* 和 *c* 的电流 `1`×`3` 数组

相位 *a*、*b* 和 *c* 各自的电流 *ia*、*ib* 和 *ic*，以 A 为单位。

### **Torque** — 电机转矩 `scalar`

电机转矩 *Tmtr*，以 N·m 为单位。

### **Speed** — 电机转速 `scalar`

电机的角速度 *ωmtr*，以弧度/秒为单位。

### **MtrElecAngle** — 电机电角 标量

电机的电气位置 *θdq*，以弧度为单位。

**数据类型:** `single`

## 参数

### **采样时间(秒)** — 采样时间，在此采样时间过后模块将再次执行 `1e-6` (默认) | 标量

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

**在 R2022b 中推出**

## 描述

三相感应电机

Induction Motor HDL 模块实现三相感应电机。该模块使用三相输入电压来调节各相电流，从而控制电机转矩或转速。

该模块使用**采样时间(秒)** 参数为定步长双精度和单精度目标生成代码。它支持 FPGA 部署的代码生成并能生成 HDL 兼容代码。

您可以使用**配置**输入端口指定感应电机参数和工作模式。您还可以使用 Induction Motor Configuration 模块生成所需的配置信号，以在**配置**输入端口指定该信号。

### 三相正弦模型电气系统

该模块可实现在静止转子参考 (*dq*) 系中表示的方程。*d* 轴与 *a* 轴对齐。转子参考系中的所有量都是相对于定子来描述的。

该模块使用以下方程来计算电角速度 (*ωem*) 和转差速度 (*ωslip*)。

ωem=Pωmωslip= ωsyn−ωem

为了计算相对于转子 *A* 轴 (*dA*) 的 *dq* 转子电角速度，该模块使用定子 *a* 轴 (*da*) 转速和转差速度之间的差值：

ωdA= ωda− ωem

为了简化磁通、电压和电流变换的方程，该模块使用转子 A 轴参考系：

ωda=ωemωdA=0

| 计算 | 方程 |
| --- | --- |
| 磁通 | ddt[λsdλsq]= [vsdvsq]− Rs[isdisq]− ωda[0−110][λsdλsq]ddt[λrdλrq]= [vrdvrq]− Rr[irdirq]− ωdA[0−110][λrdλrq]      [λsdλsqλrdλrq]= [Ls00LsLm00LmLm00LmLr00Lr][isdisqirdirq] |
| 电流 | [isdisqirdirq]= (1Lm2− LrLs)[−Lr00−LrLm00LmLm00Lm−Ls00−Ls][λsdλsqλrdλrq] |
| 电感 | Ls= Lls+LmLr= Llr+Lm |
| 电磁转矩 | Te=PLm(isqird− isdirq) |
| 功率不变的 *dq* 变换，以确保 *dq* 和三相功率相等 | [vsdvsq]= 23 [cos(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda)−sin(Θda−2π3)−sin(Θda+2π3)][vavbvc]      [iaibic]= 23  [cos(Θda)−sin(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda−2π3)−sin(Θda+2π3)][isdisq] |

上述方程用到了以下变量。

|  |  |
| --- | --- |
| *ωm* | 转子的角速度（弧度/秒） |
| *ωem* | 电气转子转速（弧度/秒） |
| *ωslip* | 电气转子转差速度（弧度/秒） |
| *ωsyn* | 同步转子转速（弧度/秒） |
| *ωda* | dq 定子相对于定子 a 轴的电角速度（弧度/秒） |
| *ωdA* | dq 定子相对于转子 A 轴的电角速度（弧度/秒） |
| *Θda* | dq 定子相对于定子 a 轴的电角（弧度） |
| *ΘdA* | dq 定子相对于转子 A 轴的电角（弧度） |
| *Lq*, *Ld* | q 轴和 d 轴电感 (H) |
| *Ls* | 定子电感(H) |
| *Lr* | 转子电感 (H) |
| *Lm* | 磁化电感(H) |
| *Lls* | 定子泄漏电感(H) |
| *Llr* | 转子泄漏电感(H) |
| *vsq*, *vsd* | 定子 q 轴和 d 轴电压 (V) |
| *isq*, *isd* | 定子 q 轴和 d 轴电流 (A) |
| *λsq*, *λsd* | 定子 q 轴和 d 轴磁通 (Wb) |
| *irq*, *ird* | 转子 q 轴和 d 轴电流 (A) |
| *λrq*, *λrd* | 转子 q 轴和 d 轴磁通 (Wb) |
| *va*, *vb*, *vc* | 定子电压 a、b、c 相 (V) |
| *ia*, *ib*, *ic* | 定子电流 a、b、c 相 (A) |
| *Rs* | 定子绕组的电阻 (ohm) |
| *Rr* | 转子绕组的电阻 (ohm) |
| *P* | 极对数 |
| *Te* | 电磁转矩 (Nm) |

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

### 功率计算

对于电机功率计算，该模块实现下列方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` |  | `PwrMtr` | 机械功率 | *Pmot* | Pmot= −ωmTe |
| `PwrBus` | 电功率 | *Pbus* | Pbus= vania+ vbnib+vcnic |
|  | `PwrElecLoss` | 电阻功率损失 | *Pelec* | Pelec= −(Rsisd2+Rsisq2+−Rrird2+Rrirq2) |
| `PwrMechLoss` | 机械功率损失 | *Pmech* | 当**端口配置**设置为**转矩**时：  Pmech= −(ωm2F+ |ωm|Tf)  当**端口配置**设置为**转速**时：  Pmech= 0 |
|  | `PwrMtrStored` | 储存的电机功率 | *Pstr* | Pstr= Pbus+ Pmot+ Pelec + Pmech |

上述方程用到了以下变量。

|  |  |
| --- | --- |
| *Rs* | 定子电阻(欧姆) |
| *Rr* | 转子电阻(Ohm) |
| *ia*, *ib*, *ic* | 定子相 a、b 和 c 电流 (A) |
| *isq*, *isd* | 定子 q 轴和 d 轴电流 (A) |
| *van*, *vbn*, *vcn* | 定子相 a、b 和 c 电压 (V) |
| *ωm* | 转子的机械角速度（弧度/秒） |
| *F* | 电机和负载的组合粘性阻尼（N·m/（弧度/秒）） |
| *Te* | 电磁转矩 (Nm) |
| *Tf* | 电机和负载的组合摩擦转矩 (Nm) |
