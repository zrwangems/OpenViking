---
type: simulink-block
title: 'Extremum Seeking Control'
family: 'slcontrol'
product_id: 'slcontrol'
product_name: 'Simulink Control Design'
documentation_release: R2025b
official_category: 'Adaptive Control'
documentation_page: 'extremumseekingcontrol'
documentation_source_path: 'ug/extremumseekingcontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# Extremum Seeking Control

## 端口
```yaml
ports:
- name: J
  summary: 目标函数标量
  direction: input
- name: theta
  summary: 扰动参数标量 | 向量
  direction: output
- name: theta_hat
  summary: 估计参数标量 | 向量
  direction: output
```

### 输入

### **J** — 目标函数标量

来自控制系统的目标函数因系统对扰动参数 **theta** 的响应而受到扰动。为计算参数更新，该模块对 **J** 进行滤波和解调。

### 输出

### **theta** — 扰动参数标量 | 向量

将这些扰动参数（*θ*）应用于您的控制系统。该模块使用目标函数 **J** 的由此产生的扰动来计算参数更新。

如果 **Number of parameters** 为 `1`，则 **theta** 输出标量信号。否则，**theta** 输出长度等于 **Number of parameters** 的向量信号。

### **theta\_hat** — 估计参数标量 | 向量

使用此输出端口可获取在受到调制信号扰动之前的估计参数值（θ^）。

如果 **Number of parameters** 为 `1`，则 **theta\_hat** 输出标量信号。否则，**theta\_hat** 输出长度等于 **Number of parameters** 的向量信号。

#### 依赖关系

要启用此输出端口，请选择 **Output estimated parameters**。
## 参数
```yaml
parameters:
- name: Time Domain
  summary: 滤波器和积分器时域 Continuous time（默认）| Discrete time
  group: ''
  block_parameter: '''timeDomainStatus'''
  type: 字符向量
  values: '''Continuous Time'' | ''Discrete Time'''
  default: '''Continuous Time'''
- name: Sample time
  summary: 离散时间滤波器和积分器采样时间 0.1（默认）| 有限正标量
  group: ''
  block_parameter: '''SampleTime'''
  type: 字符向量
  values: 有限正标量
  default: '''0.1'''
- name: Integrator method
  summary: 离散时间积分方法 Forward Euler（默认）| Backward Euler | Trapezoidal
  group: ''
  block_parameter: '''IntegratorMethods'''
  type: 字符向量
  values: '''Forward Euler'' | ''Backward Euler'' | ''Trapezoidal'''
  default: '''Forward Euler'''
- name: Number of parameters
  summary: 参数数量 1（默认）| 小于或等于 5 的正整数
  group: ''
  block_parameter: '''paramCount'''
  type: 字符向量
  values: 小于 5 的正整数
  default: '''1'''
- name: Initial condition x0
  summary: 初始参数值 0（默认）| 有限标量 | 向量
  group: ''
  block_parameter: '''initialVal'''
  type: 字符向量
  values: 有限标量 | 向量
- name: Forcing frequency omega (rad/s)
  summary: 强迫频率 1（默认）| 正有限标量 | 向量
  group: ''
  block_parameter: '''omega'''
  type: 字符向量
  values: 正有限标量 | 向量
- name: Learning rate k
  summary: 参数更新速率 1（默认）| 正有限标量 | 向量
  group: ''
  block_parameter: '''gain'''
  type: 字符向量
  values: 正有限标量 | 向量
- name: Demodulation amplitude a
  summary: 解调信号幅值 1（默认）| 正有限标量 | 向量
  group: ''
  block_parameter: '''demodAmp'''
  type: 字符向量
- name: 解调相位 phi_1 (rad)
  summary: 解调信号相位 0（默认）| 正有限标量 | 向量
  group: ''
  block_parameter: '''demodPhase'''
  type: 字符向量
  values: 正有限标量 | 向量
- name: 调制幅值 b
  summary: 调制信号幅值 0.1（默认）| 正有限标量 | 向量
  group: ''
  block_parameter: '''modAmp'''
  type: 字符向量
  values: 正有限标量 | 向量
- name: 调制相位 phi_2 (rad)
  summary: 调制信号相位 0（默认）| 正有限标量 | 向量
  group: ''
  block_parameter: '''modPhase'''
  type: 字符向量
  values: 正有限标量 | 向量
- name: 启用 HPF
  summary: 启用目标函数信号的高通滤波 off（默认）| on
  group: ''
  block_parameter: '''highPassEnable'''
  type: 字符向量
  values: '''off'' | ''on'''
- name: HPF frequency omega_h (rad/s)
  summary: 高通滤波器截止频率 1（默认）| 正有限标量 | 向量
  group: ''
  block_parameter: '''highPassCutoff'''
  type: 字符向量
  values: 正有限标量 | 向量
  default: '''1'''
- name: Enable LPF
  summary: 启用解调信号的低通滤波 off（默认）| on
  group: ''
  block_parameter: '''lowPassEnable'''
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
- name: LPF frequency omega_l (rad/s)
  summary: 低通滤波器截止频率 *ωl* 1（默认）| 正有限标量 | 向量
  group: ''
  block_parameter: '''lowPassCutoff'''
  type: 字符向量
  values: 正有限标量 | 向量
  default: '''1'''
- name: Output estimated parameters
  summary: 添加估计参数输出端口 off（默认）| on
  group: ''
  block_parameter: estimatedVarOn
  type: 字符向量
  values: '''off'' | ''on'''
  default: '''off'''
```

