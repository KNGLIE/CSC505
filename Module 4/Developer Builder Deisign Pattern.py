class ProblemSolvingSkills:
    def __init__(self, problem_solving_skills_trait):
        self.problem_solving_skills_trait = problem_solving_skills_trait


class Passion:
    def __init__(self, passion_trait):
        self.passion_trait = passion_trait


class Teamwork:
    def __init__(self, teamwork_trait):
        self.teamwork_trait = teamwork_trait


class SoftwareDeveloper:
    def __init__(self):
        self.problem_solving_skills = None
        self.passion = None
        self.teamwork = None

    def specifications(self):
        print(
            f"A good software developer has the following traits:\n Problem Solving Skills: {self.problem_solving_skills.problem_solving_skills_trait} \n Passion: {self.passion.passion_trait} \n Teamwork: {self.teamwork.teamwork_trait} "
        )


class Builder:
    def add_problem_solving_skills(self):
        pass

    def add_passion(self):
        pass

    def add_teamwork(self):
        pass

    def build(self):
        pass


class GoodDeveloper(Builder):
    def __init__(self):
        self.software_developer = SoftwareDeveloper()

    def add_problem_solving_skills(self):
        problem_solving_skills = ProblemSolvingSkills('Critical Thinking')
        self.software_developer.problem_solving_skills = problem_solving_skills
        return self

    def add_passion(self):
        passion = Passion('Constantly honing skills')
        self.software_developer.passion = passion
        return self

    def add_teamwork(self):
        teamwork = Teamwork('Communication')
        self.software_developer.teamwork = teamwork
        return self

    def create(self):
        return self.software_developer


class Director:
    def __init__(self, good_software_developer):
        self.good_software_developer = good_software_developer

    def get_developer(self):
        return self.good_software_developer.add_problem_solving_skills().add_passion().add_teamwork().create()


def main():
    good_developer = GoodDeveloper()
    director = Director(good_developer)
    developer = director.get_developer()

    developer.specifications()


if __name__ == "__main__":
    main()
    input()
