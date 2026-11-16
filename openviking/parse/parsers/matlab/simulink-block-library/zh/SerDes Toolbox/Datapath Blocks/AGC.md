---
type: simulink-block
title: 'AGC'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Datapath Blocks'
documentation_page: 'agc'
documentation_source_path: 'ref/agc.html'
language: zh-CN
chinese_source: worker-translation
---

# AGC

## 端口

### 输入

### **WaveIn** — 输入基带信号 标量 | 向量

输入基带信号。输入信号可以是按样本指定的标量信号，也可以是冲激响应向量信号。

**数据类型：** `double`
### 输出

### **WaveOut** — 估计的信道输出 标量 | 向量

估计的信道输出。如果输入信号是以标量形式指定的逐样本信号，则输出也是标量。如果输入信号是冲激响应向量信号，则输出也是向量。

**数据类型：** `double`

## 参数

### **Mode** — AGC 工作模式 `On`（默认）| `Off`

AGC 工作模式：

- `Off` — AGC 被旁路，输入波形保持不变。
- `On` — AGC 调整输入波形的增益，以在输出波形中维持 **Target RMS voltage**。

#### 编程用法

- 使用 `get_param(gcb,'Mode')` 查看当前 AGC **Mode**。
- 使用 `set_param(gcb,'Mode',value)` 将 AGC 设置为特定 **Mode**。

### **Target RMS voltage (V)** — 输出波形的期望 RMS 电压 `0.3`（默认）| [0.003, 10] 范围内的实数标量

输出波形的期望 RMS 电压，指定为 [0.003, 10] 范围内的实数标量，单位为 V。

#### 编程用法

- 使用 `get_param(gcb,'TargetRMSVoltage')` 查看 **Target RMS voltage (V)** 的当前值。
- 使用 `set_param(gcb,'TargetRMSVoltage',value)` 将 **Target RMS voltage (V)** 设置为特定值。

**数据类型：** `double`

### **Maximum gain** — 允许的最大 AGC 增益 `10`（默认）| 正实数标量

允许的最大 AGC 增益，指定为正实数标量。**Maximum gain** 为自适应算法提供稳定的启动。

#### 编程用法

- 使用 `get_param(gcb,'MaxGain')` 查看 **Maximum gain** 的当前值。
- 使用 `set_param(gcb,'MaxGain',value)` 将 **Maximum gain** 设置为特定值。

**数据类型：** `double`

### **Averaging length** — 用于 RMS 计算的平均长度 `100`（默认）| 正实数标量

平均长度，指定为正实数整数。**Averaging length** 定义对输入信号进行 RMS 计算所覆盖的符号数量。

#### 编程用法

- 使用 `get_param(gcb,'AveragingLength')` 查看 **Averaging length** 的当前值。
- 使用 `set_param(gcb,'AveragingLength',value)` 将 **Averaging length** 设置为特定值。

**数据类型：** `double`

#### IBIS-AMI 参数

### **Mode** — 在 IBIS-AMI 模型中包含 Mode 参数 on（默认）| off

选择以将 **Mode** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Mode**，则会将其从 AMI 文件中移除，实际上将 **Mode** 硬编码为其当前值。

### **Target RMS voltage** — 在 IBIS-AMI 模型中包含 Target RMS voltage 参数 on（默认）| off

选择以将 **Target RMS voltage** 作为参数包含在 IBIS-AMI 文件中。如果取消选择 **Target RMS voltage**，则会将其从 AMI 文件中移除，实际上将 **Target RMS voltage** 硬编码为其当前值。

## 所属库

SerDes Toolbox / Datapath Blocks

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

自动调整增益以维持输出波形幅度

AGC 模块对输入波形应用自适应可变增益，以实现期望的 RMS 输出电压。AGC 在指定数量的符号上对 RMS 电压进行平均，通过增大或减小增益或保持增益不变来执行自动增益控制 (AGC)。
