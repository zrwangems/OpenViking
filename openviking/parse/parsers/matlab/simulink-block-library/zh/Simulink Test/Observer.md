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
chinese_source: worker-translation
---

# Observer Reference

## 端口

R2025b 中未记录。

## 参数

### **Observer Model name** — Observer 模型的文件名 `''`（默认）| 字符向量

Observer 模型的路径。文件名必须是有效的 MATLAB® 标识符。扩展名（例如 `.slx`）是可选的。您在 Observer Reference 模块参数对话框中输入 Observer 模型名称，该对话框可通过右键单击模块并选择 **Block Parameters** 打开。您还可以从该对话框打开您指定的模型。

#### 程序化使用

|  |
| --- |
| **Parameter**: `ObserverModelName` |
| **类型**：character vector |
| **Value**: `''` | `'<observer model name>'` |
| **默认值**：`''` |

## 所属库

Simulink Test

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2019a 中引入**

## 描述

创建并包含一个 Observer 模型

Observer Reference 模块引用一个称为 Observer 模型的独立模型。Observer 模型和 Observer Reference 模块支持对主模型中的信号进行无线监测。当您分别从 **Test** 选项卡或上下文菜单中单击或选择 **Add Observer Reference** 时，Observer Reference 模块会自动添加到主 Simulink® 模型的顶层，并创建一个 Observer 模型。您只能在模型的顶层添加 Observer Reference 模块。

Observer 模型包含一个 Observer Port 模块，并且可以包含诸如示波器或验证子系统之类的模块，以分别监测或验证所观测的信号。信号通过 Observer Port 模块映射到 Observer 模型。Observer Reference 模块没有输入端口或输出端口。有关更多信息以及使用 Observer 的示例，请参阅 Access Model Data Wirelessly by Using Observers。

要停止观测信号，请从主模型中删除所有 Observer Reference 模块。
