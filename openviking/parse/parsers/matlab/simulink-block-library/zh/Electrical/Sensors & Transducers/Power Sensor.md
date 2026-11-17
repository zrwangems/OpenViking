---
type: simulink-block
title: 'Power Sensor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'powersensor'
documentation_source_path: 'ref/powersensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Power Sensor

## 端口
```yaml
ports:
- name: P
  summary: 测得的功率物理信号
  direction: output
- name: S
  summary: 正电源供电轨电气
  direction: output
- name: +
  summary: 负载正极端子电气
  direction: output
- name: '-'
  summary: 负载负极端子电气
  direction: output
```

### 输出

### **P** — 测得的功率物理信号

输出测得功率的物理信号端口

### 守恒

### **S** — 正电源供电轨电气

连接到正电源供电轨的电气守恒端口

### **+** — 负载正极端子电气

连接到负载正极端子的电气守恒端口

### **-** — 负载负极端子电气

连接到负载负极端子的电气守恒端口
## 参数
```yaml
parameters:
- name: Measurement type
  summary: 测量类型 Instantaneous power（默认）| Instantaneous power
  group: ''
- name: Averaging period
  summary: 平均周期 1e-4 s（默认）
  group: ''
```

### **Measurement type** — 测量类型 `Instantaneous power`（默认）| `Instantaneous power`

选择您要测量 `Instantaneous power` 还是 `Average power over a specified period`。默认值为 `Instantaneous power`。

### **Averaging period** — 平均周期 `1e-4` `s`（默认）

用于测量平均功率的固定时间段。

#### 依赖关系

仅当为 **Measurement type** 参数选择 `Average power over a specified period` 时，此参数才可见。
## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

## 描述

理想的瞬时或周期平均功率测量

Power Sensor 模块在假设只有负载连接到 + 端子的情况下，计算连接在 + 和 - 端子之间的负载所消耗的功率。有关内部电流和电压传感器的布置，请参阅模块图标。

该传感器可以返回瞬时功率，或在固定时间段内平均的功率。对于周期性电流和电压波形（例如与 PWM 控制相关的波形），请使用后一种选项。

下图显示了如何连接该模块以测量电阻器中耗散的功率。

有关使用数据记录查看组件功率的替代工作流程，请参阅 Buck Converter 示例。
