---
type: simulink-block
title: 'Operational Amplifier'
family: 'utilities'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'operationalamplifier'
documentation_source_path: 'ref/operationalamplifier.html'
language: zh-CN
chinese_source: worker-translation
---

# Operational Amplifier

## 端口

### 输入

### **InP** — 正输入端子标量

运算放大器的正输入端子。

**数据类型：** `single` | `double`

### **InN** — 负输入端子标量

运算放大器的负输入端子。

**数据类型：** `single` | `double`
### 输出

### **OutP** — 正输出端子标量

运算放大器的正输出端子。

**数据类型：** `single` | `double`

### **OutN** — 负输出端子标量

运算放大器的负输出端子。

**数据类型：** `single` | `double`

## 参数

### **运算放大器电路** — 运算放大器电路的类型 `Double-pole Circuit` (default) | `Multipole Circuit`

运算放大器电路的类型。

- `Double-pole Circuit` — 使用诸如开环增益、单位增益带宽、最大尾电流和压摆率等电路参数来定义简单的双极点电路。
- `Multipole Circuit` — 使用传递函数极点和零点来定义多极点电路。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OpampType` |
| **类型：** character vector |
| **值：** `Double-pole Circuit`| `Multipole Circuit` |
| **默认：** `Double-pole Circuit` |

### **从输入继承采样间隔** — 从输入继承采样间隔 off (default) | on

从输入继承采样间隔值。默认情况下，此选项处于未选中状态。

### **采样间隔 (s)** — 在 MATLAB 分析中使用的采样间隔值 `1e-8` (default) | scalar

模块在 MATLAB® 分析中使用的采样间隔值，指定为 scalar，单位为 seconds。

#### 依赖关系

要启用此参数，请取消选中 **从输入继承采样间隔** 选项。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleInterval` |
| **类型：** character vector |
| **值：** scalar |
| **默认：** `1e-8` |

### **模拟方式** — 选择模拟模式 `Code generation` (default) | `Interpreted execution`

选择模拟模式。您选择的此选项会影响模拟性能。

使用 `Code generation` 方法模拟模型需要额外的启动时间，但后续模拟运行得更快。使用 `Interpreted execution` 方法模拟模型可能会减少启动时间，但后续模拟运行得更慢。有关详细信息，请参阅 Interpreted Execution vs. Code Generation。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** character vector |
| **值：** `Code generation`| `Interpreted execution` |
| **默认：** `Code generation` |

### 信号参数

### **电源轨高 (V)** — 最大电源电压 `5` (default) | real scalar

提供给 Operational Amplifier 模块的最大电源电压，指定为 real scalar，单位为 volts。

#### 程序化使用

|  |
| --- |
| **模块参数：** `VoltageSupplyPlus` |
| **类型：** character vector |
| **值：** real scalar |
| **默认：** `5` |

### **电源轨低 (V)** — 最小电源电压 `-5` (default) | real scalar

提供给 Operational Amplifier 模块的最小电源电压，指定为 real scalar，单位为 volts。

#### 程序化使用

|  |
| --- |
| **模块参数：** `VoltageSupplyMinus` |
| **类型：** character vector |
| **值：** real scalar |
| **默认：** `-5` |

### **输入失调电压 (V)** — 输入端子处的失调电压 `0` (default) | scalar

运算放大器输入端子处的失调电压，指定为 scalar，单位为 volts。该模块使用此值在运算放大器的输出端子处获得零电压。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputOffsetVoltage` |
| **类型：** character vector |
| **值：** scalar |
| **默认：** `0` |

### 高级参数

### **开环增益 (V/V)** — 无反馈时的运算放大器增益 `3e3` (default) | positive real scalar

无任何正反馈或负反馈时运算放大器的增益，指定为 unitless positive real scalar。

#### 依赖关系

要启用此参数，请将 **运算放大器电路** 设置为 `Double Pole Circuit`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Gain` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认：** `3e3` |

