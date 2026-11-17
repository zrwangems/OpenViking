---
type: simulink-block
title: 'PS Harmonic Estimator (Amplitude, Phase)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Periodic Operators'
documentation_page: 'psharmonicestimatoramplitudephase'
documentation_source_path: 'ref/psharmonicestimatoramplitudephase.html'
language: zh-CN
chinese_source: worker-translation
---

# PS Harmonic Estimator (Amplitude, Phase)

## 端口
```yaml
ports:
- name: I
  summary: 周期信号，无类型物理信号
  direction: input
- name: A
  summary: 谐波信号的幅值，无类型物理信号
  direction: output
- name: Phi
  summary: 谐波信号的相位，rad 物理信号
  direction: output
```

### 输入

### **I** — 周期信号，无类型物理信号

输入物理信号。该信号必须是周期性的。

端口名称在模块图标中不可见，但您可以通过点击模块对话框的**描述**选项卡中的**源代码**链接，在底层源文件中查看此名称。
### 输出

### **A** — 谐波信号的幅值，无类型物理信号

对应于谐波幅值的输出物理信号。

### **Phi** — 谐波信号的相位，rad 物理信号

对应于谐波相位的输出物理信号。尽管物理输出端口是无类型的，但信号单位由模块方程决定。当将 PS-Simulink Converter 模块连接到此端口时，将其**输出信号单位**参数设置为 `1`，或设置为与角度单位 commensurate 的其他值。有关详细信息，请参阅角度单位。
## 参数
```yaml
parameters:
- name: 基频
  summary: 周期信号频率 60 Hz（默认值）
  group: ''
- name: 谐波次数
  summary: 谐波次数 1（默认值）
  group: ''
- name: 相位检测的最小幅值
  summary: 测量相位的最小信号幅值 0.001 1（默认值）
  group: ''
```

### **基频** — 周期信号频率 `60 Hz`（默认值）

周期信号的基频。

### **谐波次数** — 谐波次数 `1`（默认值）

周期信号中的谐波次数。该值必须为正整数。

### **相位检测的最小幅值** — 测量相位的最小信号幅值 `0.001 1`（默认值）

测量谐波相位所需的最小幅值。参数单位必须与输入信号的单位 commensurate。如果谐波幅值小于此值，则端口 **Phi** 的输出为 0。
## 所属库

Simscape / Foundation Library / Physical Signals / Periodic Operators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

### R2019a：单位传播

在 R2019a 之前，此模块不传播物理单位。

如果您的模型包含没有单位传播的旧版模块，请使用 Upgrade Advisor 将模块升级到最新版本。有关详细信息，请参阅升级包含旧版物理信号模块的模型。

## 描述

测量周期信号的谐波幅值和相位

PS Harmonic Estimator (Amplitude, Phase) 模块测量周期信号的单个频率分量（谐波）的幅值和相位。

如果信号在可测量的时间范围内完成一个模式（称为周期），并在随后的相同周期内重复该模式，则该信号是周期性的。信号基频是每秒的周期数。

该模块接受存在一个或多个谐波的物理信号。它输出所选谐波的相位和幅值。无类型物理端口便于单位传播。幅值的输出信号与输入信号具有相同的物理单位。相位的输出信号单位为弧度，或 1。有关详细信息，请参阅角度单位。

要获得有意义的结果，请至少运行信号的一个完整时间周期的仿真。
