---
type: simulink-block
title: 'RMS Measurement'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'rmsmeasurement'
documentation_source_path: 'ref/rmsmeasurement.html'
language: zh-CN
chinese_source: worker-translation
---

# RMS Measurement

## 端口
```yaml
ports:
- name: u
  summary: 输入信号 标量
  direction: input
  data_types: single | double
- name: RMS
  summary: 均方根 标量或向量
  direction: output
  data_types: single | double
```

### 输入

### **u** — 输入信号 标量

周期性输入信号。

**数据类型：** `single` | `double`
### 输出

### **RMS** — 均方根 标量或向量

输入信号的估计均方根值。如果选择 **Specify harmonics**，则输出为一个向量，其中每个元素对应一个指定的谐波。否则，输出为一个表示总均方根的标量。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Base frequency (Hz)
  summary: 基频 60 Hz（默认）| 标量
  group: ''
- name: Specify harmonics
  summary: 均方根输出模式 off（默认）| on
  group: ''
- name: Harmonic numbers
  summary: 谐波指定 [0 1 2]（默认）| 向量
  group: ''
- name: Sample time
  summary: 模块采样时间 0（默认）| 正数
  group: ''
```

### **Base frequency (Hz)** — 基频 `60 Hz`（默认）| 标量

输入信号对应于第一次谐波的基频。

### **Specify harmonics** — 均方根输出模式 `off`（默认）| on

指定是输出输入信号的总均方根值，还是输出所指定的各次谐波。

### **Harmonic numbers** — 谐波指定 `[0 1 2]`（默认）| 向量

指定要输出均方根值的谐波。

#### 依赖关系

要启用此参数，请选择 **Specify harmonics** 参数。

### **Sample time** — 模块采样时间 `0`（默认）| 正数

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于连续操作，将此属性设置为 `0`。对于离散操作，将采样时间显式指定为正数。此模块不支持继承采样时间。

如果此模块位于掩码子系统或其他允许连续和离散操作的变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。
## 所属库

Simscape / Electrical / Control / Measurements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

计算信号的均方根（RMS）属性

RMS Measurement 模块测量输入信号的均方根（RMS）属性。您可以使用它来测量以下属性之一：

- 输入信号的总均方根值
- 您指定的输入信号各次谐波的均方根值。

将总均方根配置与适当的传感器配合使用，可在系统中执行均方根电压、电流或功率分析。

您可以使用谐波配置对具有非线性负载的系统执行总谐波失真分析，例如：

- 变换器
- 电机驱动器
- 逆变器

### 方程

总均方根值根据输入信号
*xRMS* 计算如下：

xRMS(t)=1T∫t−Ttx(t)2dt,

其中：

- *T* 是输入信号的周期，或者等价地为其基频
  *F* 的倒数。
- *x* 是输入信号。

由于计算是在一段时间内执行的，模块需要
*T* 秒才能对输入信号的阶跃变化作出响应。此条件同样适用于启动过程。

谐波 *k* 的谐波均方根分量 *xk,RMS* 计算如下：

xk,RMS(t)=G(2T)(∫t−Ttx(t)sin(2πktT)dt)2+(∫t−Ttx(t)cos(2πktT)dt)2,

其中 *G* 对于直流分量（*k = 0*）等于 `0.5`，对于交流分量（*k > 0*）等于 1/2。
