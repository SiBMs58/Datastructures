"""
    Array based implementatie van ADT Queue.
"""
class QueueItemType:
    def __init__(self, value):
        self.value = value

class MyQueue:
    def __init__(self, max_size):
        """
        -------------------------------------------------------
        Beschrijving:
            Creëert een lege queue
            :param max_size staat voor de maximum groote van de queue
        -------------------------------------------------------
        Preconditie:
            max_size > 0
        Postconditie:
            Een lege queue is gemaakt
        -------------------------------------------------------
        """
        if max_size > 0:
            self.items = [None] * max_size
        else:
            return None
        self.front = self.rear = 0
        self.max_size = max_size
        return

    def isEmpty(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Bepaalt of een queue leeg is.
        -------------------------------------------------------
        Preconditite:
            /
        Postconditions:
            Returns True als de queue leeg is, zo niet False.
        -------------------------------------------------------
        """
        if (self.front == self.rear):
            return True
        else:
            return False

    def enqueue(self, newItem):
        """
        -------------------------------------------------------
        Beschrijving:
            Voegt het element 'newitem' toe op de ende (de staart) van de queue.
            :param newItem staat voor het element dat aan het eind (de staart)
            moet worden toegevoegd
        -------------------------------------------------------
        Preconditie:
            Er is nog plaats op de queue
        Postconditie:
            De queue is 1 item groter en het einde
            bevat het toegevoegde item
        -------------------------------------------------------
        Return : geeft True terug als het toevoegen gelukt is
        -------------------------------------------------------
        """
        #Checkt of de stack nog niet vol zit
        if (self.max_size == self.rear):
            return False
        else:
            # Voeg op het einde het NewItem toe
            self.items[self.rear] = newItem
            self.rear += 1
            return True

    def dequeue(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Plaatst de kop van de queue (volgens het FiFO principe) in
            'queueFront' en verwijderd dan deze kop
        -------------------------------------------------------
        Preconditie:
            De queue bevat items
        Postconditie:
            De queue is 1 item kleiner en de kop
            is verwijderd
        -------------------------------------------------------
        Return : geeft True terug als het verwijderen gelukt is
        -------------------------------------------------------
        """
        # Checkt of de stack al dan niet items bevat
        if (self.front == self.rear):
            return (None, False)
        else:
            queueFront = self.items[self.front]
            self.items[self.front] = None
            self.rear -= 1
            # shift elemets to the left
            self.items = self.items[1:] + self.items[:0]
            return (queueFront, True)

    def getFront(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Plaatst de kop van een queue (volgens het FiFO principe) in
            'queueFront' en laat deze kop ongewijzigt
        -------------------------------------------------------
        Preconditie:
            de stack moet items bevatten
        Postconditie:
            De waarde van de kop van de queue word weergeven en blijft ongewijzigd
        -------------------------------------------------------
        Return : de waarde van de kop van de queue terug
        -------------------------------------------------------
        """
        # Chect of de stack niet leeg is
        if (self.front == self.rear):
            return (None, False)
        else:
            queueFront = self.items[self.front]
            return (queueFront, True)

    def save(self):
        """
        -------------------------------------------------------
        Beschrijving:
            Laat de volendige queue als een lijst zien
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            De queue word weeergegeven als een queue met back
            eerste en front als laatste element in de lijst
        -------------------------------------------------------
        Return : De queue zonder None values
        -------------------------------------------------------
        """
        # Verwijder de None values in de lijst
        tempRes = []
        for val in self.items:
            if val != None:
                tempRes.append(val)
        # Traverse front to rear to
        res = []
        for i in tempRes[::-1]:
            res.append(i)

        return res

    def load(self, lijst):
        """
        -------------------------------------------------------
        Beschrijving:
            Maakte een leeg opbject aan een vult deze met een lijst
        -------------------------------------------------------
        Preconditie:
            /
        Postconditie:
            De lijst dat moet worden ingevalden is ingeladen
        -------------------------------------------------------
        Return : De lijst dat als queue moet worden ingeladen
        -------------------------------------------------------
        """
        newLijst = lijst[::-1]
        self.items = newLijst
        self.front = 0
        self.rear = len(lijst)

# Main
if __name__ == "__main__":
    q = MyQueue(10)
    print(q.isEmpty()) # --> True
    print(q.getFront()[1]) # --> False
    print(q.dequeue()[1]) # --> False
    print(q.enqueue(2)) # --> True
    print(q.enqueue(4)) # --> True
    print(q.isEmpty()) # --> False
    print(q.dequeue()[0]) # --> 2
    q.enqueue(5)
    print(q.save())

    q.load(['a', 'b', 'c'])
    print(q.save())
    print(q.dequeue()[0])
    print(q.save())
    print(q.getFront()[0])
    print(q.save())