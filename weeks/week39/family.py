class Person(object):
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parents = []

    def set_parent(self, parent):
        """Set who is parent to this person"""
        self.parents.append(parent)
        parent.children.append(self)

    def ancestors(self):
        """Print parents and grand...parents"""
        for parent in self.parents:
            print(parent.name)
            parent.ancestors()

    def siblings(self):
        """find parents children"""
        # keep track of the persons we have already printed
        persons = []
        # run through parents children
        for parent in self.parents:
            for sibling in parent.children:
                # only print siblings that are not oneself, or already printed
                if not ( sibling == self or sibling in persons):
                    persons.append(sibling)
                    print(sibling.name)
                    
    def relatives(self):
        """Print all relatives, advanced example of visitor function"""
        # first define a helper function, that prints relatives,
        # except those who are already visited
        def relatives_except(self, visited):
            """This is a helper function, that prints all parent/children
            combination except those who are already in the visited-list"""
            for person in self.parents + self.children:
                if not person in visited:
                    print person.name
                    visited.append(person)
                    relatives_except(person, visited)
        # call the helper function
        relatives_except(self, [])
                    

# Define some people to be able to test the above
rasmus = Person("Rasmus")
anne = Person("Anne")
rasmus.set_parent(anne)
ejlif = Person("Ejlif")
anne.set_parent(ejlif)
ruth = Person("Ruth")
anne.set_parent(ruth)
kirsten = Person("Kirsten")
kirsten.set_parent(ejlif)
kirsten.set_parent(ruth)
niels = Person("Niels")
rasmus.set_parent(niels)
bodil = Person("Bodil")
niels.set_parent(bodil)
harry = Person("Harry")
niels.set_parent(harry)
annekarin = Person("Anne Karin")
johan = Person("Johan")
johan.set_parent(niels)
johan.set_parent(annekarin)
jakob = Person("Jakob")
jakob.set_parent(niels)
jakob.set_parent(annekarin)
katrine = Person("Katrine")
katrine.set_parent(niels)
katrine.set_parent(annekarin)
karenmarie = Person("Karen Marie")
karenmarie.set_parent(niels)
karenmarie.set_parent(annekarin)

                
