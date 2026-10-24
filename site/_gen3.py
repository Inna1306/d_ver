# -*- coding: utf-8 -*-
from _common import *
from _gen2_data import users_table_fn, toolbar

# ---- admin-users full (toolbar + table) ----
c = f"""        <h2 class="section-title">Пользователи</h2>
{toolbar}        <div class="table-wrap">
{users_table_fn("admin-user-detail.html")}        </div>
"""
write("admin-users.html", account_page("Пользователи — админ", "Константин", "Администратор", ADMIN_NAV, "Пользователи", "avatar 12.svg", c))

CHAT = """          <aside class="chat-panel">
            <div class="chat-panel__head"><span>Чат</span><button class="btn btn--sm btn--ghost" type="button">&#10005;</button></div>
            <div class="chat-panel__body">
              <div class="chat-msg">Здравствуйте! Не могу вернуть книгу вовремя, что делать?<time>12:03</time></div>
              <div class="chat-msg chat-msg--out">Здравствуйте! Могу продлить бронь. Уточните номер брони.<time>12:07</time></div>
              <div class="chat-msg">Бронь на «Мастер и Маргарита», выдача 10.08.2025<time>12:10</time></div>
              <div class="chat-msg chat-msg--out">Спасибо, вижу вашу бронь. Хотите продлить ещё на неделю?<time>12:15</time></div>
            </div>
            <form class="chat-panel__foot"><input type="text" placeholder="Сообщение..."><button class="btn btn--sm btn--primary" type="submit">&#8594;</button></form>
          </aside>
"""

def user_detail(title_name, fio, tel, mail, reg, rows, empty=False):
    if empty:
        books = """          <div class="empty" style="padding:32px">
            <p class="empty__text">Этот пользователь пока не бронировал книги.</p>
          </div>
"""
    else:
        books = CHIPS_BOOKS + """          <div class="table-wrap">
""" + books_table(rows) + """          </div>
"""
    return f"""        <h2 class="section-title">{title_name} <span class="badge badge--active">Клиент</span></h2>
        <div class="detail-with-chat">
          <div>
            <h3 class="modal__title" style="font-size:20px">Личная информация</h3>
            <div class="confirm-card" style="margin-bottom:24px">
              <p><span>ФИО:</span> <b>{fio}</b></p>
              <p><span>Телефон:</span> {tel}</p>
              <p><span>Почта:</span> {mail}</p>
              <p><span>Роль:</span> Клиент</p>
              <p><span>Дата регистрации:</span> {reg}</p>
            </div>
            <h3 class="modal__title" style="font-size:20px">Книги пользователя</h3>
{books}          </div>
{CHAT}        </div>
"""

KUZ = [(1,"book-5.svg","Мастер и Маргарита","М.А. Булгаков","Центральная городская библиотека им. Н.А. Некрасова","10.08.2025","25.08.2025","забронирована"),
       (2,"book-6.svg","Братья Карамазовы","Ф.М. Достоевский","Центральная городская библиотека им. Н.А. Некрасова","15.04.2025","30.04.2025","возвращена"),
       (3,"book-1.svg","Путь жизни","Л.Н. Толстой","Библиотека-читальня им. И.С. Тургенева","05.09.2024","28.09.2024","возвращена"),
       (4,"book-2.svg","Мёртвые души","Н.В. Гоголь","Библиотека-читальня им. И.С. Тургенева","12.03.2024","02.04.2024","возвращена"),
       (5,"book-3.svg","Евгений Онегин","А.С. Пушкин","Центральная городская библиотека им. Н.А. Некрасова","22.10.2023","05.11.2023","возвращена")]

write("manager-user-detail.html", account_page("Кузнецов Д.О. — менеджер", "Елена", "Библиотекарь", MANAGER_NAV, "Пользователи", "avatar 7.svg",
      user_detail("Кузнецов Дмитрий Олегович","Кузнецов Дмитрий Олегович","+79001234567","d.kuznetsov@example.com","12.03.2024",KUZ)))
