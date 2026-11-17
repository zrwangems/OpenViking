---
type: simulink-block
title: 'Power Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'poweramplifier'
documentation_source_path: 'ref/poweramplifier.html'
language: zh-CN
chinese_source: worker-translation
---

# Power Amplifier

## 端口

R2025b 中未记录。

## 参数

### **Model** — 模型类型 `Memory polynomial`（默认）| `Generalized Hammerstein` | `Cross-Term Memory` | `Cross-Term Hammerstein`

模型类型，指定为 `Memory polynomial`、
`Generalized Hammerstein`、
`Cross-Term Memory` 或 `Cross-Term
Hammerstein`。下表总结了不同模型的特征：

| 模型 | 特征数据 | 系数类型 | 带内频谱再生 | 带外谐波生成 |
| --- | --- | --- | --- | --- |
| `Memory polynomial`（默认） | 带通 (I,Q) | 复数 | 是 | 否 |
| `Generalized Hammerstein` | 真实通带 | 实数 | 是 | 是 |
| `Cross-Term Memory` | 带通 (I,Q) | 复数 | 是 | 否 |
| `Cross-Term Hammerstein` | 真实通带 | 实数 | 是 | 是 |

- `Memory polynomial` – 此窄带
  记忆多项式实现（[1] 的方程 (19)）作用于输入信号的包络，不
  生成新的频率分量，并捕获带内频谱
  再生。使用此模型可创建在高频下工作的窄带放大器。

  输出信号在任何时刻都是以下维度为 Memory Depth (mem)×Voltage Order (deg) 的复数矩阵所有元素之和：

  [C11V0C12V0|V0|⋯C1,degV0|V0|deg−1C21V1C22V1|V1|⋯C2,degV1|V1|deg−1⋮⋮⋱⋮Cmem,1Vmem−1Cmem,2Vmem−1|Vmem−1|⋯Cmem,degVmem−1|Vmem−1|deg−1].

  在矩阵中，行数等于记忆项的数量，列数等于非线性的阶数。信号下标表示延迟量。
- `Generalized Hammerstein` – 此
  宽带记忆多项式实现（[1] 的方程 (18)）作用于输入信号的包络，生成
  为载波频率整数倍的新频率分量，并捕获带内频谱再生。增加
  非线性阶数会增加生成的带外频率数量。使用此模型可创建在低频下工作的
  宽带放大器。

  输出信号在任何时刻都是以下维度为 Memory Depth (mem)×Voltage Order (deg) 的实数矩阵所有元素之和：

  [C11V0C12V02⋯C1,degV0degC21V1C22V12⋯C2,degV1deg⋮⋮⋱⋮Cmem,1Vmem−1Cmem,2Vmem−12⋯Cmem,degVmem−1deg].

  在矩阵中，行数等于记忆项的数量，列数等于非线性的阶数。信号下标表示延迟量。
- `Cross-Term Memory` – 此窄带
  记忆多项式实现（[1] 的方程 (23)）作用于输入信号的包络，不
  生成新的频率分量，并捕获带内频谱
  再生。使用此模型可创建在高频下工作的窄带放大器。该模型包含前导和
  滞后记忆项，并提供记忆多项式模型的广义实现。

  输出信号在任何时刻都是通过逐元素乘积指定的矩阵所有元素之和

  **C** .\* **M**CTM，

  其中 **C** 是维度为 Memory Depth (mem)×{Memory Depth (mem)⋅(Voltage Order (deg)−1)+1} 的复数系数矩阵，并且

  MCTM=[V0V1⋮Vmem−1][1|V0||V1|⋯|Vmem−1||V0|2⋯|Vmem−1|2⋯|V0|deg−1⋯|Vmem−1|deg−1]=[V0V0|V0|V0|V1|⋯V0|Vmem−1|V0|V0|2⋯V0|Vmem−1|2⋯V0|V0|deg−1⋯V0|Vmem−1|deg−1V1V1|V0|V1|V1|⋯V1|Vmem−1|V1|V0|2⋯V1|Vmem−1|2⋯V1|V0|deg−1⋯V1|Vmem−1|deg−1⋮⋮⋮⋱⋮⋮⋱⋮⋱⋮⋱⋮Vmem−1Vmem−1|V0|Vmem−1|V1|⋯Vmem−1|Vmem−1|Vmem−1|V0|2⋯Vmem−1|Vmem−1|2⋯Vmem−1|V0|deg−1⋯Vmem−1|Vmem−1|deg−1].

在矩阵中，行数等于记忆项的数量，列数与非线性阶数和记忆项的数量成比例。信号下标表示延迟量。未出现在 `Memory polynomial` 模型中的额外列表示交叉项。

