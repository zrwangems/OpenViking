---
type: simulink-block
title: 'Tx'
family: 'serdes'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'tx'
documentation_source_path: 'ref/tx.html'
language: zh-CN
chinese_source: worker-translation
---

# Tx

## 端口

### 输入

### **WaveIn** — 输入信号 标量 | 向量

输入信号，指定为波形。

**数据类型：** `double`
### 输出

### **WaveOut** — 修改后的输出数据 标量 | 向量

修改后的输出数据，包含根据 [1] 中所述方法的有损印刷电路板传输线模型的影响。

**数据类型：** `double`

## 参数

R2025b 中未记录。

## 所属库

SerDes Toolbox / Utilities

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

具有默认设置的发射器模块

将发射器组件恢复为 SerDes Designer app 设置的默认值。如果已将某个发射器组件替换为 AMI 模块，并且现在希望将其恢复为该 app 导出的原始发射器组件，则可以使用此模块。
