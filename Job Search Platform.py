from abc import ABC, abstractmethod

class JobPosting(ABC):
    def __init__(self, title, description, salary):
        self.title = title
        self.description = description
        self.salary = salary
        self.applicants = []

    @abstractmethod
    def display_info(self):
        pass

    def apply(self, job_seeker):
        if job_seeker not in self.applicants:
            self.applicants.append(job_seeker)
            print(f"{job_seeker.name} applied for the {self.title} position.")

class FullTimeJob(JobPosting):
    def display_info(self):
        return f"Full-Time Job: {self.title}, Salary: ${self.salary}"

class PartTimeJob(JobPosting):
    def display_info(self):
        return f"Part-Time Job: {self.title}, Salary: ${self.salary}"

class Company:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.job_postings = []

    def create_job_posting(self, job_title, job_description, salary, job_type):
        if job_type.lower() == "full-time":
            job_posting = FullTimeJob(job_title, job_description, salary)
        elif job_type.lower() == "part-time":
            job_posting = PartTimeJob(job_title, job_description, salary)
        else:
            print("Invalid job type.")
            return None

        self.job_postings.append(job_posting)
        return job_posting

    def review_applications(self, job_posting):
        print(f"Reviewing applications for the {job_posting.title} position:")
        for applicant in job_posting.applicants:
            print(f"Applicant: {applicant.name}")

class JobSeeker:
    def __init__(self, name, contact_info, resume):
        self.name = name
        self.contact_info = contact_info
        self.resume = resume

    def search_jobs(self, company, job_type=None):
        matching_jobs = []
        for job_posting in company.job_postings:
            if job_type is None or isinstance(job_posting, job_type):
                matching_jobs.append(job_posting)

        return matching_jobs

if __name__ == "__main__":
    company = Company("Mxo.co", "Mxo_co@mail.ru")

    full_time_job = company.create_job_posting("Software Engineer", "Develop software applications", 80000, "full-time")
    part_time_job = company.create_job_posting("Customer Support", "Provide assistance to customers", 40000, "part-time")

    job_seeker = JobSeeker("Serop Dembelyan", "serop156@gmail.com", "Experienced software engineer with a strong background in Python.")

    matching_jobs = job_seeker.search_jobs(company, FullTimeJob)
    for job in matching_jobs:
        job.apply(job_seeker)

    matching_jobs = job_seeker.search_jobs(company, PartTimeJob)
    for job in matching_jobs:
        job.apply(job_seeker)

    company.review_applications(full_time_job)
    company.review_applications(part_time_job)
