---
layout: photos
title: Analog Photos
---

<div id="myModal" class="modal">
    <span class="close" onclick="closeModal()">&times;</span>
    <div class="modal-content">
        <div class="mySlides">
            <img src="{{ '/assets/images/analog/analog-13.webp' | relative_url }}"
                class="modal-image-vertical">
        </div>
        <div class="mySlides">
            <img src="{{ '/assets/images/analog/analog-14.webp' | relative_url }}"
                class="modal-image-horizontal">
        </div>
        <div class="mySlides">
            <img src="{{ '/assets/images/analog/analog-7.webp' | relative_url }}"
                class="modal-image-vertical">
        </div>
        <div class="mySlides">
            <img src="{{ '/assets/images/analog/analog-1.webp' | relative_url }}"
                class="modal-image-horizontal">
        </div>
        <div class="mySlides">
            <img src="{{ '/assets/images/analog/analog-5.webp' | relative_url }}"
                class="modal-image-vertical">
        </div>
        <div class="mySlides">
            <img src="{{ '/assets/images/analog/analog-9.webp' | relative_url }}"
                class="modal-image-horizontal">
        </div>
        <div class="mySlides">
            <img src="{{ '/assets/images/analog/analog-11.webp' | relative_url }}" class="modal-image-square">
        </div>
        <div class="mySlides">
            <img src="{{ '/assets/images/analog/analog-6.webp' | relative_url }}" class="modal-image-square">
        </div>
        <div class="mySlides">
            <img src="{{ '/assets/images/analog/analog-10.webp' | relative_url }}" class="modal-image-square">
        </div>
        <div class="mySlides">
            <img src="{{ '/assets/images/analog/analog-4.webp' | relative_url }}"
                class="modal-image-vertical">
        </div>
        <div class="mySlides">
            <img src="{{ '/assets/images/analog/analog-15.webp' | relative_url }}"
                class="modal-image-horizontal">
        </div>
        <div class="mySlides">
            <img src="{{ '/assets/images/analog/analog-16.webp' | relative_url }}"
                class="modal-image-vertical">
        </div>
        <div class="mySlides">
            <img src="{{ '/assets/images/analog/analog-8.webp' | relative_url }}"
                class="modal-image-horizontal">
        </div>
    </div>
</div>

<div class="photo-gallery">
  <div class="row">
    <div class="column">
      <img src="{{ '/assets/images/analog/small/analog-13.webp' | relative_url }}" onclick="openModal();currentSlide(1)" loading="lazy" alt="Analog photo 1">
      <img src="{{ '/assets/images/analog/small/analog-1.webp' | relative_url }}" onclick="openModal();currentSlide(4)" loading="lazy" alt="Analog photo 4">
      <img src="{{ '/assets/images/analog/small/analog-11.webp' | relative_url }}" onclick="openModal();currentSlide(7)" loading="lazy" alt="Analog photo 7">
      <img src="{{ '/assets/images/analog/small/analog-4.webp' | relative_url }}" onclick="openModal();currentSlide(10)" loading="lazy" alt="Analog photo 10">
    </div>
    <div class="column">
      <img src="{{ '/assets/images/analog/small/analog-14.webp' | relative_url }}" onclick="openModal();currentSlide(2)" loading="lazy" alt="Analog photo 2">
      <img src="{{ '/assets/images/analog/small/analog-5.webp' | relative_url }}" onclick="openModal();currentSlide(5)" loading="lazy" alt="Analog photo 5">
      <img src="{{ '/assets/images/analog/small/analog-6.webp' | relative_url }}" onclick="openModal();currentSlide(8)" loading="lazy" alt="Analog photo 8">
      <img src="{{ '/assets/images/analog/small/analog-15.webp' | relative_url }}" onclick="openModal();currentSlide(11)" loading="lazy" alt="Analog photo 11">
      <img src="{{ '/assets/images/analog/small/analog-8.webp' | relative_url }}" onclick="openModal();currentSlide(13)" loading="lazy" alt="Analog photo 13">
    </div>
    <div class="column">
      <img src="{{ '/assets/images/analog/small/analog-7.webp' | relative_url }}" onclick="openModal();currentSlide(3)" loading="lazy" alt="Analog photo 3">
      <img src="{{ '/assets/images/analog/small/analog-9.webp' | relative_url }}" onclick="openModal();currentSlide(6)" loading="lazy" alt="Analog photo 6">
      <img src="{{ '/assets/images/analog/small/analog-10.webp' | relative_url }}" onclick="openModal();currentSlide(9)" loading="lazy" alt="Analog photo 9">
      <img src="{{ '/assets/images/analog/small/analog-16.webp' | relative_url }}" onclick="openModal();currentSlide(12)" loading="lazy" alt="Analog photo 12">
    </div>
  </div>
</div>

<div class="photos-back">
  <a href="{{ '/photos' | relative_url }}">← back to photos</a>
</div>
