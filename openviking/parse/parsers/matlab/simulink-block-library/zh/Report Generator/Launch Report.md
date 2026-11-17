---
type: simulink-block
title: 'report'
family: 'report-generator'
product_id: 'report-generator'
product_name: 'Report Generator'
documentation_release: R2025b
official_category: ''
documentation_page: 'report'
documentation_source_path: '../rptgen/ug/report.html'
language: zh-CN
chinese_source: official
---

# report

从报告资源管理器设置文件生成报告

本页采用了机器翻译。点击此处可查看英文原文。

从报告资源管理器设置文件生成报告

## 语法

`report`

`[rptFile1,...,rptFileN] = report(setup1,...,setupN)`

`rptFile = report(simulinkModel)`

`[___] = report(___,outFormat)`

`[___] = report(___,outFormat,formatTemplate)`

`[___] = report(___,outFormat,formatStyleSheet)`

`[___] = report(___,targetFolder)`

`[___] = report(___,targetFile)`

`[___] = report(___,genOpt1,...,genOptN)`

## 说明

`report` 打开报告资源管理器作为活动窗口。

`[rptFile1,...,rptFileN] = report(setup1,...,setupN)` 从指定的报告设置文件生成报告并返回生成的报告文件的完整路径。该函数根据报告设置文件的配置生成报告。

`rptFile = report(simulinkModel)` 根据与指定 Simulink® 模型关联的报告设置文件生成报告。

**注意**

- 仅当您安装了 Simulink Report Generator™ 后才可以使用此语法。
- 在使用此语法之前，请先加载 Simulink 模型。

示例

`[___] = report(___,outFormat)` 以指定的格式生成报告。

`[___] = report(___,outFormat,formatTemplate)` 使用 `outFormat` 指定的模板生成报告。

示例

`[___] = report(___,outFormat,formatStyleSheet)` 使用 `outFormat` 指定的样式表生成报告。

示例

`[___] = report(___,targetFolder)` 在指定文件夹中创建生成的报告文件。

示例

`[___] = report(___,targetFile)` 指定生成的报告文件的目标根名称。

示例

`[___] = report(___,genOpt1,...,genOptN)` 在生成报告时使用一个或多个选项。

## 示例

### 使用报告资源管理器同时生成多个报告

打开实时脚本

使用变量来存储报告设置文件的名称。

```
rpt_file_1 = "first_rpt.rpt";
rpt_file_2 = "second_rpt.rpt";
rpt_file_3 = "third_rpt.rpt";
```

