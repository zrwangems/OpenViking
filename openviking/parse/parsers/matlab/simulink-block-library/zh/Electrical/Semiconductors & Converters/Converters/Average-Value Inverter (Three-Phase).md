---
type: simulink-block
title: 'Average-Value Inverter (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'averagevalueinverterthreephase'
documentation_source_path: 'ref/averagevalueinverterthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Average-Value Inverter (Three-Phase)

## 端口
```yaml
ports:
- name: +
  summary: 正极端子 electrical
  direction: conserving
- name: '-'
  summary: 负极端子 electrical
  direction: conserving
- name: '~'
  summary: 三相端口 electrical
  direction: conserving
- name: a
  summary: '*a* 相 electrical'
  direction: conserving
- name: b
  summary: '*b* 相 electrical'
  direction: conserving
- name: c
  summary: '*c* 相 electrical'
  direction: conserving
```

### 守恒端口

### **+** — 正极端子 electrical

与正极端子关联的电气守恒端口

### **-** — 负极端子 electrical

与负极端子关联的电气守恒端口

### **~** — 三相端口 electrical

可扩展三相端口

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a** — *a* 相 electrical

与 *a* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相 electrical

与 *b* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相 electrical

与 *c* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。
## 参数
```yaml
parameters:
- name: Electrical connection
  summary: 电气连接 Composite three-phase ports（默认）| Expanded three-phase ports
  group: ''
- name: Rated AC frequency
  summary: 交流频率，单位为 Hz 60Hz（默认）
  group: ''
- name: Phase shift
  summary: 相移 0deg（默认）
  group: ''
- name: Ratio of rated AC voltage to rated DC voltage
  summary: 额定交流电压与额定直流电压之比 sqrt(6) / pi（默认）
  group: ''
- name: Fixed power loss
  summary: 固定功率损耗 1e3W（默认）
  group: ''
- name: DC voltage for turn on
  summary: 导通直流电压 100V（默认）
  group: ''
- name: DC voltage for turn off
  summary: 关断直流电压 75V（默认）
  group: ''
```

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

选择使用复合三相端口还是扩展三相端口。

### **Rated AC frequency** — 交流频率，单位为 Hz `60``Hz`（默认）

交流频率，以 Hz 为单位指定（其中 Hz 定义为 1/s）。例如，kHz 和 MHz 是有效单位，但 rad/s 不是。

### **Phase shift** — 相移 `0``deg`（默认）

以角度单位表示的相移。

### **Ratio of rated AC voltage to rated DC voltage** — 额定交流电压与额定直流电压之比 `sqrt(6) / pi`（默认）

下表列出了常见三相两电平逆变器控制模式的比值。默认值为 6/π。

对于 180° 和 120° 导通模式，所列电压为线电压的基波 RMS 值。对于其他方法，所列电压为线电压的最大基波 RMS 值。

您可以根据特定要求控制逆变器的输出电压。DPWM 包括 30° DPWM、60° DPWM 和 120° DPWM。有关详细信息，请参阅参考文献 [3] 和 [4]。

| **控制方法** | ***V RMS（线电压）*** | ***V RMS（线电压）* 与 *v DC* 之比** |
| --- | --- | --- |
| 180° 导通模式 [1] | 6πVDC | 0.7797 |
| 120° 导通模式 [1] | 32πVDC | 0.6752 |
| 滞环电流控制 [2] | (32)(2VDCπ) | 0.7797 |
| 正弦 PWM (SPMW) [2] | (32)(VDC2) | 0.6124 |
| 空间矢量调制 (SVM) [2] | (32)(VDC3) | 0.7071 |
| 不连续 PWM (DPWM) [3], [4] | (32)(VDC3) | 0.7071 |
| 转换为平均整流器的原始交流电压 | (π2)(VDC3) | 0.7405 |

### **Fixed power loss** — 固定功率损耗 `1e3``W`（默认）

直流侧汲取的最小功率。默认值为 `1e3`。

### **DC voltage for turn on** — 导通直流电压 `100``V`（默认）

当直流电源电压升至该值以上时，逆变器产生交流输出电压。

### **DC voltage for turn off** — 关断直流电压 `75``V`（默认）

当直流电源电压降至该值以下时，逆变器关断，模块将输出交流电流设置为零。
## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在早期版本保存的模型中，请检查此模块的 **Electrical connection** 参数。

## 描述

具有固定功率损耗的平均值直流电压到三相交流电压转换器

Average-Value Inverter (Three-Phase) 模块对平均值全波逆变器进行建模。它将直流电压转换为三相交流电压，并将三相交流功率需求转换为直流功率需求。相应的直流功率需求等于固定功率损耗与交流功率需求之和。

您只能将 Average-Value Inverter (Three-Phase) 模块用作全波逆变器。它表现为直流电压控制的交流电压源。您指定的比值决定直流电压与交流电压之间的比值。

该图显示了逆变器作为全波逆变器的等效电路。然而，Average-Value Inverter (Three-Phase) 模块不会产生通常与详细表示相关的谐波，因为它执行的是平均值功率转换。

### 电气定义方程

电压定义为

vDC=vp−vn，

vref=vp+vn2，

vRMS=vratiovDC，

V0=23VRMS，

va=V0sin(2πft+φ)+vref，

vb=V0sin(2πft+φ−120∘)+vref，

以及

vc=V0sin(2πft+φ+120∘)+vref，

其中：

- *vp* 和 *vn* 分别是逆变器正极和负极端子处的电压。
- *vDC* 是逆变器正极和负极端子之间的电压差。
- *vref* 是直流偏置。
- *Vratio* 是逆变器的额定交流电压与额定直流电压之比。有关常见逆变器控制模式的 *Vratio* 值，请参阅参数中的 **Ratio of rated AC voltage to rated DC voltage** 参数。
- *VRMS* 是 RMS 交流线电压。
- *V0* 是峰值相电压。
- *f* 是频率。
- *t* 是时间。
- *φ* 是相移。
- *va*、*vb*、*vc* 分别是交流相电压。

功率、电阻和电流定义为

PAC=−vaia−vbib−vcic，

RDC=vDC2PAC+Pfixed，

以及

i=vDCRDC，

其中：

- *ia*、*ib* 和 *ic* 分别是流入逆变器的交流相电流。
- *PAC* 是交流侧的输出功率。*PAC* 的最小限值为 `0` W。
- *Pfixed* 是您在模块上指定的固定功率损耗。
- *RDC* 是直流侧的电阻。
- *i* 是从逆变器正极端子流向负极端子的电流。

当直流电源电压高于您为 **DC voltage for turn on** 参数指定的值时，逆变器开始产生交流电压，即导通。当直流电源电压降至您为 **DC voltage for turn off** 参数指定的值以下时，它停止逆变，即关断。当逆变器关断时，模块将输出交流电流设置为零。
