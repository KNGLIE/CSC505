class Evans:
    def __init__(self, requirements, design, implementation, verification, deployment):
        self.requirements = requirements
        self.design = design
        self.implementation = implementation
        self.verification = verification
        self.deployment = deployment


def menu():
    menu = input("Select a number to display the key elements of the waterfall diagram.\n1. Requirements\n2. "
                 "Design\n3. Implementation\n4. Verification\n5. Deployment\n")
    if menu == "1":
        print("Requirements:\n", waterfall.requirements)
    elif menu == "2":
        print("Design:\n", waterfall.design)
    elif menu == "3":
        print("Implementation:\n", waterfall.implementation)
    elif menu == "4":
        print("Verification:\n", waterfall.verification)
    elif menu == "5":
        print("Deployment:\n", waterfall.deployment)
    elif menu > "5":
        print("Please try again using the numbers 1-5")


waterfall = Evans("Project initiation\n Costs\n Assumptions\n Risks\n Dependencies\n Success Metrics\n Timelines",
                  "Scope of the Project\n Estimating\n Logical Design\n Scheduling\n Tracking\n Data Models\n "
                  "Physical Design", "Technical Implementation\n Code\n QA Testing",
                  "Beta Testing\n Feedback Assessment\n Flawless/Bugless test", "Delivery\n Support\n Feedback\n "
                                                                                "Updates\n New Versions")

menu()
input()
