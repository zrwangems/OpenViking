---
type: simulink-block
title: 'PWM Generator (Three-phase, Two-level)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Pulse Width Modulation'
documentation_page: 'pwmgeneratorthreephasetwolevel'
documentation_source_path: 'ref/pwmgeneratorthreephasetwolevel.html'
language: zh-CN
chinese_source: worker-translation
---

# PWM Generator (Three-phase, Two-level)

## 端口
```yaml
ports:
- name: Vabc
  summary: 三相正弦参考信号向量
  direction: input
- name: vdc
  summary: 直流母线电压信号标量
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

指定三个正弦电压，每相一个，即您希望所连接的变换器输出的电压。

### **vdc** — 直流母线电压信号标量

为变换器的直流母线电压指定一个正实数。
### 输出

### **g** — 门极控制向量

六个脉冲波形，用于确定所连接功率变换器中的开关行为。

### **ModWave** — 调制波向量

如果您要为具有 PWM 功能的硬件平台生成代码，可以将调制波部署到硬件。否则，此数据仅供您参考。
## 参数
```yaml
parameters:
- name: PWM mode
  summary: 脉宽调制方法 Continuous PWM (CPWM)（默认）| Discontinuous PWM (DPWM)
  group: ''
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
- name: Discontinuous PWM (DPWM)
  summary: '钳位方法 60 DPWM: 60 degree discontinuous PWM（默认）'
  group: ''
```

### **PWM mode** — 脉宽调制方法 `Continuous PWM (CPWM)`（默认）| `Discontinuous PWM (DPWM)`

不连续 PWM 在每个基波周期内将波形钳位到直流母线总计 120 度。连续 PWM 不进行钳位。

### **Continuous PWM** — 连续脉宽调制方法 `SPWM: sinusoidal PWM`（默认）| `SVM: space vector modulation`

#### 依赖关系

**Continuous PWM** 参数仅在将 **PWM mode** 参数设置为 `Continuous PWM (CPWM)` 时可用。

### **Sampling mode** — 波形采样方法 `Natural`（默认）| `Asymmetric` | `Symmetric`

采样模式决定了模块是在波形相交时采样调制波形，还是在载波处于其一个或两个边界条件时采样调制波形。

### **Switching frequency (Hz)** — 开关频率 `1e3`（默认）| 正数

指定您希望功率变换器中的开关进行开关的速率。

### **Sample time (s)** — 模块采样时间 `5e-5`（默认）| 正数

指定连续模块执行（输出计算）之间的时间间隔。为确保生成信号具有足够的分辨率，请将此值设置为小于或等于 `1/(10*Fsw)`，其中 *F*sw 为 **Switching frequency (Hz)**。

### **Discontinuous PWM (DPWM)** — 钳位方法 `60 DPWM: 60 degree discontinuous PWM`（默认）

指定在每个周期内分配 120 度的方法，在此期间模块将调制波钳位到直流母线。其他选项包括：

- `60 DPWM (+30 degree shift): +30 degree shift from
  60 DPWM`
- `60 DPWM (-30 degree shift): -30 degree shift from
  60 DPWM`
- `30 DPWM: 30 degree discontinuous
  PWM`
- `120 DPWM: positive dc
  component`
- `120 DPWM: negative dc
  component`

当波形被钳位时，调制中断。

#### 依赖关系

**Discontinuous PWM** 参数仅在将 **PWM mode** 参数设置为 `Discontinuous PWM (DPWM)` 时可用。
## 所属库

Simscape / Electrical / Control / Pulse Width Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

生成三相、两电平脉宽调制波形

PWM Generator (Three-phase, Two-level) 模块控制三相、两电平功率变换器的开关行为。该模块：

1. 根据模块输入计算开通和关断门极时间：

   - 三个正弦参考电压，每相一个
   - 一个直流母线电压
2. 使用门极时间生成六个控制开关的脉冲。
3. 使用门极时间生成调制波形。

### 连续和不连续 PWM

该模块提供连续和不连续脉宽调制（PWM）两种模式。该图显示了连续正弦 PWM（SPWM）和连续空间矢量调制（SVM）波形之间的一般区别。

对于不连续 PWM（DPWM），该模块在每个基波周期内将调制波钳位到正或负直流母线总计 120 度。在钳位区间内，调制中断。

具有 30 度 DPWM 的波形在每个基波周期内有四个 30 度区间。

选择正或负 30 度相移会影响 60 度 DPWM 的钳位区间。

该图显示了 120 度 DPWM 的正直流钳位和负直流钳位波形。

### 采样模式

该模块允许您选择调制波的自然采样、对称采样或不对称采样。

PWM Generator (Three-phase, Two-level) 模块不执行基于载波的 PWM。相反，该模块使用输入信号计算门极时间，然后使用门极时间生成其输出的控制开关脉冲和调制波形。

然而，基于载波的 PWM 有助于说明您选择的采样模式与模块生成的脉冲的开通和关断行为之间的关系。使用两电平、基于载波 PWM 方法的发生器：

1. 采样参考波。
2. 将采样值与三角载波进行比较。
3. 如果采样值高于载波信号，则生成开通脉冲；如果采样值低于载波，则生成关断脉冲。

为确定开通和关断脉冲行为，两电平基于载波的 PWM 发生器使用以下方法对三角波进行采样：

- Natural — 采样和比较发生在调制波与载波的交点处。
- Asymmetric — 采样发生在载波的上边界和下边界处。比较发生在采样之后的交点处。
- Symmetric — 采样仅发生在载波的上边界处。比较发生在采样之后的交点处。

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

对于三相空间矢量 PWM（SVM）和 DPWM，

Vpeak=mvdc3。

对于正常稳态运行，`0` <*m* ≤ `1`。如果瞬态（例如负载增加）导致 *Vm* 的幅值超过 *Vc* 的幅值，则发生过调制（*m* > `1`）。

如果发生过调制，功率变换器的输出电压钳位到正或负直流母线。

在 Three-Phase Two-Level PWM Generator 示例中，**Two-Level Controller** 子系统包含一个 400–V 直流母线输入，以及调制指数 *m* 为 0.8。对于 SPWM，最大输入电压为 400 V/2，即 200 V。为演示过调制，在仿真开始时添加了一个瞬态。该瞬态迫使参考电压的幅值超过直流母线电压 1/2 的幅值。为突出过调制，示波器仅包含六个输出脉冲中一个的仿真结果，以及参考电压、调制波形和输出电压的仅 *a* 相。

调制指数在 0.03–0.09 秒之间大于 1。在过调制期间：

- 脉冲保持在开通或关断位置。
- 输出电压 *Vao* 钳位到正或负直流母线。
