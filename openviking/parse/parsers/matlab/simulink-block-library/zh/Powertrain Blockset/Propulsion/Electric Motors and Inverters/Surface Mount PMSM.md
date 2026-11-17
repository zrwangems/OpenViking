---
type: simulink-block
title: 'Surface Mount PMSM'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motors and Inverters'
documentation_page: 'surfacemountpmsm'
documentation_source_path: 'ref/surfacemountpmsm.html'
language: zh-CN
chinese_source: worker-translation
---

# Surface Mount PMSM

## 端口
```yaml
ports:
- name: LdTrq
  summary: 电机上的负载转矩 scalar
  direction: input
- name: Spd
  summary: 电机轴转速 scalar
  direction: input
- name: PhaseVolt
  summary: 定子端电压 1-by-3 array
  direction: input
- name: Info
  summary: 总线信号 bus
  direction: output
- name: PhaseCurr
  summary: a、b、c 相电流 1-by-3 array
  direction: output
- name: MtrTrq
  summary: 电机转矩 scalar
  direction: output
- name: MtrSpd
  summary: 电机转速 scalar
  direction: output
```

### 输入

### **LdTrq** — 电机上的负载转矩 `scalar`

电机轴上的负载转矩，
*Tm*，单位为 N·m。

#### 依赖

要创建此端口，请为
**Mechanical input configuration**
参数选择 `Torque`。

### **Spd** — 电机轴转速 `scalar`

电机的角速度，
*ωm*，单位为 rad/s。

#### 依赖

要创建此端口，请为
**Mechanical input configuration**
参数选择 `Speed`。

### **PhaseVolt** — 定子端电压 `1`-by-`3` array

定子端电压，
*Va*、
*Vb* 和
*Vc*，单位为 V。
### 输出

### **Info** — 总线信号 bus

该总线信号包含以下模块计算量。

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
| `PwrStored` | `PwrMtrStored` | 电机储存功率 | *Pstr* | W |

### **PhaseCurr** — a、b、c 相电流 `1`-by-`3` array

a、b、c 相电流，*ia*、
*ib* 和
*ic*，单位为 A。

### **MtrTrq** — 电机转矩 `scalar`

电机转矩，*Tmtr*，单位为
N·m。

#### 依赖

要创建此端口，请为
**Mechanical input configuration**
参数选择 `Speed`。

### **MtrSpd** — 电机转速 `scalar`

电机的角速度，
*ωmtr*，单位为 rad/s。

#### 依赖

要创建此端口，请为
**Mechanical input configuration**
参数选择 `Torque`。
## 参数
```yaml
parameters:
- name: Mechanical input configuration
  summary: 选择端口配置 Torque (default) | Speed
  group: ''
  block_parameter: port_config
  values: Torque (default) | Speed
- name: Simulation type
  summary: 选择仿真类型 Continuous (default) | Discrete
  group: ''
  block_parameter: sim_type
  values: Continuous (default) | Discrete
- name: Sample Time (Ts)
  summary: 离散积分采样时间 0.001 (default) | scalar
  group: ''
  block_parameter: Ts
  values: 0.001 (default) | scalar
- name: Number of pole pairs (P)
  summary: 极对数 4（默认）| scalar
  group: ''
  block_parameter: P
  values: 4（默认）| scalar
- name: Stator resistance per phase (Rs)
  summary: 电阻 .2（默认）| scalar
  group: ''
  block_parameter: Rs
  values: .2（默认）| scalar
- name: Stator d-axis inductance (Ldq_)
  summary: 电感 3.752e-4（默认）| scalar
  group: ''
  block_parameter: Ldq_
  values: 3.752e-4（默认）| scalar
- name: Permanent flux linkage constant (lambda_pm)
  summary: 磁链 0.1194（默认）| scalar
  group: ''
  block_parameter: lambda_pm
  values: 0.1194（默认）| scalar
- name: Back-emf constant (Ke)
  summary: 反电动势 159.9771（默认）| scalar
  group: ''
  block_parameter: Ke
  values: 159.9771（默认）| scalar
- name: Torque constant (Kt)
  summary: 转矩常数 1.323（默认）| scalar
  group: ''
  block_parameter: Kt
  values: 1.323（默认）| scalar
- name: Physical inertia, viscous damping, static friction (mechanical)
  summary: 惯量、阻尼、摩擦 [0.002700,4.924e-4,0]（默认）| vector
  group: ''
  block_parameter: mechanical
  values: '[0.002700,4.924e-4,0]（默认）| vector'
- name: 初始 d 轴和 q 轴电流 (idq0)
  summary: 电流 [0 0]（默认）| vector
  group: ''
  block_parameter: idq0
  values: '[0 0] (default) | vector'
- name: Initial mechanical position (theta_init)
  summary: Angle 0 (default) | scalar
  group: ''
  block_parameter: theta_init
  values: 0 (default) | scalar
- name: Initial mechanical speed (omega_init)
  summary: Speed 0 (default) | scalar
  group: ''
  block_parameter: omega_init
  values: 0 (default) | scalar
```

