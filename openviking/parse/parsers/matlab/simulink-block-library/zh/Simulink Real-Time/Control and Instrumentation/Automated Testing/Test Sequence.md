---
type: simulink-block
title: 'Test Sequence'
family: 'sltest'
product_id: 'sltest'
product_name: 'Simulink Test'
documentation_release: R2025b
official_category: 'Test Authoring / Inputs'
documentation_page: 'testsequence'
documentation_source_path: 'ref/testsequence.html'
language: zh-CN
chinese_source: official
---

# Test Sequence

## 端口

R2025b 官方文档未提供。

## 参数

有关模块参数的描述，请参阅Subsystem。

## 所属库

Simulink Test

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

如果您使用包含 `verify` 语句的测试序列场景，则无法生成结构化文本代码。

## 版本历史

**在 R2015a 中推出**

### R2025a: 查看仅活动场景的 `verify` 结果

测试管理器不显示非活动 Test Sequence 场景中 `verify` 语句的结果。

## 描述

创建仿真测试场景、函数调用和评估

使用表格步骤序列定义测试序列。与 Test Assessment 模块类似，Test Sequence 模块使用 MATLAB® 作为动作语言。双击 Test Sequence 模块图标以打开测试序列编辑器。