### **Time Domain** — 滤波器和积分器时域 **Continuous time**（默认）| **Discrete time**

指定高通滤波器、低通滤波器和积分器的时域。

- **Continuous time** — 使用连续时间滤波器和积分器。
- **Discrete time** — 使用离散时间滤波器和积分器。使用 **Sample time** 参数指定采样时间，使用 **Integration method** 参数指定积分方法。

#### 编程用法

|  |
| --- |
| **模块参数：** `'timeDomainStatus'` |
| **类型：** 字符向量 |
| **值：** `'Continuous Time'` | `'Discrete Time'` |
| **默认值：** `'Continuous Time'` |

### **Sample time** — 离散时间滤波器和积分器采样时间 `0.1`（默认）| 有限正标量

指定离散时间高通滤波器、低通滤波器和积分器的采样时间。

在调节多个参数时，所有调节回路使用相同的采样时间。

#### 依赖关系

要启用此参数，请将 **Time Domain** 属性设置为 **Discrete time**。

#### 编程用法

|  |
| --- |
| **模块参数：** `'SampleTime'` |
| **类型：** 字符向量 |
| **值：** 有限正标量 |
| **默认值：** `'0.1'` |

### **Integrator method** — 离散时间积分方法 `Forward Euler`（默认）| `Backward Euler` | `Trapezoidal`

您可以为离散时间积分器选择以下积分方法之一。

- `Forward Euler`：

  y(n)=y(n−1)+Ts⋅u(n−1)
- `Backward Euler`：

  y(n)=y(n−1)+Ts⋅u(n)
- `Trapezoidal`：

  y(n)=y(n−1)+Ts⋅[u(n)+u(n−1)]/2

其中：

- *y* 是积分器输出
- *u* 是输入
- *n* 是当前采样时间
- *Ts* 是采样时间

在调节多个参数时，所有调节回路中的积分器使用相同的积分方法。

#### 依赖关系

要启用此参数，请将 **Time Domain** 属性设置为 **Discrete time**。

#### 编程用法

|  |
| --- |
| **模块参数：** `'IntegratorMethods'` |
| **类型：** 字符向量 |
| **值：** `'Forward Euler'` | `'Backward Euler'` | `'Trapezoidal'` |
| **默认值：** `'Forward Euler'` |

### **Number of parameters** — 参数数量 `1`（默认）| 小于或等于 5 的正整数

您可以同时调节最多五个参数。该模块为每个参数使用单独的调节回路。

#### 编程用法

|  |
| --- |
| **模块参数：** `'paramCount'` |
| **类型：** 字符向量 |
| **值：** 小于 5 的正整数 |
| **默认值：** `'1'` |

### **Initial condition x0** — 初始参数值 `0`（默认）| 有限标量 | 向量

初始参数值，对应于参数更新积分器的初始条件。

如果 **Number of parameters** 为 `1`，将 **Initial condition** 指定为有限标量。

要为多个参数指定不同的初始条件，请将 **Initial condition** 指定为长度等于 **Number of parameters** 的有限值向量。否则，要为所有参数指定相同的初始条件，请将 **Initial condition** 指定为有限标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `'initialVal'` |
| **类型：** 字符向量 |
| **值：** 有限标量 | 向量 |
| **默认：** `'0'` |

### **Forcing frequency omega (rad/s)** — 强迫频率 `1`（默认）| 正有限标量 | 向量

以弧度每秒为单位指定调制和解调信号的频率。对于给定的参数调优回路，请指定一个低于重要系统动态频率且高于高通和低通滤波器截止频率的强迫频率。

调优单个参数时，将 **Forcing frequency** 指定为正有限标量。

