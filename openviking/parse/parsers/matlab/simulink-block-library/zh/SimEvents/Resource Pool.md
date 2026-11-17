---
type: simulink-block
title: 'Resource Pool'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'resourcepool'
documentation_source_path: 'ref/resourcepool.html'
language: zh-CN
chinese_source: worker-translation
---

# Resource Pool

## 端口
```yaml
ports:
- name: Port_1
  summary: 更改资源量 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
- name: Port_u
  summary: 输出正在使用的资源数量 标量
  direction: output
  data_types: double
- name: Port_util
  summary: 输出资源池被使用的平均时间 标量
  direction: output
  data_types: double
- name: Port_avail
  summary: 输出可用资源数量 标量
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 更改资源量 标量 | 向量 | 矩阵

用于更改资源量的输入实体端口。输入不能为负值。

#### 依赖

要启用此端口，请选择 `Change amount through
control port` 作为 **Resource amount
source**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_u** — 输出正在使用的资源数量 标量

正在使用的资源数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Amount in use,
u** 的复选框。

**数据类型：** `double`

### **Port\_util** — 输出资源池被使用的平均时间 标量

资源池被使用的平均等待时间。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Average utilization,
util** 的复选框。

**数据类型：** `double`

### **Port\_avail** — 输出可用资源数量 标量

可用资源数量。

#### 依赖

要启用此端口，请点击 **Statistics** 选项卡，然后选中标记为 **Amount available,
avail** 的复选框。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Resource name
  summary: 资源池中资源的名称 Resource1（默认）| 字符向量
  group: ''
  block_parameter: ResourceName
  type: 字符向量
  values: '''Resource1'' | 字符向量'
  default: '''Resource1'''
- name: Resource granularity
  summary: 选择资源使用的粒度 Discrete unit（默认）| Fractional amount
  group: ''
  block_parameter: ResourceGranularity
  type: 字符向量
  values: '''Discrete unit'' | ''Fractional amount'''
  default: '''Discrete unit'''
- name: Reusable upon release
  summary: 指定资源在释放后是否可重用 off（默认）| on
  group: ''
  block_parameter: ReusableUponRelease
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: Resource amount source
  summary: 选择资源量来源 Dialog（默认）| Change amount through control port
  group: ''
  block_parameter: ResourceAmountSource
  type: 字符向量
  values: '''Dialog'' | ''Change amount through control port'''
  default: '''Dialog'''
- name: Resource amount
  summary: 设置资源量 10（默认）| 标量
  group: ''
  block_parameter: ResourceAmount
  type: 字符向量
  values: '''10'' | 标量'
  default: '''10'''
- name: 初始资源量
  summary: 输入资源的初始数量 10（默认）| 标量
  group: ''
  block_parameter: InitialResourceAmount
  type: 字符向量
  values: '''10'' | 标量'
  default: '''10'''
- name: 资源可见性
  summary: 选择资源的可用性 Global（默认）| Scoped
  group: ''
  block_parameter: InitialResourceAmount
  type: 字符向量
  values: '''10'' | 标量'
  default: '''10'''
- name: 使用量，u
  summary: 正在使用的资源数量 off（默认）| on
  group: ''
  block_parameter: AmountInUse
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: 平均利用率，util
  summary: 输出平均资源利用率 off（默认）| on
  group: ''
  block_parameter: AverageUtilization
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
- name: 可用量，avail
  summary: 输出可用资源数量 off（默认）| on
  group: ''
  block_parameter: AmountAvailable
  type: 字符向量
  values: '''on'' | ''off'''
  default: '''off'''
```

### **Resource name** — 资源池中资源的名称 `Resource1`（默认）| 字符向量

输入实体资源的名称。

#### 编程使用

|  |
| --- |
| **模块参数**：`ResourceName` |
| **类型**：字符向量 |
| **值**：`'Resource1'` | 字符向量 |
| **默认值**：`'Resource1'` |

### **Resource granularity** — 选择资源使用的粒度 `Discrete unit`（默认）| `Fractional amount`

选择资源使用的粒度。

- `Discrete unit` — 使用整数增量。
- `Fractional amount` — 使用小数增量。

#### 编程使用

|  |
| --- |
| **模块参数**：`ResourceGranularity` |
| **类型**：字符向量 |
| **值**：`'Discrete unit'` | `'Fractional amount'` |
| **默认值**：`'Discrete unit'` |

### **Reusable upon release** — 指定资源在释放后是否可重用 `off`（默认）| `on`

