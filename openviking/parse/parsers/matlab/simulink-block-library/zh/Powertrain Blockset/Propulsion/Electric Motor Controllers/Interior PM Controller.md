---
type: simulink-block
title: 'Interior PM Controller'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motor Controllers'
documentation_page: 'interiorpmcontroller'
documentation_source_path: 'ref/interiorpmcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Interior PM Controller

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

### **Control Type** — 选择控制方式 `Speed Control`（默认）| `Torque Control`

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
| **值：** | `Speed Control`（默认）| `Torque Control` |
| **数据类型：** | `character vector` |

#### 电机参数

### **Stator resistance, Rs** — 电阻 `0.02`（默认）| `scalar`

定子相绕组电阻，*Rs*，单位为 ohm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rs` |
| **值：** | `0.02`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖

下表总结了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Stator resistance, Rs** | **D and Q axis integral gain, Ki** | **Current Controller** |

### **D-axis inductance, Ld** — 电感 `1.7e-3`（默认）| `scalar`

D 轴绕组电感，*Ld*，单位为 H。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ld` |
| **值：** | `1.7e-3`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖

下表总结了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D 轴电感，Ld** | **转矩断点，T\_mtpa**  **D 轴表数据，id\_mtpa**  **Q 轴表数据，iq\_mtpa**  **D、q 和最大电流限值，idq\_limits** | **Id 和 Iq 计算** |

### **Q-axis inductance, Lq** — 电感 `3.2e-3`（默认）| `scalar`

Q 轴绕组电感，*Lq*，单位为 H。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lq` |
| **值：** | `3.2e-3`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Q轴电感，Lq** | **转矩断点，T\_mtpa**  **D轴表数据，id\_mtpa**  **Q轴表数据，iq\_mtpa**  **D、Q及最大电流限值，idq\_limits** | **Id和Iq计算** |

### **永磁体磁链，lambda\_pm** — 磁链 `0.2205`（默认）| `scalar`

永磁体磁链，*λpm*，单位为Wb。

#### 程序化使用

要以程序化方式设置模块参数值，请使用`set_param`函数。

要以程序化方式获取模块参数值，请使用`get_param`函数。

|  |  |
| --- | --- |
| **参数：** | `lambda_pm` |
| **值：** | `0.2205`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **永磁体磁链，lambda\_pm** | **转矩断点，T\_mtpa**  **D轴表数据，id\_mtpa**  **Q轴表数据，iq\_mtpa**  **D、Q及最大电流限值，idq\_limits** | **Id和Iq计算** |

### **极对数，PolePairs** — 极数 `4`（默认）| `scalar`

电机极对数，*P*。

#### 程序化使用

要以程序化方式设置模块参数值，请使用`set_param`函数。

要以程序化方式获取模块参数值，请使用`get_param`函数。

|  |  |
| --- | --- |
| **参数：** | `PolePairs` |
| **值：** | `4`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **极对数，PolePairs** | **转矩断点，T\_mtpa**  **D轴表数据，id\_mtpa**  **Q轴表数据，iq\_mtpa**  **D、Q及最大电流限值，idq\_limits** | **Id和Iq计算** |

### **物理惯量、粘性阻尼、静摩擦，Mechanical** — 惯量、阻尼、摩擦 `[0.0027, 4.924e-4, 0]`（默认）| `vector`

电机的机械特性：

- 电机惯量，*F*v**，单位为kgm^2
- 粘性摩擦转矩常数，*F*v**，单位为N·m/(rad/s)
- 静摩擦转矩常数，*Fs*，单位为N·m

#### 程序化使用

要以程序化方式设置模块参数值，请使用`set_param`函数。

要以程序化方式获取模块参数值，请使用`get_param`函数。

|  |  |
| --- | --- |
| **参数：** | `Mechanical` |
| **值：** | `[0.0027, 4.924e-4, 0]`（默认）| `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将**Control Type**参数设置为`Speed Control`。

对于增益计算，模块使用**Motor Parameters**选项卡上**Physical inertia, viscous damping, static friction**参数值中的惯量。

