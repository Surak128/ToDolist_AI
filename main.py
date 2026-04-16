tasks = []


def add_task():
	title = input("ชื่อเรื่อง: ").strip()
	description = input("รายละเอียด: ").strip()
	due_date = input("วันครบกำหนด (YYYY-MM-DD): ").strip()
	if tasks:
		new_id = max(t['id'] for t in tasks) + 1
	else:
		new_id = 1
	task = {
		'id': new_id,
		'title': title,
		'description': description,
		'due_date': due_date,
		'complete': False,
	}
	tasks.append(task)
	print(f"เพิ่มงานเรียบร้อย: id={new_id} ชื่อ='{title}'")


def view_tasks():
	if not tasks:
		print("ยังไม่มีงานในรายการ")
		return
	print("รายการงานทั้งหมด:")
	for idx, t in enumerate(tasks, start=1):
		status = "เสร็จแล้ว" if t.get('complete') else "ยังไม่เสร็จ"
		print(f"{idx}. {t.get('title')}  | วันครบกำหนด: {t.get('due_date')}  | สถานะ: {status}")


def edit_task():
	pass


def delete_task():
	pass


def main_menu():
	while True:
		print("เมนูหลัก:")
		print("1. เพิ่มงานใหม่")
		print("2. ดูงานทั้งหมด")
		print("3. แก้ไขงาน")
		print("4. ลบงาน")
		print("5. ออกจากโปรแกรม")
		choice = input("เลือกตัวเลือก (1-5): ").strip()
		if choice == "1":
			add_task()
		elif choice == "2":
			view_tasks()
		elif choice == "3":
			edit_task()
		elif choice == "4":
			delete_task()
		elif choice == "5":
			print("ออกจากโปรแกรม")
			break
		else:
			print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")


if __name__ == "__main__":
	main_menu()