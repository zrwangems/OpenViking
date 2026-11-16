---
type: simulink-block
title: 'Digital Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / BeagleBone Blue Hardware / Modeling / Basic'
documentation_page: 'digitalread'
documentation_source_path: 'beagleboneblue/ref/digitalread.html'
language: zh-CN
chinese_source: worker-translation
---

# Digital Read

## 端口

### 输出

### **Port\_1** — 输出信号标量

该端口输出你在 **Pin** 参数中指定的板上数字引脚的逻辑状态。

**数据类型：** `Boolean`

## 参数

### **Pin** — 数字输入的引脚编号 GPIO1\_17（默认） | GPIO1\_25 | GPIO3\_1 | GPIO3\_2 | GPIO3\_17 | GPIO3\_20

指定数字引脚编号。

要查看引脚映射表，请点击 **查看引脚映射表**。

每个模块在模型中必须具有唯一的引脚编号。

### **采样时间** — 该模块读取输入引脚值的频率 `0.1`（默认）

以 seconds 为单位指定该模块读取引脚值的频率。

当你将此参数指定为 `-1` 时，Simulink® 会根据模型中的模块上下文确定该模块的最佳采样时间。

## 所属库

Simulink Coder Support Package for BeagleBone Blue Hardware / Basic

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2018b 中引入**

## 描述

读取数字输入引脚的逻辑状态

Digital Read 模块输出板上指定数字引脚的逻辑状态。

在外部模式仿真期间，该模块输出从目标硬件上运行的可执行文件返回的仿真结果。

在所有其他模式下的仿真期间，该模块输出零。
