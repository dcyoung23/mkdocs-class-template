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