#### 模块选项

### **Mechanical input configuration** — 选择端口配置 `Torque` (default) | `Speed`

下表总结了端口配置。

| 端口配置 | 创建输入端口 | 创建输出端口 |
| --- | --- | --- |
| `Torque` | `LdTrq` | `MtrSpd` |
| `Speed` | `Spd` | `MtrTrq` |

#### 编程用法

要以编程方式设置模块参数值，
请使用 `set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `port_config` |
| **值**：| `Torque` (default) | `Speed` |
| **Data Types:** | `character vector` |

### **Simulation type** — 选择仿真类型 `Continuous` (default) | `Discrete`

默认情况下，该模块在仿真期间使用连续采样时间。如果要为单精度目标生成代码，请考虑将该参数设置为 `Discrete`。

#### 编程用法

要以编程方式设置模块参数值，
请使用 `set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `sim_type` |
| **值**：| `Continuous` (default) | `Discrete` |
| **Data Types:** | `character vector` |

#### 依赖

将 **Simulation type** 设置为 `Discrete` 会创建 **Sample Time, Ts** 参数。

### **Sample Time (Ts)** — 离散积分采样时间 `0.001` (default) | `scalar`

离散仿真的积分采样时间，单位为 s。

#### 编程用法

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `Ts` |
| **值**：| `0.001` (default) | `scalar` |
| **Data Types:** | `double` |

#### 依赖关系

将 **Simulation type** 设置为
`Discrete` 会创建 **Sample
Time, Ts** 参数。

#### 参数

### **Number of pole pairs (P)** — 极对数 `4`（默认）| `scalar`

电机极对数，*P*。

#### 编程使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `P` |
| **值**：| `4`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Stator resistance per phase (Rs)** — 电阻 `.2`（默认）| `scalar`

每相定子相电阻，
*Rs*，单位为欧姆。

#### 编程使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `Rs` |
| **值**：| `.2`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Stator d-axis inductance (Ldq\_)** — 电感 `3.752e-4`（默认）| `scalar`

定子电感，*Ldq*，单位为
H。

#### 编程使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `Ldq_` |
| **值**：| `3.752e-4`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Permanent flux linkage constant (lambda\_pm)** — 磁链 `0.1194`（默认）| `scalar`

永磁磁链常数，
*λpm*，单位为 Wb。

#### 编程使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `lambda_pm` |
| **值**：| `0.1194`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Back-emf constant (Ke)** — 反电动势 `159.9771`（默认）| `scalar`

反电动势，EMF，
*Ke*，单位为峰值 Vpk\_LL/krpm。
Vpk\_LL 是线电压峰值测量值。

为了计算永磁磁链常数，该模块实现
以下方程。

λpm=13⋅Ke1000P⋅602π

