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
language: en
---

# report

Generate reports from Report Explorer setup files

Generate reports from Report Explorer setup files

## Syntax

`report`

`[rptFile1,...,rptFileN] = report(setup1,...,setupN)`

`rptFile = report(simulinkModel)`

`[___] = report(___,outFormat)`

`[___] = report(___,outFormat,formatTemplate)`

`[___] = report(___,outFormat,formatStyleSheet)`

`[___] = report(___,targetFolder)`

`[___] = report(___,targetFile)`

`[___] = report(___,genOpt1,...,genOptN)`

## Description

`report` opens the Report Explorer as the active window.

`[rptFile1,...,rptFileN] = report(setup1,...,setupN)`
generates reports from the specified report setup files and returns the full paths of
the generated report files. The function generates the reports according to the
configuration of the report setup files.

`rptFile = report(simulinkModel)`
generates a report from the report setup file associated with the specified
Simulink® model.

**Note**

- You can use this syntax only if you have Simulink
  Report Generator™ installed.
- Load the Simulink model before using this syntax.

example

`[___] = report(___,outFormat)`
generates the reports in the specified format.

`[___] = report(___,outFormat,formatTemplate)`
generates the reports using the specified template of
`outFormat`.

example

`[___] = report(___,outFormat,formatStyleSheet)`
generates the reports using the specified style sheet of
`outFormat`.

example

`[___] = report(___,targetFolder)`
creates the generated report files in the specified folder.

example

`[___] = report(___,targetFile)`
specifies the target root name for the generated report files.

example

`[___] = report(___,genOpt1,...,genOptN)`
uses one or more options when generating the reports.

## Examples

### Generate Multiple Reports Simultaneously with Report Explorer

Open Live Script

Use variables to store the names of the report setup files.

```
rpt_file_1 = "first_rpt.rpt";
rpt_file_2 = "second_rpt.rpt";
rpt_file_3 = "third_rpt.rpt";
```

