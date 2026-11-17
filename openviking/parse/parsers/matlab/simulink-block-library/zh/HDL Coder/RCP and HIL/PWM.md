---
type: simulink-block
title: 'PWM'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'RCP and HIL'
documentation_page: 'pwm'
documentation_source_path: '../simulink/slref/pwm.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM

## 端口
```yaml
ports:
- name: D
  summary: 占空比标量
  direction: input
  data_types: double
- name: 端口 1
  summary: 输出脉冲标量
  direction: output
  data_types: double
```

### 输入

### **D** — 占空比标量

脉冲 *P* 的期望占空比，指定为范围 [0,1] 内的标量。

**数据类型：** `double`
### 输出

### **端口 1** — 输出脉冲标量

与输入占空比对应的 PWM 信号。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Period (s)
  summary: 脉冲宽度 1（默认）| 实数标量
  group: ''
  block_parameter: Period
  type: 字符串 | 字符向量
  values: 实数标量
  default: '''1'''
- name: Initial Delay
  summary: 初始延迟 0（默认）| 实数标量
  group: ''
  block_parameter: InitialDelay
  type: 字符串 | 字符向量
  values: 数值标量
  default: '0'
- name: Disallow zero duty cycle
  summary: 避免代数环 off | on
  group: ''
  block_parameter: DisallowZeroDutyCycle
  type: 字符串 | 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Run at fixed time intervals
  summary: 选择离散时间行为 on（默认）| off
  group: ''
  block_parameter: RunAtFixedTimeIntervals
  type: 字符串 | 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Sample Time
  summary: 设置脉冲分辨率 0.1（默认）| 标量
  group: ''
  block_parameter: SampleTime
  type: 字符串 | 字符向量
  values: 数值标量
  default: '0.1'
```

### **Period (s)** — 脉冲宽度 1（默认）| 实数标量

输出信号连续脉冲上升沿之间的时间。较小的值表示高频脉冲。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Period` |
| **类型：** 字符串 | 字符向量 |
| **值：** 实数标量 |
| **默认值：** `'1'` |

### **Initial Delay** — 初始延迟 0（默认）| 实数标量

指定生成的 PWM 信号的初始延迟或相位延迟，以秒为单位。

#### 程序化使用

|  |
| --- |
| **模块参数：** `InitialDelay` |
| **类型：** 字符串 | 字符向量 |
| **值：** 数值标量 |
| **默认值：** `0` |

### **Disallow zero duty cycle** — 避免代数环 `off` | `on`

启用此参数以断开包含 PWM 模块的代数环。

**注意**

启用此参数会导致信号值为 0 或以下，从而使占空比输入抛出错误。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DisallowZeroDutyCycle` |
| **类型：** 字符串 | 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'off'` |

### **Run at fixed time intervals** — 选择离散时间行为 `on`（默认）| `off`

指定模块的执行时机以及输出信号的采样时间。

- `off` — 模块在每次输入样本的延迟时间过去时执行。输出信号具有固定次采样时间。
- `on` — 模块以您使用 **Sample time** 参数指定的固定速率执行。输出信号具有您使用 **Sample time** 参数指定的采样时间。

当您选择 **Run at fixed time intervals** 时：

- 延迟信号值必须大于您为 **Sample time** 参数指定的值。
- 不是指定采样时间整数倍的延迟信号值将向下舍入到最接近的采样时间整数倍。例如，如果采样时间为 `0.1` 且延迟信号值为 `0.68`，软件将延迟舍入为 `0.6`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RunAtFixedTimeIntervals` |
| **类型：** 字符串 | 字符向量 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'off'` |

### **Sample Time** — 设置脉冲分辨率 0.1（默认）| 标量

模块执行速率和输出信号采样时间。延迟信号值必须大于指定的采样时间。

当延迟信号值不是指定采样时间的整数倍时，软件将延迟值向下舍入到最接近的采样时间整数倍值。例如，如果采样时间为 `0.1` 且延迟值为 `0.68`，软件将延迟舍入为 `0.6`。

#### 依赖关系

要启用此参数，请选择 **Run at fixed time intervals**。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** 字符串 | 字符向量 |
| **值：** 数值标量 |
| **默认值：** `0.1` |
## 所属库

Simulink / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不推荐用于生产质量代码。这与嵌入式系统中常见的资源限制以及速度和内存限制有关。生成的代码可能包含动态内存分配和释放、递归、额外内存开销以及变化较大的执行时间。虽然代码在功能上是有效的，并且在资源丰富的环境中通常可以接受，但较小的嵌入式目标通常无法支持此类代码。

通常，考虑使用 Simulink Model Discretizer 将连续模块映射为支持生产代码生成的离散等效模块。要启动 Model Discretizer，在 Simulink® Editor 中，在 **Apps** 选项卡上，在 **Apps** 下，在 **Control Systems** 下，点击 **Model Discretizer**。一个例外是 Second-Order Integrator 模块，因为对于此模块，Model Discretizer 生成的是近似离散化。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要从此模块生成 HDL 代码，必须选择 **Run at fixed time intervals** 参数。

## 版本历史

**在 R2020b 中引入**

## 描述

生成与输入占空比对应的理想脉宽调制信号

使用 PWM 模块生成理想脉宽调制信号。

脉宽调制（PWM）是一种使用方波脉冲对模拟信号进行编码的技术。这种编码通过控制方波一个周期中设置为高电平的比例来实现。该比例即为信号的占空比。调制信号与输入占空比之间的关系可以简单描述为：

y¯=Dymax+​(1−D)ymin

其中 *ymax* 和 *ymin* 分别是输出信号的上下界。对于 PWM 模块，占空比被约束在 `[0,1]` 范围内。理想 PWM 信号与占空比 *D* 成正比。
