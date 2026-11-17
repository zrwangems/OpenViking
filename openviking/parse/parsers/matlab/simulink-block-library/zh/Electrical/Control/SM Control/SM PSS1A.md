---
type: simulink-block
title: 'SM PSS1A'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smpss1a'
documentation_source_path: 'ref/smpss1a.html'
language: zh-CN
chinese_source: worker-translation
---

# SM PSS1A

## 端口

### 输入

### **V\_SI** — 转速、频率或功率标量

标幺转速、终端母线电压频率、补偿频率或电功率，指定为标量。

**数据类型：** `single` | `double`
### 输出

### **V\_ST** — 稳定转速、频率或功率标量

自动电压调节器输入稳定信号，受
*VST\_min* 和
*VST\_max* 限制，以标量形式返回。

**数据类型：** `single` | `double`

## 参数

### **Power system stabilizer (PSS) gain, K\_S (pu)** — 电力系统稳定器增益 3.15（默认）| 标量

电力系统稳定器前向通道增益。

### **PSS denominator constant for second-order block, A\_1** — 滤波器常数 1 `0`（默认）| 标量

电力系统稳定器信号调理滤波器系数 1。

### **PSS denominator constant for second-order block, A\_2** — 滤波器常数 2 `0`（默认）| 标量

电力系统稳定器信号调理滤波器系数 2。

### **PSS numerator (lead) compensating time constant, T\_1 (s)** — 超前时间常数 1 `0.76`（默认）| 标量

超前时间常数 1，与图中的第一个超前-滞后模块相关联。

### **PSS denominator (lag) compensating time constant, T\_2 (s)** — 滞后时间常数 2 `0.01`（默认）| 标量

滞后时间常数 2，与图中的第一个超前-滞后模块相关联。

### **PSS numerator (lead) compensating time constant, T\_3 (s)** — 超前时间常数 3 `0.76`（默认）| 标量

超前时间常数 3，与图中的第二个超前-滞后模块相关联。

### **PSS denominator (lag) compensating time constant, T\_4 (s)** — 滞后时间常数 4 `0.01`（默认）| 标量

滞后时间常数 4，与图中的第二个超前-滞后模块相关联。

### **PSS washout time constant, T\_5 (s)** — 洗出时间常数 `10`（默认）| 标量

洗出时间常数，与图中的洗出模块相关联。

### **PSS transducer time constant, T\_6 (s)** — 传感器时间常数 `0`（默认）| 标量

传感器时间常数，与图中的低通滤波器模块相关联。

### **Maximum PSS output, V\_STmax (pu)** — 最大稳定信号 `0.09`（默认）| 标量

电力系统稳定器输出到自动电压调节器（AVR）的最大值。

### **Minimum PSS output, V\_STmin (pu)** — 最小稳定信号 `-0.09`（默认）| 标量

电力系统稳定器输出到自动电压调节器（AVR）的最小值。

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

**在 R2018b 中引入**

## 描述

离散时间或连续时间单输入 PSS1A 电力系统稳定器

SM PSS1A 模块实现单输入 PSS1A 电力系统稳定器
（PSS），用于维持同步电机（SM）的转子角稳定性，符合 IEEE 421.5-2016[1]。
通常，您使用 PSS 通过励磁控制来增强电力系统振荡的阻尼。

您可以通过 **Sample time (-1 for inherited)** 参数在模块的连续和离散实现之间切换。要将
积分器配置为连续时间，请将 **Sample time (-1 for
inherited)** 属性设置为 `0`。要将积分器
配置为离散时间，请将 **Sample time (-1 for inherited)** 属性
设置为正的非零值，或设置为 `-1` 以从上游模块继承采样时间。

此图展示了 PSS1A 电力系统稳定器的整体结构：

在图中：

- *V\_SI* 是电力系统稳定器输入。常用的
  输入为转速、频率或功率。有关详细信息，请参阅 V\_SI。
- 低通滤波器（离散或连续）模块可用于
  对传感器建模，其时间常数为
  *T6*。
- *Ks* 对稳定器
  增益进行建模。
- 洗出（离散或连续）模块
  对高通滤波器进行建模。此处，
  *T5* 为时间
  常数。
- 二阶低通滤波器（离散或连续）模块
  考虑了高频扭转滤波器
  的低频效应。此处，*A1* 和
  *A2* 为稳定器
  二阶模块的分母常数。
- 两个超前-滞后（离散或连续）模块
  对与电力系统稳定器相关的附加动态进行建模，并表示
  超前-滞后补偿的两个阶段。