下表汇总了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **物理惯量、粘性阻尼、静摩擦，Mechanical** | **比例增益，ba**  **角度增益，Ksa**  **旋转增益，Kisa**  **惯量补偿，Jcomp**  **粘性阻尼补偿，Fv**  **静摩擦，Fs** | **速度控制器** |

#### Id和Iq计算

### **电机约束** — 电机约束 `Maximum Torque`（默认）| `Maximum Current`

MTPA控制的电机约束。

#### 程序化使用

要以程序化方式设置模块参数值，请使用`set_param`函数。

要以程序化方式获取模块参数值，请使用`get_param`函数。

|  |  |
| --- | --- |
| **参数：** | `MotorConstraint` |
| **值：** | `Maximum Torque`（默认）| `Maximum Current` |
| **数据类型：** | `character vector` |

### **最大电流，I\_max** — 电流 `44`（默认）| `scalar`

最大电流，单位为A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `I_max` |
| **值：** | `44`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Motor constraint** 设置为 `Maximum Current`。

下表总结了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **最大转矩，T\_max** | **转矩断点，T\_mtpa**  **D 轴表数据，id\_mtpa**  **Q 轴表数据，iq\_mtpa**  **D、Q 和最大电流限值，idq\_limits** | **Id 和 Iq 计算** |

### **Maximum torque, T\_max** — 转矩 `60`（默认） | `scalar`

最大转矩，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_max` |
| **值：** | `60`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请将 **Motor constraint** 设置为 `Maximum Torque`。

下表总结了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **最大转矩，T\_max** | **转矩断点，T\_mtpa**  **D 轴表数据，id\_mtpa**  **Q 轴表数据，iq\_mtpa**  **D、Q 和最大电流限值，idq\_limits** | **Id 和 Iq 计算** |

### **MTPA table breakpoints, bp** — 断点数量 `10`（默认） | `scalar`

推导出的最大转矩每安培 MTPA 表断点数量。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bp` |
| **值：** | `10`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表总结了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **MTPA 表断点，pb** | **转矩断点，T\_mtpa**  **D 轴表数据，id\_mtpa**  **Q 轴表数据，iq\_mtpa**  **D、Q 和最大电流限值，idq\_limits** | **Id 和 Iq 计算** |

### **Calculate MTPA Table Data** — 推导参数按钮

点击以推导参数。

#### 依赖关系

在 **Id and Iq Calculation** 选项卡上，当您选择 **Calculate MPTA Table data** 时，模块会计算推导参数。该表总结了推导参数对其他模块参数的依赖关系。

| **Id and Iq Calculation** 选项卡上的推导参数 | | 依赖于 | |
| --- | --- | --- | --- |
| 参数 | 选项卡 |
| **转矩断点，T\_mtpa** | Tmtpa= 32P(λpmiq+(Ld− Lq)idiq) | **最大转矩，T\_max**  **MTPA 表断点，pb** | **Id 和 Iq 计算** |
| **D 轴表数据，id\_mtpa** | Im=2Tmax3Pλpmid\_mtpa=λpm4(Lq−Ld)−λpm216(Lq−Ld)2+Im22 | **永磁体磁链，lambda\_pm**  **D 轴电感，Ld**  **Q 轴电感，Lq**  **极对数，PolePairs** | **电机参数** |
| **Q 轴表数据，iq\_mtpa** | iq\_mtpa=Im2−(imtpa)2 |
| **D, Q, and max current limits, idq\_limits** |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *imax* | 最大相电流 |
| *id* | d 轴电流 |
| *iq* | q 轴电流 |
| *id\_max* | 最大 d 轴相电流 |
| *iq\_max* | 最大 q 轴相电流 |
| *id\_mtpa* | d 轴相电流 MTPA 表 |
| *iq\_mtpa* | q 轴相电流 MTPA 表 |
| *λpm* | 永磁体磁链 |
| *Ld* | d 轴绕组电感 |
| *Lq* | q 轴绕组电感 |
| *P* | 电机极对数 |
| *Tmtpa* | 转矩 MTPA 断点 |
| *Im* | 估计最大电流 |

