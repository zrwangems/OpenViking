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
chinese_source: official
---

# Generated S-Function

## 端口

### 输入

### **Input** — S-Function 输入 视情况而定

请查看需求。
### 输出参量

### **Output** — S-Function 输出 视情况而定

请查看需求。

## 参数

### **生成的 S-Function 名称(model\_sf)** — S-Function 的名称 `model_sf` (默认) | 字符向量

生成的 S-Function 的名称。代码生成器通过将 `_sf` 追加到从其生成模块的模型或子系统的名称来派生该名称。

### **显示模块列表** — 选择显示模块列表 off (默认) | on

如果选中，则显示系统为 S-Function 生成的模块。

## 所属库

Simulink Coder / S-Function Target

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2011b 中推出**

## 描述

将模型或子系统表示为生成的 S-Function 代码

Generated S-Function 模块的实例表示代码生成器从其模型或子系统的 S-Function 系统目标文件生成的代码。

### 要求

- S-Function 模块必须与生成它的对应模型或子系统执行相同的操作。
- 在创建模块之前，显式指定 Inport 模块信号属性，如信号宽度或采样时间。此规则的唯一例外是采样时间，如生成的 S-Function 中的采样时间传播所述。
- 将 Generated S-Function 模块的求解器参数设置为与原始模型或子系统的参数相同。生成的 S-Function 代码与原始子系统具有完全相同的操作。有关此规则的例外情况，请参阅具有生成的 S-Function 的顶层模型的求解器类型。
