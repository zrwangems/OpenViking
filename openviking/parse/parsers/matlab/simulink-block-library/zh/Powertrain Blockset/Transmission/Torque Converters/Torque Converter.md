---
type: simulink-block
title: 'Torque Converter'
family: 'transmission'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Transmission / Torque Converters'
documentation_page: 'torqueconverter'
documentation_source_path: 'ref/torqueconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Torque Converter

## 端口

### 输入

### **ImpTrq** — 施加的叶轮转矩 `scalar`

施加的输入转矩，通常来自发动机曲轴或双质量飞轮，单位为 N·m。

### **TurbTrq** — 施加的涡轮转矩 `scalar`

施加的涡轮转矩，通常来自变速箱，单位为 N·m。

### **Clutch Force** — 施加的离合器力 `scalar`

施加的离合器力，通常来自液压执行器，单位为 N。

#### 依赖项

要创建此端口，请为 **锁止离合器配置** 参数选择 `External lock-up input`。
### 输出

### **Info** — Bus 信号 bus

包含这些模块计算的 Bus 信号。

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `Imp` | `ImpTrq` | | 施加的输入转矩 | N·m |
| `ImpSpd` | | 叶轮旋转轴转速 | rad/s |
| `Turb` | `TurbTrq` | | 施加的涡轮转矩 | N·m |
| `TurbSpd` | | 涡轮旋转轴转速 | rad/s |
| `Cltch` | `CltchForce` | | 施加的离合器力 | N |
| `CltchLocked` | | 离合器锁止或未锁止状态 | N/A |
| `TrqConv` | `TrqConvSpdRatio` | | 涡轮与叶轮转速比 | N/A |
| `TrqConvEta` | | 转矩转换效率 | N/A |
| `PwrInfo` | `PwrTrnsfrd` | `PwrImp` | 施加的叶轮功率 | W |
| `PwrTurb` | 施加的涡轮输出功率 | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | 机械阻尼损失 | W |
| `PwrFluidCplingLoss` | 向变速箱油的热损失 | W |
| `PwrCltchLoss` | 离合器滑摩功率损失 | W |
| `PwrStored` | `PwrStoredImp` | 叶轮旋转动能变化率 | W |
| `PwrStoredTurb` | 涡轮旋转动能变化率 | W |

### **ImpSpd** — 叶轮转速 `scalar`

叶轮旋转轴转速，ωi，单位为 rad/s。

### **TurbSpd** — 涡轮转速 `scalar`

涡轮旋转轴转速，ωt，单位为 rad/s。

## 参数

#### 配置

### **Lock-up clutch configuration** — 选择锁止离合器配置 `Lock-up` (默认) | `No lock-up` | `External lock-up input`

| 要建模 | 选择 |
| --- | --- |
| 仅液力耦合 | `No lock-up` |
| 自动离合器接合 | `Lock-up` |
| 来自外部信号的离合器压力作为输入 | `External lock-up input` |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `TCType` |
| **值:** | `Lock-up` (默认) | `No lock-up` | `External lock-up input` |
| **数据类型:** | `character vector` |

#### 依赖项

要启用 **离合器** 参数，请为 **锁止离合器配置** 参数选择 `Lock-up` 或 `External lock-up input`。

#### Torque Converter

### **Impeller shaft inertia, Ji** — 惯量 `.1` (默认) | `scalar`

叶轮轴惯量，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Ji` |
| **值:** | `.1` (默认) | `scalar` |
| **数据类型:** | `double` |

### **Impeller shaft viscous damping, bi** — 粘性阻尼系数 `.001` (默认) | `scalar`

叶轮轴粘性阻尼，单位为 N·m·s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `bi` |
| **值:** | `.001` (默认) | `scalar` |
| **数据类型:** | `double` |

### **Turbine shaft inertia, Jt** — 惯量 `.1` (默认) | `scalar`

涡轮轴惯量，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Jt` |
| **值:** | `.1` (默认) | `scalar` |
| **数据类型:** | `double` |

### **Turbine shaft viscous damping, bt** — 粘性阻尼系数 `.001` (默认) | `scalar`

涡轮轴粘性阻尼，单位为 N·m·s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `bt` |
| **值:** | `.001` (默认) | `scalar` |
| **数据类型:** | `double` |

### **Initial impeller shaft velocity, omegai\_o** — 角速度 `0` (默认) | `scalar`

初始叶轮轴速度，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `omegai_o` |
| **值:** | `0` (默认) | `scalar` |
| **数据类型:** | `double` |

### **Initial turbine shaft velocity, omegat\_o** — 角速度 `0` (默认) | `scalar`

初始涡轮轴速度，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `omegat_o` |
| **值:** | `0` (默认) | `scalar` |
| **数据类型:** | `double` |

### **Speed ratio vector, phi** — 比值 `[ 0 0.50 0.60 0.70 0.80 0.87 0.92 0.94 0.96 0.97]` (默认) | `vector`

涡轮转速与叶轮转速之比的向量。容量向量和转矩倍增向量的断点。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `phi` |
| **值:** | `[ 0 0.50 0.60 0.70 0.80 0.87 0.92 0.94 0.96 0.97]` (默认) | `vector` |
| **数据类型:** | `double` |

