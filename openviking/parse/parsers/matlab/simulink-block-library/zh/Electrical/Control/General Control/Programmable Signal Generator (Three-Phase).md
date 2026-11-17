---
type: simulink-block
title: 'Programmable Signal Generator (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / General Control'
documentation_page: 'programmablesignalgeneratorthreephase'
documentation_source_path: 'ref/programmablesignalgeneratorthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Programmable Signal Generator (Three-Phase)

## 端口

### 输出

### **abc** — 三相正弦信号向量

三相正弦信号，以向量形式返回。

**数据类型：** `single` | `double`

### **m** — 信号测量值向量

正弦信号三相正弦波的幅值、频率、相位和角度，以向量形式返回。

**数据类型：** `single` | `double`

## 参数

### **Sample time** — 模块采样时间 `1e-5`（默认）| 0 | 正标量

连续模块执行之间的时间。
在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于离散时间操作，请指定正整数。对于连续时间操作，请指定 `0`。

### 幅值

### **Variation configuration** — 幅值变化类型 `Constant`（默认）| `Ramp` | `Step` | `Modulation` | `Table`

要应用于信号幅值的变化类型。

### **Magnitude (value)** — 生成的三相正弦波幅值 `100`（默认）| 标量

生成的正序三相正弦波的幅值。

#### 依赖关系

要启用此参数，请将 **Variation configuration** 设置为
`Constant`、
`Ramp`、
`Step` 或
`Modulation`。

### **Rate of change (value/s)** — 幅值变化率 `100`（默认）| 标量

幅值的变化率。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Ramp`。

### **Step value (value)** — 幅值阶跃值 `100`（默认）| 标量

信号幅值的阶跃变化幅度。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Step`。

### **Modulation magnitude** — 调制幅值 `50`（默认）| 标量

信号幅值的调制幅度。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Modulation`。

### **Modulation frequency** — 调制频率 `10`（默认）| 标量

信号幅值的调制频率。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Modulation`。

### **Start time** — 幅值变化开始时间 `0.1`（默认）| 标量

幅值上编程变化开始的时间。

#### 依赖关系

要启用此参数，请将 **Variation configuration** 设置为
`Constant`、
`Ramp`、
`Step` 或
`Modulation`。

### **Stop time** — 幅值变化停止时间 `0.6`（默认）| 标量

幅值上编程变化停止的时间。

#### 依赖关系

要启用此参数，请将 **Variation configuration** 设置为
`Constant`、
`Ramp`、
`Step` 或
`Modulation`。

### **Table data** — 幅值表值 `[0 30 60 90]`（默认）| 向量

与 **Time values** 参数中指定的时间值对应的信号幅值。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Table`。

### **Time values** — 幅值时间值 `[0 0.3 0.6 0.9]`（默认）| 向量

信号幅值变为 **Table data** 参数中指定的值的时间值。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Table`。

### 频率

### **Variation configuration** — 频率变化类型 `Constant`（默认）| `Ramp` | `Step` | `Modulation` | `Table`

要应用于信号频率的变化类型。

### **Frequency (Hz)** — 生成的三相正弦波频率 `100`（默认）| 标量

生成的正序三相正弦波的频率。

#### 依赖关系

要启用此参数，请将 **Variation configuration** 设置为
`Constant`、
`Ramp`、
`Step` 或
`Modulation`。

### **Rate of change (Hz/s)** — 频率变化率 `100`（默认）| 标量

频率的变化率。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Ramp`。

### **Step value (Hz)** — 频率阶跃值 `100`（默认）| 标量

信号频率的阶跃变化幅度。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Step`。

### **Modulation magnitude** — 频率调制幅值 `50`（默认）| 标量

信号频率的调制幅度。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Modulation`。

### **Modulation frequency** — 频率调制频率 `10`（默认）| 标量

信号频率的调制频率。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Modulation`。

### **Start time** — 频率变化开始时间 `0.1`（默认）| 标量

频率上编程变化开始的时间。

#### 依赖关系

要启用此参数，请将 **Variation configuration** 设置为
`Constant`、
`Ramp`、
`Step` 或
`Modulation`。

### **Stop time** — 频率变化停止时间 `0.6`（默认）| 标量

频率上编程变化停止的时间。

#### 依赖关系

要启用此参数，请将 **Variation configuration** 设置为
`Constant`、
`Ramp`、
`Step` 或
`Modulation`。

### **Table data** — 频率表值 `[0 30 60 90]`（默认）| 向量

与 **Time values** 参数中指定的时间值对应的信号频率。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Table`。

### **Time values** — 频率时间值 `[0 0.3 0.6 0.9]`（默认）| 向量

信号频率变为 **Table data** 参数中指定的值的时间值。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Table`。

### 相位

### **Variation configuration** — 相位变化类型 `Constant`（默认）| `Ramp` | `Step` | `Modulation` | `Table`

要应用于相位幅值的变化类型。

### **Phase shift (deg)** — 生成的三相正弦波相移 `100`（默认）| 标量

生成的正序三相正弦波的相移。

#### 依赖关系

要启用此参数，请将 **Variation configuration** 设置为
`Constant`、
`Ramp`、
`Step` 或
`Modulation`。

