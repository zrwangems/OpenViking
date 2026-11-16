---
type: simulink-block
title: 'Note Generator'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Audio'
documentation_page: 'notegenerator'
documentation_source_path: 'microbit/ref/notegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Note Generator

## 端口

### 输出

该模块有一个输出端口。

### **Port\_1(Frequency)** — 对应音乐音符标量生成的频率

与指定音乐 **Note** 和 **Scale** 相对应而生成的频率（以 Hz 为单位）。

**数据类型：** `double`

## 参数

### **Scale** — 音乐音符的音阶 `Mid` (默认) | `Low` | `High`

指定音乐音符的音阶。Scale 可取 `Low`、`Mid` 或 `High`，将音符置于三个可用八度之一。中央 C 的频率为 261.6 Hz，对应于 Mid 音阶中 **Note** 值为 C。

### **Note** — 半音阶中音符的字母名称 `C` (默认) | `C#` | `D` | `D#` | `E` | `F` | `F#` | `G` | `G#` | `A` | `A#` | `B`

指定半音阶的 12 个音符之一。列出的音符按音高从低到高排列。每对相邻音符相隔一个半音。

## 所属库

Simulink Coder Support Package for BBC micro:bit/Audio

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2018a 中引入**

## 描述

生成与音乐音符对应的频率

Note Generator 模块生成与所选音乐音符和音阶对应的频率。
