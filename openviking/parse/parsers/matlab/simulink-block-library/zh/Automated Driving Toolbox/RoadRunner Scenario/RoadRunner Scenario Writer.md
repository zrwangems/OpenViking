---
type: simulink-block
title: 'RoadRunner Scenario Writer'
family: 'driving'
product_id: 'driving'
product_name: 'Automated Driving Toolbox'
documentation_release: R2025b
official_category: 'RoadRunner Scenario'
documentation_page: 'roadrunnerscenariowriter'
documentation_source_path: 'ref/roadrunnerscenariowriter.html'
language: zh-CN
chinese_source: worker-translation
---

# RoadRunner Scenario Writer

## 端口

### 输入

### **Message** — 要写入场景的状态信息，指定为 Simulink 消息

要写入场景的状态信息，指定为 Simulink 消息。要在模型中根据输入信号构造 Simulink 消息，请使用 Send (Simulink) 模块。然后，将 Send 模块的输出连接到 RoadRunner Scenario Writer 模块。

## 参数

### **Topic Category** — 主题类别 `Actor`（默认） | `Event` | `Diagnostics`

主题类别，指定为以下选项之一：

- `Actor` — 将行动者数据写入场景。
- `Event` — 将事件数据写入场景。
- `Diagnostics` — 将类型为 BusDiagnostics 的自定义诊断消息写入场景。

### **Actor Type** — 场景中行动者的类型 `All Types`（默认） | `Vehicle`

场景中行动者的类型，指定为 `All Types` 或 `Vehicle`。`Vehicle` 类型还包含行动者的车轮信息。

所选的行动者类型决定 **Topic** 参数可用的值。

**注意**

`All Types` 行动者类型也适用于场景中的行人。

### **Topic** — 行动者或车辆数据 `Actor Pose` | `Actor Pose (Driving Scenario compatible)` | `Vehicle Pose`

行动者数据或车辆数据。**Topic** 参数可以保存两组值，具体取决于 **Actor Type** 参数的配置。

如果以下两个字段配置均为 true，则 **Topic** 参数包含下表所述的选项：

- **Topic Category** 设置为 `Actor`。
- **Actor Type** 设置为 `All Types`。

| 选项 | 描述 |
| --- | --- |
| `Actor Pose (Driving Scenario compatible)`（默认） | 与行动者关联的动态数据，例如 actor ID、位置、速度、横滚、俯仰、偏航和角速度。选择此值时，模块会将类型为 `BusActorPose` 的总线写入场景。 |
| `Actor Pose` | 与行动者关联的动态数据，例如位姿、速度和角速度。选择此值时，模块会将类型为 `BusActorRuntime` 的总线写入场景。 |

如果以下两个字段配置均为 true，则 **Topic** 参数包含 `Vehicle Pose` 选项：

- **Topic Category** 设置为 `Actor`。
- **Actor Type** 设置为 `Vehicle`。

选择 `Vehicle Pose` 选项可启用将与车辆关联的动态数据（例如车轮位姿）写入场景。选择此值时，模块会将类型为 `BusVehicleRuntime` 的总线写入场景。

### **Event Type** — 事件类型 `Action Complete`（默认） | `User-Defined`

写入场景的事件类型，指定为以下项之一。

- `Action Complete` — 指示自定义操作已处理。选择此值时，模块会将类型为 `BusActionComplete` 的总线写入场景。
- `User-Defined` — 指示用户定义的事件已返回到场景。

  正在写入的事件必须映射到 RoadRunner Scenario 模块中其对应的总线对象。

#### 依赖关系

要启用此参数，请将 **Topic Category** 设置为 `Event`。

## 所属库

Automated Driving Toolbox / RoadRunner Scenario

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

将所选主题写入 RoadRunner 场景

RoadRunner Scenario Writer 模块将行动者、事件或诊断信息写入 RoadRunner 场景。该模块接收此主题信息作为输入，这些信息由 Simulink® 行动者行为模型内部计算，形式为 Simulink® 消息。您可以将 **Topic Category** 参数设置为 `Actor`、`Event` 或 `Diagnostics`。例如，当您选择 `Actor` 主题时，模块会将与行动者关联的动态数据（例如 actor ID、速度和角速度）写入场景。

RoadRunner Scenario Writer 模块以特定总线类型的形式将信息写入场景。总线类型定义总线对象的固定结构，包括总线元素的名称、数据类型和维度。要启用写入场景，请通过在 Block Parameters 对话框中点击 load function，将所需总线类型加载到 MATLAB® 基础工作区。此操作使模块能够接收预期类型的总线以写入场景。例如，在构建 Simulink 行动者行为模型时，您可以将 Bus Creator (Simulink) 模块的 **Output data type** 参数设置为已加载的总线类型，然后填写相应总线元素的值。然后，您可以将此总线作为输入转发到 RoadRunner Scenario Writer 模块。

如果您在 RoadRunner Scenario 中使用行动者组，可以通过以下方式使用 RoadRunner Scenario Writer 模块控制各个子行动者的行为。

- 使用一个 RoadRunner Scenario Writer 模块向不同行动者发送消息。例如，您可以使用 Message Merge 模块将携带模型中不同逻辑实现结果的消息排队到 RoadRunner Scenario Writer 模块。这些消息中的每一个都可以携带不同的 `ActorID` 值。
- 使用多个 RoadRunner Scenario Writer 模块。您可以将每个 RoadRunner Scenario Writer 模块的 `Actor Pose`、`Actor Pose (Driving Scenario compatible)` 或 `Vehicle Pose` 总线的 `ActorID` 值指向不同的子行动者。
