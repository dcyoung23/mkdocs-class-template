import os
import csv
from datetime import datetime
from pathlib import Path

def define_env(env):
    @env.macro
    def course_info():
        return {
            'num': '101',
            'title': 'Example Course',
            'school': 'Example University',
            'term': 'Semester YYYY',
            'units': '3',
            'location': 'Classroom ABC',
            'days_times': 'DD and Time',
            'dates': 'dd-MM-YYYY - dd-MM-YYYY',
            'instructor': 'Instructor Name',
            'email': 'me@domain.edu',
            'office_hours': 'TBD'
        }

    # Load the course_calendar.csv file once at startup
    csv_path = os.path.join('docs', 'data', 'course_calendar.csv')
    course_calendar = []
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            course_calendar.append({
                'date': row['date'],
                'label': row['label'],
                'title': row['title'],
                'link': row['link']
            })
    @env.macro
    def course_calendar_table(offset_week=1):
        output = []
        prev_week_no = None
        first_date = datetime.strptime(course_calendar[0]['date'], "%Y-%m-%d")
        first_day = first_date.weekday()  # Monday = 0
        for row in course_calendar:
            current_date = datetime.strptime(row['date'], "%Y-%m-%d")
            days_since = (current_date - first_date).days
            week_no = offset_week + (first_day + days_since) // 7
            if week_no != prev_week_no:
                if prev_week_no is not None:
                    output.append("</tbody></table></div>")
                output.append(f"""
<div class="cal-table-wrapper">
<table class="cal-table">
    <colgroup>
        <col style="width: 20%;">
        <col style="width: 20%;">
        <col style="width: 80%;">
    </colgroup>
    <thead>
        <tr class="cal-row">
            <th colspan="3"><a href="notes/week_{week_no}">Week {week_no}</a></th>
        </tr>
    </thead>
    <tbody>
""")
                prev_week_no = week_no
            label = row.get('label', '')
            title = row.get('title', '')
            badge_class = {
                "LECT": "blue",
                "DEMO": "green",
                "LAB": "purple",
                "PART": "purple",
                "PROJ": "gray",
                "HMWK": "yellow",
                "QUIZ": "red",
                "EXAM": "red"
            }.get(label, "red" if "Due" in title else "black" if label else "")
            label_html = f'<span class="md-cal-badge md-cal-badge-{badge_class}">{label}</span>' if label else ""
            # Handle multiple links/titles
            links = row.get('link', '').split(';') if row.get('link') else []
            titles = title.split(';')
            title_links = []
            for i, t in enumerate(titles):
                if i < len(links) and links[i].strip():
                    title_links.append(f'<a href="{links[i].strip()}">{t.strip()}</a>')
                else:
                    title_links.append(t.strip())
            title_html = '<br/>'.join(title_links)
            output.append(f"""
    <tr class="cal-row">
        <td style="text-align: center">{current_date.strftime("%a, %b %d")}</td>
        <td style="text-align: center">{label_html}</td>
        <td style="padding-left: 4%">{title_html}</td>
    </tr>
""")
        output.append("</tbody></table></div>")
        return "\n".join(output)
