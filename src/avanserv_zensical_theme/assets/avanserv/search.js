// Zensical's search dialog is a shadow root that pins --letter-spacing to -0.5px on its own
// root, so an inherited value cannot reach it. Spline Sans needs its default spacing, or the
// gaps between words close up; this adds one rule to that shadow root once it exists.
(() => {
  const sheet = new CSSStyleSheet();
  sheet.replaceSync(".r { --letter-spacing: normal; }");

  const adopt = () => {
    for (const host of document.body.children) {
      const root = host.shadowRoot;
      if (root && !root.adoptedStyleSheets.includes(sheet)) {
        root.adoptedStyleSheets = [...root.adoptedStyleSheets, sheet];
      }
    }
  };

  adopt();
  new MutationObserver(adopt).observe(document.body, { childList: true });
})();
