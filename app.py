# Danh sách để lưu các công việc
tasks = []


def add_task(task_name):
  """Thêm một công việc mới vào danh sách."""
  tasks.append(task_name)
  print(f"Đã thêm công việc: '{task_name}'")


def list_tasks():
  """Duyệt và in ra danh sách công việc có đánh số thứ tự (bắt đầu từ 1)."""
  if not tasks:
    print("Danh sách công việc đang trống.")
    return

  print("\n--- DANH SÁCH CÔNG VIỆC ---")
  for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")


if __name__ == "__main__":
  print("Chào mừng đến với ứng dụng To-Do List!")
  add_task("Học bài Git và GitHub")
  add_task("Làm bài tập thực hành ở nhà")

  # Gọi hàm hiển thị danh sách vừa viết
  list_tasks()