---
type: simulink-block
title: 'Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband'
documentation_page: 'amplifieridealizedbaseband'
documentation_source_path: 'ref/amplifieridealizedbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# Amplifier

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入基带信号 实数标量 | 实数列向量 | 复数标量 | 复数列向量
  direction: input
  data_types: double | single
- name: Port_1
  summary: 输出基带信号 实数标量 | 实数列向量 | 复数标量 | 复数列向量
  direction: output
  data_types: double | single
```

### 输入

### **Port\_1** — 输入基带信号 实数标量 | 实数列向量 | 复数标量 | 复数列向量

输入基带信号，指定为实数标量、实数列向量、复数标量或复数列向量。

**数据类型：** `double` | `single`
### 输出

### **Port\_1** — 输出基带信号 实数标量 | 实数列向量 | 复数标量 | 复数列向量

输出基带信号，指定为实数标量、实数列向量、复数标量或复数列向量。输出端口模仿输入端口的属性。例如，如果输入基带信号指定为数据类型为 double 的实数标量，则输出基带信号也指定为数据类型为 double 的实数信号。

**数据类型：** `double` | `single`
## 参数
```yaml
parameters:
- name: Model
  summary: 放大器非线性模型 cubic（默认）| ampm | modified-rapp | saleh
  group: 主选项卡
- name: Linear power gain (dB)
  summary: 放大器线性增益 0（默认）| 实数标量
  group: 主选项卡
- name: Type of Non-Linearity
  summary: 三阶非线性类型 OIP3（默认）| IIP3 | IP1dB | OP1dB | IPsat | OPsat
  group: 主选项卡
- name: IIP3 (dBm)
  summary: 输入三阶截点 Inf（默认）| 正实数
  group: 主选项卡
- name: OIP3 (dBm)
  summary: 输出三阶截点 Inf（默认）| 正实数
  group: 主选项卡
- name: IP1dB (dBm)
  summary: 输入 1 dB 压缩点 Inf（默认）| 正实数
  group: 主选项卡
- name: OP1dB (dBm)
  summary: 输出 1 dB 压缩点 Inf（默认）| 正实数
  group: 主选项卡
- name: IPsat (dBm)
  summary: 输入饱和点 Inf（默认）| 正实数
  group: 主选项卡
- name: OPsat (dBm)
  summary: 输出饱和点 Inf（默认）| 正实数
  group: 主选项卡
- name: Simulate using
  summary: 指定要运行的仿真类型 Code generation（默认）| Interpreted execution
  group: 主选项卡
- name: Plot power characteristics
  summary: 绘制功率特性按钮（默认）
  group: 主选项卡
- name: Lookup table (Pin(dBm), Pout(dBm), deg)
  summary: 查找表 [ -25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12 ]（默认）| *M*×3 实数矩阵
  group: 主选项卡
- name: Output saturation level (V)
  summary: 输出饱和电平 1（默认）| 正实数
  group: 主选项卡
- name: Magnitude smoothness factor
  summary: 幅度平滑因子 2（默认）| 正实数
  group: 主选项卡
- name: Phase gain (rad)
  summary: 相位增益 -0.45（默认）| 实数标量
  group: 主选项卡
- name: Phase saturation
  summary: 相位饱和 0.88（默认）| 正实数
  group: 主选项卡
- name: Phase smoothness factor
  summary: 相位平滑因子 [3.43, 3.43]（默认）| 正实数 | 二元组向量
  group: 主选项卡
- name: Input scaling (dB)
  summary: 输入信号电平的缩放因子 0（默认）| 非负实数
  group: 主选项卡
- name: AM / AM parameters [alpha beta]
  summary: AM/AM 转换参数 [ 2.1587, 1.1517 ]（默认）| 二元素向量
  group: 主选项卡
- name: AM / PM parameters [alpha beta]
  summary: AM/PM 转换参数 [ 4.0033, 9.1040 ]（默认）| 二元素向量
  group: 主选项卡
- name: Output scaling (dB)
  summary: 输出信号电平的缩放因子 0（默认）| 非负实数
  group: 主选项卡
- name: Include Noise
  summary: 向系统添加噪声 off（默认）| on
  group: 噪声选项卡
- name: Specify noise type
  summary: 噪声表示方式 NF（默认）| noise-temperature | noise-factor
  group: 噪声选项卡
- name: Noise temperature (K)
  summary: 用于对放大器中的噪声建模的噪声温度 290（默认）| 非负实数
  group: 噪声选项卡
- name: Noise figure (dB)
  summary: 用于对放大器中的噪声建模的噪声系数 10 * log10( 2 )（默认）| 非负实数
  group: 噪声选项卡
- name: Noise factor
  summary: 用于对放大器中的噪声建模的噪声因子 2（默认）| 大于或等于 1 的正整数标量
  group: 噪声选项卡
- name: Seed source
  summary: 初始种子的来源 auto（默认）| user
  group: 噪声选项卡
- name: Seed
  summary: 随机数生成器的种子 67987（默认）| 非负整数
  group: 噪声选项卡
