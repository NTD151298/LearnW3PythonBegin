m1 = [2,21,2,0,0,0,23,123,23,2,0,0,0,324]
m2 = [3,2,4,1,2,3,12,312,53,23]
print("m1 =", m1)
print("m2 =", m2)
i = 0
t = 0
# Vòng lặp đầu trong mảng m1
for i in range(len(m1) - 1, -1, -1):
    #    print(i, "\t", m1[i]) # Check xem nó in ra từng phần tử trong mảng theo kiểu đi ngược xuống
    #    i += 1
    # Vòng lặp m1
    for j in range(i, -1, -1): 
#        print(j, "\t", m1[j]) # Check xem nó con trỏ vòng lặp này chạy xuống theo từng phần tử một mảng m1
        if m1[i] < m1[j]:   # Check nó nếu số đang cần được so sánh nhỏ hơn thì
            t = m1[j]       # Hàm thay đổi           
            m1[j] = m1[i]       
            m1[i] = t       
#           print("m1[i]", m1[i], "m1[j]", m1[j]) # Chúng ta in sau khi đánh tráo hai số 
#    print("\n")       #Check liên tục        
#    print("m1 =", m1) #Check liên tục
#   t
#   m1[j]   m1[i]
#    print("m1 =", m1)
# Vòng lặp m2
    for k in range(len(m2)):
         if m2[k] > m1[i]:
            t = m2[k]       # Hàm thay đổi           
            m2[k] = m1[i]       
            m1[i] = t

#   t
#   m2[k]   m1[i]
#             # Sau khi chèn phần tử m2 vào m1, ta sắp xếp lại m1
#             for j in range(i):
#                 if m1[j] > m1[j+1]:
#                     m1[j], m1[j+1] = m1[j+1], m1[j]
#             break
#
# # In kết quả
print("m1 =", m1)
print("m2 =", m2)
