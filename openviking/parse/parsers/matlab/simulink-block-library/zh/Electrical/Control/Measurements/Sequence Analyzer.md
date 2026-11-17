---
type: simulink-block
title: 'Sequence Analyzer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'sequenceanalyzer'
documentation_source_path: 'ref/sequenceanalyzer.html'
language: zh-CN
chinese_source: worker-translation
---

# Sequence Analyzer

## 端口
```yaml
ports:
- name: u
  summary: 周期性输入信号向量
  direction: input
- name: mag
  summary: 幅值标量 | 向量
  direction: output
- name: angle
  summary: 相移标量 | 向量
  direction: output
```

### 输入

### **u** — 周期性输入信号向量

周期性输入信号，指定为包含三个元素的向量。
### 输出

### **mag** — 幅值标量 | 向量

正序、负序或零序的幅值。根据谐波次数，此输出为标量或向量。

### **angle** — 相移标量 | 向量

正序、负序或零序的相移，以度为单位。根据谐波次数，此输出为标量或向量。
## 参数
```yaml
parameters:
- name: Base frequency (Hz)
  summary: 基频 60（默认值）
  group: ''
- name: Harmonic numbers
  summary: 谐波次数 [1 2]（默认值）| 标量或向量
  group: ''
- name: Sequence
  summary: 序分量选择 Positive（默认值）| Negative | Zero
  group: ''
- name: Sample Time (s)
  summary: 模块采样时间 0（默认值）
  group: ''
```

### **Base frequency (Hz)** — 基频 `60`（默认值）

输入信号的基频，以 Hz 为单位。

### **Harmonic numbers** — 谐波次数 `[1 2]`（默认值）| 标量或向量

谐波次数的标量或向量。`1` 表示基频，`2` 表示二次谐波。

### **Sequence** — 序分量选择 `Positive`（默认值）| `Negative` | `Zero`

选择序分量的幅值和相位为正序、负序还是零序。

### **Sample Time (s)** — 模块采样时间 `0`（默认值）

连续模块执行之间的时间。在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，指定 `-1`。对于离散时间操作，指定正整数。对于连续时间操作，指定 `0`。

如果此模块位于掩码子系统或其他允许在连续操作和离散操作之间切换的变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。
## 所属库

Simscape / Electrical / Control / Measurements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

计算三相信号的正序、负序或零序的幅值和相位

Sequence Analyzer 模块将三相信号（通常为电压）作为输入，并输出正序、负序或零序的幅值和相位。

输入信号首先根据模块掩码中指定的基频和谐波转换为相量表示。然后，模块将相量变换为序分量。

您可以用相量表示中的 *V0*、*V1*、*V2* 表示零序、正序和负序分量；*Va*、*Vb*、*Vc* 为三相电压。序分量计算如下：

[V0V1V2]=13[1111aa21a2a2][VaVbVc]

其中 a=ej23π。
