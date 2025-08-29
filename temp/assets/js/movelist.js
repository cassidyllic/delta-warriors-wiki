function toggleVariants(moveElement) {
  const variants = moveElement.querySelector(".variants");
  const arrow = moveElement.querySelector(".move-arrow");

  if (variants && arrow) {
    moveElement.classList.toggle("expanded");
    variants.classList.toggle("expanded");
    arrow.classList.toggle("rotated");
  }
}
