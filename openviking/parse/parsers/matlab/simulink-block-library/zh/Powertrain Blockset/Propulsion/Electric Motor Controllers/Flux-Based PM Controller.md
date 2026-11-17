---
type: simulink-block
title: 'Flux-Based PM Controller'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motor Controllers'
documentation_page: 'fluxbasedpmcontroller'
documentation_source_path: 'ref/fluxbasedpmcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Flux-Based PM Controller

## 端口

### 输入

### **SpdReq** — 转子速度指令 `scalar`

转子速度指令，*ω\*m*，单位为 rad/s。

#### 依赖

要创建此端口，请为 **Control Type** 参数选择 `Speed Control`。

### **TrqCmd** — 转矩指令 `scalar`

转矩指令，*T\**，单位为 N·m。

#### 依赖

要创建此端口，请为 **Control Type** 参数选择 `Torque Control`。

### **BusVolt** — 直流母线电压 `scalar`

直流母线电压，*vbus*，单位为 V。

### **PhaseCurrA** — 电流 `scalar`

定子电流 a 相，*ia*，单位为 A。

### **PhaseCurrB** — 电流 `scalar`

定子电流 b 相，*ib*，单位为 A。

### **SpdFdbk** — 转子速度 `scalar`

转子速度，*ωm*，单位为 rad/s。

### **PosFdbk** — 转子电角度 `scalar`

转子电角度，*Θm*，单位为 rad。

### 输出

### **Info** — 总线信号 bus

包含以下模块计算结果的总线信号。

| 信号 | 描述 | 单位 |
| --- | --- | --- |
| `SrcPwr` | 源功率 | W |
| `LdPwr` | 负载功率 | W |
| `PwrLoss` | 功率损耗 | W |
| `MtrTrqEst` | 估计的电机转矩 | N·m |

### **BusCurr** — 母线电流 `scalar`

估计的直流母线电流，*ibus*，单位为 A。

### **PhaseVolt** — 定子端电压 `array`

定子端电压，*Va*、*Vb* 和 *Vc*，单位为 V。

## 参数

#### 模块选项

### **Control Type** — 选择控制方式 `Torque Control`（默认）| `Speed Control`

如果选择 `Torque Control`，该模块不实现速度控制器。

下表总结了端口配置。

| 端口配置 | 创建的端口 |
| --- | --- |
| `Speed Control` | `SpdReq` |
| `Torque Control` | `TrqCmd` |

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `control_type` |
| **值：** | `Torque Control`（默认）| `Speed Control` |
| **数据类型：** | `character vector` |

#### 电机参数

### **Number of pole pairs, PolePairs** — 极对数 `4`（默认）| `scalar`

电机极对数，*P*。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `PolePairs` |
| **值：** | `4`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Vector of d-axis current breakpoints, id\_index** — 电流 `vector`

*d* 轴电流，*id\_index*，单位为 A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `id_index` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Vector of q-axis current breakpoints, iq\_index** — 电流 `vector`

*q* 轴电流，*iq\_index*，单位为 A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `iq_index` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Corresponding d-axis flux, lambda\_d** — 磁链 `vector`

*d* 轴磁链，*λd*，单位为 Wb。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `lambda_d` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **Corresponding q-axis flux, lambda\_q** — 磁链 `vector`

*q* 轴磁链，*λq*，单位为 Wb。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `lambda_q` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 电流控制器

### **转矩控制的采样时间，Tst** — 时间 `1e-4`（默认）| `scalar`

转矩控制采样时间，*Tst*，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tst` |
| **值：** | `1e-4`（默认）| `scalar` |
| **数据类型：** | `double` |

### **D 轴比例增益，Kp\_d** — 增益 `2.4056`（默认）| `scalar`

*d* 轴比例增益，*Kpd*，单位为 V/A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kp_d` |
| **值：** | `2.4056`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Q 轴比例增益，Kp\_q** — 增益 `2.4056`（默认）| `scalar`

*q* 轴比例增益，*Kpq*，单位为 V/A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kp_q` |
| **值：** | `2.4056`（默认）| `scalar` |
| **数据类型：** | `double` |

### **D 轴积分增益，Ki\_d** — 增益 `192.45`（默认）| `scalar`

*d* 轴积分增益，*Kid*，单位为 V/A·s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ki_d` |
| **值：** | `192.45`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Q 轴积分增益，Ki\_q** — 增益 `192.45`（默认）| `scalar`

