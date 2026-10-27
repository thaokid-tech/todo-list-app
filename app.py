# Danh sách để lưu các công việc dưới dạng Dictionary
tasks = []


def add_task(task_name):
  """Thêm một công việc mới với trạng thái mặc định là chưa hoàn thành."""
  tasks.append({'name': task_name, 'completed': False})
  print(f"Đã thêm công việc: '{task_name}'")


def complete_task(task_index):
  """Đánh dấu hoàn thành công việc theo số thứ tự (bắt đầu từ 1)."""
  if 1 <= task_index <= len(tasks):
    tasks[task_index - 1]['completed'] = True
    print(f"Đã hoàn thành công việc: '{tasks[task_index - 1]['name']}'")
  else:
    print('Lỗi: Số thứ tự công việc không hợp lệ!')


def delete_task(task_index):
  """Xóa công việc khỏi danh sách dựa trên số thứ tự (bắt đầu từ 1)."""
  if 1 <= task_index <= len(tasks):
    removed_task = tasks.pop(task_index - 1)
    print(f"Đã xóa công việc: '{removed_task['name']}'")
  else:
    print('Lỗi: Số thứ tự công việc không hợp lệ!')


def list_tasks():
  """Hiển thị công việc kèm ký hiệu [x] hoặc [ ]."""
  if not tasks:
    print('Danh sách công việc đang trống.')
    return

  print('\n--- DANH SÁCH CÔNG VIỆC ---')
  for index, task in enumerate(tasks, start=1):
    status = '[x]' if task['completed'] else '[ ]'
    print(f"{index}. {status} {task['name']}")


# --- Điểm bắt đầu của chương trình ---
if __name__ == '__main__':
  print('Chào mừng đến với ứng dụng To-Do List!')
  add_task('Học bài Git và GitHub')
  add_task('Làm bài tập thực hành ở nhà')

  complete_task(1)

  # Thử nghiệm xóa công việc số 2
  delete_task(2)

  # Hiển thị lại danh sách kiểm tra
  list_tasks()