---
type: simulink-block
title: 'Flux-Based PMSM'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Electric Motors and Inverters'
documentation_page: 'fluxbasedpmsm'
documentation_source_path: 'ref/fluxbasedpmsm.html'
language: zh-CN
chinese_source: worker-translation
---

# Flux-Based PMSM

## 端口

### 输入

### **LdTrq** — 转子轴转矩 `scalar`

转子轴输入转矩，
*Tm*，单位为 N·m。

#### 依赖关系

要创建此端口，请为 **Port Configuration** 参数选择 `Torque`。

### **Spd** — 转子轴速度 `scalar`

转子的角速度，ωm，单位为 rad/s。

#### 依赖关系

要创建此端口，请为 **Port Configuration** 参数选择 `Speed`。

### **PhaseVolt** — 定子端电压 `1`-by-`3` array

定子端电压，
*Va*、
*Vb* 和
*Vc*，单位为 V。

#### 依赖关系

要创建此端口，请为 **Port Configuration** 参数选择 `Speed` 或 `Torque`。
### 输出

### **Info** — 总线信号 bus

该总线信号包含以下模块计算。

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
| `MtrPos` | | | 转子机械角位置 | *θm* | rad |
| `MtrTrq` | | | 电磁转矩 | *Te* | N·m |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | 机械功率 | *Pmot* | W |
| `PwrBus` | 电功率 | *Pbus* | W |
| `PwrNotTrnsfrd` | `PwrElecLoss` | 电阻功率损耗 | *Pelec* | W |
| `PwrMechLoss` | 机械功率损耗 | *Pmech* | W |
| `PwrStored` | `PwrMtrStored` | 电机存储功率 | *Pstr* | W |

### **PhaseCurr** — A、B、C 相电流 `1`-by-`3` array

A、B、C 相电流，*ia*、
*ib* 和
*ic*，单位为 A。

### **MtrTrq** — 电机转矩 `scalar`

电机转矩，*Tmtr*，单位为 N·m。

#### 依赖关系

要创建此端口，请为 **Port configuration** 参数选择 `Speed`。

### **MtrSpd** — 电机速度 `scalar`

电机的角速度，*ωmtr*，单位为 rad/s。

#### 依赖关系

要创建此端口，请为 **Port configuration** 参数选择 `Torque`。

## 参数

#### 模块选项

### **Simulation type** — 选择仿真类型 `Continuous`（默认） | `Discrete`

默认情况下，该模块在仿真期间使用连续采样时间。如果要为单精度目标生成代码，请考虑将该参数设置为 `Discrete`。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `sim_type` |
| **值：** | `Continuous`（默认） | `Discrete` |
| **数据类型：** | `character vector` |

#### 依赖关系

将 **Simulation Type** 设置为 `Discrete` 会创建 **Sample Time, Ts** 参数。

### **Sample time, Ts** — 离散积分采样时间 `0.001`（默认） | `scalar`

