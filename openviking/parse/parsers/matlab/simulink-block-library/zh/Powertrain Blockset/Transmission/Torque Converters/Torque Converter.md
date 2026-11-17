---
type: simulink-block
title: 'Torque Converter'
family: 'autoblks'
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
```yaml
ports:
- name: ImpTrq
  summary: 施加的泵轮扭矩 scalar
  direction: input
- name: TurbTrq
  summary: 施加的涡轮扭矩 scalar
  direction: input
- name: Clutch Force
  summary: 施加的离合器力 scalar
  direction: input
- name: Info
  summary: 总线信号 bus
  direction: output
- name: ImpSpd
  summary: 泵轮转速 scalar
  direction: output
- name: TurbSpd
  summary: 涡轮转速 scalar
  direction: output
```

### 输入

### **ImpTrq** — 施加的泵轮扭矩 `scalar`

施加的输入扭矩，通常来自发动机曲轴或双质量飞轮，单位为 N·m。

### **TurbTrq** — 施加的涡轮扭矩 `scalar`

施加的涡轮扭矩，通常来自变速器，单位为 N·m。

### **Clutch Force** — 施加的离合器力 `scalar`

施加的离合器力，通常来自液压执行器，单位为 N。

#### 依赖关系

要创建此端口，请为 **Lock-up clutch configuration** 参数选择 `External lock-up input`。

### 输出

### **Info** — 总线信号 bus

包含以下模块计算结果的总线信号。

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `Imp` | `ImpTrq` | | 施加的输入扭矩 | N·m |
| `ImpSpd` | | 泵轮旋转轴转速 | rad/s |
| `Turb` | `TurbTrq` | | 施加的涡轮扭矩 | N·m |
| `TurbSpd` | | 涡轮旋转轴转速 | rad/s |
| `Cltch` | `CltchForce` | | 施加的离合器力 | N |
| `CltchLocked` | | 离合器锁定或未锁定状态 | N/A |
| `TrqConv` | `TrqConvSpdRatio` | | 涡轮与泵轮转速比 | N/A |
| `TrqConvEta` | | 扭矩转换效率 | N/A |
| `PwrInfo` | `PwrTrnsfrd` | `PwrImp` | 施加的泵轮功率 | W |
| `PwrTurb` | 施加的涡轮输出功率 | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | 机械阻尼损失 | W |
| `PwrFluidCplingLoss` | 变速器流体热损失 | W |
| `PwrCltchLoss` | 离合器滑差功率损失 | W |
| `PwrStored` | `PwrStoredImp` | 泵轮旋转动能变化率 | W |
| `PwrStoredTurb` | 涡轮旋转动能变化率 | W |

### **ImpSpd** — 泵轮转速 `scalar`

泵轮旋转轴转速，ωi，单位为 rad/s。

### **TurbSpd** — 涡轮转速 `scalar`

