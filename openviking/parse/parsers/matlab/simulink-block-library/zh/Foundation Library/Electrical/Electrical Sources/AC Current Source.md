---
type: simulink-block
title: 'AC Current Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'accurrentsource'
documentation_source_path: 'ref/accurrentsource.html'
language: zh-CN
chinese_source: worker-translation
---

# AC Current Source

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与源正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与源负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Peak amplitude
  summary: 峰值电流幅值 1 A（默认）| 标量
  group: ''
- name: Phase shift
  summary: 以角度单位表示的相移 0 deg（默认）| 标量
  group: ''
- name: Frequency
  summary: 电流频率 60 Hz（默认）| 正标量
  group: ''
```

### **Peak amplitude** — 峰值电流幅值 `1 A`（默认）| 标量

峰值电流幅值。

### **Phase shift** — 以角度单位表示的相移 `0 deg`（默认）| 标量

以角度单位表示的相移。

### **Frequency** — 电流频率 `60 Hz`（默认）| 正标量

电流频率，以 Hz 或可直接转换为 Hz 的单位指定（其中 Hz 定义为 1/s）。例如，kHz 和 MHz 是有效单位，但 rad/s 不是。
## 所属库

Simscape / Foundation Library / Electrical / Electrical Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

理想正弦电流源

AC Current Source 模块表示一个理想电流源，它维持通过自身的正弦电流，与端子两端的电压无关。

输出电流由以下方程定义：

I=I0⋅sin(2π⋅f⋅t+φ)

其中：

- *I* 是电流。
- *I*0 是峰值幅值。
- *f* 是频率。
- *φ* 是相移。
- *t* 是时间。

电流的正方向由箭头指示。
