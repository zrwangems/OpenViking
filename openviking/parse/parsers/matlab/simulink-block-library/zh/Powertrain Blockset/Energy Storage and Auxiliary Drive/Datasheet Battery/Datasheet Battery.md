---
type: simulink-block
title: 'Datasheet Battery'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Energy Storage and Auxiliary Drive'
documentation_page: 'datasheetbattery'
documentation_source_path: 'ref/datasheetbattery.html'
language: zh-CN
chinese_source: worker-translation
---

# Datasheet Battery

## 端口

### 输入

### **CapInit** — 电池容量 `scalar`

标称温度下的额定电池容量，*Capbatt*，单位为 Ah。

#### 依赖关系

要创建此端口，请为 **初始电池容量** 参数选择 `External Input`。

### **BattCurr** — 电池负载电流 `scalar`

从电池网络流出的总电流，*Iin*，单位为 A。

### **BattTemp** — 电池温度 `scalar`

在电池外壳处测得的温度，*T*，单位为 K。

### 输出

### **Info** — 总线信号 bus

包含以下模块计算的总线信号。

| 信号 | | | 描述 | 变量 | 单位 |
| --- | --- | --- | --- | --- | --- |
| `BattCurr` | | | 从电池网络流出的总电流 | *Ibatt* | A |
| `BattAmpHr` | | | 电池能量 | *LdAmpHr* | A\*h |
| `BattSoc` | | | 荷电状态容量 | *SOC* | NA |
| `BattVolt` | | | 电池网络的总电压 | *Vout* | V |
| `BattPwr` | | | 电池网络功率 | *Pbatt* | W |
| `PwrInfo` | `PwrTrnsfrd` | `PwrLdBatt` | 电池网络功率 | *PLdBatt* | W |
| `PwrNotTrnsfrd` | `PwrLossBatt` | 电池网络功率损耗 | *PLossBatt* | W |
| `PwrStored` | `PwrStoredBatt` | 电池网络存储功率 | *PStoredBatt* | W |

### **BattVolt** — 电池输出电压 `scalar`

电池网络的总电压，*Vout*，单位为 V。

## 参数

#### 模块选项

### **初始电池容量** — 输入或参数 `Parameter`（默认） | `External Input`

初始电池容量，*Capbatt*，单位为 Ah。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `CapacityCtrl` |
| **值:** | `Parameter`（默认） | `External Input` |
| **数据类型:** | `character vector` |

#### 依赖关系

| 模块参数 **初始电池容量** 选项 | 创建 |
| --- | --- |
| `External Input` | 输入端口 `CapInit` |
| `Parameter` | 参数 **初始电池容量, BattCapInit** |

### **输出电池电压** — 未滤波或滤波 `Unfiltered`（默认） | `Filtered`

选择 `Filtered` 可对输出电池电压应用一阶滤波器。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutputVlt` |
| **值:** | `Unfiltered`（默认） | `Filtered` |
| **数据类型:** | `character vector` |

#### 依赖关系

将 **输出电池电压** 参数设置为 `Filtered` 会创建以下参数：

- **输出电池电压时间常数, Tc**
- **输出电池电压初始值, Vinit**

### **标称温度下的额定容量, BattChargeMax** — 常量 `100`（默认） | `scalar`

标称温度下的额定电池容量，单位为 Ah。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `BattChargeMax` |
| **值:** | `100`（默认） | `scalar` |
| **数据类型:** | `double` |

### **开路电压表数据, Em** — 一维查找表 `1`-by-`P` matrix

开路电压数据曲线，*Em*，作为 `P` 个工作点的放电容量的函数，单位为 V。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Em` |
| **值:** | `1`-by-`P` matrix |
| **数据类型:** | `double` |

### **用于开路电压的荷电状态断点, SOCEmBp** — 断点 `1`-by-`P` matrix

用于 `P` 个工作点的放电容量断点，无量纲。

尽管此参数与 **用于内阻的荷电状态断点, SOCRintBp** 参数相同，但模块使用独立参数以提高校准灵活性。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SOCEmBp` |
| **值:** | `1`-by-`P` matrix |
| **数据类型:** | `double` |

### **内阻表数据, RInt** — 二维查找表 `N`-by-`M` matrix

内阻映射，*Rint*，作为 `N` 个温度和 `M` 个 SOC 的函数，单位为 ohms。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RInt` |
| **值:** | `N`-by-`M` matrix |
| **数据类型:** | `double` |

### **电池温度断点, BattTempBp** — 断点 `[243.1 253.1 263.1 273.1 283.1 298.1 313.1]`（默认） | `1`-by-`N` matrix

用于 `N` 个温度的电池温度断点，单位为 K。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `BattTempBp` |
| **值:** | `[243.1 253.1 263.1 273.1 283.1 298.1 313.1]`（默认） | `1`-by-`N` matrix |
| **数据类型:** | `double` |

### **用于内阻的荷电状态断点, SOCRintBp** — 断点 `[0 0.2 0.4 0.6 0.8 1]`（默认） | `1`-by-`M` matrix

用于 `M` 个 SOC 的电池容量断点，无量纲。

尽管此参数与 **用于开路电压的荷电状态断点, SOCEmBp** 参数相同，但模块使用独立参数以提高校准灵活性。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SOCRintBp` |
| **值:** | `[0 0.2 0.4 0.6 0.8 1]`（默认） | `1`-by-`M` matrix |
| **数据类型:** | `double` |

### **串联电池单元数, Ns** — 整数 `1`（默认） | `scalar`

串联电池单元数，无量纲，*Ns*。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Ns` |
| **值:** | `1`（默认） | `scalar` |
| **数据类型:** | `double` |