#### 编程使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `Ke` |
| **值**：| `159.9771`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Torque constant (Kt)** — 转矩常数 `1.323`（默认）| `scalar`

转矩常数，*Kt*，单位为
N·m/A。

*Kt* = 电机额定转矩 /
*Ia\_peak\_rated*，其中 *Ia\_peak\_rated*
是额定电流运行时的相 *a* 峰值幅度。

为了计算永磁磁链常数，该模块实现
以下方程。

λpm=23⋅KtP

#### 编程使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `Kt` |
| **值**：| `1.323`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Physical inertia, viscous damping, static friction (mechanical)** — 惯量、阻尼、摩擦 `[0.002700,4.924e-4,0]`（默认）| `vector`

电机的机械属性：

- 惯量，*J*，单位为 kg.m^2
- 粘性阻尼，*F*，单位为 N·m/(rad/s)
- 静摩擦，*Tf*，
  单位为 N·m

#### 编程使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **Parameter:** | `mechanical` |
| **值**：| `[0.002700,4.924e-4,0]`（默认）| `vector` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请将 **Mechanical input
configuration** 参数设置为
`Torque`。

#### Initial Values

### **初始 d 轴和 q 轴电流 (idq0)** — 电流 `[0 0]`（默认）| `vector`

初始 q 轴和 d 轴电流，*iq、id*，单位为 A。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `idq0` |
| **值**：| `[0 0]` (default) | `vector` |
| **Data Types:** | `double` |

### **Initial mechanical position (theta\_init)** — Angle `0` (default) | `scalar`

电机初始角位置，*θm0*，单位为 rad。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `theta_init` |
| **值**：| `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Initial mechanical speed (omega\_init)** — Speed `0` (default) | `scalar`

电机初始角速度，*ωm0*，单位为 rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `omega_init` |
| **值**：| `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，请将 **Mechanical input configuration** 参数设置为 `Torque`。
## 所属库

Powertrain Blockset / Propulsion / Electric Motors and Inverters Motor Control Blockset / Electrical Systems / Motors

## 模块特性

Not documented in R2025b.

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

具有正弦反电动势的三相外置式永磁同步电机

Surface Mount PMSM 模块实现了一个具有正弦反电动势的三相外置式永磁同步电机（PMSM）。该模块使用三相输入电压来调节各相电流，从而可以控制电机转矩或速度。

默认情况下，该模块将 **Simulation type** 参数设置为 `Continuous`，以便在仿真期间使用连续采样时间。如果要为固定步长双精度和单精度目标生成代码，请考虑将该参数设置为 `Discrete`。然后指定 **Sample Time, Ts** 参数。

在 **Parameters** 选项卡上，如果选择 `Back-emf constant (Ke)` 或 `Torque constant (Kt)`，则该模块实现以下方程之一来计算永磁磁链常数。

| Setting | Equation |
| --- | --- |
| `Back-emf constant (Ke)` | λpm=13⋅Ke1000P⋅602π |
| `Torque constant (Kt)` | λpm=23⋅KtP |

### Motor Construction

此图显示了转子上具有单对极的电机结构。

具有两极转子的 PMSM 表贴式电机

由永磁体产生的电机磁场会随电机角度产生正弦磁通变化率。

对于坐标轴约定，当电机角度 *θr* 为零时，*a* 相磁通与永磁体磁通对齐。

### Three-Phase Sinusoidal Model Electrical System

该模块实现以下方程，这些方程在电机磁通参考坐标系（dq 坐标系）中表示。电机参考坐标系中的所有量均折算到定子侧。

ωe=Pωmddtid=1Ldvd−RLdid+LqLdPωmiq

ddtiq=1Lqvq−RLqiq−LdLqPωmid−λpmPωmLq

Te=1.5P[λpmiq+(Ld−Lq)idiq]

