---
type: simulink-block
title: 'Action Node'
family: 'systemcomposer'
product_id: 'systemcomposer'
product_name: 'System Composer'
documentation_release: R2025b
official_category: 'Describe System Behaviors / Describe Activity Diagrams'
documentation_page: 'actionnode'
documentation_source_path: 'ref/actionnode.html'
language: zh-CN
chinese_source: official
---

# Action Node

## 端口

R2025b 官方文档未提供。

## 参数

### 动作节点

### **名称** — 动作节点名称 `Action` (默认) | 动作节点名称

动作节点的名称。默认情况下，活动图编辑器会将画布上的第一个动作节点命名为 `Action`。当您添加更多的动作节点时，编辑器会在名称 `Action` 后添加越来越多的数字后缀。

**示例:** `Action2`

### **行为类型** — 活动图或 MATLAB 函数 `MATLAB` (默认) | `Activity`

指明动作节点所代表的活动类型。

- `MATLAB` - 包含现有的 MATLAB 函数（如 `rand`），或在 `.m` 文件中编写的自定义函数
- `Activity` - 包含消耗和产生令牌的另一个活动图

### **引脚名称的可见性** — 在动作节点上显示引脚名称的选项 `off` (默认) | `on`

选择该复选框后，将显示所选动作节点的所有输入和输出引脚的名称。

### **MATLAB 函数名称** — MATLAB 函数名称 函数名称

动作节点实现的 MATLAB 函数的名称。该函数可以是现有的 MATLAB 函数，也可以是您在 `.m` 文件中创建的自定义函数。

**示例:** `customfunction_add`

#### 依赖项

要启用此参数，请在属性检查器中将**行为类型**设置为 **MATLAB**。

### **持续时间** — 执行动作节点所用的时间 `0` (默认) | 正整数

活动图执行动作节点所花费的时间单位数。活动图在持续时间结束时执行一个动作节点的 MATLAB 函数。

### **构造型** — 导入的配置文件中的构造型列表 可用构造型的名称

该列表包含导入的配置文件中的构造型。要为动作节点指定构造型，请从列表中选择构造型。

您还可以使用 `<new/edit>` 选项，使用配置文件编辑器管理配置文件。

## 所属库

R2025b 官方文档未提供。

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2024a 中推出**

## 描述

通过 MATLAB 函数或嵌套活动图处理对象令牌

动作节点表示活动图中要执行的特定动作。此动作可通过 MATLAB® 函数或嵌套活动图实现。

动作节点处理传入的令牌，生成新的令牌。输入引脚会消耗输入令牌。新生成的令牌通过输出引脚输出。

要执行动作节点，其输入引脚必须持有由令牌多重性参数指定的最少数量的对象令牌，而且所有传入的控制流都必须提供一个控制令牌。

具有 MATLAB 行为的动作节点会在 MATLAB 函数完成后终止。但是，当所有输出参数节点、流最终节点和活动最终节点都至少有一个令牌时，有活动行为的动作节点就会终止。

有关活动图主题的路线图，请参阅使用活动图描述系统行为。

### 创建 Action 节点

您可以通过两种方式在活动图画布上创建动作节点：

- 将 Action Node 模块从左边的调色板拖到画布上的任意位置。
- 按住画布上所需位置的左指针，向任意方向拖动。节点的蓝色轮廓会出现在画布上。从大纲下方出现的菜单中选择**创建动作**。
