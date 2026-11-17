---
type: simulink-block
title: 'Analog Channel'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'analogchannel'
documentation_source_path: 'ref/analogchannel.html'
language: zh-CN
chinese_source: worker-translation
---

# Analog Channel

## 端口
```yaml
ports:
- name: WaveIn
  summary: 输入信号 标量 | 向量
  direction: input
  data_types: double
- name: WaveOut
  summary: 修改后的输出数据 标量 | 向量
  direction: output
  data_types: double
```

### 输入

### **WaveIn** — 输入信号 标量 | 向量

输入信号，指定为波形。

**数据类型：** `double`
### 输出

### **WaveOut** — 修改后的输出数据 标量 | 向量

修改后的输出数据，根据 [1] 中概述的方法，包含有损印刷电路板传输线模型的影响。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Channel model
  summary: 信道模型来源 Loss model（默认）| Impulse response
  group: Channel Model
- name: Target frequency (Hz)
  summary: 期望信道损耗对应的频率 20e9（默认）| 正实数标量
  group: Channel Model
- name: Loss (dB)
  summary: 目标频率处的信道损耗 8（默认）| 标量
  group: Channel Model
- name: Impedance (Ohms)
  summary: 信道特征阻抗 正实数标量
  group: Channel Model
- name: Impulse response
  summary: 用户提供的冲激响应 [zeros(1,63),1/SampleInterval,zeros(1,192)]（默认）| 矩阵
  group: Channel Model
- name: Impulse sample interval
  summary: 用户提供的冲激响应的采样间隔 6.25e-12（默认）| 正实数标量
  group: Channel Model
- name: Tx R (Ohms)
  summary: 发送器模拟模型的单端阻抗 50（默认）| 非负实数标量
  group: Channel Model
- name: Tx C (F)
  summary: 发送器模拟模型的电容 100e-15（默认）| 非负实数标量
  group: Channel Model
- name: Rx R (Ohms)
  summary: 接收器模拟模型的单端阻抗 50（默认）| 非负实数标量
  group: Channel Model
- name: Rx C (F)
  summary: 接收器模拟模型的电容 200e-15（默认）| 非负实数标量
  group: Channel Model
- name: Rise time (s)
  summary: 激励输入的 20%−80% 上升时间 10e-12（默认）| 正实数标量
  group: Channel Model
- name: Voltage (V)
  summary: 发送器模拟模型输入的峰峰值电压 1（默认）| 正实数标量
  group: Channel Model
- name: Include crosstalk
  summary: 在仿真中包含串扰 off（默认）| on
  group: 串扰
- name: Specification
  summary: 指定近端和远端干扰源的幅度 100GBASE-CR4（默认）| CEI-25G-LR | CEI-28G-SR | CEI-28G-VSR | Custom
  group: 串扰
- name: Far end crosstalk ICN (V)
  summary: 远端干扰源的期望积分噪声水平 15e-3（默认）| 非负实数标量
  group: 串扰
- name: Near end crosstalk ICN (V)
  summary: 近端干扰源期望的集成噪声水平 10e-3（默认）| 非负实数标量
  group: 串扰
- name: Symbol Time (s)
  summary: 远端串扰激励的符号时间 100e-12（默认）| 正实数标量
  group: 串扰
- name: Delay (s)
  summary: 远端串扰激励的延迟偏移 0（默认）| 非负实数标量
  group: 串扰
- name: Modulation
  summary: 远端串扰激励的调制电平 NRZ（默认）| PAM3 | PAM4 | PAM5 | PAM6 | PAM7 | PAM8 | PAM9 | PAM10 | PAM11 | PAM12 | PAM13 | PAM14 | PAM15
    | PAM16
  group: 串扰
- name: PRBS Order
  summary: 远端串扰激励的 PRBS 阶数 7（默认）| 9 | 11 | 13 | 15 | 20 | 23 | 31 | 47
  group: 串扰
- name: Symbol Time (s)
  summary: 近端串扰激励的符号时间 100e-12（默认）| 正实数标量
  group: 串扰
- name: Delay (s)
  summary: 近端串扰激励的延迟偏移 0（默认）| 非负实数标量
  group: 串扰
- name: Modulation
  summary: 近端串扰激励的调制电平 NRZ（默认）| PAM3 | PAM4 | PAM5 | PAM6 | PAM7 | PAM8 | PAM9 | PAM10 | PAM11 | PAM12 | PAM13 | PAM14 | PAM15
    | PAM16
  group: 串扰
- name: PRBS Order
  summary: 近端串扰激励的 PRBS 阶数 9（默认）| 7 | 11 | 13 | 15 | 20 | 23 | 31 | 47
  group: 串扰
