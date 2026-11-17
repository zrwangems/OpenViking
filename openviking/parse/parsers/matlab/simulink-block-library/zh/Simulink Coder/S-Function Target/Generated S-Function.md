---
type: simulink-block
title: 'Generated S-Function'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'S-Function Target'
documentation_page: 'generatedsfunction'
documentation_source_path: 'ref/generatedsfunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Generated S-Function

## 端口

### 输入

### **Input** — S-function 输入可变

参见要求。
### 输出参数

### **Output** — S-function 输出可变

参见要求。

## 参数

### **Generated S-function name (model\_sf)** — S-function 的名称 `model_sf`（默认）| 字符向量

生成的 S-function 的名称。代码生成器通过将 `_sf` 追加到生成该模块的模型或子系统的名称来派生该名称。

### **Show module list** — 选择显示模块列表 off（默认）| on

如果选中，则显示为 S-function 生成的模块。

## 所属库

Simulink Coder / S-Function Target

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2011b 中引入**

## 描述

将模型或子系统表示为生成的 S-function 代码

Generated S-Function 模块的实例表示代码生成器从其 S-function 系统目标文件为模型或子系统生成的代码。

### 要求

- S-Function 模块的行为必须与其生成来源的模型或子系统完全相同。
- 在创建模块之前，显式指定 Inport 模块信号属性，例如信号宽度或采样时间。此规则的唯一例外涉及采样时间，如 Sample Time Propagation in Generated S-Functions 中所述。
- 将 Generated S-Function 模块的求解器参数设置为与原始模型或子系统的参数相同。生成的 S-function 代码的运行方式与原始子系统完全相同。有关此规则的例外情况，请参阅 Solver Type for Top Models with Generated S-Functions。
