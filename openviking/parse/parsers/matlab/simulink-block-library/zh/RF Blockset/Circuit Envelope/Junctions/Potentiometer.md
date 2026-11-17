---
type: simulink-block
title: 'Potentiometer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Junctions'
documentation_page: 'potentiometer'
documentation_source_path: 'ref/potentiometer.html'
language: zh-CN
chinese_source: worker-translation
---

# Potentiometer

## 端口
```yaml
ports: []
```

R2025b 中未记录。
## 参数
```yaml
parameters:
- name: Minimum resistance
  summary: 电位器的最小输入电阻 10 Ohm（默认值）| 正标量
  group: ''
- name: Maximum resistance
  summary: 电位器的最大输入电阻 1e6 Ohm（默认值）| 正标量
  group: ''
- name: Potentiometer type
  summary: 电位器的曲线类型 Linear（默认值）| Logarithmic | Antilog
  group: ''
- name: Percentage of resistance at half wiper
  summary: 电位器的最大输入电阻 正标量
  group: ''
```

### **Minimum resistance** — 电位器的最小输入电阻 `10 Ohm`（默认值）| 正标量

电位器的最小输入电阻，指定为以欧姆为单位的正标量。

**数据类型：** `double`

### **Maximum resistance** — 电位器的最大输入电阻 `1e6 Ohm`（默认值）| 正标量

电位器的最大输入电阻，指定为以欧姆为单位的正标量。此值必须大于最小电阻。

**数据类型：** `double`

### **Potentiometer type** — 电位器的曲线类型 `Linear`（默认值）| `Logarithmic` | `Antilog`

电位器的曲线类型，指定为
`Linear`、
`Logarithmic`、
`Antilog`。

**数据类型：** `char`

### **Percentage of resistance at half wiper** — 电位器的最大输入电阻 正标量

对数型和反对数型电位器在半滑动端处的电阻百分比，指定为正标量。有效值取决于电位器类型：

- `Logarithmic` - 大于 0 且
  小于 50。默认值为 20。
- `Antilog` - 大于 50 且
  小于 100。默认值为 80。

#### 依赖关系

要启用此参数，请在 **Potentiometer
type** 中选择
`Logarithmic` 或
`Antilog`。

**数据类型：** `double`
## 所属库

RF Blockset / Circuit Envelope / Junctions

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015b 中引入**

## 描述

Simulink 控制的电位器

Potentiometer 模块对可变电阻器进行建模。Potentiometer 模块使用 Simulink® 信号作为输入控制信号，以改变正负端子之间的电阻。

当控制信号在 0 到 1 之间变化时，电位器电压–电流关系的方程为：

Linear:            Vpot=Ipot.(Roff.Ctl+Ron.(1−Ctl))Logarithmic:   Vpot=Ipot.(C1.exp (C2.Ctl)+C3)Antilog:           Vpot=Ipot.(C1.log  (1+C2.Ctl)+C3.Ctl+Ron)

- Linear、Logarithmic、Antilog — 电位器的电气特性。
- `Ctl` — Simulink 信号
- `Ron` — 电位器的最小电阻
- `Roff` — 电位器的最大电阻
