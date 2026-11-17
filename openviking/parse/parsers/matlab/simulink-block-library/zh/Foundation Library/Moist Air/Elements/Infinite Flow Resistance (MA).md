---
type: simulink-block
title: 'Infinite Flow Resistance (MA)'
family: 'moist-air'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'infiniteflowresistancema'
documentation_source_path: 'ref/infiniteflowresistancema.html'
language: zh-CN
chinese_source: worker-translation
---

# Infinite Flow Resistance (MA)

## 端口

### 守恒

### **A** — 质量流量和能量流量均为零的湿空气

湿空气守恒端口，其中质量流量和能量流量均等于零。

### **B** — 质量流量和能量流量均为零的湿空气

湿空气守恒端口，其中质量流量和能量流量均等于零。

## 参数

未在 R2025b 中记录。

## 所属库

Simscape / Foundation Library / Moist Air / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

湿空气网络中的完全绝热断开

Infinite Flow Resistance (MA) 模块表示湿空气网络中的一个断开。没有质量或能量流过该断开。但是，由连接到回路的 Moist Air Properties (MA) 模块指定的湿空气属性在断开的两侧相同。使用此模块可为端口 **A** 和端口 **B** 之间的压力、温度、比湿度和痕量气体质量分数差值设置优先级和初始目标值。

### 变量

若要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables 和 Initial Conditions for Blocks with Finite Moist Air Volume。

标称值提供了一种在模型中指定变量预期量值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