- `Cross-Term Hammerstein` – 此宽带记忆多项式实现作用于输入信号的包络，生成载波频率整数倍的频率分量，并捕获带内频谱再生。增加非线性阶数会增加生成的带外频率数量。使用此模型可创建在低频下工作的宽带放大器。

  在任何时刻，输出信号是由逐元素乘积指定的矩阵所有元素之和

  **C** .\* **M**CTH，

  其中 **C** 是维度为 Memory Depth (mem)×{Memory Depth (mem)⋅(Voltage Order (deg)−1)+1} 的复系数矩阵，且

  MCTH=[V0V1⋮Vmem−1][1V0V1⋯Vmem−1V02⋯Vmem−12⋯V0deg−1⋯Vmem−1deg−1]=[V0V02V0V1⋯V0Vmem−1V03⋯V0Vmem−12⋯V0deg⋯V0Vmem−1deg−1V1V1V0V12⋯V1Vmem−1V1V02⋯V1Vmem−12⋯V1V0deg−1⋯V1Vmem−1deg−1⋮⋮⋮⋱⋮⋮⋱⋮⋱⋮⋱⋮Vmem−1Vmem−1V0Vmem−1V1⋯Vmem−12Vmem−1V02⋯Vmem−13⋯Vmem−1V0deg−1⋯Vmem−1deg]。

  在矩阵中，行数等于记忆项的数量，列数与非线性阶数和记忆项的数量成比例。信号下标表示延迟量。未出现在 `Generalized Hammerstein` 模型中的额外列表示交叉项。

### **Coefficient Matrix** — 系数矩阵 1（默认）| 复矩阵 | 实矩阵

系数矩阵，对于 `Memory polynomial` 和 `Cross-Term Memory` 模型指定为复矩阵，对于 `Generalized Hammerstein` 和 `Cross-Term Hammerstein` 模型指定为实矩阵。

- 对于 `Memory polynomial` 和 `Cross-Term Memory` 模型，您可以基于测得的复数 (I,Q) 输出对输入放大器特性来辨识复系数矩阵。例如，请参阅 Coefficient Matrix Computation 中的辅助函数。
- 对于 `Generalized Hammerstein` 和 `Cross-Term Hammerstein` 模型，您可以基于测得的实数通带输出对输入放大器特性来辨识实系数矩阵。

矩阵的大小取决于延迟数量和系统非线性阶数。

- 对于 `Memory polynomial` 和 `Generalized Hammerstein` 模型，矩阵的维度为 Memory Depth (mem)×Voltage Order (deg)。
- 对于 `Cross-Term Memory` 和 `Cross-Term Hammerstein` 模型，矩阵的维度为 Memory Depth (mem)×{Memory Depth (mem)⋅(Voltage Order (deg)−1)+1}。

### **Measured interval of PA data (s)** — 输入输出数据的采样间隔 `1e-6`（默认）| 实正标量

输入输出数据的采样间隔，模块使用该间隔来定义系数矩阵，指定为实正标量。

**Coefficient Sample Time (s)** 参数已重命名为 **Measured interval of PA data (s)**。*（自 R2023b 起）*

**注意**

为提高模型精度，请将 **Measured interval of PA data (s)** 参数指定为等于或大于 Configuration 模块中的 **Step size** 参数。

### **Rin (ohm)** — 输入电阻 `50`（默认）| 实正标量

输入电阻，指定为实正标量。

### **Rout (ohm)** — 输出电阻 `50`（默认）| 实正标量

输出电阻，指定为实正标量。

### **Ground and hide negative terminals** — 将 RF 电路端子接地 on（默认）| off

选择此参数可将负端子接地并隐藏。清除此参数可暴露负端子。通过暴露这些端子，您可以将它们连接到模型的其它部分。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

### R2023b：Circuit Envelope 库中 Power Amplifier 模块的参数已重命名

Circuit Envelope 库中 Power Amplifier 模块的 **Coefficient Sample Time (s)** 参数已重命名为 **Measured interval of PA data (s)**。

当您打开在 R2023b 之前创建的包含 Power Amplifier 模块的模型时，软件会将 **Coefficient Sample Time (s)** 参数名称替换为 **Measured interval of PA data (s)**。

### R2021b：Power Amplifier 模块图标已更新

从 R2021b 开始，Power Amplifier 模块图标已更新。当您打开在 R2021b 之前创建的包含 Power Amplifier 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

对具有记忆效应的功率放大器进行建模

Power Amplifier 模块对双端口功率放大器进行建模。由 Volterra 级数推导出的记忆多项式表达式对输入和输出信号之间的非线性关系进行建模。该功率放大器包含记忆效应，因为输出响应取决于当前输入信号和先前时刻的输入信号。这些功率放大器在传输宽带或窄带信号时非常有用。
