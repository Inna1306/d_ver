# -*- coding: utf-8 -*-
from _common import *

def modal(title, inner, back="index.html", width=None):
    style = f' style="width:{width}"' if width else ''
    body = f"""<div class="modal-page">
  <div class="modal"{style}>
    <button class="modal__close" type="button" onclick="location.href='{back}'">&#10005;</button>
    <h2 class="modal__title">{title}</h2>
{inner}
  </div>
</div>
"""
    return page(title, body, topbar=False, footer=False)

FLD = """          <div class="field field--full">
            <label class="field__label">{label}</label>
            <input class="field__input" type="{typ}" placeholder="{ph}" value="{val}">
          </div>
"""

# ---------- login popup ----------
lg = """        <form class="form" action="user-home.html" method="get">
          <p class="empty__text" style="margin-bottom:24px">Войдите в аккаунт, чтобы бронировать книги и управлять ими.</p>
          <div class="field field--full">
            <label class="field__label" for="l-mail">Электронная почта</label>
            <input class="field__input" id="l-mail" type="email" placeholder="mail@example.com">
          </div>
          <div class="field field--full">
            <label class="field__label" for="l-pass">Пароль</label>
            <input class="field__input" id="l-pass" type="password" placeholder="Введите пароль">
          </div>
          <label class="check"><input type="checkbox"> Запомнить меня</label>
          <div class="modal__actions modal__actions--center" style="margin-top:24px">
            <a class="btn btn--ghost" href="modal-signup.html">Регистрация</a>
            <button class="btn btn--primary" type="submit">Войти</button>
          </div>
        </form>
"""
write("login.html", modal("Вход в аккаунт", lg, back="index.html"))

# ---------- signup ----------
su = """        <form class="form" action="user-home.html" method="get">
          <div class="field field--full"><label class="field__label">ФИО</label><input class="field__input" placeholder="Введите ФИО"></div>
          <div class="field field--full"><label class="field__label">Электронная почта</label><input class="field__input" type="email" placeholder="mail@example.com"></div>
          <div class="field field--full"><label class="field__label">Телефон</label><input class="field__input" type="tel" placeholder="+7 (___) ___-__-__"></div>
          <div class="field field--full"><label class="field__label">Пароль</label><input class="field__input" type="password" placeholder="Придумайте пароль"></div>
          <div class="field field--full"><label class="field__label">Повторите пароль</label><input class="field__input" type="password" placeholder="Повторите пароль"></div>
          <label class="check"><input type="checkbox" checked> Соглашаюсь с обработкой персональных данных</label>
          <div class="modal__actions modal__actions--center" style="margin-top:24px">
            <a class="btn btn--ghost" href="login.html">Уже есть аккаунт</a>
            <button class="btn btn--primary" type="submit">Зарегистрироваться</button>
          </div>
        </form>
"""
write("modal-signup.html", modal("Регистрация", su, back="login.html"))

# ---------- add user (admin) ----------
au = """        <form class="form">
          <div class="field field--full"><label class="field__label">ФИО</label><input class="field__input" placeholder="Введите ФИО"></div>
          <div class="field field--full"><label class="field__label">Электронная почта</label><input class="field__input" type="email" placeholder="mail@example.com"></div>
          <div class="field field--full"><label class="field__label">Телефон</label><input class="field__input" type="tel" placeholder="+7 ..."></div>
          <div class="field field--full">
            <label class="field__label">Роль</label>
            <select class="field__input"><option>Клиент</option><option>Библиотекарь</option><option>Администратор</option></select>
          </div>
          <div class="field field--full"><label class="field__label">Пароль</label><input class="field__input" type="password" placeholder="Временный пароль"></div>
          <div class="modal__actions modal__actions--center" style="margin-top:24px">
            <a class="btn btn--ghost" href="admin-users.html">Отменить</a>
            <button class="btn btn--primary" type="submit">Добавить пользователя</button>
          </div>
        </form>
"""
write("modal-add-user.html", modal("Добавить пользователя", au, back="admin-users.html"))

