---
type: simulink-block
title: 'Memoryless Nonlinearity'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments and Components'
documentation_page: 'memorylessnonlinearity'
documentation_source_path: 'ref/memorylessnonlinearity.html'
language: zh-CN
chinese_source: worker-translation
---

# Memoryless Nonlinearity

## 端口

### 输入

### **In1** — 输入 RF 基带信号 标量 | 列向量

输入 RF 基带信号，指定为标量或列向量。

**数据类型：** `double` | `single`
**复数支持：** 是
### 输出

### **Out1** — 输出 RF 基带信号 标量 | 列向量

输出 RF 基带信号，以标量或列向量形式返回。输出的数据类型与输入相同。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 主选项卡

### **Model** — 放大器非线性模型 `cubic`（默认）| `ampm` | `modified-rapp` | `saleh`

将放大器非线性模型指定为以下方法之一：

- `cubic`
- `ampm`
- `modified-rapp`
- `saleh`

有关详细信息，请参阅 Amplifier Model Methods。

### **Linear power gain (dB)** — 放大器的线性增益 `0`（默认）| 实数标量

线性增益，以 dB 为单位指定为标量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic` 或 `modified-rapp`。

### **Type of Non-linearity** — 非线性类型 `OIP3`（默认）| `IIP3` | `IP1dB` | `OP1dB` | `IPsat` | `OPsat`

三阶非线性类型，以 dBm 为单位，指定为以下选项之一：

- `IIP3` — 输入三阶截点
- `OIP3` — 输出三阶截点
- `IP1dB` — 输入 1 dB 压缩点
- `OP1dB` — 输出 1 dB 压缩点
- `IPsat` — 输入饱和点
- `OPsat` — 输出饱和点

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic`。

### **IIP3 (dBm)** — 输入三阶截点 `Inf`（默认）| 正实数

输入三阶截点，以 dBm 为单位指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic`，并将 **Type of Non-linearity** 设置为 `IIP3`。

### **OIP3 (dBm)** — 输出三阶截点 `Inf`（默认）| 正实数

输出三阶截点，以 dBm 为单位指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic`，并将 **Type of Non-linearity** 设置为 `OIP3`。

### **IP1dB (dBm)** — 输入 1 dB 压缩点 `Inf`（默认）| 正实数

输入 1 dB 压缩点，以 dBm 为单位指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic`，并将 **Type of Non-linearity** 设置为 `IP1dB`。

### **OP1dB (dBm)** — 输出 1 dB 压缩点 `Inf`（默认）| 正实数

输出 1 dB 压缩点，以 dBm 为单位指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic`，并将 **Type of Non-linearity** 设置为 `OP1dB`。

### **IPsat (dBm)** — 输入饱和点 `Inf`（默认）| 正实数

输入饱和点，以 dBm 为单位指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic`，并将 **Type of Non-linearity** 设置为 `IPsat`。

### **OPsat (dBm)** — 输出饱和点 `Inf`（默认）| 正实数

输出饱和点，以 dBm 为单位指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic`，并将 **Type of Non-linearity** 设置为 `OPsat`。

### **Lookup table (Pin(dBm), Pout(dBm), deg)** — 查找表 `[ -25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12 ]`（默认）| *M*×3 实数矩阵

查找表条目，指定为实数 *M*×3 矩阵。对于 AM/AM-AM/PM 模型方法，该表将矩阵第 2 列中的模型输出功率 dBm 电平和矩阵第 3 列中的模型相位变化（以度为单位）表示为与矩阵第 1 列中输入信号功率绝对值的关系。第 1 列输入功率必须单调递增。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `ampm`。

### **Output saturation level (V)** — 输出饱和电平 `1`（默认）| 正实数

电压输出饱和电平，以 dBm 为单位指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `modified-rapp`。

### **Magnitude smoothness factor** — 幅度平滑因子 `2`（默认）| 正实数

修正 Rapp 模型方法的 AM/AM 计算的幅度平滑因子，指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `modified-rapp`。

### **Phase gain (rad)** — 相位增益 `-0.45`（默认）| 实数标量

