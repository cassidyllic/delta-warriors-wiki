document.addEventListener("DOMContentLoaded", function () {
  const imgs = document.querySelectorAll("img[class]");

  imgs.forEach((img) => {
    const imgURL = img.getAttribute("src");

    fetch(imgURL)
      .then((res) => res.text())
      .then((data) => {
        const parser = new DOMParser();
        const svgDoc = parser.parseFromString(data, "image/svg+xml");
        const svg = svgDoc.querySelector("svg");

        if (svg) {
          img.classList.forEach((cls) => svg.classList.add(cls));

          ["width", "height", "alt", "title"].forEach((attr) => {
            if (img.hasAttribute(attr)) {
              svg.setAttribute(attr, img.getAttribute(attr));
            }
          });

          const computedStyle = getComputedStyle(img);
          svg.style.color = computedStyle.color;
          svg.style.cssFloat = computedStyle.float;

          img.replaceWith(svg);
        }
      })
      .catch(console.error);
  });
});
