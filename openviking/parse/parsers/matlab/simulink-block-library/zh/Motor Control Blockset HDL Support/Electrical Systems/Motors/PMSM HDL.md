---
type: simulink-block
title: 'PMSM HDL'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Electrical Systems / Motors'
documentation_page: 'pmsmhdl'
documentation_source_path: '../mcb/ref/pmsmhdl.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM HDL

## 端口
```yaml
ports:
- name: Config
  summary: 模块配置信号向量
  direction: input
  data_types: single
- name: PhaseVolt
  summary: 定子端电压 1×3 数组
  direction: input
  data_types: single
- name: LdTrq/Spd
  summary: 电机负载转矩或电机轴转速 标量
  direction: input
  data_types: single
- name: Reset
  summary: 复位总线信号 标量
  direction: input
  data_types: Boolean
- name: Info
  summary: 总线信号 总线
  direction: output
- name: PhaseCurr
  summary: '*a*、*b* 和 *c* 相电流 1×3 数组'
  direction: output
- name: Torque
  summary: 电机转矩 标量
  direction: output
- name: Speed
  summary: 电机转速 标量
  direction: output
- name: MtrElecAngle
  summary: 电机电角度 标量
  direction: output
  data_types: single
```

### 输入

### **Config** — 模块配置信号向量

PMSM HDL 模块的配置信号，包含模块配置参数。有关组成参数的详细信息，请参阅 PMSM Configuration 模块的 **Config** 输出。

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

模块用于复位内部积分器的复位总线信号。

**数据类型：** `Boolean`
### 输出

### **Info** — 总线信号 总线

该总线信号包含以下模块计算结果。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `IaStator` | | | 定子 A 相电流 | *ia* | A |
| `IbStator` | | | 定子 B 相电流 | *ib* | A |
| `IcStator` | | | 定子 C 相电流 | *ic* | A |
| `IdSync` | | | 直轴电流 | *id* | A |
| `IqSync` | | | 交轴电流 | *iq* | A |
| `VdSync` | | | 直轴电压 | *vd* | V |
| `VqSync` | | | 交轴电压 | *vq* | V |
| `MtrSpd` | | | 电机的机械角速度 | *ωm* | rad/s |
| `MtrPos` | | | 电机机械角位置 | *θm* | rad |
| `MtrTrq` | | | 电磁转矩 | *Te* | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | 机械功率 | *Pmot* | W |
| `PwrBus` | 电功率 | *Pbus* | W |
| `PwrNotTrnsfrd` | `PwrElecLoss` | 电阻功率损耗 | *Pelec* | W |
| `PwrMechLoss` | 机械功率损耗 | *Pmech* | W |
| `PwrStored` | `PwrMtrStored` | 电机存储功率 | *Pstr* | W |

### **PhaseCurr** — *a*、*b* 和 *c* 相电流 `1`×`3` 数组

*a*、*b* 和 *c* 相的电流，分别为 *ia*、*ib* 和 *ic*，单位为 A。

### **Torque** — 电机转矩 `标量`

电机转矩 *Tmtr*，单位为 N·m。

### **Speed** — 电机转速 `标量`

电机的角速度 *ωmtr*，单位为 rad/s。

### **MtrElecAngle** — 电机电角度 标量

电机的电位置 *θe*，单位为 rad。

**数据类型：** `single`
## 参数
```yaml
parameters:
- name: Sample time (s)
  summary: 模块再次执行前的采样时间 1e-6（默认）| 标量
  group: ''
```

### **Sample time (s)** — 模块再次执行前的采样时间 `1e-6`（默认）| 标量

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

**在 R2022b 中引入**

## 描述

具有正弦反电动势的三相永磁同步电机

PMSM HDL 模块实现了一个具有正弦反电动势的三相永磁同步电机（PMSM）。该模块使用三相输入电压来调节各相电流，从而控制电机转矩或转速。

该模块使用 **Sample Time (s)** 参数为固定步长双精度和单精度目标生成代码。它支持面向 FPGA 部署的代码生成，并生成 HDL 兼容代码。

您可以使用 **Config** 输入端口指定 PMSM 参数和工作模式。您也可以使用 PMSM Configuration 模块生成所需的配置信号，以在 **Config** 输入端口处指定。

