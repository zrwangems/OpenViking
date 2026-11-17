---
type: simulink-block
title: 'Rx'
family: 'utilities'
product_id: 'serdes'
product_name: 'SerDes Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'rx'
documentation_source_path: 'ref/rx.html'
language: zh-CN
chinese_source: worker-translation
---

# Rx

## 端口

### 输入

### **WaveIn** — 输入信号 标量 | 向量

输入信号，指定为波形。

**数据类型：** `double`
### 输出

### **WaveOut** — 修改后的输出数据 标量 | 向量

修改后的输出数据，其中包含按照 [1] 中概述的方法得到的有损印刷电路板传输线模型的影响。

**数据类型：** `double`

## 参数

未在 R2025b 中记录。

## 所属库

SerDes Toolbox / Utilities

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

具有默认设置的接收器模块

将接收器组件恢复为 SerDes Designer 应用设置的默认值。如果已将接收器组件替换为 AMI 模块，并且现在希望将其恢复为应用导出的原始发送器组件，则可以使用此模块。
