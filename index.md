---
layout: default
title: Home
display_footer: true
---

<div class="home-container">
  <div class="home-sidebar">
    <div class="sidebar-sticky-content">
      <div class="profile-header">
        {% include profile_image.html %}
        <div class="profile-title">
        <h1 id="brandon-fallin" class="bottom-gone-h1">Brandon Fallin</h1>
        <h4 id="graduate-research-assistant-university-of-florida" class="bottom-gone-h4">Graduate Research Assistant @ University of Florida</h4>
        </div>
      </div>
      <p>
      I'm currently living in Gainesville, FL and working in the <a href="https://ncr.mae.ufl.edu/" target="_blank">Nonlinear Controls and Robotics (NCR) Lab</a> while pursuing my PhD. My research focuses on privacy and obfuscation with application to nonlinear control systems. I recently graduated from the <a href="https://mae.ufl.edu/" target="_blank">University of Florida</a> with a Master's degree in Aerospace Engineering and a minor in Electrical Engineering.
      </p>
      <p>
      You can download my resume <a href="/assets/pdf/fallin-resume.pdf" target="_blank">here</a>.
      </p>
      <div class="sidebar-connect">
        {% include connect.html %}
      </div>
    </div>
	</div>
  <div class="home-main">
  	<h2 id="work-experience" class="bottom-gone-h2">Work Experience</h2>
    {% include work_experience.html %}

    <h2 id="publications" class="bottom-gone-h2">Publications</h2>
    <div id="bibliography"></div>
    <script src="/assets/js/bib.js"></script>
  </div>
</div>