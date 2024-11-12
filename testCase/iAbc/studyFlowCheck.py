





class LoginForm(forms.Form):
    #检测校验用户登录
    username = forms.CharField(max_length=15, min_length=3,
                               error_messages={
                                   "max_length": "用户名长度过长",
                                   "min_length": "用户名长度不足",
                                   "required": "用户名不能为空",
                               })
    password = forms.CharField(max_length=15, min_length=6,
                               error_messages={
                                   "max_length": "密码名长度过长",
                                   "min_length": "密码名长度不足",
                                   "required": "密码不能为空",
                               })
    def clean_username(self):
        name=self.cleaned_data.get("username")
        if not re.match(r'^[A-Za-z0-9_]{3,15}$',name):
            self.add_error('username','用户名格式不正确')
        return name