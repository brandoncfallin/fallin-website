---
layout: photos
title: Digital Photos
---

<div id="myModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <div class="modal-content">
    <div class="mySlides">
      <img src="{{ '/assets/images/digital/digital-4.webp' | relative_url }}" class="modal-image-vertical">
    </div>
    <div class="mySlides">
      <img src="{{ '/assets/images/digital/digital-14.webp' | relative_url }}" class="modal-image-horizontal">
    </div>
    <div class="mySlides">
      <img src="{{ '/assets/images/digital/digital-16.webp' | relative_url }}" class="modal-image-vertical">
    </div>
    <div class="mySlides">
      <img src="{{ '/assets/images/digital/digital-13.webp' | relative_url }}" class="modal-image-horizontal">
    </div>
    <div class="mySlides">
      <img src="{{ '/assets/images/digital/digital-9.webp' | relative_url }}" class="modal-image-vertical">
    </div>
    <div class="mySlides">
      <img src="{{ '/assets/images/digital/digital-5.webp' | relative_url }}" class="modal-image-horizontal">
    </div>
    <div class="mySlides">
      <img src="{{ '/assets/images/digital/digital-15.webp' | relative_url }}" class="modal-image-vertical">
    </div>
    <div class="mySlides">
      <img src="{{ '/assets/images/digital/digital-3.webp' | relative_url }}" class="modal-image-horizontal">
    </div>
    <div class="mySlides">
      <img src="{{ '/assets/images/digital/digital-7.webp' | relative_url }}" class="modal-image-vertical">
    </div>
    <div class="mySlides">
      <img src="{{ '/assets/images/digital/digital-6.webp' | relative_url }}" class="modal-image-horizontal">
    </div>
    <div class="mySlides">
      <img src="{{ '/assets/images/digital/digital-8.webp' | relative_url }}" class="modal-image-vertical">
    </div>
    <div class="mySlides">
      <img src="{{ '/assets/images/digital/digital-2.webp' | relative_url }}" class="modal-image-horizontal">
    </div>
  </div>
</div>

<div class="row">
  <div class="column">
    <div class="vert-container">
      <img src="{{ '/assets/images/digital/small/digital-4.webp' | relative_url }}" onclick="openModal();currentSlide(1)" fetchpriority="high">
    </div>
    <div class="horiz-container">
      <img src="{{ '/assets/images/digital/small/digital-13.webp' | relative_url }}" onclick="openModal();currentSlide(4)" fetchpriority="high">
    </div>
    <img src="{{ '/assets/images/digital/small/digital-15.webp' | relative_url }}" onclick="openModal();currentSlide(7)" fetchpriority="high">
    <img src="{{ '/assets/images/digital/small/digital-6.webp' | relative_url }}" onclick="openModal();currentSlide(10)" fetchpriority="high">
  </div>
  <div class="column">
    <img src="{{ '/assets/images/digital/small/digital-14.webp' | relative_url }}" onclick="openModal();currentSlide(2)" fetchpriority="high">
    <img src="{{ '/assets/images/digital/small/digital-9.webp' | relative_url }}" onclick="openModal();currentSlide(5)" fetchpriority="high">
    <img src="{{ '/assets/images/digital/small/digital-3.webp' | relative_url }}" onclick="openModal();currentSlide(8)" fetchpriority="high">
    <img src="{{ '/assets/images/digital/small/digital-8.webp' | relative_url }}" onclick="openModal();currentSlide(11)" fetchpriority="high">
  </div>
  <div class="column">
    <img src="{{ '/assets/images/digital/small/digital-16.webp' | relative_url }}" onclick="openModal();currentSlide(3)" fetchpriority="high">
    <img src="{{ '/assets/images/digital/small/digital-5.webp' | relative_url }}" onclick="openModal();currentSlide(6)" fetchpriority="high">
    <img src="{{ '/assets/images/digital/small/digital-7.webp' | relative_url }}" onclick="openModal();currentSlide(9)" fetchpriority="high">
    <img src="{{ '/assets/images/digital/small/digital-2.webp' | relative_url }}" onclick="openModal();currentSlide(12)" fetchpriority="high">
  </div>
</div>

<div class="photos-back">
  <a href="{{ '/photos' | relative_url }}">← back to photos</a>
</div>
