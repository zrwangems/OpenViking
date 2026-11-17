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
chinese_source: worker-translation
---

# Variable Pulse Generator

## 端口

### 输入

### **D** — 占空比标量

脉冲 *P* 的期望占空比，指定为范围 [0,1] 内的标量。

**数据类型：** `double`

### **P** — 周期标量

输出信号连续脉冲上升沿之间的时间。
较小的值表示较高频率的脉冲。

**数据类型：** `double`
### 输出

### **Port 1** — 调制脉冲信号标量

与输入占空比对应的调制输出脉冲信号。

**数据类型：** `double`

## 参数

### **Allow zero pulse width** — 允许输出信号幅度为零 off（默认）| on

启用此参数以允许输出脉冲信号支持宽度为 0 的脉冲。

**注意**

启用此参数会导致模块具有直接馈通。
这可能会在模型中引起代数环。

### **Run at fixed time intervals** — 选择连续或离散时间行为 `continuous`（默认）| `discrete`

选择模块应在连续还是离散采样模式下运行。

默认情况下，模块使用 `continuous` 采样模式，因为它可以提高变步长求解器的仿真性能。

如果需要以下操作，请选择 `discrete` 采样模式：

- 使用定步长求解器
- 生成代码
- 对模块输出进行采样

### **Sampling rate** — 设置脉冲分辨率 0.1（默认）| 标量

指定模块对输入占空比信号进行采样的速率。此采样率成为输出脉冲信号的分辨率。

#### 依赖关系

此参数要求 **Sampling mode** 设置为 `discrete`

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

通常，考虑使用 Simulink Model Discretizer 将连续模块映射为支持生产代码生成的离散等效模块。要启动 Model Discretizer，请在 Simulink® Editor 中，在 **Apps** 选项卡上，在 **Apps** 下，在 **Control Systems** 下，点击 **Model Discretizer**。一个例外是 Second-Order Integrator 模块，因为对于此模块，Model Discretizer 会生成近似离散化。

## 版本历史

**在 R2020b 中引入**

## 描述

生成理想的时变脉冲信号

使用 Variable Pulse Generator 模块创建理想的调制脉冲信号。

一般来说，模块的输出脉冲由下式描述

y(t)={1tk<t<tk+pw0tk+pw<t<tk+1

其中 *pw* 是输出脉冲宽度。

有关脉冲宽度调制的实现，请参阅 PWM。
