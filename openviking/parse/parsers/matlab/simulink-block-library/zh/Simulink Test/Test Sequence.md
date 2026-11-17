---
type: simulink-block
title: 'Test Sequence'
family: 'sltest'
product_id: 'sltest'
product_name: 'Simulink Test'
documentation_release: R2025b
official_category: ''
documentation_page: 'testsequence'
documentation_source_path: 'ref/testsequence.html'
language: zh-CN
chinese_source: worker-translation
---

# Test Sequence

## 端口

R2025b 中未记录。

## 参数

有关模块参数的描述，请参阅 Subsystem。

## 所属库

Simulink Test

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

如果使用包含 `verify` 语句的 Test Sequence Scenarios，则无法生成 Structured Text 代码。

## 版本历史

**在 R2015a 中引入**

### R2025a: 仅查看活动场景的 `verify` 结果

Test Manager 不显示非活动 Test Sequence 场景中 `verify` 语句的结果。

## 描述

创建仿真测试场景、函数调用和评估

使用表格化的步骤序列定义测试序列。与 Test Assessment 模块类似，Test Sequence 模块使用 MATLAB® 作为动作语言。双击 Test Sequence 模块图标以打开 Test Sequence 编辑器。
