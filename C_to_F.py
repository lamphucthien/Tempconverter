def c_to_f(c):
    return c * 9/5 + 32
while True:
 inp = input("Hãy nhập độ C, hoặc ấn f để dừng: ")
 if inp.lower() == 'f':
     print("End")
     break
 try:
     C = float(inp)
     print("F= ", c_to_f(C))
 except ValueError:
     print("Vui lòng nhập số hợp lệ: ")