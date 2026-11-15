---
type: simulink-block
title: 'HTTP Client'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Communications'
documentation_page: 'httpclient'
documentation_source_path: 'supportpkg/android_ref/httpclient.html'
language: en
---

# HTTP Client

## Ports

### Input

### **URL** — Path of request URL character vector

The block inputs the URL of the server.

**Tip**

If you are using the String
library blocks to create a URL, use a String to
ASCII block to convert the string to `uint8` vector.
The HTTP Client block needs the URL as a `uint8`
vector input.

**Data Types:** `uint8`

### **Payload** — Request payload character vector

The block inputs the data that the Android device sends as a payload of the request to the remote server.

#### Dependencies

- To enable this port, select **Request has payload input**
  and set it to any one of these parameters:

  - `application/json`
  - `text/plain`

**Data Types:** `uint8`

### **R** — Red component of image matrix

The block inputs the red component of an image. The matrix is of same size as
inputs **G** and **B**.

#### Dependencies

- To enable this port, select **Request has payload input**
  and set it to `image/jpeg`.

**Data Types:** `uint8`

### **G** — Green component of image matrix

The block inputs the green component of an image. The matrix is of same size as
inputs **R** and **B**.

#### Dependencies

- To enable this port, select **Request has payload input**
  and set it to `image/jpeg`.

**Data Types:** `uint8`

### **B** — Blue component of image matrix

The block inputs the blue component of an image. The matrix is of same size as
inputs **R** and **G**.

#### Dependencies

- To enable this port, select **Request has payload input**
  and set it to `image/jpeg`.

**Data Types:** `uint8`
### Output

### **Status** — Status of HTTP request `0` | `1` | `2`

The port outputs the status of the HTTP request whether the request to the remote server.

- `0` — Indicates any failure associated with the request
  sent to the server.
- `1` — Indicates a successful request sent to the
  server.
- `2` — Indicates an invalid response as the block waits to
  make the next HTTP request to the server.

**Data Types:** `uint8`

### **Message** — Message data scalar

If the **Status** port outputs `0`, then the
**Message** port outputs the error message.

#### Dependencies

- To enable this port, clear **Request has response
  output**.

**Data Types:** `uint8`

### **Response** — Response message from server character vector

For every successful HTTP request sent to the server, the port outputs the
response message. If the **Status** port outputs
`0`, then the **Response** port outputs the error
message. If the **Status** port outputs `1`, then
the **Response** port outputs the response message.

#### Dependencies

- To enable this port, select **Request has response
  output**.

**Data Types:** `uint8`

### **Data Size** — Size of response data from server scalar

The port outputs the size of the response message data received from the
server.

#### Dependencies

- To enable this port, select **Request has response
  output**.

**Data Types:** `int32`

## Parameters

### Main

### **Request Method** — HTTP request method `GET` (default) | `POST` | `PUT`

Select the HTTP request method to send a request message to the server from your
Android device.

- `GET` — This method requests data from a specified
  resource.
- `POST` — This method sends data to a server to
  create or update a resource.
- `PUT` — This method sends data to a server to
  create or update a resource.

### **Update Interval** — Interval between HTTP requests `2` (default) | positive integer

Specify the number of seconds to wait between subsequent HTTP requests.

### **Request has payload input** — Request payload input `off` (default) | `on`

Select this option if the HTTP request contains payload data in any one of these
formats: JSON, text, or image.

### **Content Type** — Input payload content type `application/json` (default) | `text/plain` | `image/jpeg`

Select the content type of the payload input of the HTTP request. In HTTP requests
such as POST or PUT, the client informs the remote server on the type of data actually
sent.

#### Dependencies

- To enable this parameter, select **Request has payload
  input**.

### **Request has response output** — Response payload output `off` (default) | `on`

Select this option if the HTTP response from the server contains payload
data.

### **Max Length of the output Message** — Maximum data length `256` (default) | positive integer

Enter the maximum length of the expected payload data response received from the
server.

#### Dependencies

- To enable this parameter, select **Request has response
  output**.

### **Accept** — Output payload data type `application/json` (default) | `text/plain`

Select the format of the output payload data of the HTTP response which the client
can understand.

#### Dependencies

- To enable this parameter, select **Request has response
  output**.

### Advanced

### **Number of custom headers** — HTTP request headers `0` (default) | `1` | `2` | `3`

Select the number of custom HTTP request headers. You can customize a header that
contains one or more key-value pairs to provide more information about the request.
The value `0` indicates that the HTTP request has no custom
header.

### **Key** — HTTP request header key clear (default) | character vector

Specify the HTTP request header key attribute. When you specify a value other than
`0` in the **Number of custom headers**
parameter, the block generates equal number of header keys. For example, if you set
**Number of custom headers** to `2`, the
block generates two **Key** parameters.

#### Dependencies

- To enable this parameter, set **Number of custom headers**
  to `1`, `2`, or
  `3`.

### **Value** — HTTP request header value clear (default) | character vector

Specify the value for the custom HTTP request header key. When you specify a value
other than `0` in the **Number of custom
headers** parameter, the block generates equal number of header values. For
example, if you set **Number of custom headers** to
`3`, the block generates three **Value**
parameters.

#### Dependencies

- To enable this parameter, set **Number of custom headers**
  to `1`, `2`, or
  `3`.

## Libraries

Simulink Support Package for Android Devices / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

## Description

Send and receive data from HTTP server over URL connection

Use the HTTP Client block to send and receive data such as text from the
remote server using the HTTP protocol. You can also use the block to send images to the remote
server. The Android® device acts as a client and can send HTTP requests to the remote server over an
uniform resource locator (URL) connection. The block supports HTTP GET, POST, and PUT methods.

**Note**

You can use only one HTTP Client block in a Simulink® model and deploy the model on your Android device.
