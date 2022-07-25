function like(productId) {
  const likeCount = document.getElementById(`likes-count-${productId}`);
  const likeButton = document.getElementById(`like-button-${productId}`);

  fetch(`/like-post/${productId}`, { method: "POST" }).then((res) => res.json()).then((data) => console.log(data));

  console.log(likeCount.value);
}
