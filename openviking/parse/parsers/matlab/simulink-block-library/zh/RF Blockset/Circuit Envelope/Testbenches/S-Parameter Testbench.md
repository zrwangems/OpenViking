---
type: simulink-block
title: 'S-Parameter Testbench'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Testbenches'
documentation_page: 'sparametertestbench'
documentation_source_path: 'ref/sparametertestbench.html'
language: zh-CN
chinese_source: worker-translation
---

# S-Parameter Testbench

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Use Internal Configuration block
  summary: 使用测试台内部配置模块 on（默认）| off
  group: ''
- name: Input power amplitude (dBm)
  summary: 输入到 DUT 的功率 -30（默认）| 实值标量
  group: ''
- name: Number of ports
  summary: 测量端口数 2（默认）| 标量整数
  group: ''
- name: Measure all S-parameters
  summary: 测量整个 S 参数矩阵 on（默认）| off
  group: ''
- name: Export measurement results to sNp
  summary: 将 S 参数数据保存到 Touchstone 文件 按钮
  group: ''
- name: S-Parameter elements
  summary: 要测量的 S 参数元素 [1 1]（默认）| 两列矩阵
  group: ''
- name: Workspace variable name
  summary: 用于将测量数据存储到 MATLAB 工作区的变量名 'SparamObjOut'（默认）| 字符向量
  group: ''
- name: Input frequency (Hz)
  summary: DUT 的载波频率 2.1e9（默认）| 标量
  group: ''
- name: Baseband bandwidth (Hz)
  summary: 输入信号的基带带宽 10e6（默认）| 正有限标量
  group: ''
- name: Reference Impedance (Ohm)
  summary: 用于 S 参数测量的阻抗 50（默认）| 正有限标量
  group: ''
- name: Show S-Parameter spectrum
  summary: 查看指定 S 参数在指定频率带宽上的测量值 off（默认）| on
  group: ''
- name: Ground and hide negative terminals
  summary: 在内部接地并隐藏 RF 电路端子 on（默认）| off
  group: ''
- name: FFT Length
  summary: FFT  bin 数量 128（默认）| 标量整数，2 的幂
  group: ''
- name: Measurement Time
  summary: 总时间持续时间 12.8 μs（默认）| 标量整数
  group: ''
- name: Ratio of wait time to measurement time
  summary: 顺序测量之间的间歇 0（默认）| 标量整数
  group: ''
- name: Ratio of Envelope to Baseband bandwidths
  summary: 内部求解器包络带宽与测量带宽的比值 8（默认）| 标量整数，2 的幂
  group: ''
- name: Adjust for steady state external signals
  summary: 针对大稳态外部信号进行调整 关闭（默认）| 打开
  group: ''
- name: Output frequency (Hz)
  summary: 输出载波频率 2.1e9（默认）| 正有限标量
  group: ''
- name: Approximate transient as small signal
  summary: 为瞬态小信号分析选择一小部分频率 关闭（默认）| 打开
  group: ''
- name: Use all steady-state simulation frequencies for small signal analysis
  summary: 使用为全谐波平衡非线性解自动选择的所有频率 打开（默认）| 关闭
  group: ''
- name: Small signal frequencies (Hz)
  summary: 承载小信号瞬态的频率 2.1e9（默认）| 标量 | 向量
  group: ''
- name: Populate Frequencies
  summary: 用于选择小信号瞬态频率的工具 按钮
  group: ''
