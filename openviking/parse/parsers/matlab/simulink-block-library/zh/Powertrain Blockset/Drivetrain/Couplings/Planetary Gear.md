---
type: simulink-block
title: 'Planetary Gear'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain / Couplings'
documentation_page: 'planetarygear'
documentation_source_path: 'ref/planetarygear.html'
language: zh-CN
chinese_source: worker-translation
---

# Planetary Gear

## 端口
```yaml
ports:
- name: SunTrq
  summary: 太阳轮施加的转矩 scalar
  direction: input
- name: CarrTrq
  summary: 行星架施加的转矩 scalar
  direction: input
- name: RingTrq
  summary: 齿圈施加的转矩 scalar
  direction: input
- name: C
  summary: 行星架角速度和转矩双向连接端口
  direction: input
- name: Info
  summary: 总线信号 bus
  direction: output
- name: SunSpd
  summary: 太阳轮角速度 scalar
  direction: output
- name: CarrSpd
  summary: 行星架角速度 scalar
  direction: output
- name: RingSpd
  summary: 齿圈角速度 scalar
  direction: output
- name: S
  summary: 太阳轮角速度和转矩双向连接端口
  direction: output
- name: R
  summary: 齿圈角速度和转矩双向连接端口
  direction: output
```

### 输入

### **SunTrq** — 太阳轮施加的转矩 `scalar`

太阳轮输入转矩，*Ts*，
单位为 N·m。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为
`Simulink`。

### **CarrTrq** — 行星架施加的转矩 `scalar`

行星架输入转矩，
*Tc*，单位为 N·m。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为
`Simulink`。

### **RingTrq** — 齿圈施加的转矩 `scalar`

齿圈施加的转矩，
*Tr*，单位为 N·m。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为
`Simulink`。

### **C** — 行星架角速度和转矩双向连接端口

行星架角速度，*ωc*，
单位为 rad/s。行星架施加的转矩，*Tc*，
单位为 N·m。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为
`Two-way connection`。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| Sun | `SunTrq` | | 太阳轮施加的转矩 | N·m |
| `SunSpd` | | 太阳轮角速度 | rad/s |
| Carr | `CarrTrq` | | 行星架施加的转矩 | N·m |
| `CarrSpd` | | 行星架角速度 | rad/s |
| Ring | `RingTrq` | | 齿圈施加的转矩 | N·m |
| PwrInfo | `PwrTrnsfrd` | `PwrSun` | 太阳轮施加的功率 | W |
| `PwrCarr` | 行星架施加的功率 | W |
| `PwrRing` | 齿圈施加的功率 | W |
| `PwrNotTrnsfrd` | `PwrDampLoss` | 机械阻尼损耗 | W |
| `PwrStored` | `PwrStoredPlntry` | 旋转动能变化率 | W |

### **SunSpd** — 太阳轮角速度 `scalar`

太阳轮角速度，*ωs*，
单位为 rad/s。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为
`Simulink`。

### **CarrSpd** — 行星架角速度 `scalar`

行星架角速度，
*ωc*，单位为 rad/s。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为
`Simulink`。

### **RingSpd** — 齿圈角速度 `scalar`

齿圈角速度，*ωr*，
单位为 rad/s。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为
`Simulink`。

### **S** — 太阳轮角速度和转矩双向连接端口

太阳轮角速度，*ωs*，
单位为 rad/s。太阳轮施加的转矩，
*Ts*，单位为 N·m。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为
`Two-way connection`。

### **R** — 齿圈角速度和转矩双向连接端口

齿圈角速度，*ωr*，
单位为 rad/s。齿圈施加的转矩，
*Tr*，单位为 N·m。

#### 依赖

