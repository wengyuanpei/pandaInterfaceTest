from lupa import luaRuntime

with open(r'C:\Users\zhang\Downloads\Draws.lua','r') as file:
    lua_code=file.read()
lua=luaRuntime(unpack_return_tuples=True)
presed_table=lua.eval(lua_code)
print(presed_table)