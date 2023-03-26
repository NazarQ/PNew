>>> property_transfer_xml = """<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento';//urn:multiCall/sessionId['?']</con:targetPath>"""
>>> l = property_transfer_xml
>>> l = property_transfer_xml.split('<con:name>')
['', "AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento';//urn:multiCall/sessionId['?']</con:targetPath>"]
>>> x = property_transfer_xml.split(' ')
>>> x[0]
'<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare'
>>> x[2]
"ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare"
>>> y = x[2]
>>> y = x[2].split()
>>> y[0]
"ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare"
>>> y = x[2].strip()
>>> y
"ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare"
>>> y = x[2].split(';')
["ns1='urn:Magento'", '//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare']
>>> z = y[1]
>>> z = y[1].split('con:targetType')
>>> z
['//ns1:loginResponse/loginReturn[1]</con:sourcePath><', '>Request</', '><con:targetStep>multiCall</con:targetStep><con:targetPath>declare']
>>> z[1]
'>Request</'
>>> q = z[1].strip('></')
>>> result = q
>>> print(result)