*q* 轴积分增益，*Kiq*，单位为 V/A·s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ki_q` |
| **值：** | `192.45`（默认）| `scalar` |
| **数据类型：** | `double` |

### **转速断点向量，wbp** — 断点 `vector`

转速断点，*ωbp*，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `wbp` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **转矩断点向量，tbp** — 断点 `vector`

转矩断点，*Tbp*，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tbp` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **对应的 d 轴电流参考值，id\_ref** — 电流 `vector`

*d* 轴参考电流，*idref*，单位为 A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `id_ref` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **对应的 q 轴电流参考值，iq\_ref** — 电流 `vector`

*q* 轴参考电流，*iqref*，单位为 A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `iq_ref` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 速度控制器

### **速度调节时间常数，Ksf** — 时间 `.1`（默认）| `scalar`

速度调节器时间常数，*Ksf*，单位为 1/s。

#### 依赖关系

要启用此参数，请将 **Control Type** 参数选择为 `Speed Control`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ksf` |
| **值：** | `.1`（默认）| `scalar` |
| **数据类型：** | `double` |

### **比例增益，Kp\_w** — 增益 `0.40475`（默认）| `scalar`

比例增益，*Kpω*，单位为 N·m/(rad/s)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kp_w` |
| **值：** | `0.40475`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Control Type** 参数选择为 `Speed Control`。

### **积分增益，Ki\_w** — 增益 `10.1615`（默认）| `scalar`

积分增益，*Kiω*，单位为 N·m/rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ki_w` |
| **值：** | `10.1615`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Control Type** 参数选择为 `Speed Control`。

### **惯量补偿，Jcomp** — 惯量 `0.0027`（默认）| `scalar`

惯量补偿，单位为 kg·m^2。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jcomp` |
| **值：** | `0.0027`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Control Type** 参数选择为 `Speed Control`。

### **静摩擦，Fs** — 摩擦 `0`（默认）| `scalar`

静摩擦，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fs` |
| **值：** | `0`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Control Type** 参数选择为 `Speed Control`。

### **粘性阻尼补偿，Fv** — Dampint `0.0004924`（默认）| `scalar`

粘性阻尼补偿，单位为 N·m/(rad/s)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fv` |
| **值：** | `0.0004924`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Control Type** 参数选择为 `Speed Control`。

#### 电气损耗

### **Parameterize losses by** — 选择类型 `Single efficiency measurement`（默认）| `Tabulated loss data` | `Tabulated efficiency data`

| 设置 | 模块实现 |
| --- | --- |
| `Single efficiency measurement` | 使用逆变器效率的恒定值计算电气损耗。 |
| `Tabulated loss data` | 根据电机转速和负载转矩的函数关系计算电气损耗。 |
| `Tabulated efficiency data` | 使用逆变器效率（电机转速和负载转矩的函数）计算电气损耗。    - 将您提供的效率值转换为损耗，并使用表格化损耗进行仿真。 - 忽略您为零转速或零转矩提供的效率值。当转矩或转速为零时，损耗假定为零。 - 使用线性插值确定损耗。根据需要为低转速和低转矩提供表格化数据，以在低功率条件下获得所需的精度水平。 - 对于超出表格范围的转速和转矩幅值，不进行损耗值外推。 |

最佳实践是使用 `Tabulated loss data` 而非 `Tabulated efficiency data`：

- 效率在零转速或零转矩时定义不明确。
- 您可以考虑零转速或零转矩时仍然存在的固定损耗。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `param_loss` |
| **值**：| `Single efficiency measurement`（默认）| `Tabulated loss data` | `Tabulated efficiency data` |
| **Data Types:** | `character vector` |

### **Overall inverter efficiency, eff** — 常量 `98`（默认）| `scalar`

整体逆变器效率，*Eff*，以 % 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `eff` |
| **值**：| `98`（默认）| `scalar` |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，对于 **Parameterize losses by**，请选择
`Tabulated loss data`。

### **Vector of speeds (w) for tabulated loss, w\_loss\_bp** — 断点 `[0 200 400 600 800 1000]`（默认）| `1`×`M` 向量