调优多个参数时，将 **Forcing frequency** 指定为长度等于 **Number of parameters** 的正有限值向量。每个强迫频率必须唯一，以确保极值搜索算法收敛。

#### 程序化使用

|  |
| --- |
| **模块参数：** `'omega'` |
| **类型：** 字符向量 |
| **值：** 正有限标量 | 向量 |
| **默认：** `'1'` |

### **Learning rate k** — 参数更新速率 `1`（默认）| 正有限标量 | 向量

学习率是一个增益因子，用于控制模块更新参数的速率。

调优单个参数时，将 **Learning rate** 指定为正有限标量。

调优多个参数时，可以为每个参数调优回路指定不同的学习率。为此，请将 **Learning rate** 指定为长度等于 **Number of parameters** 的正有限值向量。否则，要为所有调优回路指定相同的学习率，请将 **Learning rate** 指定为正有限标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `'gain'` |
| **类型：** 字符向量 |
| **值：** 正有限标量 | 向量 |
| **默认：** `'1'` |

### **Demodulation amplitude a** — 解调信号幅值 `1`（默认）| 正有限标量 | 向量

指定用于解调目标函数的信号幅值。对于大多数应用，请指定 **Demodulation amplitude** ≫ **Modulation amplitude**。这些幅值的乘积与学习率共同控制算法的收敛速度。

调优单个参数时，将 **Demodulation amplitude** 指定为正有限标量。

调优多个参数时，可以为每个参数调优回路指定不同的解调幅值。为此，请将 **Demodulation amplitude** 指定为长度等于 **Number of parameters** 的正有限值向量。否则，要为所有调优回路指定相同的幅值，请将 **Demodulation amplitude** 指定为正有限标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `'demodAmp'` |
| **类型：** 字符向量 |
| **默认：** `'1'` |

### **解调相位 phi\_1 (rad)** — 解调信号相位 `0`（默认）| 正有限标量 | 向量

指定用于解调目标函数的信号的相位 *ϕ*1，单位为弧度。

当调节单个参数时，将**解调相位**指定为正有限标量。

当调节多个参数时，可以为每个参数调节回路指定不同的解调相位。为此，将**解调相位**指定为长度等于**参数数量**的正有限值向量。否则，要为所有调节回路指定相同的相位，将**解调相位**指定为正有限标量。

解调相位和调制相位必须满足条件 cos(*ϕ*1–*ϕ*2) > 0。

#### 编程使用

|  |
| --- |
| **模块参数：** `'demodPhase'` |
| **类型：** 字符向量 |
| **值：** 正有限标量 | 向量 |
| **默认：** `'0'` |

### **调制幅值 b** — 调制信号幅值 `0.1`（默认）| 正有限标量 | 向量

添加到估计参数的扰动信号的幅值。对于大多数应用，指定**调制幅值** ≪ **解调幅值**。这些幅值的乘积与学习率共同控制算法的收敛速度。

当调节单个参数时，将**调制幅值**指定为正有限标量。

当调节多个参数时，可以为每个参数调节回路指定不同的调制幅值。为此，将**调制幅值**指定为长度等于**参数数量**的正有限值向量。否则，要为所有调节回路指定相同的幅值，将**调制幅值**指定为正有限标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `'modAmp'` |
| **类型：** 字符向量 |
| **值：** 正有限标量 | 向量 |
| **默认：** `'0.1'` |

### **调制相位 phi\_2 (rad)** — 调制信号相位 `0`（默认）| 正有限标量 | 向量

添加到估计参数的扰动信号的相位 *ϕ*2，以弧度为单位指定。必须选择解调相位 *ϕ*1 和调制相位 *ϕ*2，使得 cos(*ϕ*1–*ϕ*2) > 0。

当调节单个参数时，将**调制相位**指定为正有限标量。

当调节多个参数时，可以为每个参数调节回路指定不同的调制相位。为此，将**调制相位**指定为长度等于**参数数量**的正有限值向量。否则，要为所有调节回路指定相同的相位，将**调制相位**指定为正有限标量。

#### 编程使用

|  |
| --- |
| **模块参数：** `'modPhase'` |
| **类型：** 字符向量 |
| **值：** 正有限标量 | 向量 |
| **默认：** `'0'` |

### **启用 HPF** — 启用目标函数信号的高通滤波 `off`（默认）| `on`

选择此参数以启用高通滤波器，在解调阶段之前从目标函数信号中去除任何信号偏置。要指定滤波器截止频率，请使用 **HPF frequency** 参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `'highPassEnable'` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认：** `'off'` |

