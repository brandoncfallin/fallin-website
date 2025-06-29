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

<div class="photoswipe-gallery">
	<div class="row">
	<div class="column">
			{% include photo.html
			url="/assets/images/digital/small/digital-4.webp"
			class="large-version"
			%}
			{% include photo.html
			url="/assets/images/digital/small/digital-13.webp"
			class="large-version"
			%}
			{% include photo.html
			url="/assets/images/digital/small/digital-15.webp"
			class="large-version"
			%}
			{% include photo.html
			url="/assets/images/digital/small/digital-6.webp"
			class="large-version"
			%}
	</div>
	<div class="column">
		{% include photo.html
		url="/assets/images/digital/small/digital-14.webp"
		class="large-version"
		%}
		{% include photo.html
			url="/assets/images/digital/small/digital-9.webp"
			class="large-version"
		%}
		{% include photo.html
			url="/assets/images/digital/small/digital-3.webp"
			class="large-version"
		%}
		{% include photo.html
			url="/assets/images/digital/small/digital-8.webp"
			class="large-version"
		%}
	</div>
	<div class="column">
		{% include photo.html
		url="/assets/images/digital/small/digital-16.webp"
		class="large-version"
		%}
		{% include photo.html
			url="/assets/images/digital/small/digital-5.webp"
			class="large-version"
		%}
		{% include photo.html
			url="/assets/images/digital/small/digital-7.webp"
			class="large-version"
		%}
		{% include photo.html
			url="/assets/images/digital/small/digital-2.webp"
			class="large-version"
		%}
	</div>
</div>

<div class="photos-back">
  <a href="{{ '/photos' | relative_url }}">← back to photos</a>
</div>
