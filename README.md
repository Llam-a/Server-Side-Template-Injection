# Server-Side-Template-Injection

## Overview
Các engine template (công cụ mẫu) được sử dụng rộng rãi trong các ứng dụng web để giúp chia nhỏ mã HTML thành các phần nhỏ hơn có thể được sử dụng lại trên nhiều tập tin HTML khác nhau. Chúng giúp cho việc trình bày dữ liệu thông qua các trang web và email trở nên dễ dàng và linh hoạt hơn.

Tuy nhiên, khi nhúng các đầu vào từ phía người dùng vào các template một cách không an toàn, có thể xảy ra lỗ hổng gọi là Server-Side Template Injection (SSTI) - một lỗ hổng nghiêm trọng và thường bị nhầm lẫn với Cross-Site Scripting (XSS).

SSTI và XSS là hai lỗ hổng khác nhau. XSS xảy ra khi đầu vào người dùng được chèn vào các vị trí dữ liệu động trong mã HTML và có thể thực thi mã JavaScript độc hại trên trình duyệt của người dùng. Trong khi đó, SSTI xảy ra khi đầu vào người dùng được chèn vào các template trên máy chủ và có thể thực thi mã trên phía máy chủ.

SSTI là một lỗ hổng nghiêm trọng vì nó cho phép kẻ tấn công thực thi mã tùy ý trên máy chủ, ảnh hưởng đến tính toàn vẹn và bảo mật của ứng dụng. Do đó, việc kiểm tra và xử lý các đầu vào người dùng một cách an toàn trong các template engine là rất quan trọng để ngăn chặn SSTI.

## SSTI là gì

Server-side template injection (SSTI) là một lỗ hổng bảo mật mà kẻ tấn công chèn đầu vào độc hại vào một template để thực thi các lệnh phía máy chủ. Lỗ hổng này xảy ra khi đầu vào không hợp lệ của người dùng được nhúng vào engine template, điều này có thể dẫn đến việc thực thi mã từ xa (RCE).

Các engine template được thiết kế để kết hợp các template với mô hình dữ liệu để tạo ra các tài liệu kết quả, giúp điền dữ liệu động vào trang web. Các engine template có thể được sử dụng để hiển thị thông tin về người dùng, sản phẩm, v.v. Một số engine template phổ biến nhất có thể được liệt kê như sau:

PHP – Smarty, Twigs
Java – Velocity, Freemaker
Python – JINJA, Mako, Tornado
JavaScript – Jade, Rage
Ruby – Liquid
Khi kiểm tra đầu vào không được xử lý đúng cách phía máy chủ, một tải SSTI độc hại có thể được thực thi trên máy chủ, dẫn đến việc thực thi mã từ xa.

## Cách hoạt động của SSTI

Template dạng static cung cấp các vị trí trống (placeholder) cho engine điền dữ liệu liên quan và tạo ra trang web tương ứng. Ví dụ, trong template Twig sau, chúng ta có placeholder {first_name} để tạo nội dung chào hỏi người dùng:

```
$output = $twig->render("Dear {first_name},", array("first_name" => $user.first_name));
```

Với loại template này, SSTI không thể xảy ra vì dữ liệu được đưa vào placeholder {first_name} chỉ là dữ liệu thô.

Tuy nhiên, khi sử dụng template dạng string cho phép kết hợp trực tiếp thông tin nhập liệu từ người dùng trước khi xuất bản trên trang web, ví dụ như:

```
$output = $twig->render("Dear " . $_GET['name']);
```

Trong tình huống này, một phần của template trở thành dynamic (động), phụ thuộc vào tham số GET 'name'.

Do đó, nếu người dùng chèn payload độc hại vào tham số 'name' (ví dụ như thông qua URL http://vulnerable-website.com/?name={{bad-stuff-here}}), khi xử lý template syntax, máy chủ sẽ gặp vấn đề với nội dung `bad-stuff-here`.

*Các tài liệu sau đây có viết về cách kiểm tra, thực thi SSTI:

https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection

https://portswigger.net/research/server-side-template-injection

https://www.cobalt.io/blog/a-pentesters-guide-to-server-side-template-injection-ssti

https://www.wallarm.com/what/server-side-template-injection-ssti-vulnerability
