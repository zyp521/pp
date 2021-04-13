class a:
    
    def __enter__(self):
        print('初始化函数')
        return 

    def __exit__(self,type_,value,track):
        if track:
            print('发生错误')
            print(type_)
            print(value)
            print(track)
            return value
        else:
            print('正常结束')

with a():
    print(1/0)
    
