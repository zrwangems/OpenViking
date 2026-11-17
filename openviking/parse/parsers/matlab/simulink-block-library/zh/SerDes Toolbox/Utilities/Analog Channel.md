---
type: simulink-block
title: 'Analog Channel'
family: 'utilities'
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

### 输入

### **WaveIn** — 输入信号标量 | 向量

输入信号，指定为波形。

**数据类型：** `double`
### 输出

### **WaveOut** — 修改后的输出数据标量 | 向量

修改后的输出数据，其中包含有损印刷电路板传输线模型的影响，采用 [1] 中概述的方法。

**数据类型：** `double`

## 参数

### 通道模型

### **通道模型** — 通道模型的来源 `Loss model` (默认) | `Impulse response`

通道模型的来源。

- 选择 `Loss model` 以根据损耗模型对模拟通道建模。
- 选择 `Impulse response` 以根据冲激响应对模拟通道建模。

#### 编程用法

- 使用 `get_param(gcb,'ChannelType')` 查看当前 **通道模型**。
- 使用 `set_param(gcb,'ChannelType',value)` 设置特定的 **通道模型**。

### **目标频率 (Hz)** — 所需通道损耗的频率 `20e9` (默认) | 正实数标量

所需通道损耗的频率，指定为以 hertz 为单位的正实数标量。它对应于系统的 Nyquist 频率。

#### 依赖关系

仅当选择 `Loss model` 作为 **通道模型** 时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'TargetFrequency')` 查看 **目标频率 (Hz)** 的当前值。
- 使用 `set_param(gcb,'TargetFrequency',value)` 将 **目标频率 (Hz)** 设置为特定值。

**数据类型：** `double`

### **损耗 (dB)** — 目标频率处的通道损耗 `8` (默认) | 标量

目标频率处的通道损耗，指定为以 dB 为单位的标量。

#### 依赖关系

仅当选择 `Loss model` 作为 **通道模型** 时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'Loss')` 查看 **损耗 (dB)** 的当前值。
- 使用 `set_param(gcb,'Loss',value)` 将 **损耗 (dB)** 设置为特定值。

**数据类型：** `double`

### **阻抗 (Ohms)** — 通道特性阻抗 正实数标量

通道的特性阻抗，指定为以 ohms 为单位的正实数标量。**阻抗 (Ohms)** 取决于 SerDes Designer 应用中的 **Configuration** 选项卡或 Configuration 模块中的 **Signaling** 设置。

- 如果 **Signaling** 设置为 `Differential`，则 **阻抗 (Ohms)** 的默认值为 `100`。
- 如果 **Signaling** 设置为 `Single-ended`，则 **阻抗 (Ohms)** 的默认值为 `50`。

#### 依赖关系

