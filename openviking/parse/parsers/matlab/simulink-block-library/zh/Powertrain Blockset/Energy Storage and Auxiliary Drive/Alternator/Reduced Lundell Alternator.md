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

### 输入

### **RefVolt** — 交流发电机输出电压指令 `scalar`

交流发电机输出电压指令，单位为 V。

### **AltSpd** — 角速度 `scalar`

电机轴输入角速度，单位为 rad/s。

### **LdCurr** — 交流发电机负载电流 `scalar`

交流发电机负载电流，单位为 A。

不要将该端口连接到交流发电机额定电流，该电流为常数值。模块将交流发电机负载电流用作定子绕组电流，*is*，以确定交流发电机电压和电机转矩。如果将端口连接到额定交流发电机电流，则模块不会对负载电流变化对电压和电机转矩的动态影响进行建模。

### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `FldVolt` | | | 励磁绕组电压 | A |
| `FldFlux` | | | 励磁磁通 | Wb |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | 机械功率 | W |
| `PwrBus` | 电功率 | W |
| `PwrNotTrnsfrd` | `PwrLoss` | 电机功率损耗 | W |
| `PwrStored` | `PwrInd` | 电气绕组损耗 | W |

### **AltVolt** — 交流发电机输出电压 `scalar`

交流发电机输出电压，单位为 V。

### **LdTrq** — 电机轴转矩 `scalar`

电机轴转矩，单位为 N·m。

## 参数

#### 电机配置

### **电压常数, Kv** — 常数 `.1` (default) | `scalar`

电压常数，单位为 V/rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kv` |
| **值：** | `.1` (default) | `scalar` |
| **数据类型：** | `double` |

### **励磁绕组电阻, Rf** — 电阻 `0.2` (default) | `scalar`

励磁绕组电阻，单位为 ohm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rf` |
| **值：** | `0.2` (default) | `scalar` |
| **数据类型：** | `double` |

### **励磁绕组电感, Lf** — 电感 `0.002` (default) | `scalar`

励磁绕组电感，单位为 H。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lf` |
| **值：** | `0.002` (default) | `scalar` |
| **数据类型：** | `double` |

### **定子绕组电阻, Rs** — 电阻 `0.01` (default) | `scalar`

定子绕组电阻，单位为 ohm。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rs` |
| **值：** | `0.01` (default) | `scalar` |
| **数据类型：** | `double` |

### **二极管压降, Vd** — 电压 `0.7` (default) | `scalar`

二极管压降，单位为 V。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vd` |
| **值：** | `0.7` (default) | `scalar` |
| **数据类型：** | `double` |

#### 电压调节器

### **调节器带宽, Fv** — 带宽 `2000` (default) | `scalar`

调节器带宽，单位为 Hz。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fv` |
| **值：** | `2000` (default) | `scalar` |
| **数据类型：** | `double` |

### **电流滤波器带宽, Fc** — 带宽 `1000` (default) | `scalar`

电流滤波器带宽，单位为 Hz。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Fc` |
| **值：** | `1000` (default) | `scalar` |
| **数据类型：** | `double` |

### **励磁电压最大值, Vfmax** — 最大励磁电压 `100` (default) | `scalar`

最大励磁电压，单位为 V。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vfmax` |
| **值：** | `100` (default) | `scalar` |
| **数据类型：** | `double` |

### **励磁电压最小值, Vfmin** — 最小励磁电压 `-100` (default) | `scalar`

最小励磁电压，单位为 V。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vfmin` |
| **值：** | `-100` (default) | `scalar` |
| **数据类型：** | `double` |

#### 机械损耗

### **库仑摩擦, Kc** — 摩擦 `0` (default) | `scalar`

库仑摩擦，单位为 N·m。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kc` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

### **粘性摩擦, Kb** — 摩擦 `0` (default) | `scalar`

粘性摩擦，单位为 N·m/rad/s。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kb` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

### **风阻, Kw** — 风阻 `0` (default) | `scalar`

风阻，单位为 N·m/rad2/s2。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kw` |
| **值：** | `0` (default) | `scalar` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Energy Storage and Auxiliary Drive / Alternator

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

带外部电压调节器的 Reduced Lundell（爪极）交流发电机

Reduced Lundell Alternator 模块实现带外部电压调节器的简化 Lundell（爪极）交流发电机。反电动势（EMF）电压与输入速度和励磁电流成正比。电机作为内燃机的源转矩运行。

使用 Reduced Lundell Alternator 模块：

- 对汽车电气系统建模
- 在带前端附件驱动（FEAD）的发动机模型中

计算得到的电机轴转矩与发动机转速方向相反。您可以：

- 将外部电压调节器调谐到所需带宽。定子电流和两个二极管压降会降低定子电压。
- 将负载电流滤波到所需带宽。负载电流具有 0 A 的下饱和值。

Reduced Lundell Alternator 模块实现使用这些变量的电气、控制和机械系统方程。

### 电气

为了计算电压，模块使用以下方程。

| 计算 | 方程 |
| --- | --- |
| 交流发电机输出电压 | vs=Kvifω−Rsis−2Vd |
| 励磁绕组电压 | vf= Rfif+Lfdifdt |

### 控制

控制器假设没有电阻或电压降。

| 计算 | 方程 |
| --- | --- |
| 励磁绕组电压变换 | Vf(s)=RfIf(s)+sLfIf(s) |
| 励磁绕组电流变换 | If(s)=Vf(s)(Rf+sLf) |
| 开环电气传递函数 | G(s)= Vs(s)Vf(s)= Kvω(Rf+sLf) |
| 开环电压调节器传递函数 | GC(s)=  Vf(s)Vref(s) |
| 闭环传递函数 | T(s)= G(s)Gc(s)1+G(s)Gc(s) |
| 闭环控制器设计 | T(s)=1τs+1→ G(s)Gc(s)= 1τs  GC(s)= Kg (Kp+ Kis)  G(s)GC(s)= Kvω(Rf+sLf)Kg (Kp+ Kis)  Kp=Lf  ,Ki=Rf ,and Kg=2πfKvω |

### 机械

为了计算转矩，模块使用以下方程。

| 计算 | 方程 |
| --- | --- |
| 电气转矩 | τelec= (Kvifω)iload |
| 摩擦转矩 | τfriction= Kbω |
| 风阻转矩 | τwindage=Kwω2 |
| 启动时转矩 | τstart=Kc when ω=0 |
| 电机轴转矩 | τmech=τelec+τfriction+τwindage+τstart |

### 功率核算

对于功率核算，模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传递的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrMtr` | 机械功率 | *Pmot* | Pmot= ωτmech |
| `PwrBus` | 电功率 | *Pbus* | Pbus= − vsiload |
| `PwrNotTrnsfrd` — 穿过模块边界但未传递的功率  - 正信号表示输入 - 负信号表示损失 | `PwrLoss` | 电机功率损耗 | *Ploss* | Ploss= −(Pmot+Pbus−Pind) |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrInd` | 电气绕组损耗 | *Pind* | Pind= Lfifdifdt |

这些方程使用以下变量。

|  |  |
| --- | --- |
| *vref* | 交流发电机输出电压指令 |
| *vf* | 励磁绕组电压 |
| *if* | 励磁绕组电流 |
| *is* | 定子绕组电流 |
| *Vd* | 二极管压降 |
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
