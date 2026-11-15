---
type: simulink-block
title: 'PMSM HDL'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Electrical Systems'
documentation_page: 'pmsmhdl'
documentation_source_path: 'ref/pmsmhdl.html'
language: zh-CN
chinese_source: official
---

# PMSM HDL

## 端口

### 输入

### **Config** — 模块配置信号 矢量

包含模块配置参数的 PMSM HDL 模块的配置信号。有关组成参数的详细信息，请参阅 PMSM Configuration 模块的**配置**输出。

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
| `MtrSpd` | | | 电机的机械角速度 | *ωm* | 弧度/秒 |
| `MtrPos` | | | 电机的机械角位置 | *θm* | 弧度 |
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

电机的电气位置 *θe*，以弧度为单位。

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

具有正弦反电动势的三相永磁同步电机

PMSM HDL 模块实现具有正弦反电动势的三相永磁同步电机 (PMSM)。该模块使用三相输入电压来调节各相电流，从而控制电机转矩或转速。

该模块使用**采样时间(秒)** 参数为定步长双精度和单精度目标生成代码。它支持 FPGA 部署的代码生成并能生成 HDL 兼容代码。

您可以使用**配置**输入端口指定 PMSM 参数和工作模式。您还可以使用 PMSM Configuration 模块生成所需的配置信号，以在**配置**输入端口指定该信号。

### 电机构造

下列各图显示内置式和表贴式 PMSM 构造，且电机上有一个单极点对。

永磁体产生的电机磁场会随着电机角度的变化而产生正弦磁通变化率。

对于轴约定，当电机角度 *θr* 为零时，相位 *a* 与 *d* 轴对齐。

### 三相正弦模型电气系统

该模块实现在电机磁通参考系（*dq* 系）中表达的下列方程。电机参考系中的所有量都以定子为参考。

ωe=Pωmddtid=1Ldvd−RLdid+LqLdPωmiq

ddtiq=1Lqvq−RLqiq−LdLqPωmid−λpmPωmLq

Te=1.5P[λpmiq+(Ld−Lq)idiq]

由于电机电磁的凸极率，*Lq* 和 *Ld* 电感表示相电感和电机位置之间的关系。对于表贴式 PMSM，Ld=Lq。

上述方程用到了以下变量。

|  |  |
| --- | --- |
| *Lq*, *Ld* | *q* 轴和 *d* 轴电感 (H) |
| *R* | 定子绕组的电阻 (ohm) |
| *iq*, *id* | *q* 轴和 *d* 轴电流 (A) |
| *vq*, *vd* | *q* 轴和 *d* 轴电压 (V) |
| *ωm* | 电机的机械角速度（弧度/秒） |
| *ωe* | 电机的电气角速度（弧度/秒） |
| *λpm* | 永磁磁链(Wb) |
| *Ke* | 反电动势 (EMF)（Vpk\_LL/krpm，其中 Vpk\_LL 是线电压峰值） |
| *Kt* | 转矩常量 (N·m/A)  *Kt* = 电机的额定转矩 / *Ia\_peak\_rated*，其中，*Ia\_peak\_rated* 是 *a* 相在额定电流操作时的峰值振幅。 |
| *P* | 极对数 |
| *Te* | 电磁转矩 (Nm) |
| *Θe* | 电气角（弧度） |

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
| `PwrInfo` | `PwrTrnsfrd` - 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrMtr` | 机械功率 | *Pmot* | Pmot= −ωmTe |
| `PwrBus` | 电功率 | *Pbus* | Pbus= vania+ vbnib+vcnic |
| `PwrNotTrnsfrd` - 功率越过模块边界，但未传输  - 正信号表示输入 - 负信号表示损失 | `PwrElecLoss` | 电阻功率损失 | *Pelec* | Pelec= −32(Rsisd2+Rsisq2) |
| `PwrMechLoss` | 机械功率损失 | *Pmech* | 当**端口配置**设置为**转矩**时：  Pmech= −(ωm2F+ |ωm|Tf)  当**端口配置**设置为**转速**时：  Pmech= 0 |
| `PwrStored` - 储存的能量变化率  - 正信号表示增加 - 负信号表示减少 | `PwrMtrStored` | 储存的电机功率 | *Pstr* | Pstr= Pbus+ Pmot+ Pelec + Pmech |

上述方程用到了以下变量。

|  |  |
| --- | --- |
| *Rs* | 定子电阻(欧姆) |
| *ia*, *ib*, *ic* | 定子相位 *a*、*b* 和 *c* 电流 (A) |
| *isq*, *isd* | 定子 *q* 轴和 *d* 轴电流 (A) |
| *van*, *vbn*, *vcn* | 定子相位 *a*、*b* 和 *c* 电压 (V) |
| *ωm* | 电机的机械角速度（弧度/秒） |
| *F* | 电机和负载组合粘性阻尼 N·m/（弧度/秒） |
| *Te* | 电磁转矩 (Nm) |
| *Tf* | 电机和负载组合摩擦转矩 (Nm) |

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
