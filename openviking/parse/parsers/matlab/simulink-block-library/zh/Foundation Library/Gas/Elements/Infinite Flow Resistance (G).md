---
type: simulink-block
title: 'Infinite Flow Resistance (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Elements'
documentation_page: 'infiniteflowresistanceg'
documentation_source_path: 'ref/infiniteflowresistanceg.html'
language: zh-CN
chinese_source: worker-translation
---

# Infinite Flow Resistance (G)

## 端口

### 守恒

### **A** — 质量流量和能量流量均为零

气体守恒端口，其中质量流量和能量流量均等于零。

### **B** — 质量流量和能量流量均为零

气体守恒端口，其中质量流量和能量流量均等于零。

## 参数

未在 R2025b 中记录。

## 所属库

Simscape / Foundation Library / Gas / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

气体网络中的完全绝热断口

Infinite Flow Resistance (G) 模块表示气体网络中的一个断口。没有质量流量或能量流量通过该断口。但是，由连接到回路的 Gas Properties (G) 模块指定的气体属性在断口两侧相同。使用此模块为端口 **A** 和端口 **B** 之间的压力差和温度差设置优先级和初始目标值。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **初始目标** 部分。有关详细信息，请参阅“设置模块变量的优先级和初始目标”和“有限气体体积模块的初始条件”。

标称值提供了一种指定模型中变量预期量值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或属性检查器中的 **标称值** 部分。有关详细信息，请参阅“修改模块变量的标称值”。
