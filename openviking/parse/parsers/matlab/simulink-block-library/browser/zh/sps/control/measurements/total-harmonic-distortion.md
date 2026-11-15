---
type: simulink-block
title: 'Total Harmonic Distortion'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'totalharmonicdistortion'
documentation_source_path: 'ref/totalharmonicdistortion.html'
language: zh-CN
chinese_source: worker-translation
---

# Total Harmonic Distortion

## 端口

### 输入

### **u** — 谐波幅值 标量 | 向量

谐波幅值。

**数据类型：** `single` | `double`
### 输出

### **THD (%)** — 总谐波失真 标量 | 向量

总谐波失真，以百分比表示。

**数据类型：** `single` | `double`

## 参数

### **Fundamental frequency** — 以 Hz 为单位的基波频率 `60` `Hz`（默认）

基波频率，以 Hz 为单位。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认） | 非负标量

连续模块执行之间的时间。
在执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅“什么是采样时间？”和“指定采样时间”。

对于继承的离散时间操作，指定 `-1`。对于离散时间操作，指定正整数。对于连续时间操作，指定 `0`。

为提高精度，请将此值设置为至少比 **Time constant** 参数小 10 倍。

**注意**

如果此模块位于掩膜子系统或其他允许连续或离散操作的变体子系统中，请提升采样时间参数，以确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅“在掩膜上提升模块参数”。

## 所属库

Simscape / Electrical / Control / Measurements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

总谐波失真测量

Total Harmonic Distortion 模块使用以下方程计算总谐波失真 (THD) 百分比：

M=harmonic magnitude2,

以及

%THD=100∑i=2nMi2M1,

其中：

- *Mi* 是第 i 个谐波阶次对应的谐波幅值的均方根
  (RMS) 值。
- *M* 是 *VRMS* 或
  *IRMS*。
- ∑i=2nMi2 是所有谐波分量之和。
