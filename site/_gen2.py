# -*- coding: utf-8 -*-
from _common import *

# ================= USER ACCOUNTS (Капитолина) =================
# account user 1 — главная
c = """        <h2 class="section-title">Добро пожаловать в личный кабинет!</h2>
        <div class="welcome-stats">
          <div class="stat"><strong>12</strong><span>Вы забронировали книг</span></div>
          <div class="stat"><strong>3</strong><span>Сейчас у вас активных бронирования</span></div>
        </div>
"""
write("user-home.html", account_page("Личный кабинет — читатель", "Капитолина", "Читатель", USER_NAV, "Главная", "avatar 4.svg", c))

# account user 2 & 5 — профиль (пустой аватар / заполненный)
def profile(avatar_filled):
    av_actions = ('<div class="avatar-actions"><button class="btn btn--sm btn--ghost" type="button">&#128247; Изменить фото</button><button class="btn btn--sm btn--ghost" type="button">&#10005; Удалить фото</button></div>'
                  if avatar_filled else
                  '<div class="avatar-actions"><button class="btn btn--sm btn--ghost" type="button">&#128247; Добавить фото</button></div>')
    return f"""        <h2 class="section-title">Личная информация</h2>
        <form class="form--grid form">
          <div class="field field--full">
            <label class="field__label">ФИО</label>
            <input class="field__input" type="text" value="Власова Капитолина Владимировна">
          </div>
          <div class="field">
            <label class="field__label">Телефон</label>
            <input class="field__input" type="tel" value="+790677866543">
          </div>
          <div class="field">
            <label class="field__label">Почта</label>
            <input class="field__input" type="email" value="valsova_kap@mail.com">
          </div>
          <div class="field">
            <label class="field__label">Пароль</label>
            <input class="field__input" type="password" value="********">
          </div>
          <div class="field">
            <label class="field__label">Аватар</label>
            <img class="avatar" style="width:80px;height:80px" src="assets/avatars/{'avatar 4.svg' if avatar_filled else 'avatar 24.svg'}" alt="Аватар">
            {av_actions}
          </div>
          <div class="modal__actions field--full"><button class="btn btn--primary" type="submit">Сохранить изменения</button><a class="btn btn--ghost" href="user-home.html">Отменить</a></div>
        </form>
"""
write("user-profile.html", account_page("Профиль — читатель", "Капитолина", "Читатель", USER_NAV, "Профиль", "avatar 4.svg", profile(True)))
write("user-profile-empty.html", account_page("Профиль — читатель (пустой аватар)", "Капитолина", "Читатель", USER_NAV, "Профиль", "avatar 24.svg", profile(False)))

# account user 3 — мои книги с таблицей
rows_active = [(1,"book-5.svg","Мастер и Маргарита","М.А. Булгаков","Центральная городская библиотека им. Н.А. Некрасова","10.08.2025","25.08.2025","забронирована"),
               (2,"book-6.svg","Братья Карамазовы","Ф.М. Достоевский","Центральная городская библиотека им. Н.А. Некрасова","15.04.2025","30.04.2025","возвращена"),
               (3,"book-1.svg","Путь жизни","Л.Н. Толстой","Библиотека-читальня им. И.С. Тургенева","05.09.2024","28.09.2024","возвращена"),
               (4,"book-2.svg","Мёртвые души","Н.В. Гоголь","Библиотека-читальня им. И.С. Тургенева","12.03.2024","02.04.2024","возвращена"),
               (5,"book-3.svg","Евгений Онегин","А.С. Пушкин","Центральная городская библиотека им. Н.А. Некрасова","22.10.2023","05.11.2023","возвращена")]
c = f"""        <h2 class="section-title">Мои книги</h2>
{CHIPS_BOOKS}        <div class="table-wrap">
{books_table(rows_active)}        </div>
"""
write("user-books.html", account_page("Мои книги — читатель", "Капитолина", "Читатель", USER_NAV, "Мои книги", "avatar 4.svg", c))

# account user 4 — пустые мои книги
c = """        <h2 class="section-title">Мои книги</h2>
        <div class="empty">
          <div class="empty__icon">!</div>
          <h3 class="empty__title" style="font-size:22px">У вас нет активных броней</h3>
          <p class="empty__text">Найдите книгу и забронируйте её!</p>
          <div class="modal__actions modal__actions--center"><a class="btn btn--primary" href="search.html">Найти книгу</a></div>
        </div>
"""
write("user-books-empty.html", account_page("Мои книги пусты — читатель", "Капитолина", "Читатель", USER_NAV, "Мои книги", "avatar 4.svg", c))

# ================= MANAGER ACCOUNTS (Елена) =================
c = """        <h2 class="section-title">Добро пожаловать в админ-панель!</h2>
        <div class="welcome-stats">
          <div class="stat"><strong>10 347</strong><span>Всего пользователей</span></div>
          <div class="stat"><strong>2 057 898</strong><span>Всего книг в системе</span></div>
          <div class="stat"><strong>983</strong><span>С активными бронированиями</span></div>
        </div>
"""
write("manager-home.html", account_page("Менеджер — главная", "Елена", "Библиотекарь", MANAGER_NAV, "Главная", "avatar 7.svg", c))

