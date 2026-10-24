# -*- coding: utf-8 -*-
from _common import *

# ---- user-books.html: add action column (cancel booking) + profile change-password link ----
rows = [(1,"book-5.svg","Мастер и Маргарита","М.А. Булгаков","Центральная городская библиотека им. Н.А. Некрасова","10.08.2025","25.08.2025","забронирована"),
        (2,"book-6.svg","Братья Карамазовы","Ф.М. Достоевский","Центральная городская библиотека им. Н.А. Некрасова","15.04.2025","30.04.2025","возвращена"),
        (3,"book-1.svg","Путь жизни","Л.Н. Толстой","Библиотека-читальня им. И.С. Тургенева","05.09.2024","28.09.2024","возвращена"),
        (4,"book-2.svg","Мёртвые души","Н.В. Гоголь","Библиотека-читальня им. И.С. Тургенева","12.03.2024","02.04.2024","возвращена"),
        (5,"book-3.svg","Евгений Онегин","А.С. Пушкин","Центральная городская библиотека им. Н.А. Некрасова","22.10.2023","05.11.2023","возвращена")]
t = """        <h2 class="section-title">Мои книги</h2>
""" + CHIPS_BOOKS + """        <div class="table-wrap">
        <table class="table">
          <thead><tr><th>ID</th><th>Обложка</th><th>Название книги / автор</th><th>Библиотека</th><th>Выдача</th><th>Возврат</th><th>Статус</th><th>Действия</th></tr></thead>
          <tbody>
"""
for rid, cov, ti, au, lib, d1, d2, st in rows:
    act = '<a class="btn btn--sm btn--danger" href="modal-confirm-cancel-booking.html">Отменить бронь</a>' if st == "забронирована" else '<span class="empty__text">&mdash;</span>'
    t += f"""            <tr><td>{rid}</td><td><img class="cover-thumb" src="assets/{cov}" alt=""></td><td><b>{ti}</b> / {au}</td><td>{lib}</td><td>{d1}</td><td>{d2}</td><td>{badge(st)}</td><td>{act}</td></tr>\n"""
t += """          </tbody>
        </table>
        </div>
"""
write("user-books.html", account_page("Мои книги — читатель", "Капитолина", "Читатель", USER_NAV, "Мои книги", "avatar 4.svg", t))

# ---- profiles with change password button ----
def prof(filled):
    av_actions = ('<div class="avatar-actions"><button class="btn btn--sm btn--ghost" type="button">&#128247; Изменить фото</button><button class="btn btn--sm btn--ghost" type="button">&#10005; Удалить фото</button></div>'
                  if filled else '<div class="avatar-actions"><button class="btn btn--sm btn--ghost" type="button">&#128247; Добавить фото</button></div>')
    return f"""        <h2 class="section-title">Личная информация</h2>
        <form class="form--grid form">
          <div class="field field--full"><label class="field__label">ФИО</label><input class="field__input" value="Власова Капитолина Владимировна"></div>
          <div class="field"><label class="field__label">Телефон</label><input class="field__input" type="tel" value="+790677866543"></div>
          <div class="field"><label class="field__label">Почта</label><input class="field__input" type="email" value="valsova_kap@mail.com"></div>
          <div class="field"><label class="field__label">Пароль</label><a class="btn btn--sm btn--ghost" href="modal-change-password.html">&#128274; Сменить пароль</a></div>
          <div class="field"><label class="field__label">Аватар</label><img class="avatar" style="width:80px;height:80px" src="assets/avatars/{'avatar 4.svg' if filled else 'avatar 24.svg'}" alt="Аватар"><br>{av_actions}</div>
          <div class="modal__actions field--full"><button class="btn btn--primary" type="submit">Сохранить изменения</button><a class="btn btn--ghost" href="user-home.html">Отменить</a></div>
        </form>
"""
write("user-profile.html", account_page("Профиль — читатель", "Капитолина", "Читатель", USER_NAV, "Профиль", "avatar 4.svg", prof(True)))
write("user-profile-empty.html", account_page("Профиль — пустой аватар", "Капитолина", "Читатель", USER_NAV, "Профиль", "avatar 24.svg", prof(False)))

# ---- manager-users re-gen with toolbar+add/edit actions ----
from _gen2_data import users_table_fn, toolbar
c = f"""        <h2 class="section-title">Пользователи</h2>
{toolbar}        <div class="table-wrap">
{users_table_fn("manager-user-detail.html")}        </div>
"""
write("manager-users.html", account_page("Пользователи — менеджер", "Елена", "Библиотекарь", MANAGER_NAV, "Пользователи", "avatar 7.svg", c))
print("PART6 OK")
