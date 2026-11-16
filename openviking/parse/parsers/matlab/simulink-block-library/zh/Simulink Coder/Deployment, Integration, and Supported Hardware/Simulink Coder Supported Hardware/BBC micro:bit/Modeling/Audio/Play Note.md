---
type: simulink-block
title: 'Play Note'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Audio'
documentation_page: 'playnote'
documentation_source_path: 'microbit/ref/playnote.html'
language: zh-CN
chinese_source: worker-translation
---

# Play Note

## 端口

### 输入

该模块有一个输入端口。

### **Port\_1(Frequency)** — 要播放的音符的频率，标量

要播放的音符所对应的频率（以 Hz 为单位）。输入频率可来自 Note Generator 模块的输出，或来自 constant block 或 wave block 的输出。

**数据类型：** `double`

## 参数

### **Pin** — 连接到扬声器的引脚编号 P1 (default)

BBC micro:bit 上连接到用于播放该音符的扬声器的引脚编号。

## 所属库

Simulink Coder Support Package for BBC micro:bit/Audio

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2018a 中引入**

## 描述

在 BBC micro:bit 上的指定引脚播放音符

Play Note 模块在连接到 BBC micro:bit 上指定引脚的扬声器上播放音符。所播放的音符与输入频率相对应。
