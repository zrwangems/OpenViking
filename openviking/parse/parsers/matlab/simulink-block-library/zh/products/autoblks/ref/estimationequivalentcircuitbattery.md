---
type: simulink-block
title: 'Estimation Equivalent Circuit Battery'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Energy Storage'
documentation_page: 'estimationequivalentcircuitbattery'
documentation_source_path: 'ref/estimationequivalentcircuitbattery.html'
language: zh-CN
chinese_source: worker-translation
---

# Estimation Equivalent Circuit Battery

## 端口

### 输入

### **BattCurr** — 电池网络电流 `scalar`

从电池网络流出的组合电流，*Iin*，单位为 A。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | 描述 | 变量 | 单位 |
| --- | --- | --- | --- |
| `CapVolt` | 第 *`n`* 个 RC 对的电压 | *Vn* | V |

### **BattVolt** — 电池输出电压 `scalar`

电池网络的组合电压，*Vout*，单位为 V。

### **BattSoc** — 电池 SOC `scalar`

电池荷电状态，*SOC*。

## 参数

#### 核心电池

### **串联 RC 对数** — RC 对数 `1` (默认) | `2` | `3` | `4` | `5`

串联 RC 对数。对于锂电池，通常为 1 或 2。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `NumRC` |
| **值：** | `1` (默认) | `2` | `3` | `4` | `5` |
| **数据类型：** | `double` |

### **开路电压 Em 表数据, Em** — 电压表 `[3.8 3.8 3.8 3.8 3.8 3.8]` (默认) | `array`

开路电压表，*Em*，单位为 V。是 SOC 的函数。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Em` |
| **值：** | `[3.8 3.8 3.8 3.8 3.8 3.8]` (默认) | `array` |
| **数据类型：** | `double` |

### **串联电阻表数据, R0** — 电阻 `[0.01 0.01 0.01 0.01 0.01 0.01]` (默认) | `array`

串联电阻表，*Ro*，单位为 ohms。是 SOC 的函数。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `R0` |
| **值：** | `[0.01 0.01 0.01 0.01 0.01 0.01]` (默认) | `array` |
| **数据类型：** | `double` |

### **荷电状态断点, SOC\_BP** — SOC 断点 `[0 .2 .4 .6 .8 1]` (默认) | `vector`

荷电状态 (SOC) 断点，无量纲。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SOC_BP` |
| **值：** | `[0 .2 .4 .6 .8 1]` (默认) | `vector` |
| **数据类型：** | `double` |

### **电池容量, BattCap** — 容量 `27.6250` (默认) | `scalar`

电池容量，*Cbatt*，单位为 Ah。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BattCap` |
| **值：** | `27.6250` (默认) | `scalar` |
| **数据类型：** | `double` |

### **初始电池容量, BattCapInit** — 容量 `27.6250` (默认) | `scalar`

初始电池容量，*Cbatto*，单位为 Ah。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BattCapInit` |
| **值：** | `27.6250` (默认) | `scalar` |
| **数据类型：** | `double` |

### **初始电容器电压, InitialCapVoltage** — 电压 `0` (默认) | `vector`

初始电容器电压，单位为 V。向量维度必须等于 **串联 RC 对数**。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `InitialCapVoltage` |
| **值：** | `0` (默认) | `vector` |
| **数据类型：** | `double` |

#### R 和 C 表数据

### **网络电阻表数据, R*`n`*** — 查找表 `[0.005 0.005 0.005 0.005 0.005 0.005]` (默认) | `array`

第 *`n`* 个 RC 对的网络电阻表数据，是 SOC 的函数，单位为 ohms。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `R` |
| **值：** | `[0.005 0.005 0.005 0.005 0.005 0.005]` (默认) | `array` |
| **数据类型：** | `double` |

### **网络电容表数据, C*`n`*** — 查找表 `[10000 10000 10000 10000 10000 10000]` (默认) | `array`

第 *`n`* 个 RC 对的网络电容表数据，是 SOC 的函数，单位为 F。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `C` |
| **值：** | `[10000 10000 10000 10000 10000 10000]` (默认) | `array` |
| **数据类型：** | `double` |

#### 电池单体限值

### **积分器电压上限, Vu** — 最大值 `Inf` (默认) | `scalar`

电压上限，单位为 V。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vu` |
| **值：** | `Inf` (默认) | `scalar` |
| **数据类型：** | `double` |

### **积分器电压下限, Vl** — 最小值 `Inf` (默认) | `scalar`

电压下限，单位为 V。

#### 程序化用法

要以程序化方式设置模块参数值，请使用 `set_param` 函数。

要以程序化方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Vl` |
| **值：** | `Inf` (默认) | `scalar` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Energy Storage and Auxiliary Drive / Network Battery

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

## 描述

使用查找表确定组合电压的电阻-电容 (RC) 电路电池

Estimation Equivalent Circuit Battery 模块实现一个电阻-电容 (RC) 电路电池模型，该模型使用参数查找表确定网络电池的组合电压。这些表是荷电状态 (SOC) 的函数。考虑将该模块用于估算电池电压和 SOC，而不是用于系统级模型。

为了获取 SOC，该模块对充电电流和放电电流进行积分。该模块将以下值实现为以 SOC 为函数的查找表：

- 串联电阻，*Ro*=ƒ(*SOC*)
- 电池开路电压，*Em*=ƒ(*SOC*)
- 网络电阻，*Rn*=ƒ(*SOC*)
- 网络电容，*Cn*=ƒ(*SOC*)

为计算电池网络的组合电压，该模块使用以下方程。

VT=Em−IbattRo−∑1nVnVn=∫0t[IbattCn−VnRnCn]dtSOC=−1Cbatt∫0tIbattdtIbatt=IinVout=VT

正电流表示电池放电。负电流表示电池充电。

这些方程使用以下变量。

|  |  |
| --- | --- |
| *SOC* | 荷电状态 |
| *Em* | 电池开路电压 |
| *Ibatt* | 每个模块的电池电流 |
| *Iin* | 从电池网络流出的组合电流 |
| *Ro* | 串联电阻 |
| *n* | 串联 RC 对数 |
| *Vout*, *VT* | 电池网络的组合电压 |
| *Vn* | 第 *`n`* 个 RC 对的电压 |
| *Rn* | 第 *`n`* 个 RC 对的电阻 |
| *Cn* | 第 *`n`* 个 RC 对的电容 |
| *Cbatt* | 电池容量 |
