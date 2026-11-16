---
type: simulink-block
title: 'Custom MATLAB file'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Configuration Wizards'
documentation_page: 'custommatlabfile'
documentation_source_path: 'ref/custommatlabfile.html'
language: zh-CN
chinese_source: worker-translation
---

# Custom MATLAB file

## 端口

在 R2025b 中未记录。

## 参数

### **为以下项配置模型** — 配置目标 `Custom` (default) | `ERT (optimized for fixed-point)` | `ERT (optimized for floating-point)` | `GRT (optimized for fixed/floating-point)` | `GRT (debug for fixed/floating-point)`

使用预定义的 MATLAB 脚本更新父模型活动配置参数的目标。

### **配置函数** — 自定义 MATLAB 脚本 `rtwsampleconfig` (default)

更新父模型活动配置参数的预定义或自定义 MATLAB 脚本。

#### 依赖关系

此参数仅与此 Configuration Wizards 模块一起使用。要启用此参数，请将 **为以下项配置模型** 设置为 `Custom`。

### **配置后调用构建过程** — 启动构建过程 `off` (default) | `on`

如果选中，预定义脚本会在更新配置参数后启动代码生成和构建过程。

## 所属库

Embedded Coder / Configuration Wizards

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2011a 中引入**

## 描述

使用包含自定义 MATLAB 代码的文件更新父模型的活动配置参数

当您将 Custom MATLAB file 模块添加到 Simulink® 模型并双击它时，自定义 MATLAB® 脚本会执行并配置与代码生成相关的模型参数。设置模块参数以在配置模型后调用构建过程。

双击该模块后，打开“配置参数”对话框以查看模型参数值已更改。

将示例 MATLAB 脚本 `matlabroot/toolbox/coder/simulinkcoder_core/rtwsampleconfig.m` 与 Custom MATLAB file 模块一起使用。根据您的模型要求调整该脚本。该模块和脚本为自定义提供了一个起点。有关详细信息，请参阅创建自定义 Configuration Wizard 模块。

**注意**

为了提供在配置之间快速切换的方式，您可以在模型中包含多个 Configuration Wizard 模块。
