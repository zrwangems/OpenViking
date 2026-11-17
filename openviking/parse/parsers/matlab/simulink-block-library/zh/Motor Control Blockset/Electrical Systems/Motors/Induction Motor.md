---
type: simulink-block
title: 'Induction Motor'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Electrical Systems / Motors'
documentation_page: 'inductionmotor'
documentation_source_path: 'ref/inductionmotor.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Motor

## 端口
```yaml
ports:
- name: LdTrq
  summary: 电机上的负载转矩 标量
  direction: input
- name: Spd
  summary: 转子轴转速 标量
  direction: input
- name: PhaseVolt
  summary: 定子端电压 1×3 数组
  direction: input
- name: Info
  summary: 总线信号 总线
  direction: output
- name: PhaseCurr
  summary: a、b、c 相电流 1×3 数组
  direction: output
- name: MtrTrq
  summary: 电机转矩 标量
  direction: output
- name: MtrSpd
  summary: 电机转速 标量
  direction: output
```

### 输入

### **LdTrq** — 电机上的负载转矩 `标量`

电机轴上的负载转矩，
*Tm*，单位为 N·m。

#### 依赖

要创建此端口，请为
**端口配置**参数选择 `Torque`。

### **Spd** — 转子轴转速 `标量`

转子的角速度，
*ωm*，单位为 rad/s。

#### 依赖

要创建此端口，请为
**端口配置**参数选择 `Speed`。

### **PhaseVolt** — 定子端电压 `1`×`3` 数组

定子端电压，
*Va*、
*Vb* 和
*Vc*，单位为 V。
### 输出

### **Info** — 总线信号 总线

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
| `MtrSpd` | | | 转子的机械角速度 | *ωm* | rad/s |
| `MtrMechPos` | | | 转子机械角位置 | *θm* | rad |
| `MtrPos` | | | 转子电角位置 | *θe* | rad |
| `MtrTrq` | | | 电磁转矩 | *Te* | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | 机械功率 | *Pmot* | W |
| `PwrBus` | 电功率 | *Pbus* | W |
| `PwrNotTrnsfrd` | `PwrElecLoss` | 电阻功率损耗 | *Pelec* | W |
| `PwrMechLoss` | 机械功率损耗 | *Pmech* | W |
| `PwrStored` | `PwrMtrStored` | 电机储能功率 | *Pstr* | W |

### **PhaseCurr** — a、b、c 相电流 `1`×`3` 数组

a、b、c 相电流，*ia*、
*ib* 和
*ic*，单位为 A。

### **MtrTrq** — 电机转矩 `标量`

电机转矩，*Tmtr*，单位为
N·m。

#### 依赖

要创建此端口，请为
**端口配置**参数选择 `Speed`。

### **MtrSpd** — 电机转速 `标量`

电机的角速度，
*ωmtr*，单位为 rad/s。

#### 依赖

要创建此端口，请为
**端口配置**参数选择 `Torque`。
## 参数
```yaml
parameters:
- name: Simulation type
  summary: 选择仿真类型 Continuous（默认）| Discrete
  group: ''
  block_parameter: sim_type
  values: Continuous（默认）| Discrete
- name: Sample time, Ts
  summary: 离散积分采样时间 0.001（默认）| 标量
  group: ''
  block_parameter: Ts
  values: 0.001（默认）| 标量
- name: Port configuration
  summary: 选择端口配置 Torque（默认）| Speed
  group: ''
  block_parameter: port_config
  values: Torque（默认） | Speed
- name: File
  summary: 电机参数 ".m" 或 ".mat" 文件的路径 scalar
  group: ''
- name: Number of pole pairs, P
  summary: 极对数 2（默认） | scalar
  group: ''
  block_parameter: P
  values: 2（默认） | scalar
- name: Stator resistance and leakage inductance, Zs
  summary: 电阻和电感 [1.77 0.0139]（默认） | vector
  group: ''
  block_parameter: Zs
  values: '[1.77 0.0139]（默认） | vector'
- name: Rotor resistance and leakage inductance, Zr
  summary: 电阻和电感 [1.34 0.0121]（默认） | vector
  group: ''
  block_parameter: Zr
  values: '[1.34 0.0121]（默认） | vector'
- name: Magnetizing inductance, Lm
  summary: 电感 0.3687（默认） | scalar
  group: ''
  block_parameter: Lm
  values: 0.3687（默认） | scalar
- name: Physical inertia, viscous damping, static friction, mechanical
  summary: 惯量、阻尼、摩擦 [0.001 0 0]（默认） | vector
  group: ''
  block_parameter: mechanical
  values: '[0.001 0 0]（默认） | vector'
- name: 初始机械位置，theta_init
  summary: 角位置 0（默认）| scalar
  group: ''
  block_parameter: theta_init
  values: 0（默认）| scalar
- name: 初始机械转速，omega_init
  summary: 角速度 0（默认）| scalar
  group: ''
  block_parameter: omega_init
  values: 0（默认）| scalar
```

