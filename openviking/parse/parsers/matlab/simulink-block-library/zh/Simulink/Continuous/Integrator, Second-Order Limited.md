---
type: simulink-block
title: 'Second-Order Integrator Limited'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'secondorderintegratorlimited'
documentation_source_path: 'slref/secondorderintegratorlimited.html'
language: zh-CN
chinese_source: worker-translation
---

# Second-Order Integrator Limited

## 端口
```yaml
ports:
- name: u
  summary: 输入信号 u 标量 | 向量 | 矩阵
  direction: input
  data_types: double
- name: x0
  summary: 初始条件 x0 标量 | 向量 | 矩阵
  direction: input
  data_types: double
- name: dx0
  summary: 初始条件 dx0 标量 | 向量 | 矩阵
  direction: input
  data_types: double
- name: External Reset
  summary: 用于将状态重置为初始条件的信号 标量 | 向量 | 矩阵
  direction: input
  data_types: double
- name: x
  summary: 输出信号 x 标量 | 向量 | 矩阵
  direction: output
  data_types: double
- name: dx
  summary: 输出信号 dx 标量 | 向量 | 矩阵
  direction: output
  data_types: double
```

### 输入

### **u** — 输入信号 `u` 标量 | 向量 | 矩阵

积分器系统的输入信号 `u`，指定为标量、向量或矩阵。

此端口不具有直接馈通。

**数据类型：** `double`

### **x0** — 初始条件 `x0` 标量 | 向量 | 矩阵

指定积分器系统初始条件 `x0` 的外部信号。您可以将初始条件指定为标量、向量或矩阵。

此端口具有直接馈通。

#### 依赖关系

要启用此输入端口，请将 **Initial condition source x** 参数设置为 `external`。

**数据类型：** `double`

### **dx0** — 初始条件 `dx0` 标量 | 向量 | 矩阵

指定积分器系统初始条件 `dx0` 的外部信号。您可以将初始条件 `dx0` 指定为标量、向量或矩阵。

此端口具有直接馈通。

#### 依赖关系

要启用此输入端口，请将 **Initial condition source dx/dt** 参数设置为 `external`。

**数据类型：** `double`

### **External Reset** — 用于将状态重置为初始条件的信号 标量 | 向量 | 矩阵

外部重置信号是标量、向量或矩阵，用于将模块状态重置为初始条件。

此端口具有直接馈通。

#### 依赖关系

要启用此输入端口，请将 **External reset** 参数设置为 `rising`、`falling` 或 `either`。

**数据类型：** `double`
### 输出

### **x** — 输出信号 `x` 标量 | 向量 | 矩阵

`x` 状态输出信号，以标量、向量或矩阵形式提供。

**数据类型：** `double`

### **dx** — 输出信号 `dx` 标量 | 向量 | 矩阵

`dx` 状态输出信号，指定为标量、向量或矩阵。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Initial condition source x
  summary: 状态 *x* 的初始条件来源 internal（默认）| external
  group: x
  block_parameter: ICSourceX
  type: character vector, string
  values: '''internal'' | ''external'''
  default: '''internal'''
- name: Initial condition x
  summary: 状态 *x* 的初始条件 0.0（默认）| 标量 | 向量 | 矩阵
  group: x
  block_parameter: ICX
  type: character vector, string
  values: scalar | vector | matrix
  default: '''0.0'''
- name: Limit x
  summary: 限制状态 *x* 的值 off | on
  group: x
  block_parameter: LimitX
  type: character vector, string
  values: '''off'' | ''on'''
  default: '''off'' (Second-Order Integrator) | ''on'' (Second-Order Integrator Limited)'
- name: Upper limit x
  summary: 状态 *x* 的上限 1 | inf | 标量 | 向量 | 矩阵
  group: x
  block_parameter: UpperLimitX
  type: character vector, string
  values: '''1'' | ''inf'' | scalar | vector | matrix'
  default: '''1'' (Second-Order Integrator Limited) | ''inf'' (Second-Order Integrator)'
- name: Lower limit x
  summary: 状态 *x* 的下限 0（默认）| -inf | 标量 | 向量 | 矩阵
  group: x
  block_parameter: LowerLimitX
  type: character vector, string
  values: '''0'' | ''-inf'' | scalar | vector | matrix'
  default: '''0'' (Second-Order Integrator Limited) | ''-inf'' (Second-Order Integrator)'
- name: Wrap x
  summary: 启用 x 的环绕 off（默认）| on
  group: x
  block_parameter: WrapX
  type: character vector, string
  values: '''off'' | ''on'''
  default: '''off'''
- name: Wrapped upper value x
  summary: 环绕 x 的上限值 pi（默认）| 标量 | 向量 | 矩阵
  group: x
  block_parameter: WrappedUpperValueX
  type: character vector, string
  values: scalar | vector | matrix
  default: '''pi'''
- name: Wrapped lower value x
  summary: 环绕 x 的下限值 -pi（默认）| 标量 | 向量 | 矩阵
  group: x
  block_parameter: WrappedLowerValueX
  type: character vector, string
  values: scalar | vector | matrix
  default: '''-pi'''
- name: Absolute tolerance x
  summary: 计算状态 *x* 的绝对容差 auto（默认）| -1 | 标量 | 向量
  group: x
  block_parameter: AbsoluteToleranceX
  type: character vector, string
  values: '''auto'' | ''-1'' | any positive real scalar or vector'
  default: '''auto'''
