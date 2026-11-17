---
type: simulink-block
title: 'Reduced Lundell Alternator'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Energy Storage and Auxiliary Drive / Alternator'
documentation_page: 'reducedlundellalternator'
documentation_source_path: 'ref/reducedlundellalternator.html'
language: zh-CN
chinese_source: worker-translation
---

# Reduced Lundell Alternator

## 端口
```yaml
ports:
- name: RefVolt
  summary: 交流发电机输出电压指令 scalar
  direction: input
- name: AltSpd
  summary: 角速度 scalar
  direction: input
- name: LdCurr
  summary: 交流发电机负载电流 scalar
  direction: input
- name: Info
  summary: 总线信号 bus
  direction: output
- name: AltVolt
  summary: 交流发电机输出电压 scalar
  direction: output
- name: LdTrq
  summary: 电机轴转矩 scalar
  direction: output
```

### 输入

### **RefVolt** — 交流发电机输出电压指令 `scalar`

交流发电机输出电压指令，单位为 V。

### **AltSpd** — 角速度 `scalar`

电机轴输入角速度，单位为 rad/s。

### **LdCurr** — 交流发电机负载电流 `scalar`

交流发电机负载电流，单位为 A。

请勿将该端口连接到交流发电机额定电流，额定电流为常数值。该模块使用交流发电机负载电流作为定子绕组电流 *is*，以确定交流发电机电压和电机转矩。如果将端口连接到额定交流发电机电流，则该模块不会对负载电流变化对电压和电机转矩的动态影响进行建模。
### 输出

### **Info** — 总线信号 bus

包含以下模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `FldVolt` | | | 励磁绕组电压 | A |
| `FldFlux` | | | 励磁磁通 | Wb |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | 机械功率 | W |
| `PwrBus` | 电功率 | W |
| `PwrNotTrnsfrd` | `PwrLoss` | 电机功率损耗 | W |
| `PwrStored` | `PwrInd` | 电绕组损耗 | W |

### **AltVolt** — 交流发电机输出电压 `scalar`

交流发电机输出电压，单位为 V。

### **LdTrq** — 电机轴转矩 `scalar`

电机轴转矩，单位为 N·m。
## 参数
```yaml
parameters:
- name: Voltage constant, Kv
  summary: 常数 .1（默认）| scalar
  group: ''
  block_parameter: Kv
  values: .1（默认）| scalar
- name: Field winding resistance, Rf
  summary: 电阻 0.2（默认）| scalar
  group: ''
  block_parameter: Rf
  values: 0.2（默认）| scalar
- name: Field winding inductance, Lf
  summary: 电感 0.002（默认）| scalar
  group: ''
  block_parameter: Lf
  values: 0.002（默认）| scalar
- name: Stator winding resistance, Rs
  summary: 电阻 0.01（默认）| scalar
  group: ''
  block_parameter: Rs
  values: 0.01（默认）| scalar
- name: Diode voltage drop, Vd
  summary: 电压 0.7（默认）| scalar
  group: ''
  block_parameter: Vd
  values: 0.7（默认）| scalar
- name: Regulator bandwidth, Fv
  summary: 带宽 2000（默认）| scalar
  group: ''
  block_parameter: Fv
  values: 2000（默认）| scalar
- name: 电流滤波器带宽，Fc
  summary: 带宽 1000（默认）| scalar
  group: ''
  block_parameter: Fc
  values: 1000（默认）| scalar
- name: 励磁电压最大值，Vfmax
  summary: 最大励磁电压 100（默认）| scalar
  group: ''
  block_parameter: Vfmax
  values: 100（默认）| scalar
- name: 励磁电压最小值，Vfmin
  summary: 最小励磁电压 -100（默认）| scalar
  group: ''
  block_parameter: Vfmin
  values: -100（默认）| scalar
- name: 库仑摩擦，Kc
  summary: 摩擦 0（默认）| scalar
  group: ''
  block_parameter: Kc
  values: 0（默认）| scalar
- name: 粘性摩擦，Kb
  summary: 摩擦 0（默认）| scalar
  group: ''
  block_parameter: Kb
  values: 0（默认）| scalar
- name: 风阻，Kw
  summary: 风阻 0（默认）| scalar
  group: ''
  block_parameter: Kw
  values: 0（默认）| scalar
```

#### 电机配置

### **Voltage constant, Kv** — 常数 `.1`（默认）| `scalar`

电压常数，单位为 V/rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kv` |
| **值：** | `.1`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Field winding resistance, Rf** — 电阻 `0.2`（默认）| `scalar`

励磁绕组电阻，单位为 ohm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rf` |
| **值：** | `0.2`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Field winding inductance, Lf** — 电感 `0.002`（默认）| `scalar`

励磁绕组电感，单位为 H。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lf` |
| **值：** | `0.002`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Stator winding resistance, Rs** — 电阻 `0.01`（默认）| `scalar`

定子绕组电阻，单位为 ohm。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rs` |
| **值：** | `0.01`（默认）| `scalar` |
| **数据类型：** | `double` |

### **Diode voltage drop, Vd** — 电压 `0.7`（默认）| `scalar`

二极管电压降，单位为 V。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vd` |
| **值：** | `0.7`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 电压调节器

### **Regulator bandwidth, Fv** — 带宽 `2000`（默认）| `scalar`

调节器带宽，单位为 Hz。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fv` |
| **值：** | `2000`（默认）| `scalar` |
| **数据类型：** | `double` |

### **电流滤波器带宽，Fc** — 带宽 `1000`（默认）| `scalar`

