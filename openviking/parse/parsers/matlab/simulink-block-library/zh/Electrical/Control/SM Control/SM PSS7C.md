---
type: simulink-block
title: 'SM PSS7C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smpss7c'
documentation_source_path: 'ref/smpss7c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM PSS7C

## 端口
```yaml
ports:
- name: V_SI1
  summary: 转速、频率或功率标量
  direction: input
  data_types: single | double
- name: V_SI2
  summary: 电功率标量
  direction: input
  data_types: single | double
- name: V_ST
  summary: 稳定转速、频率或功率标量
  direction: output
  data_types: single | double
```

### 输入

### **V\_SI1** — 转速、频率或功率标量

标幺转速、终端母线电压频率、补偿频率或电功率，指定为标量。

**数据类型：** `single` | `double`

### **V\_SI2** — 电功率标量

标幺电功率，指定为标量。

**数据类型：** `single` | `double`
### 输出

### **V\_ST** — 稳定转速、频率或功率标量

自动电压调节器输入稳定信号，受
*VST\_min* 和
*VST\_max* 限制，以标量形式返回。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Power system stabilizer main gain, K_S1 (pu)
  summary: 电力系统稳定器前向通道增益 50（默认）| 标量
  group: ''
- name: Power system stabilizer gain, K_S2 (pu)
  summary: 电力系统稳定器换能器增益 0.7052（默认）| 标量
  group: ''
- name: Power system stabilizer gain, K_S3 (pu)
  summary: 电力系统稳定器增益 1（默认）| 标量
  group: ''
- name: PSS transducer time constant, T_6 (s)
  summary: 换能器时间常数 6 0（默认）| 标量
  group: ''
- name: PSS transducer time constant, T_7 (s)
  summary: 换能器时间常数 7 10（默认）| 标量
  group: ''
- name: PSS washout time constant, T_w1 (s)
  summary: 洗出时间常数 1 10（默认）| 标量
  group: ''
- name: PSS washout time constant, T_w2 (s)
  summary: 洗出时间常数 2 10（默认）| 标量
  group: ''
- name: PSS washout time constant, T_w3 (s)
  summary: 洗出时间常数 3 10（默认）| 标量
  group: ''
- name: PSS washout time constant, T_w4 (s)
  summary: 洗出时间常数 4 0（默认）| 标量
  group: ''
- name: PSS transducer time constant, T_8 (s)
  summary: 换能器时间常数 8 0.5（默认）| 标量
  group: ''
- name: PSS washout time constant, T_9 (s)
  summary: 洗出时间常数 9 0.1（默认）| 标量
  group: ''
- name: Denominator exponent for ramp-track filter, M
  summary: 斜坡跟踪滤波器分母的指数 5（默认）| 标量
  group: ''
- name: Overall exponent for ramp-track filter, N
  summary: 斜坡跟踪滤波器的整体指数 1（默认）| 标量
  group: ''
- name: PSS canonical gain 0, K_0 (pu)
  summary: 电力系统稳定器规范增益 0 0.399（默认）| 标量
  group: ''
- name: PSS canonical gain 1, K_1 (pu)
  summary: 电力系统稳定器规范增益 1 1.8462（默认）| 标量
  group: ''
- name: PSS canonical gain 2, K_2 (pu)
  summary: 电力系统稳定器规范增益 2 0.4231（默认）| 标量
  group: ''
- name: PSS canonical gain 3, K_3 (pu)
  summary: 电力系统稳定器规范增益 3 0.2104（默认）| 标量
  group: ''
- name: PSS canonical gain 4, K_4 (pu)
  summary: 电力系统稳定器规范增益 4 0（默认）| 标量
  group: ''
- name: PSS third block gain, K_i3 (pu)
  summary: 电力系统稳定器第三模块增益 1（默认）| 标量
  group: ''
- name: PSS fourth block gain, K_i4 (pu)
  summary: 电力系统稳定器第四模块增益 0（默认）| 标量
  group: ''
- name: PSS time constant (first block), T_i1 (s)
  summary: 电力系统稳定器第一模块时间常数 0.03（默认）| 标量
  group: ''
- name: PSS time constant (second block), T_i2 (s)
  summary: 电力系统稳定器第二模块时间常数 0.0293（默认）| 标量
  group: ''
- name: PSS time constant (third block), T_i3 (s)
  summary: 电力系统稳定器第三模块时间常数 0.2804（默认）| 标量
  group: ''
- name: PSS time constant (fourth block), T_i4 (s)
  summary: 电力系统稳定器第四模块时间常数 1（默认）| 标量
  group: ''
- name: Maximum PSS output, V_STmax (pu)
  summary: 最大稳定 0.05（默认）| 标量
  group: ''