### **HPF frequency omega\_h (rad/s)** — 高通滤波器截止频率 `1`（默认）| 正有限标量 | 向量

用于对目标函数信号进行高通滤波的截止频率 *ωh*，以弧度/秒为单位指定。对于给定的参数调优循环，请指定截止频率使得 *ωh* < *ω*/(2*π*)，其中 *ω* 是对应的强迫频率。

当调优单个参数时，将 **HPF frequency** 指定为正有限标量。

当调优多个参数时，可以为每个参数调优循环指定不同的频率。为此，将 **HPF frequency** 指定为长度等于 **Number of parameters** 的正有限值向量。否则，要为所有调优循环指定相同的频率，请将 **HPF frequency** 指定为正有限标量。

#### 依赖关系

要启用此参数，请选中 **Enable HPF** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'highPassCutoff'` |
| **类型：** 字符向量 |
| **值：** 正有限标量 | 向量 |
| **默认值：** `'1'` |

### **Enable LPF** — 启用解调信号的低通滤波 `off`（默认）| `on`

选中此参数以启用低通滤波器，该滤波器在参数更新阶段之前从解调信号中去除高频分量。要指定滤波器截止频率，请使用 **LPF frequency** 参数。

#### 依赖关系

要启用此参数，请选中 **Enable LPF** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'lowPassEnable'` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **LPF frequency omega\_l (rad/s)** — 低通滤波器截止频率 *ωl* `1`（默认）| 正有限标量 | 向量

用于对解调信号进行低通滤波的截止频率 *ωl*，以弧度/秒为单位指定。对于给定的参数调优循环，请指定截止频率使得 *ωl* > *ω*/(2*π*)，其中 *ω* 是对应的强迫频率。

当调优单个参数时，将 **LPF frequency** 指定为正有限标量。

当调优多个参数时，可以为每个参数调优循环指定不同的频率。为此，将 **LPF frequency** 指定为长度等于 **Number of parameters** 的正有限值向量。否则，要为所有调优循环指定相同的频率，请将 **LPF frequency** 指定为正有限标量。

#### 依赖关系

要启用此参数，请选中 **Enable LPF** 参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `'lowPassCutoff'` |
| **类型：** 字符向量 |
| **值：** 正有限标量 | 向量 |
| **默认值：** `'1'` |

### **Output estimated parameters** — 添加估计参数输出端口 `off`（默认）| `on`

选中此参数以添加 **theta\_hat** 输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `estimatedVarOn` |
| **类型：** 字符向量 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |
## 所属库

Simulink Control Design / Adaptive Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- Extremum Seeking Control 模块仅支持双精度信号的代码生成。
- 在 Rapid Accelerator 模式下运行时，Extremum Seeking Control 模块不支持数据记录。
- 要为 Extremum Seeking Control 模块生成可部署到硬件的代码，请使用离散时间控制器。为此，请将 **Time Domain** 参数设置为 **Discrete time**。

## 版本历史

**在 R2021a 中引入**

### R2023b：库位置变更

Extremum Seeking Control 模块现在位于 **Simulink Control Design/Adaptive Control** 子库中。

在 R2023b 中，当打开在先前版本中保存的模型时，Extremum Seeking Control 模块的库链接会自动更新。

### R2021b：离散时间极值搜索控制器

您现在可以设计具有离散时间高通和低通滤波器以及离散时间积分器的极值搜索控制器。然后，您可以为该控制器生成代码并将其部署到硬件目标。

## 描述

通过最大化目标函数实时计算控制器参数

极值搜索控制模块调整控制器参数以最大化目标函数。极值搜索控制器是无模型自适应控制器，可用于适应未知系统动态以及从控制参数到目标函数的未知映射。当寻求多个参数时，极值搜索控制模块为每个参数使用单独的调优循环。

极值搜索控制模块通过使用正弦信号调制（扰动）参数，并解调所得的扰动目标函数，来搜索最优控制参数。

极值搜索控制图，显示高通滤波器、解调、低通滤波器、参数更新和调制阶段。

要配置极值搜索算法，请设置适当的强制频率、解调和调制信号、学习率以及参数初始条件。配置模块时，确保系统动态处于最快时间尺度，扰动强制频率处于中等时间尺度，滤波器截止频率处于最慢时间尺度。

您可以实现连续时间和离散时间极值搜索控制器。更改控制器的时间域会影响调优循环中使用的高通滤波器、低通滤波器和积分器的时间域。要为极值搜索控制模块生成可部署到硬件的代码，请使用离散时间控制器。

有关详细信息，请参阅极值搜索控制。