- name: State name x
  summary: 状态 *x* 的名称 ''（默认）| 字符向量 | 字符串
  group: x
  block_parameter: StateNameX
  type: character vector, string
  values: ''' '' | user-defined'
  default: ''' '''
- name: Initial condition source dx/dt
  summary: 状态 *dx/dt* 的初始条件来源 internal（默认）| external
  group: dx/dt
  block_parameter: ICSourceDXDT
  type: character vector
  values: '''internal'' | ''external'''
  default: '''internal'''
- name: Initial condition dx/dt
  summary: 状态 *dx/dt* 的初始条件 0.0（默认）| 标量 | 向量 | 矩阵
  group: dx/dt
  block_parameter: ICDXDT
  type: character vector
  values: scalar | vector | matrix
  default: '''0.0'''
- name: Limit dx/dt
  summary: 限制状态 *dx/dt* 的值 off | on
  group: dx/dt
  block_parameter: LimitDXDT
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'' (Second-Order Integrator) | ''on'' (Second-Order Integrator Limited)'
- name: Upper limit dx/dt
  summary: 状态 *dx/dt* 的上限 inf（默认）| 标量 | 向量 | 矩阵
  group: dx/dt
  block_parameter: UpperLimitDXDT
  type: character vector
  values: scalar | vector | matrix
  default: '''inf'''
- name: Lower limit dx/dt
  summary: 状态 *dx/dt* 的下限 -inf（默认）| 标量 | 向量 | 矩阵
  group: dx/dt
  block_parameter: LowerLimitDXDT
  type: character vector
  values: scalar | vector | matrix
  default: '''-inf'''
- name: Absolute tolerance dx/dt
  summary: 计算状态 *dx/dt* 的绝对容差 auto（默认）| -1 | 标量 | 向量
  group: dx/dt
  block_parameter: AbsoluteToleranceDXDT
  type: character vector, string, scalar, or vector
  values: '''auto'' | ''-1'' | any positive real scalar or vector'
  default: '''auto'''