### **Torque Breakpoints, T\_mtpa** — 派生 `[0 6.41323967543524 12.8472271930531 19.3221671098192 25.8572437875407 32.4702594835269 39.177408529382 45.9931820911486 52.930379967864 60.0001984561834]`（默认）| `vector`

派生的转矩断点，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `T_mtpa` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **转矩断点，T\_mtpa** | **最大转矩，T\_max**  **MTPA 表断点，pb** | **Id 和 Iq 计算** |
| **Permanent magnet flux, lambda\_pm**  **D-axis inductance, Ld**  **Q-axis inductance, Lq**  **Number of pole pairs, PolePairs** | **Motor Parameters** |

### **D-axis table data, id\_mtpa** — 派生 `[0 -0.159333276810563 -0.633258709677809 -1.41005695027301 -2.47173666500257 -3.79592548539108 -5.35786489234899 -7.13217478652462 -9.09420364751938 -11.2209236729158]`（默认）| `vector`

派生的 d 轴表数据，单位为 A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `id_mtpa` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D 轴表数据，id\_mtpa** | **最大转矩，T\_max**  **MTPA 表断点，pb** | **Id 和 Iq 计算** |
| **Permanent magnet flux, lambda\_pm**  **D-axis inductance, Ld**  **Q-axis inductance, Lq**  **Number of pole pairs, PolePairs** | **Motor Parameters** |

### **Q-axis table data, iq\_mtpa** — 派生 `[0 4.84224935172196 9.66902512748937 14.4660510262181 19.2212063070062 23.9250934510846 28.5711892538614 33.1556572971289 37.6769488702032 42.1353166357157]`（默认）| `vector`

派生的 q 轴表数据，单位为 A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `iq_mtpa` |
| **值：** | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D 轴表数据，id\_mtpa** | **最大转矩，T\_max**  **MTPA 表断点，pb** | **Id 和 Iq 计算** |
| **Permanent magnet flux, lambda\_pm**  **D-axis inductance, Ld**  **Q-axis inductance, Lq**  **Number of pole pairs, PolePairs** | **Motor Parameters** |

### **D, Q, and max current limits, idq\_limits** — 派生 `[-11.2210468862948 42.1352838229553 43.6038305205566]`（默认）| `array`

派生的 d、q 和最大电流限值，单位为 A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `idq_limits` |
| **值：** | `array` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D、Q 和最大电流限值，idq\_limits** | **最大转矩，T\_max**  **MTPA 表断点，pb** | **Id 和 Iq 计算** |
| **Permanent magnet flux, lambda\_pm**  **D-axis inductance, Ld**  **Q-axis inductance, Lq**  **Number of pole pairs, PolePairs** | **Motor Parameters** |

#### 电流控制器

### **电流调节器带宽，EV\_current** — 带宽 `200`（默认）| `标量`

推导的电流调节器带宽，单位为 Hz。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EV_current` |
| **值：** | `200`（默认）| `标量` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **电流调节器带宽，EV\_current** | **D 轴比例增益，Kp\_d**  **Q 轴比例增益，Kp\_q**  **D 轴和 Q 轴比例增益，Ki** | **电流控制器** |

### **转矩控制采样时间，Tst** — 时间 `5e-5`（默认）| `标量`

推导的转矩控制采样时间，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Tst` |
| **值：** | `5e-5`（默认）| `标量` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **转矩控制采样时间，Tst** | **速度调节时间常数，Ksf** | **速度控制器** |

### **计算电流调节器增益** — 推导参数按钮

点击以推导参数。

#### 依赖关系

在 **电流控制器** 选项卡上，当您
选择 **计算电流调节器增益** 时，
该模块会计算推导参数。下表汇总了推导参数
对其他模块参数的依赖关系。

