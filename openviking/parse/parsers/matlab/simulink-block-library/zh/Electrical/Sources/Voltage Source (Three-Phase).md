---
type: simulink-block
title: 'Voltage Source (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'voltagesourcethreephase'
documentation_source_path: 'ref/voltagesourcethreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Voltage Source (Three-Phase)

## 端口
```yaml
ports:
- name: '~'
  summary: 三相端口电气
  direction: conserving
- name: n
  summary: 星形中性点电气
  direction: conserving
```

### 守恒端口

### **~** — 三相端口电气

与三相 *a*、*b* 和 *c* 相关联的可扩展三相端口。

### **n** — 星形中性点电气

与星形中性点相关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否对复合或扩展三相端口建模 Composite three-phase ports（默认）| Expanded three-phase ports
  group: ''
- name: Rated voltage (phase-to-phase RMS)
  summary: RMS 线电压 sqrt(3) * 100 / sqrt(2) V（默认）
  group: 主
- name: Phase shift
  summary: 相移 0 deg（默认）
  group: 主
- name: Frequency
  summary: 电压频率 60 Hz（默认）
  group: 主
- name: Source impedance
  summary: 源阻抗方法 X/R Ratio（默认）| None | Series R | Series L | Series RL
  group: 主
- name: Short-circuit power level
  summary: 短路功率水平 1e6 V*A（默认）
  group: 主
- name: Source X/R ratio
  summary: 电抗与电阻之比 15（默认）
  group: 主
- name: Source resistance
  summary: 源电阻 0.01 Ohm（默认）
  group: 主
- name: Source inductance
  summary: 源电感 3.97e-4 H（默认）
  group: 主
- name: Source harmonics
  summary: 源谐波 None（默认）| Generate harmonics
  group: 谐波
- name: Harmonic orders
  summary: 谐波次数 [5, 7, 11, 13]（默认）
  group: 谐波
- name: Harmonic magnitude to peak magnitude ratios
  summary: 谐波幅值与峰值幅值之比 [.1, .1, .1, .1]（默认）
  group: 谐波
- name: Source impedance parasitic parallel conductance
  summary: 源阻抗寄生并联电导 0 1/Ohm（默认）
  group: 寄生参数
