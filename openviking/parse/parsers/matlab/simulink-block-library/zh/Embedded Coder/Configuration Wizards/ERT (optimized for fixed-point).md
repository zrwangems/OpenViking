---
type: simulink-block
title: 'ERT (optimized for fixed-point)'
family: 'configuration-wizards'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Configuration Wizards'
documentation_page: 'ertoptimizedforfixedpoint'
documentation_source_path: 'ref/ertoptimizedforfixedpoint.html'
language: zh-CN
chinese_source: worker-translation
---

# ERT (optimized for fixed-point)

## 端口

未在 R2025b 中记录。

## 参数

### **Configure the model for** — 配置目标 `ERT (optimized for fixed-point)` (默认) | `ERT (optimized for floating-point)` | `GRT (optimized for fixed/floating-point)` | `GRT (debug for fixed/floating-point)` | `Custom`

通过预定义 MATLAB 脚本更新父模型的活动配置参数的目标。

### **Configuration function** — 自定义 MATLAB 脚本 `rtwsampleconfig` (默认)

预定义或自定义的 MATLAB 脚本，用于更新父模型的活动配置参数。

#### 依赖关系

此参数仅与 Custom MATLAB file 模块一起使用。要启用此参数，请将 **Configure the model for** 设置为 `Custom`。

### **Invoke build process after configuration** — 启动构建过程 `off` (默认) | `on`

如果选中，预定义脚本将在更新配置参数后启动代码生成和构建过程。

## 所属库

Embedded Coder / Configuration Wizards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2006b 中引入**

## 描述

更新父模型的活动配置参数，以进行 ERT 定点代码生成

当您将 ERT (optimized for fixed-point) 模块添加到 Simulink® 模型并双击它时，将执行预定义的 MATLAB® 脚本，并为使用 ERT 目标的定点代码生成优化配置模型参数。设置一个模块参数，以便在配置模型后调用构建过程。

双击该模块后，打开 Configuration Parameters 对话框，可看到模型参数值已更改。

**注意**

为提供在配置之间快速切换的方法，您可以在模型中包含多个 Configuration Wizard 模块。
