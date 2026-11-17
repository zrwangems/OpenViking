---
type: simulink-block
title: 'Outport'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Utilities'
documentation_page: 'outport'
documentation_source_path: 'ref/outport.html'
language: zh-CN
chinese_source: worker-translation
---

# Outport

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Sensor type
  summary: 传感器测量的信号类型 Ideal voltage（默认）| Ideal current | Power
  group: ''
- name: Load impedance (Ohm)
  summary: RF 电路的负载阻抗 inf（默认）| 以欧姆为单位的正整数向量
  group: ''
- name: Output
  summary: 输出信号的格式 Complex Baseband（默认）| In-phase and Quadrature Baseband | Magnitude and Angle Baseband | Real Passband
  group: ''
- name: Automatically compute output step size
  summary: 确定用于解析所列最高载波频率的最优时间步长 on（默认）| off
  group: ''
- name: Step size
  summary: 时间步长 1e-6 s（默认）| 以秒为单位的正整数
  group: ''
- name: Interpolation Filter Half Polyphase Length
  summary: 滤波器的半多相长度 12（默认）| 非负整数
  group: ''
- name: Carrier frequencies
  summary: 载波频率 0 Hz（默认）| 以 Hz 为单位的正整数向量
  group: ''
- name: Ground and hide negative terminals
  summary: 接地 RF 电路端子 on（默认）| off
  group: ''
