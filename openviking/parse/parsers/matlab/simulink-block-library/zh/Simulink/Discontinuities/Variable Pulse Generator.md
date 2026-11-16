---
type: simulink-block
title: 'Variable Pulse Generator'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'variablepulsegenerator'
documentation_source_path: 'slref/variablepulsegenerator.html'
language: zh-CN
chinese_source: official
---

# Variable Pulse Generator

## 端口

### 输入

### **D** — 占空比 标量

脉冲 *P* 的所需占空比，指定为在范围 [0,1] 内的标量。

**数据类型:** `double`

### **P** — 周期 标量

输出信号的连续脉冲的上升沿之间的时间。值越小，表示频率脉冲越高。

**数据类型:** `double`
### 输出

### **Port 1** — 调制脉冲信号 标量

对应于输入占空比的调制输出脉冲信号。

**数据类型:** `double`

## 参数

### **允许零脉冲宽度** — 允许输出信号的幅值为零 off (默认) | on

启用此参数以允许输出脉冲信号支持宽度为 0 的脉冲。

**注意**

启用此参数会导致模块具有直接馈通。这可能会在您的模型中产生代数环。

### **以固定时间间隔运行** — 选择连续或离散时间行为 **连续** (默认) | **离散**

选择模块应在连续还是离散采样模式下运行。

默认情况下，模块使用**连续**采样模式，因为该模式能提高使用变步长求解器的仿真性能。

如果您需要执行以下操作，请选择**离散**采样模式：

- 使用定步长求解器
- 生成代码
- 对模块输出进行采样

### **采样率** — 设置脉冲分辨率 0.1 (默认) | 标量

指定模块对输入占空比信号进行采样的速率。此采样率成为输出脉冲信号的分辨率。

#### 依赖关系

此参数要求**采样模式**设置为**离散**

## 所属库

Simulink / Discontinuities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产级的代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含内存的动态分配和释放、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常不能支持此类代码。

通常，考虑使用 Simulink 模型离散化器将连续模块映射到支持生产代码生成的离散等效模块。要启动模型离散化器，请在 Simulink® 编辑器中，在 **App** 选项卡上，在 **App** 下，在**控制系统**下，点击**模型离散化器**。一个例外是 Second-Order Integrator 模块，因为对于该模块，模型离散化器产生近似离散化。

## 版本历史

**在 R2020b 中推出**

## 描述

生成理想的时变脉冲信号

使用 Variable Pulse Generator 模块创建理想的调制脉冲信号。

一般情况下，模块的输出脉冲描述为

y(t)={1tk<t<tk+pw0tk+pw<t<tk+1

其中 *pw* 是输出脉冲宽度。

有关脉冲宽度调制的实现，请参阅PWM。
