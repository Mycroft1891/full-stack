# How to Web Works

## Components of the web

- Browser: A program that runs locally
- Internet: The idea of a cloud
- HTTP: The protocol to communicate with the server
- Server: The computer that responds

### HTTP Request

Whenever your web browser fetches a file (a page, a picture, etc) from a web server, it does so using HTTP - that's "Hypertext Transfer Protocol".  HTTP is a request/response protocol, which means your computer sends a request for some file (e.g. "Get me the file 'home.html'"), and the web server sends back a response ("Here's the file", followed by the file itself).


### Content Headers

HTTP headers allow the client and the server to pass additional information with the request or the response. A request header consists of its case-insensitive name followed by a colon ':', then by its value (without line breaks). Leading white space before the value is ignored.

### HTTP Methods

- GET
- HEAD
- POST
- PUT
- DELETE
- CONNECT
- OPTIONS
- TRACE
- PATCH

HTTP defines a set of request methods to indicate the desired action to be performed for a given resource. Although they can also be nouns, these request methods are sometimes referred to as HTTP verbs. Each of them implements a different semantic, but some common features are shared by a group of them: e.g. a request method can be safe, idempotent, or cacheable.


### Telnet for requests

Telnet is often used when diagnosing problems, to manually "talk" to other services without specialized client software. For example, it is sometimes used in debugging network services such as an SMTP, HTTP, FTP or POP3 server, by serving as a simple way to send commands to the server and examine the responses.

Example:

```
telnet example.com 25
```
