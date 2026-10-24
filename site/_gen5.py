# -*- coding: utf-8 -*-
from _common import *

# ---------- index.html (main.png) ----------
main_body = """<main class="screen main">
  <div class="page">
    <section class="main__hero">
      <div>
        <h1 class="main__title">Все библиотеки Москвы&nbsp;&mdash; в&nbsp;одном сервисе</h1>
        <p class="main__text">Найдите книгу в любой библиотеке города и забронируйте её онлайн.</p>
""" + search_form() + """      </div>
      <div class="main__hero-art">
        <span class="main__shape main__shape--left"></span>
        <div class="main__illustration"><img src="assets/stack-of-books-1.svg" alt="Стопка книг" style="width:80%;margin:10%"></div>
        <span class="main__shape main__shape--right"></span>
      </div>
    </section>

    <section class="main__new" id="new">
      <div class="main__new-head">
        <h2 class="section-title">Новые поступления</h2>
        <div class="slider-arrows">
          <button class="slider-arrow" type="button" aria-label="Назад">&#8592;</button>
          <button class="slider-arrow" type="button" aria-label="Вперёд">&#8594;</button>
        </div>
      </div>
      <div class="new-slider">
"""
for b in BOOKS_JS:
    main_body += book_card(b)
main_body += """      </div>
    </section>

    <section class="main__about" id="about">
      <div class="about-art"><img src="assets/books.svg" alt="Книги"></div>
      <div>
        <h2 class="section-title">О нас</h2>
        <p>Наш сервис &mdash; это единый портал, соединяющий все крупнейшие и малые библиотеки Москвы. Здесь работают лучшие библиотекари, краеведы и историки города, бережно собирающие и описывающие книжные сокровища столицы. Через наш агрегатор вы сможете быстро найти любую книгу &mdash; от редких дореволюционных изданий до новинок современной литературы.</p>
        <p>Достаточно ввести название или автора, и система покажет, в каких библиотеках есть нужный экземпляр. Вы можете выбрать удобный филиал, забронировать книгу онлайн и забрать её в назначенное время.</p>
        <p>Сервис охватывает все округа Москвы, так что любимые книги всегда окажутся рядом.</p>
      </div>
    </section>

    <section class="main__map" id="map">
      <h2 class="section-title">Библиотеки на карте</h2>
      <div class="map-frame"><img src="assets/map.png" alt="Карта библиотек Москвы"></div>
    </section>
  </div>
</main>
"""
write("index.html", page("Библиотеки Москвы — главная", main_body))

# ---------- search.html ----------
srch = """<main class="screen">
  <div class="page">
    <div class="page__header">
      <h1 class="page__title" style="font-size:24px">Поиск книги</h1>
""" + search_form({"name": "JavaScript"}) + """    </div>
    <p class="found-count">Найдено: 4 книги</p>
    <div class="books-grid">
"""
for b in BOOKS_JS:
    srch += book_card(b)
srch += """    </div>
  </div>
</main>
"""
write("search.html", page("Поиск книги", srch))

# ---------- search-not-found.html ----------
nf = """<main class="screen">
  <div class="page">
    <div class="page__header">
      <h1 class="page__title" style="font-size:24px">Поиск книги</h1>
""" + search_form({"name": "Путь 1С-разработчика"}) + """    </div>
    <div class="empty">
      <div class="empty__icon">?</div>
      <h2 class="empty__title">По вашему запросу ничего не найдено</h2>
      <p class="empty__text">К сожалению, по указанным данным книга не найдена. Проверьте правильность написания или попробуйте изменить параметры поиска (автор, название, дата).</p>
    </div>
  </div>
</main>
"""
write("search-not-found.html", page("Ничего не найдено", nf))

# ---------- booking.html ----------
libs = [("Библиотека им. Тургенева", "Трубниковский пер., д. 17"),
        ("Библиотека им. Некрасова", "ул. Бауманская, д. 58/25"),
        ("Центральная детская библиотека им. А.С. Пушкина", "ул. Большая Черкизовская, д. 4"),
        ("Центральная городская библиотека", "ул. Бауманская, д. 58/25")]