涡轮旋转轴转速，ωt，单位为 rad/s。
## 参数
```yaml
parameters:
- name: Lock-up clutch configuration
  summary: 选择锁止离合器配置 Lock-up（默认）| No lock-up | External lock-up input
  group: ''
  block_parameter: TCType
  values: Lock-up（默认）| No lock-up | External lock-up input
- name: Impeller shaft inertia, Ji
  summary: 惯量 .1（默认）| scalar
  group: ''
  block_parameter: Ji
  values: .1（默认）| scalar
- name: Impeller shaft viscous damping, bi
  summary: 粘性阻尼系数 .001（默认）| scalar
  group: ''
  block_parameter: bi
  values: .001（默认）| scalar
- name: Turbine shaft inertia, Jt
  summary: 惯量 .1（默认）| scalar
  group: ''
  block_parameter: Jt
  values: .1（默认） | scalar
- name: 涡轮轴粘性阻尼，bt
  summary: 粘性阻尼系数 .001（默认） | scalar
  group: ''
  block_parameter: bt
  values: .001（默认） | scalar
- name: 初始泵轮轴速度，omegai_o
  summary: 角速度 0（默认） | scalar
  group: ''
  block_parameter: omegai_o
  values: 0（默认） | scalar
- name: 初始涡轮轴速度，omegat_o
  summary: 角速度 0（默认） | scalar
  group: ''
  block_parameter: omegat_o
  values: 0（默认） | scalar
- name: 速度比向量，phi
  summary: 比值 [ 0 0.50 0.60 0.70 0.80 0.87 0.92 0.94 0.96 0.97]（默认） | vector
  group: ''
  block_parameter: phi
  values: '[ 0 0.50 0.60 0.70 0.80 0.87 0.92 0.94 0.96 0.97]（默认） | vector'
- name: 容量系数参数化
  summary: 选择系数比值类型 Input speed / sqrt(input torque)（默认） | Absorbed torque / input speed^2
  group: ''
  block_parameter: KType
  values: Input speed / sqrt(input torque)（默认） | Absorbed torque / input speed^2
- name: 容量向量，psi
  summary: 向量 [12.2938 12.8588 13.1452 13.6285 14.6163 16.2675 19.3503 22.1046 29.9986 50.00]（默认） | vector
  group: ''
  block_parameter: psi
  values: '[12.2938 12.8588 13.1452 13.6285 14.6163 16.2675 19.3503 22.1046 29.9986 50.00]（默认） | vector'
- name: 扭矩比向量，zeta
  summary: 向量 [2.2320 1.5462 1.4058 1.2746 1.1528 1.0732 1.0192 0.9983 0.9983 0.9983]（默认） | vector
  group: ''
  block_parameter: zeta
  values: '[2.2320 1.5462 1.4058 1.2746 1.1528 1.0732 1.0192 0.9983 0.9983 0.9983]（默认） | vector'
- name: Fluid torque response time constant (set to 0 to disable), tauTC
  summary: 时间常数 .02（默认） | scalar
  group: ''
  block_parameter: tauTC
  values: .02（默认） | scalar
- name: Interpolation method
  summary: 选择插值方法 Linear（默认） | Flat | Nearest
  group: ''
  block_parameter: InterpMethod
  values: Linear（默认） | Flat | Nearest
- name: Clutch force equivalent net radius, Reff
  summary: 有效半径 .3（默认） | scalar
  group: ''
  block_parameter: Reff
  values: .3（默认） | scalar
- name: Static friction coefficient, mus
  summary: 系数 1.2（默认） | scalar
  group: ''
  block_parameter: mus
  values: 1.2（默认） | scalar
- name: Kinetic friction coefficient, muk
  summary: 系数 1（默认） | scalar
  group: ''
  block_parameter: muk
  values: 1（默认） | scalar
- name: Start simulation with clutch initially locked
  summary: 选择以初始锁定离合器 off（默认） | on
  group: ''
  block_parameter: Jin
  values: off（默认） | on
- name: Lock-up speed ratio threshold, philu
  summary: 阈值 .85（默认） | scalar
  group: ''
  block_parameter: philu
  values: 0.1（默认） | scalar
- name: Minimum lock-up engagement speed, omegal
  summary: 角速度 900*pi/30（默认） | scalar
  group: ''
  block_parameter: omegal
  values: 0.1（默认） | scalar
- name: Lock-up disengagement speed, omegau
  summary: 角速度 800*pi/30（默认） | scalar
  group: ''
  block_parameter: omegau
  values: 0.1（默认） | scalar
- name: Lock-up clutch force gain, K_c
  summary: 增益 5000（默认） | scalar
  group: ''
  block_parameter: K_c
  values: 0.1（默认） | scalar
- name: Lock-up clutch time constant, tauC
  summary: 时间常数 .0500（默认） | scalar
  group: ''
  block_parameter: tauC
  values: 0.1（默认） | scalar
```

#### 配置

### **Lock-up clutch configuration** — 选择锁止离合器配置 `Lock-up`（默认）| `No lock-up` | `External lock-up input`

