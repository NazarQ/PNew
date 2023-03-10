Microsoft Windows [Version 10.0.18363.1316]
(c) Корпорація Майкрософт (Microsoft Corporation), 2019. Усі права захищено.

C:\Users\User>python
Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> property_transfer_xml = """<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento';//urn:multiCall/sessionId['?']</con:targetPath>"""
>>> property_transfer_xml
"<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento';//urn:multiCall/sessionId['?']</con:targetPath>"
>>> l = property_transfer_xml.split('<con:name>')
>>> l
['', "AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento';//urn:multiCall/sessionId['?']</con:targetPath>"]
>>> print(l)
['', "AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento';//urn:multiCall/sessionId['?']</con:targetPath>"]
>>> property_transfer_xml
"<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento';//urn:multiCall/sessionId['?']</con:targetPath>"
>>> x = property_transfer_xml.split(' ')
>>> x
['<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare', 'namespace', "ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare", 'namespace', "urn='urn:Magento';//urn:multiCall/sessionId['?']</con:targetPath>"]
>>> x = property_transfer_xml.split()
>>> x
['<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare', 'namespace', "ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare", 'namespace', "urn='urn:Magento';//urn:multiCall/sessionId['?']</con:targetPath>"]
>>> print(x)
['<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare', 'namespace', "ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare", 'namespace', "urn='urn:Magento';//urn:multiCall/sessionId['?']</con:targetPath>"]
>>> x[0]
'<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare'
>>> list
<class 'list'>
>>> x[1, 2, 3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
>>> x[1, 2]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: list indices must be integers or slices, not tuple
>>> x[2]
"ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare"
>>> y = x[2]
>>> y
"ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare"
>>> y = x[2].split()
>>> y
["ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare"]
>>> y[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
>>> y[0]
"ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare"
>>> y = x[2].strip[]
  File "<stdin>", line 1
    y = x[2].strip[]
                   ^
SyntaxError: invalid syntax
>>> y = x[2].strip()
>>> y
"ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare"
>>> y = x[2].split(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str or None, not int
>>> y = x[2].split(;)
  File "<stdin>", line 1
    y = x[2].split(;)
                   ^
SyntaxError: invalid syntax
>>> y = x[2].split(';')
>>> y
["ns1='urn:Magento'", '//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare']
>>> y[1]
'//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare'
>>> z = y[1]
>>> z
'//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare'
>>> z = y[1].split('con:targetType')
>>> z
['//ns1:loginResponse/loginReturn[1]</con:sourcePath><', '>Request</', '><con:targetStep>multiCall</con:targetStep><con:targetPath>declare']
>>> z[2]
'><con:targetStep>multiCall</con:targetStep><con:targetPath>declare'
>>> z[1]
'>Request</'
>>> q = z[1]
>>> q
'>Request</'
>>> q = z[1].strip()
>>> q
'>Request</'
>>> z
['//ns1:loginResponse/loginReturn[1]</con:sourcePath><', '>Request</', '><con:targetStep>multiCall</con:targetStep><con:targetPath>declare']
>>> z = y[1].split('con:targetType>', '</con:targetType')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> z = y[1].split('con:targetType>',"</con:targetType")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> z = y[1].split('con:targetType>', "</con:targetType")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object cannot be interpreted as an integer
>>> z
['//ns1:loginResponse/loginReturn[1]</con:sourcePath><', '>Request</', '><con:targetStep>multiCall</con:targetStep><con:targetPath>declare']
>>> z[2]
'><con:targetStep>multiCall</con:targetStep><con:targetPath>declare'
>>> z[]1
  File "<stdin>", line 1
    z[]1
      ^
SyntaxError: invalid syntax
>>> z[1]
'>Request</'
>>> q = z[1].stip(></)
  File "<stdin>", line 1
    q = z[1].stip(></)
                  ^
SyntaxError: invalid syntax
>>> q = z[1].stip('></')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'str' object has no attribute 'stip'. Did you mean: 'strip'?
>>> q = z[1].strip(></)
  File "<stdin>", line 1
    q = z[1].strip(></)
                   ^
SyntaxError: invalid syntax
>>> q = z[1].strip('></')
>>> q
'Request'
>>>