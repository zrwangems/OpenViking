---
type: simulink-block
title: 'Signal Sampler'
family: 'msblks'
product_id: 'msblks'
product_name: 'Mixed-Signal Blockset'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'signalsampler'
documentation_source_path: 'ref/signalsampler.html'
language: zh-CN
chinese_source: worker-translation
---

# Signal Sampler

## 端口
```yaml
ports:
- name: signal
  summary: 固定步长离散输入信号 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: clock
  summary: 饱和但已采样的时钟波形 标量
  direction: input
  data_types: double
- name: clock_time
  summary: 时钟跳变的精确时间 标量
  direction: input
- name: DecisionThreshold
  summary: 锁存输出切换极性时的电压 标量
  direction: input
  data_types: double
- name: sample
  summary: 时钟边沿处的采样输出值 标量 | -1 | -1
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
```

### 输入

### **signal** — 固定步长离散输入信号 标量

要采样的固定步长离散输入信号，指定为标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **clock** — 饱和但已采样的时钟波形 标量

饱和但已采样的时钟波形，指定为标量。**clock** 端口处的输入与 **clock\_time** 端口处的输入一起用于定义对输入信号进行采样的时间。

**数据类型：** `double`

### **clock\_time** — 时钟跳变的精确时间 标量

时钟跳变的精确时间，指定为标量。**clock\_time** 端口处的输入与 **clock** 端口处的输入一起用于定义对输入信号进行采样的时间。

### **DecisionThreshold** — 锁存输出切换极性时的电压 标量

锁存输出切换极性时的电压，指定为标量。

**数据类型：** `double`
### 输出

### **sample** — 时钟边沿处的采样输出值 标量 | `-1` | `-1`

时钟边沿处的采样输出值，以标量形式返回。

输出有两种模式：

- **Continuous** — 输出恰好是时钟边沿时刻输入信号的值。
- **Latched** — 输出为二进制，值为 `-1` 或 `1`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Clock edge
  summary: 确定何时对输入信号进行采样 Rising（默认）| Falling
  group: ''
  block_parameter: ClockEdge
  type: 字符向量
  values: Rising| Falling
- name: Output mode
  summary: 确定输出采样模式 Continuous（默认）| Latched
  group: ''
  block_parameter: OutputMode
  type: 字符向量
  values: Continuous| Latched
- name: Simulate using
  summary: 选择仿真模式 Code generation（默认）| Interpreted execution
  group: ''
  block_parameter: SimulateUsing
  type: 字符向量
  values: Code generation| Interpreted execution
- name: DecisionThresholdPort
  summary: 打开判决阈值端口 on（默认）| off
  group: ''
  block_parameter: DecisionThresholdPort
  type: 字符向量
  values: on| off
- name: Latch decision threshold
  summary: 锁存输出切换极性时的电压 0（默认）| 标量
  group: ''
  block_parameter: DecisionThreshold
  type: 字符向量
  values: 标量
- name: Latch sensitivity
  summary: 确保锁存输出切换到正确极性所需的高于或低于判决阈值的电压 0（默认）| 标量
  group: ''
  block_parameter: Sensitivity
  type: 字符向量
  values: 标量
- name: Symbol time (s)
  summary: 单个符号持续时间的时间 100e-12（默认）| 实正标量
  group: ''
  block_parameter: SymbolTime
  type: 字符向量
  values: 实正标量
- name: Sample interval (s)
  summary: 波形的均匀时间步长 6.25e-12（默认）| 实正标量
  group: ''
  block_parameter: SampleInterval
  type: 字符向量
  values: 实正标量
- name: Modulation (2:NRZ, 3:PAM3, 4:PAM4)
  summary: 调制方案 2（默认）| 3 | 4
  group: ''
  block_parameter: Modulation
  type: 字符向量
  values: 2 | 3 | 4
- name: Input waveform type
  summary: 输入波形类型 Sample（默认）| Impulse
  group: ''
  block_parameter: WaveType
  type: 字符向量
  values: Sample | Impulse
```

#### 主要

### **Clock edge** — 确定何时对输入信号进行采样 `Rising`（默认）| `Falling`

确定何时对输入信号进行采样，即时钟信号的上升沿或下降沿。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ClockEdge` |
| **类型：** 字符向量 |
| **值：** `Rising`| `Falling` |
| **默认：** `Rising` |

### **Output mode** — 确定输出采样模式 `Continuous`（默认）| `Latched`

