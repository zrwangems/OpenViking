---
type: simulink-block
title: 'Starter'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Energy Storage'
documentation_page: 'starter'
documentation_source_path: 'ref/starter.html'
language: zh-CN
chinese_source: worker-translation
---

# Starter

## 端口

### 输入

### **MtrSpd** — 角速度 `scalar`

电机轴角速度，单位为 rad/s。

### **StartVolt** — 电枢和励磁电压 `scalar`

- 电枢绕组电压 *Va* 和励磁绕组电压 *Vf*，单位为 V。
- 在串励直流电机中，电枢和励磁绕组电压为 *Vaf*。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `ArmCurr` | | | 电枢绕组电流 | A |
| `FldCurr` | | | 励磁绕组电流 | A |
| `PwrInfo` | `PwrTrnsfrd` | `PwrMtr` | 机械功率 | W |
| `PwrBus` | 电功率 | W |
| `PwrNotTrnsfrd` | `PwrLoss` | 电机功率损耗 | W |
| `PwrStored` | `PwrInd` | 电气电感 | W |

### **LdCurr** — 起动机负载电流 `scalar`

起动机负载电流，单位为 A。

### **MtrTrq** — 起动机轴转矩 `scalar`

起动机轴转矩，单位为 N·m。

## 参数

#### 配置

### **电机类型** — 选择电机类型 `Separately Excited DC Motor`（默认） | `Permanent Magnet Excited DC Motor` | `Series Connection DC Motor`

选择三种电机类型之一。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `machine_type` |
| **值：** | `Separately Excited DC Motor`（默认） | `Permanent Magnet Excited DC Motor` | `Series Connection DC Motor` |
| **数据类型：** | `character vector` |

#### 依赖关系

下表总结了电机参数依赖关系。

| 电机类型 | 启用的电机参数 |
| --- | --- |
| `Separately Excited DC Motor` | **电枢绕组电阻，Ra** |
| **电枢绕组电感，La** |
| **励磁绕组电阻 Rf** |
| **励磁绕组电感，Lf** |
| **互感，Laf** |
| **初始电枢和励磁电流，Iaf** |
| `Permanent Magnet Excited DC Motor` | **电枢绕组电阻，Rapm** |
| **电枢绕组电感，Lapm** |
| **转矩常数，Kt** |
| **初始电枢电流，Ia** |
| `Series Connection DC Motor` | **总电阻，Rser** |
| **总电感，Lser** |
| **初始电流，Iafser** |
| **互感，Lafser** |

#### Separately Excited DC Motor

### **电枢绕组电阻，Ra** — 电阻 `1`（默认） | `scalar`

电枢绕组电阻，单位为 ohm。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ra` |
| **值：** | `1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Separately Excited DC Motor`。

### **电枢绕组电感，La** — 电感 `.1`（默认） | `scalar`

电枢绕组电感，单位为 H。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `La` |
| **值：** | `.1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Separately Excited DC Motor`。

### **励磁绕组电阻，Rf** — 电阻 `.3`（默认） | `scalar`

励磁绕组电阻，单位为 ohm。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rf` |
| **值：** | `.3`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Separately Excited DC Motor`。

### **励磁绕组电感，Lf** — 电感 `.2`（默认） | `scalar`

励磁绕组电感，单位为 H。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lf` |
| **值：** | `.2`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Separately Excited DC Motor`。

### **互感，Laf** — 电感 `.3`（默认） | `scalar`

互感，单位为 H。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Laf` |
| **值：** | `.3`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Separately Excited DC Motor`。

### **初始电枢电流和励磁电流，Iaf** — 电流 `[0 0]`（默认） | `vector`

初始电枢和励磁电流，单位为 A。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Iaf` |
| **值：** | `[0 0]`（默认） | `vector` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Separately Excited DC Motor`。

#### Permanent Magnet Excited DC Motor

### **电枢绕组电阻，Rapm** — 电阻 `.5`（默认） | `scalar`

电枢绕组电阻，单位为 ohm。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rapm` |
| **值：** | `.5`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Permanent Magnet Excited DC Motor`。

### **电枢绕组电感，Lapm** — 电感 `.1`（默认） | `scalar`

电枢绕组电感，单位为 H。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lapm` |
| **值：** | `.1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Permanent Magnet Excited DC Motor`。

### **转矩常数，Kt** — 电机转矩常数 `.1`（默认） | `scalar`

电机转矩常数，单位为 N·m/A。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Kt` |
| **值：** | `.1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Permanent Magnet Excited DC Motor`。

### **初始电枢电流，Ia** — 电流 `.1`（默认） | `scalar`

初始电枢电流，单位为 A。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Ia` |
| **值：** | `.1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Permanent Magnet Excited DC Motor`。

#### Series Connection DC Motor

### **总电阻，Rser** — 电阻 `.1`（默认） | `scalar`