| **电流控制器** 选项卡上的推导参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D 轴比例增益，Kp\_d**  **Q 轴比例增益，Kp\_q**  **D 轴和 Q 轴积分增益，Ki** | **电流调节器带宽，EV\_current** | **电流控制器** |
| **定子电阻，Rs** | **电机参数** |

### **D 轴比例增益，Kp\_d** — 推导 `2.1363`（默认）| `标量`

推导的 d 轴比例增益，单位为 V/A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kp_d` |
| **值：** | `2.1363`（默认）| `标量` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D 轴比例增益，Kp\_d** | **电流调节器带宽，EV\_current** | **电流控制器** |

### **Q 轴比例增益，Kp\_q** — 推导 `4.0212`（默认）| `标量`

推导的 q 轴比例增益，单位为 V/A。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kp_q` |
| **值：** | `4.0212`（默认）| `标量` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Q 轴比例增益，Kp\_q** | **电流调节器带宽，EV\_current** | **电流控制器** |

### **D 轴和 Q 轴积分增益，Ki** — 推导 `25.1327`（默认）| `标量`

推导的 d 轴和 q 轴积分增益，单位为 V/A·s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ki` |
| **值：** | `25.1327`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **D 轴和 Q 轴积分增益，Ki** | **定子电阻，Rs** | **Motor Parameters** |

#### 速度控制器

### **运动控制器带宽，EV\_motion** — 带宽 `[20, 4, 0.8]`（默认） | `vector`

运动控制器带宽，单位为 Hz。将向量的第一个元素设置为期望的截止频率。将向量的第二个和第三个元素设置为高阶截止频率。您可以将下一个元素的值设置为前一个元素值的 `1/5`。例如，如果期望的截止频率为 `20` Hz，请指定 `[20 4 0.8]`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EV_motion` |
| **值：** | `[20, 4, 0.8]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

当 **Control Type** 参数设置为 `Speed Control` 时，该参数启用。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **运动控制器带宽，EV\_motion** | **比例增益，ba**  **角度增益，Ksa**  **旋转增益，Kisa** | **Speed Controller** |

### **状态滤波器带宽，EV\_sf** — 带宽 `200`（默认） | `scalar`

状态滤波器带宽，单位为 Hz。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `EV_sf` |
| **值：** | `200`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

当 **Control Type** 参数设置为 `Speed Control` 时，该参数启用。

| 参数 | 用于推导 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **状态滤波器带宽，EV\_sf** | **速度调节时间常数，Ksf** | **Speed Controller** |

### **Calculate Speed Regulator Gains** — 推导参数按钮

点击以推导参数。

#### 依赖关系

在 **Speed Controller** 选项卡上，当您选择 **Calculate Speed Regulator Gains** 时，模块会计算派生参数。下表汇总了依赖于其他模块参数的派生参数。

| **Speed Controller** 选项卡上的派生参数 | | 依赖于 | |
| --- | --- | --- | --- |
| 参数 | 选项卡 |
| **Proportional gain, ba** | ba=Jp−Jpp1p2p3Tsm | **Bandwidth of the motion controller, EV\_motion**  **Bandwidth of the state filter, EV\_sf** | **Speed Controller** |
| **角增益，Ksa** | Ksa=Jp(p1p2+p2p3+p3p1)−3Jp+2baTsmTsm2 | **转矩控制的采样时间，Tst** | **电流控制器** |
| **Rotational gain, Kisa** | Kisa=−Jp(p1+p2+p3)+3Jp−baTsm−KsaTsm2Tsm3 | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Speed regulation time constant, Ksf** | Ksf=1−exp(−Tsm2πEVsf)Tsm |
| **Inertia compensation, Jcomp** | *Jcomp* = *Jp* | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Viscous damping compensation, Fv** | *F*v** |
| **Static friction, Fs** | *Fs* |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *P* | 电机极对数 |
| *ba* | 速度调节器比例增益 |
| *Ksa* | 速度调节器积分增益 |
| *Kisa* | 速度调节器双积分增益 |
| *Ksf* | 速度调节器时间常数 |
| *Jp* | 电机惯量 |
| *EVsf* | 状态滤波器带宽 |
| *EVmotion* | 运动控制器带宽 |

### **Proportional gain, ba** — 派生 `3.7477`（默认）| `scalar`

派生的比例增益，单位为 N·m/(rad/s)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ba` |
| **值：** | `3.7477`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Proportional gain, ba** | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Bandwidth of the motion controller, EV\_motion** | **Speed Controller** |