```

### **Sensor type** — 传感器测量的信号类型 `Ideal voltage`（默认）| `Ideal current` | `Power`

传感器测量的信号类型，指定为：

- `Ideal voltage` — 该模块以 **Output** 参数指定的格式输出指定 **Carrier frequencies** 处电压信号的调制。这是推荐的选项，可在不增加负载阻抗和改变匹配条件的情况下感测信号。
- `Ideal current` — 该模块以 **Output** 参数指定的格式输出指定 **Carrier frequencies** 处电流信号的调制。
- `Power` — 该模块输出指定 **Carrier frequencies** 处电压信号的调制，并相对于指定的负载阻抗进行缩放。这是推荐的选项，用于感测在 RF Blockset 50 欧姆环境或其他参考阻抗中生成的信号。当您使用功率选项时，输出端口会自动在您的电路中插入负载阻抗。

  Re(Zl)Zlv(t)

  其中 *Zl* 是 **Load impedance (Ohm)** 参数的值。

### **Load impedance (Ohm)** — RF 电路的负载阻抗 `inf`（默认）| 以欧姆为单位的正整数向量

用于测量信号功率的 RF 电路负载阻抗，指定为以欧姆为单位的正整数向量。当您使用功率选项时，输出端口会自动在您的电路中插入负载阻抗。当您在给定电路的同一节点上使用多个 Outport 模块作为功率源时，产生的负载是指定负载阻抗的并联组合。

#### 依赖关系

要启用此参数，请在 **Sensor type** 中选择 `Power`。

### **Output** — 输出信号的格式 `Complex Baseband`（默认）| `In-phase and Quadrature Baseband` | `Magnitude and Angle Baseband` | `Real Passband`

输出信号的格式，指定为以下之一：

- `Complex Baseband` — 该模块在标记为 **SL** 的端口输出复值信号向量 *Ik*(*t*) + *j* · *Qk*(*t*)。向量的第 *k* 个元素是 **Carrier frequencies** 参数指定的第 *k* 个频率。
- `In-phase and Quadrature Baseband` — 该模块分别在 **I** 端口和 **Q** 端口输出两个实值信号向量 *Ik*(*t*) 和 *Qk*(*t*)。**I** 端口上的信号包含同相分量，**Q** 端口上的信号包含正交分量。向量的第 *k* 个元素是 **Carrier frequencies** 参数指定的第 *k* 个频率。载波频率等于 0 Hz 的信号的正交分量为零。
- `Magnitude and Angle Baseband` — 该模块输出两个实值向量，其元素为调制的幅度和相位角。**Mag** 端口输出 |*Ik*(*t*) + *j* · *Qk*(*t*)|，**Ang** 端口输出 Arg[*Ik*(*t*) + *j* · *Qk*(*t*)]。向量的第 *k* 个元素是 **Carrier frequencies** 参数指定的第 *k* 个频率。
- `Real Passband` — 该模块通过组合 **Carrier frequencies** 下列出的所有频率的包络和载波信号来输出实通带信号。使用 `Real Passband` 选项时，求解器采用足够小的时间步长来解析载波。因此，包络仿真带来的仿真速度提升可能有限。

  out=Real(∑k=1N(Ik(t)+j·Qk(t))·ej2πfkt)

  其中 `t` 是 **Load impedance (Ohm)** 参数的值。

### **Automatically compute output step size** — 确定用于解析所列最高载波频率的最优时间步长 `on`（默认）| `off`

确定用于解析所列最高载波频率的最优时间步长，指定为 `on` 或 `off`。选择此参数以允许 RF Blockset 确定用于解析所列最高载波频率的最优时间步长。清除此参数选择以输入步长值。

### **Step size** — 时间步长 `1e-6 s`（默认）| 以秒为单位的正整数

时间步长，指定为以秒为单位的正整数。步长应足够小以解析最快的载波信号。该步长有助于避免通带输出欠采样和混叠效应。

将时间步长值设置为 `-1` 以继承 Configuration 模块中 `Step size` 指定的时间步长。

### **Interpolation Filter Half Polyphase Length** — 滤波器的半多相长度 `12`（默认）| 非负整数

*自 R2023a 起*

滤波器的半多相长度，指定为非负整数。将半多相长度设置为大于零的值，以减轻实数通带输出上不需要的频谱镜像。如果将此参数设置为 `0`，则模块不进行滤波。

#### 依赖关系

要启用此参数，请将 **Output** 设置为 `Real Passband`。

### **Carrier frequencies** — 载波频率 `0 Hz`（默认）| 以 Hz 为单位的正整数向量

载波频率，指定为以 Hz 为单位的正整数向量。在载波频率中，元素是 Configuration 模块中基频音及其对应谐波的组合。

### **Ground and hide negative terminals** — 接地 RF 电路端子 `on`（默认）| `off`

接地 RF 电路端子，指定为 `on` 或 `off`。选择此参数以接地并隐藏负端子。清除此参数以暴露负端子。通过暴露这些端子，您可以将它们连接到模型的其他部分。

默认情况下，此选项处于选中状态。
## 所属库

RF Blockset / Circuit Envelope / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2010b 中引入**

### R2023a: Outport 模块中用于实数通带输出的 FIR 插值滤波器

Outport 模块现在支持用于实数通带输出的 FIR 插值滤波器，以减轻不需要的频谱镜像。

### R2022b: Outport 模块图标已更新

Outport 模块图标现在根据您如何设置 **Sensor type**、**Ground and hide negative terminals** 和 **Output** 参数而变化。当您打开在 R2022b 之前创建的包含 Outport 模块的模型时，软件会将模块图标替换为 R2022b 版本。

### R2021b: Outport 模块图标已更新

Outport 模块图标在 R2021b 中已更新。当您打开在 R2021b 之前创建的包含 Outport 模块的模型时，软件会将模块图标替换为 R2021b 版本。

## 描述

将 RF Blockset 信号转换为 Simulink 输出信号

Outport 模块在 RF Blockset™ 电路包络仿真环境中将载波调制信号输出为 Simulink® 信号。有关 RF 仿真的介绍，请参阅示例 Simulate High Frequency Components。

输出端口感测电流和电压的复包络或实通带信号。复基带信号由以每个指定中心频率 *fk* 为中心的同相（*Ik*）和正交（*Qk*）分量组成。**Sensor type** 参数决定模块测量哪个信号，**Output** 参数定义 Simulink 信号的格式。有关详细信息，请参阅 How to Use Outport Block。

Outport 模块图标是动态的，显示输出信号的当前格式。有关详细信息，请参阅 Outport Block Icons。

**注意**

Outport 模块的 `Real passband` 输出不支持基于帧的处理（由 Configuration 模块支持）。如果 Configuration 模块中的 **Samples per frame** 大于 1，此模块将报错。
