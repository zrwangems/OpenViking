---
type: simulink-block
title: 'Circuit Breaker (with arc)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Switches & Breakers'
documentation_page: 'circuitbreakerwitharc'
documentation_source_path: 'ref/circuitbreakerwitharc.html'
language: zh-CN
chinese_source: worker-translation
---

# Circuit Breaker (with arc)

## 端口
```yaml
ports:
- name: vT
  summary: 标量控制端口物理信号
  direction: input
- name: '1'
  summary: 端口 1 电气
  direction: input
- name: '2'
  summary: 端口 2 电气
  direction: input
- name: +
  summary: 正端口电气
  direction: input
- name: '-'
  summary: 负端口电气
  direction: input
```

### 输入

### **vT** — 标量控制端口物理信号

标量物理信号控制端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`PS control port`。
### 守恒

### **1** — 端口 1 电气

电气守恒端口。

### **2** — 端口 2 电气

电气守恒端口。

### **+** — 正端口电气

正电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Electrical control port`。

### **-** — 负端口电气

负电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Electrical control port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 指定物理控制端口还是电气控制端口 PS control port（默认）| Electrical control port
  group: ''
- name: Arc time constant, tau
  summary: 电弧时间常数 0.3e-6 s（默认）
  group: ''
- name: Cooling power, P
  summary: 冷却功率 30900 W（默认）
  group: ''
- name: Initial arc conductance, g0
  summary: 初始电弧电导 1e4 s（默认）
  group: ''
- name: Threshold
  summary: 阈值电压 0.5 V（默认）
  group: ''
```

### **Modeling option** — 指定物理控制端口还是电气控制端口 `PS control port`（默认）| `Electrical control port`

指定开关门控使用物理控制端口还是电气控制端口。

### **Arc time constant, tau** — 电弧时间常数 `0.3e-6` `s`（默认）

Mayr 电弧的时间常数。

### **Cooling power, P** — 冷却功率 `30900` `W`（默认）

冷却功率。

### **Initial arc conductance, g0** — 初始电弧电导 `1e4` `s`（默认）

断路器闭合时端口 **1** 和
**2** 之间的电导。

### **Threshold** — 阈值电压 `0.5` `V`（默认）

控制端口 *vT* 的阈值电压。该模块使用阈值电压和仿真开始时 *vT* 的值来确定断路器初始是断开还是闭合。当电压升至阈值以上时，断路器断开。
当控制端口电压降至阈值以下时，断路器闭合。
## 所属库

Simscape / Electrical / Switches & Breakers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

具有 Mayr 电弧表示的单极单掷断路器

Circuit Breaker (with arc) 模块表示一个具有 Mayr 电弧表示的单相断路器，由外部
控制信号 *vT* 控制。如果 *vT* 小于
阈值，则断路器闭合。如果 *vT* 大于或等于
阈值，则断路器在电流中断期间以电弧方式断开。外部信号可以反复断开和闭合断路器。

下表显示了外部信号 *vT* 如何控制模块
行为。

| 条件 | 模块行为 |
| --- | --- |
| *vT* < **Threshold** | 断路器闭合。端口 **1** 连接到端口 **2**。 |
| *vT* ≥ **Threshold** | 断路器正在断开或已断开。端口 **1** 通过非线性电导连接到端口 **2**。 |

Circuit Breaker (with arc) 模块比 Circuit Breaker 模块具有更高的
计算开销。如果电弧电流或电压表示的保真度是您的首要要求，请使用 Circuit
Breaker (with arc) 模块并使用全局 Simulink® 可变步长求解器。否则，请使用 Circuit
Breaker 模块。

### Mayr 电弧模型方程

断路器的定义方程为

x=ln(g)

和

i=gv，

其中：

- *g* 是电弧电导。
- *x* 是内部状态变量。
- *v* 是断路器两端的电压。
- *i* 是流过断路器的电流。

当断路器闭合时，

dxdt=0。

当断路器正在断开或已断开时，

dxdt=1τ(gv2P−1)，

其中：

- *τ* 是电弧时间常数。
- *P* 是冷却功率。
