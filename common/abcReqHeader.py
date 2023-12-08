



def abcBaseUrl(baseurl):
    if baseurl=='dev':
        baseurl_dev = 'http://api-dev.abctime.com'
        return baseurl_dev
    if baseurl == 'pre':
        baseurl_pre = 'https://pre-api.abctime.com'
        return baseurl_pre
    if baseurl=='live':
        baseurl_live = 'https://api.abctime.com'
        return baseurl_live

def reqHeader(env,uid,token):
    if env=='dev':

        headers_dev = {'PANDA-TOKEN': token, 'PANDA-UID': uid}
        return headers_dev
    if env == 'pre':
        headers_pre = {'PANDA-UID': uid, 'PANDA-TOKEN': token,
                   'Content-Type': 'application/json; charset=utf-8',
                   'PANDA-USE-NEW-VERSION': '2',
                   'versionCode': '653',
                   'Host': 'pre-api.abctime.com'}
        return headers_pre