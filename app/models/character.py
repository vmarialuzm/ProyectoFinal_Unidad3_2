class Character :

    def __init__(self,name,status,species,origin,location,image):
        self.name = name
        self.status = status
        self.species = species
        self.origin = origin
        self.location = location
        self.image = image

    def to_json(self):
        return {
            "name": self.name,
            "status": self.status,
            "species": self.species,
            "origin": self.origin,
            "location": self.location,
            "image": self.image
        }
        