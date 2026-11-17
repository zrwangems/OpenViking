---
type: simulink-block
title: 'BLDC'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Electrical Systems / Motors'
documentation_page: 'bldc'
documentation_source_path: 'ref/bldc.html'
language: zh-CN
chinese_source: worker-translation
---

# BLDC

## 端口

### 输入

### **LdTrq** — 电机上的负载转矩 `标量`

电机轴上的负载转矩，*Tm*，单位为 N·m。

#### 依赖

要启用此端口，请将 **Mechanical input configuration** 参数设置为 `Torque`。

### **Spd** — 电机轴转速 `标量`

电机的角速度，*ωm*，单位为 rad/s。

#### 依赖

要启用此端口，请将 **Mechanical input configuration** 参数设置为 `Speed`。

### **PhaseVolt** — 定子端电压 `1`×`3` 数组

定子端电压，*Va*、*Vb* 和 *Vc*，单位为 V。

### 输出

### **Info** — 总线信号 总线

该总线信号包含以下模块计算量。

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

a、b、c 相电流，*ia*、*ib* 和 *ic*，单位为 A。

### **MtrTrq** — 电机转矩 标量

电机转矩，*Tmtr*，单位为 N·m。

#### 依赖

要启用此端口，请将 **Mechanical input configuration** 参数设置为 `Speed`。

### **MtrSpd** — 电机转速 标量

电机的角速度，*ωmtr*，单位为 rad/s。

#### 依赖

要启用此端口，请将 **Mechanical input configuration** 参数设置为 `Torque`。

## 参数

### 模块选项

### **Mechanical input configuration** — 选择端口配置 `Torque`（默认）| `Speed`

下表总结了端口配置。

| 端口配置 | 创建输入端口 | 创建输出端口 |
| --- | --- | --- |
| `Torque` | `LdTrq` | `MtrSpd` |
| `Speed` | `Spd` | `MtrTrq` |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `port_config` |
| **值：** | `Torque`（默认）| `Speed` |
| **数据类型：** | `character vector` |

### **Simulation type** — 选择仿真类型 `Continuous`（默认）| `Discrete`

默认情况下，该模块在仿真期间使用连续采样时间。如果要为单精度目标生成代码，请将该参数设置为 `Discrete`。

### **Sample time (s)** — 离散积分采样时间 `25e-6`（默认）| `标量`

离散仿真的积分采样时间，单位为 s。

#### 依赖

要启用此参数，请将 **Simulation type** 设置为 `Discrete`。

### 参数

### **Number of pole pairs** — 电机极对数 `4`（默认）| `标量`

电机极对数，*P*。

### **Stator resistance per phase (Ohm)** — 每相定子电阻 `0.36`（默认）| `标量`

每相定子电阻，*Rs*，单位为欧姆。

### **Stator d-axis inductance (H)** — d 轴定子电感 `2e-4`（默认）| `标量`

*d* 轴定子电感，*Ld*，单位为 H。

### **Stator q-axis inductance (H)** — q 轴定子电感 `2e-4`（默认）| `标量`

*q* 轴定子电感，*Lq*，单位为 H。

### **Permanent flux linkage constant (Wb)** — 磁链常数 `0.0064`（默认）| `标量`

永磁磁链常数，*λpm*，单位为 Wb。

### **Inertia (kgm^2)** — 转子惯量 `7.0616e-06`（默认）| `标量`

转子惯量，*J*，单位为 kg.m^2。

### **Viscous damping (Nm/rad/s)** — 粘性阻尼 `2.6369e-06`（默认）| `标量`

粘性阻尼，*F*，单位为 N·m/(rad/s)。

### **Static friction (Nm)** — 静摩擦 `0`（默认）| `scalar`

静摩擦，*Tf*，单位为 N·m。

### Initial Values

### **Initial d-axis current (A)** — *d'* 轴初始电流 `0`（默认）| `scalar`

初始 d 轴电流，*id'*，单位为 A。

### **Initial q-axis current (A)** — *q'* 轴初始电流 `0`（默认）| `scalar`

初始 q 轴电流，*iq'*，单位为 A。

### **Initial rotor mechanical position (rad)** — 转子初始机械位置 `0`（默认）| `scalar`

电机初始角位置，*θm0*，单位为 rad。

### **Initial rotor mechanical speed (rad/s)** — 转子初始机械速度 `0`（默认）| `scalar`

电机初始角速度，*ωm0*，单位为 rad/s。

#### 依赖关系

要启用此参数，请将 **Mechanical input configuration** 设置为 `Torque`。

## 所属库

Motor Control Blockset / Electrical Systems / Motors

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

具有梯形磁通分布的三相无刷直流电机

