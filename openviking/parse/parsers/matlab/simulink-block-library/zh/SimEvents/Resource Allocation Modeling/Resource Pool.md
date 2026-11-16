---
type: simulink-block
title: 'Resource Pool'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: 'Resource Allocation Modeling'
documentation_page: 'resourcepool'
documentation_source_path: 'ref/resourcepool.html'
language: zh-CN
chinese_source: worker-translation
---

# Resource Pool

## 端口

### 输入

### **Port_1** — 更改资源量 scalar | vector | matrix

用于更改资源量的输入实体端口。该输入不能为负值。

#### 依赖关系

要启用此端口，请选择 `Change amount through control port` 作为 **资源量来源**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 输出

### **Port_u** — 输出正在使用的资源数量 scalar

正在使用的资源数量。

#### 依赖关系

要启用此端口，请单击 **统计信息** 选项卡，然后选中标记为 **使用量, u** 的框。

**数据类型：** `double`

### **Port_util** — 输出池被利用的平均时间 scalar

池被利用的平均等待时间。

#### 依赖关系

要启用此端口，请单击 **统计信息** 选项卡，然后选中标记为 **平均利用率, util** 的框。

**数据类型：** `double`

### **Port_avail** — 输出可用资源数量 scalar

可用资源数量。

#### 依赖关系

要启用此端口，请单击 **统计信息** 选项卡，然后选中标记为 **可用量, avail** 的框。

**数据类型：** `double`

## 参数

### **资源名称** — 池中资源的名称 `Resource1` (默认) | character vector

输入实体资源的名称。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ResourceName` |
| **类型**: character vector |
| **值**: `'Resource1'` | character vector |
| **默认**: `'Resource1'` |

### **资源粒度** — 选择资源使用的粒度 `Discrete unit` (默认) | `Fractional amount`

选择资源使用的粒度。

- `Discrete unit` — 使用整数增量。
- `Fractional amount` — 使用小数增量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ResourceGranularity` |
| **类型**: character vector |
| **值**: `'Discrete unit'` | `'Fractional amount'` |
| **默认**: `'Discrete unit'` |

### **释放后可重用** — 指定资源在释放后是否可重用 `off` (默认) | `on`

- 选中此复选框以允许该资源在释放后返回到资源池。此类资源的一个示例是餐厅中的餐桌，当顾客离开时可供重用。
- 清除此复选框以防止该资源在释放后返回到资源池。在这种情况下，当资源被释放时，它不再在资源池中可用。此类资源的一个示例是餐厅中的食物，食用后不可重用。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ReusableUponRelease` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认**: `'off'` |

### **资源量来源** — 选择资源量来源 `Dialog` (默认) | `Change amount through control port`

选择资源量来源。

- `Dialog`
- `Change amount through control port`

  选择此选项可启用输入实体端口和可变容量资源。到达消息的负载会递增模块的现有资源数量。例如，如果资源池有五个资源，并且负载为三的消息到达输入端口，则该模块有八个可用资源。资源数量不能递减。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ResourceAmountSource` |
| **类型**: character vector |
| **值**: `'Dialog'` | `'Change amount through control port'` |
| **默认**: `'Dialog'` |

### **资源量** — 设置资源量 `10` (默认) | scalar

输入资源量。

#### 依赖关系

选择 `Dialog` 以启用 **资源量来源**。

#### 程序化使用

|  |
| --- |
| **模块参数**: `ResourceAmount` |
| **类型**: character vector |
| **值**: `'10'` | scalar |
| **默认**: `'10'` |

### **初始资源量** — 输入初始资源量 `10` (默认) | scalar

输入初始资源量。

#### 依赖关系

选择 `Change amount through control port` 以启用 **资源量来源**。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InitialResourceAmount` |
| **类型**: character vector |
| **值**: `'10'` | scalar |
| **默认**: `'10'` |

### **资源可见性** — 选择资源的可用性 `Global` (默认) | `Scoped`

选择从此池获取的资源的行为为 `Global` 或 `Scoped`。

当选择 `Global` 时：

- 资源池名称在模型中必须唯一。
- 所有资源具有全局作用域，并且可以从模型层次结构中的任何位置引用。
- 携带从此模块获取的资源的实体必须显式放弃该资源。
- 当实体被销毁时，如果选中 **释放后可重用** 复选框，则与其关联的资源将返回到池。

当选择 `Scoped` 时：

- 资源在本地可见，并且只能从包含 Resource Pool 模块的子系统及其内部的所有子系统中引用。
- 资源池名称在 Resource Pool 模块可见的模型层次结构内必须唯一。
- 携带从此模块获取的资源的实体必须显式放弃该资源。
- 当实体离开作用域时，任何该作用域本地且尚未释放的资源会自动释放。如果选中 **释放后可重用** 复选框，则它们将返回到池。

#### 程序化使用

|  |
| --- |
| **模块参数**: `InitialResourceAmount` |
| **类型**: character vector |
| **值**: `'10'` | scalar |
| **默认**: `'10'` |

### **使用量, u** — 正在使用的资源数量 `off` (默认) | `on`

输出模块已获取但尚未释放的资源量。例如，如果资源池有 `10` 个资源，并且实体获取了全部资源，则此端口显示 `10`。当模块释放这些资源时，此端口显示 `0`。

#### 程序化使用

|  |
| --- |
| **模块参数**: `AmountInUse` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认**: `'off'` |

### **平均利用率, util** — 输出平均资源利用率 `off` (默认) | `on`

输出平均资源利用率。

#### 程序化使用

|  |
| --- |
| **模块参数**: `AverageUtilization` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认**: `'off'` |

### **可用量, avail** — 输出可用资源量 `off` (默认) | `on`

输出可用资源量。

#### 程序化使用

|  |
| --- |
| **模块参数**: `AmountAvailable` |
| **类型**: character vector |
| **值**: `'on'` | `'off'` |
| **默认**: `'off'` |

## 所属库

SimEvents / Entity Management SimEvents

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2016a 中引入**

## 描述

池实体资源

Resource Pool 模块定义实体在模型仿真期间可以使用的资源。使用 Resource Acquirer 和 Resource Releaser 模块来操作这些资源。

使用指定的可用资源量初始化该模块。然后：

- 使用一个或多个 Resource Acquirer 模块保留这些资源。
- 使用 Resource Releaser 模块将资源返回到此模块以供将来使用。

您可以确定模型层次结构中可用资源的可见性。您可以在池中选择 `Global` 或 `Scoped` 资源。

- `Global` — 资源可以从模型层次结构中的任何位置引用。
- `Scoped` — 资源在本地可见，并且只能从包含 Resource Pool 模块的子系统及其内部的所有子系统中引用。
