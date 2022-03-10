---
layout: page
title: /event
permalink: /event/
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed&display=swap');

.bodycontents {background-color: #ABC9FF;
}
.maintext {margin: 10px 10px 20px 10px;
}

h2 {color:#4C39CA; font-size: 24px; font-family: 'Roboto Condensed', sans-serif;
}
     
</style>

<div class="bodycontents">
<div class="maintext">
<h2>event, neverends </h2>
Here you can find interesting online/offline events: performances, workshop, reading group, exhibition, tour, lectures. (until June 2021)<br/>
Currently, we're posting feminist events happening in berlin via <span><a href="https://instagram.com/commaneverends" target="iframe_form">instagram </a></span> Follow us there, so we can directly connect with you and share more interesting events with you and friends! <br/>
<br/>
<iframe style="border-style: none; width:100%; height:300px;" src="https://commaneverends.github.io/table_event/index.html" frameBorder="0"></iframe>

</div>
</div>

---


<font color="red"> Send us any interesting event you wanna share. </font> 

<script data-cfasync="false" type="text/javascript" src="form-submission-handler.js"></script>

<form class="gform" method="POST" id="car_request_form" role="form" action="https://script.google.com/macros/s/AKfycbwMysNaAEAysMVrWdfiYk6VebTuwl-2aXcuTJHW/exec" target="after" onsubmit="close()">
  
<form>
  <input type="text" id="name" name="event_title" placeholder="event title:" autocomplete="off">
  <input type="text" id="film" name="event_date" placeholder="event time::" autocomplete="off">
  <input type="text" id="film" name="event_link" placeholder="event link::" autocomplete="off">
  <input type="text" id="email" name="subscription" placeholder="If you want further updates: write your email address here" autocomplete="off">  
  <input type="submit" value="[ submit ]" onclick="displayThanks()">  
 
</form>

<iframe id="after" name="after" frameborder="0" onmousewheel="" width="100%" height="0.1" style="background: transparent; border: none;">
</iframe>

<div style="display:none" class="thanks_message">
<span id="span_thanks"> Thanks for your support. See you again! </span>
</div>

<script>
function close() {
    document.querySelector('#after').addEventListener('load', function() {
        window.close();
    });
  
}
function displayThanks() {
   var span_Text = document.getElementById("span_thanks").innerText;
   alert (span_Text);
}
</script>

<a href="/link/" target="_blank"> other interesting links (click) </a>