| 要建模的对象 | 选择 |
| --- | --- |
| 仅液力耦合器 | `No lock-up` |
| 自动离合器接合 | `Lock-up` |
| 离合器压力作为来自外部信号的输入 | `External lock-up input` |

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `TCType` |
| **值**：| `Lock-up`（默认）| `No lock-up` | `External lock-up input` |
| **Data Types:** | `character vector` |

#### 依赖关系

要启用 **Clutch** 参数，请为 **Lock-up clutch configuration** 参数选择 `Lock-up` 或 `External lock-up input`。

#### Torque Converter

### **Impeller shaft inertia, Ji** — 惯量 `.1`（默认）| `scalar`

泵轮轴惯量，单位为 kg·m^2。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `Ji` |
| **值**：| `.1`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Impeller shaft viscous damping, bi** — 粘性阻尼系数 `.001`（默认）| `scalar`

泵轮轴粘性阻尼，单位为 N·m·s/rad。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `bi` |
| **值**：| `.001`（默认）| `scalar` |
| **Data Types:** | `double` |

### **Turbine shaft inertia, Jt** — 惯量 `.1`（默认）| `scalar`

涡轮轴惯量，单位为 kg·m^2。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jt` |
| **值：** | `.1`（默认） | `scalar` |
| **数据类型：** | `double` |

### **涡轮轴粘性阻尼，bt** — 粘性阻尼系数 `.001`（默认） | `scalar`

涡轮轴粘性阻尼，单位为 N·m·s/rad。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bt` |
| **值：** | `.001`（默认） | `scalar` |
| **数据类型：** | `double` |

### **初始泵轮轴速度，omegai\_o** — 角速度 `0`（默认） | `scalar`

初始泵轮轴速度，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegai_o` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

### **初始涡轮轴速度，omegat\_o** — 角速度 `0`（默认） | `scalar`

初始涡轮轴速度，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegat_o` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

### **速度比向量，phi** — 比值 `[ 0 0.50 0.60 0.70 0.80 0.87 0.92 0.94 0.96 0.97]`（默认） | `vector`

涡轮速度与泵轮速度之比的向量。容量向量和扭矩倍增向量的断点。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `phi` |
| **值：** | `[ 0 0.50 0.60 0.70 0.80 0.87 0.92 0.94 0.96 0.97]`（默认） | `vector` |
| **数据类型：** | `double` |

### **容量系数参数化** — 选择系数比值类型 `Input speed / sqrt(input torque)`（默认） | `Absorbed torque / input speed^2`

| 将系数比值设置为 | 选择 |
| --- | --- |
| 泵轮角速度与泵轮扭矩平方根之比 | `Input speed / sqrt(input torque)` |
| 泵轮吸收扭矩与泵轮角速度平方之比 | `Absorbed torque / input speed^2` |

#### 程序化使用

要以程序化方式设置模块
参数值，请使用 `set_param`
函数。

要以程序化方式获取模块
参数值，请使用 `get_param`
函数。

|  |  |
| --- | --- |
| **参数：** | `KType` |
| **值：** | `Input speed / sqrt(input torque)`（默认） | `Absorbed torque / input speed^2` |
| **数据类型：** | `character vector` |

### **容量向量，psi** — 向量 `[12.2938 12.8588 13.1452 13.6285 14.6163 16.2675 19.3503 22.1046 29.9986 50.00]`（默认） | `vector`

| **容量系数参数化** 设置 | 容量向量单位 |
| --- | --- |
| `Input speed / sqrt(input torque)` | (rad/s)/(N·m)^0.5 |
| `Absorbed torque / input speed^2` | N·m/(rad/s)^2 |

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `psi` |
| **值：** | `[12.2938 12.8588 13.1452 13.6285 14.6163 16.2675 19.3503 22.1046 29.9986 50.00]`（默认） | `vector` |
| **数据类型：** | `double` |

### **扭矩比向量，zeta** — 向量 `[2.2320 1.5462 1.4058 1.2746 1.1528 1.0732 1.0192 0.9983 0.9983 0.9983]`（默认） | `vector`