bk = """<main class="screen">
  <div class="page">
    <h1 class="page__title">Бронирование книги &laquo;JavaScript для детей&raquo;</h1>
    <article class="book-card" style="margin-bottom:32px">
      <div class="book-card__cover"><img src="assets/book-1.svg" alt="JavaScript для детей"></div>
      <div class="book-card__body">
        <h3 class="book-card__title">JavaScript для детей</h3>
        <p class="book-card__row"><b>Ник Морган</b></p>
        <p class="book-card__row"><span>2014</span></p>
        <p class="book-card__row">Эта книга позволит вам погрузиться в программирование и с легкостью освоить JavaScript. Вы напишете несколько настоящих игр &mdash; поиск сокровищ на карте, &laquo;Виселицу&raquo; и &laquo;Змейку&raquo;.</p>
      </div>
    </article>
    <form action="confirm-booking.html" method="get">
      <h2 class="section-title">Выберите библиотеку</h2>
      <div class="booking-lib-grid">
"""
for i, (n, ad) in enumerate(libs):
    bk += f'        <label class="lib-option"><input type="radio" name="library" value="{n}" {"checked" if i==1 else ""}><span><strong>{n}</strong><span>{ad}</span></span></label>\n'
bk += """      </div>
      <h2 class="section-title">Выберите период бронирования</h2>
      <div class="period-grid">
        <div class="field">
          <label class="field__label" for="b-out">Выдача книги</label>
          <input class="field__input" id="b-out" name="issue" type="date" value="2025-09-12">
        </div>
        <div class="field">
          <label class="field__label" for="b-ret">Возврат книги</label>
          <input class="field__input" id="b-ret" name="return" type="date" value="2025-09-26">
        </div>
      </div>
      <div class="modal__actions"><button class="btn btn--primary" type="submit">Забронировать</button><a class="btn btn--ghost" href="search.html">Отменить</a></div>
    </form>
  </div>
</main>
"""
write("booking.html", page("Бронирование книги", bk))

# ---------- confirm-booking.html ----------
cb = """<main class="screen">
  <div class="page">
    <div class="confirm-box">
      <h1 class="page__title">Бронирование успешно оформлено!</h1>
      <p class="empty__text">Книга будет ожидать вас в выбранной библиотеке.</p>
      <ul class="confirm-list">
        <li><span class="check-round">&#10003;</span> JavaScript для детей / Ник Морган</li>
        <li><span class="check-round">&#10003;</span> Библиотека им. Некрасова / ул. Бауманская, д. 58/25</li>
        <li><span class="check-round">&#10003;</span> Дата получения: 12.09.2025 / Дата возврата: 26.09.2025</li>
      </ul>
      <p class="empty__text">Пожалуйста, заберите книгу в указанный срок. Если вы не успеете, бронь автоматически снимется.</p>
      <div class="modal__actions modal__actions--center">
        <a class="btn btn--primary" href="active-bookings.html">Мои бронирования</a>
        <a class="btn btn--ghost" href="index.html">На главную</a>
      </div>
    </div>
  </div>
</main>
"""
write("confirm-booking.html", page("Бронирование оформлено", cb))

# ---------- active-bookings.html ----------
ab = """<main class="screen">
  <div class="page">
    <h1 class="page__title">Активные бронирования</h1>
    <div class="welcome-stats" style="margin-bottom:32px">
      <div class="stat"><strong>12</strong><span>Вы забронировали книг</span></div>
      <div class="stat"><strong>0</strong><span>Сейчас у вас активных бронирований</span></div>
    </div>
    <div class="empty">
      <div class="empty__icon">!</div>
      <h2 class="empty__title">У вас нет активных броней</h2>
      <p class="empty__text">Найдите книгу и забронируйте её!</p>
      <div class="modal__actions modal__actions--center"><a class="btn btn--primary" href="search.html">Найти книгу</a></div>
    </div>
  </div>
</main>
"""
write("active-bookings.html", page("Активные бронирования", ab))

# ---------- 404.html ----------
e404 = """<main class="screen">
  <div class="page error-404">
    <div class="error-404__art"><img src="assets/amorphous-shape-1.svg" alt="" style="width:100%"></div>
    <div class="error-404__code">404</div>
    <h1 class="page__title" style="font-size:28px">Ошибка</h1>
    <p class="empty__text">Упс, кажется что-то пошло не&nbsp;так</p>
    <div class="modal__actions modal__actions--center"><a class="btn btn--primary" href="index.html">Вернуться на главную</a></div>
  </div>
</main>
"""
write("404.html", page("404 — страница не найдена", e404))
print("PART5 OK")