### **Capacity factor parameterization** — 选择因子比类型 `Input speed / sqrt(input torque)` (默认) | `Absorbed torque / input speed^2`

| 设置因子比为 | 选择 |
| --- | --- |
| 叶轮角速度与叶轮转矩平方根 | `Input speed / sqrt(input torque)` |
| 叶轮吸收转矩与叶轮角速度平方 | `Absorbed torque / input speed^2` |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `KType` |
| **值:** | `Input speed / sqrt(input torque)` (默认) | `Absorbed torque / input speed^2` |
| **数据类型:** | `character vector` |

### **Capacity vector, psi** — 向量 `[12.2938 12.8588 13.1452 13.6285 14.6163 16.2675 19.3503 22.1046 29.9986 50.00]` (默认) | `vector`

| **容量因子参数化** 设置 | 容量向量单位 |
| --- | --- |
| `Input speed / sqrt(input torque)` | (rad/s)/(N·m)^0.5 |
| `Absorbed torque / input speed^2` | N·m/(rad/s)^2 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `psi` |
| **值:** | `[12.2938 12.8588 13.1452 13.6285 14.6163 16.2675 19.3503 22.1046 29.9986 50.00]` (默认) | `vector` |
| **数据类型:** | `double` |

### **Torque ratio vector, zeta** — 向量 `[2.2320 1.5462 1.4058 1.2746 1.1528 1.0732 1.0192 0.9983 0.9983 0.9983]` (默认) | `vector`

涡轮转矩与叶轮转矩之比的向量。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `zeta` |
| **值:** | `[2.2320 1.5462 1.4058 1.2746 1.1528 1.0732 1.0192 0.9983 0.9983 0.9983]` (默认) | `vector` |
| **数据类型:** | `double` |

### **Fluid torque response time constant (set to 0 to disable), tauTC** — 时间常数 `.02` (默认) | `scalar`

为了考虑由于输入转矩变化而导致的转矩计算延迟，请指定液力转矩传递时间常数，单位为 s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `tauTC` |
| **值:** | `.02` (默认) | `scalar` |
| **数据类型:** | `double` |

### **Interpolation method** — 选择插值方法 `Linear` (默认) | `Flat` | `Nearest`

在离散相对速度值之间插值转矩比和容量因子函数。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `InterpMethod` |
| **值:** | `Linear` (默认) | `Flat` | `Nearest` |
| **数据类型:** | `character vector` |

#### 离合器

### **Clutch force equivalent net radius, Reff** — 有效半径 `.3` (默认) | `scalar`

有效半径 Reff 与施加的离合器摩擦力一起用于确定摩擦力，单位为 m。有效半径定义为：

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

该方程使用以下变量。

|  |  |
| --- | --- |
| Ro | 环形盘外半径 |
| Ri | 环形盘内半径 |

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Reff` |
| **值:** | `.3` (默认) | `scalar` |
| **数据类型:** | `double` |

#### 依赖项

要启用 **离合器** 参数，请为 **锁止离合器配置** 参数选择 `Lock-up` 或 `External lock-up input`。

### **Static friction coefficient, mus** — 系数 `1.2` (默认) | `scalar`

离合器盘的静摩擦系数，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `mus` |
| **值:** | `1.2` (默认) | `scalar` |
| **数据类型:** | `double` |

#### 依赖项

要启用 **离合器** 参数，请为 **锁止离合器配置** 参数选择 `Lock-up` 或 `External lock-up input`。

### **Kinetic friction coefficient, muk** — 系数 `1` (默认) | `scalar`

离合器盘的动摩擦系数，无量纲。

要启用 **离合器** 参数，请为 **锁止离合器配置** 参数选择 `Lock-up` 或 `External lock-up input`。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `muk` |
| **值:** | `1` (默认) | `scalar` |
| **数据类型:** | `double` |

### **Start simulation with clutch initially locked** — 选择以初始锁定离合器 `off` (默认) | `on`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Jin` |
| **值:** | `off` (默认) | `on` |
| **数据类型:** | `character vector` |

#### 依赖项

要启用此参数，请为 **锁止离合器配置** 参数选择 `Lock-up` 或 `External lock-up input`。

### **Lock-up speed ratio threshold, philu** — 阈值 `.85` (默认) | `scalar`

设置使离合器锁止接合的转速比阈值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `philu` |
| **值:** | `0.1` (默认) | `scalar` |
| **数据类型:** | `double` |

#### 依赖项

要启用此参数，请为 **锁止离合器配置** 参数选择 `Lock-up`。

### **Minimum lock-up engagement speed, omegal** — 角速度 `900*pi/30` (默认) | `scalar`

设置使离合器锁止接合的最小叶轮转速，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `omegal` |
| **值:** | `0.1` (默认) | `scalar` |
| **数据类型:** | `double` |

#### 依赖项

要启用此参数，请为 **锁止离合器配置** 参数选择 `Lock-up`。

### **Lock-up disengagement speed, omegau** — 角速度 `800*pi/30` (默认) | `scalar`