### **Angular gain, Ksa** — 派生 `94.0877`（默认）| `scalar`

派生的角增益，单位为 N·m/rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ksa` |
| **值：** | `94.0877`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Angular gain, Ksa** | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Bandwidth of the motion controller, EV\_motion** | **Speed Controller** |

### **Rotational gain, Kisa** — 派生 `381.7822`（默认）| `scalar`

派生的旋转增益，单位为 N·m/(rad\*s)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kisa` |
| **值：** | `381.7822`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **Rotational gain, Kisa** | **Physical inertia, viscous damping, static friction, Mechanical** | **Motor Parameters** |
| **Bandwidth of the motion controller, EV\_motion** | **Speed Controller** |

### **Speed regulation time constant, Ksf** — 派生 `1217.9727`（默认）| `scalar`

派生的速度调节时间常数，单位为 1/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ksf` |
| **值：** | `1217.9727`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **速度调节时间常数，Ksf** | **转矩控制的采样时间，Tst** | **电流控制器** |
| **状态滤波器带宽，EV\_sf** | **速度控制器** |

### **惯性补偿，Jcomp** — 派生 `0.025`（默认） | `scalar`

派生的惯性补偿，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jcomp` |
| **值：** | `0.025`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **惯性补偿，Jcomp** | **物理惯性、粘性阻尼、静摩擦，Mechanical** | **电机参数** |

### **粘性阻尼补偿，Fv** — 派生 `0`（默认） | `scalar`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fv` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **粘性阻尼补偿，Fv** | **物理惯性、粘性阻尼、静摩擦，Mechanical** | **电机参数** |

### **静摩擦，Fs** — 派生 `0`（默认） | `scalar`

