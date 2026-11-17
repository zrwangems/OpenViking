---
type: simulink-block
title: 'Open Circuit'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'opencircuit'
documentation_source_path: 'ref/opencircuit.html'
language: zh-CN
chinese_source: worker-translation
---

# Open Circuit

## 端口
```yaml
ports:
- name: V
  summary: 零电流电气
  direction: unspecified
```

### 守恒

### **V** — 零电流电气

不消耗电流的电气守恒端口。
## 参数
```yaml
parameters: []
```

R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements Simscape / Electrical / Connectors & References

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

### R2019b：不再需要封顶未连接的端口

不再需要此模块。从 R2019b 开始，禁止 Simscape™ 模型中未连接守恒端口的限制已被解除。现在，如果您将守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，您仍然可以使用终结器模块来提高图的可读性。

没有移除终结器模块的计划。所有使用这些模块的现有模型的工作方式与之前版本相同。

## 描述

不消耗电流的电气端口终结器

Open Circuit 模块表示一个不消耗电流的电气端子。

您可以使用此模块来终结您希望保持开路的其他模块上的电气端口。这不是必需的，因为如果您将守恒端口保持未连接，物理网络会将该端口处的所有 Through 变量设置为 0。但是，终结器模块可以提高图的可读性。

您还可以使用此模块来设置节点处的初始绝对电压。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
