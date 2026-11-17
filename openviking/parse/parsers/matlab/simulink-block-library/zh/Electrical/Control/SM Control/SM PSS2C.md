---
type: simulink-block
title: 'SM PSS2C'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smpss2c'
documentation_source_path: 'ref/smpss2c.html'
language: zh-CN
chinese_source: worker-translation
---

# SM PSS2C

## 端口

### 输入

### **V\_SI1** — 转速、频率或功率标量

标幺转速、端母线电压频率、补偿频率或电功率，指定为标量。

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

### **PSS gain, K\_S1 (pu)** — 电力系统稳定器前向通路增益 5（默认）| 标量

电力系统稳定器前向通路增益。

### **PSS gain, K\_S2 (pu)** — 电力系统稳定器换能器增益 1.4184（默认）| 标量

电力系统稳定器换能器增益。

### **PSS gain, K\_S3 (pu)** — 电力系统稳定器增益 1（默认）| 标量

电力系统稳定器增益。

### **PSS transducer time constant, T\_6 (s)** — 换能器时间常数 6 `0`（默认）| 标量

换能器时间常数 6。

### **PSS transducer time constant, T\_7 (s)** — 换能器时间常数 7 `10`（默认）| 标量

换能器时间常数 7。

### **PSS washout time constant, T\_w1 (s)** — 洗出时间常数 1 `10`（默认）| 标量

洗出时间常数 1。

### **PSS washout time constant, T\_w2 (s)** — 洗出时间常数 2 `10`（默认）| 标量

洗出时间常数 2。

### **PSS washout time constant, T\_w3 (s)** — 洗出时间常数 3 `10`（默认）| 标量

洗出时间常数 3。

### **PSS washout time constant, T\_w4 (s)** — 洗出时间常数 4 `0`（默认）| 标量

洗出时间常数 4。

### **PSS transducer time constant, T\_8 (s)** — 换能器时间常数 8 `0.5`（默认）| 标量

换能器时间常数 8。

### **PSS washout time constant, T\_9 (s)** — 洗出时间常数 9 `0.1`（默认）| 标量

洗出时间常数 9。

### **Denominator exponent for ramp-track filter, M** — 斜坡跟踪滤波器分母指数 `5`（默认）| 标量

斜坡跟踪滤波器的分母指数。

### **Overall exponent for ramp-track filter, N** — 斜坡跟踪滤波器总指数 `1`（默认）| 标量

斜坡跟踪滤波器的总指数。

### **PSS numerator (lead) compensating time constant (first block), T\_1 (s)** — 超前时间常数 1 `0.16`（默认）| 标量

超前时间常数 1，与图中标记为 Lead-Lag1 的模块相关联。

### **PSS denominator (lag) compensating time constant (first block), T\_2 (s)** — 滞后时间常数 2 `0.04`（默认）| 标量

滞后时间常数 2，与图中标记为 Lead-Lag1 的模块相关联。

### **PSS numerator (lead) compensating time constant (second block), T\_3 (s)** — 超前时间常数 3 `0.16`（默认）| 标量

超前时间常数 3，与图中标记为 Lead-Lag2 的模块相关联。

### **PSS denominator (lag) compensating time constant (second block), T\_4 (s)** — 滞后时间常数 4 `0.04`（默认）| 标量

滞后时间常数 4，与图中标记为 Lead-Lag2 的模块相关联。

### **PSS denominator (lead) compensating time constant (third block), T\_10 (s)** — 滞后时间常数 10 `0.18`（默认）| 标量

滞后时间常数 10，与图中标记为 Lead-Lag3 的模块相关联。

### **PSS denominator (lag) compensating time constant (third block), T\_11 (s)** — 滞后时间常数 11 `0.03`（默认）| 标量

滞后时间常数 11，与图中标记为 Lead-Lag3 的模块相关联。

### **PSS denominator (lead) compensating time constant (fourth block), T\_12 (s)** — 滞后时间常数 12 `0`（默认）| 标量

滞后时间常数 12，与图中标记为 Lead-Lag4 的模块相关联。

