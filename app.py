# Danh sách để lưu các công việc dưới dạng Dictionary
tasks = []


def add_task(task_name):
  """Thêm một công việc mới với trạng thái mặc định là chưa hoàn thành (completed: False)."""
  tasks.append({"name": task_name, "completed": False})
  print(f"Đã thêm công việc: '{task_name}'")


def complete_task(task_index):
  """Đánh dấu hoàn thành công việc theo số thứ tự (bắt đầu từ 1)."""
  if 1 <= task_index <= len(tasks):
    tasks[task_index - 1]["completed"] = True
    print(f"Đã hoàn thành công việc: '{tasks[task_index - 1]['name']}'")
  else:
    print("Lỗi: Số thứ tự công việc không hợp lệ!")


def list_tasks():
  """Hiển thị công việc kèm ký hiệu [x] nếu đã xong, [ ] nếu chưa xong."""
  if not tasks:
    print("Danh sách công việc đang trống.")
    return

  print("\n--- DANH SÁCH CÔNG VIỆC ---")
  for index, task in enumerate(tasks, start=1):
    status = "[x]" if task["completed"] else "[ ]"
    print(f"{index}. {status} {task['name']}")


# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
  print("Chào mừng đến với ứng dụng To-Do List!")
  add_task("Học bài Git và GitHub")
  add_task("Làm bài tập thực hành ở nhà")

  # Đánh dấu hoàn thành công việc số 1
  complete_task(1)

  # Hiển thị lại danh sách để kiểm tra trạng thái
  list_tasks()