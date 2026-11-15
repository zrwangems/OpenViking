---
type: simulink-block
title: 'Simple Engine'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Propulsion / Internal Combustion Engines, Components, and Controllers / Engines and Controllers'
documentation_page: 'simpleengine'
documentation_source_path: 'ref/simpleengine.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Engine

## 端口

### 输入

### **TrqCmd** — 指令扭矩 `scalar`

扭矩，单位为 N·m。

### **EngSpd** — 发动机转速 `scalar`

发动机转速，单位为 rpm。
### 输出

### **Info** — 总线信号 bus

包含这些模块计算的总线信号。

| 信号 | | | 描述 | 单位 |
| --- | --- | --- | --- | --- |
| `IntkGasMassFlw` (有意置零) | | | 发动机空气质量流量输出 | kg/s |
| `NrmlzdAirChrg` (有意置零) | | | 归一化发动机气缸空气质量 | N/A |
| `Afr` (有意置零) | | | 空燃比 (AFR) | N/A |
| `FuelMassFlw` | | | 发动机燃油流量输出 | kg/s |
| `FuelVolFlw` | | | 体积燃油流量 | m3/s |
| `ExhManGasTemp` (有意置零) | | | 发动机排气温度 | K |
| `EngTrq` | | | 发动机扭矩输出 | N·m |
| `EngSpd` | | | 发动机转速 | rpm |
| `CrkAng` (有意置零) | | | 发动机曲轴绝对角度  ∫0(360)CpsEngSpd18030dθ  其中 Cps 是每动力冲程的曲轴转数。 | deg |
| `Bsfc` | | | 发动机制动比油耗 (BSFC) | g/kWh |
| `EoHC` (有意置零) | | | 发动机出口碳氢化合物排放质量流量 | kg/s |
| `EoCO` (有意置零) | | | 发动机出口一氧化碳排放质量流量 | kg/s |
| `EoNOx` (有意置零) | | | 发动机出口一氧化氮和二氧化氮排放质量流量 | kg/s |
| `EoCO2` (有意置零) | | | 发动机出口二氧化碳排放质量流量 | kg/s |
| `EoPM` (有意置零) | | | 发动机出口颗粒物排放质量流量 | kg/s |
| `PwrInfo` | `PwrTrnsfrd` | `PwrCrkshft` | 曲轴功率 | W |
| `PwrNotTrnsfrd` | `PwrFuel` | 燃料输入功率 | W |
| `PwrLoss` | 功率损失 | W |
| `PwrStored` | | *未使用* | |

### **EngTrq** — 发动机制动扭矩 `scalar`

发动机制动扭矩，单位为 N·m。

## 参数

### **发动机最大扭矩, f\_tqmax** — 断点 `[75.679776480773256 75.679776480773256 97.173658538143172 116.84042599160529 152.21029882684542 175 174.99889520597083 174.99996520122858 175 175 175 175 175 175 175 175]` (默认) | `vector`

断点，单位为 N·m。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqmax` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **发动机转速输入的断点, f\_tqmax\_n\_bpt** — 断点 `[0 750 1053.57142857143 1357.14285714286 1660.71428571429 1964.28571428571 2267.85714285714 2571.42857142857 2875 3178.57142857143 3482.14285714286 3785.71428571429 4089.28571428571 4392.85714285714 4696.42857142857 5000]` (默认) | `vector`

断点，单位为 rpm。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `f_tqmax_n_bpt` |
| **值：** | `vector` |
| **数据类型：** | `double` |

### **燃料低热值, Lhv** — 热值 `4.6E+7` (默认) | `scalar`

燃料低热值，单位为 J/kg。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Lhv` |
| **值：** | `4.6E+7` (默认) | `scalar` |
| **数据类型：** | `double` |

### **燃料比重, Sg** — 比重 `0.745` (默认) | `scalar`

燃料的比重，无量纲。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `Sg` |
| **值：** | `0.745` (默认) | `scalar` |
| **数据类型：** | `double` |

### **平均制动比油耗, BsfcAvg** — 平均制动比油耗 `350` (默认) | `scalar`

平均制动比油耗，单位为 g/kwh。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` 函数。

要以编程方式获取模块参数值，请使用
`get_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `BsfcAvg` |
| **值：** | `350` (默认) | `scalar` |
| **数据类型：** | `double` |

## 所属库

Powertrain Blockset / Propulsion / Combustion Engines Vehicle Dynamics Blockset / Powertrain / Propulsion

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

使用查找表的简化发动机模型

Simple Engine 模块实现了一个简化发动机模型，使用最大扭矩与发动机转速表、两个标量燃料质量属性和一个标量发动机效率参数来估计发动机扭矩和燃油流量。可以将该模块用于：

- 硬件在环 (HIL) 发动机控制设计
- 车辆级燃油经济性和性能仿真
