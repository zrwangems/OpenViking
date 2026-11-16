---
type: simulink-block
title: 'Digital Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Basic'
documentation_page: 'digitalwrite'
documentation_source_path: 'beagleboneblue/ref/digitalwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Write

## 端口

### 输入

### **Port\_1** — 输入信号标量

该模块将此值设置到您在 **Pin** 参数中指定的数字输出引脚。

**数据类型：** `Boolean`

## 参数

### **Pin** — 数字输出的引脚编号 GPIO1\_25（默认） | GPIO1\_17 | GPIO3\_1 | GPIO3\_2 | GPIO3\_17 | GPIO3\_20

指定数字引脚编号。

要打开引脚映射表，请点击 **查看引脚映射**。

每个模块在模型中必须具有唯一的引脚编号。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Basic

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

设置数字输出引脚的逻辑状态

Digital Write 模块设置板上指定数字引脚的逻辑状态。

在外部模式仿真期间，该模块将此值设置到您在 **Pin** 参数中指定的引脚。

在所有其他模式的仿真期间，该模块不执行任何操作。