定义生成的报告的文件夹并将路径存储在变量 `generated_reports_folder` 中。在末尾包含反斜杠 (`\`)，以便 `report` 函数将路径识别为文件夹而不是根文件名。

```
generated_reports_folder = "generated_reports\"
```

```
generated_reports_folder =
"generated_reports\"
```

在变量 `report` 中定义 `out_path_param` 函数的输出路径参量。

```
out_path_param = "-o"+generated_reports_folder
```

```
out_path_param =
"-ogenerated_reports\"
```

使用 `report` 函数一次即可生成并查看所有三个设置文件的报告。使用 `out_path_param` 变量指定生成报告的文件夹。指定生成的报告类型为 `dom-pdf` 格式和 `default-rg-docx-numbered` 模板。

该函数生成并打开临时 DOCX 文件，并将 DOCX 文件转换为 PDF 文件。如果您收到 Microsoft ® Word 弹出警告，要求您允许文档更新字段，点击**是**。

将生成的报告文件的路径存储在字符串数组 `report_file_paths` 中，并显示文件的名称。

```
[report_file_paths(1),report_file_paths(2),report_file_paths(3)] = ...
              report(rpt_file_1,rpt_file_2,rpt_file_3,...
                    "-fdom-pdf","-sdefault-rg-docx-numbered",out_path_param);
```

```
    Beginning report
    Converting report
Document conversion failed. Generating a PDF report from a template supported only on Windows platforms.
Error running report
Generating a PDF report from a template supported only on Windows platforms.
    Beginning report
    Converting report
Document conversion failed. Generating a PDF report from a template supported only on Windows platforms.
Error running report
Generating a PDF report from a template supported only on Windows platforms.
    Beginning report
    Converting report
Document conversion failed. Generating a PDF report from a template supported only on Windows platforms.
Error running report
Generating a PDF report from a template supported only on Windows platforms.
```

```
[~,generated_report_names] = fileparts(report_file_paths);
disp(generated_report_names');
```

```
    ""
    ""
    ""
```

### 使用报告浏览器报告 Simulink 模型

此示例使用:

- Simulink Report GeneratorSimulink Report Generator

打开实时脚本

此示例显示如何使用报告资源管理器来报告 Simulink 模型。您必须安装 Simulink Report Generator 才能运行此示例。

加载模型并检查哪个报告设置文件与该模型相关联。

```
model_name = "simple_model";
load_system(model_name);
model_report_name = get_param(model_name,"ReportName")
```

```
model_report_name =
'simple_RPT.rpt'
```

使用 `report` 函数在当前目录中以 `reportOnSimpleModel` 格式生成名为 `dom-pdf-direct` 的报告。使用 `-graphical` 选项启动报告资源管理器的消息列表对话框。

将生成的报告文件的路径存储在变量 `generated_report_path` 中，并显示文件名和扩展名。

```
generated_report_path = report(model_name,"-fdom-pdf-direct","-oreportOnSimpleModel","-graphical");
[~,generated_report_name,generated_report_extension] = fileparts(generated_report_path)
```

```
generated_report_name =
"reportOnSimpleModel"
```

```
generated_report_extension =
".pdf"
```

### 生成多个报告时避免文件覆盖

打开实时脚本

此示例显示如何在生成具有相同根名称的多个报告时避免覆盖。

**配置报告设置文件**

使用变量来存储报告设置文件的名称。

```
rpt_file_1 = "my_first_rpt.rpt";
rpt_file_2 = "my_second_rpt.rpt";
rpt_file_3 = "my_third_rpt.rpt";
```

使用函数 `setedit` 在报告资源管理器中打开报告设置文件。确保为所有三个文件选中**如果报告已存在，则增加以防止覆盖**复选框。

```
setedit(rpt_file_1);
setedit(rpt_file_2);
setedit(rpt_file_3);
```

**生成报告**

定义生成报告的基本路径。

```
base_report_path = fullfile("","generated_reports","myGeneratedReport")
```

```
base_report_path =
"generated_reports/myGeneratedReport"
```

在变量 `report` 中定义 `out_path_param` 函数的输出路径参量。该函数为每个报告的 `base_report_path` 追加不同的编号，并生成具有不同名称的报告文件。

```
out_path_param = "-o"+base_report_path
```

```
out_path_param =
"-ogenerated_reports/myGeneratedReport"
```

使用 `report` 函数可以同时生成并查看三个设置文件的报告。使用 `out_path_param` 参数指定生成的报告的根名称。指定生成的报告类型为 `pdf-fop` 格式，并带有 `fo-YesChapterNumbers` 样式表。将生成的报告文件的路径存储在字符串数组 `report_file_paths` 中，并显示文件的名称。请注意，由于选择了增量以防止覆盖选项，因此生成的报告文件具有不同的名称。

```
[report_file_paths(1),report_file_paths(2),report_file_paths(3)] = ...
      report(rpt_file_1,rpt_file_2,rpt_file_3,...
                "-fpdf-fop","-sfo-YesChapterNumbers",out_path_param);
```

```
    Beginning report
    Converting report
    Report complete
    Beginning report
    Converting report
    Report complete
    Beginning report
    Converting report
    Report complete
```

```
[~,generated_report_names] = fileparts(report_file_paths);
disp(generated_report_names');
```

```
    "myGeneratedReport0"
    "myGeneratedReport1"
    "myGeneratedReport2"
```

## 输入参数

### `setup1,...,setupN` — 报告设置文件的名称 字符向量 | 字符串标量

用于生成报告的报告设置文件的名称，指定为字符串标量或字符向量。

### `simulinkModel` — 与报告设置文件关联的 Simulink 模型的名称 字符向量 | 字符串标量

与用于生成报告的报告设置文件关联的 Simulink 模型的名称，指定为字符向量或字符串标量。

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

### `outFormat` — 输出报告格式 字符向量 | 字符串标量

输出报告格式，指定为 `-fFORMAT` 形式的字符向量或字符串标量，其中 `FORMAT` 是有效的格式值。

要获取 DOM 格式列表，请使用：

```
rptconvert("-domformatlist")
```

要获取旧式非 DOM 格式的列表，请使用：

```
rptconvert("-formatlist")
```

### `formatTemplate` — 输出格式模板 字符向量 | 字符串标量

用于生成报告的 `outFormat` 模板，指定为 `-sTEMPLATE` 形式的字符向量或字符串标量，其中 `TEMPLATE` 是 `outFormat` 格式的有效模板。旧格式没有模板。所有 DOM 格式都有模板。要查看 `outFormat` 格式的有效模板列表（可以是任何有效的 DOM 格式），请输入以下命令：

```
rptconvert("-templatelist",outFormat)
```

### `formatStyleSheet` — 输出格式的样式表 字符向量 | 字符串标量

用于生成报告的 `outFormat` 样式表，指定为 `-sSTYLE_SHEET` 形式的字符向量或字符串标量，其中 `STYLE_SHEET` 是 `outFormat` 格式的有效样式表。DOM 格式没有样式表。除 `db` 之外的所有非 DOM 格式都有样式表。要查看 `outFormat` 格式的有效样式表列表（可以是除 `db` 之外的任何有效的非 DOM 格式），请输入以下命令：

```
rptconvert("-stylesheetlist",outFormat)
```

### `targetFile` — 创建报告文件的基本目标文件名 字符向量 | 字符串标量

创建的报告文件的基本目标文件名，指定为 `-oNAME` 形式的字符向量或字符串标量，其中 `NAME` 是要创建的文件的基本名称或路径。

**注意**

将 `targetFile` 指定为单个基本名称或路径。为了防止该函数尝试生成具有相同名称的多个报告文件，当将此语法与多个报告设置文件一起使用时，请在报告资源管理器的**大纲**窗格中选择每个报告设置文件，并在**属性**窗格中确保选中**如果报告已存在，则递增报告编号以防止覆盖**复选框。然后，该函数通过在基本文件名或路径后追加不同的数字来创建具有不同名称的每个报告文件。

Report setup file is selected and the check box is selected

### `targetFolder` — 创建报告文件的目标文件夹 字符向量 | 字符串标量

创建报告文件的目标文件夹，指定为 `-oPATH` 形式的字符向量或字符串标量，其中 `PATH` 是相对路径或完整路径。

**注意**

`PATH` 必须以斜杠 (`/`) 或反斜杠 (`\`) 结尾。

### `genOpt1,...,genOptN` — 生成报告的选项 `"-noview"` | `"-graphical"` | `"-debug"` | `"-quiet"`

生成报告的选项，指定为：

| 值 | 描述 |
| --- | --- |
| `"-noview"` | 不打开生成的报告进行查看 |
| `"-graphical"` | 在报告资源管理器中加载报告设置文件，并在生成报告之前启动消息列表对话框。报告生成后，报告资源管理器中未加载的设置文件将被卸载。 |
| `"-debug"` | 在 MATLAB® 命令行中输出调试信息。 |
| `"-quiet"` | 抑制命令行输出。与 `-debug` 选项一起使用时，此选项将被忽略。 |

## 输出参量

### `rptFile1,...,rptFileN` — 生成的报告文件的完整路径 字符串标量

生成的报告文件的完整路径，以一个或多个字符串标量的形式返回，每个生成的报告文件一个。

## 版本历史记录

**在 R2006a 之前推出**

## 另请参阅

`setedit` | `rptconvert` | `rptlist` | `compwiz`

### 主题

- 生成报告
- 报告输出格式
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