仅当选择 `Loss model` 作为 **通道模型** 时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'Zc')` 查看 **阻抗** 的当前值。
- 使用 `set_param(gcb,'Zc',value)` 将 **阻抗** 设置为特定值。

**数据类型：** `double`

### **冲激响应** — 用户提供的冲激响应 `[zeros(1,63),1/SampleInterval,zeros(1,192)]` (默认) | 矩阵

用户提供的冲激响应，指定为无量纲矩阵。**冲激响应** 用于根据系统用户定义的冲激响应构建通道损耗模型。

您可以使用用户指定的冲激响应定义自己的串扰。如果决定包含来自自定义冲激响应的串扰，可以将最多六个串扰激励指定为冲激响应中的新列。

#### 依赖关系

仅当选择 `Impulse response` 作为 **通道模型** 时，此参数才可用

#### 编程用法

- 使用 `get_param(gcb,'ImpulseResponse')` 查看 **冲激响应** 的当前值。
- 使用 `set_param(gcb,'ImpulseResponse',value)` 将 **冲激响应** 设置为特定值。

**数据类型：** `double`

### **冲激采样间隔** — 用户提供的冲激响应的采样间隔 `6.25e-12` (默认) | 正实数标量

用户提供的冲激响应的采样间隔，指定为以 seconds 为单位的正实数标量。

**数据类型：** `double`

#### 模拟模型

### **Tx R (Ohms)** — 发射器模拟模型的单端阻抗 `50` (默认) | 非负实数标量

发射器模拟模型的单端阻抗，指定为以 ohms 为单位的非负实数标量。

#### 编程用法

- 使用 `get_param(gcb,'TxR')` 查看 **Tx R (Ohms)** 的当前值。
- 使用 `set_param(gcb,'TxR',value)` 将 **Tx R (Ohms)** 设置为特定值。

**数据类型：** `double`

### **Tx C (F)** — 发射器模拟模型的电容 `100e-15` (默认) | 非负实数标量

发射器模拟模型的电容，指定为以 farads 为单位的非负实数标量。

#### 编程用法

- 使用 `get_param(gcb,'TxC')` 查看 **Tx C (F)** 的当前值。
- 使用 `set_param(gcb,'TxC',value)` 将 **Tx C (F)** 设置为特定值。

**数据类型：** `double`

### **Rx R (Ohms)** — 接收器模拟模型的单端阻抗 `50` (默认) | 非负实数标量

接收器模拟模型的单端阻抗，指定为以 ohms 为单位的非负实数标量。

#### 编程用法

- 使用 `get_param(gcb,'RxR')` 查看 **Rx R (Ohms)** 的当前值。
- 使用 `set_param(gcb,'RxR',value)` 将 **Rx R (Ohms)** 设置为特定值。

**数据类型：** `double`

### **Rx C (F)** — 接收器模拟模型的电容 `200e-15` (默认) | 非负实数标量

接收器模拟模型的电容，指定为以 farads 为单位的非负实数标量。

#### 编程用法

- 使用 `get_param(gcb,'RxC')` 查看 **Rx C (F)** 的当前值。
- 使用 `set_param(gcb,'RxC',value)` 将 **Rx C (F)** 设置为特定值。

**数据类型：** `double`

### **上升时间 (s)** — 激励输入的 20%−80% 上升时间 `10e-12` (默认) | 正实数标量

发射器模拟模型的激励输入的 20%−80% 上升时间，指定为以 seconds 为单位的正实数标量。

#### 编程用法

- 使用 `get_param(gcb,'RiseTime')` 查看 **上升时间 (s)** 的当前值。
- 使用 `set_param(gcb,'RiseTime',value)` 将 **上升时间 (s)** 设置为特定值。

**数据类型：** `double`

### **电压 (V)** — 发射器模拟模型输入的峰峰值电压 `1` (默认) | 正实数标量

发射器模拟模型输入的峰峰值电压，指定为以 volts 为单位的正实数标量。

#### 编程用法

- 使用 `get_param(gcb,'VoltageSwingIdeal')` 查看 **电压 (V)** 的当前值。
- 使用 `set_param(gcb,'VoltageSwingIdeal',value)` 将 **电压 (V)** 设置为特定值。

**数据类型：** `double`

### 串扰

### **包含串扰** — 在仿真中包含串扰 off (默认) | on

选择以在仿真中包含串扰。默认情况下，此选项未选中。

#### 幅度

### **规范** — 指定近端和远端干扰源的幅度 `100GBASE-CR4` (默认) | `CEI-25G-LR` | `CEI-28G-SR` | `CEI-28G-VSR` | `Custom`

指定近端和远端干扰源的幅度。您可以选择为 `100GBASE-CR4`、`CEI-25G-LR`、`CEI-28G-SR`、`CEI-28G-VSR` 等规范包含允许的最大串扰，也可以指定自己的自定义串扰集成串扰噪声 (ICN) 电平。

#### 编程用法

- 使用 `get_param(gcb,'CrosstalkSpecification')` 查看 **规范** 的当前值。
- 使用 `set_param(gcb,'CrosstalkSpecification',value)` 将 **规范** 设置为特定值。

### **远端串扰 ICN (V)** — 远端干扰源所需的集成噪声电平 `15e-3` (默认) | 非负实数标量

远端干扰源所需的集成串扰噪声 (ICN) 电平，指定为以 volts 为单位的非负实数标量。ICN 指定串扰的强度。

#### 依赖关系

仅当您选择 `Custom` 作为串扰 **规范** 时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'FEXTICN')` 查看 **远端串扰 ICN (V)** 的当前值。
- 使用 `set_param(gcb,'FEXTICN',value)` 将 **远端串扰 ICN (V)** 设置为特定值。

**数据类型：** `double`

### **近端串扰 ICN (V)** — 近端干扰源所需的集成噪声电平 `10e-3` (默认) | 非负实数标量

近端干扰源所需的集成串扰噪声 (ICN) 电平，指定为以 volts 为单位的非负实数标量。ICN 指定串扰的强度。

#### 依赖关系

仅当您选择 `Custom` 作为串扰 **规范** 时，此参数才可用。

#### 编程用法

- 使用 `get_param(gcb,'NEXTICN')` 查看 **近端串扰 ICN (V)** 的当前值。
- 使用 `set_param(gcb,'NEXTICN',value)` 将 **近端串扰 ICN (V)** 设置为特定值。

**数据类型：** `double`

#### FEXT 激励

### **符号时间 (s)** — 远端串扰激励的符号时间 `100e-12` (默认) | 正实数标量

远端串扰 (FEXT) 激励的符号时间，指定为以 seconds 为单位的正实数标量。

#### 编程用法

- 使用 `get_param(gcb,'UIFEXT')` 查看 FEXT 激励中 **符号时间 (s)** 的当前值。
- 使用 `set_param(gcb,'UIFEXT',value)` 将 FEXT 激励中的 **符号时间 (s)** 设置为特定值。

