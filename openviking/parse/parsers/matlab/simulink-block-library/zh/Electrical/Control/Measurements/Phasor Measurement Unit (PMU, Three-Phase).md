---
type: simulink-block
title: 'Phasor Measurement Unit (PMU, Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Measurements'
documentation_page: 'phasormeasurementunitpmuthreephase'
documentation_source_path: 'ref/phasormeasurementunitpmuthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Phasor Measurement Unit (PMU, Three-Phase)

## 端口
```yaml
ports:
- name: abc
  summary: 三相信号向量
  direction: input
  data_types: single | double
- name: freq
  summary: 正序分量频率标量
  direction: output
  data_types: single | double
- name: angle
  summary: 正序分量相角标量
  direction: output
  data_types: single | double
- name: mag
  summary: 正序分量幅值标量
  direction: output
  data_types: single | double
```

### 输入

### **abc** — 三相信号向量

三相输入信号，指定为向量。

**数据类型：** `single` | `double`
### 输出

### **freq** — 正序分量频率标量

测得正序分量的频率，以 Hz 为单位，以标量形式返回。

**数据类型：** `single` | `double`

### **angle** — 正序分量相角标量

测得正序分量的相角，以度为单位，以标量形式返回。

**数据类型：** `single` | `double`

### **mag** — 正序分量幅值标量

测得正序分量的幅值，以标量形式返回。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Rated frequency (Hz)
  summary: 额定频率 60（默认）| 50
  group: ''
- name: Sampling points per cycle
  summary: 每周期采样点数 64（默认）| 24 | 48
  group: ''
- name: Reporting rate factor
  summary: 报告速率因子 1（默认）| 标量
  group: ''
```

### **Rated frequency (Hz)** — 额定频率 `60`（默认）| `50`

输入信号的额定频率，以 Hz 为单位。

### **Sampling points per cycle** — 每周期采样点数 `64`（默认）| `24` | `48`

每周期采样点数。

### **Reporting rate factor** — 报告速率因子 `1`（默认）| 标量

模块的报告速率与采样速率之比。
## 所属库

Simscape / Electrical / Control / Measurements

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020a 中引入**

## 描述

三相系统的频率、相位和幅值测量

Phasor Measurement Unit (PMU, Three-Phase) 模块以特定采样率测量三相系统中输入电气信号正序分量的频率、相位和幅值。

该模块使用系统时钟作为同步参考。在现实世界中，此信息通常从 GPS 采集。