```

### Channel Model

### **Channel model** — 信道模型来源 `Loss model`（默认）| `Impulse response`

信道模型来源。

- 选择 `Loss model` 以从损耗模型对模拟信道进行建模。
- 选择 `Impulse response` 以从冲激响应对模拟信道进行建模。

#### 编程使用

- 使用 `get_param(gcb,'ChannelType')` 查看当前的 **Channel model**。
- 使用 `set_param(gcb,'ChannelType',value)` 设置特定的 **Channel model**。

### **Target frequency (Hz)** — 期望信道损耗对应的频率 `20e9`（默认）| 正实数标量

期望信道损耗对应的频率，指定为以赫兹为单位的正实数标量。它对应于系统的奈奎斯特频率。

#### 依赖关系

此参数仅在 **Channel model** 选择 `Loss model` 时可用。

#### 编程使用

- 使用 `get_param(gcb,'TargetFrequency')` 查看 **Target frequency (Hz)** 的当前值。
- 使用 `set_param(gcb,'TargetFrequency',value)` 将 **Target frequency (Hz)** 设置为特定值。

**数据类型：** `double`

### **Loss (dB)** — 目标频率处的信道损耗 `8`（默认）| 标量

目标频率处的信道损耗，指定为以 dB 为单位的标量。

#### 依赖关系

此参数仅在 **Channel model** 选择 `Loss model` 时可用。

#### 编程使用

- 使用 `get_param(gcb,'Loss')` 查看 **Loss (dB)** 的当前值。
- 使用 `set_param(gcb,'Loss',value)` 将 **Loss (dB)** 设置为特定值。

**数据类型：** `double`

### **Impedance (Ohms)** — 信道特征阻抗 正实数标量

信道的特征阻抗，指定为以欧姆为单位的正实数标量。**Impedance (Ohms)** 取决于 SerDes Designer 应用或 Configuration 模块中 **Configuration** 选项卡下 **Signaling** 的设置。

- 如果 **Signaling** 设置为 `Differential`，**Impedance (Ohms)** 的默认值为 `100`。
- 如果 **Signaling** 设置为 `Single-ended`，**Impedance (Ohms)** 的默认值为 `50`。

#### 依赖关系

此参数仅在 **Channel model** 选择 `Loss model` 时可用。

#### 编程使用

- 使用 `get_param(gcb,'Zc')` 查看 **Impedance** 的当前值。
- 使用 `set_param(gcb,'Zc',value)` 将 **Impedance** 设置为特定值。

**数据类型：** `double`

### **Impulse response** — 用户提供的冲激响应 `[zeros(1,63),1/SampleInterval,zeros(1,192)]`（默认）| 矩阵

用户提供的冲激响应，指定为无量纲矩阵。**Impulse response** 用于根据用户定义的系统冲激响应构建信道损耗模型。

您可以使用用户指定的冲激响应来定义自己的串扰。如果您决定从自定义冲激响应中包含串扰，您可以在冲激响应中指定最多六个串扰激励作为新列。

#### 依赖关系

此参数仅在 **Channel model** 选择 `Impulse response` 时可用。

#### 编程使用

- 使用 `get_param(gcb,'ImpulseResponse')` 查看 **Impulse response** 的当前值。
- 使用 `set_param(gcb,'ImpulseResponse',value)` 将 **Impulse response** 设置为特定值。

**数据类型：** `double`

### **Impulse sample interval** — 用户提供的冲激响应的采样间隔 `6.25e-12`（默认）| 正实数标量

用户提供的冲激响应的采样间隔，指定为以秒为单位的正实数标量。

**数据类型：** `double`

#### Analog Model

### **Tx R (Ohms)** — 发送器模拟模型的单端阻抗 `50`（默认）| 非负实数标量

发送器模拟模型的单端阻抗，指定为非负实数标量，单位为欧姆。

#### 程序化使用

- 使用 `get_param(gcb,'TxR')` 查看 **Tx R (Ohms)** 的当前值。
- 使用 `set_param(gcb,'TxR',value)` 将 **Tx R (Ohms)** 设置为特定值。

**数据类型：** `double`

### **Tx C (F)** — 发送器模拟模型的电容 `100e-15`（默认）| 非负实数标量

发送器模拟模型的电容，指定为非负实数标量，单位为法拉。

#### 程序化使用

- 使用 `get_param(gcb,'TxC')` 查看 **Tx C (F)** 的当前值。
- 使用 `set_param(gcb,'TxC',value)` 将 **Tx C (F)** 设置为特定值。

**数据类型：** `double`

### **Rx R (Ohms)** — 接收器模拟模型的单端阻抗 `50`（默认）| 非负实数标量

接收器模拟模型的单端阻抗，指定为非负实数标量，单位为欧姆。

#### 程序化使用

- 使用 `get_param(gcb,'RxR')` 查看 **Rx R (Ohms)** 的当前值。
- 使用 `set_param(gcb,'RxR',value)` 将 **Rx R (Ohms)** 设置为特定值。

**数据类型：** `double`

### **Rx C (F)** — 接收器模拟模型的电容 `200e-15`（默认）| 非负实数标量

接收器模拟模型的电容，指定为非负实数标量，单位为法拉。

#### 程序化使用

- 使用 `get_param(gcb,'RxC')` 查看 **Rx C (F)** 的当前值。
- 使用 `set_param(gcb,'RxC',value)` 将 **Rx C (F)** 设置为特定值。

**数据类型：** `double`

### **Rise time (s)** — 激励输入的 20%−80% 上升时间 `10e-12`（默认）| 正实数标量

发送器模拟模型激励输入的 20%−80% 上升时间，指定为正实数标量，单位为秒。

#### 程序化使用

- 使用 `get_param(gcb,'RiseTime')` 查看 **Rise time (s)** 的当前值。
- 使用 `set_param(gcb,'RiseTime',value)` 将 **Rise time (s)** 设置为特定值。

**数据类型：** `double`

### **Voltage (V)** — 发送器模拟模型输入的峰峰值电压 `1`（默认）| 正实数标量

发送器模拟模型输入的峰峰值电压，指定为正实数标量，单位为伏特。

#### 程序化使用

- 使用 `get_param(gcb,'VoltageSwingIdeal')` 查看 **Voltage (V)** 的当前值。
- 使用 `set_param(gcb,'VoltageSwingIdeal',value)` 将 **Voltage (V)** 设置为特定值。

**数据类型：** `double`

### 串扰

### **Include crosstalk** — 在仿真中包含串扰 off（默认）| on

选择以在仿真中包含串扰。默认情况下，此选项未选中。

#### 幅度

### **Specification** — 指定近端和远端干扰源的幅度 `100GBASE-CR4`（默认）| `CEI-25G-LR` | `CEI-28G-SR` | `CEI-28G-VSR` | `Custom`

指定近端和远端干扰源的幅度。您可以选择包含 `100GBASE-CR4`、`CEI-25G-LR`、`CEI-28G-SR`、`CEI-28G-VSR` 等规范的最大允许串扰，也可以指定自己的自定义串扰积分串扰噪声（ICN）水平。

#### 程序化使用

- 使用 `get_param(gcb,'CrosstalkSpecification')` 查看 **Specification** 的当前值。
- 使用 `set_param(gcb,'CrosstalkSpecification',value)` 将 **Specification** 设置为特定值。

### **Far end crosstalk ICN (V)** — 远端干扰源的期望积分噪声水平 `15e-3`（默认）| 非负实数标量

远端干扰源的期望积分串扰噪声（ICN）水平，指定为非负实数标量，单位为伏特。ICN 指定串扰的强度。

#### 依赖关系

此参数仅在您选择 `Custom` 作为串扰 **Specification** 时可用。

#### 程序化使用

- 使用 `get_param(gcb,'FEXTICN')` 查看 **Far end crosstalk ICN (V)** 的当前值。
- 使用 `set_param(gcb,'FEXTICN',value)` 将 **Far end crosstalk ICN (V)** 设置为特定值。

**数据类型：** `double`

### **Near end crosstalk ICN (V)** — 近端干扰源期望的集成噪声水平 `10e-3`（默认）| 非负实数标量

近端干扰源期望的集成串扰噪声（ICN）水平，指定为非负实数标量，单位为伏特。ICN 指定串扰的强度。

#### 依赖关系

仅当选择 `Custom` 作为串扰 **Specification** 时，此参数才可用。

#### 程序化使用

- 使用 `get_param(gcb,'NEXTICN')` 查看 **Near end crosstalk ICN (V)** 的当前值。
- 使用 `set_param(gcb,'NEXTICN',value)` 将 **Near end crosstalk ICN (V)** 设置为特定值。

**数据类型：** `double`

#### FEXT 激励

### **Symbol Time (s)** — 远端串扰激励的符号时间 `100e-12`（默认）| 正实数标量

远端串扰（FEXT）激励的符号时间，指定为正实数标量，单位为秒。

#### 程序化使用

- 使用 `get_param(gcb,'UIFEXT')` 查看 FEXT 激励中 **Symbol Time (s)** 的当前值。
- 使用 `set_param(gcb,'UIFEXT',value)` 将 FEXT 激励中的 **Symbol Time (s)** 设置为特定值。

**数据类型：** `double`

### **Delay (s)** — 远端串扰激励的延迟偏移 `0`（默认）| 非负实数标量

远端串扰（FEXT）激励的延迟偏移，指定为正实数标量，单位为秒。

#### 程序化使用

- 使用 `get_param(gcb,'DelayFEXT')` 查看 FEXT 激励中 **Delay (s)** 的当前值。
- 使用 `set_param(gcb,'DelayFEXT',value)` 将 FEXT 激励中的 **Delay (s)** 设置为特定值。

**数据类型：** `double`

### **Modulation** — 远端串扰激励的调制电平 `NRZ`（默认）| `PAM3` | `PAM4` | `PAM5` | `PAM6` | `PAM7` | `PAM8` | `PAM9` | `PAM10` | `PAM11` | `PAM12` | `PAM13` | `PAM14` | `PAM15` | `PAM16`

远端串扰（FEXT）激励的调制电平，在 `NRZ`（2 电平）和 `PAM16`（16 电平）之间指定。

#### 程序化使用

- 使用 `get_param(gcb,'ModulationFEXT')` 查看 FEXT 激励中 **Modulation** 的当前值。
- 使用 `set_param(gcb,'ModulationFEXT',value)` 将 FEXT 激励中的 **Modulation** 设置为特定值。

### **PRBS Order** — 远端串扰激励的 PRBS 阶数 `7`（默认）| `9` | `11` | `13` | `15` | `20` | `23` | `31` | `47`

远端串扰（FEXT）激励的伪随机二进制序列（PRBS）阶数。

#### 程序化使用

- 使用 `get_param(gcb,'OrderFEXT')` 查看 FEXT 激励中 **PRBS Order** 的当前值。
- 使用 `set_param(gcb,'OrderFEXT',value)` 将 FEXT 激励中的 **PRBS Order** 设置为特定值。

**数据类型：** `double`

#### NEXT 激励

### **Symbol Time (s)** — 近端串扰激励的符号时间 `100e-12`（默认）| 正实数标量

近端串扰（NEXT）激励的符号时间，指定为正实数标量，单位为秒。

#### 程序化使用

- 使用 `get_param(gcb,'UINEXT')` 查看 NEXT 激励中 **Symbol Time (s)** 的当前值。
- 使用 `set_param(gcb,'UINEXT',value)` 将 NEXT 激励中的 **Symbol Time (s)** 设置为特定值。

**数据类型：** `double`

### **Delay (s)** — 近端串扰激励的延迟偏移 `0`（默认）| 非负实数标量

近端串扰（NEXT）激励的延迟偏移，指定为正实数标量，单位为秒。

#### 程序化使用

- 使用 `get_param(gcb,'DelayNEXT')` 查看 NEXT 激励中 **Delay (s)** 的当前值。
- 使用 `set_param(gcb,'DelaynEXT',value)` 将 NEXT 激励中的 **Delay (s)** 设置为特定值。

**数据类型：** `double`

### **Modulation** — 近端串扰激励的调制电平 `NRZ`（默认）| `PAM3` | `PAM4` | `PAM5` | `PAM6` | `PAM7` | `PAM8` | `PAM9` | `PAM10` | `PAM11` | `PAM12` | `PAM13` | `PAM14` | `PAM15` | `PAM16`

近端串扰（NEXT）激励的调制电平，在 `NRZ`（2 电平）和 `PAM16`（16 电平）之间指定。

#### 程序化使用

- 使用 `get_param(gcb,'ModulationNEXT')` 查看 NEXT 激励中 **Modulation** 的当前值。
- 使用 `set_param(gcb,'ModulationNEXT',value)` 将 NEXT 激励中的 **Modulation** 设置为特定值。

### **PRBS Order** — 近端串扰激励的 PRBS 阶数 `9`（默认）| `7` | `11` | `13` | `15` | `20` | `23` | `31` | `47`

近端串扰（NEXT）激励的伪随机二进制序列（PRBS）阶数。

#### 程序化使用

- 使用 `get_param(gcb,'OrderFEXT')` 查看 FEXT 激励中 **PRBS Order** 的当前值。
- 使用 `set_param(gcb,'OrderFEXT',value)` 将 FEXT 激励中的 **PRBS Order** 设置为特定值。

**数据类型：** `double`
## 所属库

SerDes Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

从通道损耗指标或冲激响应构建损耗模型

Analog Channel 模块使用通道损耗指标或来自 SerDes Toolbox™ 模型中其他来源的冲激响应来构建损耗模型。模拟模型输入仅在使用冲激响应时用于 IBIS 文件构建。有关详细信息，请参阅 SerDes System 中的 Analog Channel Loss。
