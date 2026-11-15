---
type: simulink-block
title: 'Sequence Analyzer'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'sequenceanalyzer'
documentation_source_path: 'ref/sequenceanalyzer.html'
language: zh-CN
chinese_source: worker-translation
---

# Sequence Analyzer

## 端口

### 输入

### **u** — 周期输入信号 vector

周期输入信号，指定为包含三个元素的 vector。

### 输出

### **mag** — 幅值 scalar | vector

正序、负序或零序的幅值。根据谐波次数，此输出为 scalar 或 vector。

### **angle** — 相移 scalar | vector

正序、负序或零序的相移，以 degrees 为单位。根据谐波次数，此输出为 scalar 或 vector。

## 参数

### **Base frequency (Hz)** — 基频 `60`（默认）

输入信号的基频，以 Hz 为单位。

### **Harmonic numbers** — 谐波次数 `[1 2]`（默认） | scalar or vector

谐波次数的 scalar 或 vector。`1` 表示基频，`2` 是二次谐波。

### **Sequence** — 序列选择 `Positive`（默认） | `Negative` | `Zero`

选择序列的幅值和相位是正序、负序还是零序。

### **Sample Time (s)** — 模块采样时间 `0`（默认）

连续模块执行之间的时间。执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

对于继承的离散时间操作，指定 `-1`。对于离散时间操作，指定 positive integer。对于连续时间操作，指定 `0`。

如果此模块位于封装子系统中，或其他允许您在连续操作和离散操作之间切换的变体子系统中，请提升采样时间参数。提升采样时间参数可确保在模块的连续实现和离散实现之间正确切换。有关详细信息，请参阅 Promote Block Parameters on a Mask。

## 所属库

Simscape / Electrical / Control / Measurements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

计算三相信号正序、负序或零序的幅值和相位

Sequence Analyzer 模块将三相信号（通常为电压）作为输入，并输出正序、负序或零序的幅值和相位。

输入信号首先基于模块封装中指定的基频和谐波转换为相量表示。然后，模块将相量转换为序分量。

您可以用相量表示中的 *V0*、*V1*、*V2* 表示零序、正序和负序分量；*Va*、*Vb*、*Vc* 是三相电压。序分量计算如下：

[V0V1V2]=13[1111aa21a2a2][VaVbVc]

其中 a=ej23π。
