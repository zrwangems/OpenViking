---
type: simulink-block
title: 'TND'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Program Control'
documentation_page: 'tnd'
documentation_source_path: 'ref/tnd.html'
language: zh-CN
chinese_source: worker-translation
---

# TND

## 端口

### 输入

### **EnableIn** — 使能输入 off (默认) | on

控制模块的执行。**EnableIn** 反映该模块之前的梯级状态。如果该模块之前的梯级状态为 false，**EnableIn** 为 false，则模块不执行，并且输出不更新。
### 输出

### **EN** — 使能输出 off (默认) | on

默认情况下，**EnableOut** 跟随 **EnableIn** 的状态。如果模块的 **EnableIn** 输入为 false，则不执行该模块实现的逻辑，并且 **EnableOut** 信号设置为 false。

## 参数

未在 R2025b 中记录。

## 所属库

未在 R2025b 中记录。

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2019a 中引入**

## 描述

临时结束

TND 模块实现 `TND` 梯形图逻辑指令。当梯级条件为 true 时，该模块充当梯形图执行的结束。
