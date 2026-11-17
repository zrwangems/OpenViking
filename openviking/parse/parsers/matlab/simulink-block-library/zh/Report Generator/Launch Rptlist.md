---
type: simulink-block
title: 'rptlist'
family: 'report-generator'
product_id: 'report-generator'
product_name: 'Report Generator'
documentation_release: R2025b
official_category: ''
documentation_page: 'rptlist'
documentation_source_path: '../rptgen/ug/rptlist.html'
language: zh-CN
chinese_source: official
---

# rptlist

检索 MATLAB 路径上的报告设置文件列表

本页采用了机器翻译。点击此处可查看英文原文。

检索 MATLAB 路径上的报告设置文件列表

## 语法

`rptlist`

`setupFileList = rptlist`

`rptlist(simulinkModel)`

## 说明

`rptlist` 打开报告资源管理器作为活动窗口，并在报告资源管理器的**库**窗格中显示 MATLAB® 路径上可用的报告设置文件列表。

`setupFileList = rptlist` 返回 MATLAB 路径上可用的报告设置文件列表。

`rptlist(simulinkModel)` 打开报告资源管理器作为活动窗口，并在报告资源管理器的**库**窗格中选择与指定 Simulink® 模型相关联的报告设置文件。

**注意**

- 仅当您安装了 Simulink Report Generator™ 后才可以使用此语法。
- 在使用此语法之前，请先加载 Simulink 模型。

## 输入参数

### `simulinkModel` — 与报告设置文件关联的 Simulink 模型的名称 字符向量 | 字符串标量

与报告设置文件关联的 Simulink 模型的名称，指定为字符向量或字符串标量。

要查看哪个报告设置文件与模型相关联，请检查该模型的 `ReportName` 属性的值。例如：

```
model_name = "myModel";
load_system(model_name);
model_report_name = get_param(model_name,"ReportName")
ans =
    'modelRptFile.rpt'
```

要将报告设置文件与模型关联，请将 `ReportName` 属性的值设置为报告设置文件的名称。例如：

```
model_name = "myModel";
new_rpt_file_name = "modelRptFile.rpt";
load_system(model_name);
set_param(model_name,"ReportName",new_rpt_file_name);
```

**注意**

报告设置文件名必须包含 `.rpt` 文件扩展名。

默认情况下，所有模型都与 `simulink-default.rpt` 相关联，这是一个报告设置文件，为当前 Simulink 系统生成报告。

## 版本历史记录

**在 R2006a 之前推出**

## 另请参阅

`setedit` | `report`

### 主题

- 使用报告资源管理器

## MATLAB Command

You clicked a link that corresponds to this MATLAB command:

Run the command by entering it in the MATLAB Command Window.
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

选择网站

选择网站以获取翻译的可用内容，以及查看当地活动和优惠。根据您的位置，我们建议您选择：。

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

您也可以从以下列表中选择网站：

**如何获得最佳网站性能**

选择中国网站（中文或英文）以获得最佳网站性能。其他 MathWorks 国家/地区网站并未针对您所在位置的访问进行优化。

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

亚太

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

联系您当地的办事处
