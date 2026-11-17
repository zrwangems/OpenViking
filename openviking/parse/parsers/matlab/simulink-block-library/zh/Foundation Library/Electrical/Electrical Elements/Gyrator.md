---
type: simulink-block
title: 'Gyrator'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'gyrator'
documentation_source_path: 'ref/gyrator.html'
language: zh-CN
chinese_source: worker-translation
---

# Gyrator

## 端口
```yaml
ports: []
```

该模块有四个电学守恒端口。极性由 + 和 – 符号表示。标记为 1+ 和 1– 的端口连接到初级绕组。标记为 2+ 和 2– 的端口连接到次级绕组。
## 参数
```yaml
parameters: []
```

**Gyration conductance**
:   回转电导常数 *G*。默认值为 `1`。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

电气系统中的理想回转器

回转器可用于用电容器实现电感器。其主要优势在于可以用物理尺寸小得多的电容来产生等效电感。在实践中，回转器由运算放大器加上额外的无源元件实现。

Gyrator 模块对无损耗的理想回转器进行建模，用以下方程描述：

I1=G·V2

I2=G·V1

其中

|  |  |
| --- | --- |
| *`V1`* | 输入电压 |
| *`V2`* | 输出电压 |
| *`I1`* | 流入输入 + 端的电流 |
| *`I2`* | 流出输出 + 端的电流 |
| *`G`* | 回转电导 |

连接到初级绕组和次级绕组的两个电气网络必须各自拥有自己的 Electrical Reference 模块。

### 变量

要在仿真之前为模块变量设置优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