涡轮扭矩与泵轮速度之比的向量。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `zeta` |
| **值：** | `[2.2320 1.5462 1.4058 1.2746 1.1528 1.0732 1.0192 0.9983 0.9983 0.9983]`（默认） | `vector` |
| **数据类型：** | `double` |

### **Fluid torque response time constant (set to 0 to disable), tauTC** — 时间常数 `.02`（默认） | `scalar`

为了考虑因输入扭矩变化而导致的扭矩计算延迟，请指定流体扭矩传递时间常数，单位为 s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tauTC` |
| **值：** | `.02`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Interpolation method** — 选择插值方法 `Linear`（默认） | `Flat` | `Nearest`

在离散相对速度值之间对扭矩比和容量因子函数进行插值。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InterpMethod` |
| **值：** | `Linear`（默认） | `Flat` | `Nearest` |
| **数据类型：** | `character vector` |

#### 离合器

### **Clutch force equivalent net radius, Reff** — 有效半径 `.3`（默认） | `scalar`

有效半径 Reff，与施加的离合器摩擦力一起用于确定摩擦力，单位为 m。有效半径定义为：

Reff=2(Ro3-Ri3)3(Ro2-Ri2)

该公式使用以下变量。

|  |  |
| --- | --- |
| Ro | 环形盘外半径 |
| Ri | 环形盘内半径 |

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Reff` |
| **值：** | `.3`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用 **Clutch** 参数，请为 **Lock-up clutch configuration** 参数选择 `Lock-up` 或 `External lock-up input`。

### **Static friction coefficient, mus** — 系数 `1.2`（默认） | `scalar`

离合器盘的无量纲静摩擦系数。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `mus` |
| **值：** | `1.2`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用 **Clutch** 参数，请为 **Lock-up clutch configuration** 参数选择 `Lock-up` 或 `External lock-up input`。

### **Kinetic friction coefficient, muk** — 系数 `1`（默认） | `scalar`

离合器盘的无量纲动摩擦系数。

要启用 **Clutch** 参数，请为 **Lock-up clutch configuration** 参数选择 `Lock-up` 或 `External lock-up input`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `muk` |
| **值：** | `1`（默认） | `scalar` |
| **数据类型：** | `double` |

### **Start simulation with clutch initially locked** — 选择以初始锁定离合器 `off`（默认） | `on`

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jin` |
| **值：** | `off`（默认） | `on` |
| **数据类型：** | `character vector` |

#### 依赖关系

要启用此参数，请为 **Lock-up clutch configuration** 参数选择 `Lock-up` 或 `External lock-up input`。

### **Lock-up speed ratio threshold, philu** — 阈值 `.85`（默认） | `scalar`

设置接合离合器锁止的转速比阈值。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `philu` |
| **值：** | `0.1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Lock-up clutch configuration** 参数选择 `Lock-up`。

### **Minimum lock-up engagement speed, omegal** — 角速度 `900*pi/30`（默认） | `scalar`

设置接合离合器锁止的最小泵轮转速，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegal` |
| **值：** | `0.1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Lock-up clutch configuration** 参数选择 `Lock-up`。

### **Lock-up disengagement speed, omegau** — 角速度 `800*pi/30`（默认） | `scalar`

设置分离离合器锁止的最小泵轮转速，单位为 rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `omegau` |
| **值：** | `0.1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Lock-up clutch configuration** 参数选择 `Lock-up`。

### **Lock-up clutch force gain, K\_c** — 增益 `5000`（默认） | `scalar`

开环离合器锁止力增益，单位为 N。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `K_c` |
| **值：** | `0.1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Lock-up clutch configuration** 参数选择 `Lock-up`。

### **Lock-up clutch time constant, tauC** — 时间常数 `.0500`（默认） | `scalar`

开环离合器锁止时间常数，单位为 s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `tauC` |
| **值：** | `0.1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **Lock-up clutch configuration** 参数选择 `Lock-up`。
## 所属库

