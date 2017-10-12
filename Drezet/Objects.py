class Person(object):
    """
    A person with the following attributes:

    - id: String, unique personal id
    - name: String, person's name
    - qualifications: (List-of String), the person's qualifications
    """
    def __init__(self, id, name, qualifications):
        self.id = id
        self.name = name
        self.qualifications = qualifications

class Activity(object):
    """
    A single activity with the following attributes:

    - id = String, unique activity id
    - name = String, activity name
    - rt = Int, release time
    - deadline = Int, deadline
    - pt = Int, processing time
    - weight = Float, weight of being after deadline
    - num_persons = Int, number of required persons
    - req_qual = (List-of String), required qualifications of people assigned to activity
    - dependencies = (List-of String), precedences
    """
    def __init__(self,id,name,rt,deadline,pt,weight,num_persons,req_qual,dependencies):
        self.id = id
        self.name = name
        self.rt = rt
        self.deadline = deadline
        self.pt = pt
        self.weight = weight
        self.num_persons = num_persons
        self.req_qual = req_qual
        self.dependencies = dependencies

class Schedule(object):
    """
    A schedule consisting of assignments of people to activities with the following
    attributes:

    - id = String, unique schedule id
    - start_times = Dictionary, key is activity, value is time; ex. {a4: 3, a6:5}
    - assignments = Dictionary, key is activity, value is (List-of String); ex. {a4: [John, Claire]}
    """
    def __init__(self,id,start_times,assignments):
        self.id = id
        self.start_times = start_times
        self.assignments = assignments
