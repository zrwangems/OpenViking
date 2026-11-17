---
type: simulink-block
title: 'First Order Hold'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'firstorderhold'
documentation_source_path: 'slref/firstorderhold.html'
language: zh-CN
chinese_source: worker-translation
---

# First Order Hold

## 端口
```yaml
ports:
- name: Port 1
  summary: 输入信号 标量 | 向量 | 矩阵
  direction: input
  data_types: double
- name: Port 1
  summary: 线性近似输出信号 标量 | 向量 | 矩阵
  direction: output
  data_types: double
```

### 输入

### **Port 1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为实数标量、向量或矩阵。

**数据类型：** `double`
### 输出

### **Port 1** — 线性近似输出信号 标量 | 向量 | 矩阵

输入信号的分段线性近似。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Initial output
  summary: 初始输出 0（默认）| 标量 | 向量
  group: ''
  block_parameter: InitialOutput
  type: 字符向量、字符串
  values: 标量 | 向量
  default: '''0'''
- name: Output algorithm
  summary: 输出信号近似技术 Slow (Avoid Overshoot)（默认）| Fast (Minimize Error)
  group: ''
  block_parameter: OutputAlgorithm
  type: 字符向量、字符串
  values: Slow (Avoid Overshoot)| Fast (Minimize Error)
  default: '''Slow (Avoid Overshoot)'''
- name: Reset if relative extrapolation error exceeds
  summary: 求解器重置的误差容限 inf（默认）| 非负实数标量
  group: ''
  block_parameter: ErrorTolerance
  type: 字符向量、字符串
  values: 标量
  default: '''inf'''
- name: Allow continuous input
  summary: 对连续信号应用保持 off（默认）| on
  group: ''
  block_parameter: AllowContinuousInput
  type: 字符向量、字符串
  values: '''off''| ''on'''
  default: '''off'''
```

### **Initial output** — 初始输出 `0`（默认）| 标量 | 向量

指定在仿真时间超过离散输入的第一个采样命中时间之前，模块生成的输出。

#### 依赖关系

- 此模块的初始输出不能为 `inf` 或 `NaN`。
- `Run-to-run tunable parameter` 不能在仿真运行期间更改。但是，在仿真开始之前更改它不会导致 Accelerator 或 Rapid Accelerator 重新生成代码。

#### 编程用法

|  |
| --- |
| **模块参数：** `InitialOutput` |
| **类型：** 字符向量、字符串 |
| **值：** 标量 | 向量 |
| **默认值：** `'0'` |

### **Output algorithm** — 输出信号近似技术 `Slow (Avoid Overshoot)`（默认）| `Fast (Minimize Error)`

指定用于生成输出信号的近似技术。
慢速低通算法避免对输入信号产生过冲。快速高通算法最小化近似输出中的误差，但可能对输入信号产生过冲。

#### 编程用法

|  |
| --- |
| **模块参数：** `OutputAlgorithm` |
| **类型：** 字符向量、字符串 |
| **值：** `Slow (Avoid Overshoot)`| `Fast (Minimize Error)` |
| **默认值：** `'Slow (Avoid Overshoot)'` |

### **Reset if relative extrapolation error exceeds** — 求解器重置的误差容限 `inf`（默认）| 非负实数标量

指定输出算法外推误差的容限水平。外推误差大于指定值会导致 Simulink® 重置模型的求解器。

**提示**

当此参数设置为 `inf` 时启用 **Allow continuous input** 参数可能导致仿真中的数值不准确。

#### 编程用法

|  |
| --- |
| **模块参数：** `ErrorTolerance` |
| **类型：** 字符向量、字符串 |
| **值：** 标量 |
| **默认值：** `'inf'` |

### **Allow continuous input** — 对连续信号应用保持 `off`（默认）| `on`

选择此参数以使模块能够接受连续信号作为输入。启用此参数会在输入和输出连续信号之间产生延迟。

**注意**

在使用此模块断开代数环时启用此参数。

#### 编程用法

|  |
| --- |
| **模块参数：** `AllowContinuousInput` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'`| `'on'` |
| **默认值：** `'off'` |
## 所属库

Simulink / Continuous

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

不建议用于生产代码生成。

考虑对模型进行离散化。

## 版本历史

**在 R2019b 中引入**

## 描述

对输入信号实现线性外推一阶保持

First Order Hold 模块生成输入信号的连续分段线性近似。使用 First Order Hold 模块将采样的离散信号转换为连续信号，而不会触发求解器重置。

您还可以使用 First Order Hold 模块断开模型中的代数环。
