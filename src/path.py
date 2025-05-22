import os


def root_join(*parts):
    """Функция возвращающая путь к файлу указанному из корня"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    full_path = os.path.join(base_dir, *parts)
    return full_path


if __name__ == "__main__":
    with open(root_join("html_pages", "contacts.html"), encoding="utf-8") as f:
        content = f.read()
