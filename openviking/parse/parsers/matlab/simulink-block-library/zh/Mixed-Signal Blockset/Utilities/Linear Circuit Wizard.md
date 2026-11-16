---
type: simulink-block
title: 'Linear Circuit Wizard'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'linearcircuitwizard'
documentation_source_path: 'ref/linearcircuitwizard.html'
language: zh-CN
chinese_source: worker-translation
---

# Linear Circuit Wizard

## 端口

在 R2025b 中未记录。

## 参数

### 电路定义

### **电路设计名称** — 显示在模块图标上的电路名称 `'Linear Circuit'`（默认） | character vector | string scalar

显示在模块图标上的电路名称，指定为 character vector 或 string scalar。

#### 编程用法

|  |
| --- |
| **模块参数：** `CircuitDesignName` |
| **类型：** character vector |
| **值：** character string |
| **默认值：** `'Linear Circuit'` |

### **模块名称** — 显示在模块图标下的实例名称 `'Linear Circuit'`（默认） | character vector | string scalar

显示在模块图标下的实例名称，指定为 character vector 或 string scalar。

#### 编程用法

|  |
| --- |
| **模块参数：** `BlockName` |
| **类型：** character vector |
| **值：** character string |
| **默认值：** `'Linear Circuit'` |

### **网表文件名** — 定义电路的网表文件名 character vector | string scalar

定义线性电路的网表文件（SPICE 语法）的名称，指定为 character vector 或 string scalar。

#### 编程用法

|  |
| --- |
| **模块参数：** `NetlistFileName` |
| **类型：** character vector |
| **值：** character string |

### **配置名称** — 配置文件名 character vector | string scalar

配置文件的名称，指定为 character vector 或 string scalar。您可以将当前配置保存到文件。

#### 编程用法

|  |
| --- |
| **模块参数：** `ConfigurationName` |
| **类型：** character vector |
| **值：** character string |

### **解析网表文件并启动新配置** — 解析指定的网表文件按钮

单击以解析指定的网表文件。此操作会根据新的 SPICE 语法重新定义现有端口。有关详细信息，请参阅根据 SPICE 网表对线性电路响应建模。

### **保存配置** — 将当前配置保存到文件按钮

单击以将当前电路配置保存到其名称在 **配置名称** 中指定的文件。

### **加载配置** — 加载现有配置文件按钮

单击以从名称在 **配置名称** 参数中指定的文件加载当前电路配置。

### **将配置附加到模块** — 将所选配置文件附加到 Simulink 模块 on（默认） | off

选择此项可在 Linear Circuit Wizard 模块构建 Simulink 模块时将所选配置文件附加到该 Simulink 模块。

### **构建 Simulink 模块** — 创建 Simulink 模块或对象以对网表定义的电路建模按钮

单击以创建 Simulink 模块或对象，以对 SPICE 网表定义的电路建模。

如果已为电路定义开关状态，则构建的模块将是开关电路模块。否则，它将是线性电路模块。

### 线性分析

### **极点/零点报告** — 将极点-零点报告添加到基础工作区 on（默认） | off

选择此项可在分析线性电路时将包含极点-零点报告的结构体添加到基础工作区。

### **传递函数图** — 绘制传递函数 on（默认） | off

选择此项可在分析线性电路时绘制线性电路的所有传递函数。

### **线性控制系统** — 将控制系统微分方程的矩阵添加到基础工作区 on（默认） | off

选择此项可在分析线性电路时将包含控制系统微分方程矩阵的结构体添加到基础工作区。

### **分析** — 分析线性电路以产生所选输出按钮

单击以分析线性电路并产生所选输出。

### 工作点分析

### **输出端口** — 主输出值的 Outport 端口下拉菜单，由端口定义创建

从下拉菜单中选择主输出值的输出端口。在您解析网表以定义端口之前，该下拉菜单保持为空。

### **稳态输出值** — 期望的主输出值 `0`（默认） | `scalar` | `vector`