```

### 主选项卡

### **Model** — 放大器非线性模型 `cubic`（默认）| `ampm` | `modified-rapp` | `saleh`

将放大器非线性模型指定为以下之一：

- `cubic` — 三次多项式模型使用线性功率增益确定三阶多项式的线性系数，并使用 IP3、P1dB 或 Psat 之一确定多项式的三阶系数。
- `ampm` — AM/AM-AM/PM 模型使用查找表计算放大器功率特性。
- `modified-rapp` — 修正 Rapp 模型使用归一化传递函数计算放大器功率特性。
- `saleh` — Saleh 模型也使用归一化传递函数计算放大器功率特性。

有关详细信息，请参阅 Idealized Amplifier 模块中的非线性模型。

### **Linear power gain (dB)** — 放大器线性增益 `0`（默认）| 实数标量

线性增益，以 dB 为单位指定为标量。

### **Type of Non-Linearity** — 三阶非线性类型 `OIP3`（默认）| `IIP3` | `IP1dB` | `OP1dB` | `IPsat` | `OPsat`

三阶非线性类型，指定为 `IIP3`、`OIP3`、`IP1dB`、`OP1dB`、`IPsat` 或 `OPsat`。

### **IIP3 (dBm)** — 输入三阶截点 `Inf`（默认）| 正实数

输入三阶截点，以 dBm 为单位指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic`，并将 **Type of Non-Linearity** 设置为 `IIP3`。

### **OIP3 (dBm)** — 输出三阶截点 `Inf`（默认）| 正实数

输出三阶截点，以 dBm 为单位指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic`，并将 **Type of Non-Linearity** 设置为 `OIP3`。

### **IP1dB (dBm)** — 输入 1 dB 压缩点 `Inf`（默认）| 正实数

输入 1 dB 压缩点，以 dBm 为单位指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic`，并将 **Type of Non-Linearity** 设置为 `IP1dB`。

### **OP1dB (dBm)** — 输出 1 dB 压缩点 `Inf`（默认）| 正实数

输出 1 dB 压缩点，以 dBm 为单位指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic`，并将 **Type of Non-Linearity** 设置为 `OP1dB`。

### **IPsat (dBm)** — 输入饱和点 `Inf`（默认）| 正实数

输入饱和点，以 dBm 为单位指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic`，并将 **Type of Non-Linearity** 设置为 `IPsat`。

### **OPsat (dBm)** — 输出饱和点 `Inf`（默认）| 正实数

输出饱和点，以 dBm 为单位指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `cubic`，并将 **Type of Non-Linearity** 设置为 `OPsat`。

