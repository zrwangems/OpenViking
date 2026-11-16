---
type: simulink-block
title: 'LED Text Scroll'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / LED'
documentation_page: 'ledtextscroll'
documentation_source_path: 'microbit/ref/ledtextscroll.html'
language: zh-CN
chinese_source: worker-translation
---

# LED Text Scroll

## 端口

### 输入

### **String** — 要显示的输入文本向量

该端口接受 N×1 或 1×N 数组形式的数据。数据可以包含大写字母和数字 0-9。任何其他字符在 micro:bit 上都会显示为减号。

### 输出

### **Out** — 输出数据矩阵

该端口输出二维 5×5 向量数组形式的数据，可以将其发送到 5x5 LED Matrix 模块。然后，5x5 LED Matrix 模块可以获取该数据并在 micro:bit 上显示文本。

## 参数

### **滚动速度 (1–10)** — 滚动文本速度 `5`（默认）| 1 到 10（含）之间的任意整数

希望文本滚动的速度。数值越大，滚动速度越快。

## 所属库

Simulink Coder Support Package for BBC micro:bit/LED

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2017b 中引入**

## 描述

为 BBC micro:bit 创建滚动文本

LED Text Scroll 模块根据输入字符串创建滚动文本。然后，可以将滚动文本作为输入发送到 5x5 LED Matrix 模块。随后，5x5 LED Matrix 模块会在 micro:bit 板上显示该文本。