write("manager-user-detail-returned.html", account_page("Кузнецов Д.О. — все возвращены", "Елена", "Библиотекарь", MANAGER_NAV, "Пользователи", "avatar 7.svg",
      user_detail("Кузнецов Дмитрий Олегович","Кузнецов Дмитрий Олегович","+79001234567","d.kuznetsov@example.com","12.03.2024",
                 [(r[0],r[1],r[2],r[3],r[4],r[5],r[6],"возвращена") for r in KUZ])))
write("admin-user-detail.html", account_page("Иванов С.П. — админ", "Константин", "Администратор", ADMIN_NAV, "Пользователи", "avatar 12.svg",
      user_detail("Иванов Сергей Петрович","Иванов Сергей Петрович","+79001234567","sergey.ivanov@example.com","12.05.2024",KUZ)))
write("admin-user-empty.html", account_page("Волков А.Н. — админ", "Константин", "Администратор", ADMIN_NAV, "Пользователи", "avatar 12.svg",
      user_detail("Волков Андрей Николаевич","Волков Андрей Николаевич","+79045678901","andrey.volkov@example.com","09.05.2025",None,empty=True)))

# ---- manager-books: выбор библиотеки ----
LIBLIST = ["Библиотека им. А. С. Пушкина",
           "Библиотека-читальня им. И. С. Тургенева",
           "Центральная городская детская библиотека им. А. П. Гайдара",
           "Библиотека иностранной литературы им. М. И. Рудомино",
           "Государственная публичная историческая библиотека России"]
sel_libs = """        <h2 class="section-title">Книги</h2>
        <p class="empty__text" style="margin-bottom:24px">Выберите одну из библиотек из списка. Книга будет добавлена именно в выбранную библиотеку.</p>
        <div class="radio-list">
"""
for i,l in enumerate(LIBLIST):
    sel_libs += f'          <label class="lib-option"><input type="radio" name="lib" value="{l}" {"checked" if i==0 else ""}><strong>{l}</strong></label>\n'
sel_libs += """        </div>
        <h3 class="section-title">Информация</h3>
        <div class="info-card">
          <p><span>Название:</span> <b>Библиотека им. А. С. Пушкина</b></p>
          <p><span>Адрес:</span> ул. Тверская, 25</p>
          <p><span>Описание:</span> Крупная центральная библиотека, специализируется на классике и редких изданиях.</p>
          <p><span>Всего книг:</span> 120 000</p>
          <p><span>Доступно книг:</span> 87 500</p>
        </div>
        <div class="modal__actions"><a class="btn btn--primary" href="manager-catalog.html">Перейти к книгам</a></div>
"""
write("manager-books.html", account_page("Книги — менеджер", "Елена", "Библиотекарь", MANAGER_NAV, "Книги", "avatar 7.svg", sel_libs))

# ---- catalog tables ----
CATALOG = [
 (1,"Евгений Онегин","Пушкин А.С.","1833","Роман в стихах о судьбе «лишнего человека» Евгения Онегина и любви Татьяны Лариной. Соединяет социальную критику и тонкую психологию.",20),
 (2,"Капитанская дочка","Пушкин А.С.","1836","Историческая повесть о восстании Пугачёва и судьбе дворянина Гринева. Темы чести, верности и выбора в смутное время.",5),
 (3,"Анна Каренина","Толстой Л.Н.","1875","Трагическая история любви Анны и Вронского. Роман о моральных устоях общества и поиске смысла жизни.",3),
 (4,"Война и мир","Толстой Л.Н.","1869","Эпопея о войне 1812 года, судьбах дворянских семей и размышлениях о месте человека в истории.",16),
 (5,"Преступление и наказание","Достоевский Ф.М.","1866","История студента Раскольникова, совершившего убийство ради идеи. О совести, выборе и пути к искуплению.",12),
 (6,"Братья Карамазовы","Достоевский Ф.М.","1880","Роман о семье Карамазовых, философское исследование веры, свободы и справедливости.",8),
 (7,"Идиот","Достоевский Ф.М.","1869","Князь Мышкин — человек «с чистой душой» в мире страстей и интриг. Роман о столкновении добра и порока.",6),
 (8,"Кому на Руси жить хорошо","Некрасов Н.А.","1877","Поэма о судьбах простых людей, о поиске счастья и справедливости в России.",4),
 (9,"Мёртвые души","Гоголь Н.В.","1842","Повесть о Чичикове, скупавшем «мёртвые души» крестьян. Сатира на общество.",10),
 (10,"Герой нашего времени","Лермонтов М.Ю.","1840","История Печорина, разочарованного офицера. Один из первых психологических романов в русской литературе.",7),
]
def catalog_table():
    t = """        <div class="toolbar">
          <input class="field__input" style="flex:1" type="search" placeholder="Поиск по названию или автору">
          <a class="btn btn--primary btn--sm" href="modal-add-book.html">+ Добавить книгу</a>
        </div>
        <div class="table-wrap">
        <table class="table">
          <thead><tr><th>ID</th><th>Название</th><th>Автор</th><th>Год</th><th>Описание</th><th>Кол-во экземпляров</th><th>Действия</th></tr></thead>
          <tbody>
"""
    for bid, n, au, y, d, cnt in CATALOG:
        t += f"""            <tr><td>{bid}</td><td><b>{n}</b></td><td>{au}</td><td>{y}</td><td style="max-width:360px">{d}</td><td>{cnt}</td><td><div class="row-actions"><a class="btn btn--sm btn--ghost" href="modal-edit-book.html">&#9998;</a><a class="btn btn--sm btn--danger" href="modal-confirm-delete-book.html">&#10005;</a></div></td></tr>\n"""
    t += """          </tbody>
        </table>
        </div>
"""
    return t

