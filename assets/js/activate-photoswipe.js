import PhotoSwipeLightbox from './photoswipe-lightbox.esm.js';
import PhotoSwipe from './photoswipe.esm.js';

const options = {
  gallerySelector: '.photoswipe-gallery',
  childSelector: '.photoswipe',
  pswpModule: PhotoSwipe,
  showHideAnimationType: 'none',
};

const lightbox = new PhotoSwipeLightbox(options);
lightbox.init();