- name: State name dx/dt
  summary: 状态 *dx/dt* 的名称 ' '（默认）| 字符向量 | 字符串
  group: dx/dt
  block_parameter: StateNameDXDT
  type: character vector, string
  values: ''' '' | user-defined'
  default: ''' '''
- name: External reset
  summary: 将状态重置为初始条件 none（默认）| rising | falling | either
  group: 属性
  block_parameter: ExternalReset
  type: character vector, string
  values: '''none'' | ''rising'' | ''falling'' | ''either'''
  default: '''none'''
- name: Enable zero-crossing detection
  summary: 启用零交叉检测 on（默认）| off
  group: 属性
  block_parameter: ZeroCross
  type: 字符向量、字符串
  values: '''on'' | ''off'''
  default: '''on'''
- name: 当 x 达到饱和时重新初始化 dx/dt
  summary: 当 *x* 达到饱和时重置 *dx/dt* off（默认）| on
  group: 属性
  block_parameter: ReinitDXDTwhenXreachesSaturation
  type: 字符向量、字符串
  values: '''off'' | ''on'''
  default: '''off'''
- name: 线性化时忽略状态限值和重置
  summary: 线性化时忽略状态限值和外部重置 off（默认）| on
  group: 属性
  block_parameter: IgnoreStateLimitsAndResetForLinearization
  type: 字符向量、字符串
  values: '''off'' | ''on'''
  default: '''off'''
- name: 显示输出
  summary: 要显示的输出端口 both（默认）| x | dxdt
  group: 属性
  block_parameter: ShowOutput
  type: 字符向量、字符串
  values: '''both'' | ''x'' | ''dxdt'''
  default: '''both'''
```

### x

### **Initial condition source x** — 状态 *x* 的初始条件来源 `internal`（默认）| `external`

指定状态 *x* 的初始条件来源。

- `internal` — 从 **Initial condition x** 参数获取状态 *x* 的初始条件。
- `external` — 从连接到 **X0** 输入端口的外部模块获取状态 *x* 的初始条件。

#### 限制

Simulink 软件不允许此模块的初始条件为 `inf` 或 `NaN`。

#### 依赖关系

选择 `internal` 会启用 **Initial condition x** 参数并移除 **X0** 输入端口。

选择 `external` 会禁用 **Initial condition x** 参数并启用 **X0** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`ICSourceX` |
| **类型**：character vector, string |
| **值**：`'internal'` | `'external'` |
| **默认值**：`'internal'` |

### **Initial condition x** — 状态 *x* 的初始条件 `0.0`（默认）| 标量 | 向量 | 矩阵

指定状态 *x* 的初始条件。

#### 限制

Simulink 软件不允许此模块的初始条件为 `inf` 或 `NaN`。

#### 依赖关系

要启用此参数，请将 **Initial condition source x** 设置为 `internal`。

将 **Initial condition source x** 设置为 `external` 会禁用此参数并启用 **X0** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`ICX` |
| **类型**：character vector, string |
| **值**：scalar | vector | matrix |
| **默认值**：`'0.0'` |

### **Limit x** — 限制状态 *x* 的值 `off` | `on`

将模块的状态 *x* 限制在 **Lower limit x** 和 **Upper limit x** 参数之间的值。Second-Order Integrator 模块的默认值为 `off`。Second-Order Integrator Limited 的默认值为 `on`。

- 要将状态 *x* 限制在 **Lower limit x** 和 **Upper limit x** 参数之间的值，请选中此复选框。
- 要移除状态 *x* 的范围限制，请清除此复选框。

#### 依赖关系

选中此复选框会启用 **Upper limit x** 和 **Lower limit x** 参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`LimitX` |
| **类型**：character vector, string |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` (Second-Order Integrator) | `'on'` (Second-Order Integrator Limited) |

### **Upper limit x** — 状态 *x* 的上限 `1` | `inf` | 标量 | 向量 | 矩阵

指定状态 *x* 的上限。Second-Order Integrator 模块的默认值为 `inf`。Second-Order Integrator Limited 模块的默认值为 `1`。

#### 提示

状态 *x* 的上饱和限值必须严格大于下饱和限值。

#### 依赖关系

要启用此参数，请选中 **Limit x** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`UpperLimitX` |
| **类型**：character vector, string |
| **值**：`'1' | 'inf' |` scalar | vector | matrix |
| **默认值**：`'1'` (Second-Order Integrator Limited) | `'inf'` (Second-Order Integrator) |

### **Lower limit x** — 状态 *x* 的下限 `0`（默认）| `-inf` | 标量 | 向量 | 矩阵

指定状态 *x* 的下限。Second-Order Integrator 模块的默认值为 `-inf`。Second-Order Integrator Limited 模块的默认值为 `0`。

#### 提示

状态 *x* 的下饱和限值必须严格小于上饱和限值。

#### 依赖关系

要启用此参数，请选中 **Limit x** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`LowerLimitX` |
| **类型**：character vector, string |
| **值**：`'0' | '-inf' |` scalar | vector | matrix |
| **默认值**：`'0'` (Second-Order Integrator Limited) | `'-inf'` (Second-Order Integrator) |

### **Wrap x** — 启用 x 的环绕 `off`（默认）| `on`

启用 *x* 在 **Wrapped upper value x** 和 **Wrapped lower value x** 参数之间的环绕。启用 *x* 的环绕可消除对零交叉检测的需求，减少求解器重置，提高求解器性能和精度，并在对旋转和循环状态轨迹建模时增加仿真时间跨度。

如果将 **Wrapped upper value x** 指定为 `inf`，将 **Wrapped lower value x** 指定为 `-inf`，则环绕将永远不会发生。

#### 依赖关系

选中此复选框会启用 **Wrapped upper value x** 和 **Wrapped lower value x**。

#### 编程使用

|  |
| --- |
| **模块参数**：`WrapX` |
| **类型**：character vector, string |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` |

### **Wrapped upper value x** — 环绕 x 的上限值 `pi`（默认）| 标量 | 向量 | 矩阵

指定环绕 *x* 的上限值。

#### 依赖关系

要启用此参数，请选中 **Wrap x** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`WrappedUpperValueX` |
| **类型**：character vector, string |
| **值**：scalar | vector | matrix |
| **默认值**：`'pi'` |

### **Wrapped lower value x** — 环绕 x 的下限值 `-pi`（默认）| 标量 | 向量 | 矩阵

指定环绕 *x* 的下限值。

#### 依赖关系

要启用此参数，请选中 **Wrap x** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`WrappedLowerValueX` |
| **类型**：character vector, string |
| **值**：scalar | vector | matrix |
| **默认值**：`'-pi'` |

### **Absolute tolerance x** — 计算状态 *x* 的绝对容差 `auto`（默认）| `-1` | 标量 | 向量

指定计算状态 *x* 的绝对容差。

- 您可以输入 `auto`、–1、正实数标量或向量。
- 如果输入 `auto` 或 –1，Simulink 将使用“配置参数”对话框中的绝对容差值（请参阅 Solver Pane）来计算状态 *x*。
- 如果输入实数标量值，该值将覆盖“配置参数”对话框中的绝对容差，并用于计算所有 *x* 状态。
- 如果输入实数向量，该向量的维度必须与状态 *x* 的维度匹配。这些值将覆盖“配置参数”对话框中的绝对容差。

#### 编程使用

|  |
| --- |
| **模块参数**：`AbsoluteToleranceX` |
| **类型**：character vector, string |
| **值**：`'auto'` | `'-1'` | any positive real scalar or vector |
| **默认值**：`'auto'` |

### **State name x** — 状态 *x* 的名称 `''`（默认）| 字符向量 | 字符串

为状态 *x* 分配唯一名称。

#### 提示

- 要为单个状态分配名称，请在引号之间输入名称，例如 position'。
- 要为多个 *x* 状态分配名称，请在大括号内输入以逗号分隔的列表，例如 {'a', 'b', 'c'}。每个名称必须唯一。
- 状态名称仅适用于所选模块。
- 如果为 *x* 指定状态名称，则还必须为 *dx/dt* 指定状态名称。
- *x* 和 *dx/dt* 的状态名称必须具有相同的类型和长度。
- 状态数必须能被状态名称数整除。您可以指定的名称数少于 *x* 状态数，但不能指定的名称数多于 *x* 状态数。例如，您可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。但是，您必须保持一致，并对 *dx/dt* 的状态名称应用相同的方案。
- 要使用 MATLAB® 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是字符向量、字符串或元胞数组。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateNameX` |
| **类型**：character vector, string |
| **值**：`' '` | user-defined |
| **默认值**：`' '` |

### dx/dt

### **Initial condition source dx/dt** — 状态 *dx/dt* 的初始条件来源 `internal`（默认）| `external`

将状态 *dx/dt* 的初始条件来源指定为 `internal` 或 `external`。

#### 限制

Simulink 软件不允许此模块的初始条件为 `inf` 或 `NaN`。

#### 依赖关系

- 选择 `internal` 会启用 **Initial condition dx/dt** 参数并移除 **dx0** 输入端口。
- 选择 `external` 会禁用 **Initial condition dx/dt** 参数并启用 **dx0** 输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`ICSourceDXDT` |
| **类型**：character vector |
| **值**：`'internal'` | `'external'` |
| **默认值**：`'internal'` |

### **Initial condition dx/dt** — 状态 *dx/dt* 的初始条件 `0.0`（默认）| 标量 | 向量 | 矩阵

指定状态 *dx/dt* 的初始条件。

#### 限制

Simulink 软件不允许此模块的初始条件为 `inf` 或 `NaN`。

#### 依赖关系

- 将 **Initial condition source dx/dt** 设置为 `internal` 会启用此参数。
- 将 **Initial condition source dx/dt** 设置为 `external` 会禁用此参数。

#### 编程使用

|  |
| --- |
| **模块参数**：`ICDXDT` |
| **类型**：character vector |
| **值**：scalar | vector | matrix |
| **默认值**：`'0.0'` |

### **Limit dx/dt** — 限制状态 *dx/dt* 的值 `off` | `on`

将模块的 *dx/dt* 状态限制在 **Lower limit dx/dt** 和 **Upper limit dx/dt** 参数之间的值。Second-Order Integrator 模块的默认值为 `off`。Second-Order Integrator Limited 的默认值为 `on`。

#### 提示

如果为 *x* 设置饱和限值，则由 **Upper limit dx/dt** 和 **Lower limit dx/dt** 定义的区间必须包含零。

#### 依赖关系

选中此复选框会启用 **Upper limit dx/dt** 和 **Lower limit dx/dt** 参数。

#### 编程使用

|  |
| --- |
| **Parameter:** `LimitDXDT` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'off'` (Second-Order Integrator) | `'on'` (Second-Order Integrator Limited) |

### **Upper limit dx/dt** — 状态 *dx/dt* 的上限 `inf`（默认）| 标量 | 向量 | 矩阵

指定状态 *dx/dt* 的上限。

#### 依赖关系

如果限制 *x*，则此参数必须具有严格为正值。

要启用此参数，请选中 **Limit dx/dt** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`UpperLimitDXDT` |
| **类型**：character vector |
| **值**：scalar | vector | matrix |
| **默认值**：`'inf'` |

### **Lower limit dx/dt** — 状态 *dx/dt* 的下限 `-inf`（默认）| 标量 | 向量 | 矩阵

指定状态 *dx/dt* 的下限。

#### 依赖关系

如果限制 *x*，则此参数必须具有严格为负值。

要启用此参数，请选中 **Limit dx/dt** 复选框。

#### 编程使用

|  |
| --- |
| **模块参数**：`LowerLimitDXDT` |
| **类型**：character vector |
| **值**：scalar | vector | matrix |
| **默认值**：`'-inf'` |

### **Absolute tolerance dx/dt** — 计算状态 *dx/dt* 的绝对容差 `auto`（默认）| `-1` | 标量 | 向量

指定计算状态 *dx/dt* 的绝对容差。

- 您可以输入 `auto`、`–1`、正实数标量或向量。
- 如果输入 `auto` 或 `–1`，则 Simulink 将使用“配置参数”对话框中的绝对容差值（请参阅 Solver Pane）来计算模块的 *dx/dt* 输出。
- 如果输入数值，该值将覆盖“配置参数”对话框中的绝对容差。

#### 编程使用

|  |
| --- |
| **模块参数**：`AbsoluteToleranceDXDT` |
| **类型**：character vector, string, scalar, or vector |
| **值**：`'auto'` | `'-1'` | any positive real scalar or vector |
| **默认值**：`'auto'` |

### **State name dx/dt** — 状态 *dx/dt* 的名称 `' '`（默认）| 字符向量 | 字符串

为状态 *dx/dt* 分配唯一名称。

#### 提示

- 要为单个状态分配名称，请在引号之间输入名称，例如 'velocity'。
- 要为多个 *dx/dt* 状态分配名称，请在大括号内输入以逗号分隔的列表，例如 {'a', 'b', 'c'}。每个名称必须唯一。
- 状态名称仅适用于所选模块。
- 如果为 *dx/dt* 指定状态名称，则还必须为 *x* 指定状态名称。
- *x* 和 *dx/dt* 的状态名称必须具有相同的类型和长度。
- 状态数必须能被状态名称数整除。您可以指定的名称数少于 *dx/dt* 状态数，但不能指定的名称数多于 *dx/dt* 状态数。例如，您可以在具有四个状态的系统中指定两个名称。第一个名称应用于前两个状态，第二个名称应用于后两个状态。但是，您必须保持一致，并对 *x* 的状态名称应用相同的方案。
- 要使用 MATLAB 工作区中的变量分配状态名称，请输入不带引号的变量。变量可以是字符向量、字符串或元胞数组。

#### 编程使用

|  |
| --- |
| **模块参数**：`StateNameDXDT` |
| **类型**：character vector, string |
| **值**：`' '` | user-defined |
| **默认值**：`' '` |

### 属性

### **External reset** — 将状态重置为初始条件 `none`（默认）| `rising` | `falling` | `either`

当重置信号中发生触发事件时，将状态重置为初始条件。

- `none` — 不将状态重置为初始条件。
- `rising` — 当重置信号从零上升到正值或从负值上升到正值时，重置状态。
- `falling` — 当重置信号从正值下降到零或从正值下降到负值时，重置状态。
- `either` — 当重置信号从零变为非零值或改变符号时，重置状态。

#### 编程使用

|  |
| --- |
| **模块参数**：`ExternalReset` |
| **类型**：character vector, string |
| **值**：`'none'` | `'rising'` | `'falling'` | `'either'` |
| **默认值**：`'none'` |

### **Enable zero-crossing detection** — 启用零交叉检测 `on`（默认）| `off`

选择以启用零交叉检测。有关详细信息，请参阅 Zero-Crossing Detection。

#### 编程用法

|  |
| --- |
| **参数：** `ZeroCross` |
| **类型：** 字符向量、字符串 |
| **值：** `'on'` | `'off'` |
| **默认值：** `'on'` |

### **当 x 达到饱和时重新初始化 dx/dt** — 当 *x* 达到饱和时重置 *dx/dt* `off`（默认）| `on`

在状态 *x* 达到饱和的瞬间，将 *dx/dt* 重置为其当前初始条件。

#### 提示

*dx/dt* 初始条件的值必须使 *x* 能够立即离开饱和状态。否则，Simulink 将忽略 *dx/dt* 的初始条件，以保持模块状态的数学一致性。

#### 编程用法

|  |
| --- |
| **模块参数：** `ReinitDXDTwhenXreachesSaturation` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **线性化时忽略状态限值和重置** — 线性化时忽略状态限值和外部重置 `off`（默认）| `on`

出于线性化目的，让 Simulink 忽略指定的状态限值和外部重置。

#### 编程用法

|  |
| --- |
| **模块参数：** `IgnoreStateLimitsAndResetForLinearization` |
| **类型：** 字符向量、字符串 |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **显示输出** — 要显示的输出端口 `both`（默认）| `x` | `dxdt`

指定模块上的输出端口。

- `both` — 同时显示 *x* 和 *dx/dt* 输出端口。
- `x` — 仅显示 *x* 输出端口。
- `dx/dt` — 仅显示 *dx/dt* 输出端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `ShowOutput` |
| **类型：** 字符向量、字符串 |
| **值：** `'both'` | `'x'` | `'dxdt'` |
| **默认值：** `'both'` |
## 所属库

Simulink / Continuous

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` |
| **多维信号** | `No` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产级代码。这与嵌入式系统中常见的资源限制以及速度和内存限制有关。生成的代码可能包含动态内存分配和释放、递归、额外的内存开销以及变化很大的执行时间。虽然代码在功能上是有效的，并且在资源丰富的环境中通常可以接受，但较小的嵌入式目标通常无法支持此类代码。

通常，请考虑使用 Simulink Model Discretizer 将连续模块映射为支持生产代码生成的离散等效模块。要启动 Model Discretizer，请在 Simulink Editor 的 **Apps** 选项卡中，在 **Apps** 下、**Control Systems** 下，点击 **Model Discretizer**。一个例外是 Second-Order Integrator 模块，因为对于该模块，Model Discretizer 会生成近似离散化。

## 版本历史

**在 R2010a 中引入**

## 描述

输入信号的二阶积分

Second-Order Integrator 模块和 Second-Order Integrator Limited 模块求解二阶初值问题：

d2xdt2=u,dxdt|t=0=dxo,x|t=0=xo,

其中 *u* 是系统输入。因此，该模块是一个具有两个连续状态 *x* 和 *dx/dt* 的动态系统。

**注意**

这两个状态具有数学关系，即 *dx/dt* 是 *x* 的导数。为了在整个仿真过程中满足这种关系，Simulink 对模块参数和行为施加了各种约束。

Second-Order Integrator Limited 模块与 Second-Order Integrator 模块相同，不同之处在于它默认根据指定的上限和下限限制状态。有关详细信息，请参阅限制状态。

Simulink® 软件可以使用多种不同的数值积分方法来计算模块的输出。每种方法对特定应用都有优势。使用 Configuration Parameters 对话框的 **Solver** 窗格选择最适合您应用的技术。（有关详细信息，请参阅 Solver Selection Criteria。）所选求解器使用当前输入值计算当前时间步的 Second-Order Integrator 模块状态。

使用模块参数对话框可以：

- 指定每个状态初始条件的来源是内部还是外部
- 为状态初始条件指定值
- 为任一状态或两个状态定义上限和下限
- 为每个状态指定绝对容差
- 为两个状态指定名称
- 选择外部重置条件
- 启用零交叉检测
- 当 x 达到饱和时重新初始化 dx/dt
- 指定 Simulink 在线性化操作中忽略状态限值和外部重置

### 定义初始条件

您可以在模块对话框上将每个状态的初始条件分别定义为参数，也可以从外部信号输入其中一个或两个初始条件。

- 要将状态 *x* 的初始条件定义为模块参数，请使用 **Initial condition source x** 下拉菜单选择 `internal`，并在 **Initial condition x** 字段中输入值。
- 要从外部源为状态 *x* 提供初始条件，请将 **Initial condition source x** 参数指定为 `external`。模块上会出现一个附加输入端口。
- 要将状态 *dx/dt* 的初始条件定义为模块参数，请使用 **Initial condition source dx/dt** 下拉菜单选择 `internal`，并在 **Initial condition dx/dt** 字段中输入值。
- 要从外部源为状态 *dx/dt* 提供初始条件，请将 **Initial condition source dx/dt** 指定为 `external`。模块上会出现一个附加输入端口。

如果您选择为两个状态初始条件都使用外部源，则模块如下所示。

**注意**

- Simulink 不允许初始条件值为 `inf` 或 `NaN`。
- 如果您通过指定饱和限值来限制状态 *x* 或状态 *dx/dt*（请参阅限制状态），并且一个或多个初始条件超出相应限值，则相应状态会初始化为最接近的有效值，并计算一组一致的初始条件。

### 限制状态

在对二阶系统建模时，您可能需要限制模块状态。例如，活塞在气缸内的运动由牛顿第二定律支配，并且对活塞位置（*x*）有约束。使用 Second-Order Integrator 模块，您可以彼此独立地限制状态 *x* 和 *dx/dt*。您甚至可以在仿真期间更改限值；但是，您不能更改状态是否受限。需要遵循的一条重要规则是，上限必须严格大于其对应的下限。

当您限制一个或两个状态时，模块外观会发生变化。当两个状态都受限时，模块如下所示。

对于每个状态，您可以使用模块参数对话框设置适当的饱和限值。

### 仅限制 *x*

如果您使用 Second-Order Integrator Limited 模块，则默认情况下两个状态都受限。但您也可以在 Second-Order Integrator 模块上通过选择 **Limit x** 并在相应的参数字段中输入限值来手动限制状态 *x*。

然后，模块按如下方式确定状态值：

- 当 *x* 小于或等于其下限时，*x* 的值保持在其下限，且 *dx/dt* 设置为零。
- 当 *x* 位于其下限和上限之间时，两个状态都遵循二阶 ODE 给出的轨迹。
- 当 *x* 大于或等于其上限时，*x* 的值保持在其上限，且 *dx/dt* 设置为零。

您可以选择在 *x* 达到饱和时将 *dx/dt* 重新初始化为新值。请参阅当 x 达到饱和时重新初始化 dx/dt。

### 仅限制 *dx/dt*

与状态 *x* 一样，在 Second-Order Integrator Limited 模块对话框的 **dx/dt** 窗格上，状态 *dx/dt* 默认设置为受限。您可以在 Second-Order Integrator 模块上手动设置此参数 **Limit dx/dt**。无论哪种情况，都必须为 *dx/dt* 输入适当的限值。

如果您仅限制状态 *dx/dt*，则模块按如下方式确定 *dx/dt* 的值：

- 当 *dx/dt* 小于或等于其下限时，*dx/dt* 的值保持在其下限。
- 当 *dx/dt* 位于其下限和上限之间时，两个状态都遵循二阶 ODE 给出的轨迹。
- 当 *dx/dt* 大于或等于其上限时，*dx/dt* 的值保持在其上限。

当状态 *dx/dt* 保持在其上限或下限时，*x* 的值由一阶初值问题决定：

dxdt=L,x(tL)=xL,

其中 *L* 是 *dx/dt* 限值（上限或下限），*t**L* 是 *dx/dt* 达到此限值的时间，*x**L* 是该时刻状态 *x* 的值。

### 同时限制两个状态

当您同时限制两个状态时，Simulink 通过限制 *dx/dt* 上限和下限的允许值来保持状态的数学一致性。此类限制对于满足以下约束是必要的：

- 当 *x* 处于其饱和限值时，*dx/dt* 的值必须为零。
- 为了使 *x* 离开上限，*dx/dt* 的值必须严格为负。
- 为了使 *x* 离开其下限，*dx/dt* 的值必须严格为正。

对于此类情况，*dx/dt* 的上限必须严格为正，*dx/dt* 的下限必须严格为负。

当两个状态都受限时，模块按如下方式确定状态：

- 每当 *x* 达到其限值时，产生的行为与“仅限制 x”中所述相同。
- 每当 *dx/dt* 达到其限值之一时，产生的行为与“仅限制 dx/dt”中所述相同——包括当 *dx/dt* 保持在其限值之一时使用一阶 ODE 计算 *x*。在这种情况下，当 *x* 达到其限值之一时，它会保持在该限值，且 *dx/dt* 设置为零。
- 每当两者同时达到各自的限值时，状态 *x* 的行为优先于 *dx/dt* 的行为，以保持状态的一致性。

当您同时限制两个状态时，您可以选择在状态 *x* 达到饱和时重新初始化 *dx/dt*。如果重新初始化后的值超出 *dx/dt* 的指定限值，则 *dx/dt* 会重新初始化为最接近的有效值，并计算一组一致的初始条件。请参阅当 x 达到饱和时重新初始化 dx/dt

### 重置状态

模块可以根据外部信号将其状态重置为指定的初始条件。要使模块重置其状态，请在 **Attributes** 窗格上选择 **External reset** 选项之一。触发端口会出现在模块上其输入端口下方，并指示触发类型。

- 选择 `rising` 以在重置信号从零上升到正值、从负值上升到正值或从负值上升到零时重置状态。
- 选择 `falling` 以在重置信号从正值下降到零、从正值下降到负值或从零下降到负值时重置状态。
- 选择 `either` 以在重置信号从零变为非零值或改变符号时重置状态。

重置端口具有直接馈通。如果模块输出直接或通过一系列具有直接馈通的模块反馈到此端口，则会产生代数环（请参阅 Algebraic Loop Concepts）。

### 启用零交叉检测

此参数控制是否为此模块启用零交叉检测。默认情况下，在 **Attributes** 窗格上选中 **Enable zero-crossing detection** 参数。但是，仅当 Configuration Parameters 对话框的 **Solver** 窗格上的 **Zero-crossing control** 设置为 `Use local settings` 时，此参数才生效。有关详细信息，请参阅 Zero-Crossing Detection。

### 当 *x* 达到饱和时重新初始化 *dx/dt*

对于某些建模应用，当状态 *x* 达到其限值时，必须重新初始化 *dx/dt*，以便立即将 *x* 拉出饱和状态。您可以通过在 **Attributes** 窗格上选择 **Reinitialize dx/dt when x reaches saturation** 来实现这一点。

如果此选项开启，则在 *x* 达到饱和的瞬间，Simulink 会检查 *dx/dt* 初始条件（参数或信号）的当前值是否允许状态 *x* 立即离开饱和状态。如果允许，Simulink 会在该瞬间使用初始条件（参数或信号）的值重新初始化状态 *dx/dt*。如果不允许，Simulink 会在当前瞬间忽略此参数，并将 *dx/dt* 设置为零，以使模块状态一致。

此参数仅在 *x* 实际达到饱和限值时适用。它不适用于 *x* 保持饱和状态的任何未来时间。

有关更多信息，请参阅限制状态的相关章节。有关示例，请参阅 Simulation of Bouncing Ball。

### 线性化时忽略状态限值和外部重置

对于通过线性化简化模型的情况，您可以通过选择 **Ignore state limits and the reset for linearization** 让 Simulink 忽略状态限值和外部重置。

### 指定模块输出的绝对容差

默认情况下，Simulink 软件使用 Configuration Parameters 对话框中指定的绝对容差值（请参阅 Error Tolerances for Variable-Step Solvers）来计算积分器模块的输出。如果此值不能提供足够的误差控制，请在参数对话框的 **Absolute tolerance x** 字段中为状态 *x* 指定更合适的值，并在 **Absolute tolerance dx/dt** 字段中为状态 *dx/dt* 指定更合适的值。Simulink 使用您指定的值来计算模块的状态值。

### 指定输出端口的显示

您可以使用 `ShowOutput` 参数控制是显示 *x* 输出端口还是 *dx/dt* 输出端口。您可以显示一个输出端口或两个输出端口；但是，您必须至少选择一个。

### 指定状态名称

您可以使用 `StateNameX` 和 `StateNameDXDT` 参数指定 *x* 状态和 *dx/dt* 状态的名称。但是，您必须为两者都指定名称，或者都不指定；不能只为 *x* 或只为 *dx/dt* 指定名称。两个状态名称必须具有相同的类型和长度。此外，名称数量必须能够整除状态数量。

### 选择所有选项

当您选择所有选项时，模块图标如下所示。