#### 模块选项

### **Simulation type** — 选择仿真类型 `Continuous`（默认）| `Discrete`

默认情况下，该模块在仿真期间使用连续采样时间。如果要为单精度目标生成代码，请考虑
将该参数设置为 `Discrete`。

#### 程序化使用

要以程序化方式设置模块参数值，
请使用 `set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sim_type` |
| **值：** | `Continuous`（默认）| `Discrete` |
| **数据类型：** | `character vector` |

#### 依赖

将 **Simulation Type** 设置为 `Discrete`
会创建 **Sample Time, Ts** 参数。

### **Sample time, Ts** — 离散积分采样时间 `0.001`（默认）| `标量`

离散仿真的积分采样时间，单位为
s。

#### 程序化使用

要以程序化方式设置模块参数值，
请使用 `set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ts` |
| **值：** | `0.001`（默认）| `标量` |
| **数据类型：** | `double` |

#### 依赖

将 **Simulation Type** 设置为
`Discrete` 会创建 **Sample Time,
Ts** 参数。

### **Port configuration** — 选择端口配置 `Torque`（默认）| `Speed`

下表总结了端口配置。

| 端口配置 | 创建输入端口 | 创建输出端口 |
| --- | --- | --- |
| `Torque` | `LdTrq` | `MtrSpd` |
| `Speed` | `Spd` | `MtrTrq` |

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `port_config` |
| **值：** | `Torque`（默认） | `Speed` |
| **数据类型：** | `character vector` |

#### 加载参数值

### **File** — 电机参数 ".m" 或 ".mat" 文件的路径 `scalar`

输入使用 Motor Control Blockset™ 参数估计工具保存的电机参数 ".m" 或 ".mat" 文件的路径。您也可以点击 **Browse** 按钮浏览并选择 ".m" 或 ".mat" 文件，并用文件名和路径更新 **File** 参数。有关电机参数估计过程的详细信息，请参阅 Estimate PMSM Parameters Using Parameter Estimation Blocks。

- **Load from file** - 点击此按钮从 ".m" 或 ".mat" 文件（由 **File** 参数指示）中读取估计的电机参数，并将其加载到电机模块中。
- **Save to file** - 点击此按钮从电机模块读取电机参数，并将其保存到 ".m" 或 ".mat" 文件中（文件名和位置在 **File** 参数中指定）。

**注意**

在点击 **Save to file** 按钮之前，请确保 **File** 参数中的目标文件名具有 ".m" 或 ".mat" 扩展名。如果使用任何其他文件扩展名，模块将显示错误消息。

#### 参数

### **Number of pole pairs, P** — 极对数 `2`（默认） | `scalar`

电机极对数，*P*。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `P` |
| **值：** | `2`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Stator resistance and leakage inductance, Zs** — 电阻和电感 `[1.77 0.0139]`（默认） | `vector`

定子电阻，*RS*，单位为欧姆；漏电感，*Lls*，单位为 H。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Zs` |
| **值：** | `[1.77 0.0139]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Rotor resistance and leakage inductance, Zr** — 电阻和电感 `[1.34 0.0121]`（默认） | `vector`

转子电阻，*Rr*，单位为欧姆；漏电感，*Llr*，单位为 H。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Zr` |
| **值：** | `[1.34 0.0121]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Magnetizing inductance, Lm** — 电感 `0.3687`（默认） | `scalar`

励磁电感，*Lm*，单位为 H。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lm` |
| **值：** | `0.3687`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Physical inertia, viscous damping, static friction, mechanical** — 惯量、阻尼、摩擦 `[0.001 0 0]`（默认） | `vector`

转子的机械特性：

- 惯量，*J*，单位为 kg·m^2
- 粘性阻尼，*F*，单位为 N·m/(rad/s)
- 静摩擦，*Tf*，单位为 N·m

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `mechanical` |
| **值：** | `[0.001 0 0]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **端口配置** 选择 `Torque`。

#### 初始值

### **初始机械位置，theta\_init** — 角位置 `0`（默认）| `scalar`

转子的初始角位置，
*θm0*，单位为 rad。

#### 程序化使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `theta_init` |
| **值：** | `0`（默认）| `scalar` |
| **数据类型：** | `double` |

### **初始机械转速，omega\_init** — 角速度 `0`（默认）| `scalar`

转子的初始角速度，
*ωm0*，单位为 rad/s。

#### 程序化使用

要以编程方式设置模块
参数值，请使用 `set_param`
函数。

要以编程方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `omega_init` |
| **值：** | `0`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖项

要启用此参数，请为 **端口配置** 选择 `Torque`。
## 所属库

Powertrain Blockset / Propulsion / Electric Motors and Inverters Motor Control Blockset / Electrical Systems / Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

三相感应电机

Induction Motor 模块实现了一个三相感应电机。该
模块使用三相输入电压来调节各相电流，
从而可以控制电机转矩或转速。

