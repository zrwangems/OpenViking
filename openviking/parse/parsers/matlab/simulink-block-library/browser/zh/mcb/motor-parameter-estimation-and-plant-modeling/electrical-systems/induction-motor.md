---
type: simulink-block
title: 'Induction Motor'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Motor Parameter Estimation and Plant Modeling / Electrical Systems'
documentation_page: 'inductionmotor'
documentation_source_path: 'ref/inductionmotor.html'
language: zh-CN
chinese_source: official
---

# Induction Motor

## 端口

### 输入

### **LdTrq** — 电机上的负载转矩 `scalar`

电机轴上的负载转矩 *Tm*，以 N·m 为单位。

#### 依赖关系

要创建此端口，请为**端口配置**参数选择**转矩**。

### **Spd** — 转子轴转速 `scalar`

转子的角速度 *ωm*，以弧度/秒为单位。

#### 依赖关系

要创建此端口，请为**端口配置**参数选择**转速**。

### **PhaseVolt** — 定子端电压 `1`×`3` 数组

定子端电压 *Va*、*Vb* 和 *Vc*，以 V 为单位。
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

### **PhaseCurr** — a、b、c 相电流 `1`×`3` 数组

a、b、c 相电流 *ia*、*ib* 和 *ic*，以 A 为单位。

### **MtrTrq** — 电机转矩 `scalar`

电机转矩 *Tmtr*，以 N·m 为单位。

#### 依赖关系

要创建此端口，请为**端口配置**参数选择**转速**。

### **MtrSpd** — 电机转速 `scalar`

电机的角速度 *ωmtr*，以弧度/秒为单位。

#### 依赖关系

要创建此端口，请为**端口配置**参数选择**转矩**。

## 参数

#### 模块选项

### **仿真类型** — 选择仿真类型 **连续** (默认) | **离散**

默认情况下，模块在仿真期间使用连续采样时间。如果要为单精度目标生成代码，请考虑将该参数设置为**离散**。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获得模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `sim_type` |
| **值:** | **Continuous** (默认) | **Discrete** |
| **数据类型:** | `character vector` |

#### 依赖关系

将**仿真类型**设置为**离散**会创建**采样时间 Ts** 参数。

### **采样时间 Ts** — 离散积分的采样时间 `0.001` (默认) | `scalar`

离散仿真的积分采样时间，以秒为单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获得模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Ts` |
| **值:** | `0.001` (默认) | `scalar` |
| **数据类型:** | `double` |

#### 依赖关系

将**仿真类型**设置为**离散**会创建**采样时间 Ts** 参数。

### **端口配置** — 选择端口配置 **转矩** (默认) | **转速**

下表总结了端口配置。

| 端口配置 | 创建输入端口 | 创建输出端口 |
| --- | --- | --- |
| **转矩** | `LdTrq` | `MtrSpd` |
| **转速** | `Spd` | `MtrTrq` |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获得模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `port_config` |
| **值:** | **Torque** (默认) | **Speed** |
| **数据类型:** | `character vector` |

#### 加载参数值

### **文件** — 电机参数 .m 或 .mat 文件的路径 `scalar`

输入您使用 Motor Control Blockset™ 参数估计工具保存的电机参数 .m 或 .mat 文件的路径。您也可以点击**浏览**按钮导航并选择 .m 或 .mat 文件，并用文件名和路径更新**文件**参数。有关电机参数估计过程的详细信息，请参阅Estimate PMSM Parameters Using Parameter Estimation Blocks。

- **从文件加载** - 点击此按钮以从 .m 或 .mat 文件（由**文件**参数指示）读取估计的电机参数并将其加载到电机模块。
- **保存到文件** - 点击此按钮以从电机模块读取电机参数并将其保存到 .m 或 .mat 文件（使用您在**文件**参数中指定的文件名和位置）。

**注意**

在您点击**保存到文件** 按钮之前，请确保**文件**参数中的目标文件名具有 .m 或 .mat 扩展名。如果使用任何其他文件扩展名，模块将显示一条错误消息。

#### 参数

### **极对数，P** — 极对 `2` (默认) | `scalar`

电机极对 *P*。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获得模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `P` |
| **值:** | `2` (默认) | `scalar` |
| **数据类型:** | `double` |

### **定子电阻和泄漏电感，Zs** — 电阻和电感 `[1.77 0.0139]` (默认) | `vector`

定子电阻 *RS*，以 ohm 为单位，泄漏电感 *Lls*，以 H 为单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获得模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Zs` |
| **值:** | `[1.77 0.0139]` (默认) | `vector` |
| **数据类型:** | `double` |

### **转子电阻和泄漏电感，Zr** — 电阻和电感 `[1.34 0.0121]` (默认) | `vector`

转子电阻 *Rr*，以 ohm 为单位，泄漏电感 *Llr*，以 H 为单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获得模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Zr` |
| **值:** | `[1.34 0.0121]` (默认) | `vector` |
| **数据类型:** | `double` |

### **磁化电感，Lm** — 电感 `0.3687` (默认) | `scalar`

磁化电感 *Lm*，以 H 为单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获得模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Lm` |
| **值:** | `0.3687` (默认) | `scalar` |
| **数据类型:** | `double` |