# ---------- edit user ----------
eu = """        <form class="form">
          <div class="field field--full"><label class="field__label">ID</label><input class="field__input" value="12" disabled></div>
          <div class="field field--full"><label class="field__label">ФИО</label><input class="field__input" value="Смирнова Анна Викторовна"></div>
          <div class="field field--full"><label class="field__label">Электронная почта</label><input class="field__input" value="anna.smirnova@example.com"></div>
          <div class="field field--full"><label class="field__label">Телефон</label><input class="field__input" value="+79012345678"></div>
          <div class="field field--full">
            <label class="field__label">Роль</label>
            <select class="field__input"><option selected>Клиент</option><option>Библиотекарь</option><option>Администратор</option></select>
          </div>
          <div class="modal__actions modal__actions--center" style="margin-top:24px">
            <a class="btn btn--ghost" href="admin-users.html">Отменить</a>
            <button class="btn btn--primary" type="submit">Сохранить изменения</button>
          </div>
        </form>
"""
write("modal-edit-user.html", modal("Редактировать пользователя", eu, back="admin-users.html"))

# ---------- confirm delete user ----------
du = """        <p class="empty__text" style="margin-bottom:24px">Вы уверены, что хотите удалить пользователя <b>«Иванов Сергей Петрович»</b>? Действие нельзя отменить.</p>
        <div class="modal__actions modal__actions--center">
          <a class="btn btn--ghost" href="admin-users.html">Отменить</a>
          <a class="btn btn--danger" href="admin-users.html">Удалить пользователя</a>
        </div>
"""
write("modal-confirm-delete-user.html", modal("Подтвердите удаление", du, back="admin-users.html"))

# ---------- add book ----------
ab = """        <form class="form">
          <div class="field field--full"><label class="field__label">Название книги</label><input class="field__input" placeholder="Введите название"></div>
          <div class="field field--full"><label class="field__label">Автор</label><input class="field__input" placeholder="Введите автора"></div>
          <div class="field field--full"><label class="field__label">Год выпуска</label><input class="field__input" type="number" placeholder="2025"></div>
          <div class="field field--full"><label class="field__label">Библиотека</label>
            <select class="field__input"><option>Библиотека им. А. С. Пушкина</option><option>Библиотека-читальня им. И. С. Тургенева</option><option>Центральная городская библиотека им. Н.А. Некрасова</option></select>
          </div>
          <div class="field field--full"><label class="field__label">Количество экземпляров</label>
            <div class="stepper"><button type="button">&minus;</button><output>10</output><button type="button">+</button></div>
          </div>
          <div class="field field--full"><label class="field__label">Описание книги</label><textarea class="field__input" rows="3" placeholder="Введите описание"></textarea></div>
          <div class="field field--full"><label class="field__label">Обложка книги</label>
            <div class="upload"><button class="btn btn--sm btn--ghost" type="button">Выберите файл</button><span class="empty__text">Загрузите обложку книги</span></div>
          </div>
          <div class="modal__actions modal__actions--center" style="margin-top:24px">
            <a class="btn btn--ghost" href="manager-catalog.html">Отменить</a>
            <button class="btn btn--primary" type="submit">Добавить книгу</button>
          </div>
        </form>
"""
write("modal-add-book.html", modal("Добавить книгу", ab, back="manager-catalog.html"))

# ---------- edit book ----------
eb = """        <form class="form">
          <div class="field field--full"><label class="field__label">Название книги</label><input class="field__input" value="Мастер и Маргарита"></div>
          <div class="field field--full"><label class="field__label">Автор</label><input class="field__input" value="Булгаков М.А.."></div>
          <div class="field field--full"><label class="field__label">Год выпуска</label><input class="field__input" type="number" value="1967"></div>
          <div class="field field--full"><label class="field__label">Библиотека</label>
            <select class="field__input"><option selected>Библиотека им. А. С. Пушкина</option><option>Библиотека-читальня им. И. С. Тургенева</option></select>
          </div>
          <div class="field field--full"><label class="field__label">Количество экземпляров</label>
            <div class="stepper"><button type="button">&minus;</button><output>20</output><button type="button">+</button></div>
          </div>
          <div class="field field--full"><label class="field__label">Описание книги</label><textarea class="field__input" rows="3">Фантастический роман о визите дьявола в Москву 1930-х годов.</textarea></div>
          <div class="field field--full"><label class="field__label">Обложка книги</label>
            <div class="upload"><button class="btn btn--sm btn--ghost" type="button">Выберите файл</button><span class="empty__text">book_cover.jpg</span></div>
          </div>
          <div class="modal__actions modal__actions--center" style="margin-top:24px">
            <a class="btn btn--ghost" href="manager-catalog.html">Отменить</a>
            <button class="btn btn--primary" type="submit">Сохранить изменения</button>
          </div>
        </form>
"""
write("modal-edit-book.html", modal("Редактировать книгу", eb, back="manager-catalog.html"))

