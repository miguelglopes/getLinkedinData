from linkedin_api import linkedin
from urllib.parse import urlparse

#authenticate
linkedin = linkedin.Linkedin('#####', '####')

def getSkillsFromURLS(filename="urls.txt") -> dict:

    urls = open(filename).readlines()
    [url.strip() for url in urls]

    skillsList = {}

    for url in urls:
        parsed_uri = urlparse(url)
        if parsed_uri.netloc == "www.linkedin.com":
            try:
                job = linkedin.get_job(parsed_uri.path.replace("/jobs/view/","").replace("/",""))
                inferredSkillMatches = job["inferredSkillMatches"]
                for skill in job["inferredSkillMatches"]:
                    if skill["value"] not in skillsList:
                        skillsList[skill["value"]]=0
                    skillsList[skill["value"]] = skillsList[skill["value"]] +1
            except Exception as e:
                print(e)

    #TODO SORT!!

    return skillsList 

skillsList = {}
jobs = linkedin.search_jobs("data engineer")
for job in jobs:
    j = linkedin.get_job(urn_id=job["urn_id"])
    inferredSkillMatches = j["inferredSkillMatches"]
    for skill in j["inferredSkillMatches"]:
        if skill["value"] not in skillsList:
            skillsList[skill["value"]]=0
        skillsList[skill["value"]] = skillsList[skill["value"]] +1

print("ola")