Define the folder for the generated reports and store the path in the variable `generated_reports_folder`. Include the backslash (`\`) at the end so the `report` function identifies the path as a folder and not as a root file name.

```
generated_reports_folder = "generated_reports\"
```

```
generated_reports_folder =
"generated_reports\"
```

Define the output path argument for the `report` function in the variable `out_path_param`.

```
out_path_param = "-o"+generated_reports_folder
```

```
out_path_param =
"-ogenerated_reports\"
```

Use the `report` function once to generate and view reports for all three setup files. Specify the folder to generate the reports in by using the `out_path_param` variable. Specify the generated reports type to be in the format `dom-pdf` with the template `default-rg-docx-numbered`.

The function generates and opens temporary DOCX files and converts the DOCX files to PDF files. If you get a Microsoft® Word pop up warning about allowing the document to update the fields, click **Yes**.

Store the paths of the generated report files in the string array `report_file_paths` and display the names of the files.

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

### Report on Simulink Model with Report Explorer

This example uses:

- Simulink Report GeneratorSimulink Report Generator

Open Live Script

This example shows how to use the Report Explorer to report on a Simulink model. You must have Simulink Report Generator installed to run this example.

Load the model and check which report setup file is associated with the model.

```
model_name = "simple_model";
load_system(model_name);
model_report_name = get_param(model_name,"ReportName")
```

```
model_report_name =
'simple_RPT.rpt'
```

Use the `report` function to generate a report named `reportOnSimpleModel` in the current directory using the `dom-pdf-direct` format. Launch the Message List dialog box of the Report Explorer by using the `-graphical` option.

Store the path of the generated report file in the variable `generated_report_path` and display the file name and extension.

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

### Avoid File Overwriting When Generating Multiple Reports

Open Live Script

This example shows how to avoid overwriting when generating multiple reports with the same root name.

**Configure the Report Setup Files**

Use variables to store the names of the report setup files.

```
rpt_file_1 = "my_first_rpt.rpt";
rpt_file_2 = "my_second_rpt.rpt";
rpt_file_3 = "my_third_rpt.rpt";
```

Use the function `setedit` to open the report setup files in the Report Explorer. Make sure the **If report already exists, increment to prevent overwriting** check box is selected for all three files.

```
setedit(rpt_file_1);
setedit(rpt_file_2);
setedit(rpt_file_3);
```

**Generate the Reports**

Define the base path for the generated reports.

```
base_report_path = fullfile("","generated_reports","myGeneratedReport")
```

```
base_report_path =
"generated_reports/myGeneratedReport"
```

Define the output path argument for the `report` function in the variable `out_path_param`. The function appends a different number to `base_report_path` for each report and generates report files with different names.

```
out_path_param = "-o"+base_report_path
```

```
out_path_param =
"-ogenerated_reports/myGeneratedReport"
```

Use the `report` function to generate and view reports for the three setup files simultaneously. Specify the root name for the generated reports using the `out_path_param` parameter. Specify the generated reports type to be in the format `pdf-fop` with the style sheet `fo-YesChapterNumbers`. Store the paths of the generated report files in the string array `report_file_paths` and display the names of the files. Note that the generated report files have different names because the increment to prevent overwriting option is selected.

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

## Input Arguments

### `setup1,...,setupN` — Names of report setup files character vector | string scalar

Names of report setup files to generate reports from, specified as string
scalars or character vectors.

### `simulinkModel` — Name of Simulink model associated with report setup file character vector | string scalar

Name of the Simulink model associated with the report setup file from which to generate
the report, specified as a character vector or string scalar.

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

### `outFormat` — Output report format character vector | string scalar

Output report format, specified as a character vector or string scalar in the
form of `-fFORMAT`, where `FORMAT` is a valid
format value.

To get the list of DOM formats use:

```
rptconvert("-domformatlist")
```

To
get the list of legacy, non-DOM formats use:

```
rptconvert("-formatlist")
```

### `formatTemplate` — Template of output format character vector | string scalar

Template of `outFormat` to use for generating the report,
specified as a character vector or string scalar in the form of
`-sTEMPLATE`, where `TEMPLATE` is a valid
template for the format `outFormat`. Legacy formats do not have
templates. All DOM formats have templates. To see the list of valid templates for
the `outFormat` format, which can be any valid DOM format, enter
the
command:

```
rptconvert("-templatelist",outFormat)
```

### `formatStyleSheet` — Style sheet of output format character vector | string scalar

Style sheet of `outFormat` to use for generating the report,
specified as a character vector or string scalar in the form of
`-sSTYLE_SHEET`, where `STYLE_SHEET` is a
valid style sheet for the format `outFormat`. DOM formats do
not have style sheets. All non-DOM formats, except `db`, have
style sheets. To see the list of valid style sheets for the
`outFormat` format, which can be any valid non-DOM format
except `db`, enter the
command:

```
rptconvert("-stylesheetlist",outFormat)
```

### `targetFile` — Base target file name for created report files character vector | string scalar

Base target file name for the created report files, specified as a character vector or string scalar in the form of `-oNAME`, where
`NAME` is the base name or path of the files to create.

**Note**

Specify `targetFile` as a single base name or path. To
prevent the function from trying to generate multiple report files with the
same name, when using this syntax with multiple report setup files, select
each report setup file in the **Outline** pane of the
Report Explorer and, in the **Properties** pane, ensure
that you select the **If report already exists, increment to prevent
overwriting** check box. The function then creates each report
file with a different name by appending a different number to the base file
name or path.

Report setup file is selected and the check box is selected

### `targetFolder` — Target folder in which to create report files character vector | string scalar

Target folder in which to create report files, specified as a character vector or string scalar in the form of `-oPATH`, where
`PATH` is a relative or full path.

**Note**

`PATH` must end with a slash (`/`) or
back-slash (`\`).

### `genOpt1,...,genOptN` — Options for generating the report `"-noview"` | `"-graphical"` | `"-debug"` | `"-quiet"`

Options for generating the report, specified as:

| Value | Description |
| --- | --- |
| `"-noview"` | Does not open the generated reports for viewing |
| `"-graphical"` | Loads the report setup files in the Report Explorer and launches the Message List dialog box prior to generating the report. Setup files that were not loaded in the Report Explorer before report generation are unloaded after the reports are generated. |
| `"-debug"` | Outputs debugging info in the MATLAB® command line. |
| `"-quiet"` | Suppresses command-line output. This option is ignored when used with the `-debug` option. |

## Output Arguments

### `rptFile1,...,rptFileN` — Full paths of generated report files string scalars

Full paths of the generated report files, returned as one or more string
scalars, one for each generated report file.

## Version History

**Introduced before R2006a**

## See Also

`setedit` | `rptconvert` | `rptlist` | `compwiz`

### Topics

- Generate Reports
- Report Output Format
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
