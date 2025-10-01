class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):  # เพิ่มข้อมูลเข้า stack
        self.items.append(item)

    def pop(self):  # นำข้อมูลออกจาก stack (ถ้าว่างให้แจ้ง)
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty!"

    def peek(self):  # คืนค่าข้อมูลบนสุด (ไม่ลบออก)
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty!"

    def is_empty(self):  # ตรวจสอบว่า stack ว่างไหม
        return len(self.items) == 0

    def size(self):  # จำนวนสมาชิกใน stack
        return len(self.items)


# -----------------------
# โปรแกรมทดสอบ
# -----------------------
s = Stack()
print("Is empty?", s.is_empty())

for i in range(1, 6):
    s.push(i)

print("Size after push:", s.size())
print("Top element:", s.peek())

print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())
print("Pop:", s.pop())

print("Is empty?", s.is_empty())
print("Pop from empty:", s.pop())