INFO_PUSHKIN = """        <h2 class="section-title">Библиотека им. А. С. Пушкина <span class="badge badge--active">Редкие издания</span></h2>
        <div class="info-card" style="margin-bottom:24px">
          <h3>Информация</h3>
          <p><span>Название:</span> <b>Библиотека им. А. С. Пушкина</b></p>
          <p><span>Адрес:</span> ул. Тверская, 25</p>
          <p><span>Описание:</span> Крупная центральная библиотека, специализируется на классике и редких изданиях.</p>
          <p><span>Всего книг:</span> 120 000 &nbsp;&nbsp; <span>Доступно книг:</span> 87 500</p>
        </div>
"""
write("manager-catalog.html", account_page("Книги Пушкинской библиотеки", "Елена", "Библиотекарь", MANAGER_NAV, "Книги", "avatar 7.svg", INFO_PUSHKIN + catalog_table()))

NEKRAS = """        <h2 class="section-title">Центральная городская библиотека им. Н.А. Некрасова</h2>
        <div class="info-card" style="margin-bottom:24px">
          <h3>Информация</h3>
          <p><span>Название:</span> <b>Центральная городская библиотека им. Н.А. Некрасова</b></p>
          <p><span>Адрес:</span> ул. Бауманская, д. 58/25</p>
          <p><span>Описание:</span> Крупнейший центр чтения и современных библиотечных технологий в Москве.</p>
          <p><span>Всего книг:</span> 100 000 &nbsp;&nbsp; <span>Доступно книг:</span> 95 300</p>
        </div>
"""
write("admin-library-catalog.html", account_page("Книги библиотеки Некрасова — админ", "Константин", "Администратор", ADMIN_NAV, "Библиотеки", "avatar 12.svg", NEKRAS + catalog_table()))

