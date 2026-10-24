const slider = document.querySelector('#booksSlider');
const step = 547; // ширина карточки 515px + отступ 32px

document.querySelector('[data-slider-prev]').addEventListener('click', () => {
    slider.scrollBy({ left: -step, behavior: 'smooth' });
});

document.querySelector('[data-slider-next]').addEventListener('click', () => {
    slider.scrollBy({ left: step, behavior: 'smooth' });
});