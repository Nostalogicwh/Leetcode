# 题目
你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。  

你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。


# 解题思路
双指针，1代表name，2代表typed  
- 1与2相同时，都走一步
- 1与2后面的字符相同时，多打了，2走一步
- 1与2不同时，返回false