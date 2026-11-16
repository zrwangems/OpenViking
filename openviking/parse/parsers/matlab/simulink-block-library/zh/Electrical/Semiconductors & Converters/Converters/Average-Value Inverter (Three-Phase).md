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

### 守恒

### **+** — 正极端子电气

与正极端子关联的电气守恒端口

### **-** — 负极端子电气

与负极端子关联的电气守恒端口

### **~** — 三相端口电气

可扩展三相端口

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`。

### **a** — *a* 相电气

与 *a* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相电气

与 *b* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相电气

与 *c* 相相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`。

## 参数

### **电气连接** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是使用复合三相端口还是扩展三相端口。

### **额定交流频率** — 以 Hz 为单位的交流频率 `60``Hz`（默认）

交流频率，以 Hz 为单位指定（其中 Hz 定义为 1/s）。例如，kHz 和 MHz 是有效单位，但 rad/s 不是。

### **相移** — 相移 `0``deg`（默认）

以角度单位表示的相移。

### **额定交流电压与额定直流电压之比** — 额定交流电压与额定直流电压之比 `sqrt(6) / pi`（默认）

该表显示了常见三相两电平逆变器控制模式的比值。默认值为 6/π。

对于 180° 和 120° 导通模式，列出的电压是线电压的基波 RMS 值。对于其他方法，列出的电压是线电压的最大基波 RMS 值。

您可以根据具体要求控制逆变器的输出电压。DPWM 包括 30° DPWM、60° DPWM 和 120° DPWM。有关详细信息，请参阅参考文献 [3] 和 [4]。

| **控制方法** | ***V RMS  (line-line)*** | ***V RMS (line-line)*** 与 ***v DC*** 之比 |
| --- | --- | --- |
| 180° 导通模式 [1] | 6πVDC | 0.7797 |
| 120° 导通模式 [1] | 32πVDC | 0.6752 |
| 滞环电流控制 [2] | (32)(2VDCπ) | 0.7797 |
| 正弦 PWM (SPMW) [2] | (32)(VDC2) | 0.6124 |
| 空间矢量调制 (SVM) [2] | (32)(VDC3) | 0.7071 |
| 不连续 PWM (DPWM) [3], [4] | (32)(VDC3) | 0.7071 |
| 转换为平均值整流器的原始交流电压 | (π2)(VDC3) | 0.7405 |

### **固定功率损耗** — 固定功率损耗 `1e3``W`（默认）

直流侧消耗的最小功率。默认值为 `1e3`。

### **导通直流电压** — 导通直流电压 `100``V`（默认）

当直流电源电压升至该值以上时，逆变器产生交流输出电压。

### **关断直流电压** — 关断直流电压 `75``V`（默认）

当直流电源电压降至该值以下时，逆变器关断，模块将输出交流电流设置为零。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

### R2021b：电气连接端口更新

从 R2021b 开始，要在复合端口和扩展端口之间切换，请将 **电气连接** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在较早版本中保存的模型内，请检查此模块的 **电气连接** 参数。

## 描述

带固定功率损耗的平均模型直流电压到三相交流电压转换器

Average-Value Inverter (Three-Phase) 模块对平均模型全波逆变器进行建模。它将直流电压转换为三相交流电压，并将三相交流功率需求转换为直流功率需求。相应的直流功率需求等于固定功率损耗与交流功率需求之和。

您只能将 Average-Value Inverter (Three-Phase) 模块用作全波逆变器。它表现为受直流电压控制的交流电压源。您指定的比值决定直流电压与交流电压之间的比值。

该图显示了逆变器作为全波逆变器的等效电路。但是，由于 Average-Value Inverter (Three-Phase) 模块执行平均模型功率转换，因此它不会产生通常与详细表示相关的谐波。

### 电气定义方程

电压由以下方程定义

vDC=vp−vn,

vref=vp+vn2,

vRMS=vratiovDC,

V0=23VRMS,

va=V0sin(2πft+φ)+vref,

vb=V0sin(2πft+φ−120∘)+vref,

和

vc=V0sin(2πft+φ+120∘)+vref,

其中：

- *vp* 和
  *vn* 是逆变器正极和负极端子处的电压。
- *vDC* 是逆变器正极和负极端子之间的电压差。
- *vref* 是直流偏移。
- *Vratio* 是逆变器的额定交流电压与额定直流电压之比。有关常见逆变器控制模式的 *Vratio* 值，请参阅参数中的 **额定交流电压与额定直流电压之比** 参数。
- *VRMS* 是 RMS 交流线电压。
- *V0* 是峰值相电压。
- *f* 是频率。
- *t* 是时间。
- *φ* 是相移。
- *va*、*vb*、*vc* 分别是交流相电压。

功率、电阻和电流由以下方程定义

PAC=−vaia−vbib−vcic,

RDC=vDC2PAC+Pfixed,

和

i=vDCRDC,

其中：

- *ia*、*ib* 和 *ic* 分别是流入逆变器的交流相电流。
- *PAC* 是交流侧的输出功率。*PAC* 的最小限制为 `0` W。
- *Pfixed* 是您在模块上指定的固定功率损耗。
- *RDC* 是直流侧的电阻。
- *i* 是从逆变器正极端子流向负极端子的电流。

当直流电源电压高于您为 **导通直流电压** 参数指定的值时，逆变器开始产生交流电压，即导通。当直流电源电压降至您为 **关断直流电压** 参数指定的值以下时，逆变器停止逆变，即关断。当逆变器关断时，模块将输出交流电流设置为零。