串联连接的励磁和电枢电阻，单位为 ohm。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Rser` |
| **值：** | `.1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Series Excited DC Motor`。

### **总电感，Lser** — 电感 `.1`（默认） | `scalar`

串联连接的励磁和电枢电感，单位为 H。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lser` |
| **值：** | `.1`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Series Excited DC Motor`。

### **初始电流，Iafser** — 电流 `0`（默认） | `scalar`

初始串联电流，单位为 A。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Iafser` |
| **值：** | `0`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Series Excited DC Motor`。

### **互感，Lafser** — 电感 `.3`（默认） | `scalar`

励磁和电枢互感，单位为 H。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lafser` |
| **值：** | `.3`（默认） | `scalar` |
| **数据类型：** | `double` |

#### 依赖关系

要启用此参数，请为 **电机类型** 参数选择 `Series Excited DC Motor`。

## 所属库

Powertrain Blockset / Energy Storage and Auxiliary Drive / Starter

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2017a 中引入**

## 描述

Starter 作为直流电机

Starter 模块将起动机总成实现为他励直流电机、永磁直流电机或串励直流电机。该电机作为内燃机的转矩源运行。

使用 Starter 模块：

- 在带有前端附件驱动 (FEAD) 的发动机模型中
- 对发动机起动和停止场景进行建模

Starter 模块仅支持直流电机的角速度输入。负载转矩输入需要发动机动力学。

### Separately Excited DC Motor

在他励直流电机中，励磁绕组连接到独立的直流电源。

励磁绕组电压、励磁电阻和励磁电感之间的关系由下式给出：

Vf=Lfdifdt+Rfif

反电动势是励磁电阻、互感和电机轴角速度的乘积：

EMF=LaifLafω

电枢电压由下式给出：

Va=Ladiadt+Raia+ EMF

起动机电流负载是励磁绕组电流和电枢绕组电流之和：

iload= if+ ia

起动机轴转矩是电枢电流、励磁电流和互感的乘积：

Tmech= iaifLaf

### Permanent Magnet DC Motor

在永磁直流电机中，磁体建立励磁磁通，因此没有励磁电流。

反电动势与电机轴角速度成正比：

EMF= Ktω

电枢电压由下式给出：

Va=Ladiadt+Raia+ EMF

起动机电流负载等于电枢绕组电流：

iload= ia

起动机轴转矩与电枢绕组电流成正比：

Tmech= Ktia

### Series Excited DC Motor

串励直流电机将电枢绕组和励磁绕组串联连接到公共直流电源。

反电动势是励磁和电枢初始串联电流、励磁和电枢互感以及电机轴角速度的乘积：

EMF=iafLafω

励磁和电枢绕组电压由下式给出：

Vaf=Lserdiafdt+Rseriaf+ EMF

起动机电流负载等于励磁和电枢串联电流：

iload= iaf

起动机轴转矩是励磁和电枢串联电流的平方与励磁和电枢互感的乘积：

Tmech= iaf2Laf

为保证电机稳定性，电机轴角速度必须大于串联连接的励磁和电枢电阻与互感之比：

ω>−RserLaf

### 功率核算

对于功率核算，模块实现以下方程。

| 总线信号 | | | 描述 | 变量 | 方程 |
| --- | --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrMtr` | 机械功率 | *Pmot* | Pmot= −ωTmech |
| `PwrBus` | 电功率 | *Pbus* | 他励直流电机  Pbus= vaia+vfif |
| 永磁励磁直流电机  Pbus= vaia |
| 串励直流电机  Pbus= vafiaf |
| `PwrNotTrnsfrd` — 功率跨过模块边界，但未传输  - 正信号表示输入 - 负信号表示损耗 | `PwrLoss` | 电机损耗 | *Ploss* | Ploss= −(Pmot+Pbus−Pind) |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrInd` | 电气电感 | *Pind* | 他励直流电机  Pind= Lfifdifdt+Laiadiadt |
| 永磁励磁直流电机  Pind= Laiadiadt |
| 串励直流电机  Pind=Lseriafdiafdt |

方程使用这些变量。

|  |  |
| --- | --- |
| *Ra* | 电枢绕组电阻 |
| *La* | 电枢绕组电感 |
| *EMF* | 反电动势 |
| *Rf* | 励磁绕组电阻 |
| *Lf* | 励磁绕组电感 |
| *Laf* | 励磁和电枢互感 |
| *ia* | 电枢绕组电流 |
| *if* | 励磁绕组电流 |
| *Kt* | 电机转矩常数 |
| *ω* | 电机轴角速度 |
| *Va* | 电枢绕组电压 |
| *Vf* | 励磁绕组电压 |
| *Vaf* | 励磁和电枢绕组电压 |
| *iaf* | 励磁和电枢串联电流 |
| *Rser* | 串联连接的励磁和电枢电阻 |
| *Lser* | 串联连接的励磁和电枢电感 |
| *iload* | 起动机电流负载 |
| *Tmech* | 起动机轴转矩 |
