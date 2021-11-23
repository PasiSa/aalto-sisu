from typing import List, Tuple
from django.conf import settings
import requests
from course.sis import StudentInfoSystem

class SisuAalto(StudentInfoSystem):

    def get_instances(self, course: str) -> List[Tuple[str, str]]:
        url=f"{settings.AALTO_SISU_URL_PREFIX}/courseunitrealisations?code={course}&USER_KEY={settings.AALTO_SISU_API_KEY}"
        response = requests.get(url)
        if response.status_code != 200:
            print(f"No SISU information found with given course code")
            return []

        json = response.json()
        instances = []
        for i in json:
            instances.append((i['id'], f"{i['startDate']} - {i['endDate']} ({i['type']})"))
        return instances

    def request_from_enhanced_api(self, id: str) -> dict:
        url=f"{settings.AALTO_SISU_URL_PREFIX}/courseunitrealisations-enhanced?id={id}&USER_KEY={settings.AALTO_SISU_API_KEY}"
        headers = {"X-ApiKey":f"{settings.AALTO_SISU_ENHANCED_API_KEY}"}
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            raise Exception("No SISU information found with given SISU ID")
        
        return response.json()[0]

    # Get course data, such as teachers from SIS system
    def get_course_data(self, id: str) -> dict:
        json = self.request_from_enhanced_api(id)
        coursedata = {}
        coursedata['starting_time'] = json['activityStartDate']
        coursedata['ending_time'] = json['activityEndDate']
        
        coursedata['teachers'] = []
        for i in json['responsibleTeachersDetails']:
            coursedata['teachers'].append(i['eduPersonPrincipalName'])

        return coursedata

    def get_participants(self, id: str) -> List[str]:
        json = self.request_from_enhanced_api(id)
        return json['participants']