### **并联电池单元数, Np** — 整数 `1`（默认） | `scalar`

并联电池单元数，无量纲，*Np*。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Np` |
| **值:** | `1`（默认） | `scalar` |
| **数据类型:** | `double` |

### **初始电池容量, BattCapInit** — 容量 `100`（默认） | `scalar`

初始电池容量，*Capbatt*，单位为 Ah。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `BattCapInit` |
| **值:** | `100`（默认） | `scalar` |
| **数据类型:** | `double` |

#### 依赖关系

| 模块参数 **初始电池容量** 选项 | 创建 |
| --- | --- |
| `External Input` | 输入端口 `CapInit` |
| `Parameter` | 参数 **初始电池容量, BattCapInit** |

### **输出电池电压时间常数, Tc** — 滤波器时间常数 `1/1000`（默认） | `scalar`

输出电池电压时间常数，*Tc*，单位为 s。用于一阶电压滤波器。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Tc` |
| **值:** | `-1`（默认） | `scalar` |
| **数据类型:** | `double` |

#### 依赖关系

将 **输出电池电压** 参数设置为 `Filtered` 会创建以下参数：

- **输出电池电压时间常数, Tc**
- **输出电池电压初始值, Vinit**

### **输出电池电压初始值, Vinit** — 滤波器初始电压 `4.221`（默认） | `scalar`

输出电池电压初始值，*Vinit*，单位为 V。用于一阶电压滤波器。

#### 程序化使用

要以程序方式设置模块参数值，请使用 `set_param` 函数。

要以程序方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Vinit` |
| **值:** | `-1`（默认） | `scalar` |
| **数据类型:** | `double` |

#### 依赖关系

将 **输出电池电压** 参数设置为 `Filtered` 会创建以下参数：

- **输出电池电压时间常数, Tc**
- **输出电池电压初始值, Vinit**

## 所属库

Powertrain Blockset / Energy Storage and Auxiliary Drive / Datasheet Battery

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017a 中引入**

### R2025a：参数名称和描述变更

R2025a 包含以下 Datasheet Battery 模块参数名称和描述变更。更新后的名称和描述说明了其功能。

| 参数 | | R2025a 更新 | |
| --- | --- | --- | --- |
| 名称 | 描述 | 名称 | 描述 |
| `Em` | **开路电压表数据** | `Em` | **每节电池的开路电压** |
| `RInt` | **内阻表数据** | `RInt` | **每节电池的内阻** |
| `BattTempBp` | **电池温度断点 1** | `BattTempBp` | **电池温度断点** |
| `CapLUTBp` | **开路电压断点 1** | `SOCEmBp` | **用于开路电压的荷电状态断点** |
| `CapSOCBp` | **电池容量断点 2** | `SOCRintBp` | **用于内阻的荷电状态断点** |

## 描述

锂离子、锂聚合物或铅酸电池

Datasheet Battery 模块实现锂离子、锂聚合物或铅酸电池，您可以使用制造商数据对其进行参数化。为了创建模块所需的开路电压和内阻参数，请使用制造商按温度提供的放电特性数据。有关示例，请参阅 Generate Parameter Data for Datasheet Battery Block。

为了确定电池输出电压，模块使用电池开路电压和内阻的查找表。这些查找表是荷电状态 (SOC) 和电池温度的函数，用于表征电池在各种工作点下的性能：

Em=f(SOC)Rint=f(T,SOC)

为了计算电压，模块实现以下方程。

VT=Em−IbattRintIbatt=IinNpVout={NsVT     unfilteredVoutτs+1          filteredSOC=SOCo−1Capbatt∫0tIbattdtLdAmpHr=∫0tIbattdt

正电流表示电池放电。负电流表示电池充电。

### 功率核算

对于功率核算，模块实现以下方程。

| 总线信号 | | | 描述 | 方程 |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — 模块之间传输的功率  - 正信号表示流入模块 - 负信号表示流出模块 | `PwrLdBatt` | 电池网络功率 | Vbatt=Vout   OR  Voutτs+1Pbatt=−VbattIbattPLdBatt= −Pbatt |
| `PwrNotTrnsfrd` — 穿过模块边界但未传输的功率  - 正信号表示输入 - 负信号表示损耗 | `PwrLossBatt` | 电池网络功率损耗 | PLossBatt=−NpNsIbatt2Rint |
| `PwrStored` — 存储能量的变化率  - 正信号表示增加 - 负信号表示减少 | `PwrStoredBatt` | 电池网络存储功率 | PStoredBatt=PBatt+PLossBatt |

方程使用以下变量。

|  |  |
| --- | --- |
| *SOC* | 荷电状态 |
| *SOCo* | 初始荷电状态 |
| *Em* | 电池开路电压 |
| *Ibatt* | 每个模块的电池电流 |
| *PLdBatt* | 电池网络功率 |
| *Pbatt* | 电池功率 |
| *PLossBatt* | 电池网络功率损耗 |
| *PStoredBatt* | 电池网络存储功率 |
| *Iin* | 从电池网络流出的总电流 |
| *Rint* | 电池内阻 |
| *Ns* | 串联电池单元数 |
| *Np* | 并联电池单元数 |
| *Vout*, *Vbatt* | 电池网络的总电压 |
| *VT* | 每个模块的电池电压 |
| *Capbatt* | 电池容量 |
| *LdAmpHr* | 电池能量 |
