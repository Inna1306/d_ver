# -*- coding: utf-8 -*-
A = "assets/"

def head(title):
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="style.css">
</head>
<body>
"""

TOPBAR = """<header class="topbar">
  <a class="logo" href="index.html"><span class="logo__mark">&#128218;</span>лого</a>
  <nav class="topbar__nav">
    <a href="index.html#map">Библиотеки</a>
    <a href="index.html#about">О нас</a>
    <a href="index.html#contacts">Контакты</a>
    <a href="login.html">Вход</a>
  </nav>
</header>
"""

FOOTER = """<footer class="footer" id="contacts">
  <img class="blob blob--right" src="{a}amorphous-shape-2.svg" alt="">
  <img class="blob blob--left" src="{a}amorphous-shape-3.svg" alt="">
  <div class="footer__inner">
    <div class="footer__logo">лого</div>
    <div class="footer__social">
      <a class="social-link" href="#" aria-label="ВКонтакте"><img src="{a}social-vk.svg" alt="VK"></a>
      <a class="social-link" href="#" aria-label="Telegram"><img src="{a}social-telegram.svg" alt="Telegram"></a>
      <a class="social-link" href="#" aria-label="Одноклассники"><img src="{a}social-odnoklassniki.svg" alt="OK"></a>
      <a class="social-link" href="#" aria-label="YouTube"><img src="{a}social-youtube.svg" alt="YouTube"></a>
    </div>
    <p class="footer__policy">Политика обработки персональных данных</p>
  </div>
</footer>
"""

END = """<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
"""

def page(title, body, topbar=True, footer=True):
    out = head(title)
    if topbar: out += TOPBAR
    out += body
    if footer: out += FOOTER.format(a=A)
    out += END
    return out

def write(name, html):
    with open(name, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", name)

def search_form(values=None, action="search.html"):
    v = values or {}
    return f"""<form class="hero-form" action="{action}" method="get">
  <div class="field field--full">
    <label class="field__label" for="f-name">Название</label>
    <input class="field__input" id="f-name" name="name" type="text" placeholder="Введите название книги" value="{v.get('name','')}">
  </div>
  <div class="field field--full">
    <label class="field__label" for="f-author">Автор</label>
    <input class="field__input" id="f-author" name="author" type="text" placeholder="Введите автора" value="{v.get('author','')}">
  </div>
  <div class="field">
    <label class="field__label" for="f-out">Выдача книги</label>
    <input class="field__input" id="f-out" name="issue" type="date" value="{v.get('out','')}">
  </div>
  <div class="field">
    <label class="field__label" for="f-ret">Возврат книги</label>
    <input class="field__input" id="f-ret" name="return" type="date" value="{v.get('ret','')}">
  </div>
  <div class="field--full"><button class="btn btn--primary" type="submit">Найти</button></div>
</form>
"""

BOOKS_JS = [
    dict(cover="book-1.svg", title="JavaScript для детей до профи", author="Ник Морган", year="2014",
         desc="Эта книга позволит вам погрузиться в программирование и с легкостью освоить JavaScript. Вы напишете несколько настоящих игр — поиск сокровищ на карте, «Виселицу», «Змейку»…",
         lib="Центральная городская библиотека им. Н.А. Некрасова"),
    dict(cover="book-2.svg", title="JavaScript с нуля", author="Свекис Лоренс, Ларс Майке, Персиваль Роб", year="2019",
         desc="Книга демонстрирует возможности JavaScript для разработки веб-приложений, сочетая теорию с упражнениями и интересными проектами. Она показывает…",
         lib="Центральная городская библиотека им. Н.А. Некрасова"),
    dict(cover="book-3.svg", title="Рефакторинг кода на JavaScript", author="Мартин Фаулер", year="2019",
         desc="Рефакторинг уже давно и прочно занимает достойное место среди технологий программирования, и не в последнюю очередь благодаря Мартину Фаулеру — автору одной из тех книг…",
         lib="Центральная городская библиотека им. Н.А. Некрасова"),
    dict(cover="book-4.svg", title="Полное руководство по JavaScript", author="Дэвид Флэнаган", year="2020",
         desc="Справочник по самому популярному языку программирования! JavaScript — это язык программирования для веб-страниц, который в настоящее время используется большим количеством…",
         lib="Центральная городская библиотека им. Н.А. Некрасова"),
]

def book_card(b, booking_link="booking.html"):
    return f"""<article class="book-card">
  <div class="book-card__cover"><img src="{A}{b['cover']}" alt="Обложка: {b['title']}"></div>
  <div class="book-card__body">
    <h3 class="book-card__title">{b['title']}</h3>
    <p class="book-card__row"><b>{b['author']}</b></p>
    <p class="book-card__row"><span>{b['year']}</span></p>
    <p class="book-card__row">{b['desc']}</p>
    <p class="book-card__row"><span>{b['lib']}</span></p>
    <a class="btn btn--primary btn--sm book-card__action" href="{booking_link}">Забронировать</a>
  </div>