计算损耗时查找表的转速断点，以 rad/s 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `w_loss_bp` |
| **值**：| `[0 200 400 600 800 1000]`（默认）| `1`×`M` 向量 |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，对于 **Parameterize losses by**，请选择
`Tabulated loss data`。

### **Vector of torques (T) for tabulated loss, T\_loss\_bp** — 断点 `[0 25 50 75 100]`（默认）| `1`×`N` 向量

计算损耗时查找表的转矩断点，以 N·m 为单位。

#### 编程使用

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `T_loss_bp` |
| **值**：| `[0 25 50 75 100]`（默认）| `1`×`N` 向量 |
| **Data Types:** | `double` |

#### 依赖关系

要启用此参数，对于 **Parameterize losses by**，请选择
`Tabulated loss data`。

### **Corresponding losses, losses\_table** — 表 `[100 100 100 100 100;100 150 200 250 300;100 200 300 400 500;100 250 400 550 700;100 300 500 700 900;100 350 600 850 1100]`（默认）| `M`×`N` 数组

作为 `M` 个转速和 `N` 个转矩函数的电气损耗值数组，单位为 W。每个值指定特定转速和转矩组合下的损耗。矩阵大小必须与转速和转矩向量定义的维度匹配。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `losses_table` |
| **值：** | `M`×`N` 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Parameterize losses by** 选择 `Tabulated loss data`。

### **Vector of speeds (w) for tabulated efficiency, w\_eff\_bp** — 断点 `[200 400 600 800 1000]`（默认）| `1`×`M` 向量

计算效率时查找表的转速断点，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `w_eff_bp` |
| **值：** | `[200 400 600 800 1000]`（默认）| `1`×`M` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Parameterize losses by** 选择 `Tabulated efficiency data`。

### **Vector of torques (T) for tabulated efficiency, T\_eff\_bp** — 断点 `[25 50 75 100]`（默认）| `1`×`N` 向量