**数据类型：** `double`

### **延迟 (s)** — 远端串扰激励的延迟偏移 `0` (默认) | 非负实数标量

远端串扰 (FEXT) 激励的延迟偏移，指定为以 seconds 为单位的正实数标量。

#### 编程用法

- 使用 `get_param(gcb,'DelayFEXT')` 查看 FEXT 激励中 **延迟 (s)** 的当前值。
- 使用 `set_param(gcb,'DelayFEXT',value)` 将 FEXT 激励中的 **延迟 (s)** 设置为特定值。

**数据类型：** `double`

### **调制** — 远端串扰激励的调制电平 `NRZ` (默认) | `PAM3` | `PAM4` | `PAM5` | `PAM6` | `PAM7` | `PAM8` | `PAM9` | `PAM10` | `PAM11` | `PAM12` | `PAM13` | `PAM14` | `PAM15` | `PAM16`

远端串扰 (FEXT) 激励的调制电平，指定为介于 `NRZ`（2 电平）和 `PAM16`（16 电平）之间。

#### 编程用法

- 使用 `get_param(gcb,'ModulationFEXT')` 查看 FEXT 激励中 **调制** 的当前值。
- 使用 `set_param(gcb,'ModulationFEXT',value)` 将 FEXT 激励中的 **调制** 设置为特定值。

### **PRBS 阶数** — 远端串扰激励的 PRBS 阶数 `7` (默认) | `9` | `11` | `13` | `15` | `20` | `23` | `31` | `47`

远端串扰 (FEXT) 激励的伪随机二进制序列 (PRBS) 阶数。

#### 编程用法

- 使用 `get_param(gcb,'OrderFEXT')` 查看 FEXT 激励中 **PRBS 阶数** 的当前值。
- 使用 `set_param(gcb,'OrderFEXT',value)` 将 FEXT 激励中的 **PRBS 阶数** 设置为特定值。

**数据类型：** `double`

#### NEXT 激励

### **符号时间 (s)** — 近端串扰激励的符号时间 `100e-12` (默认) | 正实数标量

近端串扰 (NEXT) 激励的符号时间，指定为以 seconds 为单位的正实数标量。

#### 编程用法

- 使用 `get_param(gcb,'UINEXT')` 查看 NEXT 激励中 **符号时间 (s)** 的当前值。
- 使用 `set_param(gcb,'UINEXT',value)` 将 NEXT 激励中的 **符号时间 (s)** 设置为特定值。

**数据类型：** `double`

### **延迟 (s)** — 近端串扰激励的延迟偏移 `0` (默认) | 非负实数标量

近端串扰 (NEXT) 激励的延迟偏移，指定为以 seconds 为单位的正实数标量。

#### 编程用法

- 使用 `get_param(gcb,'DelayNEXT')` 查看 NEXT 激励中 **延迟 (s)** 的当前值。
- 使用 `set_param(gcb,'DelaynEXT',value)` 将 NEXT 激励中的 **延迟 (s)** 设置为特定值。

**数据类型：** `double`

### **调制** — 近端串扰激励的调制电平 `NRZ` (默认) | `PAM3` | `PAM4` | `PAM5` | `PAM6` | `PAM7` | `PAM8` | `PAM9` | `PAM10` | `PAM11` | `PAM12` | `PAM13` | `PAM14` | `PAM15` | `PAM16`

近端串扰 (NEXT) 激励的调制电平，指定为介于 `NRZ`（2 电平）和 `PAM16`（16 电平）之间。

#### 编程用法

- 使用 `get_param(gcb,'ModulationNEXT')` 查看 NEXT 激励中 **调制** 的当前值。
- 使用 `set_param(gcb,'ModulationNEXT',value)` 将 NEXT 激励中的 **调制** 设置为特定值。

### **PRBS 阶数** — 近端串扰激励的 PRBS 阶数 `9` (默认) | `7` | `11` | `13` | `15` | `20` | `23` | `31` | `47`

近端串扰 (NEXT) 激励的伪随机二进制序列 (PRBS) 阶数。

#### 编程用法

- 使用 `get_param(gcb,'OrderFEXT')` 查看 FEXT 激励中 **PRBS 阶数** 的当前值。
- 使用 `set_param(gcb,'OrderFEXT',value)` 将 FEXT 激励中的 **PRBS 阶数** 设置为特定值。

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

根据通道损耗指标或冲激响应构建损耗模型

Analog Channel 模块在 SerDes Toolbox™ 模型中使用来自另一来源的通道损耗指标或冲激响应构建损耗模型。模拟模型输入仅在使用冲激响应时用于 IBIS 文件构建。有关详细信息，请参阅 SerDes System 中的 Analog Channel Loss。
