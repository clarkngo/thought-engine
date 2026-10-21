// Light/dark toggle. Saves the choice; with no saved choice the site follows the system setting.
(() => {
  const root = document.documentElement;
  const button = document.querySelector(".theme-toggle");
  if (!button) return;
  const systemDark = window.matchMedia("(prefers-color-scheme: dark)");
  const current = () => root.dataset.theme || (systemDark.matches ? "dark" : "light");

  function render() {
    const next = current() === "dark" ? "light" : "dark";
    button.querySelector("span").textContent = next === "light" ? "☀" : "☾";
    button.setAttribute("aria-label", `Switch to ${next} mode`);
    button.title = `Switch to ${next} mode`;
  }

  button.addEventListener("click", () => {
    const next = current() === "dark" ? "light" : "dark";
    root.dataset.theme = next;
    try { localStorage.setItem("theme", next); } catch {}
    render();
  });
  systemDark.addEventListener("change", render);
  render();
})();
