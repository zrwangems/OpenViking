---
type: simulink-block
title: 'SimEvents Common Design Patterns'
family: 'simevents'
product_id: 'simevents'
product_name: 'SimEvents'
documentation_release: R2025b
official_category: ''
documentation_page: 'common-design-patterns'
documentation_source_path: 'gs/common-design-patterns.html'
language: zh-CN
chinese_source: worker-translation
---

# SimEvents Common Design Patterns

SimEvents ® 库提供了可供您在建模时参考的设计模式。要访问这些模式，请打开 SimEvents 库并双击 Design Patterns 模块。

SimEvents® 库提供了可供您在建模时参考的设计模式。要访问这些模式，请打开 SimEvents 库并双击 Design Patterns 模块。

库中提供的 SimEvents 自定义设计模式

建模时请考虑以下设计模式：

| 设计模式 | 描述 | 输入规格 | 输出规格 | 应用 |
| --- | --- | --- | --- | --- |
| 具有指数随机生成间隔的实体 | 以指数分布方式生成具有随机生成间隔的实体。 | 不适用 | 具有指定属性的结构化实体 | 建模：  - 进入商店的顾客 - 热线的来电 |
| 来自随机分布的服务时间 | 将 Entity Server 中的等待时间指定为从 0 到 1 均匀分布的随机数。 | 任意实体类型 | 继承自输入 | 建模：  - 在某个范围内随机的事件的扩展   （例如，通话时长 - 有意将实体保持随机  时间 |
| 将实体属性提取为信号 | 将一个或多个实体属性提取为信号。 | 具有指定属性的结构化实体或总线对象 | `getAttribute` — 实数双精度标量信号  提取的属性 — 继承自输入 | 检查或使用特定实体属性 |
| 在生成时对实体加时间戳 | 生成具有属性 **TimeStamp** 的实体，该属性记录生成时的仿真时间。 | 不适用 | 具有属性 `Data` 和 `TimeStamp` 的结构化实体 | 当需要实体的生成时间时使用，例如，在组合调度算法中计算优先级时。 |
| 在信号值变化时释放实体 | 当阶跃函数发生跳变时释放传入实体。 | 任意实体类型 | 继承自输入 | 用于基于函数的变化控制实体的通过。 |
| 在服务完成时打开门 | 服务完成后，门打开并释放一个实体。 | 任意实体类型 | 继承自输入 | 使用任务完成来触发实体处理。 |
| 感测实体从 A 传递到 B 并打开门 | 将实体从 *A* 传递到 *B* 会打开门并释放一个实体。 | 任意实体类型 | 继承自输入 | 用于对一个路由中实体的传递进行建模，以控制另一个路由的通过。 |
| 选择具有匹配属性的实体 | 选择要推进的实体，其指定属性与控制端口处的匿名实体匹配 | 具有指定属性的结构化实体或总线对象 | 继承自输入 | 选择具有指定属性的实体进行输出 |
| 离散事件图表：带暂停的单服务器 | 一条 Ctrl 消息触发传入实体的服务暂停。第二条 Ctrl 消息继续服务。实体数据传达服务时间。 | Ctrl — 指定暂停和恢复的匿名实体  实体 — 指定服务时间的匿名实体 | 继承自输入 | 使用外部事件或信号暂停实体的服务。 |
| 离散事件图表：带超时的单服务器 | 如果服务时间（随机）超过实体数据指定的超时限制，则实体离开服务器。 | 具有指定超时限制的匿名实体 | 继承自输入 | 建模：  - 明确要求超时的协议。 - 对超过时间限制的实体实现特殊路由或其他  处理。 - 表示易腐物品的实体。 |
| 离散事件图表：自定义输出开关 | 将实体随机路由到三个输出端口之一。 | 匿名实体 | 继承自输入 | 为输出开关实现更复杂的路由算法。 |
| MATLAB 离散事件系统：自定义生成器 | 使用 MATLAB Discrete Event System 模块定义的 Custom Generator 模块是一个基本实体生成器。该生成器模块需要指定生成周期。 | 不适用 | 匿名实体 | 实现更复杂的实体生成器。 |
| MATLAB 离散事件系统：自定义服务器 | 使用 MATLAB Discrete Event System 模块定义的 Custom Server 模块是一个基本实体服务器。该服务器模块需要指定服务器数量和服务时间。 | 任意实体类型 | 继承自输入 | 实现更复杂的实体服务器。 |
| MATLAB 离散事件系统：选择队列 | 使用 MATLAB Discrete Event System 模块定义的 Selection Queue 模块存储到达 IN 端口的 `passenger` 总线类型实体。来自 call 端口的键选择具有匹配 `trainNum` 字段的 `passenger` 实体，并将它们发送到 OUT 端口。 | Key — 携带选择键的匿名实体  IN — 具有指定属性的结构化实体或总线对象 | 继承自 IN | 从队列中选择特定实体进行输出。 |

## 另请参阅

MATLAB Discrete-Event System | Discrete-Event Chart

### 主题

- 模块创作
- 离散事件系统对象
- 使用图表实现离散事件系统

## MATLAB 命令

您点击了一个对应于以下 MATLAB 命令的链接：

在 MATLAB 命令窗口中输入该命令以运行它。
Web 浏览器不支持 MATLAB 命令。

关闭

MathWorks
MathWorks

选择网站

选择网站以获取翻译后的内容（如果可用），并查看本地活动和优惠。根据您的位置，我们建议您选择：.

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您还可以从以下列表中选择网站

**如何获得最佳网站性能**

选择中国网站（中文或英文）以获得最佳网站性能。其他 MathWorks 国家/地区网站未针对您所在位置的访问进行优化。

美洲

- América Latina (Español)
- Canada (English)
- United States (English)

欧洲

- Belgium (English)
- Denmark (English)
- Deutschland (Deutsch)
- España (Español)
- Finland (English)
- France (Français)
- Ireland (English)
- Italia (Italiano)
- Luxembourg (English)

- Netherlands (English)
- Norway (English)
- Österreich (Deutsch)
- Portugal (English)
- Sweden (English)
- Switzerland
  - Deutsch
  - English
  - Français
- United Kingdom (English)

亚太地区

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

联系您当地的办事处