期望的主输出值，指定为 scalar 或 vector。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputValues` |
| **类型：** character vector |
| **值：** scalar | vector |
| **默认值：** `0` |

### **主控制变量** — 用于调节输出的变量 **Duty cycle**（默认） | **Frequency**

模块用于调节输出的变量。在 **Duty Cycle** 或 **Frequency** 之间选择。

#### 编程用法

|  |
| --- |
| **模块参数：** `ControlVariable` |
| **类型：** character vector |
| **值：** **Duty cycle** | **Frequency** |
| **默认值：** **Duty cycle** |

### **占空比值 [min,max]** — 最小控制占空比 `0`（默认） | scalar | 2-element vector

控制占空比，定义在从 0 到 1 的标度上。您可以指定一个 scalar 以应用于所有分析，也可以将控制占空比范围的最小值和最大值指定为 2-element vector，从而生成输出值作为控制占空比函数的图。

#### 编程用法

|  |
| --- |
| **模块参数：** `DutyCycle` |
| **类型：** character vector |
| **值：** scalar | 2-element vector |
| **默认值：** `0` |

### **频率 [min,max]** — 最小控制频率 `0`（默认） | scalar | 2-element vector

控制信号频率。您可以指定一个 scalar 以应用于所有分析，也可以将频率范围的最小值和最大值指定为 2-element vector，从而生成输出值作为控制信号频率函数的图。

#### 编程用法

|  |
| --- |
| **模块参数：** `Frequency` |
| **类型：** character vector |
| **值：** scalar | 2-element vector |
| **默认值：** `0` |

### **相位偏移** — 控制信号上升沿相位占控制周期的比例 `0`（默认） | scalar | vector

控制信号上升沿的相位占控制周期（0,1）的比例，指定为 scalar（单个控制信号）或 vector（多个控制信号）。

您可以使用变量 *d* 表示控制占空比，或使用 *f* 表示开关频率。

#### 编程用法

|  |
| --- |
| **模块参数：** `PhaseOffsets` |
| **类型：** character vector |
| **值：** scalar | vector |
| **默认值：** `0` |

### **脉冲持续时间** — 控制信号脉冲持续时间作为控制周期的函数 `0`（默认） | scalar | vector

控制信号脉冲持续时间作为控制周期（0,1）的函数，指定为 scalar（单个控制信号）或 vector（多个控制信号）。

您可以使用变量 *d* 表示控制占空比，或使用 *f* 表示开关频率。

#### 编程用法

|  |
| --- |
| **模块参数：** `PulseDuration` |
| **类型：** character vector |
| **值：** scalar | vector |
| **默认值：** `0` |

### **每波形采样数** — 单个开关周期输出波中的样本数 `1024`（默认） | positive integer scalar

单个稳态开关周期输出波中的样本数，指定为 positive integer scalar。

#### 编程用法

|  |
| --- |
| **模块参数：** `WaveSamples` |
| **类型：** character vector |
| **值：** scalar |
| **默认值：** `1024` |

### **分析工作点** — 开关电路的工作点分析按钮

单击以执行开关电路的开关模式功率级工作点分析。

## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

### R2025a：开关电路的调试模式

您可以为开关电路激活调试模式，以在时域仿真期间记录电路中所有节点在指定时间间隔内的波形。您还可以为 Switched Circuit 模块中的节点设置初始条件。

## 描述

生成或修改线性电路

使用 Linear Circuit Wizard 模块创建或修改线性时不变电路，例如定制设计的滤波器或带有提取寄生参数的电路。使用此模块，您可以解析描述电路元件和电路节点的 SPICE 网表文件。然后，您可以使用模块参数对话框优化输入和输出端口，并对器件噪声建模。您可以从基础工作区输出结构体查看端口和器件噪声定义。

Linear Circuit Wizard 模块建立并求解线性电路方程，以生成一组 Laplace 域传递函数。您可以通过幅值-频率图或极点-零点位置报告查看这些传递函数。

Linear Circuit Wizard 模块创建并配置一个 MATLAB System 模块，以将您的电路表示为 Simulink® 模型中的一个新模块，该模块独立于 Linear Circuit Wizard 模块。此 MATLAB System 模块使用端口和器件噪声定义以及电路分析结果进行配置。当您启动仿真时，MATLAB System 模块使用固定步长离散采样时间将 Laplace 域传递函数转换为递归数字滤波器系数，以便在仿真期间执行。

Linear Circuit Wizard 模块可以生成：

- 一个线性电路模块，
- 一个开关电路模块，
- 或一个 Control System Toolbox™ 可调对象。
