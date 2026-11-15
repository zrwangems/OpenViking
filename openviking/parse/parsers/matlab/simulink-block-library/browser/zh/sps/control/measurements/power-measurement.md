---
type: simulink-block
title: 'Power Measurement'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'powermeasurement'
documentation_source_path: 'ref/powermeasurement.html'
language: zh-CN
chinese_source: official
---

# Power Measurement

## 端口

### 输入

### **v** — 输入电压 标量

元件两端的电压（用于测量功率），单位为 V。

**数据类型:** `single` | `double`

### **i** — 输入电流 标量

通过元件的电流（用于测量功率），单位为 A。

**数据类型:** `single` | `double`
### 输出

### **P** — 实际功率 标量或向量

选定频率分量的实际功率，单位为 W。如果**谐波次数**参数值是标量，则此输出也是标量。

**数据类型:** `single` | `double`

### **Q** — 无功功率 标量或向量

选定频率分量的无功功率，单位为 var。如果**谐波次数**参数值是标量，则此输出也是标量。

**数据类型:** `single` | `double`

## 参数

### **基础频率(Hz)** — 基频 `60` (默认) | 正数

对应于分量 *k=1* 的基频。

### **谐波次数** — 频率分量 `[0 1 2 3]` (默认) | 标量或向量

要包含在输出中的频率分量。指定对应于所需分量的标量值或由所有所需分量组成的向量。

- 值 *k = 0* 对应于 DC 分量。
- 值 *k = 1* 对应于基频。
- 值 *k > 1* 对应于更高水平的谐波。

如果指定一个向量，则功率输出的阶数对应于该向量的阶数。

### **采样时间** — 模块采样时间 `0` (默认) | 正数

连续两次模块执行之间的时间。在执行期间，模块产生输出，并在需要时更新其内部状态。有关详细信息，请参阅什么是采样时间？和指定采样时间。

对于连续运行，将此属性设置为 `0`。对于离散运行，将采样时间显式指定为一个正数。此模块不支持继承的采样时间。

如果此模块位于封装子系统或允许连续运行和离散运行的其他可变子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / Measurements

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2017b 中推出**

## 描述

计算单相实际功率和无功功率

Power Measurement 模块测量单相网络中元件的实际功率和无功功率。该模块输出您指定的每个频率分量的功率数量。对于三相测量，请考虑使用 Three-Phase Power Measurement 模块。

使用此模块可测量正弦和非正弦周期性信号的功率。

对于连续时间运行，将**采样时间**参数设置为 `0`，对于离散时间运行，则显式设置为特定值。

使用**谐波次数**参数指定由要包含在功率输出中的所有频率分量组成的向量：

- 要输出 DC 分量，请指定 `0`。
- 要输出对应于基频的分量，请指定 `1`。
- 要输出对应于更高阶谐波的分量，请指定 `n > 1`。

### 方程

对于每个指定的谐波 *k*，模块根据相量方程计算实际功率 *Pk* 和无功功率 *Qk*：

Pk+jQk=G(VkejθVk)(IkejθIk¯),

其中：

- 对于 DC 分量 (*k = 0*)，*G* 等于 `0.25`；对于 AC 分量 (*k > 0*)，则等于 `0.5`。
- VkejθVk 是 *k* 分量输入电压的相量表示形式。
- IkejθIk¯ 是 IkejθIk 的复共轭，后者是 *k* 分量输入电流的相量表示形式。

模块使用以下关系估计实时 *k* 分量电压和电流相量：

VkejθVk=2T∫t−TtV(t)sin(2πkFt)dt+j2T∫t−TtV(t)cos(2πkFt)dt

IkejθIk=2T∫t−TtI(t)sin(2πkFt)dt+j2T∫t−TtI(t)cos(2πkFt)dt.

在这些相量方程中：

- *V(t)* 和 *I(t)* 分别是输入电压和输入电流。
- *T* 是输入信号的周期，或是其基础频率 *F* 的倒数，这两者是等效的。

如果输入信号具有有限谐波数 *n*，则可以根据其分量计算总实际功率 *P* 和总无功功率 *Q*：

P=∑k=0nPk

Q=∑k=1nQk.

对 *Q* 求和不包括 DC 分量 (*k = 0*)，因为该分量仅对实际功率有贡献。
