---
type: simulink-block
title: 'Current Source (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'currentsourcethreephase'
documentation_source_path: 'ref/currentsourcethreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Current Source (Three-Phase)

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
- name: Current (phase RMS)
  summary: 相电流 RMS 值 100 / sqrt(2) A（默认）
  group: ''
- name: Phase shift
  summary: 相移 0 deg（默认）
  group: ''
- name: Frequency
  summary: 电流频率 60 Hz（默认）
  group: ''
```

### **Modeling option** — 是否对复合或扩展三相端口建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是否对复合或扩展三相端口建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

### **Current (phase RMS)** — 相电流 RMS 值 `100 / sqrt(2)` `A`（默认）

相电流 RMS 值。

### **Phase shift** — 相移 `0` `deg`（默认）

相移，以角度单位表示。

### **Frequency** — 电流频率 `60` `Hz`（默认）

电流频率，以 Hz 或可直接转换为 Hz 的单位指定（其中 Hz 定义为 1/s）。例如，`kHz` 和 `MHz` 是有效单位，但 `rad/s` 不是。
## 所属库

Simscape / Electrical / Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

理想三相电流源

Current Source (Three-Phase) 模块对理想三相电流源进行建模，该电流源在其端子之间维持指定幅值的正弦电流，与电源两端的电压无关。

输出电流由以下方程定义：

I0=2iphase\_rms

ia=I0sin(2πft+φ)

ib=I0sin(2πft+φ−120∘)

ic=I0sin(2πft+φ+120∘),

其中：

- *I0* 是峰值相电流。
- *iphase\_rms* 是 RMS 相电流。
- *ia*、*ib*、*ic* 是各自的相电流。
- *f* 是频率。
- *φ* 是相移。
- *t* 是时间。

箭头指示电流流动的正方向。该电源采用星形配置，端口 **n** 提供与星形中性点的连接。
