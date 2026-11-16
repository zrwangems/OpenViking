---
type: simulink-block
title: 'Op-Amp'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Elements'
documentation_page: 'opamp'
documentation_source_path: 'ref/opamp.html'
language: zh-CN
chinese_source: official
---

# Op-Amp

## 端口

### 守恒

### **+** — 正极端子 电气

与运算放大器正极端子相关联的电气守恒端口。

### **-** — 负极端子 电气

与运算放大器负极端子相关联的电气守恒端口。

### **out** — 输出端子 电气

与运算放大器的输出节点相关联的电气守恒端口。

端口名称在模块图标中不可见，但您可以在模块对话框的**描述**选项卡中点击**源代码**链接，在基础源文件中查看此名称。

## 参数

R2025b 官方文档未提供。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Elements

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

理想的运算放大器

Op-Amp 模块对理想的运算放大器 (op-amp) 进行建模。下图显示了实现原理图。

Implementation schematic of the Op-Amp block

该模块的实现基于以下假设：

- 理想的运算放大器增益 *A* 假定为无限大
- 那么，对于有限输出，必须使 *V1* = 0
- 理想的运算放大器还意味着电流从 p 到 n 为零 (*i1* = 0)

这些假设得出该模块的以下方程：

```
equations
    v1 == p.v - n.v;
    v1 == 0;
    i1 == 0;
end
```

有关详细信息，请在模块对话框的**描述**选项卡中点击**源代码**链接。

该模块没有参数。但是，您可以在仿真之前初始化**流入输出节点的电流**变量。有关详细信息，请参阅Block-Level Variable Initialization。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的**初始目标**部分。有关详细信息，请参阅设置模块变量的优先级和初始目标值。

标称值提供了一种指定模型中变量的预期模的方法。使用基于标称值的系统缩放可提高仿真的稳健性。标称值可以来自不同的来源，其中之一是模块对话框或属性检查器中的的**标称值**部分。有关详细信息，请参阅Modify Nominal Values for a Block Variable。
