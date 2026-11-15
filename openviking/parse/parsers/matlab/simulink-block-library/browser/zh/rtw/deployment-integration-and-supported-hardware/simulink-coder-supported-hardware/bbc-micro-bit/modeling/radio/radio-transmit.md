---
type: simulink-block
title: 'Radio Transmit'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BBC micro:bit / Modeling / Radio'
documentation_page: 'radiotransmit'
documentation_source_path: 'microbit/ref/radiotransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# Radio Transmit

## 端口

### 输入

### **Data** — 要传输的数据向量

该端口接受 N×1 或 1×N 数组形式的数据。

## 参数

### **Channel number (1–100)** — 选择用于传输数据的通道 `1`（默认值）| 从 1 到 100（含）的任意整数

要从中传输数据的通道号。

**注意**

发送器和接收器必须设置为相同的通道号。

## 所属库

Simulink Coder Support Package for BBC micro:bit/Radio

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

## 描述

通过无线电向 micro:bit 设备传输数据

Radio Transmit 模块通过无线连接向其他 micro:bit 设备传输数据。