- name: Minimum PSS output, V_STmin (pu)
  summary: 最小稳定 -0.05（默认）| 标量
  group: ''
- name: 'Input signal #1 maximum limit, V_S1max (pu)'
  summary: 第一个输入的最大限值 2（默认）| 标量
  group: ''
- name: 'Input signal #1 minimum limit, V_S1min (pu)'
  summary: 第一个输入的最小限值 -2（默认）| 标量
  group: ''
- name: 'Input signal #2 maximum limit, V_S2max (pu)'
  summary: 第二个输入的最大限值 2（默认）| 标量
  group: ''
- name: 'Input signal #2 minimum limit, V_S2min (pu)'
  summary: 第二个输入的最小限值 -2（默认）| 标量
  group: ''
- name: Generator MW threshold for PSS activation, P_PSSon (pu)
  summary: 电力系统稳定器激活的发电机阈值 0（默认）| 标量
  group: ''
- name: Generator MW threshold for PSS de-activation, P_PSSoff (pu)
  summary: 电力系统稳定器去激活的发电机阈值 0（默认）| 标量
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认）| 0 | 正标量
  group: ''
```

### **Power system stabilizer main gain, K\_S1 (pu)** — 电力系统稳定器前向通道增益 50（默认）| 标量

电力系统稳定器前向通道增益。

### **Power system stabilizer gain, K\_S2 (pu)** — 电力系统稳定器换能器增益 0.7052（默认）| 标量

电力系统稳定器换能器增益。

### **Power system stabilizer gain, K\_S3 (pu)** — 电力系统稳定器增益 1（默认）| 标量

电力系统稳定器增益。

### **PSS transducer time constant, T\_6 (s)** — 换能器时间常数 6 `0`（默认）| 标量

换能器时间常数 6，与图中标记为 Low-Pass Filter 的模块相关联。

### **PSS transducer time constant, T\_7 (s)** — 换能器时间常数 7 `10`（默认）| 标量

换能器时间常数 7，与图中标记为 Low-Pass Filter1 的模块相关联。

### **PSS washout time constant, T\_w1 (s)** — 洗出时间常数 1 `10`（默认）| 标量

洗出时间常数 1，与图中标记为 Washout1 的模块相关联。

### **PSS washout time constant, T\_w2 (s)** — 洗出时间常数 2 `10`（默认）| 标量

洗出时间常数 2，与图中标记为 Washout2 的模块相关联。

### **PSS washout time constant, T\_w3 (s)** — 洗出时间常数 3 `10`（默认）| 标量

洗出时间常数 3，与图中标记为 Washout3 的模块相关联。

### **PSS washout time constant, T\_w4 (s)** — 洗出时间常数 4 `0`（默认）| 标量

洗出时间常数 4，与图中标记为 Washout4 的模块相关联。

### **PSS transducer time constant, T\_8 (s)** — 换能器时间常数 8 `0.5`（默认）| 标量

换能器时间常数 8。

### **PSS washout time constant, T\_9 (s)** — 洗出时间常数 9 `0.1`（默认）| 标量

洗出时间常数 9。

### **Denominator exponent for ramp-track filter, M** — 斜坡跟踪滤波器分母的指数 `5`（默认）| 标量

斜坡跟踪滤波器的分母指数。

### **Overall exponent for ramp-track filter, N** — 斜坡跟踪滤波器的整体指数 `1`（默认）| 标量

斜坡跟踪滤波器的整体指数。

### **PSS canonical gain 0, K\_0 (pu)** — 电力系统稳定器规范增益 0 0.399（默认）| 标量

Multi-band 子系统的电力系统稳定器规范增益 0。

### **PSS canonical gain 1, K\_1 (pu)** — 电力系统稳定器规范增益 1 1.8462（默认）| 标量

Multi-band 子系统的电力系统稳定器规范增益 1。

### **PSS canonical gain 2, K\_2 (pu)** — 电力系统稳定器规范增益 2 0.4231（默认）| 标量

Multi-band 子系统的电力系统稳定器规范增益 2。

### **PSS canonical gain 3, K\_3 (pu)** — 电力系统稳定器规范增益 3 0.2104（默认）| 标量

Multi-band 子系统的电力系统稳定器规范增益 3。

### **PSS canonical gain 4, K\_4 (pu)** — 电力系统稳定器规范增益 4 0（默认）| 标量

Multi-band 子系统的电力系统稳定器规范增益 4。

### **PSS third block gain, K\_i3 (pu)** — 电力系统稳定器第三模块增益 1（默认）| 标量

Multi-band 子系统的电力系统稳定器第三模块增益。

### **PSS fourth block gain, K\_i4 (pu)** — 电力系统稳定器第四模块增益 0（默认）| 标量

Multi-band 子系统的电力系统稳定器第四模块增益。

### **PSS time constant (first block), T\_i1 (s)** — 电力系统稳定器第一模块时间常数 0.03（默认）| 标量

Multi-band 子系统内部第一模块的电力系统稳定器时间常数。

### **PSS time constant (second block), T\_i2 (s)** — 电力系统稳定器第二模块时间常数 0.0293（默认）| 标量

Multi-band 子系统内部第二模块的电力系统稳定器时间常数。

### **PSS time constant (third block), T\_i3 (s)** — 电力系统稳定器第三模块时间常数 0.2804（默认）| 标量

Multi-band 子系统内部第三模块的电力系统稳定器时间常数。

### **PSS time constant (fourth block), T\_i4 (s)** — 电力系统稳定器第四模块时间常数 1（默认）| 标量

Multi-band 子系统内部第四模块的电力系统稳定器时间常数。

### **Maximum PSS output, V\_STmax (pu)** — 最大稳定 `0.05`（默认）| 标量

电力系统稳定器输出到自动电压调节器（AVR）的最大值。

### **Minimum PSS output, V\_STmin (pu)** — 最小稳定 `-0.05`（默认）| 标量

电力系统稳定器输出到自动电压调节器（AVR）的最小值。

### **Input signal #1 maximum limit, V\_S1max (pu)** — 第一个输入的最大限值 `2`（默认）| 标量

第一个稳定器输入的最大信号值。

### **Input signal #1 minimum limit, V\_S1min (pu)** — 第一个输入的最小限值 `-2`（默认）| 标量

第一个稳定器输入的最小信号值。

### **Input signal #2 maximum limit, V\_S2max (pu)** — 第二个输入的最大限值 `2`（默认）| 标量

第二个稳定器输入的最大信号值。

### **Input signal #2 minimum limit, V\_S2min (pu)** — 第二个输入的最小限值 `-2`（默认）| 标量

第二个稳定器输入的最小信号值。

### **Generator MW threshold for PSS activation, P\_PSSon (pu)** — 电力系统稳定器激活的发电机阈值 `0`（默认）| 标量

电力系统稳定器激活的发电机阈值。

### **Generator MW threshold for PSS de-activation, P\_PSSoff (pu)** — 电力系统稳定器去激活的发电机阈值 `0`（默认）| 标量

电力系统稳定器去激活的发电机阈值。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 0 | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将采样时间设置为 `-1`。
对于离散时间操作，将采样时间设置为正标量。对于
连续时间操作，将采样时间设置为 `0`。
## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

离散时间或连续时间单输入 PSS7C 电力系统稳定器

SM PSS7C 模块实现了一个双输入 PSS7C 电力系统稳定器
（PSS），用于维持同步电机（SM）的转子角稳定性，符合 IEEE 421.5-2016[1]。
通常，您使用 PSS 通过励磁控制来增强电力系统振荡的阻尼。

您可以使用同一模型表示两种不同类型的双输入电力系统稳定器：

- 一种稳定器，使用电功率和转速（或频率）信号
  来计算加速功率的积分。这使得
  计算出的稳定器信号对机械变化不敏感。
- 一种稳定器，使用电功率与转速
  或频率的组合。为了实现所需的稳定信号整形，系统
  直接使用转速，无需相位超前补偿，并添加一个与电功率
  成比例的信号。

您可以通过使用
**Sample time (-1 for inherited)** 参数在模块的连续和离散实现之间切换。要将
积分器配置为连续时间，请将 **Sample time (-1 for
inherited)** 属性设置为 `0`。要将积分器
配置为离散时间，请将 **Sample time (-1 for inherited)** 属性
设置为正的非零值，或设置为 `-1` 以从上
游模块继承采样时间。

此图说明了 PSS7C 电力系统
稳定器的整体结构：

在图中：

- *V\_SI1* 和 *V\_SI2* 是两个电力
  系统稳定器输入。常用的输入是转速、频率或
  功率。
- 每个稳定器输入表示了两个 Washout（离散或连续）模块，
  时间常数为
  *TW1* 至
  *TW4*，以及一个
  换能器，由 Low-Pass Filter（离散或连续）表示，
  时间常数为 *T6* 和
  *T7*。
- 为了实现斜坡跟踪滤波器特性，Ramp Tracking Filter
  子系统对串联的超前-滞后和低通滤波器模块网络进行建模。
- 为了提供相位补偿，Multi-band 子系统实现了一个
  规范状态方程，时间常数为
  *Ti1* 至
  *Ti4*，增益为
  *K0* 至
  *K4*。
- PSS 输出逻辑子系统允许表示与发电机有功功率输出相关联的 PSS 输出
  逻辑。
  *PPSSon* 和
  *PPSSoff* 是用于定义滞环的阈值
  值。
