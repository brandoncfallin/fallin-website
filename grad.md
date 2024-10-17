---
layout: photos
title: Grad Photos
---

<div id="myModal" class="modal">
  <span class="close" onclick="closeModal()">&times;</span>
  <div class="modal-content">
    {% for i in (1..12) %}
      <div class="mySlides">
        <img src="{{ '/assets/images/grad/grad-' | append: i | append: '.webp' | relative_url }}" class="modal-image-{% if i == 10 or i == 12 or i == 4 or i == 3 or i == 1 or i == 9 %}horizontal{% else %}vertical{% endif %}">
      </div>
    {% endfor %}
  </div>
</div>

<div class="photo-gallery">
  <div class="row">
    <div class="column">
      <img src="{{ '/assets/images/grad/small/grad-13.webp' | relative_url }}" onclick="openModal();currentSlide(1)" loading="lazy" alt="Grad photo 1">
      <img src="{{ '/assets/images/grad/small/grad-4.webp' | relative_url }}" onclick="openModal();currentSlide(4)" loading="lazy" alt="Grad photo 4">
      <img src="{{ '/assets/images/grad/small/grad-5.webp' | relative_url }}" onclick="openModal();currentSlide(7)" loading="lazy" alt="Grad photo 7">
    </div>
    <div class="column">
      <img src="{{ '/assets/images/grad/small/grad-10.webp' | relative_url }}" onclick="openModal();currentSlide(2)" loading="lazy" alt="Grad photo 2">
      <img src="{{ '/assets/images/grad/small/grad-12.webp' | relative_url }}" onclick="openModal();currentSlide(5)" loading="lazy" alt="Grad photo 5">
      <img src="{{ '/assets/images/grad/small/grad-15.webp' | relative_url }}" onclick="openModal();currentSlide(8)" loading="lazy" alt="Grad photo 8">
      <img src="{{ '/assets/images/grad/small/grad-1.webp' | relative_url }}" onclick="openModal();currentSlide(10)" loading="lazy" alt="Grad photo 10">
      <img src="{{ '/assets/images/grad/small/grad-9.webp' | relative_url }}" onclick="openModal();currentSlide(11)" loading="lazy" alt="Grad photo 11">
    </div>
    <div class="column">
      <img src="{{ '/assets/images/grad/small/grad-14.webp' | relative_url }}" onclick="openModal();currentSlide(3)" loading="lazy" alt="Grad photo 3">
      <img src="{{ '/assets/images/grad/small/grad-8.webp' | relative_url }}" onclick="openModal();currentSlide(6)" loading="lazy" alt="Grad photo 6">
      <img src="{{ '/assets/images/grad/small/grad-3.webp' | relative_url }}" onclick="openModal();currentSlide(9)" loading="lazy" alt="Grad photo 9">
      <img src="{{ '/assets/images/grad/small/grad-11.webp' | relative_url }}" onclick="openModal();currentSlide(12)" loading="lazy" alt="Grad photo 12">
    </div>
  </div>
</div>

<div class="photos-back">
  <a href="{{ '/photos' | relative_url }}">← back to photos</a>
</div>
