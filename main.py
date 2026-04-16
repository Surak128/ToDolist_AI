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


def update_task():
	if not tasks:
		print("ยังไม่มีงานในรายการ")
		return
	try:
		idx_str = input("เลือกลำดับงานที่ต้องการแก้ไข: ").strip()
		idx = int(idx_str)
	except ValueError:
		print("ตัวเลขไม่ถูกต้อง")
		return
	if idx < 1 or idx > len(tasks):
		print("index ไม่ถูกต้อง")
		return
	task = tasks[idx - 1]
	new_title = input(f"ชื่องาน ({task.get('title')}): ").strip()
	if new_title:
		task['title'] = new_title
	new_description = input(f"รายละเอียด ({task.get('description')}): ").strip()
	if new_description:
		task['description'] = new_description
	new_due = input(f"วันครบกำหนด ({task.get('due_date')}): ").strip()
	if new_due:
		task['due_date'] = new_due
	new_comp = input(f"สถานะเสร็จแล้ว? (y/n) [ปัจจุบัน: {'y' if task.get('complete') else 'n'}]: ").strip().lower()
	if new_comp == 'y':
		task['complete'] = True
	elif new_comp == 'n':
		task['complete'] = False
	print(f"ปรับปรุงงาน id={task.get('id')} เรียบร้อย")


def delete_task():
	if not tasks:
		print("ยังไม่มีงานในรายการ")
		return
	try:
		idx_str = input("เลือกลำดับงานที่ต้องการลบ: ").strip()
		idx = int(idx_str)
	except ValueError:
		print("ตัวเลขไม่ถูกต้อง")
		return
	if idx < 1 or idx > len(tasks):
		print("index ไม่ถูกต้อง")
		return
	task = tasks[idx - 1]
	confirm = input("ต้องการลบงานนี้จริงหรือไม่ (y/n): ").strip().lower()
	if confirm == 'y':
		removed = tasks.pop(idx - 1)
		print(f"ลบงาน id={removed.get('id')} เรียบร้อย")
	else:
		print("ยกเลิกการลบ")


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
			update_task()
		elif choice == "4":
			delete_task()
		elif choice == "5":
			print("ออกจากโปรแกรม")
			break
		else:
			print("ตัวเลือกไม่ถูกต้อง กรุณาลองใหม่")


if __name__ == "__main__":
	main_menu()