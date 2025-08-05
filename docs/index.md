<h1 style="color:#4472c4; margin-bottom: 0px; padding-bottom: 0px;">{{ course_info().title }}</h1>
<h3 style="margin-top: 0px; padding-top: 0px;">{{ course_info().num }}</h3>

<span class="md-badge-purple">{{ course_info().term }}</span> 
<span class="md-badge-purple">{{ course_info().location }}</span> 
<span class="md-badge-purple">{{ course_info().days_times }}</span>

### **Course Calendar**

{{ course_calendar_table() }}
