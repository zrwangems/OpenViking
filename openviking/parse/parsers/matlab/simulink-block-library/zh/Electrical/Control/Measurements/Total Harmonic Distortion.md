---
type: simulink-block
title: 'Total Harmonic Distortion'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'totalharmonicdistortion'
documentation_source_path: 'ref/totalharmonicdistortion.html'
language: zh-CN
chinese_source: worker-translation
---

# Total Harmonic Distortion

## 端口
```yaml
ports:
- name: u
  summary: 谐波幅值 标量 | 向量
  direction: input
  data_types: single | double
- name: THD (%)
  summary: 总谐波失真 标量 | 向量
  direction: output
  data_types: single | double
```

### 输入

### **u** — 谐波幅值 标量 | 向量

谐波幅值。

**数据类型：** `single` | `double`
### 输出

### **THD (%)** — 总谐波失真 标量 | 向量

以百分比表示的总谐波失真。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Fundamental frequency
  summary: 基波频率，单位为 Hz 60 Hz（默认值）
  group: ''
- name: Sample time (-1 for inherited)
  summary: 模块采样时间 -1（默认值）| 非负标量
  group: ''
```

### **Fundamental frequency** — 基波频率，单位为 Hz `60` `Hz`（默认值）

基波频率，单位为 Hz。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认值）| 非负标量

连续模块执行之间的时间间隔。
在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，请指定 `-1`。对于离散时间操作，请指定正整数。对于连续时间操作，请指定 `0`。

为提高精度，请将此值设置为至少比 **Time constant** 参数小 10 倍。

**注意**

如果此模块位于掩码子系统或其他允许连续或离散操作的变体子系统中，请提升采样时间参数，以确保模块在连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。
## 所属库

Simscape / Electrical / Control / Measurements

## 模块特性

R2025b 中未记录。

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

- *Mi* 是对应于第 i 次谐波阶次的谐波幅值的均方根 (RMS) 值。
- *M* 是 *VRMS* 或 *IRMS*。
- ∑i=2nMi2 是所有谐波分量之和。