修正 Rapp 模型方法的 AM/PM 计算的相位增益，以弧度为单位指定为实数标量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `modified-rapp`。

### **Phase saturation** — 相位饱和 `0.88`（默认）| 正实数

修正 Rapp 模型方法的 AM/PM 计算的相位饱和，指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `modified-rapp`。

### **Phase smoothness factor** — 相位平滑因子 `3.43`（默认）| 正标量 | 正二元素向量

修正 Rapp 模型方法的 AM/PM 计算的相位平滑因子，指定为正标量或正二元素向量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `modified-rapp`。

### **Input scaling (dB)** — 输入信号电平的缩放因子 `0`（默认）| 非负实数

Saleh 模型方法的输入信号电平缩放因子，以 dB 为单位指定为非负实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `Saleh`。

### **AM / AM parameters [alpha beta]** — AM/AM 转换参数 `[ 2.1587, 1.1517 ]`（默认）| 二元素向量

Saleh 模型方法的 AM/AM 二元组转换参数，指定为非负实数的二元素向量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `saleh`。

### **AM / PM parameters [alpha beta]** — AM/PM 转换参数 `[ 4.0033, 9.1040 ]`（默认）| 二元素向量

Saleh 模型方法的 AM/PM 二元组转换参数，指定为实数的二元素向量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `saleh`。

### **Output scaling (dB)** — 输出信号电平的缩放因子 `0`（默认）| 非负实数

Saleh 模型方法的输出信号电平缩放因子，以 dB 为单位指定为非负实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `saleh`。

### **Reference load (ohm)** — 参考负载 `1`（默认）| 正标量

参考负载值，以欧姆为单位指定为正标量。使用此值在电压电平与信号和噪声功率电平之间进行转换。

**可调：** 是

### **Plot power characteristics** — 绘制功率特性 按钮

此按钮根据 **Model** 选项卡上指定的参数绘制功率特性。

有关详细信息，请参阅提示。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 通过使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项更快。
- `Interpreted execution` — 通过使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度比使用 `Code generation` 选项更慢。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / RF Impairments and Components

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2024b：Memory Less Nonlinearity 模块更新

该模块现在允许为修正 Rapp 模型方法使用具有独立 *q*1 和 *q*2 值的二元素相位平滑因子，如下式所示。

FAM/PM(u)=Α|u|q11+(|u|B)q2

该模块现在允许在 Saleh 模型方法的二元素 AM / PM 转换参数中使用负值。此更新使您能够在 AM / PM 损伤中表达负相位旋转。

Memoryless Nonlinearity 模块的 **Model** 参数中的值已重命名：

| 参数 | R2024b 之前的值 | R2024b 起的值 |
| --- | --- | --- |
| **Model** | `Cubic polynomial` | `cubic` |
| `AM/AM - AM/PM` | `ampm` |
| `Modified Rapp` | `modified-rapp` |
| `Saleh` | `saleh` |

**Type of Non-linearity** 参数的默认值已更改：

| 参数 | R2024b 之前的默认值 | R2024b 起的默认值 |
| --- | --- | --- |
| **Type of Non-linearity** | `IIP3` | `OIP3` |

### R2023a：为放大器建模现代化无记忆非线性

Memoryless Nonlinearity 模块更新了在对放大器建模时应用无记忆非线性损伤的方法。

该模块添加了使用查找表定义损伤设置的 AM/AM-AM/PM 模型，修改了应用三次多项式模型的参数，并将 Rapp 模型替换为修正 Rapp 模型。有关放大器模型方法的详细信息，请参阅 Amplifier Model Methods。

以下建模方法已移除：

- 双曲正切模型方法
- Ghorbani 模型方法
- 三次多项式模型方法的 AM/PM 转换设置

要查看以前的模块界面，请参阅 (Legacy) Memoryless Nonlinearity 参考页。

## 描述

将放大器模型应用于复基带信号

Memoryless Nonlinearity 模块将放大器模型应用于复基带信号。使用此模块对射频 (RF) 发射器或接收器中信号放大引起的无记忆非线性损伤进行建模。有关详细信息，请参阅 Amplifier Model Methods。
