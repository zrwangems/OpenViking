---
type: simulink-block
title: 'Passive Harmonic Filter (Three-Phase)'
family: 'sps'
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

### **Modeling option** — 对复合或扩展三相端口建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

对复合或扩展三相端口建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建与三相电气系统单线图对应的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

### **Rated reactive power** — 无功功率 `100e6` `V*A`（默认）

额定频率和电压下的无功功率，单位为 V\*A。

### **Rated voltage (phase-to-phase RMS)** — 相间 RMS 电压 `4160` `V`（默认）

额定相间均方根（RMS）电压，单位为 V。

### **Rated frequency** — 额定频率 `60` `Hz`（默认）

基波频率，单位为 Hz。

### **Quality factor** — 品质因数 `10`（默认）

调谐频率锐度的指标。

### **Filter type** — 滤波器模型 `Band-pass filter, single-tuned`（默认）| `Band-pass filter, double-tuned` | `High-pass filter, second-order` | `High-pass filter, C-type`

谐波滤波器的类型。

#### 依赖关系

如果您为 **Filter type** 参数选择 `Band-pass filter, single-tuned`、`High-pass filter, second-order` 或 `High-pass filter, C-type`，则 **Tuned frequency** 参数可见。

如果您为 **Filter type** 参数选择 `Band-pass filter, double-tuned`，则 **Tuned frequency 1** 和 **Tuned frequency 2** 参数可见。

### **Filter connection** — 连接类型 `Wye with floating neutral`（默认）| `Wye with neutral port` | `Wye with grounded neutral` | `Delta`

连接类型

### **Tuned frequency** — 调谐频率 `5 * 60` `Hz`（默认）

滤波器的调谐频率，单位为 Hz。

#### 依赖关系

仅当您为 **Filter type** 参数选择 `Band-pass filter, single-tuned`、`High-pass filter, second-order` 或 `High-pass filter, C-type` 时，此参数才可见。

### **Tuned frequency 1** — 第一调谐频率 `7 * 60` `Hz`（默认）

第一调谐频率，单位为 Hz。

#### 依赖关系

仅当您为 **Filter type** 参数选择 `Band-pass filter, double-tuned` 时，此参数才可见。

### **Tuned frequency 2** — 第二调谐频率 `11 * 60` `Hz`（默认）

第二调谐频率，单位为 Hz。

#### 依赖关系

仅当您为 **Filter type** 参数选择 `Band-pass filter, double-tuned` 时，此参数才可见。

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

Passive Harmonic Filter (Three-Phase) 模块通过为谐波提供低阻抗路径来抑制系统谐波电流并降低电压畸变。在额定频率下，无源并联滤波器呈容性并提供无功功率，从而可以改善电气功率因数。

该模块的四种模型分别对应 **Filter type** 参数的一个选项：

- Band-Pass Filter, Single Tuned
- Band-Pass Filter, Double Tuned
- High-Pass Filter, Second-Order
- High-Pass Filter, C-type

### Band-Pass Filter, Single Tuned

在调谐频率下，发生 LC 谐振，滤波器阻抗达到最小值，该值等于电阻值。

滤波器调谐频率由以下方程定义：

f1=nf0=12πLC，

其中 *f1* 和 *f0* 分别为调谐频率和基波频率，*n* 为调谐频率的谐波次数，*L* 为电感，*C* 为电容。

品质因数定义为调谐频率下的感性或容性电抗与电阻之比，如下式所述：

Qf=XLNR=XCNR，

其中：

- R 是电阻。
- `XLN` 是调谐频率下电感器的阻抗 XLN=2πf1L。
- `XCN` 是调谐频率下电容器的阻抗 XCN=12πf1C。

较高的品质因数值会产生更尖锐的频率。然而，由于电阻相对较低，这会在基频下产生高功率耗散。

额定无功功率由下式给出：

Qr=V2XC0−XL0=V2XC0−XC0n2=V2XC0n2n2−1

其中 *Qr* 是单相额定无功功率，*V* 是均方根支路电压。

### Band-Pass Filter, Double Tuned

双调谐滤波器有两个调谐频率 *f1* 和 *f2*，其中 f1=n1f0 且 f2=n2f0。

双调谐滤波器包括一个串联 LC 和一个并联 RCL 电路，各自调谐在频率 *fs* 和 *fp*，接近 *f1* 和 *f2* 的几何平均频率，由以下方程表示：

fm=f1f2=fsfp，

其中

fs=12πLC

fp=12πL2C2。

该滤波器的品质因数定义为并联 `R` 和 `L` 元件在几何平均频率 *fm* 处的品质因数：

Qf=R2πfmL2。

### High-Pass Filter, Second-Order

二阶高通滤波器会分流调谐频率及以上的大部分谐波。该滤波器设计为对高次谐波具有平坦阻抗。

调谐频率由以下方程描述：

f1=nf0=12πLC。

品质因数是带通单调谐滤波器的倒数：

Qf=RXLN=RXCN。

额定无功功率与带通单调谐滤波器相同：

Qr=V2XC0−XL0=V2XC0−XC0n2=V2XC0n2n2−1

### High-Pass Filter, C-type

与单调谐版本相比，C 型高通滤波器在基波频率下具有更低的损耗，因为电容器和电感器与电阻器并联。

为防止基波电流通过电阻器，*L2* 和 *C2* 的谐振频率调谐到基波频率：

f0=12πL2C2。

品质因数使用以下方程计算：

Qf=R2πf0nL2。

### RCL 滤波器元件值

|  | Single-Tuned | Double-Tuned | Second-Order, High-Pass | C-type, High-Pass |
| --- | --- | --- | --- | --- |
| R | 12πf0CQf | 2πfmL2Qf | 2πnf0LQf | Qf(2π n f0 L2) |
| L | 1C(2πnf0)2 | V2Qrπf0(n12+n22−2) | 1C(2πnf0)2 | None |
| C | Qr2πf0V2⋅n2−1n2 | Qr4πf0V2(n12−1n12+n22−1n22) | Qr2πf0V2⋅n2−1n2 | Qr2πf0V2 |
| L2 | None | (1−f12fs2)(1−f12fp2)C(2πf12)其中  fs=12πLC, fp=f1f2fs | None | 1C2(2πnf0)2 |
| C2 | None | 1L2(2πfp)2 | None | C(n2−1) |
