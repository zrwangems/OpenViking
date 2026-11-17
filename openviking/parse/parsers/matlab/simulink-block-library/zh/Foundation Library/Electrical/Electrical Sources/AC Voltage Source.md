---
type: simulink-block
title: 'AC Voltage Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sources'
documentation_page: 'acvoltagesource'
documentation_source_path: 'ref/acvoltagesource.html'
language: zh-CN
chinese_source: worker-translation
---

# AC Voltage Source

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

与电源正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与电源负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Peak amplitude
  summary: 峰值电压幅值 1 V（默认）| 标量
  group: ''
- name: Phase shift
  summary: 以角度单位表示的相移 0 deg（默认）| 标量
  group: ''
- name: Frequency
  summary: 电压频率 60 Hz（默认）| 正标量
  group: ''
```

### **Peak amplitude** — 峰值电压幅值 `1 V`（默认）| 标量

峰值电压幅值。

### **Phase shift** — 以角度单位表示的相移 `0 deg`（默认）| 标量

以角度单位表示的相移。

### **Frequency** — 电压频率 `60 Hz`（默认）| 正标量

电压频率，以 Hz 或可直接转换为 Hz 的单位指定（其中 Hz 定义为 1/s）。例如，kHz 和 MHz 是有效单位，但 rad/s 不是。
## 所属库

Simscape / Foundation Library / Electrical / Electrical Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

理想恒定电压源

AC Voltage Source 模块表示一个理想电压源，它在其输出端子上维持正弦电压，与流过该电源的电流无关。

输出电压由以下方程定义：

V=V0⋅sin(2π⋅f⋅t+φ)

其中：

- *V* 是电压。
- *V*0 是峰值幅值。
- *f* 是频率。
- *φ* 是相移。
- *t* 是时间。

连接 **+** 和 **-** 是对应于电压源正极和负极端子的守恒电气端口。如果电流从正极流向负极，则电流为正，并且电源两端的电压等于正极端子与负极端子电压之差，*V*(+) – *V*(-)。