电流滤波器带宽，单位为 Hz。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fc` |
| **值：** | `1000`（默认）| `scalar` |
| **数据类型：** | `double` |

### **励磁电压最大值，Vfmax** — 最大励磁电压 `100`（默认）| `scalar`

最大励磁电压，单位为 V。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vfmax` |
| **值：** | `100`（默认）| `scalar` |
| **数据类型：** | `double` |

### **励磁电压最小值，Vfmin** — 最小励磁电压 `-100`（默认）| `scalar`

最小励磁电压，单位为 V。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vfmin` |
| **值：** | `-100`（默认）| `scalar` |
| **数据类型：** | `double` |

#### 机械损耗

### **库仑摩擦，Kc** — 摩擦 `0`（默认）| `scalar`

库仑摩擦，单位为 N·m。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kc` |
| **值：** | `0`（默认）| `scalar` |
| **数据类型：** | `double` |

### **粘性摩擦，Kb** — 摩擦 `0`（默认）| `scalar`

粘性摩擦，单位为 N·m/rad/s。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kb` |
| **值：** | `0`（默认）| `scalar` |
| **数据类型：** | `double` |

### **风阻，Kw** — 风阻 `0`（默认）| `scalar`

风阻，单位为
N·m/rad2/s2。

#### 程序化使用

要以程序化方式设置模块参数值，请使用
`set_param` 函数。

要以程序化方式获取模块参数值，
请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kw` |
| **值：** | `0`（默认）| `scalar` |
| **数据类型：** | `double` |
## 所属库

Powertrain Blockset / Energy Storage and Auxiliary Drive / Alternator

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

带外部电压调节器的简化 Lundell（爪极）交流发电机

Reduced Lundell Alternator 模块实现了一个带外部电压调节器的简化 Lundell（爪极）
交流发电机。反电动势 (EMF)
电压与输入速度和励磁电流成正比。该电机作为
内燃机的源转矩运行。

在以下情况下使用 Reduced Lundell Alternator 模块：

- 对汽车电气系统建模
- 在带有前端附件驱动
  (FEAD) 的发动机模型中

计算得到的电机轴转矩方向与
发动机转速相反。您可以：

- 将外部电压调节器调谐到所需带宽。
  定子电流和两个二极管压降会降低定子电压。
- 将负载电流滤波到所需带宽。
  负载电流具有 0 A 的下饱和值。

Reduced Lundell Alternator 模块实现用于
电气、控制和机械系统的方程，这些方程使用以下变量。

### Electrical

为了计算电压，该模块使用以下方程。

| 计算 | 方程 |
| --- | --- |
| 交流发电机输出电压 | vs=Kvifω−Rsis−2Vd |
| 励磁绕组电压 | vf= Rfif+Lfdifdt |

### Control

控制器假设没有电阻或电压降。

| 计算 | 方程 |
| --- | --- |
| 励磁绕组电压变换 | Vf(s)=RfIf(s)+sLfIf(s) |
| 励磁绕组电流变换 | If(s)=Vf(s)(Rf+sLf) |
| 开环电气传递函数 | G(s)= Vs(s)Vf(s)= Kvω(Rf+sLf) |
| 开环电压调节器传递函数 | GC(s)=  Vf(s)Vref(s) |
| 闭环传递函数 | T(s)= G(s)Gc(s)1+G(s)Gc(s) |
| 闭环控制器设计 | T(s)=1τs+1→ G(s)Gc(s)= 1τs  GC(s)= Kg (Kp+ Kis)  G(s)GC(s)= Kvω(Rf+sLf)Kg (Kp+ Kis)  Kp=Lf  ,Ki=Rf ,and Kg=2πfKvω |

### Mechanical

为了计算转矩，该模块使用以下方程。

| 计算 | 方程 |
| --- | --- |
| 电磁转矩 | τelec= (Kvifω)iload |
| 摩擦转矩 | τfriction= Kbω |
| 风阻转矩 | τwindage=Kwω2 |
| 启动转矩 | τstart=Kc when ω=0 |
| 电机轴转矩 | τmech=τelec+τfriction+τwindage+τstart |

### Power Accounting

为了进行功率核算，该模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrMtr` | 机械功率 | *Pmot* | Pmot= ωτmech |
| `PwrBus` | 电气功率 | *Pbus* | Pbus= − vsiload |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损耗 | `PwrLoss` | 电机功率损耗 | *Ploss* | Ploss= −(Pmot+Pbus−Pind) |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrInd` | 电气绕组损耗 | *Pind* | Pind= Lfifdifdt |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *vref* | 交流发电机输出电压指令 |
| *vf* | 励磁绕组电压 |
| *if* | 励磁绕组电流 |
| *is* | 定子绕组电流 |
| *Vd* | 二极管电压降 |
| *Rf* | 励磁绕组电阻 |
| *Rs* | 定子绕组电阻 |
| *Lf* | 励磁绕组电感 |
| *Kv* | 电压常数 |
| *Fv* | 电压调节器带宽 |
| *Fc* | 输入电流滤波器带宽 |
| *Vfmax* | 励磁控制电压上限饱和值 |
| *Vfmin* | 励磁控制电压下限饱和值 |
| *Kc* | 库仑摩擦系数 |
| *Kb* | 粘性摩擦系数 |
| *Kw* | 风阻系数 |
| *ω* | 电机轴角速度 |
| *iload* | 交流发电机负载电流 |
| *vs* | 交流发电机输出电压 |
| *τmech*, *Tmech* | 电机轴转矩 |
