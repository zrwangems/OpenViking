---
type: simulink-block
title: 'Power Measurement (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'powermeasurementthreephase'
documentation_source_path: 'ref/powermeasurementthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Power Measurement (Three-Phase)

## 端口

### 输入

### **V** — 输入电压向量

用于测量功率的元件两端的三相电压，单位为 V。

**数据类型：** `single` | `double`

### **I** — 输入电流向量

用于测量功率的元件中流过的三相电流，单位为 A。

**数据类型：** `single` | `double`
### 输出

### **P** — 有功功率标量或向量 | 向量

所选频率分量的有功功率，单位为 W。如果 **Harmonic numbers** 参数值为标量，则该输出也为标量。

**数据类型：** `single` | `double`

### **Q** — 无功功率标量或向量 | 向量

所选频率分量的无功功率，单位为 var。如果 **Harmonic numbers** 参数值为标量，则该输出也为标量。

**数据类型：** `single` | `double`

## 参数

### **Base frequency (Hz)** — 基波频率 `60`（默认）| 正数

对应于分量 *k=1* 的基波频率。

### **Harmonic numbers** — 频率分量 `[0 1 2 3]`（默认）| 标量或向量

要包含在输出中的频率分量。指定对应于所需分量的标量值，或指定所有所需分量的向量。

- 值 *k = 0* 对应于直流分量。
- 值 *k = 1* 对应于基波频率。
- 值 *k > 1* 对应于更高次谐波。

如果指定向量，则功率输出的顺序与此向量的顺序相对应。

### **Sequence** — 对称序分量 `Positive`（默认）| `Negative` | `Zero`

功率输出的对称序分量。

### **Sample time** — 模块采样时间 `0`（默认）| 正数

连续两次模块执行之间的时间。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于连续运行，将此属性设置为 `0`。对于离散运行，将采样时间显式指定为正数。此模块不支持继承采样时间。

如果此模块位于掩码子系统或其他允许连续和离散运行的变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / Measurements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

计算三相有功功率和无功功率

Power Measurement (Three-Phase) 模块测量三相网络中某个元件的有功功率和无功功率。该模块输出所选对称序分量中您指定的每个频率分量的功率量。

使用此模块可测量正弦和非正弦周期信号的功率。对于单相功率测量，请考虑使用 Power Measurement 模块。

将 **Sample time** 参数设置为 `0` 以进行连续时间运行，或显式设置以进行离散时间运行。

使用 **Harmonic numbers** 参数指定要包含在功率输出中的所有频率分量的向量：

- 要输出直流分量，请指定 `0`。
- 要输出对应于基波频率的分量，请指定 `1`。
- 要输出对应于高次谐波的分量，请指定 `n > 1`。

### 方程

对于每个指定的谐波 *k*，该模块根据相量方程计算指定序分量的有功功率 *Pk* 和无功功率 *Qk*：

Pk+jQk=32(VkejθVk)(IkejθIk¯),

其中：

- VkejθVk 是表示所选序分量的 *k* 次分量电压的相量。
- IkejθIk¯ 是 IkejθIk 的复共轭，IkejθIk 是表示所选序分量的 *k* 次分量电流的相量。

使用 **Sequence** 参数选择功率计算中使用的对称序分量：

- `Positive`：

  VkejθVk=Vk+ejθVk+, IkejθIk=Ik+ejθIk+
- `Negative`：

  VkejθVk=Vk−ejθVk−, IkejθIk=Ik−ejθIk−
- `Zero`：

  VkejθVk=Vk0ejθVk0, IkejθIk=Ik0ejθIk0

该模块使用对称分量变换 *S* 从 *abc* 电压相量集合计算对称的 *+-0* 电压相量集合：

[Vk+ejθVk+Vk−ejθVk−Vk0ejθVk0]=S[VkaejθVkaVkbejθVkbVkcejθVkc].

有关此变换的详细信息，请参阅 Symmetrical Components Transform。

该模块从三相输入电压 *V(t)* 获得此 *abc* 电压相量集合，如下所示：

[VkaejθVkaVkbejθVkbVkcejθVkc]=2T∫t−TtV(t)sin(2πkFt)dt+j2T∫t−TtV(t)cos(2πkFt)dt,

其中 *T* 是输入信号的周期，或者等效地为其基波频率 *F* 的倒数。

该模块以与计算电压相同的方式计算对称电流相量集合。

如果输入信号具有有限数量的谐波 *n*，则指定序分量的总有功功率 *P* 和总无功功率 *Q* 可由其分量计算得出：

P=∑k=0nPk

Q=∑k=1nQk.

*Q* 的求和不包括直流分量（*k = 0*），因为该分量仅对有功功率有贡献。
