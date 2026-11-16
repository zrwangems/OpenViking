---
type: simulink-block
title: 'Induction Machine Flux Observer'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Observers\u200b'
documentation_page: 'inductionmachinefluxobserver'
documentation_source_path: 'ref/inductionmachinefluxobserver.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Machine Flux Observer

## 端口

### 输入

### **iabc** — 电流矢量

在标幺制中测量的定子电流。

**数据类型：** `single` | `double`

### **wr** — 转速标量

测量的转速。

**数据类型：** `single` | `double`
### 输出

### **idqseF** — 电流矢量

同步参考坐标系中经过滤波的 *d* 轴和 *q* 轴定子电流。

**数据类型：** `single` | `double`

### **imr** — 电流标量

转子励磁电流。

**数据类型：** `single` | `double`

### **theta** — 电角度标量

转子电角度。

**数据类型：** `single` | `double`

### **we** — 同步转速标量

转子同步转速。

**数据类型：** `single` | `double`

## 参数

### **额定电气频率 (Hz)** — 频率 `60`（默认） | 正数

电机额定电气频率。

### **转子电阻，折算到定子侧 (pu)** — 电阻 `0.01`（默认） | 正数

折算到定子侧的转子电阻，采用标幺制。

### **转子漏电感，折算到定子侧 (pu)** — 电感 `0.06`（默认） | 正数

折算到定子侧的转子漏电感，采用标幺制。

### **励磁电感 (pu)** — 电感 `2.7`（默认） | 正数

采用标幺制的励磁电感。

### **dq 电流滤波器的时间常数 (s)** — 时间常数 `1e-4`（默认） | `0` 或正数

用于对 *d*-*q* 电流进行低通滤波的时间常数。

### **采样时间（-1 表示 inherited）** — 模块采样时间 `-1`（默认） | 正标量

连续模块执行之间的时间，单位为 s。在执行期间，模块产生输出，并在适当情况下更新其内部状态。有关更多信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

## 所属库

Simscape / Electrical / Control / Observers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

用于磁场定向控制的感应电机磁通观测器

Induction Machine Flux Observer 模块获取执行转子磁场定向控制 (FOC) 所需的同步转速 *ωe* 和电角度 *θe*。该图显示了观测器的等效电路。

### 方程

为了确定同步转速和电角度，Induction Machine Flux Observer 模块使用以下关系：

λdr'e=Lr'idr'e+LMidse≜LMimr,

0=Rr'idr'e−(ωe−ωr)λqr'e+dλdr'edt,

以及

iqr'e=−LMLr'iqse,

以这些组合形式表示：

idr'e=LMLr'(imr−idse)

dimrdt=Rr'Lr'(idse−imr)

以及

ωe=ωr+Rr'Lr'iqseimr

其中：

- λdr'e 是 *d* 轴转子磁通。
- imr 是励磁电流。
- idse 和 iqse 是 *d* 轴和 *q* 轴定子电流。
- idr'e 和 iqr'e 是 *d* 轴和 *q* 轴转子电流。
- ωe 是同步转速。
- ωr 是机械转速。
- Rr' 是折算到定子侧的转子电阻。
- Lr' 是折算到定子侧的转子漏电感。
- LM 是励磁电感。
