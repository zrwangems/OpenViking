---
type: simulink-block
title: 'LTI System'
family: 'control'
product_id: 'control'
product_name: 'Control System Toolbox'
documentation_release: R2025b
official_category: 'Dynamic System Models / Linear System Representation / Numeric Linear Time-Invariant Models'
documentation_page: 'ltisystem'
documentation_source_path: 'ref/ltisystem.html'
language: zh-CN
chinese_source: official
---

# LTI System

## 端口

### 输入

### **Port\_1(In1)** — 输入信号 标量 | 向量

对于单输入 LTI 系统，输入信号是标量。对于多输入系统，使用类似如下的模块将系统输入合并为一个向量信号：

- Mux (Simulink)
- Vector Concatenate (Simulink)
- Bus Creator (Simulink)
### 输出

### **Port\_1(Out1)** — 输出信号 标量 | 向量

对于单输出 LTI 系统，输出信号是标量。对于多输出系统，输出信号是向量。要将系统输出分成标量信号，请使用类似如下的模块：

- Demux (Simulink)
- Bus Selector (Simulink)

## 参数

### **LTI 系统变量** — 线性系统 动态系统模型

将模块的线性系统指定为 MATLAB® 表达式或 MATLAB 工作区、模型工作区或数据字典中的变量。该模型可以是 SISO 或 MIMO。

支持大多数线性时不变动态系统模型，以下模型除外：

- 频率响应数据模型，如 `frd` 和 `genfrd` 模型。
- 非线性辨识模型，如 `idnlarx`。
- 具有未建模动态的模型，例如 `udyn`。

指定的模型必须是本征模型（请参阅 `isproper`）。

模型可以采用连续时间或离散时间。当 LTI system 模块位于具有同步状态控制（请参阅 State Control (HDL Coder) 模块）的 Simulink 模型中时，必须指定一个离散时间模型。

Simulink 在初始化仿真之前将模型转换为其等效的状态空间模型。

### **初始状态(仅限状态空间)** — 状态空间模型的初始状态值 `[]` (默认) | 向量 | 标量

如果线性系统为状态空间形式，将初始状态值指定为一个向量，其条目数与系统的状态数相同。如果指定一个标量值，模块会将该值应用于系统中的每个状态。默认值 `[]` 将所有状态初始化为零。

对于非状态空间形式的线性系统，如传递函数或零极点增益模型，初始状态的概念并未明确定义。对于这样的模型，初始状态取决于实现算法所使用的状态坐标的选择项。因此，对于此类模型，模块会忽略此参数。

### **Pade 阶(用于线性化)** — Pade 逼近的阶数 `0` (默认) | 正整数 | 向量

为线性化例程设置 Pade 逼近的阶数。

- 默认值为 `0`，这意味着模型具有单位增益且没有动态状态。
- 将阶数设置为正整数 `n` 会向模型添加 `n` 个状态，但可以得到更准确的延迟线性模型。

使用正整数向量为每个输入通道指定不同的阶数。

## 所属库

Control System Toolbox

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

### R2024a: 对具有偏移量的状态空间模型进行仿真

现在，您可以使用 LTI System 模块对具有偏移量的状态空间模型进行仿真。使用 **LTI 系统变量**参数在 `Offsets` 属性中指定包含模型偏移量的状态空间变量。在某些工况下，对非线性动态进行线性化时，通常会产生偏移量。有关如何存储偏移量的详细信息，请参阅 `ss`。

### R2024a: 支持复系数 LTI 模型

现在，您可以使用 LTI System 模块对具有复系数的 LTI 模型进行仿真。

## 描述

在 Simulink 中使用线性时不变系统模型对象

LTI System 模块将线性系统模型对象导入 Simulink® 环境中。您可以在 **LTI 系统变量**参数中指定要导入的 LTI 模型。您可以导入任何类型的适当线性时不变动态系统模型。如果导入的系统是状态空间 (`ss`) 模型，您可以在**初始状态**参数中指定初始状态值。