### **Rate of change (deg/s)** — 相位变化率 `100`（默认）| 标量

相位的变化率。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Ramp`。

### **Step value (deg)** — 相位阶跃值 `100`（默认）| 标量

信号相位的阶跃变化幅度。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Step`。

### **Modulation magnitude** — 相位调制幅值 `50`（默认）| 标量

信号相位的调制幅度。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Modulation`。

### **Modulation frequency** — 相位调制频率 `10`（默认）| 标量

信号相位的调制频率。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Modulation`。

### **Start time** — 相位变化开始时间 `0.1`（默认）| 标量

相位上编程变化开始的时间。

#### 依赖关系

要启用此参数，请将 **Variation configuration** 设置为
`Constant`、
`Ramp`、
`Step` 或
`Modulation`。

### **Stop time** — 相位变化停止时间 `0.6`（默认）| 标量

相位上编程变化停止的时间。

#### 依赖关系

要启用此参数，请将 **Variation configuration** 设置为
`Constant`、
`Ramp`、
`Step` 或
`Modulation`。

### **Table data** — 相位表值 `[0 30 60 90]`（默认）| 向量

与 **Time values** 参数中指定的时间值对应的信号相位。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Table`。

### **Time values** — 相位时间值 `[0 0.3 0.6 0.9]`（默认）| 向量

信号频率变为 **Table data** 参数中指定的值的时间值。

#### 依赖关系

要启用此参数，请将 **Variation
configuration** 设置为
`Table`。

### 谐波

### **Enable harmonic A** — 谐波 A 叠加 `off`（默认）| `on`

谐波 A 是否叠加在生成信号的基频上。

### **Harmonic sequence** — 谐波 A 序列类型 `Zero Sequence`（默认）| `Positive Sequence` | `Negative Sequence`

谐波 A 的序列类型。

#### 依赖关系

要启用此参数，请选中 **Enable harmonic
A** 复选框。

### **Harmonic order** — 谐波 A 次数 `3`（默认）| 标量

叠加在信号基频上的谐波 A 的次数。

#### 依赖关系

要启用此参数，请选中 **Enable harmonic
A** 复选框。

### **Harmonic magnitude** — 谐波 A 幅值 `50`（默认）| 标量

叠加在信号基频上的谐波 A 的幅值。

#### 依赖关系

要启用此参数，请选中 **Enable harmonic
A** 复选框。

### **Harmonic phase shift** — 谐波 A 相移 `180`（默认）| 标量

叠加在信号基频上的谐波 A 的相移。

#### 依赖关系

要启用此参数，请选中 **Enable harmonic
A** 复选框。

### **Start time** — 谐波 A 叠加开始时间 `0.1`（默认）| 标量

谐波 A 叠加在信号基频上的时间。

#### 依赖关系

要启用此参数，请选中 **Enable harmonic
A** 复选框。

### **Stop time** — 谐波 A 叠加停止时间 `0.6`（默认）| 标量

谐波 A 停止叠加在信号基频上的时间。

#### 依赖关系

要启用此参数，请选中 **Enable harmonic
A** 复选框。

### **Enable harmonic B** — 谐波 B 叠加 `off`（默认）| `on`

谐波 B 是否叠加在生成信号的基频上。

### **Harmonic sequence** — 谐波 B 序列类型 `Zero Sequence`（默认）| `Positive Sequence` | `Negative Sequence`

谐波 B 的序列类型。

#### 依赖关系

要启用此参数，请选中 **Enable harmonic B** 复选框。

### **Harmonic order** — 谐波 B 次数 `3`（默认）| 标量

叠加在信号基频上的谐波 B 的次数。

#### 依赖关系

要启用此参数，请选中 **Enable harmonic
B** 复选框。

### **Harmonic magnitude** — 谐波 B 幅值 `50`（默认）| 标量

叠加在信号基频上的谐波 B 的幅值。

#### 依赖关系

要启用此参数，请选中 **Enable harmonic
B** 复选框。

### **Harmonic phase shift** — 谐波 B 相移 `180`（默认）| 标量

叠加在信号基频上的谐波 B 的相移。

#### 依赖关系

要启用此参数，请选中 **Enable harmonic
B** 复选框。

### **Start time** — 谐波 B 叠加开始时间 `0.1`（默认）| 标量

谐波 B 叠加在信号基频上的时间。

#### 依赖关系

要启用此参数，请选中 **Enable harmonic
B** 复选框。

### **Stop time** — 谐波 B 叠加停止时间 `0.6`（默认）| 标量

谐波 B 停止叠加在信号基频上的时间。

#### 依赖关系

要启用此参数，请选中 **Enable harmonic
B** 复选框。

## 所属库

Simscape / Electrical / Control / General Control

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

具有可编程幅值、相位、频率和叠加谐波的离散时间或连续时间三相正弦信号发生器

Programmable Signal Generator (Three-Phase)
生成具有可编程幅值、相位和频率随时间变化的三相正弦信号。您可以指定一个或两个可叠加在信号基频上的谐波。

您可以通过使用 **Sample time** 参数在模块的连续实现和离散实现之间切换。要将模块配置为连续时间，请将 **Sample time** 设置为 `0`。要将模块配置为离散时间，请将 **Sample time** 设置为正的非零值。
