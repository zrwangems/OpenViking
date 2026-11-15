---
type: simulink-block
title: 'PWM'
family: discontinuities
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'pwm'
---

# PWM

Generate ideal pulse width modulated signal corresponding to input duty cycle

## 中文

生成对应于输入占空比的理想脉冲宽度调制信号

### 所属库

Simulink / Discontinuities

### 描述

使用 PWM 模块生成理想脉冲宽度调制信号。

脉冲宽度调制 (PWM) 是一种使用方波脉冲对模拟信号进行编码的方法。这种编码通过控制方波周期中设置为高电平的那一部分所占的比例来实现。此比率就是信号的占空比。调制信号与输入占空比之间的关系可以简单描述为：

y¯=Dymax+​(1−D)ymin

其中 *ymax* 和 *ymin* 分别是输出信号的上界和下界。对于 PWM 模块，占空比限制为 `[0,1]`。理想 PWM 信号与占空比 *D* 成正比。

### 端口

#### 输入

#### **D** — 占空比 标量

脉冲 *P* 的所需占空比，指定为在范围 [0,1] 内的标量。

**数据类型:** `double`
#### 输出

#### **Port 1** — 输出脉冲 标量

对应于输入占空比的 PWM 信号。

**数据类型:** `double`

### 参数

#### **周期(秒)** — 脉冲宽度 1 (默认) | 实数标量

输出信号的连续脉冲的上升沿之间的时间。小值表示高频脉冲。

##### 编程用法

|  |
| --- |
| **模块参数**：`Period` |
| **类型：**字符串 | 字符向量 |
| **值**：实数标量 |
| **默认值：**`'1'` |

#### **初始延迟** — 初始延迟 0 (默认) | 实数标量

为生成的 PWM 信号指定初始延迟或相位延迟，以秒为单位。

##### 编程用法

|  |
| --- |
| **模块参数**：`InitialDelay` |
| **类型：**字符串 | 字符向量 |
| **值：**数值标量 |
| **默认值：**`0` |

#### **不允许零占空比** — 避免代数环 `off` | `on`

启用此参数以中断包含 PWM 模块的代数环。

**注意**

启用此参数会导致信号值为 0 或以下，这会导致占空比输入抛出错误。

##### 编程用法

|  |
| --- |
| **模块参数**：`DisallowZeroDutyCycle` |
| **类型：**字符串 | 字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'off'` |

#### **以固定时间间隔运行** — 为离散时间行为选择 `on` (默认) | `off`

指定模块执行的时间以及输出信号的采样时间。

- `off` - 模块在输入采样的延迟每次到期时执行。输出信号在子步中具有不变的采样时间。
- `on` - 模块以您使用**采样时间**参数指定的固定速率执行。输出信号具有您使用**采样时间**参数指定的采样时间。

当您选择**以固定时间间隔运行**时：

- 延迟信号值必须大于您为**采样时间**参数指定的值。
- 不是指定采样时间整数倍的延迟信号值向下舍入到最接近的采样时间整数倍。例如，如果采样时间为 `0.1` 且延迟信号值为 `0.68`，软件会将延迟舍入为 `0.6`。

##### 编程用法

|  |
| --- |
| **模块参数**：`RunAtFixedTimeIntervals` |
| **类型：**字符串 | 字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'off'` |

#### **采样时间** — 设置脉冲分辨率 0.1 (默认) | 标量

模块执行速率和输出信号采样时间。延迟信号值必须大于指定的采样时间。

当延迟信号值不是指定采样时间的整数倍时，软件将延迟值向下舍入到最接近的采样时间整数倍值。例如，如果采样时间为 `0.1` 且延迟值为 `0.68`，软件会将延迟舍入为 `0.6`。

##### 依赖关系

要启用此参数，请选择**以固定时间间隔运行**。

##### 编程用法

|  |
| --- |
| **模块参数：**`SampleTime` |
| **类型：**字符串 | 字符向量 |
| **值：**数值标量 |
| **默认值：**`0.1` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产级的代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含内存的动态分配和释放、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常不能支持此类代码。

通常，考虑使用 Simulink 模型离散化器将连续模块映射到支持生产代码生成的离散等效模块。要启动模型离散化器，请在 Simulink® 编辑器中，在 **App** 选项卡上，在 **App** 下，在**控制系统**下，点击**模型离散化器**。一个例外是 Second-Order Integrator 模块，因为对于该模块，模型离散化器产生近似离散化。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要从这个模块生成 HDL 代码，必须选择**以固定时间间隔运行**参数。

