---
type: simulink-block
title: 'Current Source (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sources'
documentation_page: 'currentsourcethreephase'
documentation_source_path: 'ref/currentsourcethreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Current Source (Three-Phase)

## 端口

### 守恒端口

### **~** — 三相端口电气

可扩展三相端口，与三相 *a*、*b* 和 *c* 相关联。

### **n** — 星形中心电气

与星形中心相关联的电气守恒端口。

## 参数

### **建模选项** — 是否对复合三相端口或扩展三相端口进行建模 `Composite three-phase ports` (default) | `Expanded three-phase ports`

是否对复合三相端口或扩展三相端口进行建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建与三相电气系统单线图对应的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

### **电流（相 RMS）** — RMS 相电流 `100 / sqrt(2)` `A` (default)

RMS 相电流。

### **相移** — 相移 `0` `deg` (default)

相移，以角度单位表示。

### **频率** — 电流频率 `60` `Hz` (default)

电流频率，以 Hz 或可直接转换为 Hz 的单位指定（其中 Hz 定义为 1/s）。例如，`kHz` 和 `MHz` 是有效单位，但 `rad/s` 不是。

## 所属库

Simscape / Electrical / Sources

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

理想三相电流源

Current Source (Three-Phase) 模块对理想三相电流源进行建模，该电流源在其端子处维持指定幅值的正弦电流，与源两端的电压无关。

输出电流由以下方程定义：

I0=2iphase\_rms

ia=I0sin(2πft+φ)

ib=I0sin(2πft+φ−120∘)

ic=I0sin(2πft+φ+120∘),

其中：

- *I0* 是峰值相电流。
- *iphase\_rms* 是 RMS 相电流。
- *ia*、*ib*、*ic* 分别是各相电流。
- *f* 是频率。
- *φ* 是相移。
- *t* 是时间。

箭头指示电流流动的正方向。该源采用星形配置，端口 **n** 提供与星形中心的连接。