```

#### 主

### **Use Internal Configuration block** — 使用测试台内部配置模块 on（默认）| off

选择以使用测试台内部配置模块。清除此参数以指定您自己的配置模块。清除此复选框将移除 **Advanced** 选项卡中的 **Approximate transient as small signal** 选项。

**注意**

使用您自己的配置模块时，步长、基频音、谐波阶数和仿真噪声等参数可能会影响测量结果。

### **Input power amplitude (dBm)** — 输入到 DUT 的功率 `-30`（默认）| 实值标量

输入到被测设备（DUT）的功率，指定为以 dBm 为单位的实值标量。您可以通过在文本框中输入值或使用旋钮选择值来更改输入功率。指定的输入功率表示 DUT 输入端口处可用的功率。有效值为 `-90` 到 `60` dBm。

当在 **Advanced** 选项卡中选中 **Approximate transient as small signal** 选项时，此参数在仿真运行期间被禁用。

**数据类型：** `double`

### **Number of ports** — 测量端口数 `2`（默认）| 标量整数

测量端口数，指定为限制在 1:128 范围内的标量整数。一旦您更改端口数，新端口将出现在模块上。

**数据类型：** `double`

### **Measure all S-parameters** — 测量整个 S 参数矩阵 on（默认）| off

选择以测量整个 S 参数矩阵。此测量通过依次激励每个端口并测量所有端口的输出来完成。当您选中此框时，**Save measurement result to .s2p** 按钮将出现在此参数下方。在这种情况下，输出信号 S 参数的维度为 *N*-by-*N*-by-*F*。*N* 是端口数，*F* 是频率数。

清除此参数以手动指定 S 参数元素。在这种情况下，输出信号 S 参数的维度为 *M*-by-*F*。*M* 是 S 参数元素的总数，*F* 是频率数。

### **Export measurement results to sNp** — 将 S 参数数据保存到 Touchstone 文件 按钮

单击以将测得的 S 参数数据保存到 Touchstone 文件。此按钮打开一个标准对话框，用于浏览和选择文件。唯一建议的文件类型是 `.sNp`，其中 *N* 是测量端口数。此按钮在第一次仿真发生之前以及仿真运行或初始化期间被禁用。它捕获先前仿真的结果。`.sNp` 中的 *N* 值对应于先前测量的端口数。

#### 依赖关系

要启用此参数，请选择 **Measure all S-parameters**。

### **S-Parameter elements** — 要测量的 S 参数元素 `[1 1]`（默认）| 两列矩阵

要测量的 S 参数元素，指定为两列矩阵。每一行代表一个 S 参数元素。第一列代表入射波端口，第二列代表散射波端口。例如，`[[2 1];[1 1]]` 表示两元素测量：S21 和 S11。您可以按任意顺序从矩阵中选择任意元素，但元素必须唯一。

#### 依赖关系

要启用此参数，请清除 **Measure all S-parameters**。

**数据类型：** `double`

### **Workspace variable name** — 用于将测量数据存储到 MATLAB 工作区的变量名 `'SparamObjOut'`（默认）| 字符向量

用于将测量数据存储到 MATLAB® 工作区的变量名，指定为字符向量。数据存储为 RF Toolbox™ `sparameters` 对象。

**数据类型：** `char`

### **Input frequency (Hz)** — DUT 的载波频率 `2.1e9`（默认）| 标量

DUT 的载波频率，指定为以 Hz 为单位的标量。默认情况下，输出频率等于输入频率，因为 S 参数测量用于量化线性系统。

对于大恒定外部信号上的小信号测量，当选中 **Adjust for steady-state external signals** 时，可以在 **Advanced** 选项卡中指定输出频率。

**数据类型：** `double`

### **Baseband bandwidth (Hz)** — 输入信号的基带带宽 `10e6`（默认）| 正有限标量

输入信号的基带带宽，指定为以 Hz 为单位的正有限标量。测量频率位于输入载波频率周围的该频带上。默认情况下，该频带比求解器包络带宽更窄，以将仿真伪影保持在测量结果之外。两个频带的比值可以使用 **Advanced** 选项卡中的 **Ratio of Envelope to Baseband bandwidths** 进行控制。

**数据类型：** `double`

### **Reference Impedance (Ohm)** — 用于 S 参数测量的阻抗 `50`（默认）| 正有限标量

用于 S 参数测量的阻抗，指定为以欧姆为单位的正有限标量。所有端口均使用相同的参考阻抗进行测量。

**数据类型：** `double`

### **Show S-Parameter spectrum** — 查看指定 S 参数在指定频率带宽上的测量值 off（默认）| on

选择此项可使用频谱分析仪查看指定 S 参数在指定频率带宽上的测量值。您可以在图中查看两种类型的曲线：`Magnitude` 或 `Real & Imag`。`Magnitude` 图显示 S 参数数据幅度，单位为 dBm。`Real & Imag` 显示 S 参数的实部和虚部。S 参数的实部和虚部图没有单位。

**注意**

要使用频谱分析仪查看 S 参数频谱，您需要 DSP System Toolbox™ 许可证。

### **Ground and hide negative terminals** — 在内部接地并隐藏 RF 电路端子 on（默认）| off

选择此项可在内部接地并隐藏负端子。清除此项可暴露负端子。通过暴露这些端子，您可以将它们连接到模型的其他部分。

#### 高级

### **FFT Length** — FFT  bin 数量 `128`（默认）| 标量整数，2 的幂

用于测量的 FFT bin 数量，指定为 2 的幂的标量整数。该值必须是 2 的整数次幂。此值控制指定带宽上测量的频谱分辨率。

### **Measurement Time** — 总时间持续时间 `12.8` μs（默认）| 标量整数

此参数为只读。

每个端口输出被测量以获得频谱结果的总时间持续时间，指定为标量整数。该值是 **Main** 选项卡中指定的 **FFT Length** 与 **Baseband bandwidth** 的比值。它让您知道，任何超过此值的系统响应都不会包含在频谱结果中。此界限是频谱分辨率限制的结果。

### **Ratio of wait time to measurement time** — 顺序测量之间的间歇 `0`（默认）| 标量整数

端口激励变化时顺序测量之间的间歇，指定为 **Measurement time** 实例数的标量整数。与实际测量类似，DUT 无法被重置以清除其内部状态。如果测量切换过快，超出 **Measurement time** 的输出可能会被收集到下一次测量中。此值有助于避免下一次测量受到污染。

### **Ratio of Envelope to Baseband bandwidths** — 内部求解器包络带宽与测量带宽的比值 `8`（默认）| 标量整数，2 的幂

内部求解器包络带宽与测量带宽之间的比值，指定为 2 的幂的标量整数。

### **Adjust for steady state external signals** — 针对大稳态外部信号进行调整 关闭（默认）| 打开

选择此项可针对大稳态外部信号进行调整，并仅测量测试台注入的小信号激励下 DUT 的线性效应。这意味着 DUT 可以包含与在每个载波的包络上时间恒定的较大信号进行混频的元件。当您选择此参数时，可以指定与输入频率不同的输出频率。

如果没有任何信号注入到测试台外部的 DUT，请清除此选项。

**注意**

DUT 不应包含任何在每个载波的包络上随时间变化的外部信号。

### **Output frequency (Hz)** — 输出载波频率 `2.1e9`（默认）| 正有限标量

输出载波频率，指定为正有限标量。

#### 依赖关系

要启用此参数，请选择 **Adjust for steady state external signals**。

### **Approximate transient as small signal** — 为瞬态小信号分析选择一小部分频率 关闭（默认）| 打开

选择此选项可为瞬态小信号分析选择一小部分频率。使用此参数可加速测量大型非线性系统在由大型外部稳态信号指定的给定工作点附近的 S 参数。

### **Use all steady-state simulation frequencies for small signal analysis** — 使用为全谐波平衡非线性解自动选择的所有频率 打开（默认）| 关闭

选择此选项可使用为全谐波平衡非线性解自动选择的所有频率。清除此选项可指定承载小信号瞬态的频率。

#### 依赖关系

要启用此参数，请选中 **Approximate transient as small signal**。

### **Small signal frequencies (Hz)** — 承载小信号瞬态的频率 `2.1e9`（默认）| 标量 | 向量

承载小信号瞬态的频率，指定为实数标量整数或向量。指定的频率应包含在完整的仿真频率集合中。如果某些频率未包含在内，则会出现警告消息。如果所有频率均未包含在内，则会出现错误消息。

#### 依赖关系

要启用此参数，请清除 **Use all steady-state simulation frequencies for small signal analysis**。

### **Populate Frequencies** — 用于选择小信号瞬态频率的工具 按钮

打开该工具以选择小信号瞬态频率，以填充 **Small signal frequencies**。所选频率是仿真频率的子集，这些仿真频率由仿真中使用的 **Fundamental tones** 和 **Harmonic order** 确定。完整的仿真频率集合在对话框右侧的组合框中给出，所选频率会高亮显示。您可以通过直接在选择框中选择频率，或在 **Small signal selection panel** 中选择所需的音调和谐波阶数，然后单击 **Select** 来进行选择。组合框中的 **Tones (Hz)** 和 **Harmonic order** 值也会使用仿真中使用的 **Fundamental tones** 和 **Harmonic order** 进行填充。

选择小信号频率窗口

#### 依赖关系

要显示此参数，请清除 **Use all steady-state simulation frequencies for small signal analysis**。
## 所属库

RF Blockset / Circuit Envelope / Testbenches

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019b 中引入**

## 描述

测量系统的 S 参数

使用 S-Parameter Testbench 模块测量通用射频系统的 S 参数数据。S 参数测试台依次向每个端口注入激励信号，并测量所有端口处的响应，以获得射频系统的散射矩阵。虽然激励信号应为小信号才能进行有意义的测量，但该测试台允许存在大幅度的稳态外部信号。
