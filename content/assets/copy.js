// Copy buttons: <button class="copy-btn" data-copy="#target"> copies the target's exact text (newlines kept).
function copyBySelection(target) {
  // Fallback for browsers/frames that block navigator.clipboard.
  const range = document.createRange();
  range.selectNodeContents(target);
  const selection = window.getSelection();
  selection.removeAllRanges();
  selection.addRange(range);
  const ok = document.execCommand("copy");
  selection.removeAllRanges();
  return ok;
}

document.addEventListener("click", async (event) => {
  const button = event.target.closest(".copy-btn");
  if (!button) return;
  const target = document.querySelector(button.dataset.copy);
  if (!target) return;
  const label = button.dataset.label || (button.dataset.label = button.textContent);
  let ok = false;
  try {
    await navigator.clipboard.writeText(target.innerText.trim());
    ok = true;
  } catch {
    ok = copyBySelection(target);
  }
  button.textContent = ok ? "Copied ✓" : "Copy failed: select the text manually";
  setTimeout(() => (button.textContent = label), 1800);
});