### 电机结构

这些图展示了电机上具有单极对的内部式和表贴式 PMSM 结构。

由永磁体产生的电机磁场随电机角度产生正弦变化的磁通变化率。

对于轴约定，当电机角度 *θr* 为零时，相-*a* 与 *d* 轴对齐。

### 三相正弦模型电气系统

该模块实现以下以电机磁通参考坐标系（*dq* 坐标系）表示的方程。电机参考坐标系中的所有量均以定子为参考。

ωe=Pωmddtid=1Ldvd−RLdid+LqLdPωmiq

ddtiq=1Lqvq−RLqiq−LdLqPωmid−λpmPωmLq

Te=1.5P[λpmiq+(Ld−Lq)idiq]

*Lq* 和 *Ld* 电感表示由于电机磁体凸极性导致的相电感与电机位置之间的关系。对于表贴式 PMSM，Ld=Lq。

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Lq*，*Ld* | *q* 轴和 *d* 轴电感（H） |
| *R* | 定子绕组电阻（ohm） |
| *iq*，*id* | *q* 轴和 *d* 轴电流（A） |
| *vq*，*vd* | *q* 轴和 *d* 轴电压（V） |
| *ωm* | 电机机械角速度（rad/s） |
| *ωe* | 电机电角速度（rad/s） |
| *λpm* | 永磁体磁链（Wb） |
| *Ke* | 反电动势（EMF）（Vpk\_LL/krpm，其中 Vpk\_LL 是线电压峰值测量值） |
| *Kt* | 转矩常数（N·m/A）  *Kt* = 电机额定转矩 / *Ia\_peak\_rated*，其中 *Ia\_peak\_rated* 是额定电流运行时相-*a* 的峰值幅值。 |
| *P* | 极对数 |
| *Te* | 电磁转矩（Nm） |
| *Θe* | 电角度（rad） |

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

### Power Accounting

对于电机功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrMtr` | 机械功率 | *Pmot* | Pmot= −ωmTe |
| `PwrBus` | 电功率 | *Pbus* | Pbus= vania+ vbnib+vcnic |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损耗 | `PwrElecLoss` | 电阻功率损耗 | *Pelec* | Pelec= −32(Rsisd2+Rsisq2) |
| `PwrMechLoss` | 机械功率损耗 | *Pmech* | 当 **Port Configuration** 设置为 `Torque` 时：  Pmech= −(ωm2F+ |ωm|Tf)  当 **Port Configuration** 设置为 `Speed` 时：  Pmech= 0 |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrMtrStored` | 存储的电机功率 | *Pstr* | Pstr= Pbus+ Pmot+ Pelec + Pmech |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Rs* | 定子电阻 (ohm) |
| *ia*,*ib*,*ic* | 定子相 *a*、*b* 和 *c* 电流 (A) |
| *isq*,*isd* | 定子 *q* 轴和 *d* 轴电流 (A) |
| *van*, *vbn*, *vcn* | 定子相 *a*、*b* 和 *c* 电压 (V) |
| *ωm* | 电机的角机械速度 (rad/s) |
| *F* | 电机和负载的组合粘性阻尼 N·m/(rad/s) |
| *Te* | 电磁转矩 (Nm) |
| *Tf* | 电机和负载的组合摩擦转矩 (Nm) |

### Amplitude Invariant *dq* Transformation

该模块使用以下方程实现幅值不变 *dq* 变换，以确保 *dq* 和三
相幅值相等。

[vsdvsq]= 23 [cos(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda)−sin(Θda−2π3)−sin(Θda+2π3)][vavbvc]

[iaibic]=   [cos(Θda)−sin(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda−2π3)−sin(Θda+2π3)][isdisq]

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Θda* | 相对于转子 *a* 轴的 *dq* 定子电角度 (rad) |
| *vsq*, *vsd* | 定子 *q* 轴和 *d* 轴电压 (V) |
| *isq*,*isd* | 定子 *q* 轴和 *d* 轴电流 (A) |
| *va*,*vb*,*vc* | 定子电压相 *a*、*b*、*c* (V) |
| *ia*, *ib*, *ic* | 定子电流相 *a*、*b*、*c* (A) |