# manager settings (2 — пустой, 8 — заполненный)
def m_settings(filled):
    val = ("Гуськова Елена Михайловна", "+790296866516", "elena_gus@mail.com") if filled else ("", "", "")
    av_actions = ('<div class="avatar-actions"><button class="btn btn--sm btn--ghost" type="button">&#128247; Изменить фото</button><button class="btn btn--sm btn--ghost" type="button">&#10005; Удалить фото</button></div>'
                  if filled else '<div class="avatar-actions"><button class="btn btn--sm btn--ghost" type="button">&#128247; Добавить фото</button></div>')
    return f"""        <h2 class="section-title">Настройки</h2>
        <form class="form--grid form">
          <div class="field field--full"><label class="field__label">ФИО</label><input class="field__input" value="{val[0]}" placeholder="Введите ФИО"></div>
          <div class="field"><label class="field__label">Телефон</label><input class="field__input" value="{val[1]}" placeholder="+7 ..."></div>
          <div class="field"><label class="field__label">Почта</label><input class="field__input" value="{val[2]}" placeholder="mail@example.com"></div>
          <div class="field"><label class="field__label">Пароль</label><input class="field__input" type="password" value="********"></div>
          <div class="field"><label class="field__label">Аватар</label><img class="avatar" style="width:80px;height:80px" src="assets/avatars/{'avatar 7.svg' if filled else 'avatar 25.svg'}" alt=""><br>{av_actions}</div>
          <div class="modal__actions field--full"><button class="btn btn--primary" type="submit">Сохранить изменения</button><a class="btn btn--ghost" href="manager-home.html">Отменить</a></div>
        </form>
"""
write("manager-settings.html", account_page("Настройки менеджера", "Елена", "Библиотекарь", MANAGER_NAV, "Настройки", "avatar 7.svg", m_settings(True)))
write("manager-settings-empty.html", account_page("Настройки менеджера (пустые)", "Елена", "Библиотекарь", MANAGER_NAV, "Настройки", "avatar 25.svg", m_settings(False)))

# manager users list (account manager 3)
USERS = [
    (1,"avatar 1.svg","Иванов Сергей Петрович","+79001234567","sergey.ivanov@example.com","04.09.2022","0","Клиент"),
    (12,"avatar 2.svg","Смирнова Анна Викторовна","+79012345678","anna.smirnova@example.com","10.01.2024","1","Клиент"),
    (14,"avatar 3.svg","Попова Елена Сергеевна","+79034567890","elena.popova@example.com","23.08.2025","&mdash;","Клиент"),
    (5,"avatar 5.svg","Волков Андрей Николаевич","+79045678901","andrey.volkov@example.com","12.08.2025","0","Клиент"),
    (16,"avatar 6.svg","Соколова Мария Алексеевна","+79056789012","maria.sokolova@example.com","19.05.2023","&mdash;","Клиент"),
    (17,"avatar 8.svg","Михайлов Алексей Дмитриевич","+79067890123","a.mikhailov@example.com","12.04.2024","1","Библиотекарь"),
    (18,"avatar 9.svg","Фёдорова Наталья Игоревна","+79078901234","natalia.fedorova@example.com","22.08.2025","3","Клиент"),
    (19,"avatar 10.svg","Морозов Павел Александрович","+79089012345","pavel.morozov@example.com","23.08.2025","&mdash;","Администратор"),
    (20,"avatar 11.svg","Васильева Ольга Петровна","+79090123456","olga.vasilieva@example.com","15.07.2022","0","Клиент"),
]
def users_table(with_add=True):
    t = """<table class="table">
  <thead><tr><th>ID</th><th>ФИО / Контакты</th><th>Последняя активность</th><th>Активные брони</th><th>Роль</th><th>Чат</th></tr></thead>
  <tbody>
"""
    for uid, av, fio, tel, mail, act, br, role in USERS:
        t += f"""    <tr><td>{uid}</td><td><div style="display:flex;gap:12px;align-items:center"><img class="avatar" style="width:44px;height:44px;margin:0" src="assets/avatars/{av}" alt=""><span><b>{fio}</b><br><span style="color:var(--placeholder);font-size:14px">{tel}<br>{mail}</span></span></div></td><td>{act}</td><td>{br}</td><td>{role}</td><td><a class="btn btn--sm btn--ghost" href="manager-user-detail.html">&#128172;</a></td></tr>\n"""
    t += """  </tbody>
</table>
"""
    return t

toolbar = """        <div class="toolbar">
          <input class="field__input" style="flex:1" type="search" placeholder="Поиск по ФИО, id, телефону или почту">
          <div class="role-filters">
            <label class="check"><input type="checkbox" checked> Все</label>
            <label class="check"><input type="checkbox"> Администратор</label>
            <label class="check"><input type="checkbox"> Библиотекарь</label>
            <label class="check"><input type="checkbox"> Клиент</label>
          </div>
        </div>
"""
c = f"""        <h2 class="section-title">Пользователи</h2>
{toolbar}        <div class="table-wrap">
{users_table()}        </div>
"""
write("manager-users.html", account_page("Пользователи — менеджер", "Елена", "Библиотекарь", MANAGER_NAV, "Пользователи", "avatar 7.svg", c))
write("admin-users.html", account_page("Пользователи — админ", "Константин", "Администратор", ADMIN_NAV, "Пользователи", "avatar 12.svg", toolbar.replace("</div>\n","</div>\n") + ""))
print("PART2a OK")
