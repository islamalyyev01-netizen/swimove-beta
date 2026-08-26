(() => {
  const root = document.querySelector('[data-viz]');
  if (!root) return;

  const tabs = Array.from(root.querySelectorAll('[data-panel]'));
  const panels = Array.from(root.querySelectorAll('[data-panel-view]'));

  const activate = (id) => {
    tabs.forEach((tab) => {
      const on = tab.getAttribute('data-panel') === id;
      tab.classList.toggle('is-active', on);
      tab.setAttribute('aria-selected', on ? 'true' : 'false');
    });

    panels.forEach((panel) => {
      const on = panel.getAttribute('data-panel-view') === id;
      panel.classList.toggle('is-hidden', !on);
      panel.hidden = !on;
      if (on) {
        panel.classList.remove('is-replay');
        // retrigger bar / zone animations
        void panel.offsetWidth;
        panel.classList.add('is-replay');
      }
    });
  };

  tabs.forEach((tab) => {
    tab.addEventListener('click', () => activate(tab.getAttribute('data-panel')));
  });

  // first paint animation
  const first = root.querySelector('[data-panel-view="volume"]');
  if (first) first.classList.add('is-replay');
})();
