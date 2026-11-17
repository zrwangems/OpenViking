---
type: simulink-block
title: 'PWM Generator (Three-phase, Three-level)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgeneratorthreephasethreelevel'
documentation_source_path: 'ref/pwmgeneratorthreephasethreelevel.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Generator (Three-phase, Three-level)

## 端口
```yaml
ports:
- name: Vabc
  summary: 三相正弦参考信号向量
  direction: input
- name: vdc
  summary: 直流母线电压信号标量
  direction: input
- name: vneutral
  summary: 直流母线中性点平衡控制标量
  direction: input
- name: g
  summary: 门极控制向量
  direction: output
- name: ModWave
  summary: 调制波向量
  direction: output
```

### 输入

### **Vabc** — 三相正弦参考信号向量

指定您希望所连接的变换器输出的三个正弦电压，每相一个。

### **vdc** — 直流母线电压信号标量

为变换器的直流母线电压指定一个正实数。

### **vneutral** — 直流母线中性点平衡控制标量

该信号是用于平衡直流电源的反馈控制环路的输出。该信号的值必须是介于 `–1` 和 `+1` 之间的实数。

### 输出

### **g** — 门极控制向量

12 个脉冲波形，用于确定所连接功率变换器中的开关行为。

### **ModWave** — 调制波向量

如果您正在为具有 PWM 功能的硬件平台生成代码，则可以将调制波部署到硬件。否则，此数据仅供参考。
## 参数
```yaml
parameters:
- name: Continuous PWM
  summary: '连续脉宽调制方法 SPWM: sinusoidal PWM（默认）| SVM: space vector modulation'
  group: ''
- name: Sampling mode
  summary: 波形采样方法 Natural（默认）| Asymmetric | Symmetric
  group: ''
- name: Switching frequency (Hz)
  summary: 开关频率 1e3（默认）| 正数
  group: ''
- name: Sample time (s)
  summary: 模块采样时间 5e-5（默认）| 正数
  group: ''
```

### **Continuous PWM** — 连续脉宽调制方法 `SPWM: sinusoidal PWM`（默认）| `SVM: space vector modulation`

指定波形技术。

### **Sampling mode** — 波形采样方法 `Natural`（默认）| `Asymmetric` | `Symmetric`

采样模式决定了模块是在波形相交时采样调制波形，还是在载波处于其一个或两个边界条件时采样调制波形。

### **Switching frequency (Hz)** — 开关频率 `1e3`（默认）| 正数

指定您希望功率变换器中的开关进行开关的速率。

### **Sample time (s)** — 模块采样时间 `5e-5`（默认）| 正数

指定连续模块执行（输出计算）之间的时间间隔。为确保生成信号具有足够的分辨率，请将此值设置为小于或等于 `1/(10*Fsw)`，其中 *F*sw 为 **Switching frequency (Hz)**。
## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

生成用于门控开关器件的三相三电平脉宽调制信号或波形

PWM Generator (Three-phase, Three-level) 模块控制三相三电平功率变换器的开关行为。该模块：

1. 根据模块输入计算开通和关断门控时间：

   - 三个正弦参考电压
   - 一个直流母线电压
   - 一个直流母线中性点平衡控制信号
2. 使用门控时间生成 12 个开关控制脉冲。
3. 使用门控时间生成调制波形。

### 采样模式

此模块允许您选择调制波的自然采样、对称采样或不对称采样。

PWM Generator (Three-phase, Two-level) 模块不执行基于载波的脉宽调制（PWM）。相反，该模块使用输入信号计算门控时间，然后使用门控时间生成开关控制脉冲及其输出的调制波形。

然而，基于载波的 PWM 有助于展示您选择的采样模式与模块生成的脉冲的开关行为之间的关系。使用三电平基于载波 PWM 方法的发生器：

1. 对参考波进行采样。
2. 将采样值与两个平行的三角载波进行比较，两者相隔一个电平。
3. 如果采样值高于载波信号，则生成开通脉冲；如果采样值低于载波，则生成关断脉冲。

为了确定开通和关断脉冲行为，三电平基于载波的 PWM 发生器使用这些方法对每个三角波进行采样：

- 自然采样 — 采样和比较发生在调制波与载波的交点处。
- 不对称采样 — 采样发生在载波的上边界和下边界处。比较发生在采样之后的交点处。
- 对称采样 — 采样仅发生在载波的上边界处。比较发生在采样之后的交点处。

### 过调制

调制指数用于衡量功率变换器输出给定电压的能力，定义为

m=VMVC，

其中

- *m* 是调制指数。
- *Vm* 是调制波的峰值。
- *Vc* 是三角载波的峰值。

对于三相 SPWM，

Vpeak=mvdc2，

其中

- *Vpeak* 是相电压基波分量的峰值。
- *vdc* 是直流母线电压。

对于三相空间矢量 PWM（SVM），

Vpeak=mvdc3。

对于正常的稳态运行，`0` <*m* ≤
`1`。如果瞬态（例如负载增加）导致 *Vm* 的幅值超过
*Vc* 的幅值，则发生过调制
（*m* > `1`）

如果发生过调制，功率变换器的输出电压将钳位到正直流母线或负直流母线。

在 Three-Phase Three-Level PWM
Generator 示例中，**Three-Level Controller**
子系统包含一个 1800–V 直流母线输入，以及一个调制指数
*m*，其值为 0.8。对于 SVM，最大输入电压为 1800/3V，即 1039.23 V。为了演示过调制，在仿真开始时添加了一个瞬态。该瞬态迫使参考电压的幅值超过直流母线电压的 1/3。为了突出过调制，示波器仅包含 12 个输出脉冲中的一个以及参考电压、调制波形和输出电压的 *a* 相仿真结果。

调制指数在 0.03–0.09 秒之间大于 1。
在过调制期间：

- 脉冲保持在开通或关断位置。
- 输出电压钳位到正直流母线或负直流母线。