### **物理惯量、粘性阻尼、静态摩擦、机械** — 惯量、阻尼、摩擦 `[0.001 0 0]` (默认) | `vector`

转子的机械属性：

- 惯量 *J*，以 kg·m^2 为单位
- 粘性阻尼 *F*，以 N·m/（弧度/秒）为单位
- 静态摩擦 *Tf*，以 N·m 为单位

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获得模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `mechanical` |
| **值:** | `[0.001 0 0]` (默认) | `vector` |
| **数据类型:** | `double` |

#### 依赖关系

要启用此参数，请为**端口配置**选择**转矩**。

#### 初始值

### **初始机械位置，theta\_init** — 角位置 `0` (默认) | `scalar`

初始转子角位置 *θm0*，以弧度为单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获得模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `theta_init` |
| **值:** | `0` (默认) | `scalar` |
| **数据类型:** | `double` |

### **初始机械转速，omega\_init** — 角速度 `0` (默认) | `scalar`

转子的初始角速度 *ωm0*，以弧度/秒为单位。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获得模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `omega_init` |
| **值:** | `0` (默认) | `scalar` |
| **数据类型:** | `double` |

#### 依赖关系

要启用此参数，请为**端口配置**选择**转矩**。

## 所属库

Powertrain Blockset / Propulsion / Electric Motors and Inverters Motor Control Blockset / Electrical Systems / Motors

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

## 描述

三相感应电机

Induction Motor 模块实现三相感应电机。该模块使用三相输入电压来调节各相电流，从而控制电机转矩或转速。

**注意**

该模块的参数使用星形等效感应电机的每相值。

默认情况下，该模块将**仿真类型**参数设置为**连续**以便在仿真期间使用连续采样时间。如果要为定步长双精度和单精度目标生成代码，请考虑将参数设置为**离散**。然后指定**采样时间 Ts** 参数。

### 三相正弦模型电气系统

该模块实现在静止转子参考 (dq) 系中表示的方程。d 轴与 a 轴对齐。转子参考系中的所有量都是相对于定子来描述的。

Three-phase induction motor currents and magnetic fields

该模块使用以下方程来计算电角速度 (*ωem*) 和转差速度 (*ωslip*)。

ωem=Pωmωslip= ωsyn−ωem

为了计算相对于转子 A 轴 (*dA*) 的 dq 转子电角速度，该模块使用定子 A 轴 (*da*) 转速和转差速度之间的差值：

ωdA= ωda− ωem

为了简化磁通、电压和电流变换的方程，该模块使用转子 A 轴参考系：

ωda=ωemωdA=0

| 计算 | 方程 |
| --- | --- |
| 磁通 | ddt[λsdλsq]= [vsdvsq]− Rs[isdisq]− ωda[0−110][λsdλsq]ddt[λrdλrq]= [vrdvrq]− Rr[irdirq]− ωdA[0−110][λrdλrq]      [λsdλsqλrdλrq]= [Ls00LsLm00LmLm00LmLr00Lr][isdisqirdirq] |
| 电流 | [isdisqirdirq]= (1Lm2− LrLs)[−Lr00−LrLm00LmLm00Lm−Ls00−Ls][λsdλsqλrdλrq] |
| 电感 | Ls= Lls+LmLr= Llr+Lm |
| 电磁转矩 | Te=PLm(isqird− isdirq) |
| 功率不变的 dq 变换，以确保 dq 和三相功率相等 | [vsdvsq]= 23 [cos(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda)−sin(Θda−2π3)−sin(Θda+2π3)][vavbvc]      [iaibic]= 23  [cos(Θda)−sin(Θda)cos(Θda−2π3)cos(Θda+2π3)−sin(Θda−2π3)−sin(Θda+2π3)][isdisq] |

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

对于功率计算，该模块实现下列方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` - 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrMtr` | 机械功率 | *Pmot* | Pmot= −ωmTe |
| `PwrBus` | 电功率 | *Pbus* | Pbus= vania+ vbnib+vcnic |
| `PwrNotTrnsfrd` - 功率越过模块边界，但未传输  - 正信号表示输入 - 负信号表示损失 | `PwrElecLoss` | 电阻功率损失 | *Pelec* | Pelec= −(Rsisd2+Rsisq2+−Rrird2+Rrirq2) |
| `PwrMechLoss` | 机械功率损失 | *Pmech* | 当**端口配置**设置为**转矩**时：  Pmech= −(ωm2F+ |ωm|Tf)  当**端口配置**设置为**转速**时：  Pmech= 0 |
| `PwrStored` - 储存的能量变化率  - 正信号表示增加 - 负信号表示减少 | `PwrMtrStored` | 储存的电机功率 | *Pstr* | Pstr= Pbus+ Pmot+ Pelec + Pmech |

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
