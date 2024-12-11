print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
def get_sum(*num):
    tmp = 0
    # Duyệt qua các tham số
    for i in num:
        tmp += i
    return tmp

result = get_sum(1, 2, 3, 4, 5)
print(result)