# ---- admin libraries list ----
LIBS = [
 (1,"Библиотека-читальня им. И.С. Тургенева","ул. Мясницкая, д. 36/1","85 000","70 120"),
 (2,"Российская государственная библиотека (РГБ)","ул. Воздвиженка, д. 3/5","5 000 000","4 870 000"),
 (3,"Государственная публичная историческая библиотека","ул. Старосадский пер., д. 9","800 000","755 000"),
 (4,"Библиотека искусств им. А.М. Боголюбова","Сухаревская пл., д. 2","150 000","142 300"),
 (5,"Библиотека иностранной литературы им. М.И. Рудомино","ул. Николоямская, д. 6","1 200 000","1 150 400"),
 (17,"Центральная детская библиотека им. А.С. Пушкина","ул. Большая Черкизовская, д. 4","60 000","54 700"),
 (18,"Московская библиотека киноискусства","ул. Каретный Ряд, д. 5/10","40 000","36 500"),
 (19,"Библиотека № 151 имени Е. И. Чарушина","ул. Ясеневая, д. 34","25 000","21 800"),
 (20,"Библиотека № 180 имени В. В. Бианки","ул. Островитянова, д. 22","30 000","27 600"),
]
lt = """        <h2 class="section-title">Библиотеки</h2>
        <div class="toolbar">
          <input class="field__input" style="flex:1" type="search" placeholder="Поиск по названию или адресу">
          <a class="btn btn--primary btn--sm" href="modal-add-library.html">+ Добавить библиотеку</a>
        </div>
        <div class="table-wrap">
        <table class="table">
          <thead><tr><th>ID</th><th>Название</th><th>Адрес</th><th>Всего книг</th><th>Доступно</th><th>Действия</th></tr></thead>
          <tbody>
"""
for lid,n,ad,total,avail in LIBS:
    lt += f"""            <tr><td>{lid}</td><td><a href="admin-library-catalog.html"><b>{n}</b></a></td><td>{ad}</td><td>{total}</td><td>{avail}</td><td><div class="row-actions"><a class="btn btn--sm btn--ghost" href="modal-edit-library.html">&#9998;</a><a class="btn btn--sm btn--danger" href="modal-confirm-delete-library.html">&#10005;</a></div></td></tr>\n"""
lt += """          </tbody>
        </table>
        </div>
"""
write("admin-libraries.html", account_page("Библиотеки — админ", "Константин", "Администратор", ADMIN_NAV, "Библиотеки", "avatar 12.svg", lt))

# ---- admin home / settings ----
c = """        <h2 class="section-title">Добро пожаловать в админ-панель!</h2>
        <div class="welcome-stats">
          <div class="stat"><strong>239</strong><span>Всего библиотек</span></div>
          <div class="stat"><strong>2 057 898</strong><span>Всего книг в системе</span></div>
          <div class="stat"><strong>10 983</strong><span>Активные бронирования</span></div>
          <div class="stat"><strong>10 347</strong><span>Всего пользователей</span></div>
          <div class="stat"><strong>983</strong><span>С активными бронированиями</span></div>
          <div class="stat"><strong>12</strong><span>Новых сообщений</span></div>
        </div>
"""
write("admin-home.html", account_page("Админ — главная", "Константин", "Администратор", ADMIN_NAV, "Главная", "avatar 12.svg", c))

def a_settings(filled):
    val = ("Пахомов Константин Владимирович","+790672866579","pahom_kostyan@mail.com") if filled else ("","","")
    av_actions = ('<div class="avatar-actions"><button class="btn btn--sm btn--ghost" type="button">&#128247; Изменить фото</button><button class="btn btn--sm btn--ghost" type="button">&#10005; Удалить фото</button></div>'
                  if filled else '<div class="avatar-actions"><button class="btn btn--sm btn--ghost" type="button">&#128247; Добавить фото</button></div>')
    return f"""        <h2 class="section-title">Настройки</h2>
        <form class="form--grid form">
          <div class="field field--full"><label class="field__label">ФИО</label><input class="field__input" value="{val[0]}" placeholder="Введите ФИО"></div>
          <div class="field"><label class="field__label">Телефон</label><input class="field__input" value="{val[1]}" placeholder="+7 ..."></div>
          <div class="field"><label class="field__label">Почта</label><input class="field__input" value="{val[2]}" placeholder="mail@example.com"></div>
          <div class="field"><label class="field__label">Пароль</label><input class="field__input" type="password" value="********"></div>
          <div class="field"><label class="field__label">Аватар</label><img class="avatar" style="width:80px;height:80px" src="assets/avatars/{'avatar 12.svg' if filled else 'avatar 26.svg'}" alt=""><br>{av_actions}</div>
          <div class="modal__actions field--full"><button class="btn btn--primary" type="submit">Сохранить изменения</button><a class="btn btn--ghost" href="admin-home.html">Отменить</a></div>
        </form>
"""
write("admin-settings.html", account_page("Настройки админа", "Константин", "Администратор", ADMIN_NAV, "Настройки", "avatar 12.svg", a_settings(True)))
write("admin-settings-empty.html", account_page("Настройки админа (пустые)", "Константин", "Администратор", ADMIN_NAV, "Настройки", "avatar 26.svg", a_settings(False)))
print("PART3 OK")
