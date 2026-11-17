---
type: simulink-block
title: 'Resource Releaser'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'resourcereleaser'
documentation_source_path: 'ref/resourcereleaser.html'
language: zh-CN
chinese_source: worker-translation
---

# Resource Releaser

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入实体 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: Port_1
  summary: 输出实体 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | enumerated | bus
    | fixed point
- name: Port_d
  summary: 已离开模块的实体数量 标量
  direction: output
  data_types: double
- name: Port_n
  summary: 尚未离开模块的实体数量 标量
  direction: output
  data_types: double
- name: Port_ex
  summary: 提取的实体数量 标量
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 输入实体 标量 | 向量 | 矩阵

进入模块的实体的输入实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`
### 输出

### **Port\_1** — 输出实体 标量 | 向量 | 矩阵

离开模块的实体的输出实体端口。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `fixed point`

### **Port\_d** — 已离开模块的实体数量 标量

已离开模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities departed, d** 的复选框。

**数据类型：** `double`

### **Port\_n** — 尚未离开模块的实体数量 标量

尚未离开模块的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities in block, n** 的复选框。

**数据类型：** `double`

### **Port\_ex** — 提取的实体数量 标量

从此模块中拉出的实体数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Number of entities extracted, ex** 的复选框。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Resource to release
  summary: 选择要释放的资源 All（默认）| Selected
  group: ''
  block_parameter: ResourceToRelease
  type: character vector
  values: '''All'' | ''Selected'''
  default: '''All'''
- name: Event actions
  summary: 指定实体在特定事件上的行为 Entry（默认）| Exit | Blocked
  group: ''
  block_parameter: EntryAction, ExitAction, BlockedAction
  type: character vector
  values: MATLAB® code
  default: ''''''
- name: Number of entities departed, d
  summary: 输出已离开模块的实体数量 off（默认）| on
  group: ''
  block_parameter: NumberEntitiesDeparted
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Number of entities in block, n
  summary: 输出模块中存在的、尚未离开的实体数量 off（默认）| on
  group: ''
  block_parameter: NumberEntitiesInBlock
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Number of entities extracted, ex
  summary: 从此模块提取的实体数量 off（默认）| on
  group: ''
  block_parameter: NumEntitiesExtracted
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
```

### **Resource to release** — 选择要释放的资源 `All`（默认）| `Selected`

选择要释放的资源。

- `All`

  释放通过实体的所有资源的使用。
- `Selected`

  释放选定的资源。选择此选项将启用 **Available Resources** 表。

#### 编程使用

|  |
| --- |
| **模块参数**：`ResourceToRelease` |
| **类型**：character vector |
| **值**：`'All'` | `'Selected'` |
| **默认值**：`'All'` |

### **Event actions** — 指定实体在特定事件上的行为 `Entry`（默认）| `Exit` | `Blocked`

在 **Event actions** 中定义行为。例如，当实体进入模块时调用 **Entry** 动作。

#### 编程使用

|  |
| --- |
| **模块参数**：`EntryAction, ExitAction, BlockedAction` |
| **类型**：character vector |
| **值**：MATLAB® code |
| **默认值**：`''` |

### **Number of entities departed, d** — 输出已离开模块的实体数量 `off`（默认）| `on`

选中此复选框将输出已离开模块的实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberEntitiesDeparted` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities in block, n** — 输出模块中存在的、尚未离开的实体数量 `off`（默认）| `on`

选中此复选框将输出模块中存在的、尚未离开的实体数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumberEntitiesInBlock` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Number of entities extracted, ex** — 从此模块提取的实体数量 `off`（默认）| `on`

由 Entity Find 模块从此模块中拉出的提取实体数量。有关查找和提取实体的详细信息，请参阅 Find and Extract Entities in SimEvents Models。

#### 编程使用

|  |
| --- |
| **模块参数**：`NumEntitiesExtracted` |
| **类型**：character vector |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |
## 所属库

SimEvents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

释放实体资源

当实体进入 Resource Releaser 模块时，该模块释放资源。该模块接受一个实体，只要下一个模块接受该实体或 Entity Find 模块提取该实体，该实体就立即离开该模块。

