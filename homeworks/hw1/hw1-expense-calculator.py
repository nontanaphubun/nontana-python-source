income = float(input("กรอกรายได้ต่อเดือน (บาท): "))
rent = float(input("กรอกค่าเช่าบ้าน (บาท): "))
food = int(input("กรอกค่ากินต่อเดือน (บาท): "))
transport = float(input("กรอกค่าเดินทาง (บาท): "))
entertain = int(input("กรอกค่าพักผ่อนต่อเดือน (บาท): "))
emergency_percent = float(input("กรอกเปอร์เซ็นต์เผื่อเงินฉุกเฉิน: "))
invest_percent = float(input("กรอกเปอร์เซ็นต์เงินลงทุน: "))

fixed = rent + transport

variable = food + entertain

total = fixed + variable

remaining = income - total

emergency = income * (emergency_percent / 100)
invest = income * (invest_percent / 100)

savings = remaining - emergency - invest

expense_ratio = (total / income) * 100

print("\n=== รายงานงบประมาณรายเดือน ===")
print(f"รายได้: {income:.2f} บาท")
print(f"ค่าใช้จ่ายคงที่: {fixed:.2f} บาท")
print(f"ค่าใช้จ่ายไม่คงที่: {variable:.2f} บาท")
print(f"ค่าใช้จ่ายทั้งหมด: {total:.2f} บาท")
print(f"รายได้คงเหลือ: {remaining:.2f} บาท")

print("\n=== การออมเงิน ===")
print(f"เงินฉุกเฉิน ({emergency_percent}%): {emergency:.2f} บาท")
print(f"เงินลงทุน ({invest_percent}%): {invest:.2f} บาท")
print(f"เงินที่เก็บออมได้: {savings:.2f} บาท")

print("\n=== วิเคราะห์ ===")
print(f"สัดส่วนค่าใช้จ่ายต่อรายได้: {expense_ratio:.2f}%")