*Lq* 和 *Ld* 电感表示由于电机磁体凸极性导致的相电感与电机位置之间的关系。对于表贴式 PMSM，Ld=Lq。

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Lq*，*Ld* | q 轴和 d 轴电感（H） |
| *R* | 定子绕组电阻（ohm） |
| *iq*，*id* | q 轴和 d 轴电流（A） |
| *vq*，*vd* | q 轴和 d 轴电压（V） |
| *ωm* | 电机机械角速度（rad/s） |
| *ωe* | 电机电角速度（rad/s） |
| *λpm* | 永磁体磁链（Wb） |
| *Ke* | 反电动势（EMF）（Vpk\_LL/krpm，其中 Vpk\_LL 是线电压峰值测量值） |
| *Kt* | 转矩常数（N·m/A） *Kt* = 电机额定转矩 / *Ia\_peak\_rated*，其中 *Ia\_peak\_rated* 是额定电流运行时 a 相电流的峰值幅值。 |
| *P* | 极对数 |
| *Te* | 电磁转矩（Nm） |
| *Θe* | 电角度（rad） |

### Mechanical System

电机角速度由下式给出：

ddtωm=1J(Te−Tf−Fωm−Tm)dθmdt=ωm

这些方程使用以下变量。

|  |  |
| --- | --- |
| *J* | 电机和负载的合成惯量（kgm^2） |
| *F* | 电机和负载的合成粘性摩擦（N·m/(rad/s)） |
| *θm* | 电机机械角位置（rad） |
| *Tm* | 电机轴转矩（Nm） |
| *Te* | 电磁转矩（Nm） |
| *Tf* | 电机轴静摩擦转矩（Nm） |
| *ωm* | 电机机械角速度（rad/s） |

### Power Accounting

对于功率核算，该模块实现以下方程。

| Bus Signal | | | Description | Variable | Equations |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrMtr` | 机械功率 | *Pmot* | Pmot= −ωmTe |
| `PwrBus` | 电功率 | *Pbus* | Pbus= vania+ vbnib+vcnic |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损耗 | `PwrElecLoss` | 电阻功率损耗 | *Pelec* | Pelec= −32(Rsisd2+Rsisq2) |
| `PwrMechLoss` | 机械功率损耗 | *Pmech* | 当 **Mechanical input configuration** 设置为 `Torque` 时：  Pmech= −(ωm2F+ |ωm|Tf)  当 **Mechanical input configuration** 设置为 `Speed` 时：  Pmech= 0 |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrMtrStored` | 电机存储功率 | *Pstr* | Pstr= Pbus+ Pmot+ Pelec + Pmech |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Rs* | 定子电阻（ohm） |
| *ia*，*ib*，*ic* | 定子 a、b 和 c 相电流（A） |
| *isq*，*isd* | 定子 q 轴和 d 轴电流（A） |
| *van*，*vbn*，*vcn* | 定子 a、b 和 c 相电压（V） |
| *ωm* | 电机机械角速度（rad/s） |
| *F* | 电机和负载的合成粘性阻尼 N·m/(rad/s) |
| *Te* | 电磁转矩（Nm） |
| *Tf* | 电机和负载的合成摩擦转矩（Nm） |

### Amplitude Invariant *dq* Transformation

该模块使用以下方程实现幅值不变 *dq* 变换，以确保 *dq* 幅值与三相幅值相等。

[vsdvsq]= 23 [cos(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda)−sin(Θda−2π3)−sin(Θda+2π3)][vavbvc]

[iaibic]=   [cos(Θda)−sin(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda−2π3)−sin(Θda+2π3)][isdisq]

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Θda* | 相对于转子 *a* 轴的 *dq* 定子电角度（rad） |
| *vsq*, *vsd* | 定子 *q* 轴和 *d* 轴电压（V） |
| *isq*,*isd* | 定子 *q* 轴和 *d* 轴电流（A） |
| *va*,*vb*,*vc* | 定子电压相 *a*、*b*、*c*（V） |
| *ia*, *ib*, *ic* | 定子电流相 *a*、*b*、*c*（A） |