BLDC 模块实现了一个三相无刷直流（BLDC）电机，其梯形反电动势在 120 电角度位置范围内保持恒定。该模块使用三相输入电压来调节各相电流，从而允许控制电机转矩或速度。

默认情况下，该模块将 **Simulation type** 参数设置为 `Continuous`，以在仿真期间使用连续采样时间。如果要将该模块用于固定步长仿真，请将该参数设置为 `Discrete`。然后指定 **Sample time (s)** 参数。

### Motor Construction

此图显示了一个单极对电机。

由于永磁体产生的电机磁场随电机角度形成梯形磁通变化率。

对于坐标轴约定，当电机角度 *θr* 为零时，*a* 相磁通与永磁体磁通对齐。

### Three-Phase Sinusoidal Model Electrical System

该模块不使用标准 *dq* 参考坐标系，而是使用 *d’q’* 参考坐标系，其由以下变换方程定义。

vd'=23((va−Ria−Ea)cosθe+(vb−Rib−Eb)cos(θe−2π3)+(vc−Ric−Ec)cos(θe+2π3))

vq'=−2π3((va−Ria−Ea)sinθe+(vb−Rib−Eb)sin(θe−2π3)+(vc−Ric−Ec)sin(θe+2π3))

Ea=Pωm∂ψa∂θeEb=Pωm∂ψb∂θeEc=Pωm∂ψc∂θe

ia=id'cosθe−iq'sinθeib=id'cos(θe−2π3)−iq'sin(θe−2π3)ic=id'cos(θe+2π3)−iq'sin(θe+2π3)

该模块实现了这些方程，并以 BLDC 电机的 *dq* 和 *d’q’* 参考坐标系表示。电机参考坐标系中的所有量均相对于定子 A 相。

ωe=Pωmddtid'=1Ldvd'+LqLdPωmiq'

ddtiq'=1Lqvq'−LdLqPωmid'

Te=1.5P((Ld−Lq)id'iq')+P(∂ψa∂θeia+∂ψb∂θeib+∂ψc∂θeic)

此表描述了这些方程中使用的变量。

|  |  |
| --- | --- |
| *Lq*，*Ld* | q 轴和 d 轴电感（H） |
| *R* | 定子绕组电阻（ohm） |
| *iq'*，*id'* | *q'* 轴和 *d'* 轴电流（A） |
| *vq'*，*vd'* | *q'* 轴和 *d'* 轴电压（V） |
| *ωm* | 电机的角机械速度（rad/s） |
| *ωe* | 电机的角电速度（rad/s） |
| *P* | 极对数 |
| *Te* | 电磁转矩（Nm） |
| *Θe* | 电角度（rad） |
| *Va*，*Vb*，*Vc* | 定子 A、B 和 C 相电压（V） |
| *ia*，*ib*，*ic* | 定子 A、B 和 C 相电流（A） |
| *Ea*，*Eb*，*Ec* | 定子 A、B 和 C 相的反电动势（V/m/s） |
| *Ψa*，*Ψb*，*Ψc* | 连接每个定子绕组的总磁通（Wb） |

### Mechanical System

电机角速度由下式给出：

ddtωm=1J(Te−Tf−Fωm−Tm)dθmdt=ωm

这些方程使用以下变量。

|  |  |
| --- | --- |
| *J* | 电机与负载的合成惯量 (kgm^2) |
| *F* | 电机与负载的合成粘性摩擦 (N·m/(rad/s)) |
| *θm* | 电机机械角位置 (rad) |
| *Tm* | 电机轴转矩 (Nm) |
| *Te* | 电磁转矩 (Nm) |
| *Tf* | 电机轴静摩擦转矩 (Nm) |
| *ωm* | 电机的角机械速度 (rad/s) |

### Amplitude Invariant *dq* Transformation

该模块使用这些方程来实现幅值不变 *dq*
变换，以确保 *dq* 与三相幅值相等。

[vsdvsq]= 23 [cos(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda)−sin(Θda−2π3)−sin(Θda+2π3)][vavbvc]

[iaibic]=   [cos(Θda)−sin(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda−2π3)−sin(Θda+2π3)][isdisq]

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Θda* | 相对于转子 *a* 轴的 *dq* 定子电角度 (rad) |
| *vsq*, *vsd* | 定子 *q* 轴和 *d* 轴电压 (V) |
| *isq*,*isd* | 定子 *q* 轴和 *d* 轴电流 (A) |
| *va*,*vb*,*vc* | 定子电压相 *a*、*b*、*c* (V) |
| *ia*, *ib*, *ic* | 定子电流相 *a*、*b*、*c* (A) |

### Trapezoidal Rate of Change of Flux

由于永磁体产生的转子磁场会随转子角度产生梯形磁通变化率。该图展示了三相 BLDC 电机三相的磁通变化率。