要创建此端口，请将 **Port Configuration** 设置为
`Two-way connection`。
## 参数
```yaml
parameters:
- name: Port Configuration
  summary: 指定配置 Simulink（默认）| Two-way connection
  group: ''
  block_parameter: port_config
  values: Simulink（默认）| Two-way connection
- name: Sun to planet ratio, Nsp
  summary: 比值 30/23（默认）| 正标量
  group: ''
  block_parameter: Nsp
  values: 30/23（默认）| 正标量
- name: Sun to ring ratio, Nsr
  summary: 比值 30/78（默认）| 正标量
  group: ''
  block_parameter: Nsr
  values: 30/78（默认）| 正标量
- name: Sun inertia, Js
  summary: 惯性 .003（默认）| 正标量
  group: ''
  block_parameter: Js
  values: .003（默认）| 正标量
- name: Planet inertia, Jp
  summary: 惯性 .001（默认）| 正标量
  group: ''
  block_parameter: Jp
  values: .001（默认）| 正标量
- name: Ring inertia, Jr
  summary: 惯性 .01（默认）| 正标量
  group: ''
  block_parameter: Jr
  values: .01（默认）| 正标量
- name: Carrier inertia, Jc
  summary: 惯性 .002（默认）| 正标量
  group: ''
  block_parameter: Jc
  values: .002（默认）| 正标量
- name: Sun viscous damping, bs
  summary: 阻尼 .001（默认）| 大于或等于 0 的标量
  group: ''
  block_parameter: bs
  values: .001（默认）| 大于或等于 0 的标量
- name: Ring viscous damping, br
  summary: 阻尼 .001（默认）| 大于或等于 0 的标量
  group: ''
  block_parameter: br
  values: .001（默认）| 大于或等于 0 的标量
- name: Planet viscous damping, bp
  summary: 阻尼 .001（默认）| 大于或等于 0 的标量
  group: ''
  block_parameter: bp
  values: .001（默认）| 大于或等于 0 的标量
- name: Carrier viscous damping, bc
  summary: 阻尼 .001（默认）| 大于或等于 0 的标量
  group: ''
  block_parameter: bc
  values: .001（默认）| 大于或等于 0 的标量
- name: 初始太阳轮速度，ws_o
  summary: 角速度 0（默认）| 大于或等于 0 的标量
  group: ''
  block_parameter: ws_o
  values: 0（默认）| 大于或等于 0 的标量
- name: 初始行星架速度，wc_o
  summary: 角速度 0（默认）| 大于或等于 0 的标量
  group: ''
  block_parameter: wc_o
  values: 0（默认）| 大于或等于 0 的标量
```

#### 模块选项

### **Port Configuration** — 指定配置 `Simulink`（默认）| `Two-way connection`

指定端口配置。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `port_config` |
| **值：** | `Simulink`（默认）| `Two-way connection` |
| **数据类型：** | `character vector` |

#### 依赖

指定 `Simulink` 会创建以下端口：

- `SunTrq`
- `CarrTrq`
- `RingTrq`
- `SunSpd`
- `CarrSpd`
- `RingSpd`

指定 `Two-way connection` 会创建以下端口：

- `C`
- `S`
- `R`

### **Sun to planet ratio, Nsp** — 比值 `30/23`（默认）| 正标量

太阳轮与行星轮的齿轮比，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Nsp` |
| **值：** | `30/23`（默认）| 正标量 |
| **数据类型：** | `double` |

### **Sun to ring ratio, Nsr** — 比值 `30/78`（默认）| 正标量

太阳轮与齿圈的齿轮比，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Nsr` |
| **值：** | `30/78`（默认）| 正标量 |
| **数据类型：** | `double` |

### **Sun inertia, Js** — 惯性 `.003`（默认）| 正标量

太阳轮惯性，*Js*，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Js` |
| **值：** | `.003`（默认）| 正标量 |
| **数据类型：** | `double` |

### **Planet inertia, Jp** — 惯性 `.001`（默认）| 正标量

行星轮惯性，*Jp*，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jp` |
| **值：** | `.001`（默认）| 正标量 |
| **数据类型：** | `double` |

### **Ring inertia, Jr** — 惯性 `.01`（默认）| 正标量

齿圈惯性，*Jr*，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jr` |
| **值：** | `.01`（默认）| 正标量 |
| **数据类型：** | `double` |

### **Carrier inertia, Jc** — 惯性 `.002`（默认）| 正标量

行星架惯性，*Jc*，单位为 kg·m^2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Jc` |
| **值：** | `.002`（默认）| 正标量 |
| **数据类型：** | `double` |

### **Sun viscous damping, bs** — 阻尼 `.001`（默认）| 大于或等于 0 的标量

