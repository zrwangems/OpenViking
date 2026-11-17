---
type: simulink-block
title: 'Timer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'timer'
documentation_source_path: 'ref/timer.html'
language: zh-CN
chinese_source: worker-translation
---

# Timer

## 端口
```yaml
ports:
- name: THRES
  summary: 阈值引脚电气端口
  direction: conserving
- name: TRIG
  summary: 触发引脚电气端口
  direction: conserving
- name: CONT
  summary: 控制引脚电气端口
  direction: conserving
- name: RESET
  summary: 复位引脚电气端口
  direction: conserving
- name: OUT
  summary: 输出引脚电气端口
  direction: conserving
- name: DISCH
  summary: 放电引脚电气端口
  direction: conserving
```

### 守恒端口

### **THRES** — 阈值引脚电气端口

与定时器阈值引脚关联的电气守恒端口

### **TRIG** — 触发引脚电气端口

与定时器触发引脚关联的电气守恒端口

### **CONT** — 控制引脚电气端口

与定时器控制引脚关联的电气守恒端口

### **RESET** — 复位引脚电气端口

与定时器复位引脚关联的电气守恒端口

### **OUT** — 输出引脚电气端口

与定时器输出引脚关联的电气守恒端口

### **DISCH** — 放电引脚电气端口

与定时器放电引脚关联的电气守恒端口
## 参数
```yaml
parameters:
- name: Power supply voltage
  summary: 电源电压 15 V（默认值）
  group: 电源
- name: Low level output voltage
  summary: 低电平输出电压 0 V（默认值）
  group: 输出
- name: High level output voltage
  summary: 高电平输出电压 14.1 V（默认值）
  group: 输出
- name: Output resistance
  summary: 输出电阻 8 Ohm（默认值）
  group: 输出
- name: Propagation delay
  summary: 传播延迟 100e-9 s（默认值）
  group: 输出
- name: Discharge switch on-resistance
  summary: 放电开关导通电阻 12 Ohm（默认值）
  group: 放电
- name: Discharge switch off-resistance
  summary: 放电开关关断电阻 500e6 Ohm（默认值）
  group: 放电
- name: Potential divider component resistance
  summary: 分压器组件电阻 5 kOhm（默认值）
  group: 分压器
```

### 电源

### **Power supply voltage** — 电源电压 `15` `V`（默认值）

模块在内部施加到定时器组件的电压值 Vcc。

### 输出

### **Low level output voltage** — 低电平输出电压 `0` `V`（默认值）

当定时器输出为低电平且未抽取输出电流时的输出电压。

### **High level output voltage** — 高电平输出电压 `14.1` `V`（默认值）

当定时器输出为高电平且未抽取电流时的输出电压 VOH。

### **Output resistance** — 输出电阻 `8` `Ohm`（默认值）

输出电压降与输出电流之比。将此参数设置为 (VOH−VOH1)/IOH1，其中 VOH1 是输出电流为 IOH1 时降低后的输出高电压。

### **Propagation delay** — 传播延迟 `100e-9` `s`（默认值）

将此值设置为输入脉冲或输出脉冲的上升时间。

### 放电

### **Discharge switch on-resistance** — 放电开关导通电阻 `12` `Ohm`（默认值）

一个典型值是放电引脚饱和电压除以对应电流。

### **Discharge switch off-resistance** — 放电开关关断电阻 `500e6` `Ohm`（默认值）

一个典型值是放电引脚漏电流除以对应的引脚电压。

### 分压器

### **Potential divider component resistance** — 分压器组件电阻 `5` `kOhm`（默认值）

555 型定时器的典型值为 5 kΩ。当芯片未连接到电路时，可以直接在正电源引脚和控制引脚之间测量该值。
## 所属库

Simscape / Electrical / Integrated Circuits

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

## 描述

定时器集成电路的行为模型

Timer 模块是定时器集成电路（如 NE555）的行为模型。

下图显示了实现结构。

**Potential divider component resistance** 参数设置构成分压器的三个电阻的值。两个比较器输入具有无限输入电阻和零输入电容。S-R Latch 模块提供置位-复位锁存器的功能。它包含一个输出电容和一个电阻，其值设置为与 **Propagation delay** 参数值匹配。该模块使用 CMOS NOT 模块对输出级反相器进行建模。在 Timer 模块对话框中，您可以定义 CMOS 门的输出电阻、低电平输出电压和高电平输出电压。放电开关将实际定时器上的 NPN 双极晶体管近似为具有定义的开关导通电阻和关断电阻值的开关。
