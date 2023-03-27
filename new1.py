property_transfer_xml = """<con:name>AuthTocken</con:name><con:sourceType>Response</con:sourceType><con:sourceStep>login</con:sourceStep><con:sourcePath>declare namespace ns1='urn:Magento';//ns1:loginResponse/loginReturn[1]</con:sourcePath><con:targetType>Request</con:targetType><con:targetStep>multiCall</con:targetStep><con:targetPath>declare namespace urn='urn:Magento';//urn:multiCall/sessionId['?']</con:targetPath>"""
l = property_transfer_xml
l = property_transfer_xml.split('<con:name>')
x = property_transfer_xml.split(' ')
y = x[2]
y = x[2].split()
y[0]
y = x[2].strip()
y = x[2].split(';')
z = y[1]
z = y[1].split('con:targetType')
z[1]
q = z[1].strip('></')
result = q
print(result)


"""______________________"""

raw_str = property_transfer_xml.split('con:targetType')
print(raw_str)
print('\n')
result = raw_str[1][:-1].strip('<').strip('>')
print(result)
