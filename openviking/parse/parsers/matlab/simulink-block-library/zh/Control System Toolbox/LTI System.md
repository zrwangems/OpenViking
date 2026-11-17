---
type: simulink-block
title: 'LTI System'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'ltisystem'
documentation_source_path: 'ref/ltisystem.html'
language: zh-CN
chinese_source: worker-translation
---

# LTI System

## 端口
```yaml
ports:
- name: Port_1(In1)
  summary: 输入信号 标量 | 向量
  direction: input
- name: Port_1(Out1)
  summary: 输出信号 标量 | 向量
  direction: output
```

### 输入

### **Port\_1(In1)** — 输入信号 标量 | 向量

对于单输入 LTI 系统，输入信号为标量。对于多输入系统，使用以下模块将系统输入合并为向量信号：

- Mux (Simulink)
- Vector
  Concatenate (Simulink)
- Bus
  Creator (Simulink)
### 输出

### **Port\_1(Out1)** — 输出信号 标量 | 向量

对于单输出 LTI 系统，输出信号为标量。对于多输出系统，输出信号为向量。要将系统输出拆分为标量信号，请使用以下模块：

- Demux (Simulink)
- Bus
  Selector (Simulink)
## 参数
```yaml
parameters:
- name: LTI system variable
  summary: 线性系统动态系统模型
  group: ''
- name: Initial states (state-space only)
  summary: 状态空间模型的初始状态值 []（默认）| 向量 | 标量
  group: ''
- name: Pade order (for linearization)
  summary: Pade 近似阶数 0（默认）| 正整数 | 向量
  group: ''
```

### **LTI system variable** — 线性系统动态系统模型

将模块的线性系统指定为 MATLAB® 表达式或 MATLAB 工作区、模型工作区或数据字典中的变量。模型可以是 SISO 或 MIMO。

大多数线性时不变动态系统模型均受支持，但以下模型除外：

- 频率响应数据模型，例如 `frd`
  和 `genfrd` 模型。
- 非线性辨识模型，例如 `idnlarx`。
- 具有未建模动态的模型，例如
  `udyn`。

指定的模型必须是正则的（参见 `isproper`）。

模型可以是连续时间或离散时间。当 LTI System 模块位于具有同步状态控制的 Simulink 模型中时（参见 State Control (HDL Coder) 模块），必须指定离散时间模型。

Simulink 在初始化仿真之前会将模型转换为其状态空间等价形式。

### **Initial states (state-space only)** — 状态空间模型的初始状态值 `[]`（默认）| 向量 | 标量

如果线性系统为状态空间形式，请将初始状态值指定为向量，其元素数量与系统状态数相同。如果指定标量值，模块会将该值应用于系统中的每个状态。默认值 `[]` 将所有状态初始化为零。

对于非状态空间形式的线性系统（例如传递函数或零极点增益模型），初始状态的概念没有明确定义。对于此类模型，初始状态取决于实现算法所使用的状态坐标选择。因此，模块对此类模型忽略此参数。

### **Pade order (for linearization)** — Pade 近似阶数 `0`（默认）| 正整数 | 向量

设置线性化例程的 Pade 近似阶数。

- 默认值为 `0`，这会导致单位增益且无动态状态。
- 将阶数设置为正整数 `n` 会向模型添加
  `n` 个状态，但会得到更精确的延迟线性模型。

使用正整数向量为每个输入通道指定不同的阶数。
## 所属库

Control System Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2024a：仿真带偏移量的状态空间模型

现在可以使用 LTI System 模块仿真带偏移量的状态空间模型。使用 **LTI system variable** 参数指定一个状态空间变量，该变量在 `Offsets` 属性中包含模型偏移量。偏移量通常出现在某些工作点对非线性动态进行线性化时。有关如何存储偏移量的详细信息，请参见 `ss`。

### R2024a：支持具有复系数的 LTI 模型

现在可以使用 LTI System 模块仿真具有复系数的 LTI 模型。

## 描述

在 Simulink 中使用线性时不变系统模型对象

LTI System 模块将线性系统模型对象导入 Simulink® 环境。在 **LTI system variable** 参数中指定要导入的 LTI 模型。可以导入任何类型的正则线性时不变动态系统模型。如果导入的系统是状态空间（`ss`）模型，可以在 **Initial states** 参数中指定初始状态值。