### 版本历史记录

**在 R2020b 中推出**

## Libraries

Simulink / Discontinuities

## Description

Use the PWM block to generate an ideal pulse width modulated signal.

Pulse-width modulation (PWM) is a technique for encoding an analog signal using square
pulses. This encoding is achieved by controlling the fraction of one period of the
square wave that is set to high. This fraction is the duty cycle of the signal. The
relationship between the modulated signal and the input duty cycle can be simply
described as:

y¯=Dymax+​(1−D)ymin

where *ymax* and *ymin* are the upper and lower bounds of the output signal, respectively. For
the PWM block, the duty cycle is constrained to `[0,1]`.
The ideal PWM signal is proportional to the duty cycle *D*.

## Ports

### Input

### **D** — Duty Cycle scalar

Desired duty cycle of the pulse *P*, specified as scalar within the range [0,1].

**Data Types:** `double`
### Output

### **Port 1** — Output pulse scalar

PWM signal corresponding to the input duty cycle.

**Data Types:** `double`

## Parameters

### **Period (s)** — Pulse width 1 (default) | real scalar

Time between rising edges of consecutive pulses of the output signal. A
small value represents a high-frequency pulse.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Period` |
| **Type:** string | character vector |
| **Values:** real scalar |
| **Default:** `'1'` |

### **Initial Delay** — Initial delay 0 (default) | real scalar

Specify an initial delay or phase delay for the generated PWM signal, in
seconds.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialDelay` |
| **Type:** string | character vector |
| **Values:** numeric scalar |
| **Default:** `0` |

### **Disallow zero duty cycle** — Avoid algebraic loops `off` | `on`

Enable this parameter to break algebraic loops containing the
PWM block.

**Note**

Enabling this parameter causes a signal value of 0 or below, which
causes the duty cycle input to throw an error.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DisallowZeroDutyCycle` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Run at fixed time intervals** — Select for discrete time behavior `on` (default) | `off`

Specify when the block executes and the sample time for the output signal.

- `off` — Block executes each time the delay
  for an input sample elapses. Output signal has fixed-in-minor
  sample time.
- `on` — Block executes at a fixed rate you
  specify using the **Sample time** parameter.
  Output signal has the sample time you specify using the
  **Sample time** parameter.

When you select **Run at fixed time intervals**:

- The delay signal values must be greater than the value you
  specify for the **Sample time**
  parameter.
- Delay signal values that are not integer multiples of the
  specified sample time are rounded down to the nearest integer
  multiple of the sample time. For example, if the sample time is
  `0.1` and the delay signal value is
  `0.68`, the software rounds the delay to
  `0.6`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RunAtFixedTimeIntervals` |
| **Type:** string | character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'off'` |

### **Sample Time** — Set pulse resolution 0.1 (default) | scalar

Block execution rate and output signal sample time. The delay signal
values must be greater than the specified sample time.

When the delay signal value is not an integer multiple of the specified
sample time, the software rounds the delay value down to the closest value
that is an integer multiple of the sample time. For example, if the sample
time is `0.1` and the delay value is
`0.68`, the software rounds the delay to
`0.6`.

#### Dependencies

To enable this parameter, select **Run at fixed time
intervals**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** string | character vector |
| **Values:** numeric scalar |
| **Default:** `0.1` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production-quality code. Relates to resource limits and restrictions on speed and memory often found in embedded systems. The code generated can contain dynamic allocation and freeing of memory, recursion, additional memory overhead, and widely-varying execution times. While the code is functionally valid and generally acceptable in resource-rich environments, smaller embedded targets often cannot support such code.

In general, consider using the Simulink Model Discretizer to map continuous blocks into discrete equivalents that support production code generation. To start the Model Discretizer, in the Simulink® Editor, on the **Apps** tab, under **Apps**, under **Control Systems**, click **Model Discretizer**. One exception is the Second-Order Integrator block because, for this block, the Model Discretizer produces an approximate discretization.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

For HDL code generation from this block, the **Run at
fixed time intervals** parameter must be selected.

## Version History

**Introduced in R2020b**
