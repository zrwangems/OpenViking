---
type: simulink-block
title: 'Integrator (Discrete or Continuous)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'integratordiscreteorcontinuous'
documentation_source_path: 'ref/integratordiscreteorcontinuous.html'
language: zh-CN
chinese_source: worker-translation
---

# Integrator (Discrete or Continuous)

## 端口

### 输入

### **u** — 积分器输入向量

积分器输入。

**数据类型：** `single` | `double`

### **Reset** — 恢复到初始状态标量

积分器复位。要将积分器状态复位为 **x0** 端口的值，请向此端口传递非零值。
或者，将值为零的 Constant 模块连接到此端口以覆盖外部复位。

**数据类型：** `single` | `double`

### **x0** — 初始状态向量

积分器初始状态。要指定复位后的状态值，请向此端口传递信号。

**数据类型：** `single` | `double`
### 输出

### **y** — 积分器输出向量

积分器输出。

**数据类型：** `single` | `double`

## 参数

### **Integrator method** — 用于指定积分或累加方法的选项 `Integration: Forward Euler`（默认）| `Integration: Backward Euler` | `Integration: Trapezoidal` | `Accumulation: Forward Euler` | `Accumulation: Backward Euler` | `Accumulation: Trapezoidal`

*自 R2025a 起*

用于指定积分或累加方法的选项。有关详细信息，请参阅 Discrete-Time Integrator 模块的 Integration and Accumulation Methods 部分。

#### 依赖关系

要启用此参数，请将 **Sample time (-1 for inherited)** 设置为 `-1` 或正实数。

### **External reset** — 复位策略 `level`（默认）| `rising` | `falling` | `either`

选择积分器的外部复位策略：

- 选择 `rising` 以在复位信号从负值或零值上升到正值时复位状态。
- 选择 `falling` 以在复位信号从正值下降到零值或负值时复位状态。
- 选择 `either` 以在复位信号从零变为非零值、从非零值变为零或改变符号时复位状态。
- 选择 `level` 以在复位信号在当前时间步为非零，或从前一时间步的非零值变为当前时间步的零值时复位状态。

### **Limit type** — 饱和策略 `Anti-windup`（默认）| `Windup`

选择积分器的限幅类型：

- 选择 `Anti-windup` 以限制积分器的状态，防止积分饱和。
- 选择 `windup` 以限制积分器的输出，允许积分器状态饱和。

### **Upper saturation limit** — 状态上限 `inf`（默认）| 实数

积分器饱和上限。将此值设置为 `inf` 表示无饱和上限，或设置为有限值以使用 **Limit type** 设置的策略对积分器进行饱和。

### **Lower saturation limit** — 状态下限 `-inf`（默认）| 实数

积分器饱和下限。将此值设置为 `-inf` 表示无饱和下限，或设置为有限值以使用 **Limit type** 设置的策略对积分器进行饱和。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| `0` | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请将此参数设置为 `-1`。
对于离散时间操作，请将此参数设置为正整数。对于连续时间操作，请将此参数设置为 `0`。

如果此模块位于支持在连续操作和离散操作之间切换的掩码子系统或变体子系统中，请提升此参数以确保在模块的连续和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

### R2025a：指定积分或累加方法

现在可以使用 **Integrator method** 参数指定模块的积分或累加方法。此模块可以使用前向欧拉、后向欧拉或梯形方法对信号进行积分或累加。

## 描述

离散时间或连续时间积分器

Integrator (Discrete or Continuous) 模块实现符合 IEEE 421.5-2016[1] 的简单积分器。

您可以使用 **Sample time (-1 for inherited)** 参数在积分器的连续和离散实现之间切换。

### 方程

**连续**

要将积分器配置为连续时间，请将 **Sample time (-1 for inherited)** 属性设置为 `0`。此表示等效于连续传递函数：

G(s)=1s.

根据上述传递函数，积分器的定义方程为：

{x˙(t)=u(t)y(t)=x(t)  x(0)=x0,

其中：

- *u* 是积分器输入。
- *x* 是积分器状态。
- *y* 是积分器输出。
- *t* 是仿真时间。
- *x0* 是积分器的初始状态。

**离散**

要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。离散表示等效于传递函数：

G(z)=Tsz−1,

其中 *Ts* 是采样时间。

此模块可以使用前向欧拉、后向欧拉或梯形方法对信号进行积分或累加。要指定模块的积分或累加方法，请使用 **Integrator method** 参数。*（自 R2025a 起）* 如果将 **Integrator method** 参数设置为 `Integration: Forward Euler`，则模块使用离散传递函数中的前向欧拉方法定义积分器方程：

{x(n+1)=x(n)+Tsu(n)y(n)=x(n)  x(0)=x0,

其中：

- *u* 是积分器输入。
- *x* 是积分器状态。
- *y* 是积分器输出。
- *n* 是仿真时间步。
- *x0* 是积分器的初始状态。

### 定义初始条件

您可以使用输入端口 **x0** 定义状态初始条件。积分器状态在每次复位时恢复到初始条件。

### 限制积分

您可以使用以下两种方法之一限制积分输出：

- 将 **Limit type** 设置为 `Anti-windup` 以使用抗积分饱和方法。

  抗积分饱和方法将积分器状态 *x* 限制在下饱和限值 *A* 和上饱和限值 *B* 之间：

  A<=x<=B .

  由于状态受到限制，当积分饱和时，输出可以立即响应输入符号的反转。
- 将 **Limit type** 设置为 `Windup` 以使用积分饱和方法。

  积分饱和方法将积分器输出 *y* 限制在下饱和限值 *A* 和上饱和限值 *B* 之间：

  A<=y<=B .

  由于输出受到限制，当积分器饱和时，状态可以继续增长。因此，在状态达到限制饱和点之前，输出无法响应输入符号的反转。

### 复位状态

您可以通过向模块的 **Reset** 端口传递非零信号来复位积分器的状态。
