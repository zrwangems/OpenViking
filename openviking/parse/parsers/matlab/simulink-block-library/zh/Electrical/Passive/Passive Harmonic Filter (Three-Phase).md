---
type: simulink-block
title: 'Passive Harmonic Filter (Three-Phase)'
family: 'passive'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'passiveharmonicfilterthreephase'
documentation_source_path: 'ref/passiveharmonicfilterthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Passive Harmonic Filter (Three-Phase)

## 端口

### 守恒

### **~** — 三相电压电气

与电压关联的可扩展三相端口。

## 参数

### **建模选项** — 是建模复合三相端口还是扩展三相端口 `Composite three-phase ports` （默认） | `Expanded three-phase ports`

是建模复合三相端口还是扩展三相端口。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建与三相电气系统单线图对应的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

### **额定无功功率** — 无功功率 `100e6` `V*A` （默认）

额定频率和电压下的无功功率，单位为 V\*A。

### **额定电压（相间 RMS）** — 相间 RMS 电压 `4160` `V` （默认）

额定相间均方根 (RMS) 电压，单位为 V。

### **额定频率** — 额定频率 `60` `Hz` （默认）

基波频率，单位为 Hz。

### **品质因数** — 品质因数 `10` （默认）

调谐频率尖锐程度的指标。

### **滤波器类型** — 滤波器模型 `Band-pass filter, single-tuned` （默认） | `Band-pass filter, double-tuned` | `High-pass filter, second-order` | `High-pass filter, C-type`

谐波滤波器的类型。

#### 依赖关系

如果您为 **滤波器类型** 参数选择 `Band-pass filter, single-tuned`、`High-pass filter, second-order` 或 `High-pass filter, C-type`，则 **调谐频率** 参数可见。

如果您为 **滤波器类型** 参数选择 `Band-pass filter, double-tuned`，则 **调谐频率 1** 和 **调谐频率 2** 参数可见。

### **滤波器连接** — 连接类型 `Wye with floating neutral` （默认） | `Wye with neutral port` | `Wye with grounded neutral` | `Delta`

连接类型

### **调谐频率** — 调谐频率 `5 * 60` `Hz` （默认）

滤波器的调谐频率，单位为 Hz。

#### 依赖关系

仅当您为 **滤波器类型** 参数选择 `Band-pass filter, single-tuned`、`High-pass filter, second-order` 或 `High-pass filter, C-type` 时，此参数才可见。

### **调谐频率 1** — 第一调谐频率 `7 * 60` `Hz` （默认）

第一调谐频率，单位为 Hz。

#### 依赖关系

仅当您为 **滤波器类型** 参数选择 `Band-pass filter, double-tuned` 时，此参数才可见。

### **调谐频率 2** — 第二调谐频率 `11 * 60` `Hz` （默认）

第二调谐频率，单位为 Hz。

#### 依赖关系

仅当您为 **滤波器类型** 参数选择 `Band-pass filter, double-tuned` 时，此参数才可见。

## 所属库

Simscape / Electrical / Passive

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

谐波电流滤波器

Passive Harmonic Filter (Three-Phase) 模块通过为谐波提供低阻抗路径来抑制系统谐波电流并降低电压畸变。在额定频率下，无源并联滤波器呈容性并提供无功功率，从而可提高电气功率因数。

该模块的四种模型分别对应 **滤波器类型** 参数的一个选项：

- 单调谐带通滤波器
- 双调谐带通滤波器
- 二阶高通滤波器
- C 型高通滤波器

### 单调谐带通滤波器

在调谐频率下，发生 LC 谐振，滤波器阻抗达到最小值，该值等于电阻值。

滤波器调谐频率由以下方程定义：

f1=nf0=12πLC,

其中 *f1* 和 *f0* 是调谐频率和基波频率，*n* 是调谐频率的谐波次数，*L* 是电感，*C* 是电容。

品质因数定义为调谐频率下的感性或容性电抗与电阻之比，如下式所述：

Qf=XLNR=XCNR,

其中：

- R 是电阻。
- `XLN` 是电感在调谐频率下的阻抗 XLN=2πf1L。
- `XCN` 是电容在调谐频率下的阻抗 XCN=12πf1C。

较高的品质因数值会产生更尖锐的频率。然而，由于电阻相对较低，这会在基频处产生高功率耗散。

额定无功功率由下式给出：

Qr=V2XC0−XL0=V2XC0−XC0n2=V2XC0n2n2−1

其中 *Qr* 是单相额定无功功率，*V* 是支路电压的均方根。

### 双调谐带通滤波器

双调谐滤波器具有两个调谐频率 *f1* 和 *f2*，其中 f1=n1f0 且 f2=n2f0。

双调谐滤波器由串联 LC 和并联 RCL 电路组成，分别调谐在频率 *fs* 和 *fp*，接近 *f1* 和 *f2* 的几何平均频率，由以下方程表示：

fm=f1f2=fsfp,

其中

fs=12πLC

fp=12πL2C2.

该滤波器的品质因数定义为并联 `R` 和 `L` 元件在几何平均频率 *fm* 处的品质因数：

Qf=R2πfmL2.

### 二阶高通滤波器

二阶高通滤波器在调谐频率及高于调谐频率处分流大部分谐波。该滤波器设计为对高次谐波具有平坦阻抗。

调谐频率由以下方程描述：

f1=nf0=12πLC.

品质因数是单调谐带通滤波器的倒数：

Qf=RXLN=RXCN.

额定无功功率与单调谐带通滤波器相同：

Qr=V2XC0−XL0=V2XC0−XC0n2=V2XC0n2n2−1

### C 型高通滤波器

与单调谐版本相比，C 型高通滤波器在基波频率处具有更低的损耗，因为电容和电感与电阻器并联。

为防止基波电流通过电阻器，*L2* 和 *C2* 的谐振频率调谐到基波频率：

f0=12πL2C2.

品质因数使用以下方程计算：

Qf=R2πf0nL2.

### RCL 滤波器元件的值

|  | 单调谐 | 双调谐 | 二阶高通 | C 型高通 |
| --- | --- | --- | --- | --- |
| R | 12πf0CQf | 2πfmL2Qf | 2πnf0LQf | Qf(2π n f0 L2) |
| L | 1C(2πnf0)2 | V2Qrπf0(n12+n22−2) | 1C(2πnf0)2 | 无 |
| C | Qr2πf0V2⋅n2−1n2 | Qr4πf0V2(n12−1n12+n22−1n22) | Qr2πf0V2⋅n2−1n2 | Qr2πf0V2 |
| L2 | 无 | (1−f12fs2)(1−f12fp2)C(2πf12)其中 fs=12πLC, fp=f1f2fs | 无 | 1C2(2πnf0)2 |
| C2 | 无 | 1L2(2πfp)2 | 无 | C(n2−1) |