您可以指定该模块释放特定资源类型或释放所有资源。

### 可用资源

使用 **Available Resources** 控件可以：

- 从模型中所有 Resource Pool 模块定义的资源中选择资源。
- 将资源添加到 Selected Resources 表中，您可以在其中修改它们。

该列表显示模型中的所有资源。（如果没有资源，**Available Resources** 列表为空）。

如果资源列表很长，您可以在文本框中键入资源名称以筛选列表。

使用 **Available Resources** 区域中的按钮帮助构建资源表。这些按钮执行以下操作。

| 按钮 | 操作 |
| --- | --- |
| 带有圆形绿色箭头符号的按钮 | 刷新 **Available Resources** 列表。该列表会更新您在模块对话框打开期间所做的任何上游模型更改。 |
| 带有指向右侧蓝色箭头的按钮 | 将选定的资源添加到 **Selected Resources** 表。 |
| 带有指向左侧蓝色箭头的按钮 | 将选定的资源从 **Selected Resources** 表移动到 **Available Resources** 列表。如果选定的资源是您手动添加的，此按钮将显示为灰色。 |

可用资源列表下方的消息区域会显示有关资源的其他消息（如适用）。

| 消息 | 含义 |
| --- | --- |
| `> Resource already selected` | 您已将资源添加到 **Selected Resources** 表。您无法再次将该资源添加到表中。 |

### Selected Resources

使用 **Selected Resources** 下的控件来构建和管理要释放的资源列表。每个资源在表中显示为一行。

使用这些控件，您可以：

- 手动添加资源。
- 修改您从 **Available Resources** 列表添加到表中以进行释放的资源。
- 通过将 **Amount Source** 参数设置为 `Dialog` 或 `Attribute` 来选择要释放的资源量。

  - `Dialog` — 在 **Amount** 列下指定要释放的资源量。
  - `Attribute` — 指定定义要释放资源量的属性名称。

**Selected Resources** 下的按钮执行以下操作。

| 按钮 | 操作 | 说明 |
| --- | --- | --- |
| 带绿色加号的按钮 | 向表中添加模板资源。 | 重命名资源并指定其属性。 |
| 带重叠相同纸张符号的按钮 | 将所选资源的副本添加到表中，作为新资源的基础。 | 重命名副本。两个资源不能具有相同的名称。 |
| 带红色叉号的按钮 | 从 **Selected Resources** 表中移除所选资源。 | 以这种方式删除资源时，不会出现确认提示，并且无法撤销该操作。 |
| 带向上蓝色箭头的按钮 | 在 **Selected Resources** 表中按顺序上移所选资源。 | 不适用 |
| 带向下蓝色箭头的按钮 | 在 **Selected Resources** 表中按顺序下移所选资源。 | 不适用 |

**注意**

如果删除一行并应用更改，删除操作可能会影响与其他属性对应的信号输出端口。例如，如果模块有一个信号输出端口 **A2**，而您删除了带有标记为 **A1** 的端口的属性，则模块会将 **A2** 重新标记为 **A1**。请验证连接到重新标记端口的任何信号是否仍按预期连接。

| 属性 | 规格 | 用法 |
| --- | --- | --- |
| **Name** | 资源的名称。每个资源必须具有唯一的名称。 | 双击现有名称，然后键入新名称。 |
| **Amount Source** | 实体请求的资源量是来自对话框还是来自属性。 | 选择 `Dialog` 或 `Attribute`。如果选择 `Attribute`，则资源量的来源来自实体的属性。此选项允许每个实体获取不同数量的资源。有关详细信息，请参阅 Set Resource Amount with Attributes。 |
| **Amount** | 要分配给资源的值（当资源来自对话框时）。 | 双击该值，然后键入要分配的值。此值是每个实体释放的资源数量。例如，如果 **Amount** 为三，则到达 Resource Releaser 模块的每个实体必须等待释放 3 个资源后才能离开该模块。要释放的资源的粒度与 Resource Pool 模块中资源的粒度一致。 |