### **Simulate using** — 指定要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` – 使用生成的 C 代码仿真模型。
  首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真将复用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution`。
- `Interpreted execution` – 使用 MATLAB® 解释器仿真模型。此选项缩短了启动时间，但后续仿真的速度慢于 `Code generation`。在此模式下，您可以调试模块的源代码。

### **Plot power characteristics** — 绘制功率特性按钮（默认）

此按钮根据 **Main** 选项卡上指定的参数绘制功率特性。

有关详细信息，请参阅 Plot Power Characteristics。

### **Lookup table (Pin(dBm), Pout(dBm), deg)** — 查找表 `[ -25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12 ]`（默认）| *M*×3 实数矩阵

查找表条目，指定为实数 *M*×3 矩阵。对于 AM/AM - AM/PM 模型，此表将矩阵第 2 列中的模型输出功率 dBm 电平和矩阵第 3 列中的模型相位变化（以度为单位）表示为与矩阵第 1 列中输入信号功率绝对值的关系。第 1 列的输入功率必须单调递增。

使用采用 `linear` 方法的 `interp1` 函数对查找表中指定的数据点进行外插和内插。此外，对于外插小于查找表中最小指定输入功率值的输入数据点，AM/AM 外插使用斜率为 1，并使用等于最小输入功率相位的恒定相位值。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `ampm`。

### **Output saturation level (V)** — 输出饱和电平 `1`（默认）| 正实数

电压输出饱和电平，指定为以 dBm 表示的正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `modified-rapp`。

### **Magnitude smoothness factor** — 幅度平滑因子 `2`（默认）| 正实数

用于 `modified-rapp` 放大器模型 AM/AM 计算的幅度平滑因子，指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `modified-rapp`。

### **Phase gain (rad)** — 相位增益 `-0.45`（默认）| 实数标量

用于 `modified-rapp` 放大器模型 AM/PM 计算的相位增益，指定为以弧度表示的实数标量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `modified-rapp`。

### **Phase saturation** — 相位饱和 `0.88`（默认）| 正实数

用于 `modified-rapp` 放大器模型 AM/PM 计算的相位饱和，指定为正实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `modified-rapp`。

### **Phase smoothness factor** — 相位平滑因子 `[3.43, 3.43]`（默认）| 正实数 | 二元组向量

用于 `modified-rapp` 放大器模型 AM/PM 计算的相位平滑因子，指定为正实数或二元组向量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `modified-rapp`。

### **Input scaling (dB)** — 输入信号电平的缩放因子 `0`（默认）| 非负实数

用于 `saleh` 放大器模型的输入信号电平缩放因子，指定为以 dB 表示的非负实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为 `saleh`。

### **AM / AM parameters [alpha beta]** — `AM/AM` 转换参数 `[ 2.1587, 1.1517 ]`（默认）| 二元素向量

用于 `saleh` 放大器模型的 AM/AM 二元组转换参数，指定为非负实数的二元素向量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为
`saleh`。

### **AM / PM parameters [alpha beta]** — `AM/PM` 转换参数 `[ 4.0033, 9.1040 ]`（默认）| 二元素向量

用于 `saleh` 放大器模型的 `AM/PM` 二元组转换参数，指定为非负实数的二元素向量。

#### 依赖关系

要启用此参数，请将 **Model** 设置为
`saleh`。

### **Output scaling (dB)** — 输出信号电平的缩放因子 `0`（默认）| 非负实数

用于 `saleh` 放大器模型的输出信号电平缩放因子，指定为以 dB 为单位的非负实数。

#### 依赖关系

要启用此参数，请将 **Model** 设置为
`saleh`。

### 噪声选项卡

### **Include Noise** — 向系统添加噪声 `off`（默认）| `on`

选择此参数以向输入信号添加系统噪声。选择此参数后，与 **Noise** 选项卡关联的参数将显示。

### **Specify noise type** — 噪声表示方式 `NF`（默认）| `noise-temperature` | `noise-factor`

噪声类型，指定为以下之一：

- `noise-temperature` — 噪声温度
- `NF` — 噪声系数
- `noise-factor` — 噪声因子

有关详细信息，请参阅 Idealized Amplifier 模块中的 Thermal Noise Simulations。

#### 依赖关系

要启用此参数，请选择 **Include Noise**。

### **Noise temperature (K)** — 用于对放大器中的噪声建模的噪声温度 `290`（默认）| 非负实数

用于对放大器中的噪声建模的噪声温度，指定为以度（K）为单位的非负实数。

#### 依赖关系

要启用此参数，请选择 **Include Noise** 并将 **Specify noise type** 设置为
`noise-temperature`。

### **Noise figure (dB)** — 用于对放大器中的噪声建模的噪声系数 `10 * log10( 2 )`（默认）| 非负实数

用于对放大器中的噪声建模的噪声系数，指定为以 dB 为单位的非负实数。

#### 依赖关系

要启用此参数，请选择 **Include Noise** 并将 **Specify noise type** 设置为
`NF`。

### **Noise factor** — 用于对放大器中的噪声建模的噪声因子 `2`（默认）| 大于或等于 1 的正整数标量

用于对放大器中的噪声建模的噪声因子，指定为大于或等于 1 的正整数标量。

#### 依赖关系

要启用此参数，请选择 **Include Noise** 并将 **Specify noise type** 设置为
`noise-factor`。

### **Seed source** — 初始种子的来源 `auto`（默认）| `user`

用于准备高斯随机数噪声发生器的初始种子来源，指定为以下之一：

- `auto` - 当 **Seed source** 设置为
  `auto` 时，每个放大器实例的种子使用随机数生成器生成。该实例的重置方法无效。
- `user` - 当 **Seed source** 设置为
  `user` 时，**Seed** 中提供的值用于初始化随机数生成器，并且重置方法使用 **Seed** 属性值重置随机数生成器。

### **Seed** — 随机数生成器的种子 `67987`（默认）| 非负整数

随机数生成器的种子，指定为小于
232 的非负整数。使用此值初始化随机数生成器。

#### 依赖关系

要启用此参数，请点击 **Include Noise** 复选框并在 **Seed source** 参数中选择 `user`。
## 所属库

RF Blockset / Idealized Baseband

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024b：理想化基带库中 Amplifier 模块的参数已重命名

理想化基带库中 Amplifier 模块的以下参数值已重命名：

| 参数 | R2024b 之前的值 | R2024b 起的值 |
| --- | --- | --- |
| **Model** | `Cubic polynomial` | `cubic` |
| `AM/AM - AM/PM` | `ampm` |
| `Modified Rapp` | `modified-rapp` |
| `Saleh` | `saleh` |
| **Specify noise type** | `Noise figure` | `NF` |
| `Noise temperature` | `noise-temperature` |
| `Noise factor` | `noise-factor` |
| **Seed source** | `Auto` | `auto` |
| `User specified` | `user` |

理想化基带库中 Amplifier 模块的以下默认值已更改：

| 参数 | R2024b 之前的默认值 | R2024b 起的默认值 |
| --- | --- | --- |
| **Type of Non-linearity** | `IIP3` | `OIP3` |
| **Specify noise type** | `Noise temperature` | `NF` |

当您打开在 R2024b 之前创建的包含 Amplifier 模块的模型时，软件会按表中所示替换参数名称和值。

## 描述

带噪声和非线性的放大器的复基带模型

Amplifier 模块生成带热噪声的放大器的复基带模型。
该模块提供四种非线性模型和三种指定噪声表示的选项。
