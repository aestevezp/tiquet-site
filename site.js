// Tiquet's landing: things appear as they come into view, the tour's phone follows the words, and the Ask
// conversation writes itself once. Without JavaScript (or with reduced motion) everything is simply there.
(() => {
  const still = matchMedia("(prefers-reduced-motion: reduce)").matches;
  const seen = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add("in"); seen.unobserve(e.target); } }), { rootMargin: "0px 0px -10% 0px" });
  document.querySelectorAll(".reveal").forEach(el => still ? el.classList.add("in") : seen.observe(el));

  // The tour: the step in the middle of the screen chooses the phone's screen.
  const steps = [...document.querySelectorAll(".step")], shots = [...document.querySelectorAll(".pin img")];
  const pick = i => { steps.forEach(s => s.classList.toggle("on", +s.dataset.i === i)); shots.forEach(s => s.classList.toggle("on", +s.dataset.i === i)); };
  const middle = new IntersectionObserver(es => es.forEach(e => e.isIntersecting && pick(+e.target.dataset.i)), { rootMargin: "-45% 0px -45% 0px" });
  steps.forEach(s => middle.observe(s));

  // Ask: question typed, a moment of thought, the answer; then the next one.
  const chat = document.querySelector("[data-chat]");
  if (chat && !still) {
    const msgs = [...chat.querySelectorAll(".msg")];
    msgs.forEach(m => m.classList.add("wait"));
    const sleep = ms => new Promise(r => setTimeout(r, ms));
    const play = async () => {
      for (const m of msgs) {
        const t = m.querySelector(".txt") || m, full = t.textContent;
        m.classList.remove("wait");
        if (m.classList.contains("q")) {
          t.textContent = "";
          for (let i = 1; i <= full.length; i++) { t.textContent = full.slice(0, i); await sleep(22); }
          await sleep(350);
        } else {
          m.classList.add("thinking"); await sleep(700); m.classList.remove("thinking");
          const words = full.split(" "); t.textContent = "";
          for (let i = 1; i <= words.length; i++) { t.textContent = words.slice(0, i).join(" "); await sleep(45); }
          await sleep(900);
        }
      }
    };
    const once = new IntersectionObserver(es => { if (es[0].isIntersecting) { once.disconnect(); play(); } }, { threshold: 0.4 });
    once.observe(chat);
  }
})();
