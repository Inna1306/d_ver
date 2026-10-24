# -*- coding: utf-8 -*-
from _common import *

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

def users_table_fn(chatlink="manager-user-detail.html"):
    t = """        <table class="table">
          <thead><tr><th>ID</th><th>ФИО / Контакты</th><th>Последняя активность</th><th>Активные брони</th><th>Роль</th><th>Чат</th></tr></thead>
          <tbody>
"""
    for uid, av, fio, tel, mail, act, br, role in USERS:
        t += f"""            <tr><td>{uid}</td><td><div style="display:flex;gap:12px;align-items:center"><img class="avatar" style="width:44px;height:44px;margin:0" src="assets/avatars/{av}" alt=""><span><b>{fio}</b><br><span style="color:var(--placeholder);font-size:14px">{tel}<br>{mail}</span></span></div></td><td>{act}</td><td>{br}</td><td>{role}</td><td><a class="btn btn--sm btn--ghost" href="{chatlink}">&#128172;</a></td></tr>\n"""
    t += """          </tbody>
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
          <a class="btn btn--primary btn--sm" href="modal-add-user.html">+ Добавить пользователя</a>
        </div>
"""