确定输出采样模式，即 `Continuous` 或 `Latched`。

在 `Continuous` 模式下，输出恰好是时钟边沿时刻输入信号的值。

在 `Latched` 模式下，输出为二进制，值为 `-1` 或 `1`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputMode` |
| **类型：** 字符向量 |
| **值：** `Continuous`| `Latched` |
| **默认：** `Continuous` |

### **Simulate using** — 选择仿真模式 `Code generation`（默认）| `Interpreted execution`

选择仿真模式。此选择会影响仿真性能。

使用 `Code generation` 方法对模型进行仿真需要额外的启动时间，但后续仿真运行更快。使用 `Interpreted execution` 方法对模型进行仿真可能会减少启动时间，但后续仿真运行较慢。有关详细信息，请参阅 Interpreted Execution vs. Code Generation。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** 字符向量 |
| **值：** `Code generation`| `Interpreted execution` |
| **默认：** `Code generation` |

#### 锁存输出

### **DecisionThresholdPort** — 打开判决阈值端口 on（默认）| off

选择以打开判决阈值端口。打开后，**DecisionThreshold** 端口处的电压用于决定何时为锁存输出切换极性。默认情况下，此选项处于选中状态。

判决阈值作为 AMI 参数受支持。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DecisionThresholdPort` |
| **类型：** 字符向量 |
| **值：** on| off |
| **默认：** on |

### **Latch decision threshold** — 锁存输出切换极性时的电压 `0`（默认）| 标量

锁存输出切换极性时的电压，指定为标量。使用此参数在模块本身中定义锁存输出的判决阈值。

判决阈值支持作为 AMI 参数。

#### 依赖关系

要启用此参数，请取消选择 **DecisionThresholdPort** 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DecisionThreshold` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `0` |

### **Latch sensitivity** — 确保锁存输出切换到正确极性所需的高于或低于判决阈值的电压 0（默认）| 标量

确保锁存输出切换到正确极性所需的高于或低于判决阈值的电压。此参数用于对锁存器的亚稳态区域进行建模。该行为按最坏情况建模，即除非采样电压位于亚稳态区域之外，否则锁存输出保持不变。如果数据采样电压位于该区域内（±**Latch sensitivity**），则位错误的概率为 50%。

**Latch sensitivity** 支持作为 AMI 参数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Sensitivity` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `0` |

#### 高级

### **Symbol time (s)** — 单个符号持续时间的时间 `100e-12`（默认）| 实正标量

单个符号持续时间的时间，以秒为单位指定为实正标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SymbolTime` |
| **类型：** 字符向量 |
| **值：** 实正标量 |
| **默认：** `100e-12` |

**数据类型：** `double`

### **Sample interval (s)** — 波形的均匀时间步长 `6.25e-12`（默认）| 实正标量

波形的均匀时间步长，以秒为单位指定为实正标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SampleInterval` |
| **类型：** 字符向量 |
| **值：** 实正标量 |
| **默认：** `6.25e-12` |

**数据类型：** `double`

### **Modulation (2:NRZ, 3:PAM3, 4:PAM4)** — 调制方案 `2`（默认）| `3` | `4`

调制方案中的逻辑电平数：

- 如果调制方案为 NRZ（不归零），则选择 `2`。
- 如果调制方案为 PAM3（脉冲幅度调制电平 3），则选择 `3`。
- 如果调制方案为 PAM4（脉冲幅度调制电平 4），则选择 `4`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Modulation` |
| **类型：** 字符向量 |
| **值：** `2` | `3` | `4` |
| **默认：** `2` |

**数据类型：** `char`

### **Input waveform type** — 输入波形类型 `Sample`（默认）| `Impulse`

输入波形类型，可以是逐样本信号或冲激响应信号。

#### 程序化使用

|  |
| --- |
| **模块参数：** `WaveType` |
| **类型：** 字符向量 |
| **值：** `Sample` | `Impulse` |
| **默认：** `Sample` |
## 所属库

Mixed-Signal Blockset / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

在输入时钟的边沿对输入信号进行采样

Signal Sampler 模块估计输入固定步长离散采样信号在特定时间（通常位于两个采样时间之间）的值。该模块使用精确的输入时间值和信号的线性插值来获得此估计值。

Signal Sampler 模块将从最后一个采样到时钟跳变发生的精确时间之间的时间间隔计算为相对于采样间隔的模余数。该模块使用线性插值来计算新的输出采样值。