计算效率时查找表的转矩断点，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_eff_bp` |
| **值：** | `[25 50 75 100]`（默认）| `1`×`N` 向量 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Parameterize losses by** 选择 `Tabulated efficiency data`。

### **Corresponding efficiency, efficiency\_table** — 表 `[96.2 98.1 98.7 99;98.1 99 99.4 99.5;98.7 99.4 99.6 99.7;99 99.5 99.7 99.8;99.2 99.6 99.7 99.8]`（默认）| `M`×`N` 数组

作为 `M` 个转速和 `N` 个转矩函数的效率数组，单位为 %。每个值指定特定转速和转矩组合下的效率。矩阵大小必须与转速和转矩向量定义的维度匹配。

模块忽略零转速或零转矩时的效率值。当转矩或转速为零时，损耗为零。模块使用线性插值。

为了在低功率条件下获得所需的精度水平，您可以为低转速和低转矩提供表格数据。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `efficiency_table` |
| **值：** | `M`×`N` 数组 |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Parameterize losses by** 选择 `Tabulated efficiency data`。

## 所属库

Powertrain Blockset / Propulsion / Electric Motor Controllers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

基于磁链的永磁同步电机控制器

Flux Based PM Controller 模块为内置式永磁同步电机 (PMSM) 实现了一个基于磁链的磁场定向控制器，并可选配外环速度控制器。内部转矩控制实现了最大转矩每安培 (MTPA) 和磁链弱磁策略。您可以指定速度或转矩控制类型。

Flux Based PM Controller 实现了速度控制、转矩确定、调节器、变换和电机的方程。

下图展示了该模块中的信息流。

展示速度控制、转矩确定、调节器、变换和电机信息流的示意图。

该模块使用以下变量实现方程。

|  |  |
| --- | --- |
| *ω* | 转子速度 |
| *ω\** | 转子速度指令 |
| *T\** | 转矩指令 |
| *id*  *i\*d* | *d* 轴电流  *d* 轴电流指令 |
| *iq*  *i\*q* | *q* 轴电流  *q* 轴电流指令 |
| *vd*,  *v\*d* | *d* 轴电压  *d* 轴电压指令 |
| *vq*  *v\*q* | *q* 轴电压  *q* 轴电压指令 |
| *va*, *vb*, *vc* | 定子 a、b、c 相电压 |
| *ia*, *ib*, *ic* | 定子 a、b、c 相电流 |

### Speed Controller

要实现速度控制器，请选择 **Control Type** 参数 `Speed Control`。如果选择 **Control Type** 参数 `Torque Control`，则该模块不实现速度控制器。

速度控制器通过实现状态滤波器，并计算前馈和反馈指令来确定转矩指令。如果不实现速度控制器，则向 Flux Based PM Controller 模块输入转矩指令。

示意图显示状态滤波器通过加速度和速度信号连接到指令前馈模块。状态滤波器还通过速度信号连接到状态反馈。

**状态滤波器**

状态滤波器是一种低通滤波器，它根据速度指令生成加速度指令。其特征方程的离散形式为：

z+KsfTsm−1

该滤波器使用此方程计算增益。

Ksf=1−exp(−Tsm2πEVsf)Tsm

这些方程使用以下变量。

|  |  |
| --- | --- |
| *EVsf* | 速度指令滤波器带宽 |
| *Tsm* | 运动控制器采样时间 |
| *Ksf* | 速度调节器时间常数 |

**状态反馈**

为了生成状态反馈转矩，该模块使用来自状态滤波器的滤波后速度误差信号。为了对速度进行滤波，该模块使用比例积分（PI）控制器。

Tcmd=Kpω(ωm\*−ωm)+KiωzTsmz−1(ωm\*−ωm)

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ωm* | 转子速度 |
| *ω\*m* | 转子速度指令 |
| *Tcmd* | 转矩指令 |
| *Kpω* | 速度调节器比例增益 |
| *Kiω* | 速度调节器积分增益 |
| *Tsm* | 速度调节器采样率 |

**指令前馈**

为了生成状态前馈转矩，该模块使用来自状态滤波器的滤波后速度和加速度。此外，前馈转矩计算使用惯量、粘性阻尼和静摩擦。为了实现零跟踪误差，转矩指令是前馈和反馈转矩指令之和。

前馈转矩指令使用此方程。

Tcmd\_ff= Jpω˙m+Fvωm+Fs ωm|ωm|

其中：

|  |  |
| --- | --- |
| *Jp* | 转子惯量 |
| *Tcmd\_ff* | 转矩指令前馈 |
| *Fs* | 静摩擦转矩常数 |
| *F*v** | 粘性摩擦转矩常数 |
| *Fs* | 静摩擦转矩常数 |
| *ωm* | 转子速度 |

**电流指令**

该模块使用查找表来确定 *d* 轴和 *q* 轴电流指令。这些查找表是机械速度和转矩的函数。为了确定查找表，您可以使用外部有限元分析（FEA）模型或测功机测试结果。

idref=f(|ωm|,|Tref|)iqref=sign(Tref)∗f(|ωm|,|Tref|)

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ωm* | 转子速度 |
| *Tref* | 转矩指令 |
| *idref*, *iqref* | 分别为 *d* 轴和 *q* 轴参考电流 |

**电压指令**

该模块使用这些方程来计算电机参考坐标系中的电压。

vd=dψddt+Rsid−ωeψqvq=dψqdt+Rsiq+ωeψd

dψddt+Rsid=Kpd(id\*−id)+KidzTstz−1(id\*−id)dψqdt+Rsiq=Kpq(iq\*−iq)+KiqzTstz−1(iq\*−iq)vd=Kpi(id\*−id)+KidzTstz−1(id\*−id)+ωeψqvq=Kpi(iq\*−iq)+KiqzTstz−1(iq\*−iq)−ωeψdψq=f(id,iq)ψd=f(id,iq)

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ωm* | 转子机械速度 |
| *ωe* | 转子电速度 |
| *Rs*, *Rr* | 分别为定子和转子绕组的电阻 |
| *iq*, *id* | 分别为 *q* 轴和 *d* 轴电流 |
| *vq*, *vd* | 分别为 *q* 轴和 *d* 轴电压 |
| *Ψq*, *Ψd* | 分别为 *q* 轴和 *d* 轴磁通 |
| *Tst* | 电流调节器采样率 |
| *Kid*, *Kiq* | 分别为 *d* 轴和 *q* 轴积分增益 |
| *Kpd*, *Kpq* | 分别为 *d* 轴和 *q* 轴比例增益 |

### 变换

为了计算平衡三相（*a*、*b*）量、正交两相（*α*、*β*）量以及旋转（*d*、*q*）参考坐标系中的电压和电流，该模块使用 Clarke 变换和 Park 变换。

在变换方程中。

ωe=Pωmdθedt= ωe

| 变换 | 描述 | 方程 |
| --- | --- | --- |
| Clarke | 将平衡三相量（*a*、*b*）转换为平衡两相正交量（*α*、*β*）。 | xα= 23xa− 13xb −13xcxβ= 32xb− 32xc |
| Park | 将平衡两相正交静止量（*α*、*β*）转换为正交旋转参考坐标系（*d*、*q*）。 | xd= xαcosθe+ xβsinθexq= −xαsinθe+ xβcosθe |
| 逆 Clarke | 将平衡两相正交量（*α*、*β*）转换为平衡三相量（*a*、*b*）。 | xa= xaxb= −12xα+ 32xβxc= −12xα− 32xβ |
| 逆 Park | 将正交旋转参考坐标系（*d*、*q*）转换为平衡两相正交静止量（*α*、*β*）。 | xα= xdcosθe− xqsinθexβ= xdsinθe+ xqcosθe |

这些变换使用以下变量。

|  |  |
| --- | --- |
| *ωm* | 转子速度 |
| *P* | 转子极对数 |
| *ωe* | 转子电速度 |
| *Θe* | 转子电角度 |
| *x* | 相电流或电压 |

### 电机

该模块使用相电流和相电压来估算直流母线电流。正电流表示电池放电。负电流表示电池充电。

该模块使用以下方程。

|  |  |
| --- | --- |
| 负载功率 | LdPwr=va ia+ vb ib+ vc ic |
| 源功率 | SrcPwr= LdPwr+PwrLoss |
| 直流母线电流 | ibus= SrcPwrvbus |
| 估算的转子转矩 | Te=1.5P[ψdiq−ψqid] |
| 单一效率源到负载的功率损耗 | PwrLoss=100−EffEff⋅LdPwr |
| 单一效率负载到源的功率损耗 | PwrLoss=100−Eff100⋅\|LdPwr\| |
| 表格化效率的功率损耗 | PwrLoss= f(ωm,MtrTrqest) |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *va*、*vb*、*vc* | 定子 a、b、c 相电压 |
| *vbus* | 估算的直流母线电压 |
| *ia*、*ib*、*ic* | 定子 a、b、c 相电流 |
| *ibus* | 估算的直流母线电流 |
| *Eff* | 逆变器总效率 |
| *ωm* | 转子机械速度 |
| *Lq*、*Ld* | 分别为 *q* 轴和 *d* 轴绕组电感 |
| *Ψq*、*Ψd* | 分别为 *q* 轴和 *d* 轴磁通 |
| *iq*、*id* | 分别为 *q* 轴和 *d* 轴电流 |
| *λ* | 永磁体磁链 |
| *P* | 转子极对数 |

### 电气损耗

要指定电气损耗，请在 **Electrical Losses** 选项卡中，对于 **Parameterize losses by**，选择以下选项之一。

| 设置 | 模块实现 |
| --- | --- |
| `Single efficiency measurement` | 使用逆变器效率的恒定值计算电气损耗。 |
| `Tabulated loss data` | 将电气损耗计算为电机速度和负载转矩的函数。 |
| `Tabulated efficiency data` | 使用作为电机速度和负载转矩函数的逆变器效率计算电气损耗。    - 将您提供的效率值转换为损耗，并在仿真中使用表格化损耗。 - 忽略您为零速度或零转矩提供的效率值。当转矩或速度为零时，假定损耗为零。 - 使用线性插值确定损耗。根据需要为低速度和低转矩提供表格化数据，以获得较低功率条件下所需的精度水平。 - 对于超出表格范围的速度和转矩幅值，不外推损耗值。 |

作为最佳实践，请使用 `Tabulated loss data` 而不是 `Tabulated efficiency data`：

- 在零速度或零转矩时，效率变得定义不明确。
- 您可以考虑在零速度或零转矩时仍然存在的固定损耗。
