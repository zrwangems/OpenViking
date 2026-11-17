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
language: en
---

# rptlist

Retrieve list of report setup files on the MATLAB path

Retrieve list of report setup files on the MATLAB path

## Syntax

`rptlist`

`setupFileList = rptlist`

`rptlist(simulinkModel)`

## Description

`rptlist` opens the Report Explorer as the active window
and displays the list of report setup files available on the MATLAB® path, in the **Library** pane of the Report
Explorer.

`setupFileList = rptlist` returns
the list of report setup files available on the MATLAB path.

`rptlist(simulinkModel)` opens the
Report Explorer as the active window and selects the report setup file
associated with the specified Simulink® model in the **Library** pane of the Report
Explorer.

**Note**

- You can use this syntax only if you have Simulink
  Report Generator™ installed.
- Load the Simulink model before using this syntax.

## Input Arguments

### `simulinkModel` — Name of Simulink model associated with report setup file character vector | string scalar

Name of Simulink model associated with report setup file, specified as a character vector or string scalar.

To see which report setup file is associated with a model, check the value of the
`ReportName` property of the model. For example:

```
model_name = "myModel";
load_system(model_name);
model_report_name = get_param(model_name,"ReportName")
ans =
    'modelRptFile.rpt'
```

To
associate a report setup file with a model, set the value of the
`ReportName` property to the name of the report setup file. For example:

```
model_name = "myModel";
new_rpt_file_name = "modelRptFile.rpt";
load_system(model_name);
set_param(model_name,"ReportName",new_rpt_file_name);
```

**Note**

The report setup file name must include the `.rpt` file
extension.

By default, all models are associated with `simulink-default.rpt`,
which is a report setup file that generates a report for the current Simulink system.

## Version History

**Introduced before R2006a**

## See Also

`setedit` | `report`

### Topics

- Working with Report Explorer

## MATLAB Command

You clicked a link that corresponds to this MATLAB command:

Run the command by entering it in the MATLAB Command Window.
Web browsers do not support MATLAB commands.

Close

MathWorks
MathWorks

Select a Web Site

Choose a web site to get translated content where available and see local events and offers. Based on your location, we recommend that you select: .

- (English)
- (Deutsch)
- (Français)

- （简体中文）
- (English)

You can also select a web site from the following list

**How to Get Best Site Performance**

Select the China site (in Chinese or English) for best site performance. Other MathWorks country sites are not optimized for visits from your location.

Americas

- América Latina (Español)
- Canada (English)
- United States (English)

Europe

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

Asia Pacific

- Australia (English)
- India (English)
- New Zealand (English)
- 中国
  - 简体中文
  - English
- 日本 (日本語)
- 한국 (한국어)

Contact your local office