# ---------- confirm delete book ----------
db = """        <p class="empty__text" style="margin-bottom:24px">Вы уверены, что хотите удалить книгу <b>«Мастер и Маргарита»</b> из библиотеки? Действие нельзя отменить.</p>
        <div class="modal__actions modal__actions--center">
          <a class="btn btn--ghost" href="manager-catalog.html">Отменить</a>
          <a class="btn btn--danger" href="manager-catalog.html">Удалить книгу</a>
        </div>
"""
write("modal-confirm-delete-book.html", modal("Подтвердите удаление", db, back="manager-catalog.html"))

# ---------- add library ----------
al = """        <form class="form">
          <div class="field field--full"><label class="field__label">Название</label><input class="field__input" placeholder="Введите название библиотеки"></div>
          <div class="field field--full"><label class="field__label">Адрес</label><input class="field__input" placeholder="Введите адрес"></div>
          <div class="field field--full"><label class="field__label">Описание</label><textarea class="field__input" rows="3" placeholder="Введите описание"></textarea></div>
          <div class="modal__actions modal__actions--center" style="margin-top:24px">
            <a class="btn btn--ghost" href="admin-libraries.html">Отменить</a>
            <button class="btn btn--primary" type="submit">Добавить библиотеку</button>
          </div>
        </form>
"""
write("modal-add-library.html", modal("Добавить библиотеку", al, back="admin-libraries.html"))

# ---------- edit library ----------
el = """        <form class="form">
          <div class="field field--full"><label class="field__label">Название</label><input class="field__input" value="Библиотека им. А. С. Пушкина"></div>
          <div class="field field--full"><label class="field__label">Адрес</label><input class="field__input" value="ул. Тверская, 25"></div>
          <div class="field field--full"><label class="field__label">Описание</label><textarea class="field__input" rows="3">Крупная центральная библиотека, специализируется на классике и редких изданиях.</textarea></div>
          <div class="modal__actions modal__actions--center" style="margin-top:24px">
            <a class="btn btn--ghost" href="admin-libraries.html">Отменить</a>
            <button class="btn btn--primary" type="submit">Сохранить изменения</button>
          </div>
        </form>
"""
write("modal-edit-library.html", modal("Редактировать библиотеку", el, back="admin-libraries.html"))

# ---------- confirm delete library ----------
dl = """        <p class="empty__text" style="margin-bottom:24px">Вы уверены, что хотите удалить <b>«Библиотеку им. А. С. Пушкина»</b>? Все книги библиотеки будут удалены. Действие нельзя отменить.</p>
        <div class="modal__actions modal__actions--center">
          <a class="btn btn--ghost" href="admin-libraries.html">Отменить</a>
          <a class="btn btn--danger" href="admin-libraries.html">Удалить библиотеку</a>
        </div>
"""
write("modal-confirm-delete-library.html", modal("Подтвердите удаление", dl, back="admin-libraries.html"))

# ---------- confirm cancel booking ----------
cc = """        <p class="empty__text" style="margin-bottom:24px">Вы уверены, что хотите отменить бронь на книгу <b>«Мастер и Маргарита»</b>?</p>
        <div class="modal__actions modal__actions--center">
          <a class="btn btn--ghost" href="active-bookings.html">Отменить</a>
          <a class="btn btn--danger" href="active-bookings.html">Отменить бронь</a>
        </div>
"""
write("modal-confirm-cancel-booking.html", modal("Подтвердите отмену брони", cc, back="active-bookings.html"))

# ---------- change password ----------
cp = """        <form class="form">
          <div class="field field--full"><label class="field__label">Текущий пароль</label><input class="field__input" type="password" placeholder="Введите текущий пароль"></div>
          <div class="field field--full"><label class="field__label">Новый пароль</label><input class="field__input" type="password" placeholder="Введите новый пароль"></div>
          <div class="field field--full"><label class="field__label">Повторите новый пароль</label><input class="field__input" type="password" placeholder="Повторите новый пароль"></div>
          <div class="modal__actions modal__actions--center" style="margin-top:24px">
            <a class="btn btn--ghost" href="user-profile.html">Отменить</a>
            <button class="btn btn--primary" type="submit">Сменить пароль</button>
          </div>
        </form>
"""
write("modal-change-password.html", modal("Смена пароля", cp, back="user-profile.html"))
print("PART4 OK")
