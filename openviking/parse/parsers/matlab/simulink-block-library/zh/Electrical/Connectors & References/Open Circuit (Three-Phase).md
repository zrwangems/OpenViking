---
type: simulink-block
title: 'Open Circuit (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'opencircuitthreephase'
documentation_source_path: 'ref/opencircuitthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Open Circuit (Three-Phase)

## 端口

### 守恒

### **~** — 三相电气端口

可展开的复合 (**a**,**b**, **c**) 三相端口。

## 参数

### **Modeling option** — 是否对复合三相端口或展开三相端口建模 `Composite three-phase ports`（默认） | `Expanded three-phase ports`

是否对复合三相端口或展开三相端口建模。

Composite three-phase ports 用单个模块端口表示三个独立电气守恒端口。您可以使用 Composite three-phase ports 构建与三相电气系统单线图相对应的模型。

Expanded three-phase ports 使用三个独立电气守恒端口表示三相系统的各相。

## 所属库

Simscape / Electrical / Connectors & References

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2019b：不再需要端接未连接端口

不再需要此模块。从 R2019b 开始，已取消 Simscape™ 模型中不允许未连接守恒端口的限制。现在，如果让某个守恒端口保持未连接，物理网络会将该端口处所有 Through 变量设置为 0。但是，您仍可以使用终结器模块来提高图的可读性。

没有移除终结器模块的计划。所有使用这些模块的现有模型的工作方式与之前版本相同。

## 描述

不消耗电流的三相终结器

Open Circuit (Three-Phase) 模块对在三相中的任何一相上均不消耗电流的三相连接进行建模。