Powertrain Blockset / Transmission / Torque Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

由泵轮、涡轮和导轮组成的三元件液力变矩器

Torque Converter 模块实现了一个由泵轮、涡轮和导轮组成的三元件液力变矩器，并具有可选的离合器锁止功能。该模块可以模拟驱动（功率从泵轮流向涡轮）和滑行（功率从涡轮耗散在液力变矩器液压油中）。

您可以指定液力变矩器特性：

- 转速比 — 涡轮角速度与泵轮角速度之比
- 扭矩比 — 涡轮扭矩与泵轮扭矩之比
- 容量系数参数化 — 输入转速或输入扭矩的函数

可选的离合器锁止配置包括：

- 无锁止 — 仅对液力耦合器建模
- 锁止 — 对自动离合器接合建模
- 外部锁止 — 将离合器压力建模为来自外部信号的输入

### 动力学

**离合器锁止条件和离合器摩擦**

根据离合器锁止条件，该模块实现以下摩擦模型。

| 如果 | 离合器条件 | 摩擦模型 |
| --- | --- | --- |
| ωi≠ωtorTS<|Jt(Ji+Jt)[Ti+Tf−ωi(bt+bi)]| | 解锁 | Tf=Tk其中：Tk=FcReffmktanh[4(ωi−ωt)]Ts=FcReffmsReff=2(Ro3-Ri3)3(Ro2-Ri2) |
| ωi=ωtandTS≥|Jt(Ji+Jt)[Ti+Tf-wt(bt+bi)+wtbt]| | 锁止 | *Tf* = *Ts* |

**锁止旋转动力学**

若离合器锁止，为对旋转动力学建模，该模块实现以下方程。

ω˙(Ji+Jt)=Ti−ω(bi+bt)+Textω=ωi=ωt

该旋转速度同时表示泵轮和涡轮的旋转速度。

**解锁旋转动力学**

若离合器解锁，为对旋转动力学建模，该模块实现以下方程。

ω˙iJi=Ti−ωibi−Tf−Tpω˙tJt=Text−ωtbt+Tf+TtTp= ωi2ψ(ϕ)Tt= Tpζ(ϕ)

为近似泵轮和涡轮之间的扭矩倍增滞后，您可以指定参数 **Fluid torque response time constant (set to 0 to disable), tauc [s]**。

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrImp` | 施加的泵轮功率 | *Pimp* | ωiTi |
| `PwrTurb` | 施加的涡轮输出功率 | *Pturb* | ωtTt |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrDampLoss` | 机械阻尼损失 | *Pdamploss* | −btωt2−biωi2 |
| `PwrFluidCplingLoss` | 传递到变速器流体的热损失 | *Pflloss* | −(Tpωi−Thydωt) |
| `PwrCltchLoss` | 离合器滑差功率损失 | *Pcltloss* | −Tk(ωi−ωt) |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredImp` | 泵轮旋转动能的变化率 | *Pstrimp* | ω˙iωiJi |
| `PwrStoredTurb` | 涡轮旋转动能的变化率 | *Pstrturb* | ω˙tωtJt |

该模块实现的方程使用以下变量。

|  |  |
| --- | --- |
| Tf | 摩擦力矩 |
| Tk | 动摩擦力矩 |
| Ts | 静摩擦力矩 |
| Ti | 施加的输入扭矩 |
| Tp | 泵轮反作用扭矩 |
| Text | 外部施加的涡轮扭矩 |
| ψ(ϕ) | 扭矩转换容量系数 |
| ζ(ϕ) | 扭矩比 |
| ωi | 泵轮旋转轴速度 |
| ωt | 涡轮旋转轴速度 |
| Ji | 泵轮旋转惯量 |
| Jt | 涡轮旋转惯量 |
| bi | 泵轮旋转粘性阻尼 |
| bt | 涡轮旋转粘性阻尼 |
| Reff | 有效离合器半径 |
| Ro | 环形盘外半径 |
| Ri | 环形盘内半径 |