离散仿真的积分采样时间，单位为 s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ts` |
| **值：** | `0.001`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

将 **Simulation Type** 设置为 `Discrete` 会创建 **Sample Time, Ts** 参数。

### **Port Configuration** — 选择端口配置 `Torque`（默认） | `Speed`

下表总结了端口配置。

| 端口配置 | 创建输入端口 | 创建输出端口 |
| --- | --- | --- |
| `Torque` | `LdTrq` | `MtrSpd` |
| `Speed` | `Spd` | `MtrTrq` |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `port_config` |
| **值：** | `Torque`（默认） | `Speed` |
| **数据类型：** | `character vector` |

### **Enable memory optimized 2D LUT** — 选择 `off`（默认） | `on`

启用优化查找表的生成，适用于限制内存的代码生成目标。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `enable_hdl` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

### **Vector of d-axis flux, flux\_d** — 磁链断点 `1`-by-`M` vector

*d* 轴磁链，*Ψd*，断点，单位为 Wb。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `flux_d` |
| **值：** | `1`-by-`M` vector |
| **数据类型：** | `double` |

### **Resample storage size for flux\_d, n1** — 磁链位大小 `2`（默认） | `4` | `8` | `16` | `32` | `64` | `128` | `256`

磁链断点存储大小，*n1*，无量纲。该模块根据存储大小对 **Corresponding d-axis current, id** 和 **Corresponding q-axis current, iq** 数据进行重采样。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `n1` |
| **值：** | `2`（默认） | `4` | `8` | `16` | `32` | `64` | `128` | `256` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT**。

### **Vector of q-axis flux, flux\_q** — 磁链断点 `1`-by-`N` vector

*q* 轴磁链，*Ψq*，断点，单位为 Wb。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `flux_q` |
| **值：** | `1`-by-`N` vector |
| **数据类型：** | `double` |

### **Resample storage size for flux\_q, n2** — 磁链位大小 `2`（默认） | `4` | `8` | `16` | `32` | `64` | `128` | `256`

磁链断点存储大小，*n2*，无量纲。该模块根据存储大小对 **Corresponding d-axis current, id** 和 **Corresponding q-axis current, iq** 数据进行重采样。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `n2` |
| **值：** | `2`（默认） | `4` | `8` | `16` | `32` | `64` | `128` | `256` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT**。

### **Corresponding d-axis current, id** — 二维查找表 `M`-by-`N` array

*d* 轴电流 *id* 的值数组，作为 `M` 个 *d* 轴磁链 *Ψd* 和 `N` 个 *q* 轴磁链 *Ψq* 的函数，单位为 A。每个值指定特定 *d* 轴和 *q* 轴磁链组合下的电流。数组大小必须与磁链向量定义的维度匹配。

如果设置 **Enable memory optimized 2D LUT**，该模块会将数据转换为单精度。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `id` |
| **值：** | `M`-by-`N` array |
| **数据类型：** | `double` |

### **Corresponding q-axis current, iq** — 二维查找表 `M`-by-`N` array

*q* 轴电流 *id* 的值数组，作为 `M` 个 *d* 轴磁链 *Ψd* 和 `N` 个 *q* 轴磁链 *Ψq* 的函数，单位为 A。每个值指定特定 *d* 轴和 *q* 轴磁链组合下的电流。数组大小必须与磁链向量定义的维度匹配。

如果设置 **Enable memory optimized 2D LUT**，该模块会将数据转换为单精度。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `iq` |
| **值：** | `M`-by-`N` array |
| **数据类型：** | `double` |

### **flux\_d max endpoint, u1max** — 磁链断点 `0.22457`（默认） | `scalar`

磁链断点最大外推端点，*u1max*，单位为 Wb。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `u1max` |
| **值：** | `0.22457`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT** 和 **Specify Extrapolation**。

### **flux\_d min endpoint, u1min** — 磁链断点 `-0.22607`（默认） | `scalar`

磁链断点最小外推端点，*u1min*，单位为 Wb。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `u1min` |
| **值：** | `-0.22607`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT** 和 **Specify Extrapolation**。

### **flux\_q max endpoint, u2max** — 磁链断点 `0.42959`（默认） | `scalar`

磁链断点最大外推端点，*u2max*，单位为 Wb。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `u2max` |
| **值：** | `0.42959`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT** 和 **Specify Extrapolation**。

### **flux\_q min endpoint, u2min** — 磁链断点 `-0.4296`（默认） | `scalar`

磁链断点最小外推端点，*u2min*，单位为 Wb。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `u2min` |
| **值：** | `-0.4296`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要创建此参数，请选择 **Enable memory optimized 2D LUT** 和 **Specify Extrapolation**。

### **Stator phase resistance, Rs** — 电阻 `0.02`（默认） | `scalar`

定子相电阻，*Rs*，单位为 ohm。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rs` |
| **值：** | `0.02`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Number of pole pairs, P** — 极对数 `4`（默认） | `scalar`

