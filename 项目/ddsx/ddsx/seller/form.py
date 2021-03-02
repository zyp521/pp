from django import forms
from django.core.exceptions import ValidationError


class SellerForm(forms.Form):
    username = forms.CharField(
        required=True,  # 必填，
        error_messages={'required': '不能为空'}
    )
    password = forms.CharField(
        required=True,  # 必填，不能为空
        min_length=6,  # 至少6位
        error_messages={'required': '不能为空', 'min_length': '至少6位'}
    )
    email = forms.CharField(
        required=True,  # 必填，不能为空
        error_messages={'required': '不能为空'}
    )
    phone = forms.CharField(
        required=True,  # 必填，不能为空
        error_messages={'required': '不能为空'}
    )
    address = forms.CharField(
        required=True,  # 必填，不能为空
        error_messages={'required': '不能为空'}
    )
    gender = forms.CharField(
        required=True,  # 必填，不能为空
        error_messages={'required': '不能为空'}
    )
    headimg = forms.FileField(
        required=True,
        error_messages={'required': '不能为空'}
    )

    # 自定义校验
    # 对用户名进行校验
    def clean_username(self):
        # 1.获取到表单输入内容
        username = self.cleaned_data.get('username')
        # 2.判断
        if 'sb' in username:
            # 抛出异常
            raise ValidationError('名称包含敏感词汇..')