</article>
"""

# ---------------- account shell ----------------
def sidebar(name, role, items, active, avatar):
    nav = ""
    for label, href in items:
        cls = ' class="is-active"' if label == active else ""
        nav += f'      <a{cls} href="{href}">{label}</a>\n'
    return f"""    <aside class="account__sidebar">
      <img class="avatar" src="{A}avatars/{avatar}" alt="Аватар">
      <h2 class="account__name">Привет, {name}!</h2>
      <p class="account__role">{role}</p>
      <nav class="account__nav">
{nav}      </nav>
    </aside>
"""

USER_NAV = [("Главная", "user-home.html"), ("Мои книги", "user-books.html"),
            ("Профиль", "user-profile.html"), ("Выход", "login.html")]
MANAGER_NAV = [("Главная", "manager-home.html"), ("Пользователи", "manager-users.html"),
               ("Книги", "manager-books.html"), ("Настройки", "manager-settings.html"),
               ("Выход", "login.html")]
ADMIN_NAV = [("Главная", "admin-home.html"), ("Пользователи", "admin-users.html"),
             ("Библиотеки", "admin-libraries.html"), ("Настройки", "admin-settings.html"),
             ("Выход", "login.html")]

def account_page(title, side_name, side_role, side_items, active, avatar, content_html):
    body = f"""<main class="screen">
  <div class="page">
    <div class="account">
{sidebar(side_name, side_role, side_items, active, avatar)}      <section class="account__content">
{content_html}      </section>
    </div>
  </div>
</main>
"""
    return page(title, body)

# user books rows (mockup account user 3 / manager 4)
USER_BOOKS = [
    (1, "book-5.svg", "Мастер и Маргарита", "М.А. Булгаков", "Центральная городская библиотека им. Н.А. Некрасова", "10.08.2025", "25.08.2025", "возвращена"),
    (2, "book-6.svg", "Братья Карамазовы", "Ф.М. Достоевский", "Центральная городская библиотека им. Н.А. Некрасова", "15.04.2025", "30.04.2025", "возвращена"),
    (3, "book-1.svg", "Путь жизни", "Л.Н. Толстой", "Библиотека-читальня им. И.С. Тургенева", "05.09.2024", "28.09.2024", "возвращена"),
    (4, "book-2.svg", "Мёртвые души", "Н.В. Гоголь", "Библиотека-читальня им. И.С. Тургенева", "12.03.2024", "02.04.2024", "возвращена"),
    (5, "book-3.svg", "Евгений Онегин", "А.С. Пушкин", "Центральная городская библиотека им. Н.А. Некрасова", "22.10.2023", "05.11.2023", "возвращена"),
]

def badge(status):
    m = {"забронирована": ("badge--active", "Забронирована"),
         "возвращена": ("badge--done", "Возвращена"),
         "просрочена": ("badge--overdue", "Просрочена")}
    c, t = m[status]
    return f'<span class="badge {c}">{t}</span>'

def books_table(rows):
    t = """<table class="table">
  <thead><tr><th>ID</th><th>Обложка</th><th>Название книги / автор</th><th>Библиотека</th><th>Выдача</th><th>Возврат</th><th>Статус</th></tr></thead>
  <tbody>
"""
    for rid, cov, title_, author, lib, d1, d2, st in rows:
        t += f"""    <tr><td>{rid}</td><td><img class="cover-thumb" src="{A}{cov}" alt=""></td><td><b>{title_}</b> / {author}</td><td>{lib}</td><td>{d1}</td><td>{d2}</td><td>{badge(st)}</td></tr>\n"""
    t += """  </tbody>
</table>
"""
    return t

CHIPS_BOOKS = """<div class="chips">
  <button class="chip is-active" type="button">Все</button>
  <button class="chip" type="button">Забронирована</button>
  <button class="chip" type="button">Возвращена</button>
</div>
"""