- 选中此复选框以允许此资源在释放后返回资源池。此类资源的一个示例是餐厅中的餐桌，当顾客离开时可供重复使用。
- 清除此复选框以防止此资源在释放后返回资源池。在这种情况下，当资源被释放时，它不再在资源池中可用。此类资源的一个示例是餐厅中的食物，在消费后不可重复使用。

#### 编程使用

|  |
| --- |
| **模块参数**：`ReusableUponRelease` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **Resource amount source** — 选择资源量来源 `Dialog`（默认）| `Change amount through control port`

选择资源量来源。

- `Dialog`
- `Change amount through control
  port`

  选择此选项以启用输入实体端口和可变容量资源。到达消息的负载会增加模块的现有资源数量。例如，如果资源池有五个资源，并且负载为三的消息到达输入端口，则该模块有八个可用资源。资源数量不能递减。

#### 编程使用

|  |
| --- |
| **模块参数**：`ResourceAmountSource` |
| **类型**：字符向量 |
| **值**：`'Dialog'` | `'Change amount through control port'` |
| **默认值**：`'Dialog'` |

### **Resource amount** — 设置资源量 `10`（默认）| 标量

输入资源量。

#### 依赖

选择 `Dialog` 以启用 **Resource amount source**。

#### 编程用法

|  |
| --- |
| **模块参数**：`ResourceAmount` |
| **类型**：字符向量 |
| **值**：`'10'` | 标量 |
| **默认值**：`'10'` |

### **初始资源量** — 输入资源的初始数量 `10`（默认）| 标量

输入资源的初始数量。

#### 依赖关系

选择 `Change amount through control port` 以启用 **资源量来源**。

#### 编程用法

|  |
| --- |
| **模块参数**：`InitialResourceAmount` |
| **类型**：字符向量 |
| **值**：`'10'` | 标量 |
| **默认值**：`'10'` |

### **资源可见性** — 选择资源的可用性 `Global`（默认）| `Scoped`

选择从此资源池获取的资源的行为为 `Global` 或 `Scoped`。

当选择 `Global` 时：

- 资源池名称在模型中必须唯一。
- 所有资源具有全局作用域，可以从模型层次结构中的任何位置引用。
- 携带从此模块获取的资源的实体必须显式释放该资源。
- 当实体被销毁时，与其关联的资源将返回到资源池（如果选中了 **释放后可重用** 复选框）。

当选择 `Scoped` 时：

- 资源在本地可见，只能从包含 Resource Pool 模块的子系统及其内部所有子系统引用。
- 资源池名称在 Resource Pool 模块可见的模型层次结构内必须唯一。
- 携带从此模块获取的资源的实体必须显式释放该资源。
- 当实体离开作用域时，该作用域本地尚未释放的任何资源将自动释放。如果选中了 **释放后可重用** 复选框，它们将返回到资源池。

#### 编程用法

|  |
| --- |
| **模块参数**：`InitialResourceAmount` |
| **类型**：字符向量 |
| **值**：`'10'` | 标量 |
| **默认值**：`'10'` |

### **使用量，u** — 正在使用的资源数量 `off`（默认）| `on`

输出模块已获取但尚未释放的资源数量。例如，如果资源池有 `10` 个资源，且实体获取了全部资源，则此端口显示 `10`。当模块释放资源时，此端口显示 `0`。

#### 编程用法

|  |
| --- |
| **模块参数**：`AmountInUse` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **平均利用率，util** — 输出平均资源利用率 `off`（默认）| `on`

输出平均资源利用率。

#### 编程用法

|  |
| --- |
| **模块参数**：`AverageUtilization` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### **可用量，avail** — 输出可用资源数量 `off`（默认）| `on`

输出可用资源数量。

#### 编程用法

|  |
| --- |
| **模块参数**：`AmountAvailable` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |
## 所属库

SimEvents / Entity Management SimEvents

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2016a 中引入**

## 描述

池化实体资源

Resource Pool 模块定义实体在模型仿真期间可以使用的资源。使用 Resource Acquirer 和 Resource Releaser 模块来操作这些资源。

使用指定的可用资源数量初始化该模块。然后：

- 使用一个或多个 Resource Acquirer 模块来预留这些资源。
- 使用 Resource Releaser 模块将资源返还给该模块以供将来使用。

您可以确定可用资源在模型层次结构中的可见性。您可以在池中选择 `Global` 或 `Scoped` 资源。

- `Global` — 资源可以从模型层次结构中的任何位置引用。
- `Scoped` — 资源在本地可见，只能从包含 Resource Pool 模块的子系统及其内部的所有子系统引用。