```

### **Modeling option** — 是否对复合或扩展三相端口建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是否对复合或扩展三相端口建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口来构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口来表示三相系统的各个相。

### 主

### **Rated voltage (phase-to-phase RMS)** — RMS 线电压 `sqrt(3) * 100 / sqrt(2)` `V`（默认）

RMS 相间电压，即线电压。

### **Phase shift** — 相移 `0` `deg`（默认）

以角度单位表示的相移。

### **Frequency** — 电压频率 `60` `Hz`（默认）

电压频率，以 Hz 或可直接转换为 Hz 的单位指定（其中 Hz 定义为 1/s）。例如，`kHz` 和 `MHz` 是有效单位，但 `rad/s` 不是。

### **Source impedance** — 源阻抗方法 `X/R Ratio`（默认）| `None` | `Series R` | `Series L` | `Series RL`

选择用于指定源阻抗的方法。默认选项为 `X/R Ratio`。选择任何其他选项将启用其他参数。选项包括：

- `None`
- `X/R Ratio`
- `Series R`
- `Series L`
- `Series RL`

### **Short-circuit power level** — 短路功率水平 `1e6` `V*A`（默认）

短路功率水平。

#### 依赖关系

仅当为 **Source Impedance** 参数选择 `X/R Ratio` 时，此参数才可见。

### **Source X/R ratio** — 电抗与电阻之比 `15`（默认）

复数阻抗，即电抗与电阻之比。

#### 依赖关系

仅当为 **Source Impedance** 参数选择 `X/R Ratio` 时，此参数才可见。

### **Source resistance** — 源电阻 `0.01` `Ohm`（默认）

源电阻。

#### 依赖关系

仅当为 **Source Impedance** 参数选择 `Series R` 或 `Series RL` 时，此参数才可见。

### **Source inductance** — 源电感 `3.97e-4` `H`（默认）

源电感。

#### 依赖关系

仅当为 **Source Impedance** 参数选择 `Series L` 或 `Series RL` 时，此参数才可见。

### 谐波

### **Source harmonics** — 源谐波 `None`（默认）| `Generate harmonics`

在 `None` 和 `Generate harmonics` 之间选择。默认值为 `None`。

### **Harmonic orders** — 谐波次数 `[5, 7, 11, 13]`（默认）

要生成谐波的附加整数谐波次数的行向量。

#### 依赖关系

仅当为 **Source representation** 参数选择 `Generate harmonics` 时，此参数才可见。

### **Harmonic magnitude to peak magnitude ratios** — 谐波幅值与峰值幅值之比 `[.1, .1, .1, .1]`（默认）

谐波幅值相对于基波幅值的比值的行向量。

#### 依赖关系

仅当为 **Source representation** 参数选择 `Generate harmonics` 时，此参数才可见。

### 寄生参数

### **Source impedance parasitic parallel conductance** — 源阻抗寄生并联电导 `0` `1/Ohm`（默认）

源阻抗寄生并联电导。

#### 依赖关系

仅当为 **Source Impedance** 参数选择 `X/R Ratio`、`Series L` 或 `Series RL` 时，此参数才可见。
## 所属库

Simscape / Electrical / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

带可选谐波的理想三相电压源

Voltage Source (Three-Phase) 模块对理想三相电压源或带谐波的三相电压源进行建模。您可以使用 Source representation 参数指定配置。

当为 **Source Impedance** 参数选择 `None` 时，Voltage Source 模块对理想三相电压源进行建模，该电源在其端子上维持指定幅值的正弦电压，与流过电源的电流无关。

该电源采用星形配置，端口 **n** 提供与星形中性点的连接。端口 **~** 是表示三相 *a*、*b* 和 *c* 的可扩展三相端口。如果电流从星形中性点流向正端子，则电流为正，每相两端的电压等于正端子电压与星形中性点电压之差，即 *V*(+) – *V*n。

### 方程

Voltage Source 模块的输出电压由以下方程定义：

v=vDC+vACsin(2πft+ϕ)+vN

va=V0sin(2πft+φ)

vN=Pv/2N(0,1)h

vc=V0sin(2πft+φ+120∘),

其中：

- *V0* 是峰值相电压。
- *vline\_rms* 是均方根（RMS）相间电压。
- *va*、*vb*、*vc* 是各自的相电压。
- *f* 是频率。
- *φ* 是相移。
- *t* 是时间。

当您指定带谐波表示的三相电压源时，Voltage Source 模块的输出电压由以下方程定义：

V0=23vline\_rmsHratios

va=V0sin((2πft+φ)Horders')

vb=V0sin((2πft+φ−θ)Horders'​)

vc=V0sin((2πft+φ+θ)Horders'),

其中：

- *V0* 是包含基波和谐波正弦波峰值电压的行向量。
- *vline\_rms* 是 RMS 相间电压。
- *Hratios* 是谐波比值的行向量。第一个元素为 1，表示基波。
- *Horders* 是谐波次数的行向量。第一个元素为 1，表示基波。
- *va*、*v*b、*v*c 是各自的相电压。
- *f* 是谐波频率的列向量。第一个元素是基波频率。
- *φ* 是谐波相移的列向量。第一个元素是基波相移。
- *θ* 是谐波相位偏移的列向量。第一个元素是 `120°`。
- *t* 是时间。

当为 **Source Impedance** 参数选择 `X/R ratio` 时，源阻抗的方程为：

R=vline\_rms2Ssc1+ϕ2

X=Rϕ

L=X2πf,

其中：

- *Ssc* 是您指定的 **Short-circuit power level**。
- *ϕ* 是您指定的 **Source X/R ratio**。
- *R* 是计算得到的源电阻。
- *X* 是计算得到的源电抗。
- *L* 是计算得到的源电感。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
