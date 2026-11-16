---
type: simulink-block
title: 'Observer Reference'
family: 'sltest'
product_id: 'sltest'
product_name: 'Simulink Test'
documentation_release: R2025b
official_category: ''
documentation_page: 'observerreference'
documentation_source_path: 'ref/observerreference.html'
language: zh-CN
chinese_source: official
---

# Observer Reference

## 端口

R2025b 官方文档未提供。

## 参数

### **Observer 模型名称** — Observer 模型的文件名 `''` (默认) | 字符向量

Observer 模型的路径。文件名必须是有效的 MATLAB® 标识符。扩展名（例如 `.slx`）是可选的。您在 Observer Reference 模块的参数对话框中输入 Observer 模型名称，通过右键点击该模块并选择**模块参数**可访问该对话框。您还可以从该对话框打开您指定的模型。

#### 编程用法

|  |
| --- |
| **参数**：`ObserverModelName` |
| **类型**：字符向量 |
| **值**：`''` | `'<observer model name>'` |
| **默认值**：`''` |

## 所属库

Simulink Test

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2019a 中推出**

## 描述

创建并包含 Observer 模型

Observer Reference 模块引用称为 Observer 模型的独立模型。Observer 模型和 Observer Reference 模块支持对主模型中的信号进行无线监控。当您分别从**测试**选项卡或上下文菜单中点击或选择**添加 Observer Reference** 时，系统会自动在主 Simulink® 模型的顶层添加一个 Observer Reference 模块，并创建一个 Observer 模型。仅可以在模型的顶层添加 Observer Reference 模块。

Observer 模型包含 Observer Port 模块，并且可以包含示波器或验证子系统等模块，分别用于监控或验证观测到的信号。信号通过 Observer Port 模块映射到 Observer 模型。Observer Reference 模块没有输入端口或输出端口。有关使用 Observer 的详细信息和示例，请参阅使用 Observer 以无线方式访问模型数据。

要停止观测信号，请从主模型中删除所有 Observer Reference 模块。