### **单位增益带宽 (Hz)** — 运算放大器增益等于单位增益时的频率 `10e6` (default) | positive real scalar

运算放大器的开环增益变为单位增益时的频率，指定为 positive real scalar，单位为 hertz。

#### 依赖关系

要启用此参数，请将 **运算放大器电路** 设置为 `Double Pole Circuit`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `FrequencyUnityGain` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认：** `10e6` |

### **最大尾电流 (A)** — 运算放大器电路中通过尾 MOSFET 的最大电流 `100e-6` (default) | positive real scalar

运算放大器电路中通过尾 MOSFET（金属氧化物半导体场效应晶体管）的电流最大值，指定为 positive real scalar，单位为 amperes。

#### 依赖关系

要启用此参数，请将 **运算放大器电路** 设置为 `Double Pole Circuit`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InputCurrentMax` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认：** `100e-6` |

### **压摆率 (V/s)** — 运算放大器输出电压的变化率 `10e6` (default) | positive real scalar

运算放大器输出电压相对于时间的变化率，指定为 positive real scalar。

#### 依赖关系

要启用此参数，请将 **运算放大器电路** 设置为 `Double Pole Circuit`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SlewRate` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认：** `10e6` |

### **输出电阻 (Ohms)** — 输出端子处的电阻 `10e3` (default) | positive real scalar

运算放大器输出端子处的电阻，指定为 positive real scalar，单位为 ohms。

#### 依赖关系

要启用此参数，请将 **运算放大器电路** 设置为 `Double Pole Circuit`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputResistance` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认：** `10e3` |

### **输出电容 (F)** — 输出端子处的电容 `50e-12` (default) | positive real scalar

运算放大器输出端子处的电容，指定为 positive real scalar，单位为 farads。

#### 依赖关系

要启用此参数，请将 **运算放大器电路** 设置为 `Double Pole Circuit`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputCapacitance` |
| **类型：** character vector |
| **值：** positive real scalar |
| **默认：** `50e-12` |

### **传递函数极点** — Laplace 域中传递函数的极点 `[-2.09e+04 -8.62e+07]` (default) | column vector

运算放大器在 Laplace 域中传递函数的极点，指定为 column vector，单位为 rad/s。

如果将 **运算放大器电路** 设置为 `Double-pole Circuit`，则该模块会根据电路参数自动为您计算极点。如果将 **运算放大器电路** 设置为 `Multipole Circuit`，则可以指定极点。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Poles` |
| **类型：** character vector |
| **值：** column vector |
| **默认：** `[-2.09e+04 -8.62e+07]` |

### **传递函数零点** — Laplace 域中传递函数的零点 `[-9.14e+07]` (default) | column vector

运算放大器在 Laplace 域中传递函数的零点，指定为 column vector，单位为 rad/s。

如果将 **运算放大器电路** 设置为 `Double-pole Circuit`，则该模块会根据电路参数自动为您计算零点。如果将 **运算放大器电路** 设置为 `Multipole Circuit`，则可以指定零点。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Zeros` |
| **类型：** character vector |
| **值：** column vector |
| **默认：** `[-9.14e+07]` |

### 分析

### **包含 Z 域近似** — 在绘制开环响应时包含 *z* 域近似 off (default) | on

在绘制运算放大器的开环响应时，除 *s* 域传递函数外，还包含 *z* 域（离散时间）近似。

### **绘制开环响应** — 绘制运算放大器开环响应的按钮

绘制运算放大器开环响应的 *s* 域传递函数。该图还报告单位增益带宽和相位裕度。您可以选择包含 *z* 域近似。

## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021b 中引入**

### R2024a：绘制开环响应

现在可以绘制运算放大器的开环响应以及 *z* 域近似。

## 描述

对具有两个或更多极点的运算放大器进行建模

使用 Operational Amplifier 模块对具有两个或更多极点的运算放大器进行建模。您可以根据重要的电路参数创建双极点放大器，或根据传递函数创建多极点放大器。使用该模块可在更大的电路系统中表征运算放大器的性能。
