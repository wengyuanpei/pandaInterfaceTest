from mitmproxy import ctx


# 当一个SSL连接建立时，这个方法会被调用
def request(flow):
    if flow.server_conn:
        cert = flow.server_conn.cert
        if cert:
            with open(r"C:\Users\zhang\Documents\pandaInterfaceTest\testCase\abcReading\pem/cert.pem", "wb") as f:
                f.write(cert.as_pem())


addons = [
    request,
]