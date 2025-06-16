import base64

import base64

encodestr =base64.b64decode('geFRzFKr9VhVeJdk/TREjQ=='.encode('utf-8'))
print(encodestr.decode('utf-8','ignore'))


one1=encodestr.decode('utf-8','ignore')
one2=base64.encode(one1)
print(one2)