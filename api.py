import requests

baseURL = "https://law.lis.virginia.gov/api"


def get_titles():
    titles_url = baseURL + "/CoVTitlesGetListOfJson/"
    titles_response = requests.get(titles_url, verify=False)
    titles_data = titles_response.json()
    return titles_data


def get_chapters(title_number):
    chapters_url = baseURL + \
        f"/CoVChaptersGetListOfJson/{title_number}"
    chapters_response = requests.get(chapters_url, verify=False)
    chapters_data = chapters_response.json()
    return chapters_data


def get_sections(title_number, chapter_number):
    sections_url = baseURL + \
        f"/CoVSectionsGetListOfJson/{title_number}/{chapter_number}"
    sections_response = requests.get(sections_url, verify=False)
    sections_data = sections_response.json()
    return sections_data


def get_details(section_number):
    details_url = baseURL + \
        f"/CoVSectionsGetSectionDetailsJson/{section_number}"
    details_response = requests.get(details_url, verify=False)
    details_data = details_response.json()
    return details_data
