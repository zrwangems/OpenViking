---
type: simulink-block
title: 'Baseband PLL'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'PLL / Architectures'
documentation_page: 'basebandpll'
documentation_source_path: 'ref/basebandpll.html'
language: zh-CN
chinese_source: worker-translation
---

# Baseband PLL

## 端口

### 输入

### **In** — 来自基带 VCO 的输入信号 标量

输入信号，指定为标量。该输入信号是基带 VCO 在相位域中的输出。

**数据类型：** `double`
### 输出

### **Filt** — 环路滤波器输出 标量

环路滤波器在相位域中的输出，以标量形式返回。

**数据类型：** `double`

### **PD** — 鉴相器输出 标量

鉴相器在相位域中的输出，以标量形式返回。

**数据类型：** `double`

### **VCO** — VCO 输出 标量

VCO 在相位域中的输出，以标量形式返回。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### **Loop filter type** — 确定如何定义环路滤波器 `Transfer function`（默认）| `2nd order passive` | `3rd order passive` | `4th order passive`

确定如何定义环路滤波器。您可以定义二阶至四阶的无源环路滤波器，也可以使用传递函数来表示环路滤波器。

如果要定义无源环路滤波器，则必须定义 PLL 系统的**Charge pump current (A)**、**Min clock divider value**、**Loop bandwidth (Hz)** 和 **Phase margin (degrees)**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Ftype` |
| **类型：** `double` |
| **值：** `Transfer function` | `2nd order passive` | `3rd order passive` | `4th order passive` |
| **默认值：** `Transfer function` |

### **VCO input sensitivity (Hz/V)** — VCO 输出频率的变化量度量 `100e6`（默认）| 正实数标量

输入电压变化引起的输出频率变化量度量，指定为正实数标量，单位为 Hz/V。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Kvco` |
| **类型：** `double` |
| **值：** 正实数标量 |
| **默认值：** `100e6` |

### **Charge pump current (A)** — 电荷泵输出电流 `5e3`（默认）| 正实数标量

电荷泵输出电流的满量程幅值，指定为正实数标量，单位为安培。

#### 依赖关系

要启用此参数，请将 **Loop filter type** 设置为 `2nd order passive`、`3rd order passive` 或 `4th order passive`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Icp` |
| **类型：** `double` |
| **值：** 正实数标量 |
| **默认值：** `5e3` |

### **Min clock divider value** — 时钟分频器可对输入频率进行分频的最小值 `100`（默认）| 正实数标量

时钟分频器可对输入频率进行分频的最小值，指定为正实数标量。

#### 依赖关系

要启用此参数，请将 **Loop filter type** 设置为 `2nd order passive`、`3rd order passive` 或 `4th order passive`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Nmin` |
| **类型：** `double` |
| **值：** 正实数标量 |
| **默认值：** `100` |

### **Loop bandwidth (Hz)** — 开环传递函数幅值变为 1 时的频率 `50e3`（默认）| 正实数标量

开环传递函数幅值变为 1 时的频率，指定为正实数标量，单位为 Hz。较低的 Loop bandwidth (Hz) 值会降低相位噪声和参考杂散，但代价是更长的锁定时间和更小的相位裕度。

#### 依赖关系

要启用此参数，请将 **Loop filter type** 设置为 `2nd order passive`、`3rd order passive` 或 `4th order passive`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Fc` |
| **类型：** `double` |
| **值：** 正实数标量 |
| **默认值：** `50e3` |

### **相位裕度（度）** — 环路带宽处开环传递函数的相位与 180° 之差 `45`（默认）| 正实数标量

环路带宽处开环传递函数的相位与 180° 之差，指定为以度为单位的正实数标量。为实现最佳锁定时间，请选择 40° 至 55° 之间的相位裕度。

#### 依赖关系

要启用此参数，请将 **环路滤波器类型** 设置为
`2nd order passive`、`3rd order
passive` 或 `4th order passive`。

#### 编程使用

|  |
| --- |
| **模块参数：** `phi` |
| **类型：** `double` |
| **值：** 正实数标量 |
| **默认值：** `45` |

### **分子** — 环路滤波器传递函数的分子 `[1.9212e-10, 5e-05]`（默认）| 实数标量 | 实数值向量

环路滤波器传递函数的分子。如果您定义的是无源环路滤波器，此值会自动为您计算。如果您使用传递函数表示环路滤波器，也可以手动更改它。

#### 依赖关系

要编辑此参数，请将 **环路滤波器类型** 设置为
`Transfer function`。

#### 编程使用

|  |
| --- |
| **模块参数：** `Fn` |
| **类型：** `double` |
| **值：** 实数标量 | 实数值标量 |
| **默认值：** `[1.9212e-10, 5e-05]` |

### **分母** — 环路滤波器传递函数的分母 `[2.0157e-15, 3.0576e-09, 0]`（默认）| 实数值向量

环路滤波器传递函数的分母。如果您定义的是无源环路滤波器，此值会自动为您计算。如果您使用传递函数表示环路滤波器，也可以手动更改它。

#### 依赖关系

要编辑此参数，请将 **环路滤波器类型** 设置为
`Transfer function`。

#### 编程使用

|  |
| --- |
| **模块参数：** `Fd` |
| **类型：** `double` |
| **值：** 实数值向量 |
| **默认值：** `[2.0157e-15, 3.0576e-09, 0]` |

### **开环分析** — 绘制开环预仿真分析 on（默认）| off

选择此项可在仿真前绘制 PLL 系统的增益裕度和相位裕度。默认情况下，此选项处于选中状态。

### **闭环分析** — 绘制闭环预仿真分析 on（默认）| off

选择此项可在仿真前绘制 PLL 系统的零极点图、环路带宽、阶跃响应和冲激响应。您必须拥有 Control System Toolbox™ 许可证才能绘制 PLL 系统的阶跃响应和冲激响应。默认情况下，此选项处于选中状态。

### **绘制环路动态** — 绘制 PLL 系统的环路动态 按钮

点击以绘制 PLL 系统的预仿真环路动态。

## 所属库

Mixed-Signal Blockset / PLL / Architectures

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

PLL 的相位域模型

Baseband PLL 模块在相位域中对 PLL 进行建模。该模块接受实数值相位偏移向量，并产生环路滤波器、鉴相器和 VCO 的输出。该模块作为反馈控制系统，自动调整本地生成信号的相位以匹配输入信号的相位。