**注意**

该模块参数使用星形等效感应
电机的每相值。

默认情况下，该模块将 **仿真
类型** 参数设置为 `Continuous`，以便在仿真期间使用连续
采样时间。如果要为固定步长双精度和
单精度目标生成代码，请考虑将该参数设置为
`Discrete`。然后指定 **采样时间，Ts**
参数。

### Three-Phase Sinusoidal Model Electrical System

该模块实现以静止转子参考（dq）坐标系表示的方程。d 轴与 a 轴对齐。转子参考坐标系中的所有量均折算到定子侧。

三相感应电机电流与磁场

该模块使用这些方程计算电角速度
（*ωem*）和转差速度
（*ωslip*）。

ωem=Pωmωslip= ωsyn−ωem

为了计算相对于转子 A 轴
（*dA*）的 dq 转子电角速度，该模块使用定子 a 轴
（*da*）速度与转差速度之间的差值：

ωdA= ωda− ωem

为了简化磁链、电压和电流变换的方程，该模块使用转子 A 轴参考坐标系：

ωda=ωemωdA=0

| 计算 | 方程 |
| --- | --- |
| 磁链 | ddt[λsdλsq]= [vsdvsq]− Rs[isdisq]− ωda[0−110][λsdλsq]ddt[λrdλrq]= [vrdvrq]− Rr[irdirq]− ωdA[0−110][λrdλrq]      [λsdλsqλrdλrq]= [Ls00LsLm00LmLm00LmLr00Lr][isdisqirdirq] |
| 电流 | [isdisqirdirq]= (1Lm2− LrLs)[−Lr00−LrLm00LmLm00Lm−Ls00−Ls][λsdλsqλrdλrq] |
| 电感 | Ls= Lls+LmLr= Llr+Lm |
| 电磁转矩 | Te=PLm(isqird− isdirq) |
| 功率不变 dq 变换，以确保 dq 功率与三相功率相等 | [vsdvsq]= 23 [cos(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda)−sin(Θda−2π3)−sin(Θda+2π3)][vavbvc]      [iaibic]= 23  [cos(Θda)−sin(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda−2π3)−sin(Θda+2π3)][isdisq] |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ωm* | 转子角速度（rad/s） |
| *ωem* | 转子电角速度（rad/s） |
| *ωslip* | 转子电转差速度（rad/s） |
| *ωsyn* | 同步转子速度（rad/s） |
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
| *va*、*vb*、*vc* | 定子 a、b、c 相电压（V） |
| *ia*、*ib*、*ic* | 定子 a、b、c 相电流（A） |
| *Rs* | 定子绕组电阻（Ohm） |
| *Rr* | 转子绕组电阻（Ohm） |
| *P* | 极对数 |
| *Te* | 电磁转矩（Nm） |

### Mechanical System

电机角速度由下式给出：

ddtωm=1J(Te−Tf−Fωm−Tm)dθmdt=ωm

这些方程使用以下变量。

|  |  |
| --- | --- |
| *J* | 电机与负载的合成惯量（kgm^2） |
| *F* | 电机与负载的合成粘性摩擦（N·m/(rad/s)） |
| *θm* | 电机机械角位置（rad） |
| *Tm* | 电机轴转矩（Nm） |
| *Te* | 电磁转矩（Nm） |
| *Tf* | 电机轴静摩擦转矩（Nm） |
| *ωm* | 电机机械角速度（rad/s） |

### Power Accounting

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrMtr` | 机械功率 | *Pmot* | Pmot= −ωmTe |
| `PwrBus` | 电功率 | *Pbus* | Pbus= vania+ vbnib+vcnic |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损耗 | `PwrElecLoss` | 电阻功率损耗 | *Pelec* | Pelec= −(Rsisd2+Rsisq2+−Rrird2+Rrirq2) |
| `PwrMechLoss` | 机械功率损耗 | *Pmech* | 当 **Port Configuration** 设置为 `Torque` 时：  Pmech= −(ωm2F+ |ωm|Tf)  当 **Port Configuration** 设置为 `Speed` 时：  Pmech= 0 |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrMtrStored` | 存储的电机功率 | *Pstr* | Pstr= Pbus+ Pmot+ Pelec + Pmech |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Rs* | 定子电阻 (Ohm) |
| *Rr* | 转子电阻 (Ohm) |
| *ia*,*ib*,*ic* | 定子 a、b 和 c 相电流 (A) |
| *isq*,*isd* | 定子 q 轴和 d 轴电流 (A) |
| *van*, *vbn*, *vcn* | 定子 a、b 和 c 相电压 (V) |
| *ωm* | 转子机械角速度 (rad/s) |
| *F* | 电机和负载的组合粘性阻尼 (N·m/(rad/s)) |
| *Te* | 电磁转矩 (Nm) |
| *Tf* | 电机和负载的组合摩擦转矩 (Nm) |
