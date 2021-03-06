#!/usr/bin/env python3
# Author Zuxing Gu

import re

'''
'.'     默认匹配除\n之外的任意一个字符，若指定flag DOTALL,则匹配任意字符，包括换行
'^'     匹配字符开头，若指定flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee",flags=re.MULTILINE)
'$'     匹配字符结尾，或e.search("foo$","bfoo\nsdfsf",flags=re.MULTILINE).group()也可以
'*'     匹配*号前的字符0次或多次，re.findall("ab*","cabb3abcbbac")  结果为['abb', 'ab', 'a']
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba") 结果['ab', 'abb']
'?'     匹配前一个字符1次或0次
'{m}'   匹配前一个字符m次
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果'abb', 'ab', 'abb']
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果'ABC'
'(...)' 分组匹配，re.search("(abc){2}a(123|456)c", "abcabca456c").group() 结果 abcabca456c
 
 
'\A'    只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的
'\Z'    匹配字符结尾，同$
'\d'    匹配数字0-9
'\D'    匹配非数字
'\w'    匹配[A-Za-z0-9]
'\W'    匹配非[A-Za-z0-9]
's'     匹配空白字符、\t、\n、\r , re.search("\s+","ab\tc1\n3").group() 结果 '\t'
'''

result = re.match('^Gu', 'Guzuxing')
print(result)
print(result.group())
print(re.match('^Gu', 'I\' m Guzuxing'))

result = re.match('^Gu\d*', 'Gu123zuxing')
print(result.group())

result = re.search('G.+', '123Gu123Zuxing123')
print(result.group())

result = re.search('Z[a-z]+i', '123Gu123Zuxing123')
print(result)

result = re.search('Z[a-z]+', '123Gu123Zuxing123')
print(result)

result = re.findall('ab{1,3}', 'ab abbc abbbbba b')
print(result)

result = re.search('ab{1,3}', 'ab abbc abbbbba b')
print(result)

result = re.split('[0-9]', 'abc12de3f4g')
print(result)

result = re.sub('[0-9]', '@', 'abc12de3f4g')
print(result)