太阳轮粘性阻尼，*bs*，单位为 N·m· s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bs` |
| **值：** | `.001`（默认）| 大于或等于 0 的标量 |
| **数据类型：** | `double` |

### **Ring viscous damping, br** — 阻尼 `.001`（默认）| 大于或等于 0 的标量

齿圈粘性阻尼，*br*，单位为 N·m· s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `br` |
| **值：** | `.001`（默认）| 大于或等于 0 的标量 |
| **数据类型：** | `double` |

### **Planet viscous damping, bp** — 阻尼 `.001`（默认）| 大于或等于 0 的标量

行星轮粘性阻尼，*bp*，单位为 N·m· s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bp` |
| **值：** | `.001`（默认）| 大于或等于 0 的标量 |
| **数据类型：** | `double` |

### **Carrier viscous damping, bc** — 阻尼 `.001`（默认）| 大于或等于 0 的标量

行星架粘性阻尼，*bc*，单位为 N·m· s/rad。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `bc` |
| **值：** | `.001`（默认）| 大于或等于 0 的标量 |
| **数据类型：** | `double` |

### **初始太阳轮速度，ws\_o** — 角速度 `0`（默认）| 大于或等于 0 的标量

初始太阳轮角速度，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `ws_o` |
| **值：** | `0`（默认）| 大于或等于 0 的标量 |
| **数据类型：** | `double` |

### **初始行星架速度，wc\_o** — 角速度 `0`（默认）| 大于或等于 0 的标量

初始行星架角速度，单位为 rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `wc_o` |
| **值：** | `0`（默认）| 大于或等于 0 的标量 |
| **数据类型：** | `double` |
## 所属库

Powertrain Blockset / Drivetrain / Couplings

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

带太阳轮、齿圈和行星架的理想行星齿轮

Planetary Gear 模块实现了一个理想行星齿轮耦合，由刚性耦合的太阳轮、齿圈和行星架齿轮组成。该模块根据太阳轮、行星架和齿圈的输入转矩计算动态响应。

在燃油经济性和动力总成研究中，您可以将 Planetary Gear 模块作为功率分流装置使用，将其与常见传动系统元件（如变速器、发动机、离合器和差速器）耦合。

这些运动方程表示行星齿轮的动态响应。

ω˙sJs=ω˙sbs+Ts+Tpsω˙cJc=ω˙cbc+Tc+Tpcω˙sJr=ω˙rbr+Tr+Tprω˙pJp=ωpbp+Trp+Tsp+Tcp

为简化运动方程，该模块使用以下运动学和几何约束。

ωcrc=rsωs+rpωpωrrr=rcωc+rpωprc=rs+rprr=rc+rp

### 功率核算

对于功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrSun` | 太阳轮施加功率 | ωsTs |
| `PwrCarr` | 行星架施加功率 | ωcTc |
| `PwrRing` | 齿圈施加功率 | ωrTr |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损失 | `PwrDampLoss` | 机械阻尼损失 | −(bsωs2+bcωc2+brωr2+bpωp2) |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredPlntry` | 旋转动能的变化率 | ω˙sωsJs+ ω˙cωcJc+ ω˙rωrJr+ ω˙pωpJp |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *ωc*、*ωp*、*ωr*、*ωs* | 行星架、行星轮、齿圈和太阳轮角速度 |
| *rc*、*rp*、*rr*、*rs* | 行星架、行星轮、齿圈和太阳轮角半径 |
| *Jc*、*Jp*、*Jr*、*Js* | 行星架、行星轮、齿圈和太阳轮惯量 |
| *bc*、*bp*、*br*、*bs* | 行星架、行星轮、齿圈和太阳轮阻尼 |
| *Tc*、*Tp*、*Tr*、*Ts* | 施加的行星架、行星轮、齿圈和太阳轮转矩 |
| *Tps* | 行星轮施加在太阳轮上的转矩 |
| *Tpc* | 行星轮施加在行星架上的转矩 |
| *Tpr* | 行星轮施加在齿圈上的转矩 |
| *Trp* | 齿圈施加在行星轮上的转矩 |
| *Tsp* | 太阳轮施加在行星轮上的转矩 |
| *Tcp* | 行星架施加在行星轮上的转矩 |
