---
type: simulink-block
title: 'Comparator'
family: 'integrated-circuits'
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

### 守恒

### **+** — 同相输入端电气

与比较器同相输入端关联的电气守恒端口。

### **-** — 反相输入端电气

与比较器反相输入端关联的电气守恒端口。

### **OUT** — 输出端口电气

与比较器输出端关联的电气守恒端口。

## 参数

### 输入

### **输入失调电压** — 输入失调电压 `5` `mV` (默认)

输入电压之差必须大于该电压，比较器才会给出逻辑输出 1。

### **平均输入电容** — 平均输入电容 `0` `pF` (默认)

通常可以在制造商数据表中找到该电容值。将该值设置为零可以缩短仿真时间。

### 输出

### **低电平输出电压** — 低电平输出电压 `0` `V` (默认)

当输入端电压差小于或等于阈值电压且输出电流为零时的稳态输出电压 VOL。

### **高电平输出电压** — 高电平输出电压 `5` `V` (默认)

当输入端电压差大于阈值电压且输出电流为零时的稳态输出电压 VOH。

### **输出电阻** — 输出电阻 `50` `Ohm` (默认)

该参数是输出电压降与输出电流之比。将该参数设置为 (VOH−VOH1)/IOH1，其中 VOH1 是输出电流为 IOH1 时降低后的输出高电压。

### **传播延迟** — 传播延迟 `0` `s` (默认)

根据高到低和低到高的传播延迟设置该值。

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

Comparator 模块是比较器集成电路的抽象行为模型。它不对内部晶体管级实现进行建模。因此，该模块在仿真期间运行速度快，但保留正确的 I/O 行为。该模块在电气上将差分输入建模为具有无限大电阻和有限或零电容。

该模块将门输出建模为一个电压源，该电压源驱动一个串联电阻和一个连接到地的电容。输出引脚连接到电阻-电容连接节点。如果输入之差大于输入阈值电压，则输出等于 **高电平输出电压** (VOH)。否则，输出等于 **低电平输出电压** (VOL)。

输出模型如下图所示。
