---
type: simulink-block
title: 'Inport'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope Simulation / Circuit Envelope Fundamentals'
documentation_page: 'inport'
documentation_source_path: 'ref/inport.html'
language: zh-CN
chinese_source: worker-translation
---

# Inport

## 端口

R2025b 中未记录。

## 参数

### **源类型** — Inport 模块对 Simulink 信号的解释 `Ideal voltage` (默认) | `Ideal current` | `Power`

Inport 模块对 Simulink 信号的解释，指定为：

- `Ideal voltage` — 该模块在 RF Blockset 环境中将 Simulink 信号输出为电压信号 *v*(*t*)。当您选择理想电压输入端口时，需要手动添加串联源阻抗，以匹配连接到输入端口的模块。下图说明了该模块的内部配置。

  Inport 模块采用电压源 v(t) 时的内部配置。

- `Ideal current` — 该模块在 RF Blockset 环境中将 Simulink 信号输出为电流信号 *i*(*t*)。当您使用理想电流输入端口时，需要手动添加并联源阻抗，以匹配连接到输入端口的模块。下图说明了该模块的内部配置。

  Inport 模块采用电流源 i(t) 时的内部配置。

- `Power` — 该模块将 Simulink 信号 *Pv*(*t*) 解释为可用功率，并在内部使用电压源和串联阻抗。您可以使用此选项导入使用 Communications Toolbox™ 创建的 50 ohm 环境或不同参考阻抗信号。当您选择此选项时，输入端口会自动在电路中插入源阻抗，如下图所示。

  源阻抗 Zs 与电压源 v(t)。

  电压 *v*(*t*) 是 Simulink 信号 *vSL*(*t*) 的缩放：

  v(t)=2Re(Zs)vSL(t)

  在上述方程中，*Zs* 是 **源阻抗 (Ohm)** 参数的值。

  发生器向负载 *Zl* 提供有功功率：

  Pload=|v(t)|2Re(Zs)|Zs+Zl|​2

  当 *Zl* = *Zs\** 时，该发生器提供可用功率 |*vSL*(*t*)|2。

### **源阻抗 (Ohm)** — 用于可用功率匹配的源阻抗 `50` (默认) | 正整数向量

用于可用功率匹配的源阻抗，指定为以 ohms 为单位的正整数向量

#### 依赖关系

要启用此参数，请在 **源类型** 中选择 `Power`。

### **载波频率** — 载波频率 `0 Hz` (默认) | 向量 | 标量

载波频率，指定为以 Hz、kHz、MHz 或 GHz 为单位的向量或标量。当您选择 **使用方波** 参数时，请将 **载波频率** 指定为大于 `0` 的正标量。在载波频率中，元素是 Configuration 模块中基波音调与对应谐波的组合。

### **使用方波** — 使用方载波 `off` (默认) | `on`

选择此参数以将输入信号调制到方载波上。

### **查看** — 绘制方波按钮

绘制方载波的仿真频率以及带有 RSM 误差的近似方波。

#### 依赖关系

要启用此参数，请选择 **使用方波**。

### **傅里叶系数数量** — 傅里叶系数数量 `10` (默认) | 大于或等于 `1` 的整数

将输入信号调制到方载波上所需的傅里叶系数数量，指定为大于或等于 `1` 的整数。

#### 依赖关系

要启用此参数，请选择 **使用方波**。

### **直流偏置** — 直流偏置 `0` (默认) | 实数

直流偏置，指定为实数。

#### 依赖关系

要启用此参数，请选择 **使用方波**。

### **占空比 (%)** — 方载波的占空比 `50` (默认) | `0` 到 `100` 之间的正整数

方载波的占空比，指定为 `0` 到 `100` 之间的正整数，以 % 为单位。

#### 依赖关系

要启用此参数，请选择 **使用方波**。

### **接地并隐藏负端子** — 接地 RF 电路端子 `on` (默认) | `off`

选择此参数以接地并隐藏负端子。清除此参数以暴露负端子。通过暴露这些端子，您可以将它们连接到模型的其他部分。

## 所属库

RF Blockset / Circuit Envelope / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

### R2022b：在电路包络仿真环境中将输入信号调制到方载波上

选择新的 **使用方波** 参数，以在电路包络仿真环境中将输入信号调制到方载波上。

### R2021b：Inport 模块图标已更新

从 R2021b 开始，Inport 模块图标现已更新。当您打开在 R2021b 之前创建的包含 Inport 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

将 Simulink 输入信号转换为 RF Blockset 信号

Inport 模块将 Simulink® 信号导入 RF Blockset™ 电路包络仿真环境。有关 RF 仿真的介绍，请参见示例 Simulate High Frequency Components。您还可以在 RF Blockset 电路包络仿真环境中将输入信号调制到方载波上。

复值输入信号 *Ik*(*t*) + *j* · *Qk*(*t*) 是在该模块的 **载波频率** 参数中指定的频率 {*fk*} 处的调制。输入端口将复值输入信号转换为适合多载波仿真的 RF 信号：

out=Real(∑k=1N(Ik(t)+j·Qk(t))·ej2πfkt)

**源类型** 参数将 Simulink 信号指定为电流源、电压源或功率源。有关详细信息，请参见 How to Use Inport Block。
Inport 模块掩码图标是动态的，并显示当前的源类型。下表显示了此模块上的图标如何根据您在模块的 **源类型** 参数上设置的源类型而变化。

| 源类型：`Ideal voltage` | 源类型：`Ideal current` | 源类型：`Power` |
| --- | --- | --- |
| Inport 模块图标，其中源类型设置为 Ideal voltage。 | Inport 模块图标，其中源类型设置为 Ideal current。 | Inport 模块图标，其中源类型设置为 Ideal current。 |
