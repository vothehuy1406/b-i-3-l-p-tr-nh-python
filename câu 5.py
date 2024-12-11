print('sinh viên: VÕ THẾ HUY')
print('MSV: 235752021610031')
a = "Hello Guy!"

def say():
    global a
    a = "Vinh University"
    print(a)  # In ra biến a trong hàm

say()  # Gọi hàm say
print(a)  # In ra biến a sau khi gọi hàm
