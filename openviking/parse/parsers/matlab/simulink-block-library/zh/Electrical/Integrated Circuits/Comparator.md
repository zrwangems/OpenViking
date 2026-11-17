---
type: simulink-block
title: 'Comparator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Integrated Circuits'
documentation_page: 'comparator'
documentation_source_path: 'ref/comparator.html'
language: zh-CN
chinese_source: worker-translation
---

# Comparator

## 端口
```yaml
ports:
- name: +
  summary: 同相输入电气端口
  direction: conserving
- name: '-'
  summary: 反相输入电气端口
  direction: conserving
- name: OUT
  summary: 输出端口电气端口
  direction: conserving
```

### 守恒端口

### **+** — 同相输入电气端口

与比较器同相输入关联的电气守恒端口。

### **-** — 反相输入电气端口

与比较器反相输入关联的电气守恒端口。

### **OUT** — 输出端口电气端口

与比较器输出关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Input offset voltage
  summary: 输入失调电压 5 mV（默认值）
  group: 输入
- name: Average input capacitance
  summary: 平均输入电容 0 pF（默认值）
  group: 输入
- name: Low level output voltage
  summary: 低电平输出电压 0 V（默认值）
  group: 输出
- name: High level output voltage
  summary: 高电平输出电压 5 V（默认值）
  group: 输出
- name: Output resistance
  summary: 输出电阻 50 Ohm（默认值）
  group: 输出
- name: Propagation delay
  summary: 传播延迟 0 s（默认值）
  group: 输出
```

### 输入

### **Input offset voltage** — 输入失调电压 `5` `mV`（默认值）

输入电压之差必须大于该电压值，比较器才会输出逻辑 1。

### **Average input capacitance** — 平均输入电容 `0` `pF`（默认值）

通常可以在制造商数据手册中找到该电容值。将此值设置为零可以加快仿真速度。

### 输出

### **Low level output voltage** — 低电平输出电压 `0` `V`（默认值）

当输入端电压差小于或等于阈值电压且输出电流为零时的稳态输出电压 VOL。

### **High level output voltage** — 高电平输出电压 `5` `V`（默认值）

当输入端电压差大于阈值电压且输出电流为零时的稳态输出电压 VOH。

### **Output resistance** — 输出电阻 `50` `Ohm`（默认值）

该参数为输出电压降与输出电流之比。将此参数设置为 (VOH−VOH1)/IOH1，其中 VOH1 是输出电流为 IOH1 时降低后的输出高电压。

### **Propagation delay** — 传播延迟 `0` `s`（默认值）

根据高到低和低到高的传播延迟设置此值。
## 所属库

Simscape / Electrical / Integrated Circuits

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

## 描述

比较器集成电路的行为模型

Comparator 模块是比较器集成电路的抽象行为模型。它不对内部晶体管级实现进行建模。因此，该模块在仿真期间运行速度快，同时保持正确的 I/O 行为。该模块将差分输入电气建模为具有无限电阻和有限或零电容。

该模块将门输出建模为驱动串联电阻的电压源以及连接到地的电容。输出引脚连接到电阻-电容连接节点。如果输入之差大于输入阈值电压，则输出等于 **High level output voltage**（VOH）。否则，输出等于 **Low level output voltage**（VOL）。

输出模型如下图所示。
