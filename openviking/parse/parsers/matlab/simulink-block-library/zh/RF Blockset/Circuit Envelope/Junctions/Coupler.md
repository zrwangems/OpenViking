---
type: simulink-block
title: 'Coupler'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Junctions'
documentation_page: 'coupler'
documentation_source_path: 'ref/coupler.html'
language: zh-CN
chinese_source: worker-translation
---

# Coupler

## 端口

R2025b 中未记录。

## 参数

### **Select component** — 耦合器类型 `Directional coupler`（默认）| `Coupler symmetrical` | `Coupler antisymmetrical` | `Hybrid quadrature (90 deg)` | `Hybrid rat-race` | `Magic tee`

耦合器类型，指定为：

- `Directional coupler`

  默认选项为 `Directional coupler`。`Directional coupler` 的 S 参数矩阵为：

  [rliliscilrlcisiscrlilcisilrl]

  其中：

  - rl =
    10(-ReturnLoss/20)
  - il =
    j10(-InsertionLoss/20)
  - is =
    j10(-(Coupling+Directivity)/20)
  - c =
    10(-Coupling/20)

  **注意**

  在 2019a 版本中，Directional Coupler 模块的 S 参数表示已更改，以便为所有指定的掩码值提供有效的实现。此实现为 s12、s13、s21、s24、s31、s34、s42 和 s43 项添加了 90 度相移。此外，还为 s14、s23、s32 和 s41 项添加了 -180 度相移。

  使用此选项可根据数据手册中的耦合器参数进行建模。
- `Coupler symmetrical`

  `Coupler symmetrical` 的 S 参数矩阵为：

  [0α0jβα0jβ00jβ0αjβ0α0]

  其中：

  - |α| ≤ 1 =
    功率传输系数
  - β = sqrt(1– α\*α)
- `Coupler antisymmetrical`

  `Coupler antisymmetrical` 的 S 参数矩阵为：

  [0α0βα0−β00−β0αβ0α0]

  其中：

  - |α| ≤ 1 =
    功率传输系数。
  - β = sqrt (1– α\*α)
- `Hybrid quadrature (90deg)`

  `Hybrid quadrature(90deg)` 的 S 参数矩阵为：

  [0-j/20-1/2-j/20-1/200-1/20-j/2-1/20-j/20]
- `Hybrid rat-race`

  `Hybrid rat-race` 的 S 参数矩阵为：

  [0−j/20−j/2−j/20j/200j/20−j/2−j/20−j/20]
- `Magic tee`

  `Magic tee` 的 S 参数矩阵为：

  [0011001−111001−100]2

Divider 模块使用 `ispassive` 函数来测试 S 参数矩阵的无源性。

### **Coupling (dB)** — 耦合到输出端口的输入信号功率比例 0（默认）| 非负实数标量

`Directional coupler` 耦合到输出端口的输入信号功率比例，指定为非负实数标量。默认值为 `0` dB。

#### 依赖关系

要启用此参数，请在 **Select component** 选项卡中选择 `Directional coupler`。

### **Directivity (dB)** — 耦合端口功率与隔离端口功率之比 `inf`（默认）| 非负实数标量

`Directional coupler` 耦合端口功率与隔离端口功率之比，指定为非负实数标量。默认值为 `inf`。

#### 依赖关系

要启用此参数，请在 **Select component** 选项卡中选择 `Directional coupler`。

### **Insertion loss (dB)** — 输入端口与输出端口之间的信号功率损耗 `inf`（默认）| 非负实数标量

`Directional coupler` 输入端口与输出端口之间的信号功率损耗，指定为非负实数标量。默认值为 `inf`。

#### 依赖关系

要启用此参数，请在 **Select component** 选项卡中选择 `Directional coupler`。

### **Return loss (dB)** — 因阻抗失配导致的信号功率损耗 `inf`（默认）| 非负实数标量

`Directional coupler` 因阻抗失配导致的信号功率损耗，指定为非负实数标量。默认值为 `inf`。

#### 依赖关系

要启用此参数，请在 **Select component** 选项卡中选择 `Directional coupler`。

### **Power transmission coefficient** — 传输信号功率 0（默认）| 实数标量

`Directional coupler` 的传输信号功率，指定为实数标量。默认值为 0。

#### 依赖关系

要启用此参数，请在 **Select component** 选项卡中选择 `Coupler symmetrical` 或 `Coupler antisymmetrical`。

### **Reference impedances (Ohm)** — 耦合器的参考阻抗 `50`（默认）| 正标量 | 正三元组向量

耦合器的参考阻抗，指定为标量或正三元组向量。

**注意**

当所有端口的参考阻抗不相等时，Coupler 模块内部的模型归一化到 50 欧姆。

### **Ground and hide negative terminals** — 接地并隐藏负端子 `on`（默认）| `off`

选择此参数以接地并隐藏负端子。
要暴露负端子，请清除此参数。通过暴露这些端子，您可以将它们连接到模型的其它部分。

默认情况下，此选项被选中。

## 所属库

RF Blockset / Circuit Envelope / Junctions

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014a 中引入**

## 描述

使用 S 参数对理想频率无关耦合器进行建模

Coupler 模块在电路包络环境中将四端口定向耦合器建模为理想 S 参数模型。耦合器的四个端口为 `Input port`（端口 1）、`Through port`（端口 2）、`Isolated port`（端口 3）、`Coupled port`（端口 4）。

定向耦合器用于采样沿传输线传播的前向波和反射波。定向耦合器在许多 RF 设计应用中有广泛用途，例如线路功率传感器和发射机自动电平控制。

混合耦合器用于以特定相位关系拆分或合并信号。
