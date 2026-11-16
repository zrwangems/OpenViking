---
type: simulink-block
title: 'Testbench Task'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Processor Testbench'
documentation_page: 'testbenchtask'
documentation_source_path: 'ref/testbenchtask.html'
language: zh-CN
chinese_source: worker-translation
---

# Testbench Task

## 端口

### 输入

### **Timer Task Function Call** — 来自定时器驱动任务标量的函数调用输入端口

此端口接受来自 Task Manager 模块的定时器驱动任务事件端口的函数调用事件信号。

## 参数

在 R2025b 中未记录。

## 所属库

SoC Blockset / Processor Testbench

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

Embedded Coder™ 不为该模块生成代码。

## 版本历史

**在 R2019b 中引入**

## 描述

对您的 SoC 处理器应用程序的外部定时器驱动任务负载

Testbench Task 模块模拟软件应用程序外部的定时器驱动任务负载。使用 Testbench Task 模块，您可以模拟当其他进程竞争处理器执行时间时对您的软件应用程序的影响。

**注意**

作为处理器测试平台的一部分，Testbench Task 模块必须放置在 SoC 模型的顶层。