设置使离合器锁止解除的最小叶轮转速，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `omegau` |
| **值:** | `0.1` (默认) | `scalar` |
| **数据类型:** | `double` |

#### 依赖项

要启用此参数，请为 **锁止离合器配置** 参数选择 `Lock-up`。

### **Lock-up clutch force gain, K\_c** — 增益 `5000` (默认) | `scalar`

开环离合器锁止力增益，单位为 N。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `K_c` |
| **值:** | `0.1` (默认) | `scalar` |
| **数据类型:** | `double` |

#### 依赖项

要启用此参数，请为 **锁止离合器配置** 参数选择 `Lock-up`。

### **Lock-up clutch time constant, tauC** — 时间常数 `.0500` (默认) | `scalar`

开环离合器锁止时间常数，单位为 s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `tauC` |
| **值:** | `0.1` (默认) | `scalar` |
| **数据类型:** | `double` |

#### 依赖项

要启用此参数，请为 **锁止离合器配置** 参数选择 `Lock-up`。

## 所属库

Powertrain Blockset / Transmission / Torque Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

由叶轮、涡轮和导轮组成的三部件液力变矩器

Torque Converter 模块实现一个由叶轮、涡轮和导轮组成的三部件液力变矩器，并具有可选离合器锁止功能。该模块可以模拟驱动（功率从叶轮流向涡轮）和滑行（来自涡轮的功率在液力变矩器液压油中耗散）。

可以指定液力变矩器特性：

- 转速比 — 涡轮角速度与叶轮角速度之比
- 转矩比 — 涡轮转矩与叶轮转矩之比
- 容量因子参数化 — 输入转速或输入转矩的函数

可选的离合器锁止配置包括：

- No lock-up — 仅对液力耦合建模
- Lock-up — 对自动离合器接合建模
- External lock-up — 将离合器压力建模为来自外部信号的输入

### 动力学

**离合器锁止条件和离合器摩擦**

根据离合器锁止条件，模块实现以下摩擦模型。

| 如果 | 离合器条件 | 摩擦模型 |
| --- | --- | --- |
| ωi≠ωt或TS<|Jt(Ji+Jt)[Ti+Tf−ωi(bt+bi)]| | 未锁止 | Tf=Tk其中：Tk=FcReffmktanh[4(ωi−ωt)]Ts=FcReffmsReff=2(Ro3-Ri3)3(Ro2-Ri2) |
| ωi=ωt且TS≥|Jt(Ji+Jt)[Ti+Tf-wt(bt+bi)+wtbt]| | 锁止 | *Tf* = *Ts* |

**锁止时的旋转动力学**

为了在离合器锁止时对旋转动力学建模，模块实现以下方程。

ω˙(Ji+Jt)=Ti−ω(bi+bt)+Textω=ωi=ωt

该旋转速度表示叶轮和涡轮两者的旋转速度。

**未锁止时的旋转动力学**

为了在离合器未锁止时对旋转动力学建模，模块实现以下方程。

ω˙iJi=Ti−ωibi−Tf−Tpω˙tJt=Text−ωtbt+Tf+TtTp= ωi2ψ(ϕ)Tt= Tpζ(ϕ)

为了近似叶轮与涡轮之间的转矩倍增滞后，可以指定参数 **液力转矩响应时间常数（设置为 0 以禁用）, tauc [s]**。

### 功率核算

对于功率核算，模块实现以下方程。

| Bus 信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrImp` | 施加的叶轮功率 | *Pimp* | ωiTi |
| `PwrTurb` | 施加的涡轮输出功率 | *Pturb* | ωtTt |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrDampLoss` | 机械阻尼损失 | *Pdamploss* | −btωt2−biωi2 |
| `PwrFluidCplingLoss` | 向变速箱油的热损失 | *Pflloss* | −(Tpωi−Thydωt) |
| `PwrCltchLoss` | 离合器滑摩功率损失 | *Pcltloss* | −Tk(ωi−ωt) |
| `PwrStored` — 储存能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredImp` | 叶轮旋转动能变化率 | *Pstrimp* | ω˙iωiJi |
| `PwrStoredTurb` | 涡轮旋转动能变化率 | *Pstrturb* | ω˙tωtJt |

模块实现使用以下变量的方程。

|  |  |
| --- | --- |
| Tf | 摩擦力矩 |
| Tk | 动摩擦力矩 |
| Ts | 静摩擦力矩 |
| Ti | 施加的输入转矩 |
| Tp | 叶轮反作用转矩 |
| Text | 外部施加的涡轮转矩 |
| ψ(ϕ) | 转矩转换容量因子 |
| ζ(ϕ) | 转矩比 |
| ωi | 叶轮旋转轴转速 |
| ωt | 涡轮旋转轴转速 |
| Ji | 叶轮旋转惯量 |
| Jt | 涡轮旋转惯量 |
| bi | 叶轮旋转粘性阻尼 |
| bt | 涡轮旋转粘性阻尼 |
| Reff | 有效离合器半径 |
| Ro | 环形盘外半径 |
| Ri | 环形盘内半径 |
