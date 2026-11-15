---
type: simulink-block
title: 'SimEvents Debugger'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Simulation, Debugging, and Visualization / Debug Simulation'
documentation_page: 'simeventsdebugger'
documentation_source_path: 'ref/simeventsdebugger.html'
language: zh-CN
chinese_source: worker-translation
---

# SimEvents Debugger

## 端口

在 R2025b 中未记录。

## 参数

### **启用调试器** — 启用调试器 `on`（默认）| `off`

选中此复选框以为您的模型启用调试器。

## 所属库

SimEvents

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

调试 SimEvents 模型

SimEvents Debugger 模块为您的 SimEvents® 模型启用调试器。使用此模块，您可以：

- 检查存储模块中的实体及其属性值
- 在模块和事件上设置断点
- 监视实体

**注意**

SimEvents 调试器是初步版本。

要开始调试您的模型：

1. 从 SimEvents 库中，将 SimEvents Debugger 模块添加到您的
   SimEvents 模型中。
2. 在 Simulink® 编辑器中，点击 **单步前进** 按钮。

   调试器界面出现。

   SimEvents Debugger 窗口左侧包含带搜索字段的资源管理器窗格。窗格右侧的检查器部分显示左侧所选元素的数据。

- 点击 **继续仿真** 按钮（球体内指向右侧的绿色箭头。）以在调试器中开始仿真。仿真完成后，调试器界面关闭。
- 要探索其数据和行为，模型树显示在左侧窗格中。选择树中的元素。
- 完成后，在 Simulink 编辑器上，点击 **停止** 按钮以停止仿真。

### 检查实体

要在调试器中检查实体：

- 要步进到下一个时间步并检查实体，请在 Simulink 编辑器中再次点击 **单步前进** 按钮。此操作会跳过 `tnow` 处的所有事件。
- 要步进到下一个事件并检查实体，请在调试器中点击带有长垂直尾部并指向右侧一张纸的绿色箭头。
- 要设置断点：

  - 在特定时间，使用仿真步进器设置断点。
  - 在事件日历上的某个事件处，在调试器中的左侧窗格中，点击事件日历。
  - 在每个事件处，在调试器中的左侧窗格中，选择事件日历。在事件日历事件窗格中，选中 **事件执行前中断** 复选框。
  - 当实体进入模块时，在调试器中选择该模块。在检查器窗格底部，选中 **进入时中断** 复选框。
  - 当实体离开模块时，在调试器中选择该模块。在检查器窗格底部，选中 **实体退出前中断** 复选框。
- 要转到断点，请在调试器中点击 **继续** 按钮（球体内指向右侧的绿色箭头。）。

  **注意**

  当您在断点处停止调试器时，Simulink 编辑器和 MATLAB® 命令窗口会显示为无响应。但是，您可以从调试器窗口检查实体、设置新断点并继续仿真。
- 要监视实体，请在左侧树中点击该模块。在检查器窗格中，选中您要监视的实体的复选框。
