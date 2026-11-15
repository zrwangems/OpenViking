---
type: simulink-block
title: 'GRT (optimized for fixed/floating-point)'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Code and Tool Customization / Model Configuration Set Customization / Code Generation Configuration Sets'
documentation_page: 'grtoptimizedforfixedfloatingpoint'
documentation_source_path: 'ref/grtoptimizedforfixedfloatingpoint.html'
language: zh-CN
chinese_source: worker-translation
---

# GRT (optimized for fixed/floating-point)

## 端口

在 R2025b 中未记录。

## 参数

### **Configure the model for** — 配置目标 `GRT (optimized for fixed/floating-point)` (default) | `ERT (optimized for fixed-point)` | `ERT (optimized for floating-point)` | `GRT (debug for fixed/floating-point)` | `Custom`

通过使用预定义 MATLAB 脚本更新父模型的活动配置参数的目标。

### **Configuration function** — 自定义 MATLAB 脚本 `rtwsampleconfig` (default)

更新父模型的活动配置参数的预定义或自定义 MATLAB 脚本。

#### 依赖关系

此参数仅与 Custom MATLAB file 模块一起使用。要启用此参数，请将 **Configure the model for** 设置为 `Custom`。

### **Invoke build process after configuration** — 启动构建过程 `off` (default) | `on`

如果选中，预定义脚本将在更新配置参数后启动代码生成和构建过程。

## 所属库

Embedded Coder / Configuration Wizards

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2006b 中引入**

## 描述

为 GRT 定点或浮点代码生成更新父模型的活动配置参数

当您将 GRT(optimized for fixed-point) 模块添加到 Simulink® 模型中并双击该模块时，预定义 MATLAB® 脚本将执行，并针对使用 GRT 目标的定点或浮点代码生成以最佳方式配置模型参数。设置一个模块参数，以在配置模型后启动构建过程。

双击该模块后，打开配置参数对话框，可以看到模型参数值已更改。

**注意**

为了提供在配置之间快速切换的方法，您可以在模型中包含多个 Configuration Wizard 模块。
