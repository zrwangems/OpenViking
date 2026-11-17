---
type: simulink-block
title: 'RoadRunner Scenario'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'RoadRunner Scenario'
documentation_page: 'roadrunnerscenario'
documentation_source_path: 'ref/roadrunnerscenario.html'
language: zh-CN
chinese_source: worker-translation
---

# RoadRunner Scenario

## 端口

R2025b 中未记录。

## 参数

### 动作

### **Action name** — 用户定义动作的名称 字符串

要映射到总线对象的用户定义动作的名称。

要添加动作名称，请点击 **User-defined actions** 输入表下方的 **Add** 按钮，然后双击 **Action name** 列中的单元格以键入新的表项。

### **Bus object name** — 总线对象的名称 字符串

与用户定义动作对应的总线对象的名称。

要添加与用户定义动作对应的总线对象名称，请在与该用户定义动作同一级别处双击 **Bus object name** 列中的单元格，然后键入新的表项。

所有添加的总线对象名称都必须有对应的总线对象。总线对象表示用户定义动作。您必须在 MATLAB® 中定义总线对象，使其包含与它在 RoadRunner Scenario 中所表示的用户定义动作相同的参数名称、数据类型和值。RoadRunner Scenario Reader 和 RoadRunner Scenario Writer 模块依赖加载到 MATLAB 工作区中的总线对象来识别传入的用户定义动作的结构。

有关为用户定义动作创建总线对象的详细信息，请参阅 Author RoadRunner Actor Behavior Using User-Defined Actions or Events in Simulink。

### 事件

### **Event name** — 用户定义事件的名称 字符串

要映射到总线对象的用户定义事件的名称。

要添加事件名称，请点击 **User-defined events** 输入表下方的 **Add** 按钮，然后双击 **Event name** 列中的单元格以键入新的表项。

### **Bus object name** — 总线对象的名称 字符串

与用户定义事件对应的总线对象的名称。

要添加与用户定义事件对应的总线对象名称，请在与该用户定义事件同一级别处双击 **Bus object name** 列中的单元格，然后键入新的表项。

所有添加的总线对象名称都必须有对应的总线对象。总线对象表示用户定义事件。您必须在 MATLAB 中定义总线对象，使其包含与它在 RoadRunner Scenario 中所表示的用户定义事件相同的参数名称、数据类型和值。RoadRunner Scenario Reader 和 RoadRunner Scenario Writer 模块依赖加载到 MATLAB 工作区中的总线对象来识别传入的用户定义事件的结构。

有关为用户定义事件创建总线对象的详细信息，请参阅 Author RoadRunner Actor Behavior Using User-Defined Actions or Events in Simulink。

### 配置

### **Maximum Points on Path** — 路径上的最大点数 `500`（默认值）| 正标量

路径跟随动作要读取的车辆参与者路径上的最大点数。

您可以将此参数的值设置为 1 到 264 之间的任意正标量。最大点数与参与者行为模型的仿真性能之间存在权衡。

仅当 Simulink 参与者行为模型包含 RoadRunner Scenario Reader 模块，且该模块通过将 **Topic Category** 设置为 `Action` 并将 **Action Type** 设置为 `Path Following` 来读取参与者的 Path Following 动作时，此参数才适用。RoadRunner Scenario Reader 模块在路径上的点数达到最大值后停止读取。

**数据类型：** `uint64`

## 所属库

Automated Driving Toolbox / RoadRunner Scenario

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

### R2025a：指定参与者路径上的最大点数

您可以指定路径跟随动作要读取的车辆参与者路径上的最大点数。

要配置最大点数，请在 **Configuration** 选项卡上的 **Maximum Points on Path** 字段中指定所需的值。

## 描述

定义 Simulink 参与者模型的接口

RoadRunner Scenario 模块定义 Simulink® 参与者模型的接口。Block Parameters 对话框包含以下选项卡，输入在这些选项卡下分组。

- Actions
- Events
- Configuration

RoadRunner Scenario 模块必须位于模型的根级别，否则模型编译将导致错误。
