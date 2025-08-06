document.addEventListener("DOMContentLoaded", function () {
  const path =
    window.location.pathname
      .replace(/\/$/, "")
      .replace(/^\/|\/$/g, "")
      .replace(/\//g, "-") || "index";

  document.body.classList.add(`page-${path}`);
});