电机极对数，*P*。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `P` |
| **值：** | `4`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Initial flux, fluxdq0** — 磁链 `[0 0]`（默认） | `vector`

初始 *d* 轴和 *q* 轴磁链，*Ψq0* 和 *Ψd0*，单位为 Wb。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `fluxdq0` |
| **值：** | `[0 0]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Initial mechanical position, theta\_init** — 角度 `0`（默认） | `scalar`

初始转子角位置，*θm0*，单位为 rad。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `theta_init` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Initial mechanical speed, omega\_init** — 速度 `0`（默认） | `scalar`

转子的初始角速度，*ωm0*，单位为 rad/s。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omega_init` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 `Torque` 配置参数。

### **Physical inertia, viscous damping, and static friction, mechanical** — 惯量、阻尼、摩擦 `[0.0027, 4.924e-4, 0]`（默认） | `vector`

转子的机械属性：

- 惯量，*J*，单位为 kgm^2
- 粘性阻尼，*F*，单位为 N·m/(rad/s)
- 静摩擦，*Tf*，单位为 N·m

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `mechanical` |
| **值：** | `[0.0027, 4.924e-4, 0]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请选择 `Torque` 配置参数。

## 所属库

Powertrain Blockset / Propulsion / Electric Motors and Inverters

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

基于磁链的永磁同步电机

Flux-Based PMSM 模块实现基于磁链的三相永磁同步电机 (PMSM)，其电动势基于表格。该模块使用三相输入电压调节各相电流，从而可以控制电机转矩或速度。

基于磁链的电机模型会考虑磁饱和和铁耗。为了计算磁饱和和铁耗，Flux-Based PMSM 模块使用磁链的逆。要获取模块参数，您可以使用有限元分析 (FEA) 或使用测功机测量相电压。

默认情况下，该模块将 **Simulation Type** 参数设置为 `Continuous`，以在仿真期间使用连续采样时间。如果要为固定步长双精度和单精度目标生成代码，请考虑将该参数设置为 `Discrete`。然后指定 **Sample Time, Ts** 参数。

要启用适用于限制内存的代码生成目标的功率损耗计算，请选择 **Enable memory optimized 2D LUT**。

### 三相正弦模型电气系统

该模块实现以静止转子参考 (dq) 坐标系表达的方程。*d* 轴与 *a* 轴对齐。转子参考坐标系中的所有量均折算到定子。

该模块使用以下方程。

| 计算 | 方程 |
| --- | --- |
| *q* 轴和 *d* 轴电压 | vd=dψddt+Rsid−ωeψqvq=dψqdt+Rsiq+ωeψd |
| *q* 轴和 *d* 轴电流 | id=f(ψd,ψq)iq=g(ψd,ψq) |
| 机电转矩 | Te=1.5P[ψdiq−ψqid] |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ωm* | 转子机械速度 |
| *ωe* | 转子电速度 |
| *Θda* | 相对于转子 a 轴的 dq 定子电角度 |
| *Rs*, *Rr* | 分别为定子和转子绕组的电阻 |
| *iq*, *id* | 分别为 *q* 轴和 *d* 轴电流 |
| *vq*, *vd* | 分别为 *q* 轴和 *d* 轴电压 |
| *Ψq*, *Ψd* | 分别为 *q* 轴和 *d* 轴磁体磁链 |
| *P* | 极对数 |
| *Te* | 电磁转矩 |

### 变换

为了计算平衡三相 (*a*, *b*) 量、正交两相 (*α*, *β*) 量和旋转 (*d*, *q*) 参考坐标系中的电压和电流，该模块使用 Clarke 和 Park 变换。

在变换方程中。

ωe=Pωmdθedt= ωe

| 变换 | 描述 | 方程 |
| --- | --- | --- |
| Clarke | 将平衡三相量 (*a*, *b*) 转换为平衡两相正交量 (*α*, *β*)。 | xα= 23xa− 13xb −13xcxβ= 32xb− 32xc |
| Park | 将平衡两相正交静止量 (*α*, *β*) 转换为正交旋转参考坐标系 (*d*, *q*)。 | xd= xαcosθe+ xβsinθexq= −xαsinθe+ xβcosθe |
| Inverse Clarke | 将平衡两相正交量 (*α*, *β*) 转换为平衡三相量 (*a*, *b*)。 | xa= xaxb= −12xα+ 32xβxc= −12xα− 32xβ |
| Inverse Park | 将正交旋转参考坐标系 (*d*, *q*) 转换为平衡两相正交静止量 (*α*, *β*)。 | xα= xdcosθe− xqsinθexβ= xdsinθe+ xqcosθe |

这些变换使用以下变量。

|  |  |
| --- | --- |
| *ωm* | 转子机械速度 |
| *P* | 电机极对数 |
| *ωe* | 转子电速度 |
| *Θe* | 转子电角度 |
| *x* | 相电流或电压 |

### 机械系统

转子角速度由下式给出：

ddtωm=1J(Te−Tf−Fωm−Tm)dθmdt=ωm

这些方程使用以下变量。

|  |  |
| --- | --- |
| *J* | 转子和负载的组合惯量 |
| *F* | 转子和负载的组合粘性摩擦 |
| *θm* | 转子机械角位置 |
| *Tm* | 转子轴转矩 |
| *Te* | 电磁转矩 |
| *Tf* | 转子和负载的组合摩擦转矩 |
| *ωm* | 转子机械速度 |

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrMtr` | 机械功率 | *Pmot* | Pmot= −ωmTe |
| `PwrBus` | 电功率 | *Pbus* | Pbus= vania+ vbnib+vcnic |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损耗 | `PwrElecLoss` | 电阻功率损耗 | *Pelec* | Pelec= −32(Rsisd2+Rsisq2) |
| `PwrMechLoss` | 机械功率损耗 | *Pmech* | 当 **Port Configuration** 设置为 `Torque` 时：  Pmech= −(ωm2F+ |ωm|Tf)  当 **Port Configuration** 设置为 `Speed` 时：  Pmech= 0 |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrMtrStored` | 电机存储功率 | *Pstr* | Pstr= Pbus+ Pmot+ Pelec + Pmech |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *Rs* | 定子电阻 |
| *ia*,*ib*,*ic* | 定子 A、B、C 相电流 |
| *isq*,*isd* | 定子 *q* 轴和 *d* 轴电流 |
| *van*, *vbn*, *vcn* | 定子 A、B、C 相电压 |
| *ωm* | 转子的机械角速度 |
| *F* | 电机和负载的组合粘性阻尼 |
| *Te* | 电磁转矩 |
| *Tf* | 电机和负载的组合摩擦转矩 |

### 查找表内存优化

**Corresponding d-axis current, id** 和 **Corresponding q-axis current, iq** 查找表的数据是 *d* 轴和 *q* 轴磁链的函数。

要启用适用于限制内存的代码生成目标的电流计算，请选择 **Enable memory optimized 2D LUT**。该模块使用线性插值来为代码生成优化电流查找表值。下表总结了优化实现。

| 用例 | | 实现 |
| --- | --- | --- |
| *d* 轴和 *q* 轴磁链与查找表断点值对齐。 | | 内存优化电流是磁链值交点处的电流查找表值。 |
| *d* 轴和 *q* 轴磁链不与查找表断点值对齐，但在范围内。 | | 内存优化电流是相应磁链值之间的线性插值。 |
| *d* 轴和 *q* 轴磁链不与查找表断点值对齐，并且超出范围。 | | 无法计算内存优化电流。模块使用外推数据。 |

**外推**

为代码生成优化的查找表不支持对超出范围的数据进行外推。但是，您可以通过选择 **Specify Extrapolation** 在功率损耗查找表中包含预先计算的外推值。

该模块使用端点参数来调整表数据大小。

| 用户输入 | 外推 |
| --- | --- |
| 用于外推以覆盖所需工作范围的查找表 | 显示外推查找表以及原始表 |
