---
type: simulink-block
title: 'PLC Controller'
family: 'plccoder'
product_id: 'plccoder'
product_name: 'Simulink PLC Coder'
documentation_release: R2025b
official_category: 'Ladder Diagram Integration / Organizational Units'
documentation_page: 'plccontroller'
documentation_source_path: 'ref/plccontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# PLC Controller

## 端口

R2025b 中未记录。

## 参数

R2025b 中未记录。

## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2019a 中引入**

## 描述

PLC Controller

在 Ladder Diagram 中，控制器是顶层组织单元，通常由任务标签和控制器标签组成。可以有一个任务或多个任务。控制器内的任务并行执行。Simulink® PLC Coder™ 中提供两种类型的控制器模块：

- PLC Controller Suite
- PLC Controller

PLC controller suite 是一种模块层次结构，用于对简单完整的 Ladder Logic Controller 结构建模，而 PLC controller 模块包含梯形逻辑语义。控制器标签存储全局变量的信息，例如 DataType、Mapping type、Port、Address 等。为梯形图定义的全局变量构成控制器的输入和输出端口。
