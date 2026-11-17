---
type: simulink-block
title: 'Inport'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Utilities'
documentation_page: 'inport'
documentation_source_path: 'ref/inport.html'
language: zh-CN
chinese_source: worker-translation
---

# Inport

## 端口

R2025b 中未记录。

## 参数

### **Source type** — Inport 模块对 Simulink 信号的解释 `Ideal voltage`（默认）| `Ideal current` | `Power`

Inport 模块对 Simulink 信号的解释，指定为：

- `Ideal voltage` — 该模块在 RF Blockset 环境中将 Simulink 信号输出为电压信号 *v*(*t*)。当您选择理想电压输入端口时，需要手动添加串联源阻抗，以匹配连接到输入端口的模块。下图展示了该模块的内部配置。

  带有电压源 v(t) 的 Inport 模块内部配置。
- `Ideal current` — 该模块在 RF Blockset 环境中将 Simulink 信号输出为电流信号 *i*(*t*)。当您使用理想电流输入端口时，需要手动添加并联源阻抗，以匹配连接到输入端口的模块。下图展示了该模块的内部配置。

  带有电流源 i(t) 的 Inport 模块内部配置。
- `Power` — 该模块将 Simulink 信号 *Pv*(*t*) 解释为可用功率，并在内部使用电压源和串联阻抗。您可以使用此选项导入 50 欧姆环境或使用 Communications Toolbox™ 创建的不同参考阻抗信号。当您选择此选项时，输入端口会自动在电路中插入源阻抗，如下图所示。

  带有电压源 v(t) 的源阻抗 Zs。

  电压 *v*(*t*) 是 Simulink 信号 *vSL*(*t*) 的缩放：

  v(t)=2Re(Zs)vSL(t)

  在上述方程中，*Zs* 是 **Source impedance (Ohm)** 参数的值。

  发生器向负载 *Zl* 输送有功功率：

  Pload=|v(t)|2Re(Zs)|Zs+Zl|​2

  当 *Zl* = *Zs\** 时，该发生器输送可用功率 |*vSL*(*t*)|2。

### **Source impedance (Ohm)** — 用于可用功率匹配的源阻抗 `50`（默认）| 正整数向量

用于可用功率匹配的源阻抗，指定为以欧姆为单位的正整数向量

#### 依赖关系

要启用此参数，请在 **Source type** 中选择 `Power`。

### **Carrier frequencies** — 载波频率 `0 Hz`（默认）| 向量 | 标量

载波频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的向量或标量。当您选择 **Use Square Wave** 参数时，请将 **Carrier frequencies** 指定为大于 `0` 的正标量。在载波频率中，元素是 Configuration 模块中基频音及其对应谐波的组合。

### **Use Square Wave** — 使用方波载波 `off`（默认）| `on`

选择此参数可将输入信号调制到方波载波上。

### **View** — 绘制方波按钮

绘制方波载波的仿真频率以及带有 RSM 误差的近似方波。

#### 依赖关系

要启用此参数，请选择 **Use Square Wave**。

### **Number of Fourier Coefficients** — 傅里叶系数数量 `10`（默认）| 大于或等于 `1` 的整数

将输入信号调制到方波载波上所需的傅里叶系数数量，指定为大于或等于 `1` 的整数。

#### 依赖关系

要启用此参数，请选择 **Use Square Wave**。

### **DC Bias** — 直流偏置 `0`（默认）| 实数

直流偏置，指定为实数。

#### 依赖关系

要启用此参数，请选择 **Use Square Wave**。

### **Duty Cycle (%)** — 方波载波的占空比 `50`（默认）| `0` 到 `100` 之间的正整数

方波载波的占空比，指定为 `0` 到 `100` 之间的正整数，以 % 为单位。

#### 依赖关系

要启用此参数，请选择 **Use Square Wave**。

### **Ground and hide negative terminals** — 将 RF 电路端子接地 `on`（默认）| `off`

选择此参数可将负极端子接地并隐藏。清除该参数可暴露负极端子。通过暴露这些端子，您可以将它们连接到模型的其它部分。

## 所属库

RF Blockset / Circuit Envelope / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

### R2022b：在电路包络仿真环境中将输入信号调制到方波载波上

选择新的 **Use Square Wave** 参数，以在电路包络仿真环境中将输入信号调制到方波载波上。

### R2021b：Inport 模块图标已更新

从 R2021b 开始，Inport 模块图标现已更新。当您打开在 R2021b 之前创建的包含 Inport 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

将 Simulink 输入信号转换为 RF Blockset 信号

Inport 模块将 Simulink® 信号导入 RF Blockset™ 电路包络仿真环境。有关 RF 仿真的介绍，请参阅示例 Simulate High Frequency Components。您还可以在 RF Blockset 电路包络仿真环境中将输入信号调制到方波载波上。

复值输入信号
*Ik*(*t*) + *j* · *Qk*(*t*)
是在模块的 **Carrier frequencies** 参数中指定的频率 {*fk*} 处的调制。输入端口将复值输入信号转换为适合多载波仿真的 RF 信号：

out=Real(∑k=1N(Ik(t)+j·Qk(t))·ej2πfkt)

**Source type** 参数将 Simulink 信号指定为电流源、电压源或功率源。有关详细信息，请参阅 How to Use Inport Block。Inport 模块掩码图标是动态的，并显示当前的源类型。下表显示了此模块上的图标如何根据您在模块的 **Source type** 参数上设置的源类型而变化。

| Source type：`Ideal voltage` | Source type：`Ideal current` | Source type： `Power` |
| --- | --- | --- |
| Source type 设置为 Ideal voltage 的 Inport 模块图标。 | Source type 设置为 Ideal current 的 Inport 模块图标。 | Source type 设置为 Ideal current 的 Inport 模块图标。 |
