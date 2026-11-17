---
type: simulink-block
title: 'Induction Motor HDL'
family: 'motor-control-blockset-hdl-support'
product_id: 'motor-control-blockset-hdl-support'
product_name: 'Motor Control Blockset HDL Support'
documentation_release: R2025b
official_category: 'Electrical Systems / Motors'
documentation_page: 'inductionmotorhdl'
documentation_source_path: '../mcb/ref/inductionmotorhdl.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Motor HDL

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

Induction Motor HDL 模块的配置信号，包含模块配置参数。

**数据类型：** `single`

### **PhaseVolt** — 定子端电压 `1`×`3` 数组

定子端电压 *Va*、*Vb* 和 *Vc*，单位为 V。

**数据类型：** `single`

### **LdTrq/Spd** — 电机负载转矩或电机轴转速 标量

该端口支持以下输入之一：

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
| `MtrSpd` | | | 转子机械角速度 | *ωm* | rad/s |
| `MtrMechPos` | | | 转子机械角位置 | *θm* | rad |
| `MtrPos` | | | 转子电角位置 | *θe* | rad |
| `MtrTrq` | | | 电磁转矩 | *Te* | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | 机械功率 | *Pmot* | W |
| `PwrBus` | 电功率 | *Pbus* | W |
| `PwrNotTrnsfrd` | `PwrElecLoss` | 电阻功率损耗 | *Pelec* | W |
| `PwrMechLoss` | 机械功率损耗 | *Pmech* | W |
| `PwrStored` | `PwrMtrStored` | 电机储能功率 | *Pstr* | W |

### **PhaseCurr** — *a*、*b* 和 *c* 相电流 `1`×`3` 数组

*a*、*b* 和 *c* 相的电流，分别为 *ia*、*ib* 和 *ic*，单位为 A。

### **Torque** — 电机转矩 `标量`

电机转矩 *Tmtr*，单位为 N·m。

### **Speed** — 电机转速 `标量`

电机的角速度 *ωmtr*，单位为 rad/s。

### **MtrElecAngle** — 电机电角度 标量

电机的电位置 *θdq*，单位为 rad。

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
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2022b 中引入**

## 描述

三相感应电机

Induction Motor HDL 模块实现了一个三相感应电机。该模块使用三相输入电压来调节各相电流，从而控制电机转矩或转速。

该模块使用 **Sample Time (s)** 参数为固定步长双精度和单精度目标生成代码。它支持面向 FPGA 部署的代码生成，并生成 HDL 兼容代码。

您可以使用 **Config** 输入端口指定感应电机参数和工作模式。您还可以使用 Induction Motor Configuration 模块生成所需的配置信号，以在 **Config** 输入端口进行指定。

### 三相正弦模型电气系统

该模块实现以静止转子参考（*dq*）坐标系表示的方程。*d* 轴与 *a* 轴对齐。转子参考坐标系中的所有量均折算到定子侧。

该模块使用以下方程计算电角速度（*ωem*）和转差速度（*ωslip*）。

ωem=Pωmωslip= ωsyn−ωem

为了计算相对于转子 *A* 轴（*dA*）的 *dq* 转子电角速度，该模块使用定子 *a* 轴（*da*）速度与转差速度之间的差值：

ωdA= ωda− ωem

为了简化磁链、电压和电流变换的方程，该模块使用转子 A 轴参考坐标系：

ωda=ωemωdA=0

| 计算 | 方程 |
| --- | --- |
| 磁链 | ddt[λsdλsq]= [vsdvsq]− Rs[isdisq]− ωda[0−110][λsdλsq]ddt[λrdλrq]= [vrdvrq]− Rr[irdirq]− ωdA[0−110][λrdλrq]      [λsdλsqλrdλrq]= [Ls00LsLm00LmLm00LmLr00Lr][isdisqirdirq] |
| 电流 | [isdisqirdirq]= (1Lm2− LrLs)[−Lr00−LrLm00LmLm00Lm−Ls00−Ls][λsdλsqλrdλrq] |
| 电感 | Ls= Lls+LmLr= Llr+Lm |
| 电磁转矩 | Te=PLm(isqird− isdirq) |
| 功率不变 *dq* 变换，以确保 *dq* 功率与三相功率相等 | [vsdvsq]= 23 [cos(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda)−sin(Θda−2π3)−sin(Θda+2π3)][vavbvc]      [iaibic]= 23  [cos(Θda)−sin(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda−2π3)−sin(Θda+2π3)][isdisq] |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ωm* | 转子角速度（rad/s） |
| *ωem* | 转子电角速度（rad/s） |
| *ωslip* | 转子电转差速度（rad/s） |
| *ωsyn* | 转子同步速度（rad/s） |
| *ωda* | 相对于定子 a 轴的 dq 定子电角速度（rad/s） |
| *ωdA* | 相对于转子 A 轴的 dq 定子电角速度（rad/s） |
| *Θda* | 相对于定子 a 轴的 dq 定子电角度（rad） |
| *ΘdA* | 相对于转子 A 轴的 dq 定子电角度（rad） |
| *Lq*、*Ld* | q 轴和 d 轴电感（H） |
| *Ls* | 定子电感（H） |
| *Lr* | 转子电感（H） |
| *Lm* | 励磁电感（H） |
| *Lls* | 定子漏电感（H） |
| *Llr* | 转子漏电感（H） |
| *vsq*、*vsd* | 定子 q 轴和 d 轴电压（V） |
| *isq*、*isd* | 定子 q 轴和 d 轴电流（A） |
| *λsq*、*λsd* | 定子 q 轴和 d 轴磁链（Wb） |
| *irq*、*ird* | 转子 q 轴和 d 轴电流（A） |
| *λrq*、*λrd* | 转子 q 轴和 d 轴磁链（Wb） |
| *va*、*vb*、*vc* | 定子电压 a、b、c 相（V） |
| *ia*、*ib*、*ic* | 定子电流 a、b、c 相（A） |
| *Rs* | 定子绕组电阻（Ohm） |
| *Rr* | 转子绕组电阻（Ohm） |
| *P* | 极对数 |
| *Te* | 电磁转矩（Nm） |

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

对于电机功率计算，该模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` |  | `PwrMtr` | 机械功率 | *Pmot* | Pmot= −ωmTe |
| `PwrBus` | 电功率 | *Pbus* | Pbus= vania+ vbnib+vcnic |
|  | `PwrElecLoss` | 电阻功率损耗 | *Pelec* | Pelec= −(Rsisd2+Rsisq2+−Rrird2+Rrirq2) |
| `PwrMechLoss` | 机械功率损耗 | *Pmech* | 当 **Port Configuration** 设置为 `Torque` 时：  Pmech= −(ωm2F+ |ωm|Tf)  当 **Port Configuration** 设置为 `Speed` 时：  Pmech= 0 |
|  | `PwrMtrStored` | 存储的电机功率 | *Pstr* | Pstr= Pbus+ Pmot+ Pelec + Pmech |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Rs* | 定子电阻 (Ohm) |
| *Rr* | 转子电阻 (Ohm) |
| *ia*,*ib*,*ic* | 定子 a、b 和 c 相电流 (A) |
| *isq*,*isd* | 定子 q 轴和 d 轴电流 (A) |
| *van*, *vbn*, *vcn* | 定子 a、b 和 c 相电压 (V) |
| *ωm* | 转子的角机械速度 (rad/s) |
| *F* | 电机和负载的组合粘性阻尼 (N·m/(rad/s)) |
| *Te* | 电磁转矩 (Nm) |
| *Tf* | 电机和负载的组合摩擦转矩 (Nm) |