### **PSS denominator (lag) compensating time constant (fourth block), T\_13 (s)** — 滞后时间常数 13 `0`（默认）| 标量

滞后时间常数 13，与图中标记为 Lead-Lag4 的模块相关联。

### **Maximum PSS output, V\_STmax (pu)** — 最大稳定 `0.1`（默认）| 标量

电力系统稳定器输出至自动电压调节器的最大值。

### **Minimum PSS output, V\_STmin (pu)** — 最小稳定 `-0.1`（默认）| 标量

电力系统稳定器输出至自动电压调节器的最小值。

### **Input signal #1 maximum limit, V\_S1max (pu)** — 第一输入最大值限制 `2`（默认）| 标量

第一稳定器输入信号的最大值。

### **Input signal #1 minimum limit, V\_S1min (pu)** — 第一输入最小值限制 `-2`（默认）| 标量

第一稳定器输入信号的最小值。

### **Input signal #2 maximum limit, V\_S2max (pu)** — 第二输入最大值限制 `2`（默认）| 标量

第二稳定器输入信号的最大值。

### **Input signal #2 minimum limit, V\_S2min (pu)** — 第二输入最小值限制 `-2`（默认）| 标量

第二稳定器输入信号的最小值。

### **Generator MW threshold for PSS activation, P\_PSSon (pu)** — 电力系统稳定器激活的发电机阈值 `0`（默认）| 标量

电力系统稳定器激活的发电机阈值。

### **Generator MW threshold for PSS de-activation, P\_PSSoff (pu)** — 电力系统稳定器去激活的发电机阈值 `0`（默认）| 标量

电力系统稳定器去激活的发电机阈值。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 0 | 正标量

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当时更新其内部状态。
有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，将采样时间设置为 `-1`。
对于离散时间操作，将采样时间设置为正标量。对于连续时间操作，将采样时间设置为 `0`。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

离散时间或连续时间单输入 PSS2C 电力系统稳定器

SM PSS2C 模块实现双输入 PSS2C 电力系统稳定器（PSS），用于维持同步电机（SM）的转子角稳定性，符合 IEEE 421.5-2016[1]。
通常，您使用 PSS 通过励磁控制来增强电力系统振荡的阻尼。

您可以使用同一模型表示两种不同类型的双输入电力系统稳定器：

- 使用电功率和转速（或频率）信号计算加速功率积分的稳定器。这使得计算出的稳定器信号对机械变化不敏感。
- 使用电功率与转速或频率组合的稳定器。为实现所需的稳定信号整形，系统直接使用转速，无需相位超前补偿，并添加一个与电功率成比例的信号。

您可以通过使用 **Sample time (-1 for inherited)** 参数在模块的连续和离散实现之间切换。要将积分器配置为连续时间，请将 **Sample time (-1 for inherited)** 属性设置为 `0`。要将积分器配置为离散时间，请将 **Sample time (-1 for inherited)** 属性设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

此图说明了 PSS2C 电力系统稳定器的整体结构：

在图中：

- *V\_SI1* 和 *V\_SI2* 是两个电力系统稳定器输入。常用输入为转速、频率或功率。
- 每个稳定器输入表示两个洗出（离散或连续）模块，时间常数为
  *TW1* 至
  *TW4*，以及一个换能器，由低通滤波器（离散或连续）表示，时间常数为 *T6* 和
  *T7*。
- 为实现斜坡跟踪滤波器特性，Ramp Tracking Filter 子系统对串联的超前-滞后和低通滤波器模块网络进行建模。
- 为提供相位补偿，Lead-Lag（离散或连续）网络对与电力系统稳定器相关的附加动态进行建模，表示四级超前-滞后补偿，时间常数为
  *T1* 至
  *T4* 以及
  *T10* 至
  *T13*。
- PSS 输出逻辑子系统允许表示与发电机有功功率输出相关的 PSS 输出逻辑。
  *PPSSon* 和
  *PPSSoff* 是用于定义滞环的阈值。
