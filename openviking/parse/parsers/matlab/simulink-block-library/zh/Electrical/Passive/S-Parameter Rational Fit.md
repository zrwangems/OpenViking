---
type: simulink-block
title: 'S-Parameter Rational Fit'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'sparameterrationalfit'
documentation_source_path: 'ref/sparameterrationalfit.html'
language: zh-CN
chinese_source: worker-translation
---

# S-Parameter Rational Fit

## 端口

### 守恒端口

### **pk** — 第 *k* 个正极端子电气

与第 *k* 个端口的正极端子关联的电气守恒端口。

此类端口的数量等于 **Number of ports** 参数的值。

### **nk** — 第 *k* 个负极端子电气

与第 *k* 个端口的负极端子关联的电气守恒端口。

此类端口的数量等于 **Number of ports** 参数的值。

#### 依赖关系

要启用此端口，请清除 **Ground and hide negative terminals** 参数。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Number of ports** — 电气连接对的数量 `2`（默认）| 正整数

电气连接对的数量。此参数名称中的“端口”一词指的是一对连接两个电气网络的端子。此定义在电信行业中很常见。

如果清除 **Ground and hide negative terminals** 参数，则模块所暴露的 Simscape “守恒端口”数量是 **Number of ports** 参数值的两倍。

如果选中 **Ground and hide negative terminals** 参数，则模块所暴露的 Simscape “守恒端口”数量等于 **Number of ports** 参数的值。

### **Reference impedance (Ohm)** — 参考线阻抗 `50`（默认）| 实数标量

参考线阻抗 *Z*0，单位为欧姆。

### **Rational fit object** — 有理拟合对象 `[]`（默认）| 方阵 | `rational` 对象 | `rfmodel.rational` 对象

有理拟合对象。使用 `rational`（RF Toolbox）函数将有理函数对象拟合到元件数据。

默认值 `[]` 表示不存在交叉耦合，并且所有端口都具有等于 **Reference impedance** 参数值的阻抗。当您没有 `rational` 对象时，可使用默认值 `[]` 进行早期测试和构建模型。

### **Ground and hide negative terminals** — 接地并隐藏负极端子的选项 `Off`（默认）| `On`

接地并隐藏负极端子的选项。

清除此参数以启用与模块负极端子关联的 **nk** 端口。

选中此参数以将所有电气连接对的负极端子接地。模块使用 Electrical Reference 模块在 S-Parameter Rational Fit 模块内部对到地的连接进行建模。

## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

对线性系统的 S 参数描述实现有理拟合近似

S-Parameter Rational Fit 模块对以散射参数（S 参数）为特征的线性系统实现有理近似。S 参数描述系统的频率行为。有关 S 参数格式的详细信息，请参阅 Data Import and Network Parameters (RF Toolbox)。有关如何计算 S 参数的详细信息，请参阅 `sparameters` (RF Toolbox)。

S-Parameter Rational Fit 模块使用通带信号运行。如果您需要仿真*基带信号*，即叠加在载波频率上的频带受限信号，请改用 S-Parameters (RF Blockset) 模块以及 RF Blockset™ Circuit Envelope 库中的其他模块。有关基带信号与通带信号之间关系的详细信息，请参阅 Passband Signal Representation in Circuit Envelope (RF Blockset) 示例。有关使用 Circuit Envelope 库中模块的详细信息，请参阅 Circuit Envelope Simulation (RF Blockset)。

您可以通过为 **Rational fit object** 参数指定值来定义有理拟合。构造有理拟合对象有两种方法：

- 您可以使用 `rational`（RF Toolbox）函数将 `rational` 函数对象拟合到元件数据。
- 您可以使用 `rfmodel.rational`（RF Toolbox）构造函数直接指定元件的极点-留数表示。使用 `rationalfit`（RF Toolbox）函数返回 `rfmodel.rational` 对象。

**注意**

要运行在 S-Parameter Rational Fit 模块中使用 `rational` 或 `rfmodel.rational` 对象作为参数值的仿真，您必须安装 RF Toolbox™。

推荐使用 `rational`（RF Toolbox）而非 `rationalfit`，因为它可实现更快的仿真并具有改进的拟合控制。

出于测试目的，您还可以将有理拟合对象指定为：

- 空集 `[]` — 此选项创建一个无反射且端口之间无交叉耦合的有理系统。所有端口向外部电路呈现的阻抗等于 **Reference impedance (Ohm)** 参数的值。
- 维度等于端口数量的方阵常数矩阵 — 此矩阵定义连接端口的常数项。零矩阵等效于空集选项，而 *(i,j)* 元素中的条目 `1` 表示从端口 *j* 到端口 *i* 的直接馈通。

**注意**

在此上下文中，“端口”指的是一对连接两个电气网络的端子。此定义在电信行业中很常见。根据此定义，单个“端口”在 Simscape™ 系列产品中表示两个“守恒端口”。

您可以通过设置 **Number of ports** 参数的值来指定端口数量。将此值限制为 `33`。更高的值会显著增加编译和仿真时间。更高阶的有理拟合也会增加编译和仿真时间。如果模型的其余部分是线性或切换线性的，请避免在有理拟合对象中包含延迟项，以便 S-Parameter Rational Fit 模块也使用线性方程。有关检查模型中是否存在非线性方程模块的详细信息，请参阅 `simscape.findNonlinearBlocks`。

### 方程

下图显示了二端口器件的四元素 S 参数矩阵。

在此图中：

- *a*i 是来自端口 *i* 的入射功率波。
- *b*i 是来自端口 *i* 的反射功率波。
- *S*ij 是传输系数，表示从端口 *j* 进入网络的信号有多少传输到端口 *i*。

该模块假设所有参考阻抗相等且具有实数标量值。这些方程描述了在一定频率范围内每个端口处入射功率波与反射功率波之间的关系，

b1=S11a1+S12a2b2=S21a1+S22a2

ai=bi=12(Vi+Z0Ii)

其中：

- *V*i 是端口 *i* 相对于地的电压。
- *Z*0 是 **Reference impedance (Ohm)** 参数的值。
- *I*i 是通过端口 *i* 的电流。

`rational` 对象通过以下形式的有理传递函数来近似频率响应 *S*ij，

F(s)=∑k=1nCks−Ak+D,

其中：

- *s* 是角频率。
- *C*k 是留数。
- *A*k 是极点。
- *D* 是直接项。