派生的静摩擦，单位为 N·m/(rad/s)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fs` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

下表汇总了参数依赖关系。

| 参数 | 依赖关系 | |
| --- | --- | --- |
| 参数 | 选项卡 |
| **静摩擦，Fs** | **物理惯性、粘性阻尼、静摩擦，Mechanical** | **电机参数** |

#### 电气损耗

### **Parameterize losses by** — 选择类型 `Single efficiency measurement`（默认）| `Tabulated loss data` | `Tabulated efficiency data`

| 设置 | 模块实现 |
| --- | --- |
| `Single efficiency measurement` | 使用逆变器效率的恒定值计算电气损耗。 |
| `Tabulated loss data` | 根据电机转速和负载转矩的函数计算电气损耗。 |
| `Tabulated efficiency data` | 使用作为电机转速和负载转矩函数的逆变器效率计算电气损耗。    - 将您提供的效率值转换为损耗，并使用表格化损耗进行仿真。 - 忽略您为零转速或零转矩提供的效率值。当转矩或转速为零时，损耗假定为零。 - 使用线性插值确定损耗。根据需要为低转速和低转矩提供表格化数据，以获得较低功率条件下所需的精度水平。 - 对于超出表格范围的转速和转矩幅值，不外推损耗值。 |

最佳实践是使用 `Tabulated loss data` 而不是 `Tabulated efficiency data`：

- 效率在零转速或零转矩时变得不确定。
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

**在 R2017a 中引入**

## 描述

用于内置式永磁同步电机的基于转矩的磁场定向控制器

Interior PM Controller 模块为内置式永磁同步电机 (PMSM) 实现了一个基于转矩的磁场定向控制器，并带有可选的外环速度控制器。内部转矩控制实现了最大转矩每安培 (MTPA) 和磁通弱磁策略。您可以指定速度控制类型或转矩控制类型。

Interior PM Controller 实现了速度控制、转矩确定、调节器、变换和电机的方程。

下图展示了该模块中的信息流。

该模块实现的方程使用以下变量。

|  |  |
| --- | --- |
| *ω* | 转子速度 |
| *ω\** | 转子速度指令 |
| *T\** | 转矩指令 |
| *id*  *i\*d* | d 轴电流  d 轴电流指令 |
| *iq*  *i\*q* | q 轴电流  q 轴电流指令 |
| *vd*,  *v\*d* | d 轴电压  d 轴电压指令 |
| *vq*  *v\*q* | q 轴电压  q 轴电压指令 |
| *va*, *vb*, *vc* | 定子 a、b、c 相电压 |
| *ia*, *ib*, *ic* | 定子 a、b、c 相电流 |

### Speed Controller

要实现速度控制器，请选择 **Control Type** 参数 `Speed Control`。如果选择 **Control Type** 参数 `Torque Control`，则该模块不实现速度控制器。

速度控制器通过实现状态滤波器，并计算前馈和反馈指令来确定转矩指令。如果不实现速度控制器，则向内嵌式 PM 控制器模块输入转矩指令。

**状态滤波器**

状态滤波器是一种低通滤波器，它根据速度指令生成加速度指令。在 **Speed Controller** 选项卡上：

- 若要使速度指令滞后时间可忽略不计，请指定 **Bandwidth of the state filter** 参数。
- 若要基于状态滤波器带宽计算 **Speed regulation time constant, Ksf** 增益，请选择 **Calculate Speed Regulator Gains**。

特征方程的离散形式为：

z+KsfTsm−1

该滤波器使用此方程计算增益。

Ksf=1−exp(−Tsm2πEVsf)Tsm

这些方程使用以下变量。

|  |  |
| --- | --- |
| *EVsf* | 速度指令滤波器的带宽 |
| *Tsm* | 运动控制器采样时间 |
| *Ksf* | 速度调节器时间常数 |

**状态反馈**

为了生成状态反馈转矩，该模块使用来自状态滤波器的滤波后速度误差信号。反馈转矩计算还需要速度调节器的增益。

在 **Speed Controller** 选项卡上，选择 **Calculate Speed Regulator Gains** 以计算：

- **Proportional gain, ba**
- **Angular gain, Ksa**
- **Rotational gain, Kisa**

对于增益计算，该模块使用 **Motor Parameters** 选项卡上 **Physical inertia, viscous damping, static friction** 参数值中的惯量。

状态反馈的增益使用以下方程计算。

| 计算 | 方程 |
| --- | --- |
| 特征方程的离散形式 | z3+(−3Jp+Tsba+ Ts2Ksa+Ts3Kisa)Jpz2+(3Jp− 2Tsba− Ts2Ksa)Jpz+−Jp+TsbaJp  (z−p1)(z−p2)(z−p3)=z3+(p1+p2+p3)z2+(p1p2+p2p3+p13)z2−p1p2p3 |
| 速度调节器比例增益 | ba=Jp−Jpp1p2p3Tsm |
| 速度调节器积分增益 | Ksa=Jp(p1p2+p2p3+p3p1)−3Jp+2baTsmTsm2 |
| 速度调节器双积分增益 | Kisa=−Jp(p1+p2+p3)+3Jp−baTsm−KsaTsm2Tsm3 |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *P* | 电机极对数 |
| *ba* | 速度调节器比例增益 |
| *Ksa* | 速度调节器积分增益 |
| *Kisa* | 速度调节器双积分增益 |
| *Jp* | 电机惯量 |
| *Tsm* | 运动控制器采样时间 |

**指令前馈**

为了生成状态前馈转矩，该模块使用来自状态滤波器的滤波后速度和加速度。此外，前馈转矩计算使用惯量、粘性阻尼和静摩擦。为了实现零跟踪误差，转矩指令是前馈和反馈转矩指令之和。

在 **Speed Controller** 选项卡上选择 **Calculate Speed Regulator Gains** 会使用 **Motor Parameters** 选项卡上的 **Physical inertia, viscous damping, static friction** 参数值更新惯量、粘性阻尼和静摩擦。

前馈转矩指令使用此方程。

Tcmd\_ff= Jpω˙m+Fvωm+Fs ωm|ωm|

其中：

|  |  |
| --- | --- |
| *Jp* | 电机惯量 |
| *Tcmd\_ff* | 转矩指令前馈 |
| *Fs* | 静摩擦转矩常数 |
| *F*v** | 粘性摩擦转矩常数 |
| *Fs* | 静摩擦转矩常数 |
| *ωm* | 转子速度 |

### Torque Determination

该模块使用最大转矩每安培（MTPA）轨迹来计算基速和电流指令。可用的母线电压决定基速。直轴（d）和交轴（q）永磁（PM）决定感应电压。

| 计算 | 方程 |
| --- | --- |
| 进入弱磁区的电基速过渡 | ωbase=  vmax(Lqiq)2+(Ldid+ λpm)2 |
| d 轴电压 | vd=−ωeLqiqmax |
| q 轴电压 | vq=ωe(Ldid\_max+ λpm) |
| 最大相电流 | imax2=id\_max2+iq\_max2 |
| 最大相对中性点电压 | vmax= vbus 3 |
| d 轴相电流 MTPA 表 | Im=2Tmax3Pλpmid\_mtpa=λpm4(Lq−Ld)−λpm216(Lq−Ld)2+Im22 |
| q 轴相电流 MTPA 表 | iq\_mtpa=Im2−(imtpa)2 |
| 转矩 MTPA 断点 | Tmtpa= 32P(λpmiq+(Ld− Lq)idiq) |
| 弱磁，使用基于速度的电压限制 | (Lqiq)2+(Ldid+ λpm)2≤ vmax2ωe2  iq= imax2− id2  (Ld2− Lq2)id2+2λpmLdid+ λpm+ Lq2imax2−vmax2ωe2=0  idfw= −λpmLd+ (λpmLd)2− (Ld2− Lq2)(λpm2+  Lq2imax2− vmax2ωe2  )(Ld2− Lq2)  Tfw= 32P(λpmiqfw+(Ld− Lq)idfwiqfw) |
| 电流指令 | ``` If|ωe|≤ ωbase 		idref= idmtpa(Tref)iqref= iqmtpa(Tref) Else 		 idfw= max(idfw, −imax)iqfw= imax2− id2		 		If  Tfw<Tref 			idref= idfwiqref= iqfw 		Else 			idref= idfwiqref= Tref32P(λpm+(Ld− Lq)idfw) 		End End ``` |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *imax* | 最大相电流 |
| *id* | d 轴电流 |
| *iq* | q 轴电流 |
| *id\_max* | 最大 d 轴相电流 |
| *iq\_max* | 最大 q 轴相电流 |
| *id\_mtpa* | d 轴相电流 MTPA 表 |
| *iq\_mtpa* | q 轴相电流 MTPA 表 |
| *Im* | 估计最大电流 |
| *idfw* | d 轴弱磁电流 |
| *iqfw* | q 轴弱磁电流 |
| *ωe* | 转子电速度 |
| *λpm* | 永磁磁链 |
| *vd* | d 轴电压 |
| *vq* | q 轴电压 |
| *vmax* | 最大相对中性点电压 |
| *vbus* | 直流母线电压 |
| *Ld* | d 轴绕组电感 |
| *Lq* | q 轴绕组电感 |
| *P* | 电机极对数 |
| *Tfw* | 弱磁转矩 |
| *Tmtpa* | 转矩 MTPA 断点 |

### Current Regulators

该模块通过抗积分饱和功能调节电流。经典比例积分（PI）电流调节器不考虑 d 轴和 q 轴耦合或反电动势（EMF）耦合。因此，瞬态性能会恶化。为了考虑耦合，该模块在转子参考坐标系的标量格式中实现复矢量电流调节器（CVCR）。CVCR 解耦：

- d 轴和 q 轴电流交叉耦合
- 反电动势交叉耦合

电流频率响应是一阶系统，带宽为 *EVcurrent*。

该模块实现以下方程。

| 计算 | 方程 |
| --- | --- |
| 转子参考坐标系中的电机电压 | Lddiddt= vd−Rsid+pωmLqiqLqdiqdt= vq−Rsiq−pωmLdid−pωmλpm |
| 电流调节器增益 | ωb=2πEVcurrentKp\_d=LdωbKp\_q=LqωbKi=Rsωb |
| 传递函数 | ididref= ωbs+ωbiqiqref= ωbs+ωb |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *EVcurrent* | 电流调节器带宽 |
| *id* | d 轴电流 |
| *iq* | q 轴电流 |
| *Kp\_d* | 电流调节器 d 轴增益 |
| *Kp\_q* | 电流调节器 q 轴增益 |
| *Ld* | d 轴绕组电感 |
| *Lq* | q 轴绕组电感 |
| *Rs* | 定子相绕组电阻 |
| *ωm* | 转子速度 |
| *vd* | d 轴电压 |
| *vq* | q 轴电压 |
| *λpm* | 永磁磁链 |
| *P* | 电机极对数 |

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

变换使用以下变量。

|  |  |
| --- | --- |
| *ωm* | 转子速度 |
| *P* | 电机极对数 |
| *ωe* | 转子电速度 |
| *Θe* | 转子电角度 |
| *x* | 相电流或电压 |

### 电机

该模块使用相电流和相电压来估算直流母线电流。正电流表示电池放电。负电流表示电池充电。该模块使用以下方程。

|  |  |
| --- | --- |
| 负载功率 | LdPwr=va ia+ vb ib+ vc ic |
| 源功率 | SrcPwr= LdPwr+PwrLoss |
| 直流母线电流 | ibus= SrcPwrvbus |
| 估算的转子转矩 | MtrTrqest=1.5P[λiq+(Ld−Lq)idiq] |
| 单一效率源到负载的功率损耗 | PwrLoss=100−EffEff⋅LdPwr |
| 单一效率负载到源的功率损耗 | PwrLoss=100−Eff100⋅|LdPwr| |
| 表格化效率的功率损耗 | PwrLoss= f(ωm,MtrTrqest) |

方程使用以下变量。

|  |  |
| --- | --- |
| *va*、*vb*、*vc* | 定子 a、b、c 相电压 |
| *vbus* | 估算的直流母线电压 |
| *ia*、*ib*、*ic* | 定子 a、b、c 相电流 |
| *ibus* | 估算的直流母线电流 |
| *Eff* | 逆变器总效率 |
| *ωm* | 转子机械速度 |
| *Lq* | q 轴绕组电感 |
| *Ld* | d 轴绕组电感 |
| *iq* | q 轴电流 |
| *id* | d 轴电流 |
| *λ* | 永磁体磁链 |
| *P* | 电机极对数 |

### 电气损耗

要指定电气损耗，请在 **Electrical Losses** 选项卡中，对于 **Parameterize losses by**，选择以下选项之一。

| 设置 | 模块实现 |
| --- | --- |
| `Single efficiency measurement` | 使用逆变器效率的恒定值计算电气损耗。 |
| `Tabulated loss data` | 电气损耗作为电机速度和负载转矩的函数计算。 |
| `Tabulated efficiency data` | 使用作为电机速度和负载转矩函数的逆变器效率计算电气损耗。    - 将您提供的效率值转换为损耗，并使用表格化损耗进行仿真。 - 忽略您为零速度或零转矩提供的效率值。当转矩或速度为零时，假定损耗为零。 - 使用线性插值确定损耗。根据需要提供低速和低转矩的表格化数据，以获得较低功率条件下所需的精度水平。 - 对于超出表格范围的速度和转矩幅值，不外推损耗值。 |

最佳实践是使用 `Tabulated loss data` 而不是 `Tabulated efficiency data`：

- 效率在零速度或零转矩时变得定义不明确。
- 您可以考虑在零速度或零转矩时仍然存在的固定损耗。
