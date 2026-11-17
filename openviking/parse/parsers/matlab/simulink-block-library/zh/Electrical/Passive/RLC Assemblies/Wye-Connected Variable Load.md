---
type: simulink-block
title: 'Wye-Connected Variable Load'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / RLC Assemblies'
documentation_page: 'wyeconnectedvariableload'
documentation_source_path: 'ref/wyeconnectedvariableload.html'
language: zh-CN
chinese_source: worker-translation
---

# Wye-Connected Variable Load

## 端口
```yaml
ports:
- name: P
  summary: 有功功率物理信号
  direction: input
- name: '~'
  summary: 三相端口电气
  direction: input
- name: n
  summary: 中性相电气
  direction: input
```

### 输入

### **P** — 有功功率物理信号

与有功功率关联的物理信号输入端口。
### 守恒

### **~** — 三相端口电气

可扩展三相
端口。

### **n** — 中性相电气

与中性相关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否对复合或扩展三相端口建模 Composite three-phase ports（默认）| Expanded three-phase ports
  group: ''
- name: Rated voltage
  summary: 额定线电压 24e3 V（默认）
  group: ''
- name: Minimum real power
  summary: 最小有功功率 1e3 W（默认）| 正标量
  group: ''
```

### **Modeling option** — 是否对复合或扩展三相端口建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是否对复合或扩展三相端口建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建对应于三相电气系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各个相。

### **Rated voltage** — 额定线电压 `24e3` `V`（默认）

用于电阻方程的 RMS 额定线电压。

### **Minimum real power** — 最小有功功率 `1e3` `W`（默认）| 正标量

三相负载在额定电压供电时消耗的最小有功功率。该值必须大于 0。
## 所属库

Simscape / Electrical / Passive / RLC Assemblies

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

## 描述

以星形配置接线的三相可变负载

Wye-Connected Variable Load 模块对以星形配置接线的三相可变负载进行建模。负载的每一支路包含一个电阻。该模块计算在您指定的额定电压下消耗物理信号输入 P 的有功功率所需的电阻。因此，该模块可以表示实际负载。

为确保电阻始终大于零，您需要指定负载消耗的最小有功功率。最小有功功率必须大于零。

### 方程

电阻定义为

R=VRated2P，

其中：

- *R* 是每相串联电阻。
- *VRated* 是 RMS 额定线电压。
- *P* 是所需的三相有功功